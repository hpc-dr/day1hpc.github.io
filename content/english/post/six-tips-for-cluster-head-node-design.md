---
title: "Six tips for cluster head node design"
date: 2023-04-27T11:42:51+0000
# post thumb
images:
    - "images/post/cGaBaxDR9Qo.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "cGaBaxDR9Qo"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "CPUs",  "DCV",  "EC2",  "EFA",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "MPI",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "bioinformatics",  "cloud computing",  "design",  "elastic",  "elastic fabric adapter",  "head node",  "headnode",  "infiniband",  "scientific computing",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

We always worry the most about the compute nodes on a cluster (for a good reason - it's where all the action is), but it's worth taking a moment to think about your head node, because that's where you can really define your user's experience.

Matt Vaughn stopped by to explain some of the fundamentals for head node design in AWS ParallelCluster and gave us 6 tips for getting it close enough the first time - but don't forget these are just mouse clicks, and you can change your mind later, really easily.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

Chapters:

00:52 - What's in a head node anyway?
01:50 - Head node instance and CPU choice
02:15 - Graphics-enabled head node?
03:58 - AWS Systems Manager
05:43 - DCV for visualization
06:52 - Head node security groups and access
07:15 - Post install scripts to customize the environment
08:33 - Head node storage

{{< youtube cGaBaxDR9Qo >}}