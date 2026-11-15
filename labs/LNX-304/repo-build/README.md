# Lab: build an RPM repository and a flat Debian repository

`setup` builds two noarch RPMs (`site-a` 1.0 and `site-b` 1.0) and two `.deb` files of the same names into `incoming/`. Turn them into repositories, then add a newer `site-a` and update the RPM repository.

## Starting state

`incoming/` holds `site-a-1.0-1.noarch.rpm`, `site-b-1.0-1.noarch.rpm`, `site-a_1.0_all.deb`, `site-b_1.0_all.deb`, and `site-a-1.1-1.noarch.rpm` (the update, to be added later).

## Your task

1. RPM: copy the two 1.0 RPMs into `repo/rpm/`, run `createrepo_c repo/rpm`, then copy `site-a-1.1-1.noarch.rpm` in and run `createrepo_c --update repo/rpm`.
2. Debian: copy the two `.deb` files into `repo/deb/`, create `Packages` and `Packages.gz` with `apt-ftparchive packages .` (run from `repo/deb`), and a `Release` file with `apt-ftparchive release .`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-304/repo-build/setup
# ...build the repositories...
LAB_DIR=$PWD /path/to/repo/labs/LNX-304/repo-build/check
```

## Notes

- Needs `rpm`, `createrepo-c` (`createrepo_c`), `apt-utils` and `dpkg-dev`. No root needed.
- Sign `repodata/repomd.xml` and `Release` as in the signing lab if you want a full exercise.
- Reading material: [the lesson](lesson:LNX-304-T04). Afterwards, try [the quiz](quiz:LNX-304-T04).
