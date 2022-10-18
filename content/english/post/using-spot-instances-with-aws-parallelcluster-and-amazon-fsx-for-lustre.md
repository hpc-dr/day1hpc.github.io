---
title: "Using Spot Instances with AWS ParallelCluster and Amazon FSx for Lustre"
date: 2022-01-19T00:00:00-0800
# post thumb
images:
    - "images/post/hpcblog-77-header-1260x630.png"
#author
author: "Matt Vaughn"
# description
description: ""
# Taxonomies
categories: [ "AWS ParallelCluster", ]
tags: [ "FSx for Lustre",  "HPC",  "ParallelCluster",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

Processing large amounts of complex data often requires leveraging a mix of different Amazon EC2 instance types. These types of computations also benefit from shared, high performance, scalable storage like Amazon FSx for Lustre. A way to save costs on your analysis is to use Amazon EC2 Spot Instances, which can help to reduce EC2 costs up to 90% compared to On-Demand Instance pricing. This post will guide you in the creation of a fault-tolerant cluster using AWS ParallelCluster. We will explain how to configure ParallelCluster to automatically unmount the Amazon FSx for Lustre filesystem and resubmit the interrupted jobs back into the queue in the case of Spot interruption events.

Read the full post at the [AWS HPC Blog](https://aws.amazon.com/blogs/hpc/using-spot-instances-with-aws-parallelcluster-and-amazon-fsx-for-lustre/).
