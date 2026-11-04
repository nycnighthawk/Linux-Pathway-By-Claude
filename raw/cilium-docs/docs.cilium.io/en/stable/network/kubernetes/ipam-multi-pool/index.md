---
{"title": "CRD-Backed by Cilium Multi-Pool IPAM", "url": "https://docs.cilium.io/en/stable/network/kubernetes/ipam-multi-pool/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# CRD-Backed by Cilium Multi-Pool IPAM[](#crd-backed-by-cilium-multi-pool-ipam "Link to this heading")

This is a quick tutorial walking through how to enable multi-pool IPAM backed by the `CiliumPodIPPool`{.docutils .literal .notranslate} CRD. The purpose of this tutorial is to show how components are configured and resources interact with each other to enable users to automate or extend on their own.

For more details, see the section [Multi-Pool](../../concepts/ipam/multi-pool/#ipam-crd-multi-pool)

## Enable Multi-pool IPAM mode[](#enable-multi-pool-ipam-mode "Link to this heading")

1.  Setup Cilium for Kubernetes using helm with the options:

    -   `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipam.mode=multi-pool`{.docutils .literal .notranslate}

    -   `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`kubeProxyReplacement=true`{.docutils .literal .notranslate}

    -   `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`bpf.masquerade=true`{.docutils .literal .notranslate}

    For more details on why each of these options are needed, please refer to [Limitations](../../concepts/ipam/multi-pool/#ipam-crd-multi-pool-limitations).

2.  Create the `default`{.docutils .literal .notranslate} pool for IPv4 addresses with the options:

    -   `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipam.operator.autoCreateCiliumPodIPPools.default.ipv4.cidrs='{10.10.0.0/16}'`{.docutils .literal .notranslate}

    -   `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipam.operator.autoCreateCiliumPodIPPools.default.ipv4.maskSize=27`{.docutils .literal .notranslate}

3.  Deploy Cilium and Cilium-Operator. Cilium will automatically wait until the `podCIDR`{.docutils .literal .notranslate} is allocated for its node by Cilium Operator.

## Validate installation[](#validate-installation "Link to this heading")

1.  Validate that Cilium has started up correctly

    ``` {#codecell0}
    $ cilium status --wait
        /¯¯\
     /¯¯\__/¯¯\    Cilium:             OK
     \__/¯¯\__/    Operator:           OK
     /¯¯\__/¯¯\    Envoy DaemonSet:    disabled (using embedded mode)
     \__/¯¯\__/    Hubble Relay:       OK
        \__/       ClusterMesh:        disabled

    [...]
    ```

    Copy First Line Copy Commands Copy All

2.  Validate that the `CiliumPodIPPool`{.docutils .literal .notranslate} resource for the `default`{.docutils .literal .notranslate} pool was created with the CIDRs specified in the `ipam.operator.autoCreateCiliumPodIPPools.default.*`{.docutils .literal .notranslate} Helm values:

    ``` {#codecell1}
    $ kubectl get ciliumpodippool default -o yaml
    apiVersion: cilium.io/v2alpha1
    kind: CiliumPodIPPool
    metadata:
      name: default
    spec:
      ipv4:
        cidrs:
        - 10.10.0.0/16
        maskSize: 27
    ```

    Copy First Line Copy Commands Copy All

3.  Create an additional pod IP pool `mars`{.docutils .literal .notranslate} using the following `CiliumPodIPPool`{.docutils .literal .notranslate} resource:

    ``` {#codecell2}
    $ cat <<EOF | kubectl apply -f -
    apiVersion: cilium.io/v2alpha1
    kind: CiliumPodIPPool
    metadata:
      name: mars
    spec:
      ipv4:
        cidrs:
        - 10.20.0.0/16
        maskSize: 27
    EOF
    ```

    Copy First Line Copy Commands Copy All

4.  Validate that both pool resources exist:

    ``` {#codecell3}
    $ kubectl get ciliumpodippools
    NAME      AGE
    default   106s
    mars      7s
    ```

    Copy First Line Copy Commands Copy All

5.  Create two deployments with two pods each. One allocating from the `default`{.docutils .literal .notranslate} pool and one allocating from the `mars`{.docutils .literal .notranslate} pool by way of the `ipam.cilium.io/ipam-pool:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`mars`{.docutils .literal .notranslate} annotation:

    ``` {#codecell4}
    $ cat <<EOF | kubectl apply -f -
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx-default
    spec:
      selector:
        matchLabels:
          app: nginx-default
      replicas: 2
      template:
        metadata:
          labels:
            app: nginx-default
        spec:
          containers:
          - name: nginx
            image: nginx:1.25.1
            ports:
            - containerPort: 80
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx-mars
    spec:
      selector:
        matchLabels:
          app: nginx-mars
      replicas: 2
      template:
        metadata:
          labels:
            app: nginx-mars
          annotations:
            ipam.cilium.io/ip-pool: mars
        spec:
          containers:
          - name: nginx
            image: nginx:1.25.1
            ports:
            - containerPort: 80
    EOF
    ```

    Copy First Line Copy Commands Copy All

6.  Validate that the pods were assigned IPv4 addresses from different CIDRs as specified in the pool definition:

    ``` {#codecell5}
    $ kubectl get pods -o wide
    NAME                             READY   STATUS    RESTARTS   AGE    IP            NODE           NOMINATED NODE   READINESS GATES
    nginx-default-79885c7f58-fdfgf   1/1     Running   0          5s     10.10.10.36   kind-worker2   <none>           <none>
    nginx-default-79885c7f58-qch6b   1/1     Running   0          5s     10.10.10.77   kind-worker    <none>           <none>
    nginx-mars-76766f95f5-d9vzt      1/1     Running   0          5s     10.20.0.20    kind-worker2   <none>           <none>
    nginx-mars-76766f95f5-mtn2r      1/1     Running   0          5s     10.20.0.37    kind-worker    <none>           <none>
    ```

    Copy First Line Copy Commands Copy All

7.  Test connectivity between pods:

    ``` {#codecell6}
    $ kubectl exec pod/nginx-default-79885c7f58-fdfgf -- curl -s -o /dev/null -w "%{http_code}" http://10.20.0.37
    200
    ```

    Copy First Line Copy Commands Copy All

8.  Alternatively, the `ipam.cilium.io/ipam-pool`{.docutils .literal .notranslate} annotation can also be applied to a namespace:

    ``` {#codecell7}
    $ kubectl create namespace cilium-test-1
    $ kubectl annotate namespace cilium-test-1 ipam.cilium.io/ip-pool=mars
    ```

    Copy First Line Copy Commands Copy All

    All new pods created in the namespace `cilium-test-1`{.docutils .literal .notranslate} will be assigned IPv4 addresses from the `mars`{.docutils .literal .notranslate} pool. Run the Cilium connectivity tests (which use namespace `cilium-test-1`{.docutils .literal .notranslate} by default to create their workloads) to verify connectivity:

    ``` {#codecell8}
    $ cilium connectivity test
    [...]
    ✅ All 42 tests (295 actions) successful, 13 tests skipped, 0 scenarios skipped.
    ```

    Copy First Line Copy Commands Copy All

> **Note:** The connectivity test requires a cluster with at least 2 worker nodes to complete successfully.

1.  Verify that the connectivity test pods were assigned IPv4 addresses from the 10.20.0.0/16 CIDR defined in the `mars`{.docutils .literal .notranslate} pool:

    ``` {#codecell9}
    $ kubectl --namespace cilium-test get pods -o wide
    NAME                                  READY   STATUS    RESTARTS   AGE     IP            NODE                 NOMINATED NODE   READINESS GATES
    client-6f6788d7cc-7fw9w               1/1     Running   0          8m56s   10.20.0.238   kind-worker          <none>           <none>
    client2-bc59f56d5-hsv2g               1/1     Running   0          8m56s   10.20.0.193   kind-worker          <none>           <none>
    echo-other-node-646976b7dd-5zlr4      2/2     Running   0          8m56s   10.20.1.145   kind-worker2         <none>           <none>
    echo-same-node-58f99d79f4-4k5v4       2/2     Running   0          8m56s   10.20.0.202   kind-worker          <none>           <none>
    ...
    ```

    Copy First Line Copy Commands Copy All
