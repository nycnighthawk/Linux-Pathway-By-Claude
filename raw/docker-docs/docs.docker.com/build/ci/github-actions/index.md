---
{"title": "Docker Build GitHub Actions", "url": "https://docs.docker.com/build/ci/github-actions/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Docker Build GitHub Actions {#docker-build-github-actions pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

GitHub Actions is a popular CI/CD platform for automating your build, test, and deployment pipeline. Docker provides a set of official GitHub Actions for you to use in your workflows. These official actions are reusable, easy-to-use components for building, annotating, and pushing images.

The following GitHub Actions are available:

-   [Build and push Docker images](https://github.com/marketplace/actions/build-and-push-docker-images): build and push Docker images with BuildKit.
-   [Docker Buildx Bake](https://github.com/marketplace/actions/docker-buildx-bake): enables using high-level builds with [Bake](https://docs.docker.com/build/bake/).
-   [Docker Login](https://github.com/marketplace/actions/docker-login): sign in to a Docker registry.
-   [Docker Setup Buildx](https://github.com/marketplace/actions/docker-setup-buildx): creates and boots a BuildKit builder.
-   [Docker Metadata action](https://github.com/marketplace/actions/docker-metadata-action): extracts metadata from Git reference and GitHub events to generate tags, labels, and annotations.
-   [Docker Setup Compose](https://github.com/marketplace/actions/docker-setup-compose): installs and sets up [Compose](https://docs.docker.com/compose/).
-   [Docker Setup Docker](https://github.com/marketplace/actions/docker-setup-docker): installs Docker Engine.
-   [Docker Setup QEMU](https://github.com/marketplace/actions/docker-setup-qemu): installs [QEMU](https://github.com/qemu/qemu) static binaries for multi-platform builds.
-   [Docker Scout](https://github.com/docker/scout-action): analyze Docker images for security vulnerabilities.

Using Docker\'s actions provides an easy-to-use interface, while still allowing flexibility for customizing build parameters.

> Note
>
> For an alternative to configuring individual actions, see [Docker GitHub Builder](https://docs.docker.com/build/ci/github-actions/github-builder/). It provides Docker-maintained reusable workflows for building images and artifacts with BuildKit.

## [Get started](#get-started) {#get-started .scroll-mt-20 .flex .items-center .gap-2}

Build an image from your GitHub repository and push it to Docker Hub with the following workflow.

### [Prerequisites](#prerequisites) {#prerequisites .scroll-mt-20 .flex .items-center .gap-2}

-   A GitHub repository with your application and a `Dockerfile` at its root.
-   A Docker Hub account and a [personal access token](https://docs.docker.com/security/access-tokens/personal-access-tokens/) with permission to push images.

### [Configure your GitHub repository](#configure-your-github-repository) {#configure-your-github-repository .scroll-mt-20 .flex .items-center .gap-2}

Add your Docker Hub credentials to your GitHub repository:

1.  Open your repository\'s **Settings**.
2.  Under **Security**, go to **Secrets and variables \> Actions**.
3.  Under **Secrets**, create a repository secret named `DOCKERHUB_TOKEN` containing your Docker access token.
4.  Under **Variables**, create a repository variable named `DOCKERHUB_USERNAME` containing your Docker Hub username.

### [Set up your GitHub Actions workflow](#set-up-your-github-actions-workflow) {#set-up-your-github-actions-workflow .scroll-mt-20 .flex .items-center .gap-2}

Create `.github/workflows/docker-ci.yml` in your repository with the following contents. Replace `my-image` with the name of your Docker Hub repository, and change `main` if your default branch has a different name.

``` {.chroma tabindex="0"}
name: Build and push Docker image

on:
  push:
    branches:
      - main
  pull_request:

permissions:
  contents: read

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Extract Docker image metadata
        id: meta
        uses: docker/metadata-action@v6
        with:
          images: ${{ vars.DOCKERHUB_USERNAME }}/my-image

      - name: Sign in to Docker Hub
        if: github.event_name != 'pull_request'
        uses: docker/login-action@v4
        with:
          username: ${{ vars.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v4

      - name: Build and push Docker image
        uses: docker/build-push-action@v7
        with:
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          annotations: ${{ steps.meta.outputs.annotations }}
```

Commit the workflow file and push it to your default branch to run it. The workflow also runs on pull requests. Pull-request builds skip signing in to Docker Hub and pushing the image, so they don\'t require registry secrets, including for pull requests from forks.

The build action uses Git context by default: BuildKit fetches your repository directly at the Git reference for the event that triggered the workflow, so no checkout step is needed. Changes to files made by earlier workflow steps are ignored because the build uses files from Git.

The metadata action generates tags, labels, and annotations from the GitHub event and passes them to the build step. For example, a push to `main` publishes `DOCKERHUB_USERNAME/my-image:main`. See [Manage tags and labels](https://docs.docker.com/build/ci/github-actions/manage-tags-labels/) and [Annotations](https://docs.docker.com/build/ci/github-actions/annotations/) to customize this metadata.

This workflow builds images but doesn\'t run application tests. To add tests, see [Test before push](https://docs.docker.com/build/ci/github-actions/test-before-push/). For additional build options, see [Multi-platform images](https://docs.docker.com/build/ci/github-actions/multi-platform/) and [SBOM and provenance attestations](https://docs.docker.com/build/ci/github-actions/attestations/), which covers default provenance and how to add SBOM attestations when pushing to a registry.

## [Examples](#examples) {#examples .scroll-mt-20 .flex .items-center .gap-2}

If you\'re looking for examples on how to use the Docker GitHub Actions, refer to the following sections:

-   [Add image annotations with GitHub Actions](/build/ci/github-actions/annotations/)

-   [Add SBOM and provenance attestations with GitHub Actions](/build/ci/github-actions/attestations/)

-   [Validating build configuration with GitHub Actions](/build/ci/github-actions/checks/)

-   [Using secrets with GitHub Actions](/build/ci/github-actions/secrets/)

-   [GitHub Actions build summary](/build/ci/github-actions/build-summary/)

-   [Configuring your GitHub Actions builder](/build/ci/github-actions/configure-builder/)

-   [Cache management with GitHub Actions](/build/ci/github-actions/cache/)

-   [Copy image between registries with GitHub Actions](/build/ci/github-actions/copy-image-registries/)

-   [Export to Docker with GitHub Actions](/build/ci/github-actions/export-docker/)

-   [Docker GitHub Builder](/build/ci/github-actions/github-builder/)

-   [Local registry with GitHub Actions](/build/ci/github-actions/local-registry/)

-   [Multi-platform image with GitHub Actions](/build/ci/github-actions/multi-platform/)

-   [Named contexts with GitHub Actions](/build/ci/github-actions/named-contexts/)

-   [Push to multiple registries with GitHub Actions](/build/ci/github-actions/push-multi-registries/)

-   [Reproducible builds with GitHub Actions](/build/ci/github-actions/reproducible-builds/)

-   [Share built image between jobs with GitHub Actions](/build/ci/github-actions/share-image-jobs/)

-   [Manage tags and labels with GitHub Actions](/build/ci/github-actions/manage-tags-labels/)

-   [Test before push with GitHub Actions](/build/ci/github-actions/test-before-push/)

-   [Update Docker Hub description with GitHub Actions](/build/ci/github-actions/update-dockerhub-desc/)
