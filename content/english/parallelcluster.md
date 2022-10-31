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

ParallelCluster helps you securely build and manage cost-efficient **HPC Clusters on AWS**, powered by the latest compute, networking, and storage technologies, and as scalable as AWS itself. 

* **Latest compute**: Your HPC clusters run on [Amazon EC2](https://aws.amazon.com/ec2/). With over 500 (and growing) [instance types](https://aws.amazon.com/ec2/instance-explorer/) available, you can tailor your cluster's compute architecture to specific workloads. You can build clusters powered by the latest x86 CPUs from Intel and AMD, [AWS Graviton](https://aws.amazon.com/ec2/graviton/) (our Arm-based processors), and accelerators like [Trainium](https://aws.amazon.com/machine-learning/trainium/) or powerful NVIDIA GPUs. If a new instance type meets your needs, adding it to your production infastructure is as simple as changing a configuration setting. 
* **Scalable**: Rather than being statically provisioned for your peak workload, your clusters can scale up when you need them and back down again when you don't. ParallelCluster builds on [Slurm](https://www.schedmd.com/), a popular open-source job scheduler, and integrates it with AWS scaling technologies used by thousands of customers every day to elastically meet their computing demands. 
* **Familar interfaces**: You can choose from Amazon Linux, Centos, or Ubuntu operating systems to build your clusters. Each feature a best-of-class user environment that supports modern systems for managing software such as [GNU modules](https://modules.readthedocs.io/en/latest/), [Conda](https://docs.conda.io/en/latest/), and [Spack](https://spack.io/). You can access them over SSH, Amazon Systems Manager, and EC2 Instance Connect. You can also use interactive desktops and visualization tools via [NICE DCV](/dcv), which is built-in to ParallelCluster systems. On the management side of things, ParallelCluster has a graphical interface (and a CLI) to model and control all the resources you need for your HPC applications. It also has a web service API you can use for advanced workflow management. 
* **Advanced Networking**: [Amazon Elastic Fabric Adapter](https://aws.amazon.com/hpc/efa/) (EFA), our high-performance data-center scale networking protocol, is built in to most modern EC2 instances -- ParallelCluster configures it for you automatically. You can also tune inter-instance latency with network placement groups that put your HPC EC2 instances in close physical proximity in our data centers. And, your clusters can have any combination of public and private networking (VPCs), SSH bastion hosts, static IP addresses, and policy-based network security groups, all configurable using ParallelCluster. 
* **Performant Storage**: Data is just is important as compute the modern HPC universe. ParallelCluster helps you provision, manage, and use high-performance shared filesystems built securely on your choice of Amazon storage technologies. By default, your cluster's home directory is exported to all compute nodes from an [AWS Elastic Block Store](https://aws.amazon.com/ebs/) (EBS) volume. You can add additional shared filesystems built on [FSx for Lustre](https://aws.amazon.com/fsx/lustre/) (as well as [NetApp ONTAP](https://aws.amazon.com/fsx/netapp-ontap/) and [OpenZFS](https://aws.amazon.com/fsx/openzfs/)). If you choose FSx for Lustre, you can integrate with [Amazon S3](https://aws.amazon.com/s3/) and [Amazon File Cache](https://aws.amazon.com/filecache/) to manage data lifecycle, control costs, and integrate with on-premises storage. 
* **Secure by Design**: Responsbility for security and compliance at AWS is [shared between you and AWS](https://aws.amazon.com/compliance/shared-responsibility-model/). AWS protects and [ensures compiance](https://aws.amazon.com/compliance/) for the infrastructure that runs all the services it offers, while you protect the assets you run on AWS. ParallelCluster helps with this by offering secure-by-default configurations for user authentication and authorization, networking access, software installation and updates, and more. You can build on these foundations with additional filesystem encryption, IAM policies and roles, integration with Active Directory, networking configuration, and secrets management. These are all provided by AWS services and are usable from within ParallelCluster. 
* **Cloud-Ready**: Today's HPC finds it integrated with complex instrumentation and business systems, many of which are native to the web. ParallelCluster systems are built on the cloud, using cloud technologies. This means you can use technologies like [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), [AWS Lambda](https://aws.amazon.com/lambda/), and [AWS Step Functions](https://aws.amazon.com/step-functions/) to process events, orchestrate jobs, manage data, and other mission-critical tasks that involve non-HPC systems. 

## Learn More About ParallelCluster

<style>
.boof {
  float:right !important;
  width:350px;
  padding: 10px;
  }
</style>
{{< image src="/images/hpc/media-ident-square.png" class="boof" >}}

First, let's make sure you're comfortable that ParallelCluster is the right path for your AWS workloads. We have 100% cloud-native offering known as [AWS Batch](/batch/) which is also scalable, flexible, and adaptable to a wide number of use cases. We have an in-depth blog post that helps explain **[when to choose AWS Batch versus AWS ParallelCluster](https://aws.amazon.com/blogs/hpc/choosing-between-batch-or-parallelcluster-for-hpc/)**. Once you're read it over, feel free to keep exploring the linked articles below describing ParallelCluster's key features, configuration mechanics, and migration paths. 

{{< tabs >}}
  {{< tab "Key Features" >}} 
- [Introducing AWS ParallelCluster 3](https://aws.amazon.com/blogs/hpc/introducing-aws-parallelcluster-3/)- This blog describes the features of ParallelCluster 3.
- [ParallelCluster 3 - built by customers](https://youtu.be/a-99esKLcls) - In this Tech Short video (17m) the ParallelCluster product team talks about new features in version 3.
- [Multiuser support via Active Directory](https://aws.amazon.com/blogs/hpc/introducing-aws-parallelcluster-multiuser-support-via-active-directory/) - Learn about configuring a multi-user cluster.
- [Custom AMIs in ParallelCluster 3](https://aws.amazon.com/blogs/hpc/custom-amis-with-parallelcluster-3/) - Learn about customizing the VM image that powers your HPC cluster
- [Expanded filesystems support in v3.2](https://aws.amazon.com/blogs/hpc/expanded-filesystems-support-in-aws-parallelcluster-3-2/) - Learn how ParallelCluster supports a diversity of network filesystems
- [Slurm-based memory-aware scheduling](https://aws.amazon.com/blogs/hpc/slurm-based-memory-aware-scheduling-in-aws-parallelcluster-3-2/) - Learn how we recently added support for memory-aware job scheduling to ParallelCluster.
  {{< /tab >}}
  {{< tab "Configuration" >}}  
- [PCluster Manager - A new GUI for building and managing clusters](https://youtu.be/Z1vlpJYb1KQ) - Follow on with a video (20m) tour through the ParallelCluster management console.
- [ParallelCluster 3\'s config file](https://youtu.be/6gAwAK5IJ2w) - Learn how the ParallelCluster configuration file is an example of *infrastructure as code* (13m).
  {{< /tab >}}
  {{< tab "Migrate from SGE" >}}
Since SGE is no longer supported by the community, we worked with the team at [SchedMD](https://www.schedmd.com/) to create a tutorial series to help everyone understand what tools are available in Slurm, to make the shift easier.
- [Easing your migration from SGE to Slurm in AWS ParallelCluster 3](https://aws.amazon.com/blogs/hpc/easing-your-migration-from-sge-to-slurm-in-aws-parallelcluster-3/) - This blog post kicks off the tutorial with several handy cheat sheets.
- 4-Part Tech Shorts series - These are hands-on tutorials with examples, delivered by experts from SchedMD and AWS:
  - [Command Line Tools](https://youtu.be/zCEN4GblrRs)
  - [Job Scripts](https://youtu.be/HYMqq0L6fLU)
  - [Array Jobs](https://youtu.be/PVO7_fZAT0I)
  - [Slurm Accounting](https://youtu.be/TzTIN17CG-s)
  {{< /tab >}}
{{< tab "Migrate from ParallelCluster 2" >}}
In 2021, we released an all-new version of ParallelCluster. If you use version 2, we've made it straightforward to migrate to the modern release. 
- [ParallelCluster 3\'s config file](https://youtu.be/6gAwAK5IJ2w) - Learn how the ParallelCluster 3 configuration file is an example of *infrastructure as code* (13m).
- [Migrating to AWS ParallelCluster v3 – updated CLI interactions](https://aws.amazon.com/blogs/hpc/aws-parallelcluster-v3-updated-cli/) - Version 3 introduces some new CLI interactions. This blog tells you about them. 
- [ParallelCluster 3 Configuration Converter](https://aws.amazon.com/blogs/hpc/using-the-parallelcluster-3-configuration-converter/) - This post describes a helpful migration assistant that ships with ParallelCluster 3.
{{< /tab >}}
{{< /tabs >}}  

## Build with ParallelCluster

<style>
.boof2 {
  float:right !important;
  width:350px;
  padding: 10px;
  }
</style>
{{< image src="/images/pcmanager/Create_Cluster_MultipleQueues2.png" class="boof2" >}}

There are two ways to get ParallelCluster::

1. **We suggest using [AWS ParallelCluster Manager](https://pcluster.cloud/01-getting-started.html)**, a web-based interface for designing and deploying your clusters. It helps you easily integrate fast file systems (like Lustre), visual desktops, and tools to **control your spend** using Slurm accounting. You can quickly deploy the **PCluster Manager** application in your own AWS account by following the tutorial [here](https://pcluster.cloud/01-getting-started.html).

2. If you're familiar with AWS already, or just want a CLI, we have that too. You can install the ParallelCluster Python package on nearly any modern computer. The procedure is [documented here](https://docs.aws.amazon.com/parallelcluster/latest/ug/install-v3-parallelcluster.html) but starts with:

``` bash
$ python3 -m pip install --upgrade "aws-parallelcluster>3"
```

## Scale with ParallelCluster

ParallelCluster delivers you a canonical Beowulf cluster experience on AWS, but with added twists like elasticity, and support for fast storage and networking, built-in *by design*. That means you can run virtually any workload you like on AWS and expect to see great results.

The tabs here feature videos and blog posts describing how different customers have scaled with ParallelCluster - hopefully you'll recognize some that are familiar to your needs. If not, reach out!

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
