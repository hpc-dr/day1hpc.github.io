---
title: "Persistent storage for Kubernetes "
date: 2022-11-22T00:00:00-0800
# post thumb
images:
    - "images/post/Amazon_EFS_video_thumbnail.jpg"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: []
tags: [ "Elastic Kubernetes Service",  "Elastic File System (EFS)",  "Technical How-to",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

Stateful applications rely on data being persisted and retrieved to run properly. When running stateful applications using Kubernetes, state needs to be persisted regardless of container, pod, or node crashes or terminations. This requires persistent storage, that is, storage that lives beyond the lifetime of the container, pod, or node. In this blog, we cover […]

<a href="https://aws.amazon.com/blogs/storage/persistent-storage-for-kubernetes/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS Blog Channel</a>