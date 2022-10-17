---
title: "Pushing pixels with NICE DCV"
date: 2021-07-30T00:00:00-0700
# post thumb
images:
    - "images/post/dalle-hpc-01.png"
#author
author: "Matt Vaughn"
# description
description: ""
# Taxonomies
categories: []
tags: [ "HPC",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

NICE DCV, our high-performance, low-latency remote-display protocol, was originally created for scientists and engineers who ran large workloads on far-away supercomputers, but needed to visualize data without moving it. Pushing pixels over limited bandwidth across the globe has been the goal of the DCV team since 2007. DCV was able to make very frugal use of very scarce bandwidth, because it was super lean, used data-compression techniques and quickly adopted cutting-edge technologies of the time from GPUs (this is HPC, after all, we left nothing on the table when it came to exploiting new gadgets). This allowed the team to create a super light-weight visualization package that could stream pixels over almost any network. Fast forward to the 2020s, and a generation of gamers, artists, and film-makers all want to do the same thing as HPC researchers- only this time there are way more pixels, because we now have HD and 4k (and some people have multiple), and for most of them, it’s 60 frames per second, or it’s not worth having. Today we have around 12x the number of pixels, and around 3x the frame rate compared to TV of circa 2007. Fortunately, networking improved a lot in that time: a high-end user’s broadband connection grew around 60x in bandwidth, but the 120x growth in computing power really tipped the balance in favor of bringing remote streaming to the masses. Still, physics remains, meaning the latency forced on us by the curvature of the earth and the speed of light, is still a challenge. We still haven’t beaten physics, but we’re making up for it by building our own global fiber network and adding more machinery (and in local and wavelength zones) to get closer to more customers as soon as we can.

Read the full post at the [AWS HPC Blog](https://aws.amazon.com/blogs/hpc/pushing-pixels-with-nice-dcv/).
