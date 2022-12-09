---
title: "NCCL on EFA makes the ML world go around in the cloud"
date: 2022-06-30T17:05:07+0000
# post thumb
images:
    - "images/post/kDtHpRB5luw.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "kDtHpRB5luw"
layout: "video"
# Taxonomies
categories: [ "AI/ML",  "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "CPUs",  "DCV",  "EC2",  "EFA",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "ML frameworks",  "MPI",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "bioinformatics",  "cloud computing",  "elastic",  "elastic fabric adapter",  "infiniband",  "machine learning",  "model training",  "mxnet",  "pytorch",  "scientific computing",  "technical computing",  "tensor flow",  "tensorflow",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Machine Learning is a huge workload, and one of the most demanding when it comes to scaling to thousands (and thousands) of CPUs. Some of the largest workloads customers run in the cloud are deep learning models, which require huge numbers of GPUs and saturate the networks connecting them.

To make all that work on AWS, NVIDIA's collectives communications library (NCCL) relies on libfabrics to speak to the EFA hardware that makes up EC2's high performance interconnect.

Rashika Kheria leads the team in Annapurna that handles this interface, ensuring your models, using all your favorite frameworks, scale really nicely to as far as your imagination allows (well, maybe a little further). She came to Tech Shorts to tell us how that works.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube kDtHpRB5luw >}}