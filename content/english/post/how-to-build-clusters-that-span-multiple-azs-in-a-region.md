---
title: "How to build clusters that span multiple AZs in a region"
date: 2023-06-01T17:28:06+0000
# post thumb
images:
    - "images/post/cyNarSvc0mY.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "cyNarSvc0mY"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "CPUs",  "DCV",  "EC2",  "EFA",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "MPI",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "availability zones",  "bioinformatics",  "cloud computing",  "elastic",  "elastic fabric adapter",  "infiniband",  "multi-AZ",  "scientific computing",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Building ParallelClusters that span multiple Availability Zones in a region take some careful planning with respect to storage and networking, but opens up options for more capacity - which is often the driver behind this design.

Matt Vaughn works us through some examples to understand how to do this well.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

Chapters:

00:00 - Why multi-AZ clusters?
00:37 - Single AZ case
02:08 - Multi-AZ simple case
02:42 - No EFA across AZs
04:00 - Share storage considerations
04:24 - EFS in a multi-AZ cluster
04:44 - Cross-AZ data charges
05:34 - Lustre in a multi-AZ cluster
06:20 - Outro

{{< youtube cyNarSvc0mY >}}