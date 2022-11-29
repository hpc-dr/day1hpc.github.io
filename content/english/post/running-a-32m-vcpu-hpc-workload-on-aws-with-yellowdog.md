---
title: "Running a 3.2M vCPU HPC Workload on AWS with YellowDog"
date: 2021-11-23T00:00:00-0800
# post thumb
images:
    - "images/post/hpcblog-102-header-1260x630.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "Life Sciences", ]
tags: [ "HPC",  "Life Sciences",  "Modeling",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

OMass Therapeutics, a biotechnology company identifying medicines against highly validated target ecosystems, used Yellowdog on AWS to analyze and screen 337 million compounds in 7 hours, a task which would have taken two months using an on-premises HPC cluster. YellowDog, based in Bristol in the UK, ran the drug discovery application on an extremely large, multi-region cluster in AWS with the AWS ‘pay-as-you-go’ pricing model. It provided a central, unified interface to monitor and manage AWS Region selection, compute provisioning, job allocation and execution. The entire workload completed in 65 minutes, enabling scientists to start work on analysis the same day, significantly accelerating the drug discovery process. In this post, we’ll discuss the AWS and YellowDog services we deployed, and the mechanisms used to scale to 3.2m vCPUs using multiple EC2 instance types across multiple regions in 33 minutes, running at a 95% utilization rate.

<a href="https://aws.amazon.com/blogs/hpc/running-a-3-2m-vcpu-hpc-workload-on-aws-with-yellowdog/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS HPC Blog</a>