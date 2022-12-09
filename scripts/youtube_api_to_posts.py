import argparse
import csv
import googleapiclient.discovery
import json
import os
import pytz
import re
import requests
import sys

from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from typing import Any, Dict, List, Tuple

SELF = os.path.realpath(__file__)
PARENT_DIR = os.path.dirname(__file__)
POSTS_DIR = os.path.join(os.path.dirname(PARENT_DIR), "content", "english", "post")
IMAGE_ASSETS = os.path.join(os.path.dirname(PARENT_DIR), "assets")
IMAGE_ASSETS_SUBDIR = os.path.join("images", "post")

def slugify(s) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s)
    s = re.sub(r"^-+|-+$", "", s)
    return s

def _chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def date_published_to_iso(date_published: str) -> str:
    # extract from string date 2022-10-11T16:53:39Z
    dt = datetime.strptime(date_published, "%Y-%m-%dT%H:%M:%SZ")
    # set time zone
    timezone = pytz.timezone("UTC")
    dt2 = timezone.localize(dt)
    # template 2020-03-15T15:40:24+06:00
    dt3 = dt2.strftime("%Y-%m-%dT%H:%M:%S%z")
    return dt3

def transform_tags(tags: List) -> List[str]:
    
    # Strip these out of tags
    PREFIXES = ["Amazon", "AWS"]

    # Tranform K => V
    TRANSFORMS = {
        "Energy (Oil & Gas)": "Energy",
        "High Performance Computing": "HPC",
        "Launch": "Product Launch",
        "Media Entertainment": "Media",
        "Windows on AWS": "Windows",
    }

    # Omit these tags entirely
    FILTERED = [
        "Advanced (300)",
        "Announcements",
        "Cloud Digital Interface",
        "Customer Solutions",
        "Partner Network",
        "Thought Leadership",
    ]

    # Strip out prefixes like Amazon and AWS from the categories. We
    # use the in the categories but should use the short forms for tags.
    fixed_tags = []
    for tag in tags:
        for prefix in PREFIXES:
            patt = re.compile("^" + prefix + " ")
            tag = patt.sub("", tag)
        fixed_tags.append(tag)

    # Some tags should be replaced with others, defined
    # in TRANSFORMS
    mapped_tags = []
    for tag in fixed_tags:
        if tag in TRANSFORMS:
            tag = TRANSFORMS[tag]
        mapped_tags.append(tag)

    # Some tags should simply be ignored
    filtered_tags = []
    for tag in mapped_tags:
        if tag not in FILTERED:
            filtered_tags.append(tag)
    return filtered_tags

def extract_tags(keywords:List[str]) -> List[str]:
    return keywords

def infer_tags(text: str, title:str=None) -> List[str]:
    return []

def extract_categories(tags:List[str]) -> List[str]:

    # Use a mapping of tags -> blog categories to 
    # compile a list of categories for the provided tag set
    
    categories = []

    # Load tag:category map
    TRANSFORMS = {}
    with open(os.path.join(PARENT_DIR, "youtube-tags-categories.csv"), encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file, dialect='excel', delimiter=",")
        for row in csv_reader:
            print(row)
            if row["Category"] != "":
                TRANSFORMS[row["Tag"]] = row["Category"]

    for tag in tags:
        if TRANSFORMS.get(tag, None) is not None:
            categories.append(TRANSFORMS.get(tag))

    categories = sorted(list(set(categories)))
    return categories

def download_image(url: str, file_name: str, headers: dict = None, force=False):

    # Downloads the flavor image for a blgo post
    #
    if headers is None:
        headers = {}
    # Save the image
    destination_path = os.path.join(IMAGE_ASSETS, file_name)
    if not os.path.exists(destination_path) or force is True:   
        # Send GET request
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(os.path.join(IMAGE_ASSETS, file_name), "wb") as f:
                f.write(response.content)
        else:
            print(response.status_code)

def get_videos(video_stubs:List, youtube:googleapiclient) -> List[ Dict ]:
    # Get extended video objects for a list of video object stubs
    videos = []
    video_ids = []
    for stub in video_stubs:
        video_ids.append(stub.get("contentDetails").get("videoId"))
    for group_ids in _chunker(video_ids, 50):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=",".join(group_ids)
        )
        response = request.execute()
        videos.extend(response.get('items'))
    return videos

def get_playlist_videos(playlist_id:str, youtube:googleapiclient) -> List[str]:
    # Return all Youtube video objects in a playlist
    videos = []
    data = {
        "part": "snippet,contentDetails",
        "playlistId": playlist_id,
        "maxResults": 1000,
        "pageToken": None
    }

    # Iterate through all youtube videos in the playlist
    first_request = True
    next_page_token = None
    while first_request is True or next_page_token is not None:
        first_request = False
        request = youtube.playlistItems().list(**data)
        response = request.execute()
        videos.extend(response['items'])
        next_page_token = response.get('nextPageToken', None)
        data["pageToken"] = next_page_token

    return videos


def video_to_blog(video):
    # Build up blog, a dictionary used to populate Jinja templates
    # print(json.dumps(video, indent=4))
    # raise SystemError()
    blog = {
        "title": video["snippet"]["title"],
        "excerpt": video["snippet"]["description"],
        "thumbnail": video["snippet"]["thumbnails"]["medium"]["url"],
        # "thumbnail_filename": slugify(row["image"]) + ".png",
        "id": video["id"],
        "date_published": date_published_to_iso(video["snippet"]["publishedAt"]),
        "filename": slugify(video["snippet"]["title"]) + ".md",
    }

    # Replace quotes in title and excerpt
    blog["title"] = blog["title"].replace('"', "'")
    blog["excerpt"] = blog["excerpt"].replace('"', "'")
    
    # TODO Compute thumbnail filename
    blog["thumbnail_filename"] = os.path.join(
        IMAGE_ASSETS_SUBDIR, video["id"] + ".png"
    )
    tags = extract_tags(video["snippet"].get("tags", []))
    tags.extend(infer_tags(blog['excerpt'], blog['title']))
    tags = list(set(tags))
    blog['tags'] = tags
    # Add "techshorts" to tags
    blog["tags"].append("techshorts")

    # categories
    categories = extract_categories(tags)
    blog['categories'] = categories
    return blog

def main(values):
    
    force_dl = values.force

    environment = Environment(
        loader=FileSystemLoader(os.path.join(PARENT_DIR, "./templates/"))
    )
    template = environment.get_template("techshort.md.j2")

    youtube = googleapiclient.discovery.build(
        "youtube",  "v3", developerKey = values.key)
    
    videos = get_playlist_videos(values.uploads, youtube=youtube)
    videos_data = get_videos(video_stubs=videos, youtube=youtube)

    filenames = []
    categories = []
    tags = []

    for vid in videos_data:
        data = video_to_blog(vid)

        filenames.append(data["filename"])
        categories.extend(data["categories"])
        tags.extend(data["tags"])

        content = template.render(**data)
        filename = os.path.join(POSTS_DIR, data["filename"])
        if not os.path.exists(filename) or force_dl:
            with open(filename, mode="w", encoding="utf-8") as post:
                post.write(content)
                # Download the illustrative image associated with each post
                if data["thumbnail"] != "":
                    download_image(data["thumbnail"], data["thumbnail_filename"], force=force_dl)

    print("Filenames:")
    print("\n".join(filenames))
    print("Categories:")
    print("\n".join(sorted(list(set(categories)))))
    print("Tags:")
    print("\n".join(sorted(list(set(tags)))))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel", type=str, required=False, default="UChSIn5kcWQvJxW17KIjdLVw", help="Channel ID (optional)")
    parser.add_argument("--uploads", type=str, required=False, default="UUhSIn5kcWQvJxW17KIjdLVw", help="Uploads Playlist ID (optional)")
    # Reaad default from os.env 
    parser.add_argument("--key", type=str, required=False, default=os.environ.get("YOUTUBE_DATA_API_KEY", "oxDEADBEEF"), help="Youtube Data V3 API Key [YOUTUBE_DATA_API_KEY]")
    parser.add_argument("--force", action="store_true", help="Force re-download")
    args = parser.parse_args()
    main(args)
