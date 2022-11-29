---
title: "Scaling a read-intensive, low-latency file system to 10M+ IOPs"
date: 2021-11-04T00:00:00-0700
# post thumb
images:
    - "images/post/scaling-read-fs-f1.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "Financial Services", ]
tags: [ "Financial Services",  "Best Practices",  "Storage",  "HPC",  "EC2",  "Technical How-to",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

Many shared file systems are used in supporting read-intensive applications, like financial backtesting. These applications typically exploit copies of datasets whose authoritative copy resides somewhere else. For small datasets, in-memory databases and caching techniques can yield impressive results. However, low latency flash-based scalable shared file systems can provide both massive IOPs and bandwidth. They’re also easy to adopt because of their use of a file-level abstraction. In this post, I’ll share how to easily create and scale a shared, distributed POSIX compatible file system that performs at local NVMe speeds for files opened read-only.

<a href="https://aws.amazon.com/blogs/hpc/scaling-a-read-intensive-low-latency-file-system-to-10m-iops/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS HPC Blog</a>