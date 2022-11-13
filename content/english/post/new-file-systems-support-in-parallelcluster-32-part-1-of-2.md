---
title: "New file systems support in ParallelCluster 3.2 (Part 1 of 2)"
date: 2022-07-28T14:07:47+0000
# post thumb
images:
    - "images/post/2JOoMv-K1FY.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "2JOoMv-K1FY"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "HPC",  "Schedulers",  "Storage",  "elastic fabric adapter",  "ParallelCluster",  "MPI",  "lustre",  "openzfs",  "filesystems",  "elastic",  "scientific computing",  "virtualization",  "High Performance Computing",  "EC2",  "GPUs",  "tightly-coupled",  "vizualization",  "ZFS",  "bioinformatics",  "cloud computing",  "CPUs",  "technical computing",  "infiniband",  "DCV",  "Lustre",  "EFA",  "autoscaling",  "netapp ONTAP",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

ParallelCluster can now mount lots and lots of file systems that you've previously created in your AWS account, in addition to the scratch filesystem you can ask it to create for you when you launch your cluster. And as of today, ParallelCluster supports OpenZFS as one of those filesystems, along with Netapp ONTAP - which will help you get access to data on your enterprise filesystems, too.

Olly Perks and Austin Cherian describe all this in detail, as part 1 of a 2-part series covering the new features of ParallelCluster 3.2.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube 2JOoMv-K1FY >}}