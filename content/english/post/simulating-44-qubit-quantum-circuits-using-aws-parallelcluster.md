---
title: "Simulating 44-Qubit quantum circuits using AWS ParallelCluster"
date: 2022-08-30T00:00:00-0700
# post thumb
images:
    - "images/post/CleanShot-2022-08-03-at-12.25.24-1260x627.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: [ "AWS ParallelCluster", ]
tags: [ "Quantum technologies",  "ParallelCluster",  "Simulation",  "Center for Quantum Computing",  "HPC",  "Quantum Technologies",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

A key part of the development of quantum hardware and quantum algorithms is simulation using existing classical architectures and HPC techniques. In this blog post, we describe how to perform large-scale quantum circuits simulations using AWS ParallelCluster with QuEST, the Quantum Exact Simulation Toolkit. We demonstrate a simple and rapid deployment of computational resources up to 4,096 compute instances to simulate random quantum circuits with up to 44 qubits. We were able to allocate as many as 4096 EC2 instances of c5.18xlarge to simulate a non-trivial 44 qubit quantum circuit in fewer than 3.5 hours.

<a href="https://aws.amazon.com/blogs/hpc/simulating-44-qubit-quantum-circuits-using-aws-parallelcluster/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS Blog Channel</a>