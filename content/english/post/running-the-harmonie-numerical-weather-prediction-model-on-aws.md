---
title: "Running the Harmonie numerical weather prediction model on AWS"
date: 2021-09-30T00:00:00-0700
# post thumb
images:
    - "images/post/harmonie-header-1260x630.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "Climate/Environment/Weather",  "AWS ParallelCluster", ]
tags: [ "Modeling",  "HPC",  "Climate/Environment/Weather",  "ParallelCluster",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

The Danish Meteorological Institute (DMI) is responsible for running atmospheric, climate and ocean models covering the kingdom of Denmark. We worked together with the DMI to port and run a full numerical weather prediction (NWP) cycling dataflow with the Harmonie Numerical Weather Prediction (NWP) model to AWS. You can find a report of the porting and operational experience in the ACCORD community newsletter. In this blog post, we expand on that report to present the initial timing results from running the forecast component of Harmonie model on AWS. We also present these as-is timing results together with as-is timings attained on the supercomputing systems based on Cray XC40 and Intel Xeon based Cray XC50.

<a href="https://aws.amazon.com/blogs/hpc/running-the-harmonie-numerical-weather-prediction-on-aws/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS Blog Channel</a>