---
title: "AWS Batch now supports Kubernetes using Amazon EKS"
date: 2022-10-25T13:57:30+0000
# post thumb
images:
    - "images/post/su5gGg8A1H8.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "su5gGg8A1H8"
layout: "video"
# Taxonomies
categories: [ "AWS Batch",  "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "AWS Batch",  "Amazon EKS",  "CPUs",  "DCV",  "EC2",  "EFA",  "Elastic Kubernetes Service",  "GPUs",  "HPC",  "High Performance Computing",  "KubeCon",  "Kubernetes",  "Lustre",  "MPI",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "batch",  "bioinformatics",  "cloud computing",  "containers",  "elastic",  "elastic fabric adapter",  "infiniband",  "scientific computing",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Since it was launched in 2017, AWS Batch has used the Amazon Elastic Container Service (Amazon ECS) to create the clusters it uses for deploying container jobs. That included AWS Fargate, which is a serverless face to ECS.

But starting today, AWS Batch now supports Kubernetes via the Amazon Elastic Kubernetes Service (Amazon EKS). This is great news for the thousands (and thousands) of customers who use K8s for their enterprise workloads, built on zillions of micro services, managed by EKS.

It's also great news for Kubernetes, since there's now a rich, reliable and cloud-native service for running massive volumes of asynchronous workloads in huge batches.

Angel Pizarro, our Principal Dev Advocate for AWS Batch, joins Naina Thangaraj our Snr Product Manager for AWS Batch to discuss the details.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube su5gGg8A1H8 >}}