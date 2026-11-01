---
{"title": "Defaults certificate for Ingresses", "url": "https://docs.cilium.io/en/stable/network/servicemesh/tls-default-certificate/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Defaults certificate for Ingresses[](#defaults-certificate-for-ingresses "Link to this heading")

Cilium can use a default certificate for ingresses without `.spec.tls[].secretName`{.docutils .literal .notranslate} set. It's still necessary to have `.spec.tls[].hosts`{.docutils .literal .notranslate} defined.

## Prerequisites[](#prerequisites "Link to this heading")

-   Cilium must be configured with Kubernetes Ingress Support. Please refer to [Kubernetes Ingress Support](../ingress/#gs-ingress) for more details.

## Installation[](#installation "Link to this heading")

Defaults certificate for Ingresses can be enabled with helm flags `ingressController.defaultSecretNamespace`{.docutils .literal .notranslate} and `` ingressController.defaultSecretName` ``{.docutils .literal .notranslate} set as true. Please refer to [Installation using Helm](../../../installation/k8s-install-helm/#k8s-install-helm) for a fresh installation.

``` {#codecell0 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set ingressController.defaultSecretNamespace=kube-system \
   --set ingressController.defaultSecretName=default-cert
kubectl -n kube-system rollout restart deployment/cilium-operator
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

``` {#codecell1 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set ingressController.defaultSecretNamespace=kube-system \
   --set ingressController.defaultSecretName=default-cert
kubectl -n kube-system rollout restart deployment/cilium-operator
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

Install the latest version of the Cilium CLI. The Cilium CLI can be used to install Cilium, inspect the state of a Cilium installation, and enable/disable various features (e.g. clustermesh, Hubble).

``` {#codecell2}
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
```

Copy First Line Copy All

``` {#codecell3}
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "arm64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-darwin-${CLI_ARCH}.tar.gz{,.sha256sum}
shasum -a 256 -c cilium-darwin-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-darwin-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-darwin-${CLI_ARCH}.tar.gz{,.sha256sum}
```

Copy First Line Copy All

See the full page of [releases](https://github.com/cilium/cilium-cli/releases/latest).

Cilium Ingress Controller can be enabled with the following command:

``` {#codecell4 .literal-block}
$ cilium install 1.20.4 \
    --set kubeProxyReplacement=true \
    --set ingressController.enabled=true \
    --set ingressController.defaultSecretNamespace=kube-system \
    --set ingressController.defaultSecretName=default-cert
```

Copy First Line Copy All
