---
title: "SC'24"
date: 2024-03-18
email: "bouffler@amazon.com"
description: "Resources for builders who attended the AWS booth theatre at SC'24 in Atlanta."
layout: "static"
draft: false
social:
  - icon: "fab fa-bsky"
    link: "https://bsky.app/profile/techhpc.bsky.social"
images:
- "images/sc24/AWS-theatre-banner.png"


---

<style>
.iconcenter {
  float:center !important;
  width:180px;
  padding: 0px;
  }
.iconmap {
  width:240px;
  padding: 0px;
  }
</style>

<style>
.vid {
  float:right !important;
  width:350px;
  padding: 10px;
  }
</style>

## We want to help you get to your first "a ha!" moment in the least possible time - here's where to start

**You probably saw some of our expert builders** creating a complex HPC architecture live during the conference. If you were excited about the speed with which it's possible to deploy completely new architectures and workflows, we've pulled some recipes and other resources together that you can adapt to suit your environment.

**If you can't find what you need** reach out to us at ask-hpc@amazon.com.

----

#### 10am-11am - **Secure and successful foundation for HPC on AWS with NIST SP 800-223**
*This session lays out the foundational plumbing for a secure and scalable HPC environment on the cloud. We show architectural best-practices for cost optimization, security, and compliance alignment. We’ll show you how to achieve reproducibility using infrastructure-as-code techniques that will automate (and validate) your environments for deploying workloads.*

##### Resources
* **Blog post coming next week** - we have a blog post, and a recipe/repo coming next week that will walk you through the details of setting up a compliant environment.
* **If your compliance needs don't extend to NIST SP 800**, then we suggest you look at our network stacks in the [HPC Recipes Library](https://github.com/aws-samples/aws-hpc-recipes/tree/main) - either [HPC Basic](https://github.com/aws-samples/aws-hpc-recipes/tree/main/recipes/net/hpc_basic) or [HPC Large Scale](https://github.com/aws-samples/aws-hpc-recipes/tree/main/recipes/net/hpc_large_scale) should do a rgeat job for you.

#### 11am-12pm - **Re-imagining HPC with AWS Parallel Computing Service**
*We introduce **AWS Parallel Computing Service** (AWS PCS), a new managed service that transforms how organizations operate HPC environments in the cloud. We'll demonstrate how PCS can eliminate operational overhead while preserving the familiar Slurm experience your users rely on. In real time, we'll build a production-ready HPC cluster that integrates elastic storage from both NFS and high-performance Lustre, along with advanced compute capabilities like GPUs and our EFA networking. We'll show you how a single infrastructure can efficiently support both large-scale simulation and model training workloads, simplify operations but maintaining the performance your applications demand.*

<a target="pcs" href="https://youtu.be/Vw0qT9vrhlY">{{< image src="/images/post/Vw0qT9vrhlY.png" class="vid" >}}</a>

##### Resources for PCS

We have a **LOT** of tutorials and recipes for on-boarding to PCS.

* We have a [playlist of all our PCS tutorials](https://www.youtube.com/playlist?list=PL6tstO5J3TRGPTfz6C4XY3gT6Fg70nAPN) in our Tech Shorts channel on YouTube.
* If you just want to [get started with one-click](https://youtu.be/Vw0qT9vrhlY), so you can kick the tires and see how PCS works, then go straight to [this tutorial](https://youtu.be/Vw0qT9vrhlY) from Matt Vaughn.

#### 12pm-1pm - **Deploy a Terascale Lustre file system In minutes, not months**
*Come see a live build of a massive **1 Terabyte per second shared file system using Amazon FSx for Lustre**. We’ll accelerate a large data-set from Amazon S3 and make use of file system semantics and metadata acceleration. You’ll get to see the simplicity of on-demand provisioning of an HPC cluster, too, faster than it took you to even specify the system you’re working on today.*

##### Resources

Amazon FSx for Lustre is probably one of the easiest services to launch and use. Randy Seamens does a great job of explaining it in both a [blog post](https://aws.amazon.com/blogs/hpc/build-and-deploy-a-1-tb-s-file-system-in-under-an-hour/), and a [Tech Short on YouTube](https://www.youtube.com/watch?v=Nm3j5PWPFrY) where you'll see it in action, driving up to 1 TByte/s of I/O.

There are also [some specific recipes](https://github.com/aws-samples/aws-hpc-recipes/tree/main/recipes/storage) available in the HPC Recipes Library, including for alternatives to Lustre if, for example, you're looking for a scalable solution to /home instead (in which case, check out [EFS Simple](https://github.com/aws-samples/aws-hpc-recipes/tree/main/recipes/storage/efs_simple)).

#### 1pm-2m - **Providing workspaces and visualization tool for data analysis, and managing budgets**
*With our Slurm cluster managed with AWS Parallel Computing Service, we’ll explore different options for the end-user experience. We’ll first use a PCS-managed group of Login nodes to provide SSH access to the cluster. Next, we’ll illustrate how you can “Bring your own Login node” to the Research and Engineering Studio (RES) on AWS to provide individual or shared virtual graphical desktops. We’ll demonstrate visualization capabilities using Paraview in RES, powered by Amazon DCV, with hooks into Slurm’s job management.*

##### Resources

You can find out more about **Research and Engineering Studio on AWS** from it's [homepage](https://aws.amazon.com/hpc/res/), our [walkthough video on Tech Shorts](https://www.youtube.com/watch?v=2Nku6MWDwT0). We've also published a [blog post](https://youtu.be/U7zue5GJwco) about RES-ready images for AWS ParallelCluster - this same option is also available for Parallel Computing Service, too - and we'll have a blog post coming on this topic in the next couple of weeks.

#### 2pm-3pm - **Building your performant applications on different architectures on AWS**
*Now we’ll explore how to build, optimize, and run codes on our clusters making use of the Elastic Fabric Adaptor (EFA) which supports all our CPU and GPU architectures. We’ll show a software build of OpenFOAM using Spack. Then we’ll test this build on multiple architectures, and discuss how to validate that the build has been built to leverage best of each underlying architecture. Finally, we’ll submit a large-scale batch array of simulations that we’ll use later for trainng an ML model for rapid automotive design.*

##### Resources

You'll probably have seen Matt or one of our other builders using Spack to install performant binaries from source **without any fuss**, and if this gets you interested in Spack, we think that's a great thing.

You can see Matt [installing Spack as part of a machine image pipeline](https://youtu.be/d_AUNURmhwY?si=sHVLJXnwFVgwTrY7&t=275) in EC2 Image Builder on Tech Shorts. If you need some background on why Spack helps, you can't do better than [this blog post from 2022](https://aws.amazon.com/blogs/hpc/introducing-the-spack-rolling-binary-cache/) (an oldie, but it's an ever green message).

AWS is a major sponsor of the [High Performance Software Foundation](https://hpsf.io), of which Spack is a founding project. We deeply believe in the important of open-source to the HPC community, and we encourage you to do a deep dive on Spack to see how it can help in your own environment.

#### 3pm-4pm - **Cloud native HPC: Taking a different path to the same destination (an end-to-end AI 4 CAE workflow)**
*So far we’ve shown how to recreate a traditional HPC environment on the cloud, giving your users with prior knowledge of HPC systems a robust and performant system to leverage for their research. What if your users are researchers have no prior knowledge of HPC and instead prefer to work in data science environments like Jupyter Notebooks? This sessions shows how you can leverage a cloud-native scheduler, AWS Batch, and a popular data science workflow framework, Metaflow, to achieve massive scale for your workloads.*

##### Resources

You'll see more on this in coming weeks as we prep some content around the work we've been doing with our friends from [MetaFlow](https://metaflow.org/).

#### 4pm-5pm - **Using advanced HPC to change how we do engineering design**
*We can now work through the whole workflow we’ve been building to show you a glimpse of the near future. The simulation runs we kicked off will now serve as a training dataset for building a deep-learning surrogate model. Then we’ll take a hundred unseen geometries and do large-scale batch-inference using the pre-trained models, visualizing the results with our graphical desktops.*

##### Resources

Neil Ashton has been leading this project in AWS, and has presented a number of papers on the topic. He stopped by Tech Shorts to talk about surrogate models and how they can be deployed in aerospace industries, and CAE more generally.

<a target="pcs" href="https://youtu.be/FVqPtpv210g">{{< image src="/images/post/FVqPtpv210g.png" class="vid" >}}</a>
<a target="pcs" href="https://youtu.be/s71vV-gi-ds">{{< image src="/images/post/s71vV-gi-ds.png" class="vid" >}}</a>
