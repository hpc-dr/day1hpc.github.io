---
title: "Genomics workflow set made easy with AWS Genomics CLI"
date: 2022-03-25T11:29:03+0000
# post thumb
images:
    - "images/post/30cfBPdzykA.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "30cfBPdzykA"
layout: "video"
# Taxonomies
categories: [ "AWS Batch",  "AWS ParallelCluster",  "Amazon NICE DCV",  "Life Sciences", ]
tags: [ "AWS Batch",  "Batch",  "CPUs",  "Covid-19",  "DCV",  "EC2",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "ParallelCluster",  "Schedulers",  "Storage",  "WDL",  "bioinformatics",  "cloud",  "cromwell",  "genomics",  "miniWDL",  "nextflow",  "pipelines",  "snakemake",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

The AWS Genomics CLI (or AGC) seriously removes all the grunt work involved in setting up bioinformatics pipelines to run in the cloud. We know that Snakemake, Cromwell, NextFlow and miniWDL all work happily in the cloud on AWS Batch, but AGC means you don't have to know to set all that stuff up - it does it for you.

You can have completely separate tool chains using completely different workflow languages all running at the same time, on the same infrastructure (if you like), sharing data and tooling.

Lee Pang from the dev team that built this came along to show us how it works, and - most importantly - how easy it is to get productive. Zero to hero in less than 30 mins - it's really impressive. 

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube 30cfBPdzykA >}}