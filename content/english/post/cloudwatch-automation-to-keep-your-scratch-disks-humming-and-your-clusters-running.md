---
title: "CloudWatch automation to keep your scratch disks humming, and your clusters running."
date: 2021-06-10T15:19:32+0000
# post thumb
images:
    - "images/post/oFYzPXNoMYo.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "oFYzPXNoMYo"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon NICE DCV",  "Life Sciences", ]
tags: [ "Amazon S3",  "CPUs",  "Covid-19",  "DCV",  "EC2",  "GPUs",  "HPC",  "High Performance Computing",  "Lustre",  "ParallelCluster",  "Schedulers",  "Storage",  "object storage",  "openfoam",  "virtualization",  "vizualization",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Some workloads generate a LOT of output files and sometimes quite suddenly. For codes like OpenFOAM, this is data that you may not need until later when you run a post-processing job.

Given the amount of data isn’t always predictable, there are a few ways to prepare for this deluge, but most of them involve pre-provisioning too much storage in advance (and hoping you guessed correctly).

We’ve never been fans of guessing like that - we think infrastructure should just expand when you need it.

Stephen Sachs from our HPC Performance Engineering team came up with a great technique for solving this. He’s built some cloud automation with CloudWatch into AWS ParallelCluster so it triggers a “drain” process (a shell script) that pushes all the output files into Amazon S3 whenever the local filesystem on a compute instance reaches 80%. It’s surprisingly easy to do.

Even if this isn’t the exact problem you’re trying to solve it’s a great thought process because it takes much of the automation outside the scheduler, outside the cluster even, and makes it really easy to set up, and really visible and auditable. You can even see plots of the activity.

During the discussion, a GitHub repo with the sample shell scripts that you can steal and repurpose to your needs. They’re here:  https://github.com/stephenmsachs/s3-openfoam

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube oFYzPXNoMYo >}}