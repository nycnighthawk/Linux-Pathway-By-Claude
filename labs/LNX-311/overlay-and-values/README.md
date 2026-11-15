# Lab: a production overlay and a safe values file

`base/` holds a small application; `chart/values.yaml` holds a chart's defaults. Both are in your working directory (`$LAB_DIR`).

## Starting state

`setup` writes `base/` (a Deployment `web` and a Service), `chart/values.yaml` and an empty `overlays/prod/`.

## Your task

1. `overlays/prod/kustomization.yaml`: refers to `../../base`, sets `namespace: shop`, changes image `web` to tag `1.4.2` through `images`, sets `replicas` for `web` to 3, adds a `configMapGenerator` named `web-config` with the literal `LOG_LEVEL=warn`, and a `patches` entry targeting Deployment `web` that sets the memory limit to `512Mi`.
2. `values-prod.yaml`: an override file for the chart that sets `replicaCount: 3`, `image.tag: 1.4.2` and `ingress.host: shop.example.com`. Every key in the file must already exist in `chart/values.yaml` (the check rejects unknown keys, like a schema would).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-311/overlay-and-values/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-311/overlay-and-values/check
```

Needs Python 3 with PyYAML. Reading: [the lesson](lesson:LNX-311-T08); then [the quiz](quiz:LNX-311-T08).
