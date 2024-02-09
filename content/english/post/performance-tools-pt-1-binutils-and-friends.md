---
title: "Performance tools Pt 1 - binutils and friends"
date: 2024-02-09T15:04:35+0000
# post thumb
images:
    - "images/post/aNGcfVG4ZqU.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "aNGcfVG4ZqU"
layout: "video"
# Taxonomies
categories: [ "AI/ML",  "AWS Batch",  "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "AI/ML",  "AWS",  "Batch",  "CPUs",  "DCV",  "DLLs",  "EC2",  "EFA",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "MPI",  "NCCL",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "aws batch",  "bioinformatics",  "cloud computing",  "dynamic linking",  "elastic",  "elastic fabric adapter",  "hacks",  "hpc instances",  "infiniband",  "job scheduling",  "libraries",  "performance",  "scientific computing",  "supercomputing",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Welcome to the world of dynamically linked libraries and all the fun involved in predicting - and then manipulating - which libraries your binaries see and use ... all so you can get the results and performance you expect.

Dr Stephen Sachs from our performance engineering team lives in this world every day, and gave up a bunch of his time to help the Tech Shorts community understand how to use all these tools.

Part 1: readelf, nm, strings, ldd, objdump
Part 2: static vs dynamic linking
Part 3: RPATH and RUNPATH - manipulating which libraries your executable sees.
Part 4: let's hack a binary to show you how this all works in practice.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by emailing us at ask-hpc@amazon.com.

00:00 - Intro to dynamic linking and binary hacking
00:27 - readelf
03:40 - nm
06:43 - strings
09:09 - ldd
10:12 - objdump
13:14 - What's next

{{< youtube aNGcfVG4ZqU >}}