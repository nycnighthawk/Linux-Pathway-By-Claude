# Lab: write a bootc Containerfile

`setup` creates a `Containerfile` skeleton with `?` marks and an empty `site/` directory. Complete the Containerfile and write the kernel-argument drop-in, following the rules of an image-based system. Nothing is built; the check reads your files (and parses the TOML).

## Starting state

`Containerfile` contains `FROM ?`, a placeholder `RUN` and nothing else useful. `site/10-site.toml` does not exist.

## Your task

1. `FROM` a bootc base image (the name must contain `bootc`).
2. Install `chrony` and `tmux` with `dnf -y install` and clean the cache in the same `RUN` (`dnf clean all`).
3. Write `site/10-site.toml` with `kargs = ["audit=1"]` and `COPY` it to `/usr/lib/bootc/kargs.d/10-site.toml`.
4. Enable `chronyd.service` with `systemctl enable`.
5. End with `RUN bootc container lint`.
6. The file must not contain `VOLUME`, `ENTRYPOINT` or `CMD` (an operating system image is not an application container), and must not write a password or token.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-304/bootc-containerfile/setup
# ...edit Containerfile, write site/10-site.toml...
LAB_DIR=$PWD /path/to/repo/labs/LNX-304/bootc-containerfile/check
```

## Notes

- Needs `python3` 3.11 or later for `tomllib`. To try a real build you also need `podman` and a bootc base image.
- Reading material: [the lesson](lesson:LNX-304-T08). Afterwards, try [the quiz](quiz:LNX-304-T08).
