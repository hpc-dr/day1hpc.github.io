---
title: "How to manage HPC jobs using a serverless API"
date: 2021-11-17T00:00:00-0800
# post thumb
images:
    - "images/post/dalle-hpc-01.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "AWS ParallelCluster", ]
tags: [ "Serverless Application Model",  "API Gateway",  "HPC",  "Lambda",  "ParallelCluster",  "Systems Manager",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

HPC systems are traditionally access through a Command Line Interface (CLI) where the users submit and manage their computational jobs. Depending on their experience and sophistication, the CLI can be a daunting experience for users not accustomed in using it. Fortunately, the cloud offers many other options for users to submit and manage their computational jobs. In this blog post we will cover how to create a serverless API to interact with an HPC system in the the cloud built with AWS ParallelCluster.

<a href="{{ url }}" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS HPC Blog</a>