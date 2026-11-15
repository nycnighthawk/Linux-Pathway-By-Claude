# Lab: package one tool as a .deb and as an OCI image

You will package a tiny script twice. First as a Debian package built straight from a staged tree, then as an OCI image
layout assembled by hand, so that the digests, sizes and `diff_ids` that registries and runtimes rely on are no longer a
mystery. No container runtime is needed.

## Starting state

`setup` writes `stage/` (the install tree: `usr/bin/hello`, a README under `usr/share/doc/hello`), `rootfs/app/hello` (the
image filesystem) and a blank `answers.txt`.

## Your task

1. Add `stage/DEBIAN/control` with `Package: hello`, `Version: 1.0`, `Architecture: all`, a `Maintainer`, `Depends: coreutils`
   and a `Description`. Build with `dpkg-deb --root-owner-group --build stage pkg/hello_1.0_all.deb`, inspect with
   `dpkg-deb -I` and `dpkg-deb -c`, then remove `stage/DEBIAN` again.
2. Build the OCI layout in `oci/`:
   - make a layer tar of `rootfs/` with `tar --owner=0 --group=0 --numeric-owner` and compute `sha256sum` of the uncompressed tar
     (that is the `diff_id`); optionally gzip it and take a second digest and the size of the compressed file;
   - store each blob as `oci/blobs/sha256/<hex digest>`: the layer, a config JSON (architecture, os `linux`,
     `config.Entrypoint` `["/app/hello"]`, `rootfs` with the `diff_ids`) and a manifest JSON pointing at config and layer
     with digests and sizes;
   - write `oci/oci-layout` (`{"imageLayoutVersion":"1.0.0"}`) and `oci/index.json` listing the manifest.
3. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-220/packaging-deb-oci/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-220/packaging-deb-oci/check
```

## Notes

- The lab needs `dpkg`, `tar`, `gzip`, `coreutils` and `python3`. If you have `skopeo`, `skopeo inspect oci:oci` can read
  the result.
- Reading material: [the lesson](lesson:LNX-220-T10). Afterwards, try [the quiz](quiz:LNX-220-T10).
