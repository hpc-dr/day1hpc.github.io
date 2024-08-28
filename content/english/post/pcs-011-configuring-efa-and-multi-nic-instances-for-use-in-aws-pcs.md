---
title: "[PCS-011] Configuring EFA and multi-NIC instances for use in AWS PCS"
date: 2024-08-28T18:33:42+0000
# post thumb
images:
    - "images/post/5hkA-y4alB0.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "5hkA-y4alB0"
layout: "video"
# Taxonomies
categories: [ "AI/ML",  "AWS Batch",  "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "AI/ML",  "AWS",  "AWS PCS",  "Batch",  "CPUs",  "DCV",  "EC2",  "EFA",  "GPUs",  "HPC",  "HPC as a service",  "HPCaaS",  "High Performance Computing",  "Lustre",  "MPI",  "NCCL",  "PCS",  "Parallel Computing Service",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "aws batch",  "bioinformatics",  "cloud computing",  "elastic",  "elastic fabric adapter",  "hpc instances",  "infiniband",  "job scheduling",  "scientific computing",  "supercomputing",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

You need to do a few key things to get EFA enabled in AWS PCS clusters - and there's an extra step or two if you're using multi-rail EFA instances like the HPC7a or any accelerated instances from the P4 or P5 families. Matt shows us how.

Introducing AWS Parallel Computing Service, which is for customers who run high performance computing (HPC) workloads and build scientific and engineering models so they can accelerate their R&D and drive innovation.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by emailing us at ask-hpc@amazon.com.

Chapters

00:00 - Start
03:26 - Multi-NIC instances
04:38 - EFA Security Group
06:19 - Cluster Placement Group
07:39 - Launch Template
10:48 - CloudFormation template deep-dive
17:05 - What did the CFN stack create for us?
17:16 - Adding everything into PCS (final steps)

{{< youtube 5hkA-y4alB0 >}}