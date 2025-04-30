---
title: "How to use Capacity Blocks for ML with AWS Batch"
date: 2025-04-29T00:00:00-0700
# post thumb
images:
    - "images/post/HPCBlog-364-header-1120x630.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "AWS Batch",  "AI/ML", ]
tags: [ "HPC",  "Batch",  "AI/ML",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

Capacity Blocks for ML (CBML) are a powerful feature that allows you to reserve highly sought-after GPU based EC2 instances for a future date to support your short-duration machine learning (ML) workloads. Since the reservations are “for a future date” you must have a mechanism to launch the instances that you have paid for and place jobs onto them at that specific time. This is where AWS Batch comes in. With an always-on queue ready to accept jobs, and the ability to scale your capacity block reservation at the correct time, AWS Batch provides you with everything you need to maximize your CBML reservations.

<a href="https://aws.amazon.com/blogs/hpc/how-to-use-capacity-blocks-for-ml-with-aws-batch/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS Blog Channel</a>