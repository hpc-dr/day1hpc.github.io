---
title: "Understanding the AWS Batch termination process"
date: 2022-06-21T00:00:00-0700
# post thumb
images:
    - "images/post/hpcblog-121-header-v2.png"
#author
author: "Matt Vaughn"
# description
description: ""
# Taxonomies
categories: [ "AWS Batch", ]
tags: [ "Batch",  "HPC",  "Best Practices",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

In this blog post, we help you understand the AWS Batch job termination process and how you may take actions to gracefully terminate a job by capturing SIGTERM signal inside the application. It provides you with an efficient way to exit your Batch jobs. You also get to know about how job timeouts occur, and how the retry operation works with both traditional AWS Batch jobs and array jobs.

Read the full post at the [AWS HPC Blog](https://aws.amazon.com/blogs/hpc/understanding-the-aws-batch-termination-process/).
