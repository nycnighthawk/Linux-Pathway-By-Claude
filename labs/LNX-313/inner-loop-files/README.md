# Lab: the three files of a fast inner loop

Create these files in `$LAB_DIR` for a Python service `api` (port 8080, source in `./src`, dependencies in `requirements.txt`).

1. `skaffold.yaml` (`apiVersion: skaffold/v4beta11`, `kind: Config`): one artifact `registry.example/api` with `context: .` and a Docker build using `Dockerfile`,
   a `sync.manual` rule copying `src/**/*.py` into `/app/src`, manifests from the Kustomize path `k8s/overlays/dev`, a `kubectl` deployer, and a `portForward`
   of `service` `api` port `8080` to local port `8080`.
2. `Tiltfile`: `docker_build('registry.example/api', '.', live_update=[...])` where the live update has `sync('./src', '/app/src')` and
   `run('pip install -r requirements.txt', trigger=['./requirements.txt'])`; `k8s_yaml(kustomize('k8s/overlays/dev'))`; `k8s_resource('api', port_forwards=8080)`;
   and `local_resource('unit-tests', 'pytest -q', deps=['./src'])`.
3. `.devcontainer/devcontainer.json`: image `mcr.microsoft.com/devcontainers/python:3.12`, features `ghcr.io/devcontainers/features/docker-outside-of-docker:1`
   and `ghcr.io/devcontainers/features/kubectl-helm-minikube:1`, `forwardPorts: [8080]`, `postCreateCommand: "pip install -r requirements.txt"`,
   the VS Code extension `ms-python.python`, and `remoteUser: vscode`.

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-313/inner-loop-files/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-313/inner-loop-files/check
```

Needs `python3` and `PyYAML`. Reading: [the lesson](lesson:LNX-313-T10), then [the quiz](quiz:LNX-313-T10).
