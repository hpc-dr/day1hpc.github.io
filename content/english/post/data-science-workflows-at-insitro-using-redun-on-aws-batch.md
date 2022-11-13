---
title: "Data Science workflows at insitro: using redun on AWS Batch"
date: 2022-03-31T00:00:00-0700
# post thumb
images:
    - "images/post/hpcblog-116-p1-fig1.png"
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

Matt Rasmussen, VP of Software Engineering at insitro describes their recently released, open-source data science framework, redun, which allows data scientists to define complex scientific workflows that scale from their laptop to large-scale distributed runs on serverless platforms like AWS Batch and AWS Glue. I this post, Matt shows how redun lends itself to Bioinformatics workflows which typically involve wrapping Unix-based programs that require file staging to and from object storage. In the next blog post, Matt describes how redun scales to large and heterogenous workflows by leveraging AWS Batch features such as Array Jobs and AWS Glue features such as Glue DynamicFrame.

<a href="{{ url }}" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS HPC Blog</a>