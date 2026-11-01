---
{"title": "Cloud driver", "url": "https://docs.docker.com/build/builders/drivers/cloud/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Cloud driver {#cloud-driver pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

The Buildx cloud driver connects to managed BuildKit instances in Docker Build Cloud. Docker provisions and maintains the builder infrastructure, shared build cache, and native `linux/amd64` and `linux/arm64` nodes.

The cloud driver requires Buildx version 0.37.0 or later and access to Docker Build Cloud.

## [Synopsis](#synopsis) {#synopsis .scroll-mt-20 .flex .items-center .gap-2}

Before connecting Buildx, create a cloud builder on the [Docker Build Cloud Dashboard](https://app.docker.com/build/). Then sign in and connect to the builder:

``` {.chroma tabindex="0"}
$ docker login
$ docker buildx create --driver cloud ORG/BUILDER_NAME
```

The command adds the cloud builder to your local Buildx configuration. It does not create a builder in Docker Build Cloud.

For service prerequisites and authentication, see [Docker Build Cloud setup](https://docs.docker.com/build-cloud/setup/). For build examples, see [Building with Docker Build Cloud](https://docs.docker.com/build-cloud/usage/).
