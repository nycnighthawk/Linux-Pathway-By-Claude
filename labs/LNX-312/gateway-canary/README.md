# Lab: a Gateway and a canary HTTPRoute

Write two manifests. The check parses them with PyYAML; no cluster is needed.

## Files (created by `setup` in `$LAB_DIR`)

1. `gateway.yaml`: a `Gateway` named `edge` in namespace `infra`, class `lab`, with one listener `https`
   (port 443, protocol `HTTPS`, hostname `*.example.test`, TLS mode `Terminate` with certificate reference `edge-cert`)
   whose `allowedRoutes.namespaces.from` is `Selector` matching the label `edge-access: "true"`.
2. `route.yaml`: an `HTTPRoute` named `shop` in namespace `shop`, parent `edge` in `infra`, hostname `shop.example.test`,
   a path prefix `/` rule sending 90 percent of traffic to Service `shop-v1` port 80 and 10 percent to `shop-v2` port 80,
   plus a header rule: requests with header `x-canary: always` go only to `shop-v2`.

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-312/gateway-canary/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-312/gateway-canary/check
```

Needs `python3` and `PyYAML`. API group and version: `gateway.networking.k8s.io/v1`.
Reading: [the lesson](lesson:LNX-312-T06), then [the quiz](quiz:LNX-312-T06).
