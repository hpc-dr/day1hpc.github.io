#!/usr/bin/env python3

import argparse
import csv
import hashlib
import os
import pytz
import re
import sys

from collections import OrderedDict
from datetime import datetime, timedelta
from icalendar import Calendar, Event, vText
from jinja2 import Environment, FileSystemLoader
from random import choice, randrange
from typing import Dict, List

SELF = os.path.realpath(__file__)
PARENT_DIR = os.path.dirname(__file__)
POSTS_DIR = os.path.join(os.path.dirname(PARENT_DIR), "content", "english", "sc22")
IMAGE_ASSETS = os.path.join(os.path.dirname(PARENT_DIR), "assets")
IMAGE_ASSETS_SUBDIR = os.path.join("images", "post")
FILENAME = "index.md"
TIME_DELTA = 120
MAX_LENGTH = 256
URL = 'https://day1hpc.com/sc22'

def post_time(row) -> datetime:
    start_time = row['Date'] + '-2022' + ' ' + row['Start']
    end_time = row['Date'] + '-2022' + ' ' + row['End']
    start_dt = datetime.strptime(start_time, '%d-%b-%Y %H:%M')
    timezone = pytz.timezone("America/Chicago")
    start_dt = timezone.localize(start_dt)
    return start_dt

def short_hash(value: str, length=12) -> str:
    return hashlib.md5(value.encode()).hexdigest()[:length]

def to_station_name(station) -> str:
    if station == 'T':
        return 'Booth Theater'
    else:
        return 'Demo Station ' + str(station)

def speaker(raw_data) -> str:
    pattern = r'<\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b>'
    raw_data = re.sub(pattern, '', raw_data)
    raw_data = raw_data.strip()
    if 'Team' in raw_data:
        raw_data = 'the ' + raw_data
    return raw_data

def extract_topics(row) -> List[str]:
    topics_raw = row.get("Topic", '')
    topics = topics_raw.split(",")
    topics = [t.strip() for t in topics]
    return topics

def topics_to_tags(tags) -> List[str]:
    return ['#' + t.replace(' ', '') for t in tags]

def row_to_event(row) -> Dict:
    event = {
                'title': row['Title'],
                'abstract': row['Abstract'],
                'day_of_week': row['Dow'][:3],
                'speaker': speaker(row.get('Speaker', '')),
                'speaker_affiliation': row.get('SpeakerAffil', ''),
                'start': row['Start'],
                'end': row['End'],
                'range': row['Start'] + '-' + row['End'],
                'station_name': to_station_name(row['Station']),
                'post_time': post_time(row),
                'tags': topics_to_tags(extract_topics(row))
            }    
    return event

def build_post(event, templates) -> str:
    for t in templates:
        resp = t.render(**event)
        if len(resp) <= MAX_LENGTH:
            return resp

def randomize_post_time(pt):
    td_skewed = 5 * (randrange(6, 48))
    td = timedelta(minutes=td_skewed)
    post_time = pt - td
    return post_time

def schedule_posts(posts, times=None):
    if times == None:
        times = []
    for p in posts:
        p['post_time'] = randomize_post_time(p['post_time'])
    

def main(values):

    environment = Environment(
        loader=FileSystemLoader(os.path.join(PARENT_DIR, "./templates/"))
    )
    templates = []
    templates.append(environment.get_template("post1.j2"))
    templates.append(environment.get_template("post2.j2"))
    templates.append(environment.get_template("post3.j2"))

    posts = []

    with open("scheduled_posts.csv", "w") as posts_file:
        post_writer = csv.writer(posts_file)
        with open(values.csv.name, encoding='utf-8-sig') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",")
            for row in csv_reader:
                event = row_to_event(row)
                post = build_post(event, templates)
                posts.append(post)

    # schedule posts
    posts = schedule_posts(posts)

    for post in posts:
        post_timestr = event['post_time'].strftime("%-m/%-d/%Y %H:%M:%S")
        post_url = URL
        post_writer.writerow([post_timestr, post, post_url])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", type=argparse.FileType("r"), default=sys.stdin)
    args = parser.parse_args()
    main(args)

