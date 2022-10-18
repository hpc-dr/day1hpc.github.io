---
title: "Interesting GPU & CPU performance results from GROMACS"
date: 2021-05-06T16:33:38+0000
# post thumb
images:
    - "images/post/Zz91uPbk12Y.png"
author: "Brendan Bouffler"
# description
description: ""
video_id: "Zz91uPbk12Y"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Life Sciences", ]
tags: [ "Drug Discovery",  "Computational Chemistry",  "CPUs",  "MD",  "High Performance Computing",  "GPUs",  "GROMACS",  "HPC",  "ParallelCluster",  "EC2",  "Schedulers",  "virtualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Carsten Kutzner is a researcher and scientific software developer at the Max Planck Institute for Biophysical Chemistry in Göttingen in Germany. He's been doing some really diverse benchmarking studies in collaboration with our HPC engineering team, and he joins us today to talk about some of the results of that investigation.

What's most interesting (and soft of unexpected) is the instances he concludes are the best for the job - whether you're optimizing for sheer performance against the clock, or price performance because you need to maximize your budget within a more generous time window. No spoilers here: you need to hear him talk.

Molecular Dynamicists are used to doing these calculations because they measure their progress in nanoseconds of simulation time per DAY of wall clock time. As Carsten points out: if your job runs for days or weeks, it matters whether you can squeeze 10% more from the compute units it's running on.

In the talk we mention his a few resources, and here's the links:

* Karsten's home page with a trove of great data: https://www.mpibpc.mpg.de/grubmueller/bench
* Christian's workshop to guide you setting up the exact same infrastructure that Carsten uses: https://gromacs-on-pcluster.workshop.aws/
* Austin's blog post from a few weeks ago about GROMACS performance comparisons on CPUs. https://aws.amazon.com/blogs/hpc/gromacs-price-performance-optimizations-on-aws/
* Austin's talk a couple weeks ago about how to build these clusters to run this kind of benchmark operation: https://www.youtube.com/watch?v=ubAvlgNN9PQ

As usual, if you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube Zz91uPbk12Y >}}