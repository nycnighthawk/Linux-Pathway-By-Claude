# Lab: a CRD with a structural schema

Write `widget-crd.yaml` in your working directory (`$LAB_DIR`) so that valid Widgets are accepted and invalid ones rejected.

## Starting state

`setup` writes `good-widget.yaml`, `bad-widget-size.yaml`, `bad-widget-mode.yaml` and an empty `widget-crd.yaml`.

## Your task

Define the CRD `widgets.example.com` (group `example.com`, kind `Widget`, plural `widgets`, namespaced) with one served and stored version `v1` that:

1. has a structural schema with `spec.size` (integer, 1 to 10, required) and `spec.mode` (string, enum `fast`, `safe`, default `safe`);
2. enables the `status` subresource;
3. defines an `additionalPrinterColumns` entry named `Size` from `.spec.size`;
4. has `status.conditions` as an array of objects in the schema.

The check validates each sample against your schema: the good one passes, the two bad ones fail.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-311/crd-schema/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-311/crd-schema/check
```

Needs Python 3 with PyYAML and jsonschema. Reading: [the lesson](lesson:LNX-311-T09); then [the quiz](quiz:LNX-311-T09).
