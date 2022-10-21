---
title: "AWS Elastic Fabric Adapter"
date: 2022-10-17
#author
author: "Brendan Bouffler"
layout: "single-notitle"
# description
description: "AWS Elastic Fabric Adapter (EFA) is a high performance networking interface for EC2 instances that enables customers to run applications requiring high levels of inter-node communications at scale on AWS. EC2 instances that enables customers to run applications requiring high levels of inter-node communications at scale on AWS."
images:
  - "images/hpc/efa-ident-large.png"
# Taxonomies
categories: ["EFA"]
tags: ["networking","HPC"]
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

{{< image src="/images/hpc/efa-ident-square.png" class="boof" >}}

# Elastic Fabric Adapter (EFA)

The AWS Elastic Fabric Adapter (EFA) is a high-performance networking interface for Amazon EC2 instances that enables you to run applications requiring high levels of inter-node communications at scale on AWS.

It's natively supported by [Intel MPI](https://www.intel.com/content/www/us/en/developer/tools/oneapi/mpi-library.html#gs.f1ru48), [Open MPI](https://www.open-mpi.org/), [MVAPICH](https://mvapich.cse.ohio-state.edu/), and [NCCL](https://developer.nvidia.com/nccl) and is available on across CPU and GPU architectures including our own [AWS Graviton processors](https://aws.amazon.com/ec2/graviton/).

## How does it work?

Amazon EC2 compute infrastructure is very much **not** like a ‘normal’ supercomputer (whatever that is). We don’t start with a blank page every few years and design the next big system. It’s a little more like a city where we build on what’s there already, renovate occasionally, and push for bigger and better and faster, while keeping the lights on and the traffic flowing at all times.

While this leads to different design decisions, it also leads to **interesting discoveries**. It turns out that most HPC codes are more sensitive to networks that can deliver large amounts of data reliability and quickly between communicators. And they're **[far less sensitive to individual packet latency](https://aws.amazon.com/blogs/hpc/in-the-search-for-performance-theres-more-than-one-way-to-build-a-network/)** than we all thought.

EFA is a great example of how we've been able to keep packets flowing *and* solve some complex problems HPC users face in a novel way - without losing any performance for HPC and ML applications.

<style>
.boof3 {
  float:right !important;
  width:250px;
  padding: 10px;
  }
</style>

{{< image src="/images/hpc/media-ident-square.png" class="boof3" >}}

<style>
.boof4 {
  width:350px;
  padding: 10px;
  }
</style>
<a href="https://youtu.be/inJxFXMMp0U" target="2022-10-21-00">{{< image src="/images/hpc/ts-title-what-is-efa.png" class="boof4" >}}</a>
<a href="https://youtu.be/inJxFXMMp0U" target="2022-10-21-00">{{< image src="/images/hpc/ts-title-how-does-efa-work.png" class="boof4" >}}</a>

---
## Deeper Dive
{{< tabs >}}
  {{< tab "Tech Specs" >}}
- **[EFA-enabled Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types)** - there are dozens of instances types that now support EFA. That gives you a lot of options to customize a cluster queue specifically for your workloads.
- **[A paper at IEEE Spectrum about EFA and SRD](https://hpc.news/ieeeSRD)** - a deep dive into the design decisions and characteristics of EFA and SRD.
- **[EFA manual setup guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html)** - if you need to install the EFA stack from scratch yourself, this guide will help you.
  {{< /tab >}}
  {{< tab "Blog Posts" >}}
* **[There\'s more than one way to build a network](https://aws.amazon.com/blogs/hpc/in-the-search-for-performance-theres-more-than-one-way-to-build-a-network/)** - blog post explaining many of the EFA design decisions.
* **[EFA has gone mainstream](https://aws.amazon.com/blogs/hpc/efa-is-now-mainstream/)** - Most new Amazon EC2 instance families carry EFA-enabled interfaces.
  {{< /tab >}}
  {{< tab "Video explainers" >}}
* **[Deep dive on EFA and SRD](https://youtu.be/IgPWzhIHX68)** - 36 mins - A deep dive with one of our Principal Engineers into the thought process and design decisions that lead to EFA.
* **[Speeds\'n\'Feeds Event](https://youtu.be/YjS0e4g7zk0)** - 10-mins - a fast-paced EFA update from January '22 on all the latest news and developments in EFA and - especially - new instance support.
* **[NCCL on EFA](https://youtu.be/kDtHpRB5luw)** - 15m - An insight into how **machine learning** workloads are supported on EFA from the engineering team who support the libfabric interface to NCCL.
  {{< /tab >}}
  {{< tab "Getting Started" >}}
* [EFA section of hpcworkshops.com](https://www.hpcworkshops.com/08-efa.html) - the same workshops delivered by our Solution Architects every year at SuperComputing and ISC.
* [How to make sure you\'re job is using EFA](https://youtu.be/Wq8EMMXsvyo) - How to debug scenarios where you're not sure if your MPI is running over EFA or TCP. The performance difference can be dramatic, so these simple steps will help you figure it out.
  {{< /tab >}}
{{< /tabs >}}

## EFA Performance

Customers tell us their workloads scale on EFA the same way they do on-site using traditional interconnects. We see the same thing in the lab, too.

There are a number of [performance studies](/tags/performance) studies covering a wide range of HPC codes. To stay in touch with this side of what we do, we suggest following [HPC Tech Shorts](https://hpc.news/techshorts) and our [HPC Blog Channel](https://hpc.news/blog).

* [Numerical Weather Prediction](https://aws.amazon.com/blogs/hpc/best-price-performance-for-nwp-on-aws/)
* [Large-scale CFD fire simulations for Amazon.com](https://aws.amazon.com/blogs/hpc/amazon-runs-large-scale-cfd-fire-simulations-on-aws/)
* [Scaling CFD by breaking down a workflow, to speed it up](https://youtu.be/F8YzcuYr7YI)
* [Simcenter STAR-CCM+](https://aws.amazon.com/blogs/hpc/simcenter-star-ccm-price-performance-on-aws/)
* [GROMACS performance optimizations](https://aws.amazon.com/blogs/hpc/gromacs-price-performance-optimizations-on-aws/)
* [The impact of network conditions on application performance is complicated](https://youtu.be/gtQeLmZloJo)

## EFA in TV broadcasting - an unexpected use case

In HPC, we're used to the tools and techniques we create flowing into the rest of the industry, solving lots of problems once thought too hard, and unlocking new possibilities for everyone. This is what happened when the team thaty looks after Holywood asked us for help with solving a networking problem.

This story will take you into the world of broadcast video, andf explains why we have EFA enabled on some smaller than normal instance sizes. It started with some difficult problems presented to us by customers in the entertainment industry, and led to an invention called the Cloud Digital Interface (CDI).

* [How EFA enables uncompressed live video for TV broadcast](https://aws.amazon.com/blogs/hpc/how-we-enabled-uncompressed-live-video-with-cdi-over-efa/)
* [What supercomputers, scientists and TV stations have in common](https://youtu.be/x3zCTVP_LKQ) - 13min - background on why this problem exists in broadcast.
