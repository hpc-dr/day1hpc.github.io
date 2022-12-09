---
title: "Controlling hybrid workflows between on-premises and cloud with EnginFrame"
date: 2022-03-31T20:54:58+0000
# post thumb
images:
    - "images/post/a6R0FqsYGy0.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "a6R0FqsYGy0"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon NICE DCV",  "Life Sciences", ]
tags: [ "CPUs",  "Covid-19",  "DCV",  "EC2",  "EnginFrame",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "ParallelCluster",  "Schedulers",  "Storage",  "cloud",  "hybrid",  "on-prem",  "on-premises",  "scripting",  "slurm",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

EnginFrame makes life easy for scientists and engineers so they can use HPC resources without having to understand the complexity.

BUT: EnginFrame also makes the local sysadmin a hero by giving them the ability to embed into simple scripts the decisions that lead to determining how and where and when a job gets run.

The use cases are almost endless:

* decide whether your job bursts to the cloud based on congestion conditions in your on--prem queues
* figure out if data needs to be moved first before a job can be run
* decide based on job parameters whether a job is fit for execution in the AWS spot market, or should be run on-prem, or run in on-demand queues.

The workshop we discussed is here: https://hpc.news/efConnectorWorkshop

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube a6R0FqsYGy0 >}}