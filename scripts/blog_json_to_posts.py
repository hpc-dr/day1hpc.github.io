#!/usr/bin/env python3

import argparse
import json
import os
import pytz
import re
import requests
import sys

from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from typing import Dict, List
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


def infer_tags(text: str, title:str=None) -> List[str]:
    # Infers tags from text with a regex

    if title is not None:
        text = title + ' ' + text

    PATTERNS = {
        "AI/ML": [r"AI/ML", r"machine learning", r"neural network", r'\bML\b'],
        "Arm": [r'\bArm\b', r'Graviton'],
        "NICE DCV": [r'NICE DCV', r'\bDCV'],
        "EFA": [r"EFA", r"Elastic Fabric Adapter"],
        "ParallelCluster": [r"ParallelCluster"],
        "Batch": [r"Batch"],
        "Slurm": [r"Slurm"],
        "HPC": [r"HPC", r"High Performance Computing"],
        "Climate/Environment/Weather": [r"Climate", r"Weather", r"Meteoro"],
        "CAE/CFD": [r"engineering", r'\bCAE\b', r"CFD", r"fluid dynamics"],
        "Life Sciences": [
            r"Genomics",
            r"Sequencing",
            r"NGS",
            r"Cryo-EM",
            r"CryoEM",
            r"Parabricks",
            r"GROMACS",
            r"small molecule",
            r"protein",
            r"DNA",
            r"bioinformatics",
            r"pharmaceutical",
            r"genetic",
            r"medicine",
            r"medical",
            r"biotech",
            r"molecular dynamics",
        ],
        "Financial Services": [r"financial", r"banking"],
        "Quantum technologies": [r'quantum'],
        "Simulation": [r'simulation'],
        "Media": [r'media', r'animation', r'film', r'entertainment'],
        "Modeling": [r'modeling', r'model']
    }
    tags = []
    for t, pats in PATTERNS.items():
        for p in pats:
            rx = re.compile(p)
            if rx.search(text, re.IGNORECASE):
                tags.append(t)
                continue
    return tags


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

def datestr_to_datetime(datestr:str) -> datetime:
    # extract from string date
    formats = ["%d %b %y", "%d %b %Y", "%d-%b-%y"]
    for f in formats:
        try:
            dt = datetime.strptime(datestr, f)
            return dt
        except Exception:
            pass
    raise ValueError("{0} was not in a recognized format".format(datestr))

def date_published_to_iso(date_published: str) -> str:
    # extract from string date
    dt = datestr_to_datetime(date_published)
    # try:
    #     dt = datetime.strptime(date_published, "%d %b %y")
    # except ValueError:
    #     dt = datetime.strptime(date_published, "%d-%b-%y")
    # set time zone
    timezone = pytz.timezone("America/Los_Angeles")
    dt2 = timezone.localize(dt)
    # template 2020-03-15T15:40:24+06:00
    dt3 = dt2.strftime("%Y-%m-%dT%H:%M:%S%z")
    return dt3


def extract_categories(tags: List[str]) -> List[str]:

    # Given a list of tags, some of which are inferred, 
    # classify the blog into a category

    # Tranform Tag => Category
    TRANSFORMS = {
        "Batch": "AWS Batch",
        "ParallelCluster": "AWS ParallelCluster",
        "EFA": "Elastic Fabric Adapter",
        "NICE DCV": "NICE DCV",
        "AI/ML": "AI/ML",
        "CAE/CFD": "CAE/CFD",
        "Climate/Environment/Weather": "Climate/Environment/Weather",
        "Financial Services": "Financial Services",
        "Life Sciences": "Life Sciences"
    }

    # Match and sometimes transform tags to categories
    mapped_tags = []
    for tag in tags:
        if tag in TRANSFORMS:
            tag = TRANSFORMS[tag]
            mapped_tags.append(tag)

    return mapped_tags

def extract_tags(categories_lst: str, transform=True) -> List[str]:
    tags = categories_lst
    if transform:
        tags = transform_tags(tags)
    return tags

def image_path(row_image:str) -> str:
    if row_image is not None and row_image != "":
        return slugify(row_image) + ".png"
    else:
        return ""

def row_to_blog(row):
    # Build up blog, a dictionary used to populate Jinja templates
    blog = {
        "title": row["title"],
        "excerpt": row["excerpt"],
        "thumbnail": row["image"],
        "thumbnail_filename": image_path(row["image"]),
        "url": row["url"],
        "datetime_published": datestr_to_datetime(row["datePublished"]),
        "date_published": date_published_to_iso(row["datePublished"]),
        "filename": slugify(row["title"]) + ".md",
    }
    # Compute Image path (or default)
    if row["image"] != "" and row["image"] is not None:
        parts = urlparse(blog["thumbnail"])
        blog["thumbnail_filename"] = os.path.join(
            IMAGE_ASSETS_SUBDIR, os.path.basename(parts.path)
        )
    else:
        # TODO - replace with something sensible
        blog["thumbnail_filename"] = os.path.join(
            IMAGE_ASSETS_SUBDIR, "dalle-hpc-01.png"
        )

    # tags
    tags = extract_tags(row["categories"])
    tags.extend(infer_tags(blog['excerpt'], blog['title']))
    tags = list(set(tags))
    blog['tags'] = tags
    # Add "blog" to tags
    blog["tags"].append("hpcblog")

    # categories
    categories = extract_categories(tags)
    blog['categories'] = categories

    return blog


def intersection(lst1:List, lst2:List) -> bool: 
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return len(lst3) > 0

def validate(data:Dict, source:str):

    aws_includes = ["HPC", "Compute", "Graviton", "Elastic File System (EFS)", "File Cache", "Amazon FSx for Lustre", "Amazon FSx for OpenZFS"]
    storage_includes = ["Elastic File System (EFS)", "File Cache", "FSx for Lustre", "FSx for OpenZFS"]

    cats = data["tags"]

    if source == "hpc" or source == "quantum":
        return True

    if source == "storage":

        if "re:Invent" in data["title"]:
            return False
        if not intersection(storage_includes, data["tags"]):
            return False
        if data["datetime_published"] < datetime(2021, 11, 30):
            return False

    # Filters for omitting AWS News Blog entries
    if source == "aws":
        if "Week in Review" in data["title"]:
            return False
        if not intersection(aws_includes, data["tags"]):
            return False
        if data["datetime_published"] < datetime(2021, 11, 30):
            return False

    return True

def main(values):
    force_dl = values.force
    environment = Environment(
        loader=FileSystemLoader(os.path.join(PARENT_DIR, "./templates/"))
    )
    template = environment.get_template("blog.md.j2")
    with open(values.json, 'rb') as jf:
        data = json.load(jf)
        for row in data:
            data = row_to_blog(row)
            if validate(data, values.source):
                content = template.render(**data)
                filename = os.path.join(POSTS_DIR, data["filename"])
                print("Post filename:", filename)
                if not os.path.exists(filename) or force_dl is True:
                    with open(filename, mode="w", encoding="utf-8") as post:
                        post.write(content)
                    # Download the illustrative image associated with each post
                    if data["thumbnail"] != "" and data["thumbnail"] is not None:
                        download_image(data["thumbnail"], data["thumbnail_filename"], force=force_dl)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("json", type=str, help="Blog export file (JSON).")
    parser.add_argument("--source", default="hpc", choices=["hpc", "aws", "quantum", "storage"], help="Data source")
    parser.add_argument("--force", action="store_true", help="Force re-download")
    args = parser.parse_args()
    main(args)
