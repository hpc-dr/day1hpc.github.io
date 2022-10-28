---
title: "Climate/Environment/Weather on AWS HPC"
date: 2022-10-01
#author
author: "Matt Vaughn"
layout: "single-notitle"
# description
description: "AWS is a great place for your Climate/Environment/Weather HPC needs."
images:
  - "images/hpc/efa-ident-large.png"
# Taxonomies
categories: []
tags: ["climate/environment/weather"]
type: "regular" # available type (regular or featured)
draft: false
---

<style>
.boof-weather {
  float:center !important;
  width:1110px;
  padding: 10px;
  }
</style>

{{< image src="/images/hpc/weather-ident-large.png" position="center" class="boof-weather" >}}

## Learn about climate, environment, and weather on AWS HPC

Weather simulation is a reliably difficult workload for almost any HPC architecture and is often used as a litmus test by many customers before they look at a novel technologies or different systems. Customers have asked us frequently about our performance, and that’s been even more the case since we launched the [Elastic Fabric  Adapter](/efa/) and several new HPC-oriented instance families.

The Hpc6a is built on AMD's Milan, and the [AWS Graviton](https://aws.amazon.com/ec2/graviton/) is our Arm64-based processor. Both perform excellently with a variety of weather and climate codes, as you can see in the blog posts, videos and discussions linked on this page.

<style>
.boof-blog {
  float:right !important;
  width:200px;
  padding: 10px;
  }
</style>

## Numerical weather prediction (NWP) codes

{{< image src="/images/hpc/media-ident-mini.png" position="left" class="boof-blog" >}}

- [An overview of Numerical Weather Prediction (NWP) workloads on AWS HPC-optimized instances](https://aws.amazon.com/blogs/hpc/best-price-performance-for-nwp-on-aws/). We test three popular NWP codes: WRF, MPAS, and FV3GFS on the Hpc6a **(Blog)**.

- [NAVGEM on the Cloud: Computational Evaluation of Cloud HPC with a Global Atmospheric Model](https://youtu.be/GTHWf0OVGrw) - A talk from the HPC User Forum about a project comparing the performance of the NAVGEM on an in-house supercomputer system against several cloud offerings including AWS. **(Video, Fall 2019)**.

- [Running the Harmonie weather model  on AWS](https://aws.amazon.com/blogs/hpc/running-the-harmonie-numerical-weather-prediction-on-aws/) - the Danish Meteorological Institute (DMI) ported and ran their full cycling dataflow with the Harmonie model on AWS **(Blog)**.

- [Training forecasters to warn severe hazardous weather on AWS](https://aws.amazon.com/blogs/hpc/training-forecasters-to-warn-severe-hazardous-weather-on-aws/) **(Blog)**.

## The impact of AWS Graviton in modeling

<style>
.boof-video {
  float:right !important;
  width:350px;
  padding: 10px;
  }
</style>

{{< image src="/images/post/ts-title-wrf-on-graviton2.png" class="boof-video" >}}

- WRF Performance on AWS Graviton2 - **[(Blog](https://aws.amazon.com/blogs/hpc/numerical-weather-prediction-on-aws-graviton2/) || [Video)](https://youtu.be/D2ppdRKSz5I)** - an exploration of how **WRF** performs on AWS Graviton2, delivering suprising performance results.
- [Arm a world-leading forecast model with AWS Graviton and Lambda](https://aws.amazon.com/blogs/hpc/how-to-arm-a-world-leading-forecast-model-with-aws-graviton-and-lambda/) - the UK MetOffice describe their experience of gathering their SurfaceNet data gathering of over 1 billion observations a year using AWS Lamba and their switch to using AWS Graviton **(Blog)**.

## Getting hands on (with help) in a workshop

<style>
.boof-ws {
  float:left !important;
  width:500px;
  padding: 5px;
  }
</style>

{{< image src="/images/hpc/ws-nwp-large.png" class="boof-ws" >}}

**[These workshops](https://weather.hpcworkshops.com/)** lead you through getting started with AWS ParallelCluster including installation and use of WRF, MPAS, and Unified Forecase System FV3GFS. **[(Workshop)](https://weather.hpcworkshops.com/)**

You can work through them in your own AWS account, or use them in a class-room scenario for a group.
