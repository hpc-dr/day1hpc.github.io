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

This is what makes DCV a light-weight visualization package that can stream pixels over almost any network. So lean, in fact, that with reasonable bandwidth most users can't tell that the data and the server are hundreds, or sometimes thousands of miles away.

DCV is another example of great tech that was born in HPC, but has expanded to a lot of places we never imagined - including desktop gaming.
## What's behind DCV?

- [Pushing pixels with NICE DCV](https://aws.amazon.com/blogs/hpc/pushing-pixels-with-nice-dcv/) - a short post explaining where DCV came from and how it solves some hard problems in novel ways.
- [Supercomputing visualization good enough for the most demanding gamers](https://youtu.be/_L-U_ET4qrw) - 25min - an insight into some of DCV's tricks (like the QUIC transport layer) that minimize jitter and make the remote desktop feel like it's local. It worked so well, it's now used for gaming.
- [An introduction to DCV](https://youtu.be/-mhNktbKmAc) - 25min - What is DCV, and how is it availble?
- [What's the impact of DCV's pixel streaming on my AWS Bill?](https://youtu.be/-YBh4d_zKxc) - 23min - it turns out to be small, but in this talk, we walk through all the possibilities and use cases, so you know how what to expect.
- [Putting bitrates into perspective](https://aws.amazon.com/blogs/hpc/putting-bitrates-into-perspective/) - a short post on the same topic.

## HPC use for DCV
- [PCluster Manager - A new GUI for building and managing clusters]() - 20min - a chat with Charlie Gruenwald, one of our principal engineers working on AWS ParallelCluster and the force behind PCluster Manager.
- [How Netflix used DCV (and AWS) to distribute their creative workforce (and saved our sanity)](https://youtu.be/PUAeBQ98Odc) - 26min - a talk from Michelle Brenner of Netflix describing how DCV is embedded in their video production workflows (which we all benefit from).
- [Your own VDI solution built with DCV and EnginFrame](https://aws.amazon.com/blogs/hpc/a-vdi-solution-with-enginframe-and-nice-dcv-session-manager-built-with-aws-cdk/) - shows how to set up a fully functional Linux and Windows virtual desktop infrastructure (VDI) that is accessible through a simple web-based user interface.

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

