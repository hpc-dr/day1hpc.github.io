---
title: "Running cost-effective GROMACS simulations using Amazon EC2 Spot Instances with AWS ParallelCluster"
date: 2022-06-09T00:00:00-0700
# post thumb
images:
    - "images/post/hpcblog-69-header.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Life Sciences", ]
tags: [ "HPC",  "ParallelCluster",  "Simulation",  "Life Sciences",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

In this blog post, we cover how to run GROMACS – a popular open source designed for simulations of proteins, lipids, and nucleic acids – cost effectively by leveraging EC2 Spot Instances within AWS ParallelCluster. We also show how to checkpoint GROMACS to recover gracefully from possible Spot Instance interruptions.

<a href="https://aws.amazon.com/blogs/hpc/running-gromacs-on-spot-with-checkpointing/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS HPC Blog</a>