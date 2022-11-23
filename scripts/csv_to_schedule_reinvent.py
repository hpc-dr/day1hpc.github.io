#!/usr/bin/env python3

import argparse
import csv
import hashlib
import os
import pytz
import re
import sys

from collections import OrderedDict
from datetime import datetime
from icalendar import Calendar, Event, vText
from jinja2 import Environment, FileSystemLoader
from typing import Dict, List

SELF = os.path.realpath(__file__)
PARENT_DIR = os.path.dirname(__file__)
POSTS_DIR = os.path.join(os.path.dirname(PARENT_DIR), "content", "english", "reinvent")
IMAGE_ASSETS = os.path.join(os.path.dirname(PARENT_DIR), "assets")
IMAGE_ASSETS_SUBDIR = os.path.join("images", "post")
FILENAME = "index.md"

def short_hash(value: str, length=12) -> str:
    return hashlib.md5(value.encode()).hexdigest()[:length]

def to_station_name(station:str) -> str:
    return station

def to_ical(row:Dict) -> object:

    start_time = row['Date'] + '/2022' + ' ' + row['Start']
    end_time = row['Date'] + '/2022' + ' ' + row['End']
    start_dt = datetime.strptime(start_time, '%m/%d/%Y %H:%M')
    end_dt = datetime.strptime(end_time, '%m/%d/%Y %H:%M')
    timezone = pytz.timezone("US/Pacific")
    start_dt = timezone.localize(start_dt)
    end_dt = timezone.localize(end_dt)
    cal = Calendar()
    cal.add('prodid', '-//AWS re:Invent Schedule//aws.dev//')
    cal.add('version', '2.0')
    event = Event()
    event.add('summary', row['Session_ID'] + ': ' + row['Title'])
    event.add('description', row['Abstract'])
    event.add('dtstart', start_dt)
    event.add('dtend', end_dt)
    event.add('url', 'https://day1hpc.com/reinvent/')
    event['location'] = to_station_name(row['Location']) + ', Las Vegas, NV, USA'
    cal.add_component(event)
    return cal

def ical_filename(event:Dict) -> str:
    filename = short_hash('|'.join([event['title'], event['station_name'], event['day_of_week'], event['start'], event['end']])) + '.ics'
    return filename

def write_ical(event:Dict) -> None:
    filepath = os.path.join(POSTS_DIR, event['ical_filename'])
    with open(filepath, 'wb') as f:
        f.write(event['ical'].to_ical())
    return filepath

def extract_topics(row:Dict) -> List[str]:
    topics_raw = row.get("Tags", '')
    topics = topics_raw.split(",")
    topics = [t.strip() for t in topics]
    return topics

def cleanup_speaker(raw_data:str) -> str:
    # Strip out emails
    pattern = r'<\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b>'
    raw_data = re.sub(pattern, '', raw_data)
    raw_data = raw_data.strip()
    return raw_data

def get_speakers(row:Dict) -> Dict:
    speakers = {}
    for a in ['Speaker_1', 'Speaker_2']:
        ak = a + '_Aff'
        aff = row.get(ak, None)
        if aff is not None and aff != '':
            if aff not in speakers:
                speakers[aff] = []
            spk = row.get(a).split(';')
            spk = [s.strip() for s in spk]
            spk = [cleanup_speaker(s) for s in spk]
            spk = sorted(spk)
            speakers[aff].extend(spk)
    return speakers

def build_speakers_text(speakers:Dict) -> str:
    response = ''
    spkaffs = []
    for aff, spks in speakers.items():
        spaf = ''
        a = '(' + aff + ')'
        if len(spks) == 1:
            spaf = spks[0] + ' ' + a
        elif len(spks) == 2:
            spaf = spks[0] + ' and ' + spks[1] + ' ' + a
        else:
            spaf = ', '.join(spks) + ' ' + a
        spkaffs.append(spaf)
    if len(spkaffs) == 1:
        response = spkaffs[0]
    else:
        response = ' | '.join(spkaffs)
    return response

def row_to_event(row:Dict) -> Dict:
    event = {
                'title': row['Title'],
                'session_id': row['Session_ID'],
                'session_type': row['Session_Type'],
                'session_duration': row['Session_Length'],
                'session_level': row['Session_Level'],
                'abstract': row['Abstract'],
                'day_of_week': row['Dow'],
                'speaker': '',
                'speaker_affiliation': '',
                'speakers': get_speakers(row),
                'start': row['Start'],
                'end': row['End'],
                'range': row['Start'] + '-' + row['End'],
                'station_name': to_station_name(row['Location']),
                'ical': to_ical(row),
                'topics': extract_topics(row)
            }
    
    event['ical'] = to_ical(row)
    event['ical_filename'] = ical_filename(event)

    return event

def main(values:Dict):
    environment = Environment(
        loader=FileSystemLoader(os.path.join(PARENT_DIR, "./templates/"))
    )
    template = environment.get_template("reinvent_index.md.j2")

    data = OrderedDict()
    topics_master_list = []
    navs = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    with open(values.csv.name, encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=",")
        for row in csv_reader:
            event = row_to_event(row)
            write_ical(event)
            # Put into data object
            dow = event['day_of_week']
            station_name = event['station_name']
            if dow not in data:
                data[dow] = OrderedDict()
            if station_name not in data[dow]:
                data[dow][station_name] = []
            
            e = {
                "title": event["title"],
                "abstract": event["abstract"],
                "session_type": event["session_type"],
                "session_id": event["session_id"],
                "speakers": build_speakers_text(event["speakers"]),
                "speaker": "",
                "speaker_affiliation": "",
                "day_of_week": event["day_of_week"],
                "range": event["range"],
                "location": event["station_name"],
                "id": re.sub('.ics', '', event['ical_filename']),
                "ical_filename": event['ical_filename'],
                "topics": event['topics']
            }

            data[dow][station_name].append(e)
            topics_master_list.extend(e["topics"])

    topics_master_list = sorted(list(set(topics_master_list)))
    navs.extend(topics_master_list)

    # Render index.md
    content = template.render(data=data, topics=topics_master_list, anchors=navs)
    indexfile = os.path.join(POSTS_DIR, FILENAME)
    with open(indexfile, mode="w", encoding="utf-8") as post:
            post.write(content)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", type=argparse.FileType("r"), default=sys.stdin)
    args = parser.parse_args()
    main(args)
