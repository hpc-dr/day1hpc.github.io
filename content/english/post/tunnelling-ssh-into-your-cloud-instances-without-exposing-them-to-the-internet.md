---
title: "Tunnelling SSH into your cloud instances, without exposing them to the internet"
date: 2024-04-18T15:23:20+0000
# post thumb
images:
    - "images/post/Rt4-jjoo1Og.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "Rt4-jjoo1Og"
layout: "video"
# Taxonomies
categories: [ "AI/ML",  "AWS Batch",  "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "AI/ML",  "AWS",  "AWS SSM",  "Batch",  "CPUs",  "DCV",  "EC2",  "EFA",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "MPI",  "NCCL",  "ParallelCluster",  "SSH",  "SSH tunnels",  "Schedulers",  "Storage",  "autoscaling",  "aws batch",  "aws systems manager",  "bioinformatics",  "cloud computing",  "elastic",  "elastic fabric adapter",  "hpc instances",  "infiniband",  "job scheduling",  "scientific computing",  "supercomputing",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Watch this video to learn how to securely SSH into your AWS EC2 instances without exposing them to the internet!

Setting up Systems Manager Session Manager allows you to proxy SSH connections through a secure tunnel. This lets you maintain full control over who can access your instances, without opening up firewall ports.

We'll walk through how to set this up, and some additional tips for using SSH without lots of command line kungfu.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by emailing us at ask-hpc@amazon.com.

{{< youtube Rt4-jjoo1Og >}}