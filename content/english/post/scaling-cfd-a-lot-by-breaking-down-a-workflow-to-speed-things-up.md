---
title: "Scaling CFD a lot by breaking down a workflow, to speed things up"
date: 2022-03-03T17:26:49+0000
# post thumb
images:
    - "images/post/F8YzcuYr7YI.png"
author: "Brendan Bouffler"
# description
description: ""
video_id: "F8YzcuYr7YI"
layout: "video"
# Taxonomies
categories: [ "AWS ParallelCluster",  "Amazon NICE DCV",  "Life Sciences", ]
tags: [ "hierarchical",  "Schedulers",  "snappyHexMesh",  "Meshing",  "Covid-19",  "CPUs",  "GPUs",  "Domain Decomposition",  "Storage",  "EC2",  "High Performance Computing",  "Lustre",  "Solver performance",  "HPC",  "redistributePar",  "DCV",  "vizualization",  "CFD",  "scotch",  "openfoam",  "virtualization",  "clusters",  "ParallelCluster",  "techshorts", ]
type: "regular" # available type (regular or featured)
draft: false
---

Sometimes when we're looking for performance we lose the forrest for all those trees - we miss the huge improvements we can do to unglamorous parts of the overall workflow, while we obsess on the pieces that look hard. It's an engineer thing, I think.

In today's Tech Short, Neil Ashton shows us exactly this kind of example from the world of CFD (using OpenFOAM, but this lesson applies generally) - and shows us how to break the problem down in order to speed it all up - and pretty easily, too.

The workshops we reference in the discussion are all listed here: https://aws.amazon.com/hpc/cfd/

If you have ideas for technical topics you'd like to see us cover in a future show, let us know by finding us on Twitter (@TechHpc) and DM'ing us with your idea.

{{< youtube F8YzcuYr7YI >}}