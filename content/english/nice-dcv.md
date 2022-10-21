---
title: "NICE DCV"
date: 2022-10-17
#author
author: "Brendan Bouffler"
layout: "single-notitle"
# description
description: "NICE DCV is a high performance, low latency pixel streaming protocol that encrypts and transports pixels to devices, putting your desktop closer to your results. You can access, manipulate, and share business-critical information, regardless of your location, over local networks or the internet."
images:
  - "images/post/DCV.png"
# Taxonomies
categories: ["products"]
tags: ["streaming","visualization"]
type: "featured" # available type (regular or featured)
draft: false
---

<style>
.boof {
  float:right !important;
  width:350px;
  padding: 10px;
  }
</style>

{{< image src="/images/hpc/dcv-ident-square.png" class="boof" >}}

# NICE DCV

NICE DCV is a high performance, low latency pixel streaming protocol that encrypts and transports pixels to devices, putting your desktop closer to your results. You can access, manipulate, and share business-critical information, regardless of your location, over local networks or the internet.

DCV makes *very* frugal use of scarce bandwidth, because it's super-lean, uses data-compression techniques and has always quickly adopted cutting-edge technologies (this is HPC, after all, we leave nothing on the table when it came to exploiting new gadgets).

## A desktop ... in a web browser?

DCV also has a Web SDK which means you can offer your end users virtual desktops embedded in browser tabs (check out the [talk from Netflix](https://youtu.be/PUAeBQ98Odc) about how they did just that for their global network of editors).

All of this is what makes DCV a light-weight visualization package that can stream pixels over almost any network. So lean, in fact, that with reasonable bandwidth most users can't tell that the data and the server are hundreds, or sometimes thousands of miles away.

## What's behind DCV?

DCV is another example of great tech that was born in HPC, but has expanded to a lot of places we never imagined - including desktop gaming.

<style>
.boof3 {
  float:right !important;
  width:350px;
  padding: 10px;
  }
</style>

{{< image src="/images/hpc/media-ident-square.png" class="boof3" >}}

- **[Pushing pixels with NICE DCV](https://aws.amazon.com/blogs/hpc/pushing-pixels-with-nice-dcv/)** - a short post explaining where DCV came from and how it solves some hard problems in novel ways.
- **[Supercomputing visualization good enough for the most demanding gamers](https://youtu.be/_L-U_ET4qrw)** - 25min - an insight into some of DCV's tricks (like the QUIC transport layer) that minimize jitter and make the remote desktop feel like it's local. It worked so well, it's now used for gaming.
- **[An introduction to DCV](https://youtu.be/-mhNktbKmAc)** - 25min - What is DCV, and how is it availble?
- **What's the impact of DCV\'s pixel streaming on my AWS Bill?** - **[[Video 23min]](https://youtu.be/-YBh4d_zKxc)** || **[[Blog Post]](https://aws.amazon.com/blogs/hpc/putting-bitrates-into-perspective/)** - it turns out to be small, but in this talk, we walk through all the possibilities and use cases, so you know how what to expect.

## HPC use for DCV
- **[PCluster Manager - A new GUI for building and managing clusters](https://youtu.be/PChP3FQWeJQ)** - 20min - a chat with Sean Smith showing us how to use PCluster Manager to design and build a cluster.
- **[How Netflix used DCV (and AWS) to distribute their creative workforce (and saved our sanity)](https://youtu.be/PUAeBQ98Odc)** - 26min - a talk from Michelle Brenner of Netflix describing how DCV is embedded in their video production workflows (which we all benefit from).

## DCV in gaming

<style>
.screenshot {
  float:right !important;
  width:500px;
  padding: 10px;
  }
</style>

{{< image src="/images/post/dcv-gamers-screenshot-1.png" class="screenshot" >}}

Most of the techniques that DCV uses to minimize the effects of internet jitter and unpredictable latency, work really well for cloud gaming, too.

- **[Pushing pixels with NICE DCV](https://aws.amazon.com/blogs/hpc/pushing-pixels-with-nice-dcv/)** - a short post explaining where DCV came from and how it solves some hard problems in novel ways.
- **[Supercomputing visualization good enough for the most demanding gamers](https://youtu.be/_L-U_ET4qrw)** - 25min - an insight into some of DCV's tricks (like the QUIC transport layer) that minimize jitter and make the remote desktop feel like it's local. It worked so well, it's now used for gaming.

## Getting started with DCV

It's easy to get started with DCV:

1. **[DCV Preconfigured AMI](https://aws.amazon.com/marketplace/seller-profile?id=74eff437-1315-4130-8b04-27da3fa01de1)** - this AMI is in AWS Marketplace, and is available for Windows and Linux server versions - includiong options for G4 and G5 Amazon EC2 instances, which are GPU enabled. 
2. **[Preconfigured DCV EC2 instance with CloudFormation](https://download.nice-dcv.com/cloudformation.html)** - you can launch using an AWS CloudFormation template, which we provide.
3. **[Install DCV Manually](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up.html)** - you can install manually, which makes more sense if you're plannign to use DCV in a more taylored configuration.
