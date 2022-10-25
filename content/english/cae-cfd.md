---
title: "CAE/CFD on AWS HPC"
date: 2022-10-01
#author
author: "Matt Vaughn"
layout: "single-notitle"
# description
description: "AWS is a great place for your CAE/CFD HPC needs."
images:
  - "images/hpc/efa-ident-large.png"
# Taxonomies
categories: []
tags: ["cae/cfd"]
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

{{< image src="/images/hpc/cfd-ident-large.png" position="center" class="boof-weather" >}}

## Running engineering workloads on AWS lets iterate through your design space *fast*

That's because Amazon EC2 isn't just fast - it's super-versatile. More than 500 compute instance types means you can match each elements of your pipeline to exactly the right compute. When you're able to tune every element like this, everything gets faster and you save money not having hardware idle waiting for another part of the pipeline.

Some key pieces of technology make this possible.

- **Amazon EC2** provides the raw compute resources, like CPUs, GPUs and memory.
- **FSx for Lustre** and **FSx for OpenZFS** high-speed parallel filesystems that safely store all your data in whatever form you need it.
- **Elastic Fabric Adapter** connects every piece with an network designed for scientific, engineering, and machine learning workloads.

Finally, **AWS ParallelCluster brings all of this together** into clusters you can easily create, scale, duplicate and retire - all inside your security perimeter.

<style>
.boof-blog {
  float:right !important;
  width:200;
  padding: 10px;
  }
</style>

{{< image src="/images/hpc/ws-strap-mini.png" class="boof-blog" >}}

- [Getting the best OpenFOAM Performance on AWS](https://aws.amazon.com/blogs/hpc/getting-the-best-openfoam-performance-on-aws/)
- [Running large-scale CFD fire simulations on AWS for Amazon.com](https://aws.amazon.com/blogs/hpc/amazon-runs-large-scale-cfd-fire-simulations-on-aws/)
- [Simcenter STAR-CCM+ price-performance on AWS](https://aws.amazon.com/blogs/hpc/simcenter-star-ccm-price-performance-on-aws/)

- [EFA is now mainstream, and that’s a Good Thing | AWS HPC Blog](https://aws.amazon.com/blogs/hpc/efa-is-now-mainstream/)
- [New: Introducing AWS ParallelCluster 3 | AWS HPC Blog](https://aws.amazon.com/blogs/hpc/introducing-aws-parallelcluster-3/)

- [Running finite element analysis using Simcenter Nastran on AWS | AWS HPC Blog](https://aws.amazon.com/blogs/hpc/running-finite-element-analysis-using-simcenter-nastran-on-aws/)
- [Cost-optimization on Spot Instances using checkpoint for Ansys LS-DYNA | AWS HPC Blog](https://aws.amazon.com/blogs/hpc/cost-optimization-on-spot-instances-using-checkpoints-for-ansys-ls-dyna/)
- [Accelerate Computer-Aided Engineering Workloads with Hybrid Cloud HPC Scenarios](https://aws.amazon.com/blogs/apn/accelerate-computer-aided-engineering-workloads-with-hybrid-cloud-hpc-scenarios/)
- [The America's Cup And INEOS TEAM UK - BBC Click](https://www.youtube.com/watch?v=yLc5qsJVu5U)

- [CFD on AWS graviton2 CPUs - early results](https://youtu.be/4WgE472wIqU)
- **CFD performance on Ice Lake CPU with the Amazon EC2 C6i** - [Part 1](https://youtu.be/9w9-KhZLOnU) || [Part 2](https://youtu.be/F8YzcuYr7YI)

# Getting hands on, with help

The HPC team 
**[Running Hexagon CAE applications](https://catalog.workshops.aws/cae-hexagon)**	The purpose of this workshop is to help you to run your Hexagon (MSC) applications on AWS. We’ll go from creating the HPC cluster using AWS ParallelCluster, to the installation of the codes such as Cradle CFD, MSC Nastran, Marc, Actran, Simufact etc. and finally example submission scripts for you to run your own cases.	