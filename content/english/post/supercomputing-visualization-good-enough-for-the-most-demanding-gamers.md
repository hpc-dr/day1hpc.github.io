---
title: "Supercomputing Visualization good enough for the most demanding gamers."
date: 2021-04-22T15:16:21+0000
# post thumb
images:
    - "images/post/_L-U_ET4qrw.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "_L-U_ET4qrw"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon NICE DCV", ]
tags: [ "HPC",  "High Performance Computing",  "CPUs",  "Schedulers",  "Storage",  "EC2",  "DCV",  "GPUs",  "Lustre",  "ParallelCluster",  "vizualization",  "virtualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

DCV was originally created for scientists and engineers who run thing on supercomputers. They needed to visualize massive datasets produced by really large compute workloads crunching petabytes of data. That takes some fast machines and some very fancy GPUs. Since we don’t like putting scientist into freezing data centers our DCV engineers worked out how to push pixels over the internet quickly, without any loss of fidelity.

Fast forward 20 years and a generation of gamers want to do the same thing, only this time there are way more pixels (blame HD and 4k) and it’s 60 frames per second, or bust.

That meant we had to so some extra tricks to make video streams not miss a beat when very normal things happen, like the internet drops a packet or there’s some congestion because your mum is on a zoom call with her team at the office.

Our senior software engineer, Marco Mastropaolo leads us through the things we’ve done with DCV to make it work for both HPC, and the gamers.

During the discussion, we mentioned Marco’s detailed talk at NVIDIA’s GTC 21. That’s here: https://tinyurl.com/dcvgtc21

More about DCV is here: https://aws.amazon.com/hpc/dcv/

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube _L-U_ET4qrw >}}