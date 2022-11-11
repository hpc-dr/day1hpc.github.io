---
title: "How EFA works and why we don't use infiniband in the cloud."
date: 2021-05-13T15:00:17+0000
# post thumb
images:
    - "images/post/IgPWzhIHX68.png"
author: "Brendan Bouffler"
# description
description: ""
video_id: "IgPWzhIHX68"
layout: "video"
# Taxonomies
categories: [ "AI/ML",  "AWS ParallelCluster",  "Amazon Elastic Fabric Adapter", ]
tags: [ "virtualization",  "EC2",  "low latency",  "fabric",  "Intel MPI",  "MVAPICH",  "High Performance Computing",  "CPUs",  "open MPI",  "Storage",  "HPC",  "networking",  "Lustre",  "Schedulers",  "GPUs",  "ParallelCluster",  "infiniband",  "MPI",  "NCCL",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

AWS’s compute infrastructure is very much not like a ‘normal’ supercomputer (whatever that is). We don’t start with a blank page every few years and design the next big system. It’s more like a city where we have to build on what’s there already, renovate occasionally, and push for bigger and better and faster whilst keeping the lights on at all times.

That leads to a bunch of design decisions that drive our engineers in a very different direction and our Elastic Fabric Adapter is an example of just that. Brian Barrett (one of our Principal Engineers in the HPC team) joins us this week to talk about the genesis of EFA, how it works, and why it convinced us that we could do without specialist fabrics like Infiniband and still deliver the same (or better) application scaling performance that our HPC customers were pushing us for.

During the discussion, we mentioned an IEEE paper which is worth reading for more insights into SRD: “A Cloud-Optimized Transport Protocol for Elastic and Scalable HPC” : https://ieeexplore.ieee.org/document/9167399

And we also shamelessly tried to hire all of you for our EFA engineering team to work on some more difficult problems. That link is here: http://boofla.io/jobs

More about EFA is here: https://aws.amazon.com/hpc/efa/

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube IgPWzhIHX68 >}}