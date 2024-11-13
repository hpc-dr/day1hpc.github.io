---
title: "[PCS-006] - Using EC2 Image Builder for AWS PCS machine images"
date: 2024-11-13T14:16:11+0000
# post thumb
images:
    - "images/post/d_AUNURmhwY.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "d_AUNURmhwY"
layout: "video"
# Taxonomies
categories: [ "AI/ML",  "AWS Batch",  "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "AI/ML",  "AWS",  "AWS PCS",  "Batch",  "CPUs",  "DCV",  "EC2",  "EFA",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "MPI",  "NCCL",  "PCS",  "Parallel Computing Service",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "aws batch",  "bioinformatics",  "cloud computing",  "elastic",  "elastic fabric adapter",  "hpc instances",  "infiniband",  "job scheduling",  "scientific computing",  "supercomputing",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Are you looking to build HPC clusters with AWS Parallel Computing Service?

Today, Matt walks you through how to use EC2 Image Builder to automate creating optimized machine images specifically for this purpose.

Image Builder and our recipes library provide you pre-built components to install essential HPC software like Slurm, EFA, and CloudWatch. You'll see a step-by-step demo of building a pipeline to create a customized HPC-ready AMI.

Image Builder makes it easy to reproduce your environment and respond quickly to updates. The video shows how you can create child AMIs to layer on domain-specific apps for different user groups. Whether you need an optimized machine image for CFD, pharmacology, or finance applications, Image Builder provides a managed service to ensure consistency across AMIs. Automating machine image creation reduces mistakes and empowers you to provision the precise HPC environment you need.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by emailing us at ask-hpc@amazon.com.

Chapters

00:00 - Start
00:21 - What does PCS need in an AMI?
00:53 - Introducing the HPC ready armies in the HPC recipe library
01:32 - What components have we put in the recipe/repo ?
04:35 - We think everyone should consider using Spack, too
05:27 - All-in-one HPC Recipe to get you started
06:06 - Let's deploy this stack, and start building
06:47 - They're deployed, let's check out the components we now have
07:40 - Let's build a pipeline
08:20 - Selecting our image builder components
11:17 - We need a little more space on our root volume
11:29 - Distribution settings
11:40 - Let's build an image
12:28 - We can automate this even more
19:12 - Let's do this all again using the CLI
21:22 - Some special considerations for your local region selection
22:32 - Considerations for some distros
22:57 - Spack, again (yes, we're fans - you should be too)
26:22 - Layering AMIs pipelines on each other

{{< youtube d_AUNURmhwY >}}