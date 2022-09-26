## Get Started

```shell
brew install hugo
```

## Check out and test the repo

The site is published off the `prod` branch. 

```shell
git clone day1hpc/day1hpc.github.io@prod
cd day1hpc.github.io
# start server with drafts enabled
hugo server -D
```

## Create or edit content
```shell
git checkout staging
# create a branch to hold your work
git checkout -b <BRANCH_NAME>
# start server with drafts enabled
hugo server -D
# do your work
# commit to BRANCH_NAME
# merge to staging
# open a PR to prod branch
```

