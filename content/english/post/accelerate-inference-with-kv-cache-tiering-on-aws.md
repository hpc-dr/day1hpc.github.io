---
title: "Accelerate inference with KV cache tiering on AWS"
date: 2026-09-21T00:00:00-0700
# post thumb
images:
    - "images/post/Arch_Amazon-FSx-for-Lustre_64@5x.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: []
tags: [ "Modeling",  "Storage",  "FSx for Lustre",  "Trainium",  "Simple Storage Service (S3)",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

When running large language model (LLM) inference at scale on AWS, the GPU might not be the only thing that limits you. The GPU generates tokens fast, but what then contributes to performance is everything around it: memory, storage, and the network path that connects them. That’s the difference between a demo and production. Training […]

<a href="/blogs/storage/accelerate-inference-with-kv-cache-tiering-on-aws/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS Blog Channel</a>