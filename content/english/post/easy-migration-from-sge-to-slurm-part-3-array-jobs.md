---
title: "Easy migration from SGE to Slurm - Part 3 - Array Jobs"
date: 2021-11-11T17:54:45+0000
# post thumb
images:
    - "images/post/PVO7_fZAT0I.png"
author: "Brendan Bouffler"
# description
description: ""
video_id: "PVO7_fZAT0I"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon NICE DCV",  "Life Sciences", ]
tags: [ "DCV",  "Covid-19",  "EC2",  "slurm",  "array jobs",  "HPC",  "job scripts",  "GPUs",  "Lustre",  "workflow",  "vizualization",  "CPUs",  "virtualization",  "ParallelCluster",  "Schedulers",  "sge",  "High Performance Computing",  "Storage",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

As part of the launch of ParallelCluster 3, we want to make it easy to migrate all your workflows from to Slurm, but we know that it can seem daunting. So we enlisted the help of SchedMD's Director of Cloud Engineering, Nick Ihli to help us show you how it's a lot easier than it might look.

(Seriously, you may need to change very little).

Over the next 5 x Tech Shorts we'll show:

Part 1) Command line syntax and which Slurm commands map to  familiar SGE ones.
Part 2) Job Scripts - what's the stuff you need to care about to adjust ytour scripts? What's actually easier with Slurm?
Part 3) Array Jobs - Slurm has a really elegant way to handle array jobs, and also has some really nice SGE-like commands that will fool you into thinking nothing actually changed.
Part 4) Job Accounting - everyone who has more than 1 user should look at this, because it'll help you manage what your users are doing, limit what damage they can do, and - most importantly - help you understand how you can tune the experience for them so it's even better.
Part 5) Slurm's API for controlling jobs. Coupled with ParallelCluster's API, you can create some really imaginative solutions for your site. 'Infrastructure as Code' takes on a whole new meaning.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube PVO7_fZAT0I >}}