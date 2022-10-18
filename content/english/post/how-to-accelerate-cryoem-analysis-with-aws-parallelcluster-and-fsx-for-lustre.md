---
title: "How to accelerate CryoEM Analysis with AWS ParallelCluster and FSx for Lustre"
date: 2021-03-11T10:55:25+0000
# post thumb
images:
    - "images/post/24QVburwONo.png"
author: "Brendan Bouffler"
# description
description: ""
video_id: "24QVburwONo"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Life Sciences", ]
tags: [ "Lustre",  "CPUs",  "CryoEM",  "High Performance Computing",  "Storage",  "GPUs",  "HPC",  "ParallelCluster",  "EC2",  "Drug Design",  "Schedulers",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

In today’s show, we’re talking about how to choose the right compute and storage elements to get great performance for CryoSPARC, which is one of the popular codes used in cryogenic electron microscopy (CryoEM) analysis.

This is important because, as you’ll hear in the discussion, breaking the pipeline down into different stages and optimizing the infrastructure for each one can speed up the entire workflow, and save a whole lot of money on that compute, too. All these workloads ran on AWS ParallelCluster, which lets you have multiple queues with different instance types and orchestration options (check out last week’s show: https://www.youtube.com/watch?v=C4iSNjcW5O4). ParallelCluster also makes it easy to construct an FSx for Lustre filesystem on the fly using data from an Amazon S3 bucket.

Steve Litster is our Principal HPC business leader for Healthcare and Lifesciences, based out of Boston, and is a recovering x-ray crystallographer (and still has occasional flashbacks of being in a lab). Brian Skjerven is a Sr. HPC Specialist Solutions Architect based in London.

The folks at Structura BioTechnology (https://structura.bio/) who make CryoSPARC are going to publish a deployment guide in the next couple weeks that Brian has helped them create using the performance data he describes in the show.

    It's here:     https://guide.cryosparc.com/deploy/cryosparc-on-aws

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube 24QVburwONo >}}