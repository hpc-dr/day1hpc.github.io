---
title: "Cost-optimization on Spot Instances using checkpoint for Ansys LS-DYNA"
date: 2021-09-27T00:00:00-0700
# post thumb
images:
    - "images/post/ls-dyna-spot-header-1260x630.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "AWS ParallelCluster", ]
tags: [ "Technical How-to",  "HPC",  "EC2",  "ParallelCluster",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

A major portion of the costs incurred for running Finite Element Analyses (FEA) workloads on AWS comes from the usage of Amazon EC2 instances. Amazon EC2 Spot Instances offer a cost-effective architectural choice, allowing you to take advantage of unused EC2 capacity for up to a 90% discount compared to On-Demand Instance prices. In this post, we describe how you 0can run fault-tolerant FEA workloads on Spot Instances using Ansys LS-DYNA’s checkpointing and auto-restart utility.

<a href="{{ url }}" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS HPC Blog</a>