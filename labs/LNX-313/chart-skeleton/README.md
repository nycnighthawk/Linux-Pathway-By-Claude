# Lab: a chart that lints, validates and upgrades safely

In `$LAB_DIR/web/` write a small chart. The check validates it without Helm installed (YAML, JSON Schema and template pattern checks).

1. `Chart.yaml`: `apiVersion: v2`, `name: web`, `type: application`, `version: 0.1.0`, `appVersion: "1.4.2"`.
2. `values.yaml`: `replicaCount: 2`, `image.repository: registry.example/web`, `image.tag: ""` (empty means use the app version),
   `image.pullPolicy: IfNotPresent`, `autoscaling.enabled: false`, `resources` with requests and limits for memory only
   (`requests.cpu` `100m`, `requests.memory` `128Mi`, `limits.memory` `128Mi`), `podSecurityContext.runAsNonRoot: true`.
3. `values.schema.json`: draft-07 schema that requires `image` and `replicaCount`, makes `replicaCount` an integer of at least 1,
   makes `image.repository` a non-empty string, and sets `additionalProperties` false on `image`.
4. `templates/deployment.yaml`: must contain `include "web.fullname" .`, omit `replicas` when autoscaling is enabled
   (`if not .Values.autoscaling.enabled`), render resources with `toYaml .Values.resources | nindent`, use `required` for `image.repository`,
   and build the image from `.Values.image.tag | default .Chart.AppVersion`.
5. `templates/_helpers.tpl`: defines `web.fullname` and `web.selectorLabels`.

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-313/chart-skeleton/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-313/chart-skeleton/check
```

Needs `python3` with `PyYAML` and `jsonschema`. Reading: [the lesson](lesson:LNX-313-T06), then [the quiz](quiz:LNX-313-T06).
