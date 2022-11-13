---
title: "AWS's HPC Storage storage options - choose, use and abuse. Here's how."
date: 2021-07-09T12:43:09+0000
# post thumb
images:
    - "images/post/PY_X49SQWuo.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "PY_X49SQWuo"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon NICE DCV",  "Life Sciences", ]
tags: [ "HPC",  "High Performance Computing",  "Covid-19",  "CPUs",  "Schedulers",  "Storage",  "EC2",  "DCV",  "GPUs",  "Lustre",  "ParallelCluster",  "vizualization",  "virtualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

AWS has a LOT of storage options (block, PIOPS, object, volume, loads of file sytems), pretty much all of which can be used for HPC. That's because we're not forced to come up with one single massively fast storage solution that can cope with a hurricane of worst-case usage - you're not making one-way door decisions on infrastructure. Cloud infrastructure is a two-way door and you can change your mind as many times as you like.

So, yes, you can have 200 GByte/s Lustre, but if you're doing embarrassingly-parallel workloads that just need to stream data through a CPU, you're missing an optimization right there. You can have very specifically tuned storage for very specific workloads (and specific clusters or compute environments, too, if you like). And you can have very specifically lower costs associated with it if you do.

Our Principal Developer Advocate, Angel Pizarro (@delagoya) walks us through the options, and helps you figure out how each of these native AWS services might form part of your environment.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube PY_X49SQWuo >}}