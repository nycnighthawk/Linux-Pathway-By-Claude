# Lab: package a script as a Debian package

`setup` creates a small source tree, `hello-site-1.0/`, with a script, a configuration file and a licence. Add the `debian/` directory and build an unsigned binary package without root.

## Starting state

`setup` writes `hello-site-1.0/` (upstream files only, no `debian/`) into `$LAB_DIR`.

## Your task

1. Create `hello-site-1.0/debian/` with `control` (source `hello-site`, `Build-Depends: debhelper-compat (= 13)`, binary package `hello-site`, `Architecture: all`, a description), `changelog` (version `1.0-1`), `copyright`, `rules` (executable, `dh $@`), `source/format` (`3.0 (native)` is fine for the lab) and an `install` file that puts `hello-site` in `usr/bin` and `hello-site.conf` in `etc`.
2. Build: `cd hello-site-1.0 && dpkg-buildpackage -us -uc -b`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-304/deb-package/setup
# ...write debian/, build...
LAB_DIR=$PWD /path/to/repo/labs/LNX-304/deb-package/check
```

## Notes

- Needs `dpkg-dev`, `debhelper`, `fakeroot` (and `lintian` for extra checks). No root needed.
- `dpkg-deb -I`, `dpkg-deb -c` and `dpkg-deb -e` show what you built. For the clean-room version, run the `.dsc` through `sbuild`.
- Reading material: [the lesson](lesson:LNX-304-T02). Afterwards, try [the quiz](quiz:LNX-304-T02).
