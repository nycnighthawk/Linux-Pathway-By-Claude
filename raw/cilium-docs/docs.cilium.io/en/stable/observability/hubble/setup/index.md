---
{"title": "Setting up Hubble Observability", "url": "https://docs.cilium.io/en/stable/observability/hubble/setup/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Setting up Hubble Observability[](#setting-up-hubble-observability "Link to this heading")

Hubble is the observability layer of Cilium and can be used to obtain cluster-wide visibility into the network and security layer of your Kubernetes cluster.

Note

This guide assumes that Cilium has been correctly installed in your Kubernetes cluster. Please see [Cilium Quick Installation](../../../gettingstarted/k8s-install-default/#k8s-quick-install) for more information. If unsure, run `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} and validate that Cilium is up and running.

## Enable Hubble in Cilium[](#enable-hubble-in-cilium "Link to this heading")

Tip

Enabling Hubble requires the TCP port 4244 to be open on all nodes running Cilium. This is required for Relay to operate correctly.

In order to enable Hubble and install Hubble relay, run the command `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`hubble`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`enable`{.docutils .literal .notranslate} as shown below:

``` {#codecell0}
$ cilium hubble enable
🔑 Found existing CA in secret cilium-ca
✨ Patching ConfigMap cilium-config to enable Hubble...
♻️  Restarted Cilium pods
🔑 Generating certificates for Relay...
2021/04/13 17:11:23 [INFO] generate received request
2021/04/13 17:11:23 [INFO] received CSR
2021/04/13 17:11:23 [INFO] generating key: ecdsa-256
2021/04/13 17:11:23 [INFO] encoded CSR
2021/04/13 17:11:23 [INFO] signed certificate with serial number 365589302067830033295858933512588007090526050046
2021/04/13 17:11:24 [INFO] generate received request
2021/04/13 17:11:24 [INFO] received CSR
2021/04/13 17:11:24 [INFO] generating key: ecdsa-256
2021/04/13 17:11:24 [INFO] encoded CSR
2021/04/13 17:11:24 [INFO] signed certificate with serial number 644167683731852948186644541769558498727586273511
✨ Deploying Relay...
```

Copy First Line Copy Commands Copy All

If you installed Cilium via `helm`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`install`{.docutils .literal .notranslate}, Hubble is enabled by default. You may enable Hubble Relay with the following command:

``` {#codecell1 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set hubble.relay.enabled=true
```

Copy First Line Copy All

``` {#codecell2 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set hubble.relay.enabled=true
```

Copy First Line Copy All

Run `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} to validate that Hubble is enabled and running:

``` {#codecell3}
$ cilium status
    /¯¯\
 /¯¯\__/¯¯\    Cilium:             OK
 \__/¯¯\__/    Operator:           OK
 /¯¯\__/¯¯\    Envoy DaemonSet:    OK
 \__/¯¯\__/    Hubble Relay:       OK
    \__/       ClusterMesh:        disabled

DaemonSet             cilium                   Desired: 1, Ready: 1/1, Available: 1/1
DaemonSet             cilium-envoy             Desired: 1, Ready: 1/1, Available: 1/1
Deployment            cilium-operator          Desired: 1, Ready: 1/1, Available: 1/1
Deployment            hubble-relay             Desired: 1, Ready: 1/1, Available: 1/1
Containers:           cilium                   Running: 1
                      cilium-envoy             Running: 1
                      cilium-operator          Running: 1
                      clustermesh-apiserver
                      hubble-relay             Running: 1
Cluster Pods:         8/8 managed by Cilium
Helm chart version:   1.17.0
Image versions        cilium             quay.io/cilium/cilium:latest: 1
                      cilium-envoy       quay.io/cilium/cilium-envoy:v1.32.3-1739240299-e85e926b0fa4cec519cefff54b60bd7942d7871b@sha256:ced8a89d642d10d648471afc2d8737238f1479c368955e6f2553ded58029ac88: 1
                      cilium-operator    quay.io/cilium/operator-generic-ci:latest: 1
                      hubble-relay       quay.io/cilium/hubble-relay-ci:latest: 1
```

Copy First Line Copy Commands Copy All

## Install the Hubble Client[](#install-the-hubble-client "Link to this heading")

In order to access the observability data collected by Hubble, you must first install Hubble CLI.

Select the tab for your platform below and install the latest release of Hubble CLI.

Download the latest hubble release:

``` {#codecell4}
HUBBLE_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/hubble/main/stable.txt)
HUBBLE_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then HUBBLE_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/hubble/releases/download/$HUBBLE_VERSION/hubble-linux-${HUBBLE_ARCH}.tar.gz{,.sha256sum}
sha256sum --check hubble-linux-${HUBBLE_ARCH}.tar.gz.sha256sum
sudo tar xzvfC hubble-linux-${HUBBLE_ARCH}.tar.gz /usr/local/bin
rm hubble-linux-${HUBBLE_ARCH}.tar.gz{,.sha256sum}
```

Copy First Line Copy All

Download the latest hubble release:

``` {#codecell5}
HUBBLE_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/hubble/main/stable.txt)
HUBBLE_ARCH=amd64
if [ "$(uname -m)" = "arm64" ]; then HUBBLE_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/hubble/releases/download/$HUBBLE_VERSION/hubble-darwin-${HUBBLE_ARCH}.tar.gz{,.sha256sum}
shasum -a 256 -c hubble-darwin-${HUBBLE_ARCH}.tar.gz.sha256sum
sudo tar xzvfC hubble-darwin-${HUBBLE_ARCH}.tar.gz /usr/local/bin
rm hubble-darwin-${HUBBLE_ARCH}.tar.gz{,.sha256sum}
```

Copy First Line Copy All

Download the latest hubble release:

``` {#codecell6}
curl -LO "https://raw.githubusercontent.com/cilium/hubble/main/stable.txt"
set /p HUBBLE_VERSION=<stable.txt
curl -L --fail -O "https://github.com/cilium/hubble/releases/download/%HUBBLE_VERSION%/hubble-windows-amd64.tar.gz"
curl -L --fail -O "https://github.com/cilium/hubble/releases/download/%HUBBLE_VERSION%/hubble-windows-amd64.tar.gz.sha256sum"
certutil -hashfile hubble-windows-amd64.tar.gz SHA256
type hubble-windows-amd64.tar.gz.sha256sum
:: verify that the checksum from the two commands above match
tar zxf hubble-windows-amd64.tar.gz
```

Copy First Line Copy All

and move the `hubble.exe`{.docutils .literal .notranslate} CLI to a directory listed in the `%PATH%`{.docutils .literal .notranslate} environment variable after extracting it from the tarball.

## Validate Hubble API Access[](#validate-hubble-api-access "Link to this heading")

Note

The following commands use the `-P`{.docutils .literal .notranslate} (`--port-forward`{.docutils .literal .notranslate}) flag to automatically port-forward the Hubble Relay service from your local machine on port `4245`{.docutils .literal .notranslate}.

You can also omit the flag and create a port-forward manually with the Cilium CLI:

``` {#codecell7}
$ cilium hubble port-forward
ℹ️ Hubble Relay is available at 127.0.0.1:4245
```

Copy First Line Copy Commands Copy All

Or with kubectl:

``` {#codecell8}
$ kubectl -n kube-system port-forward service/hubble-relay 4245:80
Forwarding from 127.0.0.1:4245 -> 4245
Forwarding from [::1]:4245 -> 4245
```

Copy First Line Copy Commands Copy All

For more information on this method, see [Use Port Forwarding to Access Application in a Cluster](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/).

Now you can validate that you can access the Hubble API via the installed CLI:

``` {#codecell9}
$ hubble status -P
Healthcheck (via 127.0.0.1:4245): Ok
Current/Max Flows: 11917/12288 (96.98%)
Flows/s: 11.74
Connected Nodes: 3/3
```

Copy First Line Copy Commands Copy All

You can also query the flow API and look for flows:

``` {#codecell10}
$ hubble observe -P
Feb 12 19:13:58.111: kube-system/hubble-relay-6467f4f4d-xrxfs:47550 (ID:95552) -> 172.18.0.2:4244 (host) to-stack FORWARDED (TCP Flags: ACK, PSH)
...
```

Copy First Line Copy Commands Copy All

Note

If you port forward to a port other than `4245`{.docutils .literal .notranslate} (`--port-forward-port`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`PORT`{.docutils .literal .notranslate} when using automatic port-forwarding), make sure to use the `--server`{.docutils .literal .notranslate} flag or `HUBBLE_SERVER`{.docutils .literal .notranslate} environment variable to set the Hubble server address (default: `localhost:4245`{.docutils .literal .notranslate}).

For more information, check out Hubble CLI's help message by running `hubble`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`help`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} or `hubble`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`help`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`observe`{.docutils .literal .notranslate} as well as `hubble`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`config`{.docutils .literal .notranslate} for configuring Hubble CLI.

Note

If you have [enabled TLS](../configuration/tls/#hubble-enable-tls) then you will need to specify additional flags to [access the Hubble API](../configuration/tls/#hubble-api-tls).

## Troubleshooting Hubble Deployment[](#troubleshooting-hubble-deployment "Link to this heading")

Validate the state of Hubble and/or Hubble Relay by running `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate}:

``` {#codecell11}
$ cilium status
    /¯¯\
 /¯¯\__/¯¯\    Cilium:             OK
 \__/¯¯\__/    Operator:           OK
 /¯¯\__/¯¯\    Envoy DaemonSet:    OK
 \__/¯¯\__/    Hubble Relay:       OK
    \__/       ClusterMesh:        disabled

DaemonSet             cilium                   Desired: 1, Ready: 1/1, Available: 1/1
DaemonSet             cilium-envoy             Desired: 1, Ready: 1/1, Available: 1/1
Deployment            cilium-operator          Desired: 1, Ready: 1/1, Available: 1/1
Deployment            hubble-relay             Desired: 1, Ready: 1/1, Available: 1/1
Containers:           cilium                   Running: 1
                      cilium-envoy             Running: 1
                      cilium-operator          Running: 1
                      clustermesh-apiserver
                      hubble-relay             Running: 1
Cluster Pods:         8/8 managed by Cilium
Helm chart version:   1.17.0
Image versions        cilium             quay.io/cilium/cilium:latest: 1
                      cilium-envoy       quay.io/cilium/cilium-envoy:v1.32.3-1739240299-e85e926b0fa4cec519cefff54b60bd7942d7871b@sha256:ced8a89d642d10d648471afc2d8737238f1479c368955e6f2553ded58029ac88: 1
                      cilium-operator    quay.io/cilium/operator-generic-ci:latest: 1
                      hubble-relay       quay.io/cilium/hubble-relay-ci:latest: 1
```

Copy First Line Copy Commands Copy All

### Hubble Relay[](#hubble-relay "Link to this heading")

If Hubble Relay is enabled, `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} should display: `OK`{.docutils .literal .notranslate}. Otherwise, we should expect to see errors/warnings reported:

``` {#codecell12}
$ cilium status
    /¯¯\
 /¯¯\__/¯¯\    Cilium:             OK
 \__/¯¯\__/    Operator:           OK
 /¯¯\__/¯¯\    Envoy DaemonSet:    OK
 \__/¯¯\__/    Hubble Relay:       1 errors, 2 warnings
    \__/       ClusterMesh:        disabled

DaemonSet              cilium                   Desired: 1, Ready: 1/1, Available: 1/1
DaemonSet              cilium-envoy             Desired: 1, Ready: 1/1, Available: 1/1
Deployment             cilium-operator          Desired: 1, Ready: 1/1, Available: 1/1
Deployment             hubble-relay             Desired: 1, Unavailable: 1/1
Containers:            cilium                   Running: 1
                       cilium-envoy             Running: 1
                       cilium-operator          Running: 1
                       clustermesh-apiserver
                       hubble-relay             Pending: 1
Cluster Pods:          8/8 managed by Cilium
Helm chart version:    1.17.0
Image versions         cilium             quay.io/cilium/cilium:latest: 1
                       cilium-envoy       quay.io/cilium/cilium-envoy:v1.32.3-1739240299-e85e926b0fa4cec519cefff54b60bd7942d7871b@sha256:ced8a89d642d10d648471afc2d8737238f1479c368955e6f2553ded58029ac88: 1
                       cilium-operator    quay.io/cilium/operator-generic-ci:latest: 1
                       hubble-relay       quay.io/cilium/hubble-relay-ci:latest-: 1
Errors:                hubble-relay       hubble-relay                     1 pods of Deployment hubble-relay are not ready
Warnings:              hubble-relay       hubble-relay-85f98cc7df-s2lkq    pod is pending
                       hubble-relay       hubble-relay-85f98cc7df-s2lkq    pod is pending
```

Copy First Line Copy Commands Copy All

Tip

If warnings or errors are reported for both `Cilium`{.docutils .literal .notranslate} and `Hubble`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Relay`{.docutils .literal .notranslate}, it often hints at a misconfiguration in Hubble or the Hubble system failing to start. Since Hubble is a non-critical system running in the Cilium Agent, it is expected for the Cilium pods to remain running and healthy even when Hubble fails to start. See the [Hubble](#hubble-setup-troubleshooting) section below for Hubble-specific troubleshooting steps.

Verify the state of the pods with:

``` {#codecell13}
$ kubectl -n kube-system get pods -l k8s-app=hubble-relay
NAME                           READY   STATUS             RESTARTS      AGE
hubble-relay-6467f4f4d-x825b   0/1     CrashLoopBackOff   5 (19s ago)   7m28s
```

Copy First Line Copy Commands Copy All

If one or more pods are in `Pending`{.docutils .literal .notranslate} state, describe the pod(s) with:

``` {#codecell14}
$ kubectl describe -n kube-system pod/cilium-5bjkq
Name:             hubble-relay-6467f4f4d-x825b
Namespace:        kube-system
...
```

Copy First Line Copy Commands Copy All

If one or more pods are not in `Running`{.docutils .literal .notranslate} state, look at the pod(s) logs with:

``` {#codecell15}
$ kubectl -n kube-system logs hubble-relay-6467f4f4d-x825b
time="2025-02-12T21:21:40.246596435Z" level=info msg="Starting gRPC health server..." addr=":4222" subsys=hubble-relay
time="2025-02-12T21:21:40.246611018Z" level=info msg="Starting gRPC server..." options="{peerTarget:hubble-peer.kube-system.svc.cluster.local.:443 retryTimeout:30000000000 listenAddress::4245 healthListenAddress::4222 metricsListenAddress: log:0x400038fc00 serverTLSConfig:<nil> insecureServer:true clientTLSConfig:0x4000b12528 clusterName:cluster insecureClient:false observerOptions:[0x28cb1e0 0x28cb2e0] grpcMetrics:<nil> grpcUnaryInterceptors:[] grpcStreamInterceptors:[]}" subsys=hubble-relay
time="2025-02-12T21:21:40.251658493Z" level=info msg="Failed to create peer notify client for peers change notification; will try again after the timeout has expired" connection timeout=30s error="rpc error: code = Unavailable desc = connection error: desc = \"transport: Error while dialing: dial tcp 10.96.49.4:443: connect: connection refused\"" subsys=hubble-relay
time="2025-02-12T21:22:10.25956541Z" level=info msg="Failed to create peer notify client for peers change notification; will try again after the timeout has expired" connection timeout=30s error="rpc error: code = Unavailable desc = connection error: desc = \"transport: Error while dialing: dial tcp 10.96.49.4:443: connect: connection refused\"" subsys=hubble-relay
time="2025-02-12T21:22:40.265123839Z" level=info msg="Failed to create peer notify client for peers change notification; will try again after the timeout has expired" connection timeout=30s error="rpc error: code = Unavailable desc = connection error: desc = \"transport: Error while dialing: dial tcp 10.96.49.4:443: connect: connection refused\"" subsys=hubble-relay
time="2025-02-12T21:22:49.055746359Z" level=info msg="Stopping server..." subsys=hubble-relay
time="2025-02-12T21:22:49.056293486Z" level=info msg="Server stopped" subsys=hubble-relay
```

Copy First Line Copy Commands Copy All

If you face a `connection`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`refused`{.docutils .literal .notranslate} error, it means that Hubble-Relay can't connect to the Hubble API exposed by Cilium agents through the `hubble-peer`{.docutils .literal .notranslate} service. See the [Hubble](#hubble-setup-troubleshooting) section below for Hubble-specific troubleshooting steps.

For TLS related errors, see [Hubble TLS Troubleshooting](../configuration/tls/#hubble-enable-tls-troubleshooting).

### Hubble[](#hubble "Link to this heading")

If Hubble is enabled, `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} should display: `OK`{.docutils .literal .notranslate} for `Cilium`{.docutils .literal .notranslate}. Otherwise, we should expect to see errors/warnings reported:

``` {#codecell16}
$ cilium status
    /¯¯\
 /¯¯\__/¯¯\    Cilium:             1 warnings
 \__/¯¯\__/    Operator:           OK
 /¯¯\__/¯¯\    Envoy DaemonSet:    OK
 \__/¯¯\__/    Hubble Relay:       1 errors
    \__/       ClusterMesh:        disabled

DaemonSet              cilium                   Desired: 1, Ready: 1/1, Available: 1/1
DaemonSet              cilium-envoy             Desired: 1, Ready: 1/1, Available: 1/1
Deployment             cilium-operator          Desired: 1, Ready: 1/1, Available: 1/1
Deployment             hubble-relay             Desired: 1, Unavailable: 1/1
Containers:            cilium                   Running: 1
                       cilium-envoy             Running: 1
                       cilium-operator          Running: 1
                       clustermesh-apiserver
                       hubble-relay             Running: 1
Cluster Pods:          8/8 managed by Cilium
Helm chart version:    1.17.0
Image versions         cilium             quay.io/cilium/cilium:latest: 1
                       cilium-envoy       quay.io/cilium/cilium-envoy:v1.32.3-1739240299-e85e926b0fa4cec519cefff54b60bd7942d7871b@sha256:ced8a89d642d10d648471afc2d8737238f1479c368955e6f2553ded58029ac88: 1
                       cilium-operator    quay.io/cilium/operator-generic-ci:latest: 1
                       hubble-relay       quay.io/cilium/hubble-relay-ci:latest: 1
Errors:                hubble-relay       hubble-relay    1 pods of Deployment hubble-relay are not ready
Warnings:              cilium             cilium-5bjkq    Hubble: failed to setup metrics: metric 'unknown-metric' does not exist
```

Copy First Line Copy Commands Copy All

Verify the state of the pods with:

``` {#codecell17}
$ kubectl -n kube-system get pods -l k8s-app=cilium
NAME           READY   STATUS    RESTARTS      AGE
cilium-5bjkq   1/1     Running   1 (18m ago)   33m
```

Copy First Line Copy Commands Copy All

If one or more pods are in `Pending`{.docutils .literal .notranslate} state, describe the pod(s) with:

``` {#codecell18}
$ kubectl describe -n kube-system pod/cilium-5bjkq
Name:                 cilium-5bjkq
Namespace:            kube-system
...
```

Copy First Line Copy Commands Copy All

If one or more pods are not in `Running`{.docutils .literal .notranslate} state, look at the pod(s) logs with:

``` {#codecell19}
$ kubectl logs -n kube-system -c cilium-agent -l k8s-app=cilium --tail=-1 | grep subsys=hubble
time="2025-02-12T22:12:01.227357082Z" level=info msg="Starting Hubble Metrics server" address=":9965" metrics=unknown-metric subsys=hubble tls=false
time="2025-02-12T22:12:01.22740229Z" level=error msg="Failed to launch hubble" error="failed to setup metrics: metric 'unknown-metric' does not exist" subsys=hubble
```

Copy First Line Copy Commands Copy All

## Next Steps[](#next-steps "Link to this heading")

-   [Inspecting Network Flows with the CLI](../hubble-cli/#hubble-cli)

-   [Service Map & Hubble UI](../hubble-ui/#hubble-ui)

-   [Configure TLS with Hubble](../configuration/tls/#hubble-enable-tls)
