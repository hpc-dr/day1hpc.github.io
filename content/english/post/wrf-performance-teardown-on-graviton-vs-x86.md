---
title: "WRF performance teardown on Graviton vs x86"
date: 2021-05-20T16:16:52+0000
# post thumb
images:
    - "images/post/D2ppdRKSz5I.png"
author: "Brendan Bouffler"
# description
description: ""
video_id: "D2ppdRKSz5I"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Climate/Environment/Weather", ]
tags: [ "Graviton",  "HPC",  "EC2",  "CPUs",  "Lustre",  "WRF",  "MPI",  "x86",  "ParallelCluster",  "weather simulation",  "GPUs",  "Storage",  "Schedulers",  "performance",  "Arm",  "High Performance Computing",  "virtualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

(A complete teardown of WRF performance on x86 and AWS Graviton, from memory subsystems, compilers and MPI stacks).

Weather simulation is a reliably difficult workload for almost any HPC architecture and is often used as a litmus test by many customers before they look too hard at a novel or different systems. Customers have asked us frequently about our performance for codes like WRF, and that’s been even more the case since we launched our Arm-based processor, the AWS Graviton2, in a range of EC2 instances.

So it’s exciting that Karthik Raman and Matt Koop (two leading engineers from our global HPC solution architecture team) dived deep to look at WRF’s performance across a range of instance types (both Intel and Graviton), with EFA (our fast fabric, as you might remember from last week) as well as investigating the impact of different MPIs and compilers.

The results were startling: our Graviton instances performed and scaled pretty much exactly inline with our Intel ones - but at a much lower price, which should be pleasing to everyone.

We sat down at the virtual water cooler with Karthik and Matt to dig into this and understand what the moving parts are that brought this about. We get into memory subsystems, MPIs, collective operations and a lot more.

In the discussion, we reference a lot of material published last week in a blog post at the HPC blog, here: https://aws.amazon.com/blogs/hpc/numerical-weather-prediction-on-aws-graviton2/

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube D2ppdRKSz5I >}}