---
title: "Price-Performance Analysis of Amazon EC2 GPU Instance Types using NVIDIA’s GPU optimized seismic code"
date: 2021-08-12T00:00:00-0700
# post thumb
images:
    - "images/post/hpc-blog-header-price-perf-1-1260x630.png"
#author
author: "Matt Vaughn"
# description
description: ""
# Taxonomies
categories: []
tags: [ "Modeling",  "Energy",  "HPC",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

Seismic imaging is the process of positioning the Earth’s subsurface reflectors. It transforms the seismic data recorded in time at the Earth’s surface to an image of the Earth’s subsurface. This is done by back-propagating data from time to space in a given velocity model. Kirchhoff depth migration is a well-known technique used in geophysics for seismic imaging. Kirchhoff time and depth migration produce an image with higher resolution and generate an image of the subsurface for a subset class of the data, providing valuable information about the petrophysical properties of the rocks and helps to determine how accurate the velocity model is. This blog post looks at the price-performance characteristics computing Kirchhoff migration methods on GPUs using Nvidia’s GPU-optimized code.

Read the full post at the [AWS HPC Blog](https://aws.amazon.com/blogs/hpc/price-performance-analysis-of-gpu-instance-types-using-nvidias-gpu-optimized-seismic-code/).
