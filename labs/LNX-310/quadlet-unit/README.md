# Lab: a hardened Quadlet container, volume and pod

Quadlet turns small `.container`, `.volume` and `.pod` files into systemd services. You will fix a careless container definition and add a volume and a two-container pod. The grader parses the files and checks the hardening choices from the lesson; if a Podman installation is present it also runs the Quadlet generator in dry-run mode and reports its output as a note.

## Starting state

`setup` creates `quadlet/web.container` (with several mistakes) and `quadlet/api.container` (not yet in a pod). `$LAB_DIR` is your working directory.

## Your task

1. `quadlet/web.container`: pin the image (a version tag or digest, not `latest`); publish only on loopback (`127.0.0.1:...`); mount the named volume `site.volume` at `/usr/share/nginx/html` with the read-only option and an SELinux relabel option; set `ReadOnly=true`, `NoNewPrivileges=true`, `DropCapability=ALL`, a `HealthCmd`, and `Notify=healthy`; in `[Service]` restart on failure or always; in `[Unit]` order after and want `network-online.target`; in `[Install]` start with `WantedBy=default.target`.
2. Create `quadlet/site.volume` with a `[Volume]` section.
3. Create `quadlet/app.pod` with `PodName=app` and a loopback `PublishPort`.
4. `quadlet/api.container`: join the pod with `Pod=app.pod`, keep a pinned image, and remove its own `PublishPort` (the pod owns the port).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-310/quadlet-unit/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-310/quadlet-unit/check
```

## Notes

- Real run (rootless): copy the files to `~/.config/containers/systemd/`, then `systemctl --user daemon-reload` and `systemctl --user start web.service`; debug with `/usr/lib/systemd/system-generators/podman-system-generator --user --dryrun`.
- Reading: [the lesson](lesson:LNX-310-T03). Afterwards try [the quiz](quiz:LNX-310-T03).
