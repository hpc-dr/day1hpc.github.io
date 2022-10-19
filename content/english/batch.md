---
title: "AWS Batch"
date: 2022-10-17
#author
author: "Angel Pizarro"
# description
description: "AWS Batch is is an always-on scheduler that lets you easily and efficiently run thousands of container jobs. Workflow builders love it for scaling their workloads, from machine learning to genomics. It scales from one job to millions and takes away the chore of spinning up fleets of compute instances and keeping them busy."
layout: "single-notitle"
images:
  - "images/hpc/batch-ident-large.png"
# Taxonomies
categories: ["products"]
tags: ["batch","containers", "hpc"]
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

{{< image src="/images/hpc/batch-ident-square.png" class="boof" >}}

# AWS Batch
**AWS Batch** is an always-on scheduler that lets you easily and efficiently run thousands of container jobs.
**Workflow builders** love it for scaling their workloads, from machine learning to genomics. It scales from **one job to millions** and takes away the chore of spinning up fleets of compute instances and keeping them busy.

## Features
- [Choosing between AWS Batch or AWS ParallelCluster for your HPC Workloads](https://aws.amazon.com/blogs/hpc/choosing-between-batch-or-parallelcluster-for-hpc/)
- [Introducing fair-share scheduling for AWS Batch](https://aws.amazon.com/blogs/hpc/introducing-fair-share-scheduling-for-aws-batch/)
- [New console features including container insights in AWS Batch](https://youtu.be/uv4jJ7XIAfs)
- [Batch can now use Fargate for a truly serverless experience](https://youtu.be/weKeR-qg_-4)
- [AWS Batch's new Faster Scaling features](https://youtu.be/uQCUpw7uSjY)
- [Introducing support for per-job Amazon EFS volumes in AWS Batch](https://aws.amazon.com/blogs/hpc/introducing-support-for-per-job-amazon-efs-volumes-in-aws-batch/)
- [Fair share scheduling to maximize user happiness in AWS Batch](https://youtu.be/Ws_fvv1_Sv8)

## Announcements
- [BioContainers are now available in Amazon ECR Public Gallery](https://aws.amazon.com/blogs/hpc/biocontainers-are-now-available-in-amazon-ecr-public-gallery/)

## Skills

{{< image src="/images/hpc/media-ident-square.png" class="boof" >}}

- [AWS Batch Dos and Don’ts: Best Practices in a Nutshell](https://aws.amazon.com/blogs/hpc/aws-batch-best-practices/)
- [What\'s the difference between canceling and terminating a job in AWS Batch?](https://aws.amazon.com/blogs/hpc/reader-question-what-is-the-difference-between-canceling-and-terminating-a-job-in-aws-batch/)
- [Rearchitecting AWS Batch managed services to leverage AWS Fargate](https://aws.amazon.com/blogs/hpc/rearchitecting-aws-batch-managed-services-to-leverage-aws-fargate/)
- [Understanding the AWS Batch termination process](https://aws.amazon.com/blogs/hpc/understanding-the-aws-batch-termination-process/)
- [Using AWS Batch Console Support for Step Functions Workflows](https://aws.amazon.com/blogs/hpc/using-aws-batch-console-support-for-step-functions/)

## Use cases
  
### HCLS
- [Optimize Protein Folding Costs with OpenFold on AWS Batch](https://aws.amazon.com/blogs/hpc/optimize-protein-folding-costs-with-openfold-on-aws-batch/)
- [Protein folding in the cloud - a protein primer with Brian Loyal](https://youtu.be/h9QPdUGWkZQ)
- [AlphaFold vs OpenFold - accelerating time to result in protein folding](https://youtu.be/CHBFgz1ZF7o)

- [Analyzing Genomic Data using Amazon Genomics CLI and Amazon SageMaker](https://aws.amazon.com/blogs/hpc/analyzing-genomic-data-using-amazon-genomics-cli-and-amazon-sagemaker/)

- [Accelerating drug discovery with Amazon EC2 Spot Instances](https://aws.amazon.com/blogs/hpc/accelerating-drug-discovery-with-amazon-ec2-spot-instances/)
- [Running 20k simulations in 3 days to accelerate early stage drug discovery with AWS Batch](https://aws.amazon.com/blogs/hpc/running-20k-simulations-in-3-days-with-aws-batch/)
- [miniWDL workflows with 100% cloud elasticity, and no DevOps geekery](https://youtu.be/N-IlEZKa_-0)
- [Nextflow Tower and how it makes it easy to manage a lot of infrastructure quickly.](https://youtu.be/JOguxRohITA)
- [Genomics workflow set made easy with AWS Genomics CLI](https://youtu.be/30cfBPdzykA)

### VFX

- [Efficient and cost-effective rendering pipelines with Blender and AWS Batch](https://aws.amazon.com/blogs/hpc/efficient-and-cost-effective-rendering-pipelines-with-blender-and-aws-batch/)
- [Getting Started with NVIDIA Clara Parabricks on AWS Batch using AWS CloudFormation](https://aws.amazon.com/blogs/hpc/getting-started-with-nvidia-parabricks-on-aws-batch-using-aws-cloudformation/)

- [Encoding workflow dependencies in AWS Batch](https://aws.amazon.com/blogs/hpc/encoding-workflow-dependencies-in-aws-batch/)
- [AWS Batch updates: higher compute utilization, AWS PrivateLink support, and updatable compute environments](https://aws.amazon.com/blogs/hpc/aws-batch-updates-higher-compute-utilization-aws-privatelink-support-and-updatable-compute-environments/)

### Data Science
- [Data Science workflows at insitro: how redun uses the advanced service features from AWS Batch and AWS Glue](https://aws.amazon.com/blogs/hpc/how-insitro-redun-uses-advanced-aws-features/)
- [Data Science workflows at insitro: using redun on AWS Batch](https://aws.amazon.com/blogs/hpc/data-science-workflows-at-insitro-using-redun-on-aws-batch/)
- [Bayesian ML Models at Scale with AWS Batch](https://aws.amazon.com/blogs/hpc/bayesian-ml-models-at-scale-with-aws-batch/)
- [Bayesian models and half a million cores - what're you waiting for?](https://youtu.be/CcqeeRyx93k)

- [Scalable and Cost-Effective Batch Processing for ML workloads with AWS Batch and Amazon FSx](https://aws.amazon.com/blogs/hpc/ml-training-with-aws-batch-and-amazon-fsx/)

- [Optimize your Monte Carlo simulations using AWS Batch](https://aws.amazon.com/blogs/hpc/optimizing-monte-carlo-simulations-using-aws-batch/)




