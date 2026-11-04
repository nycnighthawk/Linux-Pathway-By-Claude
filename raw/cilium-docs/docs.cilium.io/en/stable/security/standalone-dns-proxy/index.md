---
{"title": "Standalone DNS Proxy (alpha)", "url": "https://docs.cilium.io/en/stable/security/standalone-dns-proxy/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Standalone DNS Proxy (alpha)[](#standalone-dns-proxy-alpha "Link to this heading")

Note

This is an alpha feature. Please provide feedback and file a GitHub issue if you experience any problems.

The Standalone DNS Proxy is an independent component that runs as a separate DaemonSet in the cluster, providing DNS proxying capabilities independent of the Cilium agent. The in-agent proxy runs alongside the Standalone DNS Proxy. The load of DNS request is shared between both proxies.

## Overview[](#overview "Link to this heading")

The Standalone DNS Proxy communicates with the Cilium agent via gRPC to:

1.  Receive DNS policy rules from the agent

2.  Report DNS query results for policy enforcement to the agent

## Configuration[](#configuration "Link to this heading")

To enable the Standalone DNS Proxy, set the following Helm values:

``` {#codecell0}
# Enable L7 proxy and configure DNS proxy port
l7Proxy: true
dnsProxy:
  proxyPort: 10094  # Must be non-zero when using standalone DNS proxy, choosing 10094 as example

# Enable standalone DNS proxy
standaloneDnsProxy:
  enabled: true
  serverPort: 10095 # Must be non-zero when using standalone DNS proxy, choosing 10095 as example
```

Copy First Line Copy All

Important

The standalone DNS proxy uses the agent's DNS configuration to ensure consistency:

-   `dnsProxy.proxyPort`{.docutils .literal .notranslate} must be explicitly set to a non-zero value (e.g., 10094)

-   `dnsProxy.enableDnsCompression`{.docutils .literal .notranslate} and other DNS settings will automatically use the same defaults as the agent (default: true)

The Helm chart will fail validation if `proxyPort`{.docutils .literal .notranslate} is not configured correctly.

## Testing the Standalone DNS Proxy[](#testing-the-standalone-dns-proxy "Link to this heading")

This section provides steps to test the Standalone DNS Proxy in a development environment. To test the standalone DNS proxy feature, you need to build container images from source. The following instructions guide you through building and deploying the standalone DNS proxy in a local development environment using kind (Kubernetes in Docker).

### Building and Deploying[](#building-and-deploying "Link to this heading")

1.  **Build the Standalone DNS Proxy Image**

    Build the standalone DNS proxy container image from source:

    ``` {#codecell1}
    $ make docker-standalone-dns-proxy-image
    ```

    Copy Line

    This creates a local image `quay.io/cilium/standalone-dns-proxy:latest`{.docutils .literal .notranslate}.

2.  **Set Up kind Cluster with Cilium**

    Create a kind cluster and build/install Cilium from source:

    ``` {#codecell2}
    $ make kind && make kind-image && make kind-install-cilium
    ```

    Copy Line

3.  **Load the Standalone DNS Proxy Image into kind**

    Load the standalone DNS proxy image you built into the kind cluster:

    ``` {#codecell3}
    $ kind load docker-image quay.io/cilium/standalone-dns-proxy:latest
    ```

    Copy Line

4.  **Upgrade Cilium to Enable Standalone DNS Proxy**

    Enable the standalone DNS proxy and configure it to work with the Cilium agent:

    ``` {#codecell4}
    $ cilium upgrade \
        --chart-directory='./install/kubernetes/cilium' \
        --set='l7Proxy=true' \
        --set='dnsProxy.proxyPort=10094' \
        --helm-set='standaloneDnsProxy.enabled=true' \
        --helm-set='standaloneDnsProxy.image.repository=quay.io/cilium/standalone-dns-proxy' \
        --helm-set='standaloneDnsProxy.image.tag=latest' \
        --helm-set='standaloneDnsProxy.image.useDigest=false' \
        --helm-set='standaloneDnsProxy.image.pullPolicy=Never'
    ```

    Copy First Line Copy Commands Copy All

    The configuration flags in this example ensure the standalone proxy is operational by applying the following configurations:

    -   `dnsProxy.proxyPort=10094`{.docutils .literal .notranslate} sets the DNS proxy port used by both the agent and standalone DNS proxy

    -   `l7Proxy=true`{.docutils .literal .notranslate} enables L7 proxy support required for DNS policy enforcement

    -   The standalone DNS proxy automatically inherits DNS settings from the agent configuration

    -   `image.tag=latest`{.docutils .literal .notranslate} and `image.pullPolicy=Never`{.docutils .literal .notranslate} are used to reference the locally-built image

5.  **Restart Cilium Agent**

    Restart the Cilium agent to apply the configuration changes:

    ``` {#codecell5}
    $ kubectl rollout restart ds -n kube-system cilium
    ```

    Copy Line

6.  **Verify Deployment**

    Check that the standalone DNS proxy pods are running:

    ``` {#codecell6}
    $ kubectl -n kube-system get pods -l k8s-app=standalone-dns-proxy
    NAME                          READY   STATUS    RESTARTS   AGE
    standalone-dns-proxy-xxxxx    1/1     Running   0          1m
    ```

    Copy First Line Copy Commands Copy All

7.  **Apply DNS Policy**

    Apply a policy that allows pods with the label `org:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`alliance`{.docutils .literal .notranslate} to query specific domains (`cilium.io`{.docutils .literal .notranslate} and its subdomains) and blocks all other queries:

    ``` {#codecell7}
    apiVersion: cilium.io/v2
    kind: CiliumNetworkPolicy
    metadata:
      name: "tofqdn-dns-visibility"
    spec:
      endpointSelector:
        matchLabels:
          any:org: alliance
      egress:
      - toEndpoints:
        - matchLabels:
           "k8s:io.kubernetes.pod.namespace": kube-system
           "k8s:k8s-app": kube-dns
        toPorts:
          - ports:
             - port: "53"
               protocol: ANY
            rules:
              dns:
                - matchName: "cilium.io"
                - matchPattern: "*.cilium.io"
                - matchPattern: "*.api.cilium.io"

      - toFQDNs:
          - matchName: "cilium.io"
          - matchName: "sub.cilium.io"
          - matchName: "service1.api.cilium.io"
          - matchPattern: "special*service.api.cilium.io"
        toPorts:
          - ports:
             - port: "80"
               protocol: TCP
    ```

    Copy First Line Copy All

    ``` {#codecell8}
    $ kubectl apply -f examples/policies/l7/dns/dns.yaml
    ```

    Copy Line

8.  **Deploy Test Pod**

    Create a test pod with the matching label:

    ``` {#codecell9}
    $ kubectl run test-pod --image=nicolaka/netshoot --labels="org=alliance" -- sleep 3600
    ```

    Copy Line

9.  **Verify DNS Policy Enforcement**

    Test that DNS queries are being intercepted and resolved for allowed domains:

    ``` {#codecell10}
    $ kubectl exec test-pod -- nslookup cilium.io.
    ```

    Copy Line

    Queries to `cilium.io`{.docutils .literal .notranslate} should succeed.

    Now test that queries to non-allowed domains are refused:

    ``` {#codecell11}
    $ kubectl exec test-pod -- nslookup example.com.
    Server:         10.96.0.10
    Address:        10.96.0.10#53

    ** server can't find example.com: REFUSED
    ```

    Copy First Line Copy Commands Copy All

    The query to `example.com`{.docutils .literal .notranslate} is refused because it's not in the allowed DNS policy rules.

10. **Test Standalone Proxy Resilience**

    > Verify that the standalone DNS proxy continues to work even when the Cilium agent is down:
    >
    > ``` {#codecell12}
    > # Intentionally break the Cilium agent by using a non-existent image
    > $ kubectl set image -n kube-system ds/cilium cilium-agent=quay.io/cilium/cilium:non-existent-image
    >
    > # Wait for agent pods to enter ImagePullBackOff state
    > $ kubectl wait --for=condition=Ready=false pod -n kube-system -l k8s-app=cilium --timeout=60s
    >
    > # DNS queries for allowed domains should still work via standalone DNS proxy
    > $ kubectl exec test-pod -- nslookup cilium.io
    >
    > # Verify that policy enforcement still works - non-allowed domains are still refused
    > $ kubectl exec test-pod -- nslookup example.com
    > Server:         10.96.0.10
    > Address:        10.96.0.10#53
    >
    > ** server can't find example.com: REFUSED
    > ```
    >
    > Copy First Line Copy Commands Copy All
    >
    > Both queries demonstrate that the standalone DNS proxy continues to enforce DNS policies independently, allowing `cilium.io`{.docutils .literal .notranslate} and refusing `example.com`{.docutils .literal .notranslate}, even when the agent is unavailable.

11. **Restore Cilium Agent**

    > Restore the Cilium agent to normal operation:
    >
    > ``` {#codecell13}
    > $ kubectl rollout undo ds/cilium -n kube-system
    > ```
    >
    > Copy Line

For more information on DNS policies, see [DNS based](../policy/layer3/#dns-based).

## Limitations[](#limitations "Link to this heading")

The Standalone DNS Proxy alpha release has the following known limitations:

-   The standalone DNS proxy uses the agent's DNS configuration. The `dnsProxy.proxyPort`{.docutils .literal .notranslate} must be explicitly set to a non-zero value when the standalone DNS proxy is enabled (it does not automatically select a free port).

-   Metrics related to DNS are not supported yet. The metrics are currently only available from the in-agent DNS proxy.

-   Standalone DNS proxy depends on Cilium agent to read DNS policies, enforce them and communicate via gRPC. If there are connectivity issues between the proxy and agent, DNS policy enforcement may be affected.

-   While the standalone DNS proxy can continue to proxy DNS requests when the agent is down, it cannot allocate new identities for domains that haven't been observed before. If an endpoint looks up a new domain (one that hasn't been cached) while the agent is unavailable, the resulting traffic will be dropped because no security identity can be allocated. Only DNS lookups for previously observed domains (with cached identities) will work during agent downtime.

## Troubleshooting[](#troubleshooting "Link to this heading")

### Validation Errors[](#validation-errors "Link to this heading")

If the Helm chart fails with a validation error about `dnsProxy.proxyPort`{.docutils .literal .notranslate}:

``` {#codecell14}
Error: standaloneDnsProxy requires dnsProxy.proxyPort to be set to a non-zero value (e.g., 10094)
```

Copy Line

This means you need to explicitly configure the DNS proxy port in your values:

``` {#codecell15}
dnsProxy:
  proxyPort: 10094  # Must be non-zero
```

Copy First Line Copy All

### Port Configuration Verification[](#port-configuration-verification "Link to this heading")

To verify that the DNS proxy port is correctly configured:

``` {#codecell16}
$ kubectl -n kube-system get configmap cilium-config -o yaml | grep 'tofqdns-proxy-port'
$ kubectl -n kube-system get configmap standalone-dns-proxy-config -o yaml | grep 'tofqdns-proxy-port'
```

Copy First Line Copy Commands Copy All

Both ConfigMaps should show the same value from `dnsProxy.proxyPort`{.docutils .literal .notranslate}.

### gRPC Communication Issues[](#grpc-communication-issues "Link to this heading")

If there are communication issues between the proxy and agent, review agent logs for connection errors:

``` {#codecell17}
$ kubectl -n kube-system logs -l k8s-app=cilium --tail=100 | grep -i "fqdn.sdp-grpc-server"
```

Copy Line

## API Reference[](#api-reference "Link to this heading")

For detailed API documentation, see [SDP gRPC API Reference](../../sdpapi/#sdpapi-ref).

## Further Reading[](#further-reading "Link to this heading")

-   [DNS based](../policy/layer3/#dns-based)

-   [DNS Proxy](../policy/layer7/#dns-proxy)
