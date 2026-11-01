---
{"title": "Tutorial: Monitoring Generic IP Options with Cilium", "url": "https://docs.cilium.io/en/stable/observability/hubble/ip-packet-tracing/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Tutorial: Monitoring Generic IP Options with Cilium[](#tutorial-monitoring-generic-ip-options-with-cilium "Link to this heading")

This tutorial demonstrates how to configure Cilium to detect, extract, and monitor arbitrary IP Options from network packets.

Cilium v1.19 and later implements IP Options packet tracing. IP Options tracing supports reading specific IP Options (configured via Helm) and displaying the extracted data within Cilium Monitor and Hubble. This capability is essential for observing network metadata injected by sidecars or upstream appliances.

Note that Cilium is responsible only for observing this metadata. You are responsible for ensuring that your applications, sidecars, or network devices are configured to inject the desired IP Options into the traffic.

## Prerequisites[](#prerequisites "Link to this heading")

-   Dependencies: `kind`{.docutils .literal .notranslate}, `helm`{.docutils .literal .notranslate}, `docker`{.docutils .literal .notranslate}, `Hubble`{.docutils .literal .notranslate} CLI, and the `cilium`{.docutils .literal .notranslate} CLI.

## Cluster Setup[](#cluster-setup "Link to this heading")

Create a kind cluster and install Cilium with the `bpf.monitorTraceIPOption`{.docutils .literal .notranslate} flag enabled.

1.  Configure kind

    Create a `kind-config-ip-tracing.yaml`{.docutils .literal .notranslate} file based on the following template. This will create 2 nodes (1 control plane and 1 worker).

    ``` {#codecell0}
    kind: Cluster
    apiVersion: kind.x-k8s.io/v1alpha4
    nodes:
    - role: control-plane
    - role: worker
    networking:
      disableDefaultCNI: true
    ```

    Copy First Line Copy All

2.  Create the kind Cluster

    ``` {#codecell1}
    kind create cluster --config=kind-config-ip-tracing.yaml
    ```

    Copy Line

3.  Setup Helm Repository

    Add the Cilium Helm repository if you haven't already

    ``` {#codecell2}
    helm repo add cilium https://helm.cilium.io/
    ```

    Copy Line

4.  Install Cilium with IP Option Monitoring and restart the agent

    Install Cilium using Helm. The key flag here is `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`bpf.monitorTraceIPOption=136`{.docutils .literal .notranslate}. This flag configures Cilium to extract data from IP Option 136 packets. IP option 136 represents a "Stream ID", which will be used later in this guide to generate tracing packets.

    > ``` {#codecell3 .literal-block}
    > helm install cilium cilium/cilium --version 1.20.4 \
    >    --namespace kube-system \
    >    --set hubble.enabled=true \
    >    --set hubble.relay.enabled=true \
    >    --set hubble.ui.enabled=true \
    >    --set bpf.monitorTraceIPOption=136
    > kubectl -n kube-system wait --for=condition=ready pod -l k8s-app=cilium --timeout=300s
    > ```
    >
    > Copy First Line Copy All
    >
    > ``` {#codecell4 .literal-block}
    > helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
    >    --namespace kube-system \
    >    --set hubble.enabled=true \
    >    --set hubble.relay.enabled=true \
    >    --set hubble.ui.enabled=true \
    >    --set bpf.monitorTraceIPOption=136
    > kubectl -n kube-system wait --for=condition=ready pod -l k8s-app=cilium --timeout=300s
    > ```
    >
    > Copy First Line Copy All

## Manual Verification[](#manual-verification "Link to this heading")

To verify the feature, manually inject a known Trace ID into packets using `nping`{.docutils .literal .notranslate}. The following examples uses a payload of 4 bytes to meet the strict length requirements.

1.  Deploy Client and Server Pods Deploy an `nginx`{.docutils .literal .notranslate} server and a `netshoot`{.docutils .literal .notranslate} client (containing `nping`{.docutils .literal .notranslate}):

    ``` {#codecell5}
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: client
      labels:
        app: client
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: client
      template:
        metadata:
          labels:
            app: client
        spec:
          containers:
          - name: client
            image: nicolaka/netshoot
            command:
            - sleep
            args:
            - "infinity"
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: server
      labels:
        app: server
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: server
      template:
        metadata:
          labels:
            app: server
        spec:
          containers:
          - name: server
            image: nginx
            ports:
            - containerPort: 80
    ```

    Copy First Line Copy All

    ``` {#codecell6 .literal-block}
    kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-ip-options/ip-options-pods.yaml
    ```

    Copy Line

    Wait for the deployments to become ready

    ``` {#codecell7}
    kubectl rollout status deployment client
    kubectl rollout status deployment server
    ```

    Copy First Line Copy All

2.  Trigger Traffic with Valid IP Options

    Execute `nping`{.docutils .literal .notranslate} from the client to the server, manually specifying the IP Option hex string.

    ``` {#codecell8}
    # 1. Get the IP of the server pod
    server_ip=$(kubectl get pods -l app=server -o jsonpath='{.items[0].status.podIP}')

    # 2. Run nping with Option 136 (0x88)
    # Format: \x88 (Type 136) \x04 (Data + header length) \x34\x21 (Data/ID)
    # The data 0x3421 corresponds to decimal 13345.
    # Note: Length must be exactly 2, 4 or 8 bytes of payload. Length 4 for the message indicates 2 bytes of payload
    kubectl exec deployment/client -- nping --tcp -p 80 --ip-options '\x88\x04\x34\x21' -c 3 ${server_ip}
    ```

    Copy First Line Copy Commands Copy All

## Observing with Hubble[](#observing-with-hubble "Link to this heading")

With traffic flowing, use the Hubble CLI to observe the extracted data.

1.  Build and Connect Hubble

    ``` {#codecell9}
    cd hubble
    make hubble
    cilium hubble port-forward &
    ```

    Copy First Line Copy All

2.  Filter by Trace ID

    Filter specifically for the injected ID `13345`{.docutils .literal .notranslate} (hex `0x3421`{.docutils .literal .notranslate}):

    ``` {#codecell10}
    ./hubble observe -f --ip-trace-id 13345
    ```

    Copy Line

    Verify that flows between the `client`{.docutils .literal .notranslate} and `server`{.docutils .literal .notranslate} pods appear with the matching ID.
