---
title: "Sending Celery tasks to AWS Batch for heavy lifting"
date: 2023-05-11T12:39:26+0000
# post thumb
images:
    - "images/post/URW0Ngq1suQ.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "URW0Ngq1suQ"
layout: "video"
# Taxonomies
categories: [ "AI/ML",  "AWS ParallelCluster",  "Amazon NICE DCV",  "Elastic Fabric Adapter",  "Life Sciences", ]
tags: [ "CPUs",  "DCV",  "EC2",  "EFA",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "MPI",  "ParallelCluster",  "Schedulers",  "Storage",  "autoscaling",  "bioinformatics",  "celery",  "cloud computing",  "distributed tasks",  "elastic",  "elastic fabric adapter",  "infiniband",  "machine learning",  "scientific computing",  "technical computing",  "tightly-coupled",  "virtualization",  "vizualization",  "web services",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Celery is a great distributed task processing system and gets used in websites and enterprise apps everywhere. But sometimes those tasks aren't little things that can be handled by microservices - they might need some  heavy CPU or machine-learning element that requires some heavy lifting on some dedicated hardware.

That's where Angel's Celery integration for AWS comes in. He blogged about it last week, and came into the Tech Shorts studio to explain how it works, and show it to us in action.

The blog is here: https://aws.amazon.com/blogs/hpc/run-celery-workers-for-compute-intensive-tasks-with-aws-batch/

... and this contains links to his repo on GitHub, too.

You can find Angel on twitter here: https://twitter.com/delagoya if you want to find out more.

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube URW0Ngq1suQ >}}