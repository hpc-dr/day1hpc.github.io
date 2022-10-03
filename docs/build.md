## Get Started

```shell
brew install hugo
```

## Check out and test the repo

The site is published off the `prod` branch. 

```shell
git clone day1hpc/day1hpc.github.io@main
cd day1hpc.github.io
# start server with drafts enabled
hugo server -D
```

## Create or edit content and posts
```shell
git checkout staging
# create a branch to hold your work
git checkout -b <BRANCH_NAME>
# start server with drafts enabled
hugo server -D
# do your work
# view your live site on http://localhost:1313/ (it will autoreload your changes as you go)
# when done, commit to BRANCH_NAME
# merge to staging
# open a PR to main branch to merge in staging 
# accept PR on Github site (we will eventually enforce this workflow via repo settings)
# site will update after Github action runs
```

### CICD

There is a publication workflow for building the hugo site and making it available via Github pages at `.github/workflows/pages.yml`. We should not generally need to touch it.

## Repo Structure

Posts are all in `content/english`. Create a new one with: 

```shell
cd day1hpc.github.io
hugo new post/my-first-post.md
```

Images and other media are in `assets/images`. We are trying to keep them further partitioned by post type, so keep the ones embedded in posts in `assets/images/post`.

Other files (about, etc) are at the top level of the `content` directory and are directly editable. 

### Archetypes

Hugo supports templates for content types. The template for new files in the `author` and `post` types are stored in `archetypes/author.md` and `archetypes/post.md` respectively. In theory, we can create multiple kinds of post, each with different templates, to help streamline our work. 

### Front Matter

```yaml
---
title: "AWS Batch"
date: 2022-09-26T13:29:51-05:00
#author
author: "Angel Pizarro"
# description
description: "This is meta description"
images:
  - "images/post/Batch.png"
# Taxonomies
categories: ["photography"]
tags: ["photo","image"]
type: "featured" # available type (regular or featured)
draft: false
---
```

Each post needs accurate metadata, which is found in its front matter YAML. 
* title: Public title of the page
* date: Displayed creation date
* author: One of the folks named in `content/english/author`
* description: SEO description of the post. Important for Google and other engines. 
* images: one or more featured images in the post. Providing more than one will activate a carousel display.
* categories and tags: site taxonomy
* type: either `featured` (prominent on home page and in hero carousel) or `regular`
* draft: in progress. Will be shown locally in Hugo "drafts mode" but not on public site

## Configuration & Organization

### General

General config is managed by `config/_default/config.toml` and `config/_default/params.toml`.  There are many knobs to tweak in the params file.

### Menus

These are controlled by `config/_default/menus.en.toml`. Can have single-level menus **or** drop-downs.

## Internationalization

The theme is designed to support multiple lanaguages. This means a lot of the boilerplate text around the site is represented as variables defined in the `i18n` directory. An example is the string `Continue Reading` which is rendered from the embedded text slug `continue_reading`. This is important to know if you want to change the boilerplate text, as you will find a bunch of `{{text}}` type content in the files that create it.


## Theme

The theme files are in `themes/logbook-hugo`. I have avoided editing them until I run into a problem that cannot be solved by some other means. Editing themes is a bit of a 1-way door in that we will have to sync up any changes made there with future releases of the theme. 

