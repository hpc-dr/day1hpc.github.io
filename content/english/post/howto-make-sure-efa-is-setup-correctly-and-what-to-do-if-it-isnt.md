---
title: "HOWTO make sure EFA is setup correctly (and what to do if it isn't)."
date: 2021-05-28T14:22:10+0000
# post thumb
images:
    - "images/post/Wq8EMMXsvyo.png"
author: "Brendan Bouffler"
# description
description: ""
video_id: "Wq8EMMXsvyo"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon Elastic Fabric Adapter", ]
tags: [ "HPC",  "EC2",  "CPUs",  "Lustre",  "vizualization",  "ParallelCluster",  "infiniband",  "GPUs",  "Storage",  "EFA",  "Schedulers",  "elastic fabric adapter",  "fabrics",  "High Performance Computing",  "virtualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

By popular request, we’re looking today at the EFA software stack and environment: how to make sure it’s set up correctly (so you get great performance from your codes), how to tell if it’s not, and how to fix that.

Austin Cherian, our performance junkie from the HPC Developer Relations team in AWS Engineering joins us to deep dive into the nitty gritty of the stack and some useful techniques for debugging. We cover both Open MPI and Intel MPI, as well as checking the libfabric providers and the hardware enablement underneath.

In the discussion, we reference a lot of helpful pages, including:

* the EFA homepage: https://aws.amazon.com/hpc/efa/
* supported instances: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types
* the user guide: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html
* troubleshooting: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshooting-ena.html#disable-enhanced-networking-ena-instance-store

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube Wq8EMMXsvyo >}}