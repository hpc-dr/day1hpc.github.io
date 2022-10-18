---
title: "Introducing fair-share scheduling for AWS Batch"
date: 2021-11-09T00:00:00-0800
# post thumb
images:
    - "images/post/hpcblog-72-f6.gif"
#author
author: "Matt Vaughn"
# description
description: ""
# Taxonomies
categories: [ "AWS Batch", ]
tags: [ "Batch",  "HPC",  "Product Launch",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

Today we are announcing fair-share scheduling (FSS) for AWS Batch, which provides fine-grain control of the scheduling behavior by using a scheduling policy. With FSS, customers can prevent “unfair” situations caused by strict first-in, first-out scheduling where high priority jobs can’t “jump the queue” without draining other jobs first. You can now balance resource consumption between groups of workloads and have confidence that the shared compute environment is not dominated by a single workload. In this post, we’ll explain how fair-share scheduling works in more detail. You’ll also find a link to a step-by-step workshop at the end of this post, so you can try it out yourself.

Read the full post at the [AWS HPC Blog](https://aws.amazon.com/blogs/hpc/introducing-fair-share-scheduling-for-aws-batch/).
