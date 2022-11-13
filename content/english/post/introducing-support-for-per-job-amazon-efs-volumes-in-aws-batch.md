---
title: "Introducing support for per-job Amazon EFS volumes in AWS Batch"
date: 2021-04-05T00:00:00-0700
# post thumb
images:
    - "images/post/batch-efs-header-1260x630.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "AWS Batch", ]
tags: [ "Batch",  "Technical How-to",  "HPC",  "Elastic Container Service",  "Fargate",  "Elastic File System (EFS)",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

Large-scale data analysis usually involves some multi-step process where the output of one job acts as the input of subsequent jobs. Customers using AWS Batch for data analysis want a simple and performant storage solution to share with and between jobs. We are excited to announce that customers can now use Amazon Elastic File System (Amazon […]

<a href="{{ url }}" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS HPC Blog</a>