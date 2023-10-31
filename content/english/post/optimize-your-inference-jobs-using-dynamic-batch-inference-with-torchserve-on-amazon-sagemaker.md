---
title: "Optimize your inference jobs using dynamic batch inference with TorchServe on Amazon SageMaker"
date: 2022-01-12T00:00:00-0800
# post thumb
images:
    - "images/post/dalle-hpc-01.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "AWS Batch", ]
tags: [ "Batch",  "Modeling",  "SageMaker",  "Artificial Intelligence",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

In deep learning, batch processing refers to feeding multiple inputs into a model. Although it’s essential during training, it can be very helpful to manage the cost and optimize throughput during inference time as well. Hardware accelerators are optimized for parallelism, and batching helps saturate the compute capacity and often leads to higher throughput. Batching […]

<a href="https://aws.amazon.com/blogs/machine-learning/optimize-your-inference-jobs-using-dynamic-batch-inference-with-torchserve-on-amazon-sagemaker/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS Blog Channel</a>