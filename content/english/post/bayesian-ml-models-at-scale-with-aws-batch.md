---
title: "Bayesian ML Models at Scale with AWS Batch"
date: 2022-06-14T00:00:00-0700
# post thumb
images:
    - "images/post/hpcblog-124-header.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "AWS Batch",  "AI/ML", ]
tags: [ "Batch",  "HPC",  "Modeling",  "AI/ML",  "Media",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

Ampersand is a data-driven TV advertising technology company that provides aggregated TV audience impression insights and planning on 42 million households, in every media market, across more than 165 networks and apps and in all dayparts (broadcast day segments). The Ampersand Data Science team estimated that building their statistical models would require up to 600,000 physical CPU hours to run, which would not be feasible without using a massively parallel and large-scale architecture in the cloud. AWS Batch enabled Ampersand to compress their time of computation over 500x through massive scaling while optimizing their costs using Amazon EC2 Spot. In this blog post, we will provide an overview of how Ampersand built their TV audience impressions (“impressions”) models at scale on AWS, review the architecture they have been using, and discuss optimizations they conducted to run their workload efficiently on AWS Batch.

<a href="{{ url }}" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS HPC Blog</a>