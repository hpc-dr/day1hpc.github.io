---
title: "[PCS-007] - Using Hashicorp Packer for AWS PCS machine images"
date: 2024-11-13T14:16:19+0000
# post thumb
images:
    - "images/post/Nfqwbiakxgw.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "Nfqwbiakxgw"
layout: "video"
# Taxonomies
categories: [ "AI/ML",  "AWS Batch",  "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "AI/ML",  "AWS",  "AWS PCS",  "Batch",  "CPUs",  "DCV",  "EC2",  "EFA",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "MPI",  "NCCL",  "PCS",  "Parallel Computing Service",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "aws batch",  "bioinformatics",  "cloud computing",  "elastic",  "elastic fabric adapter",  "hpc instances",  "infiniband",  "job scheduling",  "scientific computing",  "supercomputing",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Are you interested in learning how to automate building machine images for HPC?

Matt walks you through using HashiCorp Packer to efficiently create Amazon Machine Images (AMIs) tailored for AWS Parallel Computing Service.

You'll see a full demonstration of developing a template, configuring builders and provisioners, and launching a complete AMI build process. And it all uses a recipe which we've provided in the HPC Recipe Library.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by emailing us at ask-hpc@amazon.com.

Chapters

00:00 - Start
00:29 - Packer's anatomy
02:15 - Anatomy of our Packer template
04:11 - Packer Provisioners
09:05 - Adding a provisioner (for Spack)

{{< youtube Nfqwbiakxgw >}}