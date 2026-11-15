# Lab: fix a Compose file and a BuildKit Dockerfile

A small web service with a PostgreSQL database ships with a Compose file and a Dockerfile that break several rules from the lesson. Correct both. The grader parses the YAML and reads the Dockerfile; no engine is needed.

## Starting state

`setup` writes `compose.yaml` and `Dockerfile`. `$LAB_DIR` is your working directory.

## Your task

`compose.yaml`:
- `web` publishes only on loopback (`127.0.0.1:8000:8000`), has `read_only: true`, drops all capabilities (`cap_drop: [ALL]`) and restarts `unless-stopped`.
- `web` waits for `db` with `depends_on` and `condition: service_healthy`.
- `db` uses a pinned image (a version tag, not `latest`), has a `healthcheck` with a `test`, and receives its password only through a Compose secret: define a top-level secret `db_password` from a file, mount it into `db`, set `POSTGRES_PASSWORD_FILE`, and remove every literal password from `environment`.

`Dockerfile`:
- Begin with `# syntax=docker/dockerfile:1`.
- Copy `requirements.txt`, install dependencies, then copy the source (cache order).
- Install with a cache mount (`RUN --mount=type=cache,...`) and take the private index token from a secret mount (`--mount=type=secret,id=pip_token`); remove the `ARG` and `ENV` that carry the token.
- Run as a numeric non-root user and use the exec form for `ENTRYPOINT` or `CMD`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-310/compose-buildkit/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-310/compose-buildkit/check
```

## Notes

- Needs `python3-yaml`. Reading: [the lesson](lesson:LNX-310-T04). Afterwards try [the quiz](quiz:LNX-310-T04).
- Real run: `docker compose config` prints the resolved model; `docker buildx build --secret id=pip_token,src=token.txt .` supplies the secret.
