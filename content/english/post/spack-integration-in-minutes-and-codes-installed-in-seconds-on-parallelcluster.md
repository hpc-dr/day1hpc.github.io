---
title: "Spack integration in minutes and codes installed in seconds on ParallelCluster"
date: 2023-06-08T09:03:24+0000
# post thumb
images:
    - "images/post/WzXjVgpZ8IU.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "WzXjVgpZ8IU"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "CPUs",  "DCV",  "EC2",  "EFA",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "MPI",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "bioinformatics",  "cloud computing",  "elastic",  "elastic fabric adapter",  "infiniband",  "package management",  "scientific computing",  "spack",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Building scientific or engineering code stacks from source used to suck in the time before Spack. Todd, Greg and the community built an amazing resource that houses all the build recipes and knows all the dependencies SO YOU DON'T HAVE TO :-)

Now we've added our Spack integration to ParallelCluster and set it up to make great use of Spack's binary cache which means that once something is built you don't need to build it again.

Think GROMACS in one second. OpenFOAM in 16 seconds. Yes, really.

Matt dropped by to explain how this works.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

00:00 - Intro
00:30 - Zero to WRF in 20 mins
00:55 - ParallelCluster
01:58 - Custom actions
02:35 - App installation speedups
03:05 - Add this to your cluster
04:00 - Installing Palace (a hard example)
05:20 - How fast is this?
06:55 - Outro

{{< youtube WzXjVgpZ8IU >}}