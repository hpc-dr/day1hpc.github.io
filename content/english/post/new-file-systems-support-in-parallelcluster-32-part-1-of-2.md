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
tags: [ "CPUs",  "DCV",  "EC2",  "EFA",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "MPI",  "ParallelCluster",  "Schedulers",  "Storage",  "ZFS",  "autoscaling",  "bioinformatics",  "cloud computing",  "elastic",  "elastic fabric adapter",  "filesystems",  "infiniband",  "lustre",  "netapp ONTAP",  "openzfs",  "scientific computing",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

ParallelCluster can now mount lots and lots of file systems that you've previously created in your AWS account, in addition to the scratch filesystem you can ask it to create for you when you launch your cluster. And as of today, ParallelCluster supports OpenZFS as one of those filesystems, along with Netapp ONTAP - which will help you get access to data on your enterprise filesystems, too.

Olly Perks and Austin Cherian describe all this in detail, as part 1 of a 2-part series covering the new features of ParallelCluster 3.2.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube 2JOoMv-K1FY >}}