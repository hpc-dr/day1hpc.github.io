---
title: "Efficient and cost-effective rendering pipelines with Blender and AWS Batch"
date: 2022-07-05T00:00:00-0700
# post thumb
images:
    - "images/post/CleanShot-2022-06-17-at-16.15.49.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "AWS Batch", ]
tags: [ "HPC",  "Batch",  "Media",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

This blog post explains how to run parallel rendering workloads and produce an animation in a cost and time effective way using AWS Batch and AWS Step Functions. AWS Batch manages the rendering jobs on Amazon Elastic Compute Cloud (Amazon EC2), and AWS Step Functions coordinates the dependencies across the individual steps of the rendering workflow. Additionally, Amazon EC2 Spot instances can be used to reduce compute costs by up to 90% compared to On-Demand prices.

<a href="https://aws.amazon.com/blogs/hpc/efficient-and-cost-effective-rendering-pipelines-with-blender-and-aws-batch/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS HPC Blog</a>