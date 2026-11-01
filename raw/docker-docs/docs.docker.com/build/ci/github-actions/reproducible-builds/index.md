---
{"title": "Reproducible builds with GitHub Actions", "url": "https://docs.docker.com/build/ci/github-actions/reproducible-builds/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Reproducible builds with GitHub Actions {#reproducible-builds-with-github-actions pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

`SOURCE_DATE_EPOCH` is a [standardized environment variable](https://reproducible-builds.org/docs/source-date-epoch/) for instructing build tools to produce a reproducible output. Setting the environment variable for a build makes the timestamps in the image index, config, and file metadata reflect the specified Unix time.

To set the environment variable in GitHub Actions, use the built-in `env` property on the build step.

## [Unix epoch timestamps](#unix-epoch-timestamps) {#unix-epoch-timestamps .scroll-mt-20 .flex .items-center .gap-2}

The following example sets the `SOURCE_DATE_EPOCH` variable to 0, Unix epoch.

``` {.chroma tabindex="0"}
name: ci

on:
  push:

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v4

      - name: Build
        uses: docker/build-push-action@v7
        with:
          tags: user/app:latest
        env:
          SOURCE_DATE_EPOCH: 0
```

``` {.chroma tabindex="0"}
name: ci

on:
  push:

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v4

      - name: Build
        uses: docker/bake-action@v7
        env:
          SOURCE_DATE_EPOCH: 0
```

## [Git commit timestamps](#git-commit-timestamps) {#git-commit-timestamps .scroll-mt-20 .flex .items-center .gap-2}

The following example sets `SOURCE_DATE_EPOCH` to the Git commit timestamp.

``` {.chroma tabindex="0"}
name: ci

on:
  push:

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v4

      - name: Get Git commit timestamps
        run: echo "TIMESTAMP=$(git log -1 --pretty=%ct)" >> $GITHUB_ENV

      - name: Build
        uses: docker/build-push-action@v7
        with:
          tags: user/app:latest
        env:
          SOURCE_DATE_EPOCH: ${{ env.TIMESTAMP }}
```

``` {.chroma tabindex="0"}
name: ci

on:
  push:

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v4

      - name: Get Git commit timestamps
        run: echo "TIMESTAMP=$(git log -1 --pretty=%ct)" >> $GITHUB_ENV

      - name: Build
        uses: docker/bake-action@v7
        env:
          SOURCE_DATE_EPOCH: ${{ env.TIMESTAMP }}
```

## [Additional information](#additional-information) {#additional-information .scroll-mt-20 .flex .items-center .gap-2}

For more information about the `SOURCE_DATE_EPOCH` support in BuildKit, see [BuildKit documentation](https://github.com/moby/buildkit/blob/master/docs/build-repro.md#source_date_epoch).
