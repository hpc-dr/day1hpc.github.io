---
title: "Deep dive into the AWS ParallelCluster 3 configuration file"
date: 2021-11-15T00:00:00-0800
# post thumb
images:
    - "images/post/pc3-header-1260x630.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "AWS ParallelCluster", ]
tags: [ "HPC",  "ParallelCluster",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

In September, we announced the release of AWS ParallelCluster 3, a major release with lots of changes and new features. To help get you started migrating your clusters, we provided the Moving from AWS ParallelCluster 2.x to 3.x guide. We know moving versions can be a quite an undertaking, so we’re augmenting that official documentation with additional color and context on a few key areas. With this blog post, we’ll focus on the configuration file format changes for ParallelCluster 3, and how they map back to the same configuration sections for ParallelCluster 2.

<a href="https://aws.amazon.com/blogs/hpc/deep-dive-into-the-aws-parallelcluster-3-configuration-file/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS Blog Channel</a>