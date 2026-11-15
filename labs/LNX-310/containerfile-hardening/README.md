# Lab: rewrite a bloated Containerfile

A Go service is built by a single-stage file that is large, runs as root and leaks a token. Rewrite `Containerfile` (and add an ignore file) so that it follows the lesson. The grader reads the files; it does not run a build, so the checks are the same ones a linter such as Hadolint plus a review would make.

## Starting state

`setup` writes `Containerfile` and no ignore file. `$LAB_DIR` is your working directory.

## Your task

1. Use a multi-stage build: at least two `FROM` lines, a named build stage, and `COPY --from=<stage>` into the final stage.
2. Pin bases: no `latest`; every `FROM` uses a version tag or a digest.
3. The final stage installs no compilers or package managers' build tools (no `build-essential`, `gcc`, `apt-get` or `pip`).
4. In any stage that uses `apt-get`, combine `update` and `install` in one `RUN`, use `--no-install-recommends` and remove `/var/lib/apt/lists`.
5. The final stage sets a numeric non-root `USER` (not 0 and not `root`) and an exec-form `ENTRYPOINT`.
6. Remove the secret-bearing `ENV`/`ARG` lines, the `ADD` of a URL and any `curl ... | sh`.
7. Add the label `org.opencontainers.image.source`.
8. Create `.containerignore` (or `.dockerignore`) that excludes `.git` and `.env`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-310/containerfile-hardening/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-310/containerfile-hardening/check
```

## Notes

- Reading: [the lesson](lesson:LNX-310-T05). Afterwards try [the quiz](quiz:LNX-310-T05).
- Real run: `podman build -t app:1 .`, then `podman run --rm --read-only --cap-drop ALL --user 10001 app:1`.
