---
title: "Linking Lustre and object storage - Data repository associations in Amazon FSx"
date: 2024-09-19T13:45:03+0000
# post thumb
images:
    - "images/post/o4Kw7sba_Xc.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "o4Kw7sba_Xc"
layout: "video"
# Taxonomies
categories: [ "AI/ML",  "AWS Batch",  "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "AI/ML",  "AWS",  "Batch",  "CPUs",  "DCV",  "EC2",  "EFA",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "MPI",  "NCCL",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "aws batch",  "bioinformatics",  "cloud computing",  "elastic",  "elastic fabric adapter",  "hpc instances",  "infiniband",  "job scheduling",  "scientific computing",  "supercomputing",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

HPC and machine learning are increasingly being used to solve complex problems, but working with massive datasets can be prohibitively expensive. 

Today's Tech Short shows how to elevate data in S3 into a high speed POSIX filesystem in just two clicks. Simply specify the S3 path and filesystem location to create an association. The entire bucket structure becomes visible as metadata in the filesystem, while the data remains in low-cost S3 storage.

When files are accessed, they are efficiently streamed from S3 on-demand. Pre-loading and caching commands allow optimizing read performance.

If you need to efficiently process huge datasets for HPC, machine learning or other applications, watch this video to see how FSx for Lustre can save you time and money by seamlessly integrating S3 object storage with a high performance filesystem.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by emailing us at ask-hpc@amazon.com.

{{< youtube o4Kw7sba_Xc >}}