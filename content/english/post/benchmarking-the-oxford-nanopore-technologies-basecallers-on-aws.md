---
title: "Benchmarking the Oxford Nanopore Technologies basecallers on AWS"
date: 2023-05-18T00:00:00-0700
# post thumb
images:
    - "images/post/HPCBlog-205-header-1120x630.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "Life Sciences",  "AWS Batch", ]
tags: [ "Life Sciences",  "HPC",  "Batch",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

Oxford Nanopore sequencers enables direct, real-time analysis of long DNA or RNA fragments. They work by monitoring changes to an electrical current as nucleic acids are passed through a protein nanopore. The resulting signal is decoded to provide the specific DNA or RNA sequence by virtue of  compute-intensive algorithms called basecallers. This blog post presents the benchmarking results for two of those Oxford Nanopore basecallers — Guppy and Dorado — on AWS. This benchmarking project was conducted in collaboration between G42 Healthcare, Oxford Nanopore Technologies and AWS.

<a href="https://aws.amazon.com/blogs/hpc/benchmarking-the-oxford-nanopore-technologies-basecallers-on-aws/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS Blog Channel</a>