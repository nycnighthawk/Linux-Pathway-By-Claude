---
{"title": "Local and tar exporters", "url": "https://docs.docker.com/build/exporters/local-tar/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Local and tar exporters {#local-and-tar-exporters pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

The `local` and `tar` exporters output the root filesystem of the build result into a local directory. They\'re useful for producing artifacts that aren\'t container images.

-   `local` exports files and directories.
-   `tar` exports the same, but bundles the export into a tarball.

## [Synopsis](#synopsis) {#synopsis .scroll-mt-20 .flex .items-center .gap-2}

Build a container image using the `local` exporter:

``` {.chroma tabindex="0"}
$ docker buildx build --output type=local[,parameters] .
$ docker buildx build --output type=tar[,parameters] .
```

The following table describes the available parameters:

  Parameter          Type      Default   Description
  ------------------ --------- --------- -----------------------------------------------------------------------------------
  `dest`             String              Path to copy files to
  `platform-split`   Boolean   `true`    `local` exporter only. Split multi-platform outputs into platform subdirectories.

## [Multi-platform builds with local exporter](#multi-platform-builds-with-local-exporter) {#multi-platform-builds-with-local-exporter .scroll-mt-20 .flex .items-center .gap-2}

The `platform-split` parameter controls how multi-platform build outputs are organized.

Consider this Dockerfile that creates platform-specific files:

``` {.chroma tabindex="0"}
FROM busybox AS build
ARG TARGETOS
ARG TARGETARCH
RUN mkdir /out && echo foo > /out/hello-$TARGETOS-$TARGETARCH

FROM scratch
COPY --from=build /out /
```

### [Split by platform (default)](#split-by-platform-default) {#split-by-platform-default .scroll-mt-20 .flex .items-center .gap-2}

By default, the local exporter creates a separate subdirectory for each platform:

``` {.chroma tabindex="0"}
$ docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --output type=local,dest=./output \
  .
```

This produces the following directory structure:

``` {.chroma tabindex="0"}
output/
├── linux_amd64/
│   └── hello-linux-amd64
└── linux_arm64/
    └── hello-linux-arm64
```

### [Merge all platforms](#merge-all-platforms) {#merge-all-platforms .scroll-mt-20 .flex .items-center .gap-2}

To merge files from all platforms into the same directory, set `platform-split=false`:

``` {.chroma tabindex="0"}
$ docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --output type=local,dest=./output,platform-split=false \
  .
```

This produces a flat directory structure:

``` {.chroma tabindex="0"}
output/
├── hello-linux-amd64
└── hello-linux-arm64
```

Files from all platforms merge into a single directory. If multiple platforms produce files with identical names, the export fails with an error.

### [Single-platform builds](#single-platform-builds) {#single-platform-builds .scroll-mt-20 .flex .items-center .gap-2}

Single-platform builds export directly to the destination directory without creating a platform subdirectory:

``` {.chroma tabindex="0"}
$ docker buildx build \
  --platform linux/amd64 \
  --output type=local,dest=./output \
  .
```

This produces:

``` {.chroma tabindex="0"}
output/
└── hello-linux-amd64
```

To include the platform subdirectory even for single-platform builds, explicitly set `platform-split=true`:

``` {.chroma tabindex="0"}
$ docker buildx build \
  --platform linux/amd64 \
  --output type=local,dest=./output,platform-split=true \
  .
```

This produces:

``` {.chroma tabindex="0"}
output/
└── linux_amd64/
    └── hello-linux-amd64
```

## [Further reading](#further-reading) {#further-reading .scroll-mt-20 .flex .items-center .gap-2}

For more information on the `local` or `tar` exporters, see the [BuildKit README](https://github.com/moby/buildkit/blob/master/README.md#local-directory).
