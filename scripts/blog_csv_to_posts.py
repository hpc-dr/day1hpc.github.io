#!/usr/bin/env python3

import argparse
import csv
import os
from unicodedata import category
import pytz
import re
import requests
import sys

from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from typing import List
from urllib.parse import urlparse

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


def download_image(url:str, file_name:str, headers:dict=None):
    return True

    if headers is None:
        headers = {}
    # Send GET request
    response = requests.get(url, headers=headers)
    # Save the image
    if response.status_code == 200:
        with open(os.path.join(IMAGE_ASSETS, file_name), "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)

def transform_categories(categories: List) -> List[str]:

    alloweds = []

    # Implement allow list
    CATEGORIES_ALLOW = [
        "Artificial Intelligence",
        "AWS Batch",
        "AWS ParallelCluster",
        "EFA",
        "Amazon FSx for Lustre",
        "Life Sciences",
        "NICE DCV",
        "Financial Services",
    ]
    for c in categories:
        if c in CATEGORIES_ALLOW:
            alloweds.append(c)

    # if 'Artificial Intelligence' in alloweds:
    #     raise SystemError(alloweds)

    # Strip these out of categories
    PREFIXES = []

    # Tranform K => V
    TRANSFORMS = {
        "Artificial Intelligence": "AI/ML",
        "EFA": "Amazon EFA",
    }

    # Some categories should be replaced with others, defined
    # in TRANSFORMS
    transformed = []
    for c in alloweds:
        if c in TRANSFORMS:
            tag = TRANSFORMS[c]
        else:
            tag = c
        transformed.append(tag)

    return transformed

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
        "Advanced 300",
        "Amplify",
        "Announcements",
        "Cloud Digital Interface",
        "Customer Solutions",
        "Launch",
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

def date_published_to_iso(date_published: str) -> str:
    # extract from string date
    dt = datetime.strptime(date_published, "%d %b %Y")
    # set time zone
    timezone = pytz.timezone("America/Los_Angeles")
    dt2 = timezone.localize(dt)
    # template 2020-03-15T15:40:24+06:00
    dt3 = dt2.strftime("%Y-%m-%dT%H:%M:%S%z")
    return dt3


def extract_categories(categories_str: str) -> List[str]:
    CATEGORIES_ALLOW = [
        "Artificial Intelligence",
        "AWS Batch",
        "AWS ParallelCluster",
        "EFA",
        "Amazon FSx for Lustre",
        "Life Sciences",
        "NICE DCV",
        "Financial Services",
    ]
    
    tags = extract_tags(categories_str, transform=False)
    categories = transform_categories(tags)

    return categories


def extract_tags(categories_str: str, transform=True) -> List[str]:
    tags = categories_str.split(" | ")
    if transform:
        tags = transform_tags(tags)
    return tags


def row_to_blog(row):
    # Build up blog, a dictionary used to populate Jinja templates
    blog = {
        "title": row["title"],
        "excerpt": row["excerpt"],
        "thumbnail": row["image"],
        "thumbnail_filename": slugify(row["image"]) + ".png",
        "url": row["URL"],
        "categories": extract_categories(row["categories"]),
        "tags": extract_tags(row["categories"]),
        "date_published": date_published_to_iso(row["datePublished"]),
        "filename": slugify(row["title"]) + ".md",
    }
    # Compute Image path (or default)
    if row["image"] != "":
        parts = urlparse(blog["thumbnail"])
        blog["thumbnail_filename"] = os.path.join(IMAGE_ASSETS_SUBDIR, os.path.basename(parts.path))
    else:
        # TODO - replace with something sensible
        blog["thumbnail_filename"] = os.path.join(IMAGE_ASSETS_SUBDIR, 'dalle-hpc-01.png')
    # Add "blog" to tags
    blog["tags"].append("hpcblog")
    return blog


def main(values):
    environment = Environment(
        loader=FileSystemLoader(os.path.join(PARENT_DIR, "./templates/"))
    )
    template = environment.get_template("blog.md.j2")
    with open(values.csv.name) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=",")
        for row in csv_reader:
            data = row_to_blog(row)
            # Render and write blog post stubs
            content = template.render(**data)
            filename = os.path.join(POSTS_DIR, data["filename"])
            with open(filename, mode="w", encoding="utf-8") as post:
                post.write(content)
                print(data["filename"])
            # Download the illustrative image associated with each post
            if data["thumbnail"] != "":
                download_image(
                    data["thumbnail"], data["thumbnail_filename"]
                )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", type=argparse.FileType("r"), default=sys.stdin)
    args = parser.parse_args()
    main(args)
