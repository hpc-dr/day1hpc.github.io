---
title: "Data Science workflows at insitro: how redun uses the advanced service features from AWS Batch and AWS Glue"
date: 2022-03-31T00:00:00-0700
# post thumb
images:
    - "images/post/hpcblog-116-p2-fig2-831x630.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "AWS Batch",  "Life Sciences", ]
tags: [ "Batch",  "HPC",  "Life Sciences",  "Glue",  "Artificial Intelligence",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

Matt Rasmussen, VP of Software Engineering at insitro, expands on his first post on redun, insitro’s data science tool for bioinformatics, to describe how redun makes use of advanced AWS features. Specifically, Matt describes how AWS Batch’s Array Jobs is used to support workflows with large fan-out, and how AWS Glue’s DynamicFrame is used to run computationally heterogenous workflows with different back-end needs such as Spark, all in the same workflow definition.

<a href="{{ url }}" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS HPC Blog</a>