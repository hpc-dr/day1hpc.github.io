---
title: "KEK's novel solution for CryoEM's software and infra (Part 2 of 4)"
date: 2022-10-11T16:53:39+0000
# post thumb
images:
    - "images/post/rdF1AzfadOY.png"
author: "Brendan Bouffler"
# description
description: ""
video_id: "rdF1AzfadOY"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon Elastic Fabric Adapter",  "Amazon NICE DCV",  "Life Sciences", ]
tags: [ "Lustre",  "CPUs",  "MPI",  "autoscaling",  "Storage",  "HPC Japan",  "DCV",  "cloud computing",  "EC2",  "ParallelCluster",  "cryoEM",  "HPC",  "vizualization",  "Schedulers",  "technical computing",  "tightly-coupled",  "elastic fabric adapter",  "bioinformatics",  "scientific computing",  "infiniband",  "elastic",  "High Performance Computing",  "virtualization",  "GPUs",  "EFA",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

CryoEM is an awesome research tool, but it also comes with some challenges. The software stack is complex, and the hardware it needs is sometimes exotic and hard to get. Afterwards, there's a massive dataset and a serious set of challenges to moving it around, and managing it. (No one wants to get stuck baby sitting someone else's petabyte dataset unless they have to).

The team at KEK in Japan took all these challenges head on and solved them in a very different way (spoiler: it involved the cloud). But as is often the case, when teams in Japan solve a big HPC problem, it's usually something that's going to get picked up around the world. And KEK are very much those kinds of people.

Today is just one part in a series of Four HPC Tech Shorts dedicated to the work KEK did (yes, it's _that_ awesome).

Part 1 - describes the problem, and the extra challenge of doing work in a world of lock downs due to Covid.
Part 2 - describes the software and infrastructure solution they came up with, and shows you how it works.
Part 3 - discusses the impact this had on their operations, and its special role in forming a distributed CryoEM network across the whole country. A mesh of centers sharing knowledge, resources, and talent - really efficiently.
Part4 - the final episode is a deep dive into the arsenal of benchmark data they’ve amassed, which the CryoEM junkies watching this channel can use to make their own decisions about what’s going to be the best CPU and GPU combinations to use for your workloads, at the resolutions you’re working at.

Like we said: there's a ton of stuff for us all to learn from our friends at KEK in Japan.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube rdF1AzfadOY >}}