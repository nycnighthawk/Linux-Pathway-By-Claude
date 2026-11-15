# Lab: a Pod with an init container, a native sidecar and an exact request

Write two files in `$LAB_DIR`. The check parses them with PyYAML.

1. `pod.yaml`: a Pod `shop` with, in this order,
   - init container `wait-db` (image `busybox:1.37`, request cpu `50m`),
   - native sidecar `log-agent` (image `fluent/fluent-bit:3.2`, `restartPolicy: Always`, request cpu `100m`, a `startupProbe`, and the volume `logs` mounted read-only at `/logs`),
   - init container `migrate` (image `registry.example/shop:1.0`, request cpu `1000m`),
   - application container `app` (image `registry.example/shop:1.0`, request cpu `500m`, volume `logs` mounted read-write at `/logs`),
   - an `emptyDir` volume named `logs`.
2. `answer.txt`: one line `effective_cpu_m=<number>` with the Pod's effective CPU request in millicores.

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-313/pod-with-sidecar/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-313/pod-with-sidecar/check
```

Needs `python3` and `PyYAML`. Reading: [the lesson](lesson:LNX-313-T01), then [the quiz](quiz:LNX-313-T01).
