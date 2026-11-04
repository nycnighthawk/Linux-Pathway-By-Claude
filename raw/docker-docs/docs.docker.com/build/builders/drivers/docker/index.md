---
{"title": "Docker driver", "url": "https://docs.docker.com/build/builders/drivers/docker/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Docker driver {#docker-driver pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

The Buildx Docker driver is the default driver. It uses the BuildKit server components built directly into the Docker Engine. The Docker driver requires no configuration.

Unlike the other drivers, builders using the Docker driver can\'t be manually created. They\'re only created automatically from the Docker context.

Images built with the Docker driver are automatically loaded to the local image store.

## [Synopsis](#synopsis) {#synopsis .scroll-mt-20 .flex .items-center .gap-2}

``` {.chroma tabindex="0"}
# The Docker driver is used by buildx by default
docker buildx build .
```

It\'s not possible to configure which BuildKit version to use, or to pass any additional BuildKit parameters to a builder using the Docker driver. The BuildKit version and parameters are preset by the Docker Engine internally.

If you need additional configuration and flexibility, consider using the [Docker container driver](https://docs.docker.com/build/builders/drivers/docker-container/).

## [Further reading](#further-reading) {#further-reading .scroll-mt-20 .flex .items-center .gap-2}

For more information on the Docker driver, see the [buildx reference](/reference/cli/docker/buildx/create/#driver).
