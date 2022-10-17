---
title: "Data Science workflows at insitro: using redun on AWS Batch"
date: 2022-03-31T00:00:00-0700
# post thumb
images:
    - "images/post/hpcblog-116-p1-fig1.png"
#author
author: "Matt Vaughn"
# description
description: ""
# Taxonomies
categories: [ "Life Sciences",  "Amazon Batch", ]
tags: [ "Artificial Intelligence",  "HPC",  "Life Sciences",  "Batch",  "Glue",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

Matt Rasmussen, VP of Software Engineering at insitro describes their recently released, open-source data science framework, redun, which allows data scientists to define complex scientific workflows that scale from their laptop to large-scale distributed runs on serverless platforms like AWS Batch and AWS Glue. I this post, Matt shows how redun lends itself to Bioinformatics workflows which typically involve wrapping Unix-based programs that require file staging to and from object storage. In the next blog post, Matt describes how redun scales to large and heterogenous workflows by leveraging AWS Batch features such as Array Jobs and AWS Glue features such as Glue DynamicFrame.

Read the full post at the [AWS HPC Blog](https://aws.amazon.com/blogs/hpc/data-science-workflows-at-insitro-using-redun-on-aws-batch/).
