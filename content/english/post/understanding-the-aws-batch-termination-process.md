---
title: "Understanding the AWS Batch termination process"
date: 2022-06-21T00:00:00-0700
# post thumb
images:
    - "images/post/hpcblog-121-header-v2.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "AWS Batch", ]
tags: [ "HPC",  "Best Practices",  "Batch",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

In this blog post, we help you understand the AWS Batch job termination process and how you may take actions to gracefully terminate a job by capturing SIGTERM signal inside the application. It provides you with an efficient way to exit your Batch jobs. You also get to know about how job timeouts occur, and how the retry operation works with both traditional AWS Batch jobs and array jobs.

<a href="https://aws.amazon.com/blogs/hpc/understanding-the-aws-batch-termination-process/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS Blog Channel</a>