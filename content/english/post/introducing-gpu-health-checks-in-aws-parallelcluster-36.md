---
title: "Introducing GPU health checks in AWS ParallelCluster 3.6"
date: 2023-05-23T00:00:00-0700
# post thumb
images:
    - "images/post/hpcblog-207-header-1120x630.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "AWS ParallelCluster",  "AI/ML", ]
tags: [ "ParallelCluster",  "AI/ML",  "Slurm",  "HPC",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

AWS ParallelCluster 3.6.0 can now detect GPU failures in HPC and AI/ML tasks. Health checks run at the start of Slurm jobs and if they fail, the job is requeued on another instance. This can increase reliability and prevent wasted spend.

<a href="https://aws.amazon.com/blogs/hpc/introducing-gpu-health-checks-in-aws-parallelcluster-3-6/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS Blog Channel</a>