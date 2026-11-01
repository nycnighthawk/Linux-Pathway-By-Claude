---
{"title": "Using Bake with additional contexts", "url": "https://docs.docker.com/build/bake/contexts/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Using Bake with additional contexts {#using-bake-with-additional-contexts pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

In addition to the main `context` key that defines the build context, each target can also define additional named contexts with a map defined with key `contexts`. These values map to the `--build-context` flag in the [build command](/reference/cli/docker/buildx/build/#build-context).

Inside the Dockerfile these contexts can be used with the `FROM` instruction or `--from` flag.

Supported context values are:

-   Local filesystem directories
-   Container images
-   Git URLs
-   HTTP URLs
-   Name of another target in the Bake file

## [Pinning alpine image](#pinning-alpine-image) {#pinning-alpine-image .scroll-mt-20 .flex .items-center .gap-2}

Dockerfile

``` {.chroma tabindex="0"}
# syntax=docker/dockerfile:1
FROM alpine
RUN echo "Hello world"
```

docker-bake.hcl

``` {.chroma tabindex="0"}
target "app" {
  contexts = {
    alpine = "docker-image://alpine:3.13"
  }
}
```

## [Using a secondary source directory](#using-a-secondary-source-directory) {#using-a-secondary-source-directory .scroll-mt-20 .flex .items-center .gap-2}

Dockerfile

``` {.chroma tabindex="0"}
FROM golang
COPY --from=src . .
```

docker-bake.hcl

``` {.chroma tabindex="0"}
# Running `docker buildx bake app` will result in `src` not pointing
# to some previous build stage but to the client filesystem, not part of the context.
target "app" {
  contexts = {
    src = "../path/to/source"
  }
}
```

## [Using a target as a build context](#using-a-target-as-a-build-context) {#using-a-target-as-a-build-context .scroll-mt-20 .flex .items-center .gap-2}

To use a result of one target as a build context of another, specify the target name with `target:` prefix.

baseapp.Dockerfile

``` {.chroma tabindex="0"}
FROM scratch
```

Dockerfile

``` {.chroma tabindex="0"}
# syntax=docker/dockerfile:1
FROM baseapp
RUN echo "Hello world"
```

docker-bake.hcl

``` {.chroma tabindex="0"}
target "base" {
  dockerfile = "baseapp.Dockerfile"
}

target "app" {
  contexts = {
    baseapp = "target:base"
  }
}
```

In most cases you should just use a single multi-stage Dockerfile with multiple targets for similar behavior. This case is only recommended when you have multiple Dockerfiles that can\'t be merged into one.
