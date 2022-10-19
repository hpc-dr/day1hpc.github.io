---
title: "NCCL on EFA makes the ML world go around in the cloud"
date: 2022-06-30T17:05:07+0000
# post thumb
images:
    - "images/post/kDtHpRB5luw.png"
author: "Brendan Bouffler"
# description
description: ""
video_id: "kDtHpRB5luw"
# Taxonomies
categories: [ "AI/ML",  "AWS ParallelCluster",  "Amazon Elastic Fabric Adapter",  "Amazon NICE DCV",  "Life Sciences", ]
tags: [ "bioinformatics",  "technical computing",  "infiniband",  "tensorflow",  "model training",  "MPI",  "vizualization",  "tightly-coupled",  "High Performance Computing",  "Storage",  "GPUs",  "EFA",  "virtualization",  "machine learning",  "Lustre",  "pytorch",  "CPUs",  "elastic fabric adapter",  "ParallelCluster",  "mxnet",  "Schedulers",  "ML frameworks",  "elastic",  "autoscaling",  "DCV",  "tensor flow",  "HPC",  "scientific computing",  "cloud computing",  "EC2",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Machine Learning is a huge workload, and one of the most demanding when it comes to scaling to thousands (and thousands) of CPUs. Some of the largest workloads customers run in the cloud are deep learning models, which require huge numbers of GPUs and saturate the networks connecting them.

To make all that work on AWS, NVIDIA's collectives communications library (NCCL) relies on libfabrics to speak to the EFA hardware that makes up EC2's high performance interconnect.

Rashika Kheria leads the team in Annapurna that handles this interface, ensuring your models, using all your favorite frameworks, scale really nicely to as far as your imagination allows (well, maybe a little further). She came to Tech Shorts to tell us how that works.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube kDtHpRB5luw >}}