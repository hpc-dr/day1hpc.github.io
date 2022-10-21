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

## Numerical Weather Prediction

{{< image src="/images/hpc/media-ident-mini.png" position="left" class="boof-blog" >}}

- [An overview of Numerical Weather Prediction (NWP) workloads on AWS HPC-optimized instances](https://aws.amazon.com/blogs/hpc/best-price-performance-for-nwp-on-aws/). We test three popular NWP codes: WRF, MPAS, and FV3GFS on the Hpc6a.

- [NAVGEM on the Cloud: Computational Evaluation of Cloud HPC with a Global Atmospheric Model](https://youtu.be/GTHWf0OVGrw) - Prompted by DoD priorities for modernization, cost savings, and redundancy, this project compared the performance of the NAVGEM on an in-house supercomputer system against several cloud offerings including AWS. This talk was recorded at the HPC User Forum in the fall of 2019.

- [Running the Harmonie weather model  on AWS](https://aws.amazon.com/blogs/hpc/running-the-harmonie-numerical-weather-prediction-on-aws/) - We worked together with the  Danish Meteorological Institute (DMI) to port and run a full numerical weather prediction (NWP) cycling dataflow with the Harmonie Numerical Weather Prediction (NWP) model to AWS.

## The role of AWS Graviton in Weather

<style>
.boof-video {
  float:right !important;
  width:400px;
  padding: 10px;
  }
</style>

{{< image src="/images/post/ts-title-wrf-on-graviton2.png" class="boof-video" >}}

- [Arm a world-leading forecast model with AWS Graviton and Lambda](https://aws.amazon.com/blogs/hpc/how-to-arm-a-world-leading-forecast-model-with-aws-graviton-and-lambda/) - the UK MetOffice is a a well-recognized scientific leader in weather, climate and environmental forecasts and severe weather warnings for the protection of life and property. They describe their experience of gathering their SurfaceNet data gathering of over 1 billion observations a year using AWS Lamba and their switch to using AWS Graviton.
- Numerical weather prediction on AWS Graviton2 - **[[Blog]](https://aws.amazon.com/blogs/hpc/numerical-weather-prediction-on-aws-graviton2/) [[Video]](https://youtu.be/D2ppdRKSz5I)** - an exploration of how WRF performs on AWS Graviton2, delivering suprising performance results.

## Cloud as a training tool

- [Training forecasters to warn severe hazardous weather on AWS](https://aws.amazon.com/blogs/hpc/training-forecasters-to-warn-severe-hazardous-weather-on-aws/)

