---
title: "ParallelCluster 3 - Launch and Cluster Operations"
date: 2022-01-20T15:11:08+0000
# post thumb
images:
    - "images/post/Vwfx7ruTrUw.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "Vwfx7ruTrUw"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon NICE DCV",  "Life Sciences", ]
tags: [ "CPUs",  "Covid-19",  "DCV",  "EC2",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "ParallelCluster",  "Schedulers",  "Slurm",  "Storage",  "queues",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

In a previous show (https://youtu.be/6gAwAK5IJ2w), we talked about  'Infrastructure as Code', or how the ParallelCluster 3 YAML config translated to an actual cluster running, ready to take jobs.

Today, Austin Cherian joins us again to walk through standing up the cluster using that config, and how we can adjust the cluster on the fly if, for example, we needed to add some new node types into the compute fleets, like if we need some fat memory nodes, or a new GPU type.

The reference guide for doing dynamic updates is here: https://docs.aws.amazon.com/parallelcluster/latest/ug/using-pcluster-update-cluster-v3.html

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube Vwfx7ruTrUw >}}