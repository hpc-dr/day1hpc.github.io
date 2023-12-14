---
title: "Hpc7a performance tweaks you'll want to know about"
date: 2023-12-14T15:31:06+0000
# post thumb
images:
    - "images/post/lB9yTSkUV60.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "lB9yTSkUV60"
layout: "video"
# Taxonomies
categories: [ "AI/ML",  "AWS Batch",  "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "AI/ML",  "AWS",  "Batch",  "CPUs",  "DCV",  "EC2",  "EFA",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "MPI",  "NCCL",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "aws batch",  "bioinformatics",  "cloud computing",  "elastic",  "elastic fabric adapter",  "hpc instances",  "hpc7a",  "infiniband",  "job scheduling",  "performance",  "scientific computing",  "supercomputing",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Looking to maximize performance on AWS's latest HPC instances?

Today we dive into the technical details of how the hpc7a instance type is architected. Stephen Sachs from our HPC performance engineering team explains how understanding the CPU, memory, and networking configuration can help you fully utilize all the compute power this instance family has to offer.

We'll cover how to properly disable CPU cores to optimize memory bandwidth, leveraging both network adapters using MPI for multi-rail for lower latency, and configure MPI runtimes like Intel MPI and Open MPI to get the best results.

Whether you're a seasoned HPC developer or just getting started, this is a must-watch to learn how to squeeze every ounce of performance out of these powerful cloud instances.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by emailing us at ask-hpc@amazon.com.

{{< youtube lB9yTSkUV60 >}}