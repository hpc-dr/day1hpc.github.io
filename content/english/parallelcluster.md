---
title: "AWS ParallelCluster"
date: 2022-10-17
author: "Matt Vaughn"
description: "AWS ParallelCluster is an open source tool that makes it easy to deploy and manage HPC clusters on AWS"
layout: "single-notitle"
images:
  - "images/hpc/pc-ident-large.png"
# Taxonomies
categories: ["AWS ParallelCluster"]
tags: ["hpc","products"]
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

{{< image src="/images/hpc/pc-ident-square.png" class="boof" >}}

# AWS ParallelCluster
ParallelCluster is a tool for creating and managing **HPC clusters on AWS,** whether they're powered by x86 CPUs, AWS Gravitons (our Arm-based processors), or powerful GPUs for machine-learning applications.

ParallelCluster brings together advanced **compute, storage and networking** into a *single console*. It adds great features like **desktop visualization** (with [NICE DCV](/dcv)) for any cluster, and [integrates deeply with Slurm](https://docs.aws.amazon.com/parallelcluster/latest/ug/schedulers.slurm.html) to provide cloud-native scaling for all your applications.

ParallelCluster has a graphical interface (and a CLI) to model and control all the resources you need for your HPC applications, and an API you can use for sophisticated management of workflows.

## Deployment

<style>
.boof2 {
  float:right !important;
  width:600px;
  padding: 10px;
  }
</style>
{{< image src="/images/post/pcmanager-sizzle.png" class="boof2" >}}

There are two ways to get ParallelCluster::

1. **We suggest using [PCluster Manager](https://pcluster.cloud/01-getting-started.html)**, which is a visual interface for designing and deploying your clusters. **PCluster Manager** has great features that help you integrate fast filesytems (like Lustre), get one-click desktops connections using NICE DCV, and **controlling your spend** using Slurm Accounting. PCluster Manager can be deployed to your AWS account very quickly, by following the tutorial [here](https://pcluster.cloud/01-getting-started.html).

2. If you're familiar with AWS already, and just want the CLI, you can install it on almost any computer with python installed. The procedure is [documented here](https://docs.aws.amazon.com/parallelcluster/latest/ug/install-v3-parallelcluster.html), but pretty much starts with:

``` bash
$ pip3 install "aws-parallelcluster<3.0" --upgrade --user
```

---

## Learning about ParallelCluster

First, you should make sure you're comfortable that ParallelCluster is the right path for your workloads in AWS. There's a great blog post which helps to explain **[the difference between AWS Batch or AWS ParallelCluster](https://aws.amazon.com/blogs/hpc/choosing-between-batch-or-parallelcluster-for-hpc/)**.

{{< tabs >}}
  {{< tab "Configuration" >}}  
- **[Introducing AWS ParallelCluster 3](https://aws.amazon.com/blogs/hpc/introducing-aws-parallelcluster-3/)** - blog
- [ParallelCluster 3 - built by customers](https://youtu.be/a-99esKLcls) - 17min - Tech Short video with the product team, talking about all the new features of ParallelCluster v3.
- **[PCluster Manager - A new GUI for building and managing clusters](https://youtu.be/Z1vlpJYb1KQ)** - a tour through the management console for ParallelCluster.
- [ParallelCluster 3\'s config file](https://youtu.be/6gAwAK5IJ2w) - a look at the new config file syntax as an example of *infrastructure as code*.
  {{< /tab >}}
  {{< tab "Key Features" >}} 
- **[Introducing AWS ParallelCluster 3](https://aws.amazon.com/blogs/hpc/introducing-aws-parallelcluster-3/)** - a blog describing this new major version of ParallelCluster and it's main features.
- [Multiuser support via Active Directory](https://aws.amazon.com/blogs/hpc/introducing-aws-parallelcluster-multiuser-support-via-active-directory/)
- [Custom AMIs in ParallelCluster 3](https://aws.amazon.com/blogs/hpc/custom-amis-with-parallelcluster-3/)
- [Expanded filesystems support in v3.2](https://aws.amazon.com/blogs/hpc/expanded-filesystems-support-in-aws-parallelcluster-3-2/)
- [Slurm-based memory-aware scheduling](https://aws.amazon.com/blogs/hpc/slurm-based-memory-aware-scheduling-in-aws-parallelcluster-3-2/)
  {{< /tab >}}
{{< /tabs >}}  

## Scheduler Migration

{{< image src="/images/hpc/media-ident-square.png" class="boof" >}}

**Migrating between schedulers** doesn't need to be hard. Since SGE is no longer supported by the community, we worked with the team at [SchedMD](https://www.schedmd.com/) to create a tutorial series to help everyone understand what tools are available in Slurm, to make the shift easier.

There's a blog post with several cheat sheets, and a Tech Shorts series in 4-parts so you can find exactly what you want.

- [Easing your migration from SGE to Slurm in AWS ParallelCluster 3](https://aws.amazon.com/blogs/hpc/easing-your-migration-from-sge-to-slurm-in-aws-parallelcluster-3/)
- [Part 1 - Command Line Tools](https://youtu.be/zCEN4GblrRs)
- [Part 2 - Job Scripts](https://youtu.be/HYMqq0L6fLU)
- [Part 3 - Array Jobs](https://youtu.be/PVO7_fZAT0I)
- [Part 4 - Slurm Accounting](https://youtu.be/TzTIN17CG-s)

## Migration for legacy ParallelCluster v2 customers

- [Infrastructure as code - Understand ParallelCluster 3\'s config](https://youtu.be/6gAwAK5IJ2w)
- [Migrating to AWS ParallelCluster v3 – updated CLI interactions](https://aws.amazon.com/blogs/hpc/aws-parallelcluster-v3-updated-cli/)
- **[ParallelCluster 3 Configuration Converter](https://aws.amazon.com/blogs/hpc/using-the-parallelcluster-3-configuration-converter/)**

## Use cases

ParallelCluster delivers you a canonical Beowulf cluster experience on AWS, but with added twists like elasticity, and support for fast storage and networking, built-in *by design*. That means you can run virtually any workload you like on AWS and expect to see great results.

The tabs here have videos and blog posts describing different use-cases for ParallelCluster.

{{< tabs >}}
  {{< tab "CFD/CAE" >}}  
- [Running large-scale CFD fire simulations on AWS for Amazon.com](https://aws.amazon.com/blogs/hpc/amazon-runs-large-scale-cfd-fire-simulations-on-aws/)
- [Cost-optimization on Spot Instances using checkpoint for Ansys LS-DYNA](https://aws.amazon.com/blogs/hpc/cost-optimization-on-spot-instances-using-checkpoints-for-ansys-ls-dyna/)
  {{< /tab >}}
  {{< tab "Life Sciences" >}}  
- [How Thermo Fisher Scientific Accelerated Cryo-EM using AWS ParallelCluster](https://aws.amazon.com/blogs/hpc/how-thermo-fisher-scientific-accelerated-cryo-em-using-aws-parallelcluster/)
- [Running cost-effective GROMACS simulations using Amazon EC2 Spot Instances with AWS ParallelCluster](https://aws.amazon.com/blogs/hpc/running-gromacs-on-spot-with-checkpointing/)
  {{< /tab >}}
{{< tab "Chemistry" >}}  
- [Quantum Chemistry Calculation with FHI-aims code on AWS](https://aws.amazon.com/blogs/hpc/quantum-chemistry-calculation-on-aws/)
  {{< /tab >}}
{{< tab "Weather/Climate" >}}  
- [Running the Harmonie numerical weather prediction model on AWS](https://aws.amazon.com/blogs/hpc/running-the-harmonie-numerical-weather-prediction-on-aws/)
- [Supporting climate model simulations to accelerate climate science](https://aws.amazon.com/blogs/hpc/supporting-climate-model-simulations-to-accelerate-climate-science/)
- [Numerical weather prediction on AWS Graviton2](https://aws.amazon.com/blogs/hpc/numerical-weather-prediction-on-aws-graviton2/)
  {{< /tab >}}
{{< tab "Quantum Computing" >}}  
- [Simulating 44-Qubit quantum circuits using AWS ParallelCluster](https://aws.amazon.com/blogs/hpc/simulating-44-qubit-quantum-circuits-using-aws-parallelcluster/)
  {{< /tab >}}
{{< /tabs >}}