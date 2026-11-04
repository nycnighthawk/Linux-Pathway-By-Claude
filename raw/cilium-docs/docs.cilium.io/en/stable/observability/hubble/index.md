---
{"title": "Network Observability with Hubble", "url": "https://docs.cilium.io/en/stable/observability/hubble/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Network Observability with Hubble[](#network-observability-with-hubble "Link to this heading")

Observability is provided by Hubble which enables deep visibility into the communication and behavior of services as well as the networking infrastructure in a completely transparent manner. Hubble is able to provide visibility at the node level, cluster level or even across clusters in a [Multi-Cluster (Cluster Mesh)](../../network/clustermesh/intro/#cluster-mesh) scenario. For an introduction to Hubble and how it relates to Cilium, read the section [Introduction to Cilium & Hubble](../../overview/intro/#intro).

By default, Hubble API operates within the scope of the individual node on which the Cilium agent runs. This confines the network insights to the traffic observed by the local Cilium agent. Hubble CLI (`hubble`{.docutils .literal .notranslate}) can be used to query the Hubble API provided via a local Unix Domain Socket. The Hubble CLI binary is installed by default on Cilium agent pods.

Upon deploying Hubble Relay, network visibility is provided for the entire cluster or even multiple clusters in a ClusterMesh scenario. In this mode, Hubble data can be accessed by directing Hubble CLI (`hubble`{.docutils .literal .notranslate}) to the Hubble Relay service or via Hubble UI. Hubble UI is a web interface which enables automatic discovery of the services dependency graph at the L3/L4 and even L7 layer, allowing user-friendly visualization and filtering of data flows as a service map.

-   [Setting up Hubble Observability](setup/)
    -   [Enable Hubble in Cilium](setup/#enable-hubble-in-cilium)
    -   [Install the Hubble Client](setup/#install-the-hubble-client)
    -   [Validate Hubble API Access](setup/#validate-hubble-api-access)
    -   [Troubleshooting Hubble Deployment](setup/#troubleshooting-hubble-deployment)
    -   [Next Steps](setup/#next-steps)
-   [Inspecting Network Flows with the CLI](hubble-cli/)
    -   [Pre-Requisites](hubble-cli/#pre-requisites)
    -   [Inspecting the cluster's network traffic with Hubble Relay](hubble-cli/#inspecting-the-cluster-s-network-traffic-with-hubble-relay)
    -   [Filtering Encrypted Traffic](hubble-cli/#filtering-encrypted-traffic)
    -   [Filtering Reply Traffic](hubble-cli/#filtering-reply-traffic)
    -   [Next Steps](hubble-cli/#next-steps)
-   [Service Map & Hubble UI](hubble-ui/)
    -   [Enable the Hubble UI](hubble-ui/#enable-the-hubble-ui)
    -   [Open the Hubble UI](hubble-ui/#open-the-hubble-ui)
    -   [Inspecting a wide variety of network traffic](hubble-ui/#inspecting-a-wide-variety-of-network-traffic)
-   [Tutorial: Monitoring Generic IP Options with Cilium](ip-packet-tracing/)
    -   [Prerequisites](ip-packet-tracing/#prerequisites)
    -   [Cluster Setup](ip-packet-tracing/#cluster-setup)
    -   [Manual Verification](ip-packet-tracing/#manual-verification)
    -   [Observing with Hubble](ip-packet-tracing/#observing-with-hubble)
-   [Configuring Hubble exporter](configuration/export/)
    -   [Prerequisites](configuration/export/#prerequisites)
    -   [Basic Configuration](configuration/export/#basic-configuration)
    -   [Performance tuning](configuration/export/#performance-tuning)
    -   [Dynamic exporter configuration](configuration/export/#dynamic-exporter-configuration)
-   [Configure TLS with Hubble](configuration/tls/)
    -   [Enable TLS on the Hubble API](configuration/tls/#enable-tls-on-the-hubble-api)
    -   [Hubble Metrics TLS and Authentication](configuration/tls/#hubble-metrics-tls-and-authentication)
    -   [Access the Hubble API with TLS Enabled](configuration/tls/#access-the-hubble-api-with-tls-enabled)
