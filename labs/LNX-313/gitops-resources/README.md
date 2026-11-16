# Lab: connect a repository to a cluster, two ways

Write two files in `$LAB_DIR`.

1. `argocd.yaml` (multi-document): an `AppProject` `shop` that allows only the repository `https://git.example/shop/config.git` and destination namespace `shop`
   on `https://kubernetes.default.svc`, and an `Application` `shop-api` in namespace `argocd` in project `shop`, source repo `https://git.example/shop/config.git`,
   path `apps/api/overlays/prod`, `targetRevision: main`, destination namespace `shop`, with automated sync (`prune: true`, `selfHeal: true`), sync option `CreateNamespace=true`,
   and `ignoreDifferences` for `/spec/replicas` of `apps/Deployment`.
2. `flux.yaml` (multi-document, `flux-system` namespace): a `GitRepository` `config` (URL as above, branch `main`, interval `1m`) and two `Kustomization`s:
   `infra` (path `./infrastructure`, interval `10m`, prune true, source `config`) and `apps` (path `./apps/prod`, interval `5m`, prune true, `dependsOn: infra`,
   a health check on `Deployment/api` in `shop`, `decryption.provider: sops` with secret `sops-age`).

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-313/gitops-resources/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-313/gitops-resources/check
```

Needs `python3` and `PyYAML`. API versions: `argoproj.io/v1alpha1`, `source.toolkit.fluxcd.io/v1`, `kustomize.toolkit.fluxcd.io/v1` (to verify for your installed versions).
Reading: [the lesson](lesson:LNX-313-T07), then [the quiz](quiz:LNX-313-T07).
