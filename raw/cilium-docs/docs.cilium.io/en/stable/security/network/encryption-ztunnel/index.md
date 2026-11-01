---
{"title": "Ztunnel Transparent Encryption (Beta)", "url": "https://docs.cilium.io/en/stable/security/network/encryption-ztunnel/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Ztunnel Transparent Encryption (Beta)[](#ztunnel-transparent-encryption-beta "Link to this heading")

Note

This is a beta feature. Please provide feedback and file a GitHub issue if you experience any problems.

This guide explains how to configure Cilium to use ztunnel for transparent encryption and mutual TLS (mTLS) authentication between Cilium-managed endpoints. ztunnel is a purpose-built per-node proxy that provides transparent Layer 4 mTLS encryption and authentication for pod-to-pod communication.

When ztunnel is enabled in Cilium, the agent running on each cluster node establishes a control plane connection with the local ztunnel proxy. Cilium enrolls pods into the mesh on a per-namespace basis, allowing fine-grained control over which workloads participate in mTLS encryption. Enrolled pods have their traffic transparently redirected to the ztunnel proxy using iptables rules configured in their network namespace, where the traffic is encrypted and authenticated using mutual TLS before being sent to the destination.

## Generating secrets for authentication[](#generating-secrets-for-authentication "Link to this heading")

Cilium's ztunnel integration requires a set of private keys and accompanying to certificates be present via Kubernetes secrets. This follows the same pattern as IPsec key injections.

These keys can be generated with the following bash script prior to deploying Cilium.

``` {#codecell0}
#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# Copyright Authors of Cilium

set -eu

# == Bootstrap ===
openssl genrsa -out bootstrap-private.key 2048

echo '
[ req ]
distinguished_name = req_distinguished_name
x509_extensions = v3_ca
prompt = no

[ req_distinguished_name ]
O = cluster.local

[ v3_ca ]
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid:always,issuer
basicConstraints = CA:FALSE
keyUsage = digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth, clientAuth
subjectAltName = @alt_names

[alt_names]
DNS.1 = localhost
' > openssl.conf

openssl req -x509 -new -nodes -key bootstrap-private.key -sha256 -days 3650 -out bootstrap-root.crt -config openssl.conf

# == CA ==
openssl genrsa -out ca-private.key 2048

echo '
[ req ]
distinguished_name = req_distinguished_name
x509_extensions = v3_ca
prompt = no

[ req_distinguished_name ]
O = cluster.local

[ v3_ca ]
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid:always,issuer
basicConstraints = critical, CA:true
keyUsage = critical, digitalSignature, cRLSign, keyCertSign
' > openssl.conf

openssl req -x509 -new -nodes -key ca-private.key -sha256 -days 3650 -out ca-root.crt -config openssl.conf

kubectl --namespace kube-system create secret generic cilium-ztunnel-secrets \
      --from-file=bootstrap-private.key=bootstrap-private.key \
      --from-file=bootstrap-root.crt=bootstrap-root.crt \
      --from-file=ca-private.key=ca-private.key \
      --from-file=ca-root.crt=ca-root.crt
```

Copy First Line Copy All

The 'bootstrap' keys are used to secure the connection between ztunnel and Cilium's xDS and certificate server implementation.

The 'ca' keys are used as the root certificate for creating in-memory and ephemeral client certificates on ztunnel's request.

## Enable ztunnel in Cilium[](#enable-ztunnel-in-cilium "Link to this heading")

Before you install Cilium with ztunnel enabled, ensure that:

-   The necessary Kubernetes secrets are available.

-   Cluster Mesh is not enabled (ztunnel is currently not compatible with Cluster Mesh).

If you are deploying Cilium with the Cilium CLI, pass the following options:

``` {#codecell1 .literal-block}
cilium install 1.20.4 \
   --set encryption.enabled=true \
   --set encryption.type=ztunnel
```

Copy First Line Copy All

If you are deploying Cilium with Helm by following [Installation using Helm](../../../installation/k8s-install-helm/#k8s-install-helm), pass the following options:

``` {#codecell2 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
  --namespace kube-system \
  --set encryption.enabled=true \
  --set encryption.type=ztunnel
```

Copy First Line Copy All

## Enrolling Namespaces[](#enrolling-namespaces "Link to this heading")

After enabling ztunnel in Cilium, you need to explicitly enroll namespaces to enable mTLS encryption for their workloads. This is done by applying a label to the namespace:

``` {#codecell3}
kubectl label namespace <namespace-name> io.cilium/mtls-enabled=true
```

Copy Line

To verify that a namespace is enrolled:

``` {#codecell4}
kubectl get namespace <namespace-name> --show-labels
```

Copy Line

When a namespace is enrolled:

-   All existing pods in the namespace (except ztunnel pods themselves) are enrolled

-   Iptables rules are configured in each pod's network namespace for traffic redirection

-   Pod metadata is sent to the ztunnel proxy via the ZDS protocol

-   Future pods created in the namespace are automatically enrolled

To disenroll a namespace:

``` {#codecell5}
kubectl label namespace <namespace-name> io.cilium/mtls-enabled-
```

Copy Line

This will:

1.  Disenroll all pods in the namespace from ztunnel

2.  Remove the iptables rules from each pod's network namespace

3.  Notify ztunnel to stop processing traffic for those workloads

## Validate the Setup[](#validate-the-setup "Link to this heading")

1.  Check that ztunnel has been enabled:

    ``` {#codecell6}
    kubectl -n kube-system describe cm cilium-config | grep enable-ztunnel -A2
    ```

    Copy Line

    You should see output indicating that ztunnel encryption is enabled.

2.  Check which namespaces are enrolled:

    ``` {#codecell7}
    kubectl get namespaces -l io.cilium/mtls-enabled=true
    ```

    Copy Line

    This shows all namespaces labeled for ztunnel enrollment.

    To verify that these namespaces are actually enrolled in the StateDB table:

    ``` {#codecell8}
    kubectl exec -n kube-system ds/cilium -- cilium-dbg statedb dump | jq '.["mtls-enrolled-namespaces"]'
    ```

    Copy Line

    The results of this query should show which namespaces have been successfully processed by the enrollment reconciler.

3.  Run a `bash`{.docutils .literal .notranslate} shell in one of the Cilium pods hosting a mtls-enrolled pod with `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-n`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`kube-system`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`exec`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-ti`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`pod/<cilium-pod-hosting-mtls-pod>`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`--`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`bash`{.docutils .literal .notranslate} and execute the following commands:

    Install tcpdump

    ``` {#codecell9}
    $ apt-get update
    $ apt-get -y install tcpdump
    ```

    Copy First Line Copy Commands Copy All

    Check that traffic is encrypted. In the example below, this can be verified by the fact that packets will have a destination port of 15008 (HBONE). In the example below, `eth0`{.docutils .literal .notranslate} is the interface used for pod-to-pod communication. Replace this interface with e.g. `cilium_vxlan`{.docutils .literal .notranslate} if tunneling is enabled.

    ``` {#codecell10}
    tcpdump -i eth0 port 15008
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
    13:00:06.982499 IP 10.244.1.95.15008 > 10.244.2.3.33446: ...
    13:00:06.982536 IP 10.244.2.3.33446 > 10.244.1.95.15008: ...
    13:00:06.982675 IP 10.244.2.3.33446 > 10.244.1.95.15008: ...
    ```

    Copy First Line Copy All

## Limitations[](#limitations "Link to this heading")

-   Traffic between workloads is only supported when both the source and destination endpoints are enrolled in ztunnel. Communication between an enrolled workload and a non-enrolled workload is not supported.

-   The ztunnel integration currently only supports enrollment via namespace labels. Pod-level enrollment is not supported.

-   Only TCP traffic is currently supported for mTLS encryption. UDP and other protocols are not redirected to ztunnel.

-   The integration requires iptables support in the kernel and cannot be used with environments that do not support iptables (such as some minimal container runtimes).

-   Ztunnel interferes with Cilium network policy as traffic is encrypted before it leaves the pod, meaning L4 policies won't work except for directly targeting the ztunnel HBONE port (15008).

## Known Issues[](#known-issues "Link to this heading")

-   Cluster Mesh is not currently supported when ztunnel is enabled. Attempting to enable both will result in a validation error.

-   Pods without a network namespace path (such as host-networked pods) cannot be enrolled in ztunnel and will be skipped during enrollment.
