# Lab: a mirror configuration and a faithful copy plan

You will write the client configuration that sends Docker Hub pulls through an internal mirror, write the Skopeo command that copies a multi-architecture image without losing platforms or the digest, and read a recorded image index. The grader parses the TOML and the script; no registry is needed.

## Starting state

`setup` writes `index.json` (the output of `skopeo inspect --raw` for a multi-architecture image), `registries.conf` (nearly empty), `copy.sh` (a stub) and `answers.txt`.

## Your task

1. `registries.conf` (TOML, v2 format): `unqualified-search-registries` with only `registry.example.com`; `short-name-mode = "enforcing"`; a `[[registry]]` for `prefix = "docker.io"` with `location = "docker.io"` and a `[[registry.mirror]]` whose location is `mirror.internal:5000/dockerhub` and `pull-from-mirror = "digest-only"`; and a `[[registry]]` with `location = "registry.badvendor.example"` and `blocked = true`. Do not set `insecure = true` for the mirror.
2. `copy.sh`: one `skopeo copy` that copies `docker://docker.io/library/alpine:3.21` to `docker://mirror.internal:5000/base/alpine:3.21`, keeping every platform (`--all`) and the manifest digest (`--preserve-digests`), with TLS verification left on.
3. `answers.txt`: `platform_count` (platforms in `index.json`), `arm64_digest` (the manifest digest for `linux/arm64`) and `copy_needs_all` (`yes` or `no`: would a plain `skopeo copy` on an amd64 host keep the arm64 manifest?).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-310/registries-mirror/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-310/registries-mirror/check
```

## Notes

- Needs Python 3.11 or later for `tomllib`. Reading: [the lesson](lesson:LNX-310-T06). Afterwards try [the quiz](quiz:LNX-310-T06).
- Real run: `podman pull --log-level=debug docker.io/library/alpine` shows which host answered.
