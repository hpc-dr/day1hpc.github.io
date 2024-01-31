---
title: "In search of performance, details matter - behind the scenes in ParallelCluster"
date: 2024-01-31T11:44:14+0000
# post thumb
images:
    - "images/post/NUQzRHXdPbg.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "NUQzRHXdPbg"
layout: "video"
# Taxonomies
categories: [ "AI/ML",  "AWS Batch",  "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "AI/ML",  "AWS",  "Batch",  "CPUs",  "DCV",  "EC2",  "EFA",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "MPI",  "NCCL",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "aws batch",  "bioinformatics",  "cloud computing",  "elastic",  "elastic fabric adapter",  "hpc instances",  "infiniband",  "job scheduling",  "performance",  "scientific computing",  "supercomputing",  "technical computing",  "tightly-coupled",  "tuning",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Delving into the important but unheralded optimizations that enable HPC systems to truly fly, Stephen Sachs walks us through some of the nitty gritty details that can throttle - or unleash - performance.

From ancient Fortran codes pushing stack limits, to NFS threads saturating head nodes, it's a masterclass in the hidden factors that separate functional clusters from blazing fast ones. For anyone running simulations and models on a cluster in the cloud, the tips here will give you some insights into the countless interdependencies that make up a working HPC system.

The next time your code screams instead of grinds, remember the care poured into finely tuning these massive machines, and be grateful for the wizards who work their magic.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by emailing us at ask-hpc@amazon.com.

{{< youtube NUQzRHXdPbg >}}