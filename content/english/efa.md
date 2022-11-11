---
title: "AWS Elastic Fabric Adapter"
date: 2022-10-17
#author
author: "Brendan Bouffler"
layout: "product"
# description
description: "AWS Elastic Fabric Adapter (EFA) is a high performance networking interface for EC2 instances that enables customers to run applications requiring high levels of inter-node communications at scale on AWS. EC2 instances that enables customers to run applications requiring high levels of inter-node communications at scale on AWS."
images:
  - "images/hpc/efa-ident-large.png"
product_images:
  - "images/hpc/efa-ident-strip.png"
  - "images/hpc/efa-ksp-compute.png"
  - "images/hpc/efa-ksp-performance.png"
  - "images/hpc/efa-ksp-scalable.png"
  - "images/hpc/efa-ksp-familiar.png"
  - "images/hpc/efa-ksp-cloud.png"
# Taxonomies
categories: ["AWS Elastic Fabric Adapter"]
tags: ["networking","HPC"]
type: "featured" # available type (regular or featured)
draft: false
---

The AWS Elastic Fabric Adapter (EFA) is a custom-built high speed network adapter built into dozens (and dozens) of Amazon EC2 instance types. It delivers the same kind of experience as you’d find on a traditional, on-premises, HPC cluster for scaling applications requiring high levels of inter-node communications on AWS.

It's natively supported by [Intel MPI](https://www.intel.com/content/www/us/en/developer/tools/oneapi/mpi-library.html#gs.f1ru48), [Open MPI](https://www.open-mpi.org/), [MVAPICH](https://mvapich.cse.ohio-state.edu/), and [NCCL](https://developer.nvidia.com/nccl) and is available on across CPU and GPU architectures including our own [AWS Graviton processors](https://aws.amazon.com/ec2/graviton/).

### How does it work?

Amazon EC2 compute infrastructure is very much **not** like a ‘normal’ supercomputer (whatever that is). We don’t start with a blank page every few years and design the next big system. It’s a little more like a city where we build on what’s there already, renovate occasionally, and push for bigger and better and faster, while keeping the lights on and the traffic flowing at all times. So we've built this into the **[Scalable Reliable Datagram (SRD)](https://hpc.news/ieeeSRD)**, which underpins EFA's performance.

SRD is different from other HPC datagrams in that it doesn't look for a single fastest path. In a network as large as the one in Amazon EC2, it made sense to exploit as many paths as possible, so SRD swarms the packets over a lot of fast pathways simultaneously. It turns out that most HPC codes are [more sensitive to reliability between communicators than the latency of any one packet](https://aws.amazon.com/blogs/hpc/in-the-search-for-performance-theres-more-than-one-way-to-build-a-network/).

<style>
.boof4 {
  width:300px;
  padding: 10px;
  }
</style>
<a href="https://youtu.be/inJxFXMMp0U" target="2022-10-21-00">{{< image src="/images/hpc/ts-title-what-is-efa.png" class="boof4" >}}</a>
<a href="https://youtu.be/XyllOcIQ_jM" target="2022-10-21-01">{{< image src="/images/hpc/ts-title-how-does-efa-work.png" class="boof4" >}}</a>
<a href="https://hpc.news/ieeeSRD" target="2022-10-21-02">{{< image src="/images/hpc/efa-ieee-picon.png" class="boof4" >}}</a>

<div class="row">
<div class="col">
{{< collapse "**Explore the background design of SRD and EFA**" >}}
<style>
table tr th:empty {
  display: none;
}
table td {
  text-align: center;
}
</style>
| | |
|---|---|
| [There\'s more than one way to build a network](https://aws.amazon.com/blogs/hpc/in-the-search-for-performance-theres-more-than-one-way-to-build-a-network/) | [How does EFA work (in 8 min)?](https://youtu.be/XyllOcIQ_jM) |
| [Scalable Reliable Datagram (SRD)](https://hpc.news/ieeeSRD) | [Deep dive on EFA and SRD with one of EFA\'s designers](https://youtu.be/IgPWzhIHX68) |
{{</ collapse >}}
</div>
</div>

----

### Amazon EC2 Instance Support

In 2021, we began the process of using EFA adapters in [most new Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types). That means there are dozens of instances types that now support EFA. That gives you a lot of options to customize a cluster queue specifically for your workloads.

EFA supports instances using Intel Xeon CPUs, AMD's EPYC Milans, and our own Awrm-based AWS Graviton processors. EFA is also present in a wide variety of accelerated instances, built on technology like  NVIDIA's GPUs, as well as AWS Inferentia and AWS Trainiums.

You can [use the AWS CLI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types) to get a **list of all the instances** that are EFA-capable in any AWS region you're working in.

<div class="row">
<div class="col">
{{< collapse "**Learn more about EFA-supported Amazon EC2 Instances**" >}}
<style>
table tr th:empty {
  display: none;
}
table td {
  text-align: center;
}
</style>
| | |
|---|---|
| [Hpc6a - HPC optimzed, AMD x86_64](https://aws.amazon.com/blogs/aws/new-amazon-ec2-hpc6a-instance-optimized-for-high-performance-computing/) | [C7g Instances - HPC-ready AWS Graviton3](https://aws.amazon.com/about-aws/whats-new/2022/05/amazon-ec2-c7g-instances-powered-aws-graviton3-processors/) |
| [P4de - NVIDIA A100s for ML and HPC](https://aws.amazon.com/about-aws/whats-new/2022/05/amazon-ec2-p4de-gpu-instances-ml-training-hpc/) | [Trn1 - Custom processors tuned for ML training ](https://aws.amazon.com/blogs/aws/amazon-ec2-trn1-instances-for-high-performance-model-training-are-now-available/) |
| [C6i - 3rd Generation Intel Ice Lake](https://aws.amazon.com/about-aws/whats-new/2021/10/amazon-ec2-c6i-instances/) | [M6a - Large-Memory AMD EPYC](https://aws.amazon.com/blogs/aws/new-amazon-ec2-m6a-instances-powered-by-3rd-gen-amd-epyc-processors/) |
{{</ collapse >}}

</div>
</div>

----

### EFA Performance

Customers tell us their workloads scale on EFA the same way they do on-site using traditional interconnects. We see the same thing in the lab, too.

There are several [performance studies](/tags/performance) studies that you'll find on this site covering a wide range of HPC codes.

This area moves fast - especially when new processors are launched by silicon vendors. To stay in touch with this side of what we do, we suggest following [HPC Tech Shorts](https://hpc.news/techshorts) and our [HPC Blog Channel](https://hpc.news/blog). 

<div class="row">
<div class="col">
{{< collapse "**Learn more about EFA's impact on performance**" >}}
<style>
table tr th:empty {
  display: none;
}
table td {
  text-align: center;
}
</style>
| | |
|---|---|
| [Numerical Weather Prediction](https://aws.amazon.com/blogs/hpc/best-price-performance-for-nwp-on-aws/) | [The impact of network conditions on code performance](https://youtu.be/gtQeLmZloJo) |
| [Large-scale CFD fire simulations for Amazon.com](https://aws.amazon.com/blogs/hpc/amazon-runs-large-scale-cfd-fire-simulations-on-aws/) | [Bare metal vs EC2 virtual machines](https://aws.amazon.com/blogs/hpc/bare-metal-performance-with-the-aws-nitro-system/) |
| [Simcenter STAR-CCM+](https://aws.amazon.com/blogs/hpc/simcenter-star-ccm-price-performance-on-aws/) | [GROMACS performance optimizations](https://aws.amazon.com/blogs/hpc/gromacs-price-performance-optimizations-on-aws/) |
{{</ collapse >}}

</div>
</div>

---

### EFA in TV broadcasting - an unexpected use case

In HPC, we're used to the tools and techniques we create flowing into the rest of the industry, solving lots of problems once thought too hard, and unlocking new possibilities for everyone. This is what happened when the team that [looks after Holywood](https://youtu.be/x3zCTVP_LKQ) asked us for help with solving a networking problem.

[This story]](https://aws.amazon.com/blogs/hpc/how-we-enabled-uncompressed-live-video-with-cdi-over-efa/) will take you into the world of broadcast video, and explains why we have EFA enabled on some smaller than normal instance sizes. It started with some difficult problems presented to us by customers in the entertainment industry, and led to an invention called the Cloud Digital Interface (CDI).

## Getting Started with EFA

The fastest - and easiest - way to get started with EFA enabled instances is to use [AWS ParallelCluster](/parallelcluster/), since all the fiddly parts of the software stack and network configuration are done for you. And the easiest way to get started with ParallelCluster is to use PCluster Manager.

However, that won't suit everyone's needs, so there's some resources that will help you with a more specific path if that's what you need.

- **[EFA manual setup guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html)** - if you need to install the EFA stack from scratch yourself, this guide will help you.
* **[EFA section of hpcworkshops.com](https://www.hpcworkshops.com/08-efa.html)** - the same workshops delivered by our Solution Architects every year at SuperComputing and ISC.
* **[Debugging EFA](https://youtu.be/Wq8EMMXsvyo)** - Not seeing the performance you expected? It's possible there's something not working in your software stack, or in your VPC configuration in Amazon EC2. This video will show you how to debug common scenarios to make sure your MPI is running over EFA instead of TCP. The performance difference can be dramatic.