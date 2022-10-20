---
title: "The impact of network conditions on application performance is complicated."
date: 2021-06-03T15:16:16+0000
# post thumb
images:
    - "images/post/gtQeLmZloJo.png"
author: "Brendan Bouffler"
# description
description: ""
video_id: "gtQeLmZloJo"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon Elastic Fabric Adapter",  "Amazon NICE DCV",  "Life Sciences", ]
tags: [ "latency",  "DCV",  "HPC",  "EC2",  "CPUs",  "Lustre",  "vizualization",  "MPI",  "benchmarks",  "ParallelCluster",  "GPUs",  "Storage",  "Schedulers",  "networking",  "Covid-19",  "High Performance Computing",  "virtualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

In the search for HPC application performance, there’s more than one way to build a network. 

HPC applications (or “codes” as we usually call them) are often at the mercy of the network underpinning an HPC cluster. If your CPUs aren’t busy, it’s usually because something that’s meant to be feeding them data isn’t doing so at a fast enough rate. And often the culprit is the network.

Peter Mendygral has a lot of years of experience looking at networks and is one of the co-authors of the GPCnet benchmark, which aims to have a more nuanced look at how networks deliver for (or fail) the clusters built on them. In todays’s discussion, Pete speaks about the real world conditions found on many network fabrics, and shows us that when they depart from the idealized scenarios that common micro benchmarks measure, the results are anything but stellar.

This helps to understand some of the motivations behind AWS’s Elastic Fabric Adapter (EFA) design and in particular, how the Scalable Reliable Datagram (SRD) it’s built on, solves problems very differently.

During the discussion, we reference a paper about GPCnet. You can find it here. https://escholarship.org/content/qt17m1r82n/qt17m1r82n.pdf?t=q15wzn&v=lg

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube gtQeLmZloJo >}}