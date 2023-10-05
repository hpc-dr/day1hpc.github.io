---
title: "A deep dive into HTC Grid on AWS"
date: 2023-10-05T17:26:26+0000
# post thumb
images:
    - "images/post/dJ0GTgz5Nrs.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "dJ0GTgz5Nrs"
layout: "video"
# Taxonomies
categories: [ "AI/ML",  "AWS Batch",  "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Financial Services",  "Life Sciences", ]
tags: [ "AI/ML",  "AWS",  "Batch",  "CPUs",  "DCV",  "EC2",  "EFA",  "FSI",  "GPUs",  "HPC",  "HTC",  "High Performance Computing",  "Lustre",  "MPI",  "NCCL",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "aws batch",  "banking",  "bioinformatics",  "cloud computing",  "elastic",  "elastic fabric adapter",  "financial services",  "grid",  "grid scheduler",  "hpc instances",  "infiniband",  "job scheduling",  "scientific computing",  "supercomputing",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

FSI customers frequently start with a blank page when writing their plans for shifting HPC workloads into the cloud. Our solution architects saw a pattern tho - lots of customers trying to solve the same problems we'd witnessed elsewhere.

So Carlos Manzanedo Rueda, Clement Rey, and Kirill Bogdanov created 'HTC Grid'. It's an open source package you can download and use. It'll get you much closer to your goal than starting from scratch. It navigates you around the problems that slowed other people down. And it's highly customizable.

Kirill stopped by to explain the architecture and what drove some of their decisions.

You can find out more about the FSI HPC space from a previous talk by Alex Kimber - our chief HPC FSI nerd.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by emailing us at ask-hpc@amazon.com.

{{< youtube dJ0GTgz5Nrs >}}