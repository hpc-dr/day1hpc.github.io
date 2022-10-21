---
title: "How to explore Slurm's job management API from a Python notebook - (Part 5)"
date: 2022-01-27T16:48:25+0000
# post thumb
images:
    - "images/post/NzTXEA4zl2E.png"
author: "Brendan Bouffler"
# description
description: ""
video_id: "NzTXEA4zl2E"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon NICE DCV",  "Life Sciences", ]
tags: [ "DCV",  "Covid-19",  "SGE",  "EC2",  "HPC",  "job control",  "GPUs",  "Lustre",  "Slurm",  "API",  "vizualization",  "CPUs",  "virtualization",  "ParallelCluster",  "Schedulers",  "High Performance Computing",  "Storage",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Slurm's job management API, coupled with ParallelCluster's own API for managing cluster infrastructure opens up a lot of doors to create new ways for your users to interact with HPC resources - in this case without having to leave their familiar Jupyter notebook environment.

We made this video as part of the launch of ParallelCluster 3 - we want to make it easy to migrate all your workflows from to Slurm, and we figured it would be easier if you heard abotu it from the source.

So we enlisted the help of SchedMD's Director of Cloud Engineering, Nick Ihli to help us show you how it's a lot easier than it might look.

Joining Nick today is Josiah Bjorgaard from the AWS APN Solution Architecture team, who regularly works with Nick and the team from SchedMD to solve lots of customer problems.

This is the final part of a 5-part series where we covered: 

Part 1) Command line syntax and which Slurm commands map to  familiar SGE ones.
Part 2) Job Scripts - what's the stuff you need to care about to adjust ytour scripts? What's actually easier with Slurm?
Part 3) Array Jobs - Slurm has a really elegant way to handle array jobs, and also has some really nice SGE-like commands that will fool you into thinking nothing actually changed.
Part 4) Job Accounting - everyone who has more than 1 user should look at this, because it'll help you manage what your users are doing, limit what damage they can do, and - most importantly - help you understand how you can tune the experience for them so it's even better.
Part 5) Slurm's API for controlling jobs. Coupled with ParallelCluster's API, you can create some really imaginative solutions for your site. 'Infrastructure as Code' takes on a whole new meaning.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube NzTXEA4zl2E >}}