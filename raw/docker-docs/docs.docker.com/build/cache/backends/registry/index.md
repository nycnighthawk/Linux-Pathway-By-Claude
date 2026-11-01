---
{"title": "Registry cache", "url": "https://docs.docker.com/build/cache/backends/registry/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Registry cache {#registry-cache pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

The `registry` cache storage can be thought of as an extension to the `inline` cache. Unlike the `inline` cache, the `registry` cache is entirely separate from the image, which allows for more flexible usage - `registry`-backed cache can do everything that the inline cache can do, and more:

-   Allows for separating the cache and resulting image artifacts so that you can distribute your final image without the cache inside.
-   It can efficiently cache multi-stage builds in `max` mode, instead of only the final stage.
-   It works with other exporters for more flexibility, instead of only the `image` exporter.

This cache storage backend works with the default `docker` driver only when the [containerd image store](https://docs.docker.com/desktop/features/containerd/) is enabled. If the containerd image store isn\'t enabled, use a different driver. See [Build drivers](https://docs.docker.com/build/builders/drivers/) for more information.

## [Synopsis](#synopsis) {#synopsis .scroll-mt-20 .flex .items-center .gap-2}

Unlike the simpler `inline` cache, the `registry` cache supports several configuration parameters:

``` {.chroma tabindex="0"}
$ docker buildx build --push -t <registry>/<image> \
  --cache-to type=registry,ref=<registry>/<cache-image>[,parameters...] \
  --cache-from type=registry,ref=<registry>/<cache-image> .
```

The following table describes the available CSV parameters that you can pass to `--cache-to` and `--cache-from`.

  Name                  Option                    Type                      Default   Description
  --------------------- ------------------------- ------------------------- --------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `ref`                 `cache-to`,`cache-from`   String                              Full name of the cache image to import.
  `mode`                `cache-to`                `min`,`max`               `min`     Cache layers to export, see [cache mode](https://docs.docker.com/build/cache/backends/#cache-mode).
  `oci-mediatypes`      `cache-to`                `true`,`false`            `true`    Use OCI media types in exported manifests, see [OCI media types](https://docs.docker.com/build/cache/backends/#oci-media-types).
  `image-manifest`      `cache-to`                `true`,`false`            `true`    When using OCI media types, generate an image manifest instead of an image index for the cache image, see [OCI media types](https://docs.docker.com/build/cache/backends/#oci-media-types).
  `compression`         `cache-to`                `gzip`,`estargz`,`zstd`   `gzip`    Compression type, see [cache compression](https://docs.docker.com/build/cache/backends/#cache-compression).
  `compression-level`   `cache-to`                `0..22`                             Compression level, see [cache compression](https://docs.docker.com/build/cache/backends/#cache-compression).
  `force-compression`   `cache-to`                `true`,`false`            `false`   Forcibly apply compression, see [cache compression](https://docs.docker.com/build/cache/backends/#cache-compression).
  `ignore-error`        `cache-to`                Boolean                   `false`   Ignore errors caused by failed cache exports.

You can choose any valid value for `ref`, as long as it\'s not the same as the target location that you push your image to. You might choose different tags (e.g. `foo/bar:latest` and `foo/bar:build-cache`), separate image names (e.g. `foo/bar` and `foo/bar-cache`), or even different repositories (e.g. `docker.io/foo/bar` and `ghcr.io/foo/bar`). It\'s up to you to decide the strategy that you want to use for separating your image from your cache images.

If the `--cache-from` target doesn\'t exist, then the cache import step will fail, but the build continues.

## [Further reading](#further-reading) {#further-reading .scroll-mt-20 .flex .items-center .gap-2}

For an introduction to caching see [Docker build cache](https://docs.docker.com/build/cache/).

For more information on the `registry` cache backend, see the [BuildKit README](https://github.com/moby/buildkit#registry-push-image-and-cache-separately).
