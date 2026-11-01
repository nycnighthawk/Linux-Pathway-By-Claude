---
{"title": "Local cache", "url": "https://docs.docker.com/build/cache/backends/local/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Local cache {#local-cache pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

The `local` cache store is a simple cache option that stores your cache as files in a directory on your filesystem, using an [OCI image layout](https://github.com/opencontainers/image-spec/blob/main/image-layout.md) for the underlying directory structure. Local cache is a good choice if you\'re just testing, or if you want the flexibility to self-manage a shared storage solution.

This cache storage backend works with the default `docker` driver only when the [containerd image store](https://docs.docker.com/desktop/features/containerd/) is enabled. If the containerd image store isn\'t enabled, use a different driver. See [Build drivers](https://docs.docker.com/build/builders/drivers/) for more information.

## [Synopsis](#synopsis) {#synopsis .scroll-mt-20 .flex .items-center .gap-2}

``` {.chroma tabindex="0"}
$ docker buildx build --push -t <registry>/<image> \
  --cache-to type=local,dest=path/to/local/dir[,parameters...] \
  --cache-from type=local,src=path/to/local/dir .
```

The following table describes the available CSV parameters that you can pass to `--cache-to` and `--cache-from`.

  Name                  Option                    Type                      Default    Description
  --------------------- ------------------------- ------------------------- ---------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `src`                 `cache-from`              String                               Path of the local directory where cache gets imported from.
  `digest`              `cache-from`              String                               Digest of manifest to import, see [cache versioning](#cache-versioning).
  `tag`                 `cache-to`,`cache-from`   String                    `latest`   Tag of the cache manifest, see [cache versioning](#cache-versioning).
  `dest`                `cache-to`                String                               Path of the local directory where cache gets exported to.
  `mode`                `cache-to`                `min`,`max`               `min`      Cache layers to export, see [cache mode](https://docs.docker.com/build/cache/backends/#cache-mode).
  `oci-mediatypes`      `cache-to`                `true`,`false`            `true`     Use OCI media types in exported manifests, see [OCI media types](https://docs.docker.com/build/cache/backends/#oci-media-types).
  `image-manifest`      `cache-to`                `true`,`false`            `true`     When using OCI media types, generate an image manifest instead of an image index for the cache image, see [OCI media types](https://docs.docker.com/build/cache/backends/#oci-media-types).
  `compression`         `cache-to`                `gzip`,`estargz`,`zstd`   `gzip`     Compression type, see [cache compression](https://docs.docker.com/build/cache/backends/#cache-compression).
  `compression-level`   `cache-to`                `0..22`                              Compression level, see [cache compression](https://docs.docker.com/build/cache/backends/#cache-compression).
  `force-compression`   `cache-to`                `true`,`false`            `false`    Forcibly apply compression, see [cache compression](https://docs.docker.com/build/cache/backends/#cache-compression).
  `ignore-error`        `cache-to`                Boolean                   `false`    Ignore errors caused by failed cache exports.
  `reset`               `cache-to`                `true`,`false`            `false`    Delete blobs that no tag references, see [cache versioning](#cache-versioning).

If the `src` cache doesn\'t exist, then the cache import step will fail, but the build continues.

## [Cache versioning](#cache-versioning) {#cache-versioning .scroll-mt-20 .flex .items-center .gap-2}

A local cache directory uses an OCI image layout. Its `index.json` file associates tags with cache manifests, while the `blobs` directory stores the manifest and cache data.

By default, BuildKit exports and imports the cache tagged `latest`. Use different tags to keep multiple caches in the same directory:

``` {.chroma tabindex="0"}
$ docker buildx build --cache-to type=local,dest=path/to/local/dir,tag=v1 .
$ docker buildx build --cache-to type=local,dest=path/to/local/dir,tag=v2 .
```

Exporting another cache with the same tag updates that tag to reference the new manifest. Manifests referenced by other tags remain unchanged.

Import a cache by specifying its tag:

``` {.chroma tabindex="0"}
$ docker buildx build --cache-from type=local,src=path/to/local/dir,tag=v1 .
```

A digest identifies an exact cache manifest. BuildKit reports the digest of each exported manifest in the build output. Use `digest` instead of `tag` when you need a specific manifest:

``` {.chroma tabindex="0"}
$ docker buildx build \
  --cache-from type=local,src=path/to/local/dir,digest=sha256:DIGEST .
```

If you specify both `digest` and `tag`, BuildKit uses `digest`.

By default, updating a tag doesn\'t delete the blobs used by its previous manifest. The previous manifest remains available by digest, so the local cache directory grows over time.

Buildx version 0.35.0 and later supports `reset=true` on export, which deletes blobs that no tag references:

``` {.chroma tabindex="0"}
$ docker buildx build --cache-to type=local,dest=path/to/local/dir,reset=true .
```

Blobs that other tags reference are kept. Manifests that no tag references are deleted, so you can no longer import them by digest.

## [Further reading](#further-reading) {#further-reading .scroll-mt-20 .flex .items-center .gap-2}

For an introduction to caching see [Docker build cache](https://docs.docker.com/build/cache/).

For more information on the `local` cache backend, see the [BuildKit README](https://github.com/moby/buildkit#local-directory-1).
