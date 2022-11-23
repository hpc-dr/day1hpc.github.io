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

def to_station_name(station) -> str:
    return station

def to_ical(row) -> object:

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
    event.add('summary', row['Session_ID'] + ':' + row['Title'])
    event.add('description', row['Abstract'])
    event.add('dtstart', start_dt)
    event.add('dtend', end_dt)
    event['location'] = to_station_name(row['Location']) + ', Las Vegas, NV, USA'
    cal.add_component(event)
    return cal

def ical_filename(event) -> str:
    filename = short_hash('|'.join([event['title'], event['station_name'], event['day_of_week'], event['start'], event['end']])) + '.ics'
    return filename

def write_ical(event) -> None:
    filepath = os.path.join(POSTS_DIR, event['ical_filename'])
    with open(filepath, 'wb') as f:
        f.write(event['ical'].to_ical())
    return filepath

def speaker(raw_data) -> str:
    # Strip out emails
    pattern = r'<\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b>'
    raw_data = re.sub(pattern, '', raw_data)
    raw_data = raw_data.strip()
    return raw_data

def extract_topics(row) -> List[str]:
    topics_raw = row.get("Topic", '')
    topics = topics_raw.split(",")
    topics = [t.strip() for t in topics]
    return topics

def row_to_event(row) -> Dict:
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
                # 'speaker': speaker(row.get('Speaker_1', '')),
                # 'speaker_affiliation': row.get('Speaker_1_Affil', ''),
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

# {"Tuesday": {"T": [
#     {
#     "title": "Title",
#      "abstract": "Abstract",
#      "start": "Datetime",
#      "end": "Datetime",
#      "presenter": "Presenter",
#      "affiliation": "Affiliation",
#      "ical": "MD5HEX.ics",
#      "topics": ["meep", "merp", "moop"]
#     }
# ]}}

def main(values):
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
                "speaker": event["speaker"],
                "speaker_affiliation": event["speaker_affiliation"],
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
    
    raise SystemExit()

    # Render demo and theater schedule file for 3P

    fnames = ['day_of_week', 'range', 'location', 'speaker', 'speaker_affiliation', 'title', 'abstract']

    theater = open("./theater_schedule.csv", "w", encoding='utf-8-sig')
    demos = open("./demo_schedule.csv", "w", encoding='utf-8-sig')
    
    twriter = csv.DictWriter(theater, fieldnames=fnames)
    twriter.writeheader()

    dwriter = csv.DictWriter(demos, fieldnames=fnames)
    dwriter.writeheader()

    for dow, locs in data.items():
        for loc, events in locs.items():
            if "Theater" in loc:
                for event in events:
                    event.pop('ical_filename')
                    event.pop('id')
                    twriter.writerow(event)
            else:
                for event in events:
                    event.pop('ical_filename')
                    event.pop('id')
                    dwriter.writerow(event)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", type=argparse.FileType("r"), default=sys.stdin)
    args = parser.parse_args()
    main(args)
