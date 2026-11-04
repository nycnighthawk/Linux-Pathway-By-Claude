---
{"title": "Docker build cache", "url": "https://docs.docker.com/build/cache", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Docker build cache {#docker-build-cache pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

When you build the same Docker image multiple times, knowing how to optimize the build cache is a great tool for making sure the builds run fast.

## [How the build cache works](#how-the-build-cache-works) {#how-the-build-cache-works .scroll-mt-20 .flex .items-center .gap-2}

Understanding Docker\'s build cache helps you write better Dockerfiles that result in faster builds.

The following example shows a small Dockerfile for a program written in C.

``` {.chroma tabindex="0"}
# syntax=docker/dockerfile:1
FROM ubuntu:latest

RUN apt-get update && apt-get install -y build-essentials
COPY main.c Makefile /src/
WORKDIR /src/
RUN make build
```

Each instruction in this Dockerfile translates to a layer in your final image. You can think of image layers as a stack, with each layer adding more content on top of the layers that came before it:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgYXJpYS1oaWRkZW49InRydWUiIGRhdGEtc2xvdD0iaWNvbiI+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNNS40NyA1LjQ3YS43NS43NS4wIDAxMS4wNi4wTDEyIDEwLjk0bDUuNDctNS40N2EuNzUuNzUuMCAxMTEuMDYgMS4wNkwxMy4wNiAxMmw1LjQ3IDUuNDdhLjc1Ljc1LjAgMTEtMS4wNiAxLjA2TDEyIDEzLjA2bC01LjQ3IDUuNDdhLjc1Ljc1LjAgMDEtMS4wNi0xLjA2TDEwLjk0IDEyIDUuNDcgNi41M2EuNzUuNzUuMCAwMTAtMS4wNnoiIGNsaXAtcnVsZT0iZXZlbm9kZCI+PC9wYXRoPjwvc3ZnPg==)

![Image layer diagram](https://docs.docker.com/build/images/cache-stack.png)

Whenever a layer changes, that layer will need to be re-built. For example, suppose you make a change to your program in the `main.c` file. After this change, the `COPY` command will have to run again in order for those changes to appear in the image. In other words, Docker will invalidate the cache for this layer.

If a layer changes, all other layers that come after it are also affected. When the layer with the `COPY` command gets invalidated, all layers that follow will need to run again, too:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgYXJpYS1oaWRkZW49InRydWUiIGRhdGEtc2xvdD0iaWNvbiI+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNNS40NyA1LjQ3YS43NS43NS4wIDAxMS4wNi4wTDEyIDEwLjk0bDUuNDctNS40N2EuNzUuNzUuMCAxMTEuMDYgMS4wNkwxMy4wNiAxMmw1LjQ3IDUuNDdhLjc1Ljc1LjAgMTEtMS4wNiAxLjA2TDEyIDEzLjA2bC01LjQ3IDUuNDdhLjc1Ljc1LjAgMDEtMS4wNi0xLjA2TDEwLjk0IDEyIDUuNDcgNi41M2EuNzUuNzUuMCAwMTAtMS4wNnoiIGNsaXAtcnVsZT0iZXZlbm9kZCI+PC9wYXRoPjwvc3ZnPg==)

![Image layer diagram, showing cache invalidation](https://docs.docker.com/build/images/cache-stack-invalidated.png)

And that\'s the Docker build cache in a nutshell. Once a layer changes, then all downstream layers need to be rebuilt as well. Even if they wouldn\'t build anything differently, they still need to re-run.

## [Other resources](#other-resources) {#other-resources .scroll-mt-20 .flex .items-center .gap-2}

For more information on using cache to do efficient builds, see:

-   [Cache invalidation](https://docs.docker.com/build/cache/invalidation/)
-   [Optimize build cache](https://docs.docker.com/build-cloud/optimization/)
-   [Garbage collection](https://docs.docker.com/build/cache/garbage-collection/)
-   [Cache storage backends](https://docs.docker.com/build/cache/backends/)
