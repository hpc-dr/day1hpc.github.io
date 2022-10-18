---
title: "Bayesian models and half a million cores - what're you waiting for?"
date: 2022-06-24T14:59:17+0000
# post thumb
images:
    - "images/post/CcqeeRyx93k.png"
author: "Brendan Bouffler"
# description
description: ""
video_id: "CcqeeRyx93k"
# Taxonomies
categories: [ "AI/ML",  "AWS ParallelCluster",  "Amazon Elastic Fabric Adapter",  "Amazon NICE DCV",  "Life Sciences", ]
tags: [ "bioinformatics",  "technical computing",  "infiniband",  "MPI",  "advertising",  "vizualization",  "Ampersand",  "tightly-coupled",  "High Performance Computing",  "Storage",  "GPUs",  "TV",  "EFA",  "virtualization",  "Lustre",  "ML models",  "CPUs",  "HPDA",  "elastic fabric adapter",  "hidden markov models",  "ParallelCluster",  "Schedulers",  "analytics",  "elastic",  "autoscaling",  "DCV",  "HPC",  "scientific computing",  "Bayesian",  "cloud computing",  "EC2",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

The Ampersand Data Science team had a challenge: their Bayesian statistical models needed more than half a million core-hours of runtime, regularly, if they were to get an answer fast enough for it to be useful to their customers.

Scaling to a million core or more isn't really a challenge now (thanks to Amazon EC2). The hard part is all the code pipelines and plumbing - and the management of the entire thing when it's in flight.

Daniel Gerlanc (Senior Director for Data Science) and Jeffrey Enos (Senior Machine Learning Engineer) swung by the Tech Shorts virtual watercooler to tell us how it worked, what was most surprising, and which bits made all the difference.

There's also a blog that was posted last week which talks to some of this too. Worth a read: https://aws.amazon.com/blogs/hpc/bayesian-ml-models-at-scale-with-aws-batch/

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube CcqeeRyx93k >}}