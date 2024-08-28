---
title: "[PCS-015] Bring your own login nodes for AWS Parallel Computing Service"
date: 2024-08-28T18:33:10+0000
# post thumb
images:
    - "images/post/Az0wLO7B_Ns.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "Az0wLO7B_Ns"
layout: "video"
# Taxonomies
categories: [ "AI/ML",  "AWS Batch",  "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "AI/ML",  "AWS",  "AWS PCS",  "Batch",  "CPUs",  "DCV",  "EC2",  "EFA",  "GPUs",  "HPC",  "HPC as a service",  "HPCaaS",  "High Performance Computing",  "Lustre",  "MPI",  "NCCL",  "PCS",  "Parallel Computing Service",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "aws batch",  "bioinformatics",  "cloud computing",  "elastic",  "elastic fabric adapter",  "hpc instances",  "infiniband",  "job scheduling",  "login node",  "scientific computing",  "supercomputing",  "technical computing",  "tightly-coupled",  "virtualization",  "visualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

You can build login nodes that connect to AWS PCS clusters - even if they're not part of the cluster! This is super helpful if you want to give each one of your users access to their own personal login node - to keep their CPU and I/O usage from impacting each other.

You can also use this to cook visualization nodes with amazing remote viz tech like DCV.

Introducing AWS Parallel Computing Service, which is for customers who run high performance computing (HPC) workloads and build scientific and engineering models so they can accelerate their R&D and drive innovation.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by emailing us at ask-hpc@amazon.com.

Chapters

00:00 - Start
01:23 - What's involved in creating a login node?
03:10 - Hands on tutorial
03:28 - Metadata gathering
04:15 - Supported distros
05:41 - Security groups
07:39 - Why SSM?
08:11 - Connecting to the instance
09:26 - Installing Slurm
11:07 - Configure sackd

{{< youtube Az0wLO7B_Ns >}}