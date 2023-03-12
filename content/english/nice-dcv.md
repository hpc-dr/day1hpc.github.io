---
title: "NICE DCV"
date: 2022-11-13
#author
author: "Brendan Bouffler"
layout: "product"
# description
description: "NICE DCV is a high performance, low latency pixel streaming protocol that encrypts and transports pixels to devices, putting your desktop closer to your results. You can access, manipulate, and share business-critical information, regardless of your location, over local networks or the internet."
images:
  - "images/hpc/Ident-DCV@3x.webp"
product_images:
  - "images/g3/ksp-dcv-title.webp"
  - "images/g3/ksp-dcv-desktop.webp"
  - "images/g3/ksp-dcv-adaptable.webp"
  - "images/g3/ksp-dcv-secure.webp"
  - "images/g3/ksp-dcv-versatile.webp"
  - "images/g3/ksp-dcv-sdk.webp"        
# Taxonomies
categories: ["NICE DCV", "products"]
tags: ["streaming","visualization"]
type: "featured" # available type (regular or featured)
draft: false
---

NICE DCV is a **high performance, low latency pixel streaming protocol** that encrypts and transports pixels to devices, putting your desktop closer to your results. With NICE DCV, you can access, manipulate, and share business-critical information, regardless of your location, over local networks or the internet.

DCV makes *very* frugal use of scarce bandwidth, because it's super-lean, uses data-compression techniques, and has always quickly adopted cutting-edge technologies (this is HPC, after all, we leave nothing on the table when it came to exploiting new gadgets).

DCV is tightly integrated into ParallelCluster and [PCluster Manager](https://youtu.be/PChP3FQWeJQ) (our UI for building and managing clusters).

### A desktop ... in a web browser?

DCV also has a Web SDK which means you can offer your end users virtual desktops embedded in browser tabs (check out the [talk from Moichelle Brenner from Netflix](https://youtu.be/PUAeBQ98Odc) about how they did just that for their global network of editors). DCV is now deeply embedded in their video production workflows (which we all benefit from).

All of this is what makes DCV a light-weight visualization package that can stream pixels over almost any network. So lean, in fact, that with reasonable bandwidth most users can't tell that the data and the server are hundreds, or sometimes thousands of miles away.

### What's behind DCV?

DCV is another example of great tech that was born in HPC, but has expanded to a lot of places we never imagined - including desktop gaming.

<div class="row">
<div class="col">
{{< collapse "Learn more about NICE DCV" >}}
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
| [The evolution of NICE DCV](https://aws.amazon.com/blogs/hpc/pushing-pixels-with-nice-dcv/) | [Supercomputing visualization good enough for gamers](https://youtu.be/_L-U_ET4qrw) |
| [An overview of DCV](https://youtu.be/-mhNktbKmAc) | Impact of video quality on bitrates **[[Blog]](https://aws.amazon.com/blogs/hpc/putting-bitrates-into-perspective/)** **[[Video]](https://www.youtube.com/watch?v=-YBh4d_zKxc)** |
{{</ collapse >}}

</div>
</div>

----

### DCV in gaming

<style>
.screenshot {
  float:right !important;
  width:500px;
  padding: 10px;
  }
</style>

{{< image src="/images/post/dcv-gamers-screenshot-1.png" class="screenshot" >}}

Most of the techniques that DCV uses to minimize the effects of internet jitter and unpredictable latency, work really well for cloud gaming, too.

- **[Pushing pixels with NICE DCV](https://aws.amazon.com/blogs/hpc/pushing-pixels-with-nice-dcv/)** - a short post explaining where DCV came from and how it solves some hard problems in novel ways.
- **[Supercomputing visualization good enough for the most demanding gamers](https://youtu.be/_L-U_ET4qrw)** - an insight into some of DCV's tricks (like the QUIC transport layer) that minimize jitter and make the remote desktop feel like it's local. It worked so well, it's now used for gaming.

## Getting started with DCV

It's easy to get started with DCV:

1. **[DCV Preconfigured AMI](https://aws.amazon.com/marketplace/seller-profile?id=74eff437-1315-4130-8b04-27da3fa01de1)** - this AMI is in AWS Marketplace, and is available for Windows and Linux server versions - includiong options for G4 and G5 Amazon EC2 instances, which are GPU enabled. 
2. **[Preconfigured DCV EC2 instance with CloudFormation](https://download.nice-dcv.com/cloudformation.html)** - you can launch using an AWS CloudFormation template, which we provide.
3. **[Install DCV Manually](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up.html)** - you can install manually, which makes more sense if you're plannign to use DCV in a more taylored configuration.
