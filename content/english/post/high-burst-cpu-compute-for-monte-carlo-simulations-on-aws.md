---
title: "High Burst CPU Compute for Monte Carlo Simulations on AWS"
date: 2021-09-01T00:00:00-0700
# post thumb
images:
    - "images/post/mc-playtech-header-1260x630.png"
#author
author: "Matt Vaughn"
# description
description: " (reposted from AWS HPC Blog)"
# Taxonomies
categories: []
tags: [ "API Gateway",  "HPC",  "Serverless",  "Lambda",  "Simulation",  "hpcblog", ]
type: "regular" # available type (regular or featured)
draft: false
---

Playtech mathematicians and game designers need accurate, detailed game play simulation results to create fun experiences for players. While software developers have been able to iterate on code in an agile manner for many years, for non-analytical solutions, mathematicians have had to rely on slow CPU-bound Monte-Carlo simulations, waiting, as software engineers once did, many hours or overnight to get the results of their latest changes. These statistics are also required as evidence of game fairness in the highly regulated online gaming business. Playtech has developed an AWS Lambda Serverless based solution that provides massive burst compute performance that allows game simulations in minutes rather than hours. This post goes into the details of the architecture, as well as some examples of using the system in our development and operations.

<a href="{{ url }}" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" style="margin-top: 8px;">Read the Post on the AWS HPC Blog</a>