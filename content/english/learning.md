---
title: "Learning pathways to the cloud"
date: 2022-11-13
#author
author: "Brendan Bouffler"
layout: "single-notitle"
# description
description: "AWS is a great place for your Life Sciences HPC needs."
images:
  - "images/hpc/Ident-Learning@3x.webp"
# Taxonomies
categories: []
tags: ["life-sciences"]
type: "featured" # available type (regular or featured)
draft: false
---

<style>
.boof-weather {
  float:center !important;
  width:1110px;
  padding: 0px;
  }
</style>

{{< image src="/images/hpc/Ident-Learning@3x.webp" position="center" class="boof-weather" >}}

## Navigating your way into AWS

We get it - there are too many things going on in AWS that if you haven't been following from the beginning, it's daunting to know where to start. We've put material together to help you bridge the knowledge gap. To get high level knowledge of AWS, so you can bust through the jargon and get on top of the most important concepts, we've created a set of short videos in our YouTube channel - **[HPC Tech Shorts](https://hpc.news/techshorts)** to get started with.

Workshops dive deeper, and will get you hands-on with the tools to build some practical working clusters. 

## HPC Tech Shorts Foundations

The [HPC Tech Shorts](https://hpc.news/techshorts) channel releases new shows each week, including a subset dedicated for addressing foundational topics about HPC in the cloud. Consider subscribing to the channel so you get updates as new content is released.

<style>
.learn {
  width:350px;
  padding: 0px;
  }
</style>

### Intro to AWS

<a href="https://youtu.be/KHx22oJSNso">{{< image src="/images/tsf/tsf-getting-familiar.png" class="learn" >}}</a>
<a href="https://youtu.be/9eZ-53klGoE">{{< image src="/images/post/9eZ-53klGoE.png" class="learn" >}}</a>

----

### Understanding Amazon EC2 and EFA

<a href="https://youtu.be/1y5Ix2HS8sw">{{< image src="/images/tsf/tsf-understanding-ec2.png" class="learn" >}}</a>
<a target="2022-10-28" href="https://youtu.be/inJxFXMMp0U">{{< image src="/images/tsf/tsf-what-is-efa.png" class="learn" >}}</a>
<a href="https://youtu.be/XyllOcIQ_jM">{{< image src="/images/tsf/tsf-how-does-efa-work.png" class="learn" >}}</a>

### HPC clusters and job management

<a href="https://youtu.be/gmw7A3kOh60">{{< image src="/images/tsf/tsf-what-is-pc.png" class="learn" >}}</a>
<a href="https://youtu.be/24tBOQDAyUA">{{< image src="/images/tsf/tsf-what-is-batch.png" class="learn" >}}</a>
<a href="https://youtu.be/9eZ-53klGoE">{{< image src="/images/post/9eZ-53klGoE.png" class="learn" >}}</a>

#### Elements of cluster design

<a href="https://youtu.be/cGaBaxDR9Qo">{{< image src="/images/post/cGaBaxDR9Qo.png" class="learn" >}}</a>
<a href="https://youtu.be/h72NVKYru0Y">{{< image src="/images/post/h72NVKYru0Y.png" class="learn" >}}</a>
---

<style>
.ws {
  float:right !important;
  width:550px;
  padding: 0px;
  }
</style>

## Hands-on Workshops

{{< image src="/images/hpc/hpcworkshops-dot-com@3x.webp" class="ws" >}}

Our solution architect teams conduct a lot of HPC training throughout the year, and the content here draws from that.

There are two primary groups of workshops:

1. **Whole Day Workshops** - the content we use for delivering workshops at large events like SuperComputing and ISC, in the tutorial tracks. This content is designed for a whole day of immersion, with AWS instructors on-hand to answer questions and help you debug. it lives at **[hpcworkshops.com](https://hpcworkshops.com)**.
2. **Specific topics** - these workshops often drill down into a specific task you might want to accomplish, like '*standing up my favorite CFD code on a cluster in the cloud*'.

## AWS ParallelCluster workshops
| Workshop  | Description  |
| :----------- | :-------------|
| **[AWS Immersion Day - High Performance Computing track](https://catalog.us-east-1.prod.workshops.aws/workshops/f5746dfb-de90-45cb-bf5c-d05419a20dae)** | Setup process of creating your first HPC cluster on AWS. You will use AWS ParallelCluster 3 to do so, and you will see how it deploys services such as Amazon EC2 with Elastic Fabric Adapter, Amazon Elastic Block Store and Amazon FSx for Lustre. Also covers examples of using the cluster for CFD with OpenFOAM and molecular dynamics with LAMMPS. |
| **[Running CFD on AWS ParallelCluster](https://catalog.us-east-1.prod.workshops.aws/workshops/21c996a7-8ec9-42a5-9fd6-00949d151bc2)**|  The purpose of this workshop is to help you to run your CFD codes on AWS. We’ll go from creating the HPC cluster using AWS ParallelCluster, to the installation of the most popular codes e.g STAR-CCM+, OpenFOAM, Fluent, MSC Cradle and finally example submission scripts for you to run your own cases.  |
| **[Running Hexagon Computational Aided Engineering (CAE) applications on ParallelCluster](https://catalog.workshops.aws/cae-hexagon)**  | The purpose of this workshop is to help you to run your Hexagon (MSC) applications on AWS. We’ll go from creating the HPC cluster using AWS ParallelCluster, to the installation of the codes such as Cradle CFD, MSC Nastran, Marc, Actran, Simufact etc. and finally example submission scripts for you to run your own cases.|
| **[Slurm REST API - Accounting and Federation on AWS ParallelCluster](https://catalog.workshops.aws/hpc-slurm)**|  In this workshop, we will use Jupyter Notebooks (managed in SageMaker) to create AWS ParallelClusters, enable Slurm REST API, Slurm Accounting and Slurm Federation on those clusters. Through a real-world astrophysics numerical simulation (Athena++), you will learn how to run MPI jobs on AWS ParallelCluster through a REST interface and also learn how to burst HPC jobs from one cluster to another.  |
| **[How to use Spack to create a build cache and use it in ParallelCluster](https://catalog.us-east-1.prod.workshops.aws/workshops/3b03d3bb-2a2e-41e5-a3ee-7771f36e6982)**| In this workshop we will use Spack to compile OpenFOAM then create a build cache on S3 to store our compiled applications. Then, an AWS ParallelCluster cluster will install OpenFOAM from the build cache.  |
| **[Running Quantum ESPRESSO on AWS ParallelCluster](https://catalog.us-east-1.prod.workshops.aws/workshops/c1fb813d-e925-4325-908e-dd4fef6f43f4)**| We will walk through scripts and templates to set up a HPC system on AWS with EFA and Amazon FSx for Lustre. We'll then step through the installation and compilation of Quantum ESPRESSO with the Intel MKL library and run molecular dynamics simulations.  |
| **[Running WRF on AWS ParallelCluster](https://catalog.us-east-1.prod.workshops.aws/workshops/7bed597e-98dc-48d7-88a5-b0bc87d1a459)**| This workshop walks through some common HPC services, providing scripts and templates to set up a HPC system with EFA to run an end-to-end weather simulation using WRF. We will also detail some best practices to optimize scalability and performance of the simulation itself, providing results to compare different configuration performances.  |
| **[Weather Forecasting on AWS HPC](https://weather.hpcworkshops.com/)**| These workshops lead you through getting started and on into installation and use of WRF, MPAS, and Unified Forecase System FV3GFS.  |

## AWS Batch Workshops

| Workshop  | Description  |
| :----------- | :-------------|
| **[Learn AWS Batch](https://catalog.us-east-1.prod.workshops.aws/workshops/81ff4a6e-0a3c-41d4-be17-6ffc942d6451)**| This workshop teaches you about AWS Batch from the ground floor. You will learn about the AWS Batch resource types, create your first resources, and use those resources in some examples.  |
| **[Intro to AWS Batch for Amazon Elastic Kubernetes Service](https://catalog.us-east-1.prod.workshops.aws/workshops/b67b6665-f7a2-427f-affb-caccd087d50d)**| AWS Batch for Amazon Elastic Kubernetes Service (Amazon EKS) provides a fully-managed service for running your batch computing workloads on top of your pre-existing EKS clusters. This workshop provides you with the necessary background information on AWS Batch for EKS, and a walk-through implementing a couple of example workloads.   |
| **[Amazon Genomics CLI (AGC)](https://catalog.us-east-1.prod.workshops.aws/workshops/fa1442ae-312d-4d8c-93f9-f925b7385c34)**| This workshop shows how to install the Amazon Genomics CLI and use it to run genomics pipelines defined in Nextflow, WDL, Snakemake, and CWL.|
| **[Running Large Scale Simulations On AWS Using R](https://catalog.us-east-1.prod.workshops.aws/workshops/4522540d-c97b-482b-9725-3f5ce058e6b8)**|  Many businesses in the Health Care and Life Sciences domain compete on the effectivness of various treatments & drugs. To study the effectiveness, they run statistical analysis, typically written in R. This approach is limited by the compute power that an individual researcher can access. In this workshop we show how to run a Monte-Carlo Simulation using AWS Batch from R.  |
| **[Running Monte-Carlo Simulations on AWS Batch](https://catalog.us-east-1.prod.workshops.aws/workshops/f0e00661-b38d-43d3-b731-7fb608e71d32)**|  Monte Carlo methods are used to value and analyze some financial assets by simulating the various sources of uncertainty affecting their value (usually done by help of stochastic asset models), and then determining the distribution of their value over the range of resultant outcomes. This workshop walks through technical details to efficiently scale and optimize your Monte Carlo simulations.  |

