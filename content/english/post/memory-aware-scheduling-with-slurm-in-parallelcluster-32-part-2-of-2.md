---
title: "Memory aware scheduling with Slurm in ParallelCluster 3.2 (Part 2 of 2)"
date: 2022-07-28T14:07:45+0000
# post thumb
images:
    - "images/post/3YP8CbckYQA.png"
author: "Brendan Bouffler"
# description
description: ""
video_id: "3YP8CbckYQA"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon Elastic Fabric Adapter",  "Amazon NICE DCV",  "Life Sciences", ]
tags: [ "memory aware",  "EC2",  "GPUs",  "Lustre",  "virtualization",  "technical computing",  "ParallelCluster",  "vizualization",  "elastic fabric adapter",  "High Performance Computing",  "Storage",  "cloud computing",  "slurm",  "scientific computing",  "bioinformatics",  "scheduling",  "HPC",  "autoscaling",  "CPUs",  "DCV",  "MPI",  "elastic",  "tightly-coupled",  "EFA",  "Schedulers",  "infiniband",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

If you've ever had to iteratively guess how much memory is left in a bunch of compute nodes in order to get your memory-hungry jobs running, then this feature will save your sanity.

It's a new integration between ParallelCluster and Slurm that lets you specify how much RAM your jobs need, and gives Slurm the ability to figure out how to place your jobs in order to achieve that - not just counting cores, which is the default behavior for most schedulers.

Olly Perks and Austin Cherian describe this in detail, as part of a 2-part series covering the new features of ParallelCluster 3.2 (part 1 covered new file systems support and you can find it here: https://youtu.be/2JOoMv-K1FY).

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube 3YP8CbckYQA >}}