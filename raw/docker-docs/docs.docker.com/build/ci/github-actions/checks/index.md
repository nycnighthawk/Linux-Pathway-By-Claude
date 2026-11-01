---
{"title": "Validating build configuration with GitHub Actions", "url": "https://docs.docker.com/build/ci/github-actions/checks/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Validating build configuration with GitHub Actions {#validating-build-configuration-with-github-actions pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

[Build checks](https://docs.docker.com/build/checks/) let you validate your `docker build` configuration without actually running the build.

## [Run checks with `docker/build-push-action`](#run-checks-with-dockerbuild-push-action) {#run-checks-with-dockerbuild-push-action .scroll-mt-20 .flex .items-center .gap-2}

To run build checks in a GitHub Actions workflow with the `build-push-action`, set the `call` input parameter to `check`. With this set, the workflow fails if any check warnings are detected for your build\'s configuration.

``` {.chroma tabindex="0"}
name: ci

on:
  push:

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - name: Login to Docker Hub
        uses: docker/login-action@v4
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v4

      - name: Validate build configuration
        uses: docker/build-push-action@v7
        with:
          call: check

      - name: Build and push
        uses: docker/build-push-action@v7
        with:
          push: true
          tags: user/app:latest
```

## [Run checks with `docker/bake-action`](#run-checks-with-dockerbake-action) {#run-checks-with-dockerbake-action .scroll-mt-20 .flex .items-center .gap-2}

If you\'re using Bake and `docker/bake-action` to run your builds, you don\'t need to specify any special inputs in your GitHub Actions workflow configuration. Instead, define a Bake target that calls the `check` method, and invoke that target in your CI.

``` {.chroma tabindex="0"}
target "build" {
  dockerfile = "Dockerfile"
  args = {
    FOO = "bar"
  }
}
target "validate-build" {
  inherits = ["build"]
  call = "check"
}
```

``` {.chroma tabindex="0"}
name: ci

on:
  push:

env:
  IMAGE_NAME: user/app

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - name: Login to Docker Hub
        uses: docker/login-action@v4
        with:
          username: ${{ vars.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v4

      - name: Validate build configuration
        uses: docker/bake-action@v7
        with:
          targets: validate-build

      - name: Build
        uses: docker/bake-action@v7
        with:
          targets: build
          push: true
```

### [Using the `call` input directly](#using-the-call-input-directly) {#using-the-call-input-directly .scroll-mt-20 .flex .items-center .gap-2}

You can also set the build method with the `call` input which is equivalent to using the `--call` flag with `docker buildx bake`

For example, to run a check without defining `call` in your Bake file:

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

      - name: Validate build configuration
        uses: docker/bake-action@v7
        with:
          targets: build
          call: check
```
