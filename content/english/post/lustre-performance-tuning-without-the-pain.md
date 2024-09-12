---
title: "Lustre performance tuning without the pain"
date: 2024-09-12T15:18:39+0000
# post thumb
images:
    - "images/post/GgLTcjE2Y8Y.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "GgLTcjE2Y8Y"
layout: "video"
# Taxonomies
categories: [ "AI/ML",  "AWS Batch",  "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "AI/ML",  "AWS",  "Batch",  "CPUs",  "DCV",  "EC2",  "EFA",  "FSx for Lustre",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "MPI",  "NCCL",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "aws batch",  "bioinformatics",  "cloud computing",  "dynamic IOPS",  "elastic",  "elastic fabric adapter",  "hpc instances",  "infiniband",  "job scheduling",  "scientific computing",  "supercomputing",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Are you struggling to keep up with the storage demands of your HPC users? Got specific applications that are just ... even more needy than others?

Today we show you how to scale capacity, throughput, and metadata performance on the fly without disruption. This includes a show'n'tell about the new adjustable metadata IOPS features that launched just recently.

Whether you need high IOPS, sub-millisecond latencies, or hundreds of GB/s throughput, FSx for Lustre provides the flexibility to tailor your storage performance to match your compute requirements.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by emailing us at ask-hpc@amazon.com.

Chapters

00:00 - Intro
00:32 - What is Amazon FSx for Lustre?
01:10 - Creating a Lustre file system (in a few minutes) 
02:15 - The link between performance and capacity
03:04 - Provisioned Metadata IOPS (new)
04:55 - How Metadata IOPS can scale with capacity, too
05:45 - Data compression (for free)
07:42 - Altering a Lustre file system later
09:08 - Changing metadata IOPS later, too

{{< youtube GgLTcjE2Y8Y >}}