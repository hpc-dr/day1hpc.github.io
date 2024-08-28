---
title: "[PCS-004] Create and use a custom AMI for AWS Parallel Computing Service"
date: 2024-08-28T18:33:18+0000
# post thumb
images:
    - "images/post/3ysMkZrDlGI.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "3ysMkZrDlGI"
layout: "video"
# Taxonomies
categories: [ "AI/ML",  "AWS Batch",  "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "AI/ML",  "AWS",  "AWS PCS",  "Batch",  "CPUs",  "DCV",  "EC2",  "EFA",  "GPUs",  "HPC",  "HPC as a service",  "HPCaaS",  "High Performance Computing",  "Lustre",  "MPI",  "NCCL",  "PCS",  "Parallel Computing Service",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "aws batch",  "bioinformatics",  "cloud computing",  "elastic",  "elastic fabric adapter",  "hpc instances",  "infiniband",  "job scheduling",  "scientific computing",  "supercomputing",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Custom AMIs are powerful in PCS - and also quite necessary. Matt shows us the easiest way to create one, and lets on some tricks to make it easy - and extendable later on.

Introducing AWS Parallel Computing Service, which is for customers who run high performance computing (HPC) workloads and build scientific and engineering models so they can accelerate their R&D and drive innovation.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by emailing us at ask-hpc@amazon.com.

Chapters

00:00 - Start
03:02 - Launching an instance to build on
07:57 - Reboot
10:32 - Connecting to an EFS file system
12:25 - Install SSM and CloudWatch agents
13:54 - Install PCS agent
14:56 - Install Slurm
16:22 - Installing application software via Spack
19:51 - Confirm Spack installed correctly
20:34 - Installing OpenFOAM
22:46 - Check OpenFOAM in our environment
23:56 - Build your AMI
25:17 - Add the AMI to a PCS node group

{{< youtube 3ysMkZrDlGI >}}