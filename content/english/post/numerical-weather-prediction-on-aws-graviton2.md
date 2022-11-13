---
title: "Numerical weather prediction on AWS Graviton2"
date: 2021-05-10T00:00:00-0700
# post thumb
images:
    - "images/post/wfr-g2-header-1260x630.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "Climate/Environment/Weather",  "AWS ParallelCluster", ]
tags: [ "Simulation",  "HPC",  "Graviton",  "Modeling",  "Arm",  "Climate/Environment/Weather",  "FSx for Lustre",  "Best Practices",  "ParallelCluster",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

The Weather Research and Forecasting (WRF) model is a numerical weather prediction (NWP) system designed to serve both atmospheric research and operational forecasting needs. With the release of Arm-based AWS Graviton2 Amazon Elastic Compute Cloud (EC2) instances, a common question has been how these instances perform on large-scale NWP workloads. In this blog, we will present results from a standard WRF benchmark simulation and compare across three different instance types.

<a href="{{ url }}" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS HPC Blog</a>