---
title: "AWS Batch's new Faster Scaling features"
date: 2021-04-15T16:50:36+0000
# post thumb
images:
    - "images/post/uQCUpw7uSjY.png"
author: "Brendan Bouffler"
# description
description: " (reposted from HPC Tech Shorts Youtube channel)"
video_id: "uQCUpw7uSjY"
layout: "video"
# Taxonomies
categories: []
tags: [ "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Our AWS Batch development team have been working on some major improvements to the way Batch assesses the need to scale up or down. We’re doing 5x as many scaling evaluations per hour now which should pick up the pace significantly. With some other improvements which we talk about in the video, we’re hoping customers will see less throttling on the submitjob API call and just see an overall faster submission rate, and faster time to results (since that’s what really matters).

Jo Adegbola is the Sr Manager of all of our AWS Batch software engineering teams and works closely with Steve Kendrex the Principal Product Manager for Batch obsessing on how to “make stuff go fast” for Batch users everywhere.

During the show we referred to a couple of paths to get started on Batch.


1. A tutorial to get started with simple jobs on Batch running in EC2 Spot: https://aws.amazon.com/getting-started/hands-on/run-batch-jobs-at-scale-with-ec2-spot/
2. A workshop for scientists who use NextFlow to run genomics pipelines on Batch: https://genomics-nf.workshop.aws (https://genomics-nf.workshop.aws/)

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube uQCUpw7uSjY >}}