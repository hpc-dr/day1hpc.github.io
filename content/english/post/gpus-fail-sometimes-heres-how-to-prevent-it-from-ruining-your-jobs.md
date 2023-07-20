---
title: "GPUs fail sometimes - here's how to prevent it from ruining your jobs"
date: 2023-07-20T14:52:28+0000
# post thumb
images:
    - "images/post/2TL5ZfGb7i8.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "2TL5ZfGb7i8"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "CPUs",  "DCV",  "EC2",  "EFA",  "GPU health",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "MPI",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "bioinformatics",  "cloud computing",  "elastic",  "elastic fabric adapter",  "hardware failiure",  "infiniband",  "scientific computing",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

GPUs fail. There: we've said it. Hardware is ... well, it's hardware, and so it's prone to failing sometimes. Have a large enough number of GPUs working away in a data center and the odds are good that there's a hinky one somewhere in that big, cold, dreadfully noisy room.

But you can do a simple action to prevent this from ruining your day, by running NVIDIA's  GPU health checks before your jobs kick off. And you can now do that auto-magic-ally, due to this new feature in ParallelCluster 3.6.

Matt Vaughn told us how it works.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube 2TL5ZfGb7i8 >}}