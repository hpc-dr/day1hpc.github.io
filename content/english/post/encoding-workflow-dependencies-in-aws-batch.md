---
title: "Encoding workflow dependencies in AWS Batch"
date: 2022-05-11T00:00:00-0700
# post thumb
images:
    - "images/post/hpcblog-31-header-1260x630.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "AWS Batch", ]
tags: [ "Batch",  "Best Practices",  "HPC",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

This post covers the different ways you can encode a dependency between basic and array jobs in AWS Batch. We also cover why you may want to encode dependencies outside of Batch altogether using a workflow system like AWS Step Functions or Apache Airflow.

<a href="{{ url }}" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS HPC Blog</a>