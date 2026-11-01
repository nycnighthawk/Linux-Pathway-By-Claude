---
{"title": "Mutual Authentication (Beta)", "url": "https://docs.cilium.io/en/stable/network/servicemesh/mutual-authentication/mutual-authentication/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Mutual Authentication (Beta)[](#mutual-authentication-beta "Link to this heading")

Note

This is a beta feature. Please provide feedback and file a GitHub issue if you experience any problems.

This feature is still incomplete, see [Detailed Roadmap Status](#mutual-auth-roadmap) below for more details.

## Mutual Authentication and mTLS Background[](#mutual-authentication-and-mtls-background "Link to this heading")

Mutual Transport Layer Security (mTLS) is a mechanism that ensures the authenticity, integrity, and confidentiality of data exchanged between two entities over a network.

Unlike traditional TLS, which involves a one-way authentication process where the client verifies the server's identity, mutual TLS adds an additional layer of security by requiring both the client and the server to authenticate each other.

Mutual TLS aims at providing authentication, confidentiality and integrity to service-to-service communications.

## Mutual Authentication in Cilium[](#mutual-authentication-in-cilium "Link to this heading")

Cilium's mTLS-based Mutual Authentication support brings the mutual authentication handshake out-of-band for regular connections.

For Cilium to meet most of the common requirements for service-to-service authentication and encryption, users must enable encryption.

Note

Cilium's encryption features, [WireGuard Transparent Encryption](../../../../security/network/encryption-wireguard/#encryption-wg) and [IPsec Transparent Encryption](../../../../security/network/encryption-ipsec/#encryption-ipsec), can be enabled to automatically create and maintain encrypted connections between Pods.

To address the challenge of identity verification in dynamic and heterogeneous environments, mutual authentication requires a framework for secure identity verification for distributed systems.

Note

To learn more about the Mutual Authentication architecture for the Cilium Service Mesh, read the [CFP](https://github.com/cilium/design-cfps/blob/main/cilium/CFP-22215-mutual-auth-for-service-mesh.md).

## Identity Management[](#identity-management "Link to this heading")

In Cilium's current mutual authentication support, identity management is provided through the use of SPIFFE (Secure Production Identity Framework for Everyone).

### SPIFFE benefits[](#spiffe-benefits "Link to this heading")

Here are some of the benefits provided by [SPIFFE](https://spiffe.io/) :

-   Trustworthy identity issuance: SPIFFE provides a standardized mechanism for issuing and managing identities. It ensures that each service in a distributed system receives a unique and verifiable identity, even in dynamic environments where services may scale up or down frequently.

-   Identity attestation: SPIFFE allows services to prove their identities through attestation. It ensures that services can demonstrate their authenticity and integrity by providing verifiable evidence about their identity, like digital signatures or cryptographic proofs.

-   Dynamic and scalable environments: SPIFFE addresses the challenges of identity management in dynamic environments. It supports automatic identity issuance, rotation, and revocation, which are critical in cloud-native architectures where services may be constantly deployed, updated, or retired.

### Cilium and SPIFFE[](#cilium-and-spiffe "Link to this heading")

SPIFFE provides an API model that allows workloads to request an identity from a central server. In our case, a workload means the same thing that a Cilium Security Identity does - a set of pods described by a label set. A SPIFFE identity is a subclass of URI, and looks something like this: `spiffe://trust.domain/path/with/encoded/info`{.docutils .literal .notranslate}.

There are two main parts of a SPIFFE setup:

-   A central SPIRE server, which forms the root of trust for the trust domain.

-   A per-node SPIRE agent, which first gets its own identity from the SPIRE server, then validates the identity requests of workloads running on its node.

When a workload wants to get its identity, usually at startup, it connects to the local SPIRE agent using the SPIFFE workload API, and describes itself to the agent.

The SPIRE agent then checks that the workload is really who it says it is, and then connects to the SPIRE server and attests that the workload is requesting an identity, and that the request is valid.

The SPIRE agent checks a number of things about the workload, that the pod is actually running on the node it's coming from, that the labels match, and so on.

Once the SPIRE agent has requested an identity from the SPIRE server, it passes it back to the workload in the SVID (SPIFFE Verified Identity Document) format. This document includes a TLS keypair in the X.509 version.

In the usual flow for SPIRE, the workload requests its own information from the SPIRE server. In Cilium's support for SPIFFE, the Cilium agents get a common SPIFFE identity and can themselves ask for identities on behalf of other workloads.

This is demonstrated in the following example.

## Prerequisites[](#prerequisites "Link to this heading")

-   Mutual authentication is only currently supported with SPIFFE APIs for certificate management.

-   The Cilium Helm chart includes an option to deploy a SPIRE server for mutual authentication. You may also deploy your own SPIRE server and configure Cilium to use it.

## Installation[](#installation "Link to this heading")

Note

The default installation requires [PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) support in the cluster, so please check with your cluster provider if it's supported or how to enable it.

For lab or local cluster, you can switch to in-memory storage by passing `authentication.mutual.spire.install.server.dataStorage.enabled=false`{.docutils .literal .notranslate} to the installation command, at the cost of re-creating all data when the SPIRE server pod is restarted.

Install the latest version of the Cilium CLI. The Cilium CLI can be used to install Cilium, inspect the state of a Cilium installation, and enable/disable various features (e.g. clustermesh, Hubble).

``` {#codecell0}
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
```

Copy First Line Copy All

``` {#codecell1}
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

You can enable mutual authentication and its associated SPIRE server with the following command. This command requires the Cilium CLI Helm mode version 0.15 or later.

``` {#codecell2}
$ cilium install \
    --set authentication.mutual.spire.enabled=true \
    --set authentication.mutual.spire.install.enabled=true
```

Copy First Line Copy Commands Copy All

Next, you can check the status of the Cilium agent and operator:

``` {#codecell3}
$ cilium status
```

Copy Line

The Cilium Helm chart includes an option to deploy SPIRE server for mutual authentication. You may also deploy your own SPIRE server and configure Cilium to use it. Please refer to [Installation using Helm](../../../../installation/k8s-install-helm/#k8s-install-helm) for a fresh installation.

``` {#codecell4 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set authentication.enabled=true \
   --set authentication.mutual.spire.enabled=true \
   --set authentication.mutual.spire.install.enabled=true
kubectl -n kube-system rollout restart deployment/cilium-operator
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

``` {#codecell5 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set authentication.enabled=true \
   --set authentication.mutual.spire.enabled=true \
   --set authentication.mutual.spire.install.enabled=true
kubectl -n kube-system rollout restart deployment/cilium-operator
kubectl -n kube-system rollout restart ds/cilium
```

Copy First Line Copy All

Next, you can check the status of the Cilium agent and operator:

``` {#codecell6}
$ cilium status
```

Copy Line

Install the latest version of the Cilium CLI. The Cilium CLI can be used to install Cilium, inspect the state of a Cilium installation, and enable/disable various features (e.g. clustermesh, Hubble).

``` {#codecell7}
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
```

Copy First Line Copy All

``` {#codecell8}
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

## Examples[](#examples "Link to this heading")

Please refer to the following example on how to use and leverage the mutual authentication feature:

-   [Mutual Authentication Example](../mutual-authentication-example/)

Video

> If you'd like a video explanation and demo of Mutual Authentication in Cilium, check out [eCHO episode 100: Next-gen mutual authentication in Cilium](https://www.youtube.com/watch?v=BWjDlynXhzg).

## Limitations[](#limitations "Link to this heading")

-   Cilium Mutual Authentication is still in development and considered beta. Several planned security features have not been implemented yet, see below for details.

-   Cilium's Mutual authentication has only been validated with SPIRE, the production-ready implementation of SPIFFE. As Cilium uses SPIFFE APIs, it's possible that other SPIFFE implementations may work. However, Cilium is currently only tested with the supplied SPIRE install, and using any other SPIFFE implementation is currently not supported.

-   There is no current option to build a single trust domain across multiple clusters for combining Cluster Mesh and Service Mesh. Therefore clusters connected in a Cluster Mesh are not currently compatible with Mutual Authentication.

-   The current support of mutual authentication only works within a Cilium-managed cluster and is not compatible with an external mTLS solution.

## Detailed Roadmap Status[](#detailed-roadmap-status "Link to this heading")

The following table shows the roadmap status of the mutual authentication feature. There are several work items outstanding before the feature is complete from a security model perspective. For details, see [GitHub issue 28986](https://github.com/cilium/cilium/issues/28986).

  --------------------------------------------- ------
  SPIFFE/SPIRE Integration                      Beta
  Authentication API for agent                  Beta
  mTLS handshake between agents                 Beta
  Auth cache to enable per-identity handshake   Beta
  CiliumNetworkPolicy support                   Beta
  Integrate with WireGuard                      TODO
  Per-connection handshake                      TODO
  Sync ipcache with auth data                   TODO
  Detailed documentation of security model      TODO
  Conduct penetration test of model             TODO
  Minimize packet drops                         TODO
  Use auth secret for network encryption        TODO
  Review maturity and consider for stable       TODO
  --------------------------------------------- ------
