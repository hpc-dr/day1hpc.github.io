---
title: "AWS ParallelCluster"
date: 2022-10-17
author: "Matt Vaughn"
description: "AWS ParallelCluster is an open source tool that makes it easy to deploy and manage HPC clusters on AWS"
layout: "product"
images:
  - "images/hpc/pc-ident-large.png"
  - "images/hpc/pc-ident-large.png"
## Taxonomies
categories: ["AWS ParallelCluster"]
tags: ["hpc","products"]
type: "featured" # available type (regular or featured)
draft: false
---

<div class="container">
<div class="row">

AWS ParallelCluster helps you build and manage cost-efficient **HPC Clusters on AWS**. ParallelCluster HPC systems are powered by the latest compute architectures and are scalable as AWS itself. They feature advanced networking and high-performance storage to handle challenging workloads. But, they are also easy to use, with familiar software environments. They are designed around a high degree of security and compliance to help protect your data. And, they are cloud-ready so you can integrate them with non-HPC systems. 

</div>
</div>

----

### Latest compute
<div class="container-fluid">
<div class="row">
<div class="col-2">{{< image src="/images/hpc/1-pc-ksp-compute-strap.png" class="img-float-center" >}}</div>
<div class="col">

Your HPC clusters run on [Amazon EC2](https://aws.amazon.com/ec2/). With over 500 (and growing) [instance types](https://aws.amazon.com/ec2/instance-explorer/) available, you can tailor your cluster's compute architecture to specific workloads. You can build clusters powered by the latest x86 CPUs from Intel and AMD, [AWS Graviton](https://aws.amazon.com/ec2/graviton/) (our Arm-based processors), and accelerators like [Trainium](https://aws.amazon.com/machine-learning/trainium/) or powerful NVIDIA GPUs. If a new instance type meets your needs, adding it to your production infastructure is as simple as changing a configuration setting.

</div>
</div>

<div class="row">
<div class="col">
{{< collapse "Learn more about EC2 for HPC" >}}
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
</div>

-----

### Supremely scalable
<div class="container-fluid">
<div class="row">
<div class="col">

Rather than being statically provisioned for your peak workload, your AWS-based clusters can be dynamic. This means they scale up their resource footprint when you have jobs to run, then scale back down again when you don't. ParallelCluster builds on [Slurm](https://www.schedmd.com/), a popular open-source job scheduler, and integrates it with AWS scaling technologies like [EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet.html) and [Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html) used by thousands of customers every day to elastically meet their computing demands. 

</div>
<div class="col-2">{{< image src="/images/hpc/2-pc-ksp-scalable-strap.png" class="img-float-center" >}}</div>
</div>

<div class="row">
<div class="col">

{{< collapse "Learn more about elastic scaling" >}}
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
| [Thermo Fisher\'s Elastic GPU cluster for CryoEM](https://aws.amazon.com/blogs/hpc/how-thermo-fisher-scientific-accelerated-cryo-em-using-aws-parallelcluster/) | [GROMACS using Spot Instances and AWS Graviton](https://aws.amazon.com/blogs/hpc/running-gromacs-on-spot-with-checkpointing/) |
| [Migrating from SGE to Slurm in ParallelCluster 3](https://aws.amazon.com/blogs/hpc/easing-your-migration-from-sge-to-slurm-in-aws-parallelcluster-3/) | [Memory-aware Slurm job scheduling](https://aws.amazon.com/blogs/hpc/slurm-based-memory-aware-scheduling-in-aws-parallelcluster-3-2/) |
{{</ collapse >}}

</div>
</div>
</div>

-----

### Advanced networking
<div class="container-fluid">
<div class="row">
<div class="col-2">{{< image src="/images/hpc/4-pc-ksp-network-strap.png" class="img-float-center" >}}</div>
<div class="col">

[Amazon Elastic Fabric Adapter](https://aws.amazon.com/hpc/efa/) (EFA), our high-performance data-center scale networking protocol, is built in to most modern EC2 instances -- ParallelCluster configures it for you automatically. You can also easily tune inter-instance latency with [instance placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) that put your HPC EC2 instances in close physical proximity in our data centers. And, your clusters can have any combination of public and private networking (VPCs), SSH bastion hosts, static IP addresses, and policy-based network security groups, all configurable using ParallelCluster.

</div>
</div>

<div class="row">
<div class="col">

{{< collapse "Learn more about AWS HPC networking" >}}
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
| [What is EFA?](https://youtu.be/inJxFXMMp0U) | [How does EFA work?](https://youtu.be/inJxFXMMp0U) |
| [EFA-enabled Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types) | [IEEE Spectrum paper on EFA and SRD](https://hpc.news/ieeeSRD) |
{{</ collapse >}}

</div>
</div>
</div>

-----

### Performant storage
<div class="container-fluid">
<div class="row">
<div class="col">

Data is just is important as compute the modern HPC universe. ParallelCluster helps you provision, manage, and use high-performance shared filesystems built securely on your choice of Amazon storage technologies. By default, your cluster's home directory is exported to all compute nodes from an [AWS Elastic Block Store](https://aws.amazon.com/ebs/) (EBS) volume. You can add additional shared filesystems built on [FSx for Lustre](https://aws.amazon.com/fsx/lustre/) (as well as [NetApp ONTAP](https://aws.amazon.com/fsx/netapp-ontap/) and [OpenZFS](https://aws.amazon.com/fsx/openzfs/)). If you choose FSx for Lustre, you can integrate with [Amazon S3](https://aws.amazon.com/s3/) and [Amazon File Cache](https://aws.amazon.com/filecache/) to manage data lifecycle, control costs, and integrate with on-premises storage. 

</div>
<div class="col-2">{{< image src="/images/hpc/5-pc-ksp-storage-strap.png" class="img-float-center" >}}</div>
</div>

<div class="row">
<div class="col">
{{< collapse "Learn more about high performance storage" >}}
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
| [A video explainer on AWS HPC Storage](https://www.youtube.com/watch?v=PY_X49SQWuo) | [Introducing FSx for OpenZFS](https://www.youtube.com/watch?v=AaAy6_bpI9Q&t=750s) |
| [Introducing FSx for Lustre](https://www.youtube.com/watch?v=0AVdf3jKuvo) | [Building highly-available HPC infrastructure on AWS](https://aws.amazon.com/blogs/hpc/highly-available-hpc-infrastructure-on-aws/) |
{{</ collapse >}}

</div>
</div>
</div>

-----

### Familar interfaces
<div class="container-fluid">
<div class="row">

<div class="col-2">{{< image src="/images/hpc/3-pc-ksp-familiar-strap.png" class="img-float-center" >}}</div>

<div class = "col">

You can choose from [Amazon Linux](https://aws.amazon.com/linux/), Centos, or Ubuntu operating systems to build your clusters. Each feature a best-of-class user environment that supports modern systems for managing software such as [GNU modules](https://modules.readthedocs.io/en/latest/), [Conda](https://docs.conda.io/en/latest/), and [Spack](https://spack.io/). You can access them directly over SSH, or indirectly via [Amazon Systems Manager](https://docs.aws.amazon.com/systems-manager) or [EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html). You can also use interactive desktops and visualization tools via [NICE DCV](/dcv), which is built-in to ParallelCluster systems. On the management side of things, ParallelCluster has a graphical interface (and a CLI) to model and control all the resources you need for your HPC applications. It also has a web service API you can use for advanced workflow management. 

</div>

</div>

<div class="row">
<div class="col">

{{< collapse "Learn more about user interfaces" >}}
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
| [An introduction to DCV](https://youtu.be/-mhNktbKmAc) | [Pushing pixels with NICE DCV](https://aws.amazon.com/blogs/hpc/pushing-pixels-with-nice-dcv/) |
| [The PCluster Manager GUI](https://youtu.be/PChP3FQWeJQ) | [Connect to EC2 instances via SSM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/session-manager.html) | 
| [Using the Slurm REST API with ParallelCluster](https://aws.amazon.com/blogs/hpc/using-the-slurm-rest-api-to-integrate-with-distributed-architectures-on-aws/) | [The ParallelCluster Serverless API](https://docs.aws.amazon.com/parallelcluster/latest/ug/api-reference-v3.html) |
{{</ collapse >}}

</div>
</div>
</div>

-----

### Secure by design
<div class="container-fluid">
<div class="row">
<div class="col">

Responsbility for security at AWS is [shared between you and AWS](https://aws.amazon.com/compliance/shared-responsibility-model/). AWS protects and [ensures compliance](https://aws.amazon.com/compliance/) for the infrastructure that runs all the services it offers, while you protect the assets you run on AWS. ParallelCluster helps with this by offering secure-by-default configurations for user authentication and authorization, networking access, software installation and updates, and more. You can build on these foundations with additional filesystem encryption, IAM policies and roles, integration with Active Directory, networking configuration, and secrets management. These are all provided by AWS services and are usable from within ParallelCluster. 

</div>
<div class="col-2">{{< image src="/images/hpc/6-pc-ksp-secure-strap.png" class="img-float-center" >}}</div>
</div>

<div class="row">
<div class="col">

{{< collapse "Learn more about HPC security on AWS" >}}
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
| [Security in ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/security.html) | [Complicance validation for ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/security-compliance-validation.html) |
| [ParallelCluster with Active Directory](https://aws.amazon.com/blogs/hpc/introducing-aws-parallelcluster-multiuser-support-via-active-directory/) | [Video guide to Active Directory integration](https://www.youtube.com/watch?v=wvd6bFieht0) |
{{</ collapse >}}

</div>
</div>
</div>

-----

### Cloud-ready
<div class="container-fluid">
<div class="row">

<div class="col-2">{{< image src="/images/hpc/7-pc-ksp-cloud-ready-strap.png" class="img-float-center" >}}</div>

<div class="col">

Today's HPC finds itself integrated with complex instrumentation and business systems, many of which are native to the web. ParallelCluster systems are built on the cloud, using cloud technologies. This means you can integrate them with services like [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), [AWS Lambda](https://aws.amazon.com/lambda/), and [AWS Step Functions](https://aws.amazon.com/step-functions/) to process events, orchestrate jobs, manage data, and other mission-critical tasks that involve non-HPC systems. 

</div>
</div>

<div class="row">
<div class="col">

{{< collapse "Learn more about cloud-ready HPC" >}}
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
| [AWS Services that power ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/aws-services-v3.html) | [Working with Amazon S3](https://docs.aws.amazon.com/parallelcluster/latest/ug/s3_resources-v3.html) |
| [AWS Identity and Access Management roles with ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/iam-roles-in-parallelcluster-v3.html) | [Multi-user clusters with Active Directory](https://aws.amazon.com/blogs/hpc/introducing-aws-parallelcluster-multiuser-support-via-active-directory/) | 
{{</ collapse >}}

</div>
</div>
</div>

-----

## Learn More About ParallelCluster
<div class="container-fluid">
<div class="row">
<div class="col">

First, let's make sure you're comfortable that ParallelCluster is the right path for your AWS workloads. We also have 100% cloud-native offering known as [AWS Batch](/batch/). Batch builds on many of the same AWS technologies as ParallelCluster, so it is also scalable, flexible, and adaptable to a wide number of use cases. We have an in-depth blog post that helps explain **[when to choose AWS Batch versus AWS ParallelCluster](https://aws.amazon.com/blogs/hpc/choosing-between-batch-or-parallelcluster-for-hpc/)**. Once you're read it over, feel free to keep exploring more resources below describing key features and configurations of ParallelCluster. 
* [Introducing AWS ParallelCluster 3](https://aws.amazon.com/blogs/hpc/introducing-aws-parallelcluster-3/)- This blog describes the features of ParallelCluster 3.
* [ParallelCluster 3 - built by customers](https://youtu.be/a-99esKLcls) - In this Tech Short video (17m) the ParallelCluster product team talks about new features in version 3.
* [PCluster Manager - A new GUI for building and managing clusters](https://youtu.be/Z1vlpJYb1KQ) - A video (20m) tour through the ParallelCluster web console.
* [ParallelCluster 3\'s config file](https://youtu.be/6gAwAK5IJ2w) - Learn how the ParallelCluster configuration file is an example of *infrastructure as code* (13m).
* [Customizing ParallelCluster 3 AMIs](https://aws.amazon.com/blogs/hpc/custom-amis-with-parallelcluster-3/) - Learn about customizing the virtual machine image that powers your HPC cluster.
</div>

<div class="col-4">
{{< image src="/images/hpc/media-ident-square.png" class="img-float-right" >}}
</div>
</div>
</div>

----

## Build with ParallelCluster

<div class="container-fluid">
<div class="row">
<div class="col">

There are two ways to get ParallelCluster::

1. **We suggest using [PCluster Manager](https://pcluster.cloud/01-getting-started.html)**, a web-based interface for designing and deploying your clusters. It helps you easily integrate fast file systems (like Lustre), visual desktops, and tools to **control your spend** using Slurm accounting. You can quickly deploy the **PCluster Manager** application in your own AWS account by following the tutorial [here](https://pcluster.cloud/01-getting-started.html).

2. If you're familiar with AWS already, or just want a CLI, we have that too. You can install the ParallelCluster [Python package](https://pypi.org/project/aws-parallelcluster/) on nearly any modern computer. The procedure is [documented here](https://docs.aws.amazon.com/parallelcluster/latest/ug/install-v3-parallelcluster.html) but starts with:

``` bash
$ python3 -m pip install --upgrade "aws-parallelcluster>3"
```
</div>

<div class="col-4">{{< image src="/images/pcmanager/Create_Cluster_MultipleQueues.png" class="img-float-center img-drop-shadow" >}}</div>

</div>
</div>

<div class="row">
<div class="col">

{{< collapse "Learn more from interactive workshops" >}}
You can run these workshops in your own AWS account. Most take 1-2 hours to complete and cost between 5 and 15 dollars. 
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
| [Running CFD on AWS ParallelCluster at scale](https://catalog.us-east-1.prod.workshops.aws/workshops/21c996a7-8ec9-42a5-9fd6-00949d151bc2/en-US) | [Running WRF on AWS ParallelCluster](https://catalog.us-east-1.prod.workshops.aws/workshops/7bed597e-98dc-48d7-88a5-b0bc87d1a459/en-US) |
| [Slurm REST API, Accounting and Federation on AWS ParallelCluster](https://catalog.us-east-1.prod.workshops.aws/workshops/d431e0b1-9f08-4d82-822e-ea56962b2a0b/en-US) | [Running Hexagon Manufacturing Intelligence (HMI) applications on AWS ParallelCluster](https://catalog.us-east-1.prod.workshops.aws/workshops/8885ed02-5402-4426-818f-edee72b5a07a/en-US) |
| [ HPC Workshops - Best practices from the AWS Field Team](https://www.hpcworkshops.com/) | [The Numerical Weather Prediction (NWP) Workshop](https://weather.hpcworkshops.com/) |
{{</ collapse >}}

</div>
</div>
</div>

-----

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

We're always adding new content to this site and at the [AWS HPC blog](https://aws.amazon.com/blogs/hpc/) and [Techshorts Youtube channel](https://www.youtube.com/channel/UChSIn5kcWQvJxW17KIjdLVw). Check back often for more [articles](/tags/hpcblog/) and [videos](/tags/techshorts/) on ParallelCluster and other HPC technologies from AWS. 
