---
{"title": "Setting up Cluster Mesh", "url": "https://docs.cilium.io/en/stable/network/clustermesh/setup/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Setting up Cluster Mesh[](#setting-up-cluster-mesh "Link to this heading")

This is a step-by-step guide on how to build a mesh of Kubernetes clusters. This guide shows you how to connect the clusters together, enable pod-to-pod connectivity across all clusters, set up cross-cluster [service discovery and load-balancing](../load-balancing/#gs-clustermesh-load-balancing) and finally enforce security policies to restrict access.

Video

Aside from this step-by-step guide, if you would like to watch how Cilium's Clustermesh feature works, check out [eCHO Episode 41: Cilium Clustermesh](https://www.youtube.com/watch?v=VBOONHW65NU&t=342s).

## Prerequisites[](#prerequisites "Link to this heading")

### Cluster Addressing Requirements[](#cluster-addressing-requirements "Link to this heading")

-   All clusters must be configured with the same datapath mode. Cilium install may default to [Encapsulation](../../concepts/routing/#arch-overlay) or [Native-Routing](../../concepts/routing/#native-routing) mode depending on the specific cloud environment.

-   The Cilium versions of all clusters must differ by no more than one minor release. For example, Cilium `1.18.x`{.docutils .literal .notranslate} can connect to clusters running Cilium `1.17.x`{.docutils .literal .notranslate} or `1.19.x`{.docutils .literal .notranslate}, but not `1.16.x`{.docutils .literal .notranslate}.

-   PodCIDR ranges in all clusters and all nodes must be non-conflicting and unique IP addresses.

-   Nodes in all clusters must have IP connectivity between each other using the configured InternalIP for each node. This requirement is typically met by establishing peering or VPN tunnels between the networks of the nodes of each cluster.

-   The network between clusters must allow the inter-cluster communication. The exact ports are documented in the [Firewall Rules](../../../operations/system_requirements/#firewall-requirements) section.

Note

For cloud-specific deployments, the following guides show how to meet the above requirements:

-   [AKS-to-AKS Clustermesh Preparation](../aks-clustermesh-prep/)
-   [EKS-to-EKS Clustermesh Preparation](../eks-clustermesh-prep/)
-   [GKE-to-GKE Clustermesh Preparation](../gke-clustermesh-prep/)

#### Additional Requirements for Native-routed Datapath Modes[](#additional-requirements-for-native-routed-datapath-modes "Link to this heading")

-   Cilium in each cluster must be configured with a native routing CIDR that covers all the PodCIDR ranges across all connected clusters. Cluster CIDRs are typically allocated from the `10.0.0.0/8`{.docutils .literal .notranslate} private address space. When this is the case a native routing CIDR such as `10.0.0.0/8`{.docutils .literal .notranslate} should cover all clusters:

> -   ConfigMap option `ipv4-native-routing-cidr=10.0.0.0/8`{.docutils .literal .notranslate}
>
> -   Helm option `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipv4NativeRoutingCIDR=10.0.0.0/8`{.docutils .literal .notranslate}
>
> -   `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`install`{.docutils .literal .notranslate} option `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipv4NativeRoutingCIDR=10.0.0.0/8`{.docutils .literal .notranslate}

-   In addition to nodes, pods in all clusters must have IP connectivity between each other. This requirement is typically met by establishing peering or VPN tunnels between the networks of the nodes of each cluster

-   The network between clusters must allow pod-to-pod inter-cluster communication across any ports that the pods may use. This is typically accomplished with firewall rules allowing pods in different clusters to reach each other on all ports.

### Scaling Limitations[](#scaling-limitations "Link to this heading")

-   By default, the maximum number of clusters that can be connected together using Cluster Mesh is 255. By using the option `maxConnectedClusters`{.docutils .literal .notranslate} this limit can be set to 511, at the expense of lowering the maximum number of cluster-local identities. Reference the following table for valid configurations and their corresponding cluster-local identity limits:

  MaxConnectedClusters   Maximum cluster-local identities      
  ---------------------- ---------------------------------- -- --
  255 (default)          65535                                 
  511                    32767                                 

-   All clusters across a Cluster Mesh must be configured with the same `maxConnectedClusters`{.docutils .literal .notranslate} value.

> -   ConfigMap option `max-connected-clusters=511`{.docutils .literal .notranslate}
>
> -   Helm option `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`clustermesh.maxConnectedClusters=511`{.docutils .literal .notranslate}
>
> -   `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`install`{.docutils .literal .notranslate} option `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`clustermesh.maxConnectedClusters=511`{.docutils .literal .notranslate}

Note

This option controls the bit allocation of numeric identities and will affect the maximum number of cluster-local identities that can be allocated. By default, cluster-local [Security Identities](../../../internals/security-identities/#security-identities) are limited to 65535, regardless of whether Cluster Mesh is used or not.

Warning

`MaxConnectedClusters`{.docutils .literal .notranslate} can only be set once during Cilium installation and should not be changed for existing clusters. Changing this option on a live cluster may result in connection disruption and possible incorrect enforcement of network policies

## Prepare the Clusters[](#prepare-the-clusters "Link to this heading")

For the rest of this tutorial, we will assume that you intend to connect two clusters together with the kubectl configuration context stored in the environment variables `$CLUSTER1`{.docutils .literal .notranslate} and `$CLUSTER2`{.docutils .literal .notranslate}. This context name is the same as you typically pass to `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`--context`{.docutils .literal .notranslate}.

### Specify the Cluster Name and ID[](#specify-the-cluster-name-and-id "Link to this heading")

Cilium needs to be installed onto each cluster.

Each cluster must be assigned a unique human-readable name as well as a numeric cluster ID (1-255). The cluster name must respect the following constraints:

-   It must contain at most 32 characters;

-   It must begin and end with a lower case alphanumeric character;

-   It may contain lower case alphanumeric characters and dashes between.

It is best to assign both the cluster name and the cluster ID at installation time. Set the following Helm values for each cluster:

``` {#codecell0}
cluster:
  name: cluster1
  id: 1
```

Copy First Line Copy All

Use a different name and ID in each cluster. Review [Cilium Quick Installation](../../../gettingstarted/k8s-install-default/#k8s-install-quick) for more details and use cases.

Important

If you change the cluster ID and/or cluster name in a cluster with running workloads, you will need to restart all workloads. The cluster ID is used to generate the security identity and it will need to be re-created in order to establish access across clusters.

### Configure TLS certificates[](#configure-tls-certificates "Link to this heading")

Cluster Mesh uses mTLS to secure control plane connections within and between clusters. TLS certificates can be generated automatically or manually provided.

The following options are available to configure TLS certificates automatically:

-   cilium's [certgen](https://github.com/cilium/certgen) (using a Kubernetes `CronJob`{.docutils .literal .notranslate})

-   [cert-manager](https://cert-manager.io/)

-   [Helm](https://helm.sh/docs/chart_template_guide/function_list/#gensignedcert)

Every cluster must trust the certificates presented by the other clusters. Use a common root CA, or configure `tls.caBundle`{.docutils .literal .notranslate} with every trusted CA certificate.

When using certgen, TLS certificates are generated at installation time and a Kubernetes `CronJob`{.docutils .literal .notranslate} is scheduled to renew them (regardless of their expiration date). The certgen method is easier to implement than cert-manager but less flexible.

The following Helm values configure certgen:

``` {#codecell1}
clustermesh:
  apiserver:
    tls:
      auto:
        # enable automatic TLS certificate generation
        enabled: true
        # auto generate certificates using cronJob method
        method: cronJob
        # certificates validity duration in days (default 1 year)
        certValidityDuration: 365
        # schedule for certificate re-generation (crontab syntax)
        schedule: "0 0 1 */4 *"
```

Copy First Line Copy All

This method relies on [cert-manager](https://cert-manager.io/) to generate the TLS certificates. cert-manager is the de facto way to manage TLS certificates on Kubernetes, and it has the following advantages compared to the other documented methods:

-   Support for multiple issuers (e.g. a custom CA, [Vault](https://www.vaultproject.io/), [Let's Encrypt](https://letsencrypt.org/), [Google's Certificate Authority Service](https://cloud.google.com/certificate-authority-service), and more) allowing to choose the issuer fitting your organization's requirements.

-   Manages certificates via a [CRD](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) which is easier to inspect with Kubernetes tools than PEM files.

**Installation steps:**

1.  First, install [cert-manager](https://cert-manager.io/docs/installation/) and setup an [issuer](https://cert-manager.io/docs/configuration/). Please make sure that your issuer can create certificates for the configured Cluster Mesh API server names.

2.  Install or upgrade Cilium with the following Helm values:

``` {#codecell2}
clustermesh:
  apiserver:
    tls:
      auto:
        # enable automatic TLS certificate generation
        enabled: true
        # auto generate certificates using cert-manager
        method: certmanager
        # certificates validity duration in days (default 1 year)
        certValidityDuration: 365
        certManagerIssuerRef:
          # Reference to cert-manager's issuer
          group: cert-manager.io
          kind: ClusterIssuer
          name: ca-issuer
```

Copy First Line Copy All

During the first Cilium installation, cert-manager's webhook might not yet be available when Cilium creates its `Certificate`{.docutils .literal .notranslate} resources. See [TLS Certificate Troubleshooting](../../../operations/troubleshooting/#troubleshooting-clustermesh-tls) if that occurs.

When using Helm, TLS certificates are (re-)generated every time Helm is used to install or upgrade Cilium.

The following Helm values configure Helm certificate generation:

``` {#codecell3}
clustermesh:
  apiserver:
    tls:
      auto:
        # enable automatic TLS certificate generation
        enabled: true
        # auto generate certificates using helm method
        method: helm
        # certificates validity duration in days (default 1 year)
        certValidityDuration: 365
```

Copy First Line Copy All

The downside of the Helm method is that while certificates are automatically generated, they are not automatically renewed. Consequently, running `helm`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`upgrade`{.docutils .literal .notranslate} is required when certificates are about to expire (i.e. before the configured `clustermesh.apiserver.tls.auto.certValidityDuration`{.docutils .literal .notranslate}).

In order to provide your own TLS certificates, `clustermesh.apiserver.tls.auto.enabled`{.docutils .literal .notranslate} must be set to `false`{.docutils .literal .notranslate}, and the following fixed-name Secrets must be created in the namespace where Cilium is installed, which is typically `kube-system`{.docutils .literal .notranslate}.

The **Common Name (CN)** and **Subject Alternative Name (SAN)** of the certificates must be set as follows:

-   Server: CN `clustermesh-apiserver.<namespace>.svc`{.docutils .literal .notranslate}. SANs must include `clustermesh-apiserver.<namespace>.svc`{.docutils .literal .notranslate}, `*.mesh.cilium.io`{.docutils .literal .notranslate}, `127.0.0.1`{.docutils .literal .notranslate}, `::1`{.docutils .literal .notranslate}, and every DNS name through which remote clusters reach the Cluster Mesh API Service

-   Admin: CN `admin-<cluster-name>`{.docutils .literal .notranslate}

-   Remote: CN `remote`{.docutils .literal .notranslate} with the default `migration`{.docutils .literal .notranslate} authentication mode

-   Local: CN `local-<cluster-name>`{.docutils .literal .notranslate}

Once the certificates have been issued, create the following Secrets in the target namespace:

-   `clustermesh-apiserver-server-cert`{.docutils .literal .notranslate}

-   `clustermesh-apiserver-admin-cert`{.docutils .literal .notranslate}

-   `clustermesh-apiserver-remote-cert`{.docutils .literal .notranslate}

-   `clustermesh-apiserver-local-cert`{.docutils .literal .notranslate}

Each Secret must contain the following keys:

-   `tls.crt`{.docutils .literal .notranslate}: The certificate file

-   `tls.key`{.docutils .literal .notranslate}: The private key file

-   `ca.crt`{.docutils .literal .notranslate}: The CA certificate file

After creating the Secrets, install or upgrade Cilium with automatic certificate generation disabled using the following Helm values:

``` {#codecell4}
clustermesh:
  apiserver:
    tls:
      auto:
        enabled: false
```

Copy First Line Copy All

For TLS troubleshooting, see [TLS Certificate Troubleshooting](../../../operations/troubleshooting/#troubleshooting-clustermesh-tls).

### Configure Cluster Mesh with Helm[](#configure-cluster-mesh-with-helm "Link to this heading")

The following example values files configure `cluster1`{.docutils .literal .notranslate} and `cluster2`{.docutils .literal .notranslate} as a Cluster Mesh. Adapt them to your environment. They assume that the Cluster Mesh API servers are reachable through a LoadBalancer exposed with a `clusterX.example.com`{.docutils .literal .notranslate} DNS name, and use certgen with a shared CA for simplicity. Choose a different certificate method if appropriate, as described in [Configure TLS certificates](#clustermesh-setup-tls).

Create the following values files:

``` {#codecell5}
cluster:
  name: cluster1
  id: 1

clustermesh:
  useAPIServer: true

  config:
    enabled: true

  apiserver:
    service:
      type: LoadBalancer
      annotations: {}
      # The following annotations are examples. Adapt them to your
      # environment and context.
      #
      # Optional: Have ExternalDNS create the DNS records to
      # reach this API server. Otherwise, create the same record
      # through your usual DNS management workflow.
      # annotations:
      #   external-dns.alpha.kubernetes.io/hostname: cluster1.example.com
      #
      # AKS:
      # annotations:
      #   service.beta.kubernetes.io/azure-load-balancer-internal: "true"
      #
      # EKS:
      # annotations:
      #   service.beta.kubernetes.io/aws-load-balancer-scheme: internal
      #
      # GKE:
      # annotations:
      #   networking.gke.io/load-balancer-type: Internal
      #   networking.gke.io/internal-load-balancer-allow-global-access: "true"
    tls:
      auto:
        enabled: true
        method: cronJob
        server:
          extraDnsNames:
            - cluster1.example.com

  # Optional Cluster Mesh features that you may find useful:
  # enableEndpointSliceSynchronization: true
  # mcsapi:
  #   enabled: true
  #   corednsAutoConfigure:
  #     enabled: true
```

Copy First Line Copy All

``` {#codecell6}
cluster:
  name: cluster2
  id: 2

clustermesh:
  useAPIServer: true

  config:
    enabled: true

  apiserver:
    service:
      type: LoadBalancer
      annotations: {}
      # The following annotations are examples. Adapt them to your
      # environment and context.
      #
      # Optional: Have ExternalDNS create the DNS records to
      # reach this API server. Otherwise, create the same record
      # through your usual DNS management workflow.
      # annotations:
      #   external-dns.alpha.kubernetes.io/hostname: cluster2.example.com
      #
      # AKS:
      # annotations:
      #   service.beta.kubernetes.io/azure-load-balancer-internal: "true"
      #
      # EKS:
      # annotations:
      #   service.beta.kubernetes.io/aws-load-balancer-scheme: internal
      #
      # GKE:
      # annotations:
      #   networking.gke.io/load-balancer-type: Internal
      #   networking.gke.io/internal-load-balancer-allow-global-access: "true"
    tls:
      auto:
        enabled: true
        method: cronJob
        server:
          extraDnsNames:
            - cluster2.example.com

  # Optional Cluster Mesh features that you may find useful:
  # enableEndpointSliceSynchronization: true
  # mcsapi:
  #   enabled: true
  #   corednsAutoConfigure:
  #     enabled: true
```

Copy First Line Copy All

``` {#codecell7}
clustermesh:
  config:
    clusters:
      cluster1:
        address: cluster1.example.com
        port: 2379
      cluster2:
        address: cluster2.example.com
        port: 2379
```

Copy First Line Copy All

The `clusters.yaml`{.docutils .literal .notranslate} file contains all the remote clusters so that you don't have to repeat the same information in every cluster's values file. Note that this is possible since Cilium ignores the local cluster from the list of remote clusters.

Important

All the possible values for `clustermesh.apiserver.service.type`{.docutils .literal .notranslate} are:

LoadBalancer:

:   A Kubernetes service of type LoadBalancer is used to expose the control plane. This uses a stable LoadBalancer IP and is typically the best option.

NodePort:

:   A Kubernetes service of type NodePort is used to expose the control plane. This requires stable Node IPs. If a node disappears, the Cluster Mesh may have to reconnect to a different node. If all nodes have become unavailable, you may have to re-connect the clusters to extract new node IPs.

ClusterIP:

:   A Kubernetes service of type ClusterIP is used to expose the control plane. This requires the ClusterIPs are routable between clusters. This is typically only available via the helm chart installation method.

``` {#codecell8 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --kube-context $CLUSTER1 --reuse-values -f clusters.yaml -f cluster1.yaml
```

Copy First Line Copy All

``` {#codecell9 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --kube-context $CLUSTER1 --reuse-values -f clusters.yaml -f cluster1.yaml
```

Copy First Line Copy All

Copy the Cilium CA to `cluster2`{.docutils .literal .notranslate} before enabling Cluster Mesh there, so both clusters generate certificates signed by the same CA:

``` {#codecell10}
$ kubectl --context $CLUSTER1 get secret -n kube-system cilium-ca -o yaml | \
    kubectl --context $CLUSTER2 create -f -
```

Copy First Line Copy Commands Copy All

``` {#codecell11 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --kube-context $CLUSTER2 --reuse-values -f clusters.yaml -f cluster2.yaml
```

Copy First Line Copy All

``` {#codecell12 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --kube-context $CLUSTER2 --reuse-values -f clusters.yaml -f cluster2.yaml
```

Copy First Line Copy All

Adapt these files to your configuration-management model as needed. For example, you can use a common values file for all the shared settings or split the cluster map into group files to apply only the groups that each cluster should join and build a "partial mesh" instead of connecting every cluster to every other cluster.

Cluster Mesh supports many other configuration scenarios such as using a standalone etcd with the KVStore mode, generating your own certificates and/or etcd client config, or configuring a partial mesh where not all clusters are connected to all others. Don't hesitate to explore the Helm values to discover all the available options.

### Install the Cilium CLI[](#install-the-cilium-cli "Link to this heading")

The remaining validation steps use the Cilium CLI. It is also required if you use the alternative Cilium CLI setup.

Install the latest version of the Cilium CLI. The Cilium CLI can be used to install Cilium, inspect the state of a Cilium installation, and enable/disable various features (e.g. clustermesh, Hubble).

``` {#codecell13}
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
```

Copy First Line Copy All

``` {#codecell14}
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

### Alternative: configure with the Cilium CLI[](#alternative-configure-with-the-cilium-cli "Link to this heading")

The Cilium CLI can also enable and configure Cluster Mesh across clusters. It is a wrapper around Helm and may be used alongside Helm when applicable. This can be convenient if you are already using the Cilium CLI to configure Cilium or to do a quick setup such as in a lab environment or for a demo.

This alternative still requires a unique `cluster.name`{.docutils .literal .notranslate} and `cluster.id`{.docutils .literal .notranslate} to be configured in every cluster.

Example install using the Cilium CLI:

``` {#codecell15}
$ cilium install --set cluster.name=$CLUSTER1 --set cluster.id=1 --context $CLUSTER1
$ cilium install --set cluster.name=$CLUSTER2 --set cluster.id=2 --context $CLUSTER2
```

Copy First Line Copy Commands Copy All

Review [Cilium Quick Installation](../../../gettingstarted/k8s-install-default/#k8s-install-quick) for more details and use cases.

Enable all required components by running `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`clustermesh`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`enable`{.docutils .literal .notranslate} in the context of both clusters. This will deploy the `clustermesh-apiserver`{.docutils .literal .notranslate} into the cluster and generate all required certificates and import them as Kubernetes secrets. It will also attempt to auto-detect the best service type for the LoadBalancer to expose the Cluster Mesh control plane to other clusters.

``` {#codecell16}
$ cilium clustermesh enable --context $CLUSTER1
$ cilium clustermesh enable --context $CLUSTER2
```

Copy First Line Copy Commands Copy All

Finally, connect the clusters. This step only needs to be done in one direction. The connection will automatically be established in both directions:

``` {#codecell17}
$ cilium clustermesh connect --context $CLUSTER1 --destination-context $CLUSTER2
```

Copy Line

### Validate Cluster Mesh[](#validate-cluster-mesh "Link to this heading")

Wait for the Cluster Mesh components to come up by invoking `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`clustermesh`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`--wait`{.docutils .literal .notranslate}. If you are using a service of type LoadBalancer then this will also wait for the LoadBalancer to be assigned an IP.

``` {#codecell18}
$ cilium clustermesh status --context $CLUSTER1 --wait
$ cilium clustermesh status --context $CLUSTER2 --wait
```

Copy First Line Copy Commands Copy All

The output will look something like this:

``` {#codecell19}
✅ Cluster access information is available:
  - 10.168.0.89:2379
✅ Service "clustermesh-apiserver" of type "LoadBalancer" found
⌛ Waiting (12s) for clusters to be connected: 2 nodes are not ready
⌛ Waiting (25s) for clusters to be connected: 2 nodes are not ready
⌛ Waiting (38s) for clusters to be connected: 2 nodes are not ready
⌛ Waiting (51s) for clusters to be connected: 2 nodes are not ready
⌛ Waiting (1m4s) for clusters to be connected: 2 nodes are not ready
⌛ Waiting (1m17s) for clusters to be connected: 1 nodes are not ready
✅ All 2 nodes are connected to all clusters [min:1 / avg:1.0 / max:1]
🔌 Cluster Connections:
- cilium-cli-ci-multicluster-2-168: 2/2 configured, 2/2 connected
```

Copy First Line Copy All

If this step does not complete successfully, proceed to the [Troubleshooting](#clustermesh-setup-troubleshooting) section.

### Test Pod Connectivity Between Clusters[](#test-pod-connectivity-between-clusters "Link to this heading")

Congratulations, you have successfully connected your clusters together. You can validate the connectivity by running the connectivity test in multi cluster mode:

``` {#codecell20}
$ cilium connectivity test --context $CLUSTER1 --multi-cluster $CLUSTER2
```

Copy Line

### Next Steps[](#next-steps "Link to this heading")

Logical next steps to explore from here are:

> -   [Load-balancing & Service Discovery](../load-balancing/#gs-clustermesh-load-balancing)
>
> -   [Network Policy](../policy/#gs-clustermesh-network-policy)

## Troubleshooting[](#troubleshooting "Link to this heading")

Use the following list of steps to troubleshoot issues with ClusterMesh:

> 1.  Validate that Cilium pods are healthy and ready:
>
>     ``` {#codecell21}
>     $ cilium status --context $CLUSTER1
>     $ cilium status --context $CLUSTER2
>     ```
>
>     Copy First Line Copy Commands Copy All
>
> 2.  Validate that Cluster Mesh is enabled and operational:
>
>     ``` {#codecell22}
>     $ cilium clustermesh status --context $CLUSTER1
>     $ cilium clustermesh status --context $CLUSTER2
>     ```
>
>     Copy First Line Copy Commands Copy All

If you cannot resolve the issue with the above commands, see the [Cluster Mesh Troubleshooting](../../../operations/troubleshooting/#troubleshooting-clustermesh) for a more detailed troubleshooting guide.
