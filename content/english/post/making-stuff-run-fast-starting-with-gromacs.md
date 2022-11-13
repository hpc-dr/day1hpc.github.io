---
title: "'Making stuff run fast', starting with GROMACS."
date: 2021-04-08T15:00:15+0000
# post thumb
images:
    - "images/post/ubAvlgNN9PQ.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "ubAvlgNN9PQ"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon NICE DCV",  "Life Sciences", ]
tags: [ "HPC",  "High Performance Computing",  "CPUs",  "Schedulers",  "Storage",  "GROMACS",  "EC2",  "DCV",  "GPUs",  "molecular dynamics",  "Lustre",  "ParallelCluster",  "vizualization",  "virtualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

We just published a blog post last week with a deep dive into what makes GROMACS tick. The blog post talked about software stacks and EC2 instances that will deliver the best possible performance for people trying to do some molecular dynamics quickly. This turns out to be pretty much EVERYONE in the MD community, because these are people who measure their progress in nanoseconds of simulation PER DAY of wall clock time.

Austin Cherian is one of our senior engineers in the Developer Relations team, and the one who is the most obsessed with performance and getting the performance testing methodology right. We asked him to join tech shorts this week to show us how he uses and abuses AWS ParallelCluster in his quest of “making stuff go fast”, because his use cases are pretty common, and might help you imagine some better ways of working.

During the discussion, he talks about his blog post which you can find here: https://aws.amazon.com/blogs/hpc/gromacs-price-performance-optimizations-on-aws/

We also mention the step-by-step workshop for running this environment on AWS ParallelCluster, and that’s here: https://gromacs-on-pcluster.workshop.aws/setup.html

Last but not least, check out the new HPC blog channel because you’ll find loads of articles from HOWTOs through to useful stories from customers and other builders who’ve helped make the cloud a more awesome experience for HPC.  https://aws.amazon.com/blogs/hpc

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube ubAvlgNN9PQ >}}