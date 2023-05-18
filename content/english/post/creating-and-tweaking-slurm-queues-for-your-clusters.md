---
title: "Creating and tweaking Slurm queues for your clusters"
date: 2023-05-18T12:56:50+0000
# post thumb
images:
    - "images/post/h72NVKYru0Y.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "h72NVKYru0Y"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "CPUs",  "DCV",  "EC2",  "EFA",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "MPI",  "ParallelCluster",  "Schedulers",  "Slurm",  "Storage",  "autoscaling",  "bioinformatics",  "cloud computing",  "elastic",  "elastic fabric adapter",  "infiniband",  "queues",  "scheduling",  "scientific computing",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Compute queues are where all the action is on an HPC cluster. In the cloud, you get the chance to customize the queues to match the code you're going to run on them - which is actually pretty fancy when you think about it.

Matt Vaughn stopped by to show us how to do all that in a few clicks. ParallelCluster is quite powerful and VERY configurable. Thankfully, it's UI makes this all a good deal simpler than it sounds.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

Chapters:

00:28 - Why queues are still relevant in the cloud
01:36 - Memory aware scheduling
02:20 - Scale down time
03:15 - Queue update strategy
04:40 - Adding a queue
07:00 - Compute resources
09:07 - Static and dynamic nodes
10:10 - EFA and placement groups
11:20 - Multi-threading (SMT or hyperthreading)
11:55 - Advance options per CR
14:00 - Outro

{{< youtube h72NVKYru0Y >}}