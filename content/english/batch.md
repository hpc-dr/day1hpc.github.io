---
title: "AWS Batch"
date: 2022-11-07
author: "Angel Pizarro"
description: "AWS Batch is is an always-on job scheduler and resource orchestrator that lets you easily and efficiently run thousands of containerized applications. Workflow builders love it for scaling their workloads, from machine learning to genomics. It scales from one job to tens of millions, and takes away the chore of spinning up fleets of compute instances and keeping them busy."
layout: "product"
images:
  - "images/hpc/Ident-Batch@3x.webp"
product_images:
  - "images/g3/ksp-batch-title.webp"
  - "images/g3/ksp-batch-compute.webp"
  - "images/g3/ksp-batch-cost.webp"
  - "images/g3/ksp-batch-scheduler.webp"
  - "images/g3/ksp-batch-scale.webp"
  - "images/g3/ksp-batch-secure.webp"
  - "images/g3/ksp-batch-cloud.webp"
# Taxonomies
categories: ["AWS Batch", "products"]
tags: ["batch","containers", "hpc"]
type: "featured" # available type (regular or featured)
draft: false
---

<div class="container">
<div class="row" >

AWS Batch is is an **always-on job scheduler and resource orchestrator** that lets you easily and efficiently run thousands of containerized applications.

 **Workflow builders** love it for scaling their workloads, from machine learning to genomics. Batch scales from **one job** to **millions of jobs**, and takes away the chore of spinning up fleets of compute instances and keeping them busy.
</div>
</div>
<p>
<style>
.boof4 {
  width:300px;
  padding: 10px;
  }
</style>
<center>
<a href="https://youtu.be/24tBOQDAyUA" target="2023-03-08-01">{{< image src="/images/tsf/tsf-what-is-batch.png" class="boof4" >}}</a>
<a href="https://youtu.be/su5gGg8A1H8" target="2023-03-08-00">{{< image src="/images/post/su5gGg8A1H8.png" class="boof4" >}}</a>
<a href="https://youtu.be/XAvosrqaCMQ" target="2023-03-08-01">{{< image src="/images/post/XAvosrqaCMQ.png" class="boof4" >}}</a>

</center>

</p>

----
### Scale for all your needs

<div class="container-fluid">
<div class="row">
<div class="col-2">{{< image src="/images/batch/autoscale.png" class="img-float-center" >}}</div>
<div class="col">

AWS Batch **efficiently** and **dynamically** provisions and scales compute on your behalf. Batch can scale from  **one job** to **millions of jobs**. Our largest analysis (so far) used Batch to orchastrate over five million vCPUs across multiple AWS Regions. And once your work is done, Batch handles scaling down those resources too! 

Batch leverages **AWS scaling technologies** like [EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet.html) and [Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html) used by thousands of customers every day to elastically meet their computing demands. 
</div>
</div>

<div class="row">
<div class="col">
{{< collapse "Learn more about scaling your workloads with AWS Batch" >}}
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
| [Scalable and Cost-Effective Batch Processing for ML workloads with AWS Batch and Amazon FSx](https://aws.amazon.com/blogs/hpc/ml-training-with-aws-batch-and-amazon-fsx/) | [Introducing fair-share scheduling for AWS Batch](https://aws.amazon.com/blogs/hpc/introducing-fair-share-scheduling-for-aws-batch/) |
| [AWS Batch now supports Kubernetes](https://aws.amazon.com/blogs/aws/aws-batch-for-amazon-elastic-kubernetes-service/) | [Span AWS Regions using the AWS Cyclone solution with AWS Batch](https://github.com/awslabs/aws-cyclone-solution)|
{{</ collapse >}}

</div>
</div>
</div>

----

### Cost and throughput optimized

<div class="container-fluid">
<div class="row">
<div class="col">

AWS Batch optimizes for **throughput** and **cost**. It does so by scaling compute resources to process jobs in the job queue using **allocation strategies to fit your business needs and budget**. Batch can also use EC2 Spot Instances to save up to a 90% discount compared to On-Demand prices, with a preference for instance types that are less likely to be interrupted. 

</div>
<div class="col-2">{{< image src="/images/hpc/icons/cost.png" class="img-float-center" >}}</div>
</div>

<div class="row">
<div class="col">
{{< collapse "Learn more about optimizing costs with AWS Batch" >}}
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
| [AWS Batch allocations strategies](https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html) | [Using On-Demand or Spot Instances](https://docs.aws.amazon.com/batch/latest/userguide/best-practices.html#bestpractice5) |
| [EC2 Spot Best Practices for AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/best-practices.html#bestpractice6) | [A serverless cost gaurdian solution for AWS Batch](https://aws.amazon.com/blogs/hpc/avoid-overspending-with-aws-batch-using-a-serverless-cost-guardian-monitoring-architecture/)  | 
{{</ collapse >}}
</div>
</div>
</div>

----

### Secure by design
<div class="container-fluid">
<div class="row">
<div class="col-2">{{< image src="/images/hpc/icons/secure.png" class="img-float-center" >}}</div>
<div class="col">

Responsbility for security at AWS is [shared between you and AWS](https://aws.amazon.com/compliance/shared-responsibility-model/). AWS protects the infrastructure that runs all the services it offers, while you protect the assets you run on AWS. 

AWS Batch uses IAM to control and monitor the AWS resources that your jobs can access, such as Amazon DynamoDB tables. Through IAM, you can also define policies for different users in your organization. For example, administrators can be granted full access permissions to any AWS Batch API operation, developers can have limited permissions related to configuring compute environments and registering jobs, and end users can be restricted to the permissions needed to submit and delete jobs.

</div>
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
| [Security in AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/security.html) | [Compliance Validation for AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/compliance.html) |
| [How to authenticate private container registries using AWS Batch](https://aws.amazon.com/blogs/compute/how-to-authenticate-private-container-registries-using-aws-batch/) | [Identity and Access Management for AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/security-iam.html) |

{{</ collapse >}}

</div>
</div>
</div>

----

### Advanced scheduling capabilities

<div class="container-fluid">
<div class="row">
<div class="col">

With AWS Batch, you can set up multiple queues with different priority levels. Batch jobs are stored in the queues until compute resources are available to run the job. The AWS Batch scheduler evaluates when, where, and how to run jobs that have been submitted to a queue based on the resource requirements of each job. The scheduler evaluates the priority of each queue and runs jobs in priority order on optimal compute resources (for example, memory-optimized compared to CPU-optimized), as long as those jobs have no outstanding dependencies.

</div>
<div class="col-2">{{< image src="/images/hpc/icons/scheduling.png" class="img-float-center" >}}</div>
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
| [Introducing fair-share scheduling for AWS Batch](https://aws.amazon.com/blogs/hpc/introducing-fair-share-scheduling-for-aws-batch/) | [AWS Batch Scheduling Policies User Guide](https://docs.aws.amazon.com/batch/latest/userguide/scheduling-policies.html) |
| [Video: Fair share scheduling to maximize user happiness in AWS Batch](https://youtu.be/Ws_fvv1_Sv8) | [Workshop: Fair-share scheduling on AWS Batch](https://catalog.us-east-1.prod.workshops.aws/workshops/c3d652f2-6de1-4014-9a1b-c1b3c8f08b8d/en-US/intro/batch) |

{{</ collapse >}}

</div>
</div>
</div>

----

### Integrated monitoring and logging

<div class="container-fluid">
<div class="row">
<div class="col-2">{{< image src="/images/batch/logs.png" class="img-float-center" >}}</div>
<div class="col">

AWS Batch displays key operational metrics for your batch jobs in the AWS Management Console. You can view metrics related to compute capacity, as well as metrics for running, pending, and completed jobs. Logs for your jobs (for example, STDERR and STDOUT) are available in the console and are also written to Amazon CloudWatch Logs. You can leverage this information to provide insights on your jobs and the instances used to run them.

</div>
</div>

<div class="row">
<div class="col">
{{< collapse "Learn more about logging and monitoring with AWS Batch" >}}
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
| [Custom logging with AWS Batch](https://aws.amazon.com/blogs/compute/custom-logging-with-aws-batch/) | [AWS Batch Runtime Monitoring Dashboards Solution](https://github.com/aws-samples/aws-batch-runtime-monitoring) |
| [Video: New console features including container insights in AWS Batch](https://youtu.be/uv4jJ7XIAfs) | [A serverless cost gaurdian solution for AWS Batch](https://aws.amazon.com/blogs/hpc/avoid-overspending-with-aws-batch-using-a-serverless-cost-guardian-monitoring-architecture/) |
{{</ collapse >}}

</div>
</div>
</div>

-----

### Cloud-native
<div class="container-fluid">
<div class="row">
<div class="col">

AWS Batch was built on the cloud, using AWS cloud technologies. This means you can integrate AWS Batch with services like [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), [AWS Lambda](https://aws.amazon.com/lambda/), and [AWS Step Functions](https://aws.amazon.com/step-functions/) to process events, orchestrate jobs, manage data, and other mission-critical tasks across your entire business, not just your HPC workloads.

</div>
<div class="col-2">{{< image src="/images/hpc/icons/cloud.png" class="img-float-center" >}}</div>
</div>

<div class="row">
<div class="col">
{{< collapse "Learn more about cloud-native HPC with AWS Batch" >}}
<style>
table tr th:empty {
  display: none;
}
table td {
  text-align: center;
}
</style>
| | |
|--|--|
| [Batch can now use Fargate for a truly serverless experience](https://youtu.be/weKeR-qg_-4) | [A serverless cost gaurdian solution for AWS Batch](https://aws.amazon.com/blogs/hpc/avoid-overspending-with-aws-batch-using-a-serverless-cost-guardian-monitoring-architecture/) | 
| [Rearchitecting AWS Batch managed services to leverage AWS Fargate](https://aws.amazon.com/blogs/hpc/rearchitecting-aws-batch-managed-services-to-leverage-aws-fargate/) | [Using AWS Batch Console Support for Step Functions Workflows](https://aws.amazon.com/blogs/hpc/using-aws-batch-console-support-for-step-functions/) |

{{</ collapse >}}

</div>
</div>
</div>

-----

### Latest compute
<div class="container-fluid">
<div class="row">
<div class="col-2">{{< image src="/images/batch/compute.png" class="img-float-center" >}}</div>
<div class="col">

Your AWS Batch jobs run on [Amazon EC2](https://aws.amazon.com/ec2/). With over 500 (and growing) [instance types](https://aws.amazon.com/ec2/instance-explorer/) available, you can tailor your Batch compute environments  to specific workloads. You leverage the latest x86 CPUs from Intel and AMD, [AWS Graviton](https://aws.amazon.com/ec2/graviton/) (our Arm-based processors), and accelerators like [Trainium](https://aws.amazon.com/machine-learning/trainium/) or powerful NVIDIA GPUs. If a new instance type meets your needs, adding it to your production infastructure is as simple as changing a configuration setting.

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

## Learn More About AWS Batch
<div class="container-fluid">
<div class="row">
<div class="col">

First, let's make sure you're comfortable that AWS Batch is the right tool for your workloads. AWS also has a command line tool for standing up traditional HPC clusters called [AWS ParallelCluster](/parallelcluster/). AWS ParallelCluster builds on many of the same AWS technologies as AWS Batch, so it is also scalable, flexible, and adaptable to a wide number of use cases.

If you're  familiar with using a traditional HPC resource - like a SLURM cluster - you may wonder what makes AWS Batch different. To find out, read our post to help you **[choose between AWS Batch or AWS ParallelCluster](https://aws.amazon.com/blogs/hpc/choosing-between-batch-or-parallelcluster-for-hpc/)**. 

{{< collapse "Tools for learning more about AWS Batch" >}}
| | |
|---|---|
| [AWS Batch Dos and Don’ts: Best Practices in a Nutshell](https://aws.amazon.com/blogs/hpc/aws-batch-best-practices/) | [What\'s the difference between canceling and terminating a job in AWS Batch?](https://aws.amazon.com/blogs/hpc/reader-question-what-is-the-difference-between-canceling-and-terminating-a-job-in-aws-batch/) |
| [Understanding the AWS Batch termination process](https://aws.amazon.com/blogs/hpc/understanding-the-aws-batch-termination-process/) | [Using AWS Batch Console Support for Step Functions Workflows](https://aws.amazon.com/blogs/hpc/using-aws-batch-console-support-for-step-functions/) |
| [AWS Batch updates: higher compute utilization, AWS PrivateLink support, and updatable compute environments](https://aws.amazon.com/blogs/hpc/aws-batch-updates-higher-compute-utilization-aws-privatelink-support-and-updatable-compute-environments/) | [Encoding workflow dependencies in AWS Batch](https://aws.amazon.com/blogs/hpc/encoding-workflow-dependencies-in-aws-batch/) |
</div>
{{</ collapse >}}

<!-- <div class="col-4">
{{< image src="/images/hpc/media-ident-mini.png" class="img-float-right" >}}
</div> -->
</div>
</div>

---- 
<!-- 
## Major features you'll want to know about
<div class="container-fluid">
<div class="row">
<div class="col">

- [Introducing fair-share scheduling for AWS Batch](https://aws.amazon.com/blogs/hpc/introducing-fair-share-scheduling-for-aws-batch/)
- [New console features including container insights in AWS Batch](https://youtu.be/uv4jJ7XIAfs)
- [Batch can now use Fargate for a truly serverless experience](https://youtu.be/weKeR-qg_-4)
- [AWS Batch's new Faster Scaling features](https://youtu.be/uQCUpw7uSjY)
- [Introducing support for per-job Amazon EFS volumes in AWS Batch](https://aws.amazon.com/blogs/hpc/introducing-support-for-per-job-amazon-efs-volumes-in-aws-batch/)
- [Fair share scheduling to maximize user happiness in AWS Batch](https://youtu.be/Ws_fvv1_Sv8)
- [BioContainers are now available in Amazon ECR Public Gallery](https://aws.amazon.com/blogs/hpc/biocontainers-are-now-available-in-amazon-ecr-public-gallery/)

</div>

<div class="col-5">
{{< image src="/images/hpc/20s batch.gif" class="boof4" >}}
</div>
</div>
</div>
 -->

## Workflow engines love Batch

If you're working with Nextflow or Cromwell natively, then you'll probably love finding out about the **[AWS Genomics CLI](https://aws.amazon.com/genomics-cli/)** which does pretty much all the boring set up work for you and sets you up for running Nextflow piplines in around half an hour (from a standing start).

{{< tabs >}}
  {{< tab "Netflow" >}}
- [Genomics Workflows on AWS - Nextflow](https://docs.opendata.aws/genomics-workflows/orchestration/nextflow/nextflow-overview.html)
- [Nextflow\'s getting started guide for AWS Batch](https://www.nextflow.io/docs/latest/awscloud.html)
- [Nextflow\'s Summit in 2022](https://summit.nextflow.io/) - lots of great talks.
  {{< /tab >}}
  {{< tab "Cromwell" >}}
- [Genomics Workflows on AWS - Cromwell](https://docs.opendata.aws/genomics-workflows/orchestration/nextflow/nextflow-overview.html)
- [Cromwell on AWS](https://aws.amazon.com/blogs/industries/cromwell-on-aws-a-simpler-and-improved-aws-batch-backend/) - blog post by Mark Schreiber about an improved integration.
  {{< /tab >}}
  {{< tab "Metaflow" >}}
- [Metaflow\'s Season 2 blockbuster on AWS Batch](https://docs.metaflow.org/getting-started/tutorials/season-2-scaling-out-and-up/episode05)
  {{< /tab >}}
{{< /tabs >}}


## Use cases

{{< tabs >}}
  {{< tab "Data Science + Machine Learning" >}}
- Data Science workflows at insitro: advanced service features from AWS Batch and AWS Glue - **[[Part 1]](https://aws.amazon.com/blogs/hpc/how-insitro-redun-uses-advanced-aws-features/)** **[[Part 2]](https://aws.amazon.com/blogs/hpc/data-science-workflows-at-insitro-using-redun-on-aws-batch/)**
- Bayesian ML Models at Scale with AWS Batch [[Blog Post]](https://aws.amazon.com/blogs/hpc/bayesian-ml-models-at-scale-with-aws-batch/) || [[Video]](https://youtu.be/CcqeeRyx93k) - with the data science team from Ampersand in New York.
- [Scalable and Cost-Effective Batch Processing for ML workloads with AWS Batch and Amazon FSx](https://aws.amazon.com/blogs/hpc/ml-training-with-aws-batch-and-amazon-fsx/)
  {{< /tab >}}  
  {{< tab "Healthcare & Life Sciences" >}}
- [Optimize Protein Folding Costs with OpenFold on AWS Batch](https://aws.amazon.com/blogs/hpc/optimize-protein-folding-costs-with-openfold-on-aws-batch/)
- [Protein folding in the cloud - a protein primer with Brian Loyal](https://youtu.be/h9QPdUGWkZQ)
- [AlphaFold vs OpenFold - accelerating time to result in protein folding](https://youtu.be/CHBFgz1ZF7o)
- [Analyzing Genomic Data using Amazon Genomics CLI and Amazon SageMaker](https://aws.amazon.com/blogs/hpc/analyzing-genomic-data-using-amazon-genomics-cli-and-amazon-sagemaker/)
- [Accelerating drug discovery with Amazon EC2 Spot Instances](https://aws.amazon.com/blogs/hpc/accelerating-drug-discovery-with-amazon-ec2-spot-instances/)
- [Running 20k simulations in 3 days to accelerate early stage drug discovery with AWS Batch](https://aws.amazon.com/blogs/hpc/running-20k-simulations-in-3-days-with-aws-batch/)
- [miniWDL workflows with 100% cloud elasticity, and no DevOps geekery](https://youtu.be/N-IlEZKa_-0)
- [Nextflow Tower and how it makes it easy to manage a lot of infrastructure quickly.](https://youtu.be/JOguxRohITA)
- [Genomics workflow set made easy with AWS Genomics CLI](https://youtu.be/30cfBPdzykA)
- [Getting Started with NVIDIA Clara Parabricks on AWS Batch using AWS CloudFormation](https://aws.amazon.com/blogs/hpc/getting-started-with-nvidia-parabricks-on-aws-batch-using-aws-cloudformation/)
  {{< /tab >}}
  {{< tab "Visual FX" >}}
- [Efficient and cost-effective rendering pipelines with Blender and AWS Batch](https://aws.amazon.com/blogs/hpc/efficient-and-cost-effective-rendering-pipelines-with-blender-and-aws-batch/)
  {{< /tab >}}
  {{< tab "Others" >}}
- [Optimize your Monte Carlo simulations using AWS Batch](https://aws.amazon.com/blogs/hpc/optimizing-monte-carlo-simulations-using-aws-batch/)
- [Building well-architected serverless applications: Optimizing application performance](https://aws.amazon.com/blogs/compute/building-well-architected-serverless-applications-optimizing-application-performance-part-3/)
  {{< /tab >}}  
{{< /tabs >}}
