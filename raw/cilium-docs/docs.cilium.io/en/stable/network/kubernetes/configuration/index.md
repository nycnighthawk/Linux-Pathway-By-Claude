---
{"title": "Configuration", "url": "https://docs.cilium.io/en/stable/network/kubernetes/configuration/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Configuration[](#configuration "Link to this heading")

## ConfigMap Options[](#configmap-options "Link to this heading")

In the [ConfigMap](../../../glossary/#term-ConfigMap) there are several options that can be configured according to your preferences:

-   `debug`{.docutils .literal .notranslate} - Sets to run Cilium in full debug mode, which enables verbose logging and configures eBPF programs to emit more visibility events into the output of `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`monitor`{.docutils .literal .notranslate}.

-   `enable-ipv4`{.docutils .literal .notranslate} - Enable IPv4 addressing support

-   `enable-ipv6`{.docutils .literal .notranslate} - Enable IPv6 addressing support

-   `clean-cilium-bpf-state`{.docutils .literal .notranslate} - Removes all eBPF state from the filesystem on startup. Endpoints will be restored with the same IP addresses, but ongoing connections may be briefly disrupted and loadbalancing decisions will be lost, so active connections via the loadbalancer will break. All eBPF state will be reconstructed from their original sources (for example, from Kubernetes or the kvstore). This may be used to mitigate serious issues regarding eBPF maps. This option should be turned off again after restarting the daemon.

-   `clean-cilium-state`{.docutils .literal .notranslate} - Removes **all** Cilium state, including unrecoverable information such as all endpoint state, as well as recoverable state such as eBPF state pinned to the filesystem, CNI configuration files, library code, links, routes, and other information. **This operation is irreversible**. Existing endpoints currently managed by Cilium may continue to operate as before, but Cilium will no longer manage them and they may stop working without warning. After using this operation, endpoints must be deleted and reconnected to allow the new instance of Cilium to manage them.

-   `monitor-aggregation`{.docutils .literal .notranslate} - This option enables coalescing of tracing events in `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`monitor`{.docutils .literal .notranslate} to only include periodic updates from active flows, or any packets that involve an L4 connection state change. Valid options are `none`{.docutils .literal .notranslate}, `low`{.docutils .literal .notranslate}, `medium`{.docutils .literal .notranslate}, `maximum`{.docutils .literal .notranslate}.

    -   `none`{.docutils .literal .notranslate} - Generate a tracing event on every receive and send packet.

    -   `low`{.docutils .literal .notranslate} - Generate a tracing event on every send packet.

    -   `medium`{.docutils .literal .notranslate} - Generate a tracing event for send packets only on every new connection, any time a packet contains TCP flags that have not been previously seen for the packet direction, and on average once per `monitor-aggregation-interval`{.docutils .literal .notranslate} (assuming that a packet is seen during the interval). Each direction tracks TCP flags and report interval separately. If Cilium drops a packet, it will emit one event per packet dropped.

    -   `maximum`{.docutils .literal .notranslate} - An alias for the most aggressive aggregation level. Currently this is equivalent to setting `monitor-aggregation`{.docutils .literal .notranslate} to `medium`{.docutils .literal .notranslate}.

    When socket load-balancing is enabled, these aggregation levels also apply to socket translation events:

    -   `none`{.docutils .literal .notranslate} - Emit all socket trace events

    -   `lowest`{.docutils .literal .notranslate}/`low`{.docutils .literal .notranslate} - Suppress reverse-direction (recv) socket trace events

    -   `medium`{.docutils .literal .notranslate}/`maximum`{.docutils .literal .notranslate} - Emit socket trace events only for connect system calls

-   `monitor-aggregation-interval`{.docutils .literal .notranslate} - Defines the interval to report tracing events. Only applicable for `monitor-aggregation`{.docutils .literal .notranslate} levels `medium`{.docutils .literal .notranslate} or higher. Assuming new packets are sent at least once per interval, this ensures that on average one event is sent during the interval.

-   `preallocate-bpf-maps`{.docutils .literal .notranslate} - Pre-allocation of map entries allows per-packet latency to be reduced, at the expense of up-front memory allocation for the entries in the maps. Set to `true`{.docutils .literal .notranslate} to optimize for latency. If this value is modified, then during the next Cilium startup connectivity may be temporarily disrupted for endpoints with active connections.

Any changes that you perform in the Cilium [ConfigMap](../../../glossary/#term-ConfigMap) and in `cilium-etcd-secrets`{.docutils .literal .notranslate} `Secret`{.docutils .literal .notranslate} will require you to restart any existing Cilium pods in order for them to pick the latest configuration.

Attention

When updating keys or values in the ConfigMap, the changes might take up to 2 minutes to be propagated to all nodes running in the cluster. For more information see the official Kubernetes docs: [Mounted ConfigMaps are updated automatically](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#mounted-configmaps-are-updated-automatically)

The following [ConfigMap](../../../glossary/#term-ConfigMap) is an example where the etcd cluster is running in 2 nodes, `node-1`{.docutils .literal .notranslate} and `node-2`{.docutils .literal .notranslate} with TLS, and client to server authentication enabled.

``` {#codecell0}
apiVersion: v1
kind: ConfigMap
metadata:
  name: cilium-config
  namespace: kube-system
data:
  # The kvstore configuration is used to enable use of a kvstore for state
  # storage.
  kvstore: etcd
  kvstore-opt: '{"etcd.config": "/var/lib/etcd-config/etcd.config"}'

  # This etcd-config contains the etcd endpoints of your cluster. If you use
  # TLS please make sure you follow the tutorial in https://cilium.link/etcd-config
  etcd-config: |-
    ---
    endpoints:
      - https://node-1:31079
      - https://node-2:31079
    #
    # In case you want to use TLS in etcd, uncomment the 'trusted-ca-file' line
    # and create a kubernetes secret by following the tutorial in
    # https://cilium.link/etcd-config
    trusted-ca-file: '/var/lib/etcd-secrets/etcd-client-ca.crt'
    #
    # In case you want client to server authentication, uncomment the following
    # lines and create a kubernetes secret by following the tutorial in
    # https://cilium.link/etcd-config
    key-file: '/var/lib/etcd-secrets/etcd-client.key'
    cert-file: '/var/lib/etcd-secrets/etcd-client.crt'

  # If you want to run cilium in debug mode change this value to true
  debug: "false"
  enable-ipv4: "true"
  # If you want to clean cilium state; change this value to true
  clean-cilium-state: "false"
```

Copy First Line Copy All

### CNI[](#cni "Link to this heading")

[CNI](../../../glossary/#term-CNI) - Container Network Interface is the plugin layer used by Kubernetes to delegate networking configuration. You can find additional information on the [CNI](../../../glossary/#term-CNI) project website.

CNI configuration is automatically taken care of when deploying Cilium via the provided [DaemonSet](../../../glossary/#term-DaemonSet). The `cilium`{.docutils .literal .notranslate} pod will generate an appropriate CNI configuration file and write it to disk on startup.

Note

In order for CNI installation to work properly, the `kubelet`{.docutils .literal .notranslate} task must either be running on the host filesystem of the worker node, or the `/etc/cni/net.d`{.docutils .literal .notranslate} and `/opt/cni/bin`{.docutils .literal .notranslate} directories must be mounted into the container where `kubelet`{.docutils .literal .notranslate} is running. This can be achieved with [Volumes](../../../glossary/#term-Volumes) mounts.

The CNI auto installation is performed as follows:

1.  The `/etc/cni/net.d`{.docutils .literal .notranslate} and `/opt/cni/bin`{.docutils .literal .notranslate} directories are mounted from the host filesystem into the pod where Cilium is running.

2.  The binary `cilium-cni`{.docutils .literal .notranslate} is installed to `/opt/cni/bin`{.docutils .literal .notranslate}. Any existing binary with the name `cilium-cni`{.docutils .literal .notranslate} is overwritten.

3.  The file `/etc/cni/net.d/05-cilium.conflist`{.docutils .literal .notranslate} is written.

## Adjusting CNI configuration[](#adjusting-cni-configuration "Link to this heading")

The CNI configuration file is automatically written and maintained by the cilium pod. It is written after the agent has finished initialization and is ready to handle pod sandbox creation. In addition, the agent will remove any other CNI configuration files by default.

There are a number of Helm variables that adjust CNI configuration management. For a full description, see the helm documentation. A brief summary:

  Helm variable                                       Description                              Default
  --------------------------------------------------- ---------------------------------------- ---------
  `cni.customConf`{.docutils .literal .notranslate}   Disable CNI configuration management     false
  `cni.exclusive`{.docutils .literal .notranslate}    Remove other CNI configuration files     true
  `cni.install`{.docutils .literal .notranslate}      Install CNI configuration and binaries   true

If you want to provide your own custom CNI configuration file, you can do so by passing a path to a cni template file, either on disk or provided via a configMap. The Helm options that configure this are:

  Helm variable                                         Description
  ----------------------------------------------------- ----------------------------------------------------------------
  `cni.readCniConf`{.docutils .literal .notranslate}    Path (inside the agent) to a source CNI configuration file
  `cni.configMap`{.docutils .literal .notranslate}      Name of a ConfigMap containing a source CNI configuration file
  `cni.configMapKey`{.docutils .literal .notranslate}   Install CNI configuration and binaries

These Helm variables are converted to a smaller set of cilium ConfigMap keys:

  ConfigMap key                                                  Description
  -------------------------------------------------------------- --------------------------------------------------------
  `write-cni-conf-when-ready`{.docutils .literal .notranslate}   Path to write the CNI configuration file
  `read-cni-conf`{.docutils .literal .notranslate}               Path to read the source CNI configuration file
  `cni-exclusive`{.docutils .literal .notranslate}               Whether or not to remove other CNI configuration files

### CRD Validation[](#crd-validation "Link to this heading")

Custom Resource Validation was introduced in Kubernetes since version `1.8.0`{.docutils .literal .notranslate}. This is still considered an alpha feature in Kubernetes `1.8.0`{.docutils .literal .notranslate} and beta in Kubernetes `1.9.0`{.docutils .literal .notranslate}.

Since Cilium `v1.0.0-rc3`{.docutils .literal .notranslate}, Cilium will create, or update in case it exists, the Cilium Network Policy (CNP) Resource Definition with the embedded validation schema. This allows the validation of CiliumNetworkPolicy to be done on the kube-apiserver when the policy is imported with an ability to provide direct feedback when importing the resource.

To enable this feature, the flag `--feature-gates=CustomResourceValidation=true`{.docutils .literal .notranslate} must be set when starting kube-apiserver. Cilium itself will automatically make use of this feature and no additional flag is required.

Note

In case there is an invalid CNP before updating to Cilium `v1.0.0-rc3`{.docutils .literal .notranslate}, which contains the validator, the kube-apiserver validator will prevent Cilium from updating that invalid CNP with Cilium node status. By checking Cilium logs for `unable`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`to`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`update`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`CNP,`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`retrying...`{.docutils .literal .notranslate}, it is possible to determine which Cilium Network Policies are considered invalid after updating to Cilium `v1.0.0-rc3`{.docutils .literal .notranslate}.

To verify that the CNP resource definition contains the validation schema, run the following command:

``` {#codecell1}
$ kubectl get crd ciliumnetworkpolicies.cilium.io -o json | grep -A 12 openAPIV3Schema
        "openAPIV3Schema": {
            "oneOf": [
                {
                    "required": [
                        "spec"
                    ]
                },
                {
                    "required": [
                        "specs"
                    ]
                }
            ],
```

Copy First Line Copy Commands Copy All

In case the user writes a policy that does not conform to the schema, Kubernetes will return an error, e.g.:

``` {#codecell2}
cat <<EOF > ./bad-cnp.yaml
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: my-new-cilium-object
spec:
  description: "Policy to test multiple rules in a single file"
  endpointSelector:
    matchLabels:
      app: details
      track: stable
      version: v1
  ingress:
  - fromEndpoints:
    - matchLabels:
        app: reviews
        track: stable
        version: v1
    toPorts:
    - ports:
      - port: '65536'
        protocol: TCP
      rules:
        http:
        - method: GET
          path: "/health"
EOF

kubectl create -f ./bad-cnp.yaml
...
spec.ingress.toPorts.ports.port in body should match '^(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[0-9]{1,4})$'
```

Copy First Line Copy All

In this case, the policy has a port out of the 0-65535 range.

### Mounting BPFFS with systemd[](#mounting-bpffs-with-systemd "Link to this heading")

Due to how systemd [mounts](https://unix.stackexchange.com/questions/283442/systemd-mount-fails-where-setting-doesnt-match-unit-name) filesystems, the mount point path must be reflected in the unit filename.

``` {#codecell3}
cat <<EOF | sudo tee /etc/systemd/system/sys-fs-bpf.mount
[Unit]
Description=Cilium BPF mounts
Documentation=https://docs.cilium.io/
DefaultDependencies=no
Before=local-fs.target umount.target
After=swap.target

[Mount]
What=bpffs
Where=/sys/fs/bpf
Type=bpf
Options=rw,nosuid,nodev,noexec,relatime,mode=700

[Install]
WantedBy=multi-user.target
EOF
```

Copy First Line Copy All

### Container Runtimes[](#container-runtimes "Link to this heading")

## CRIO[](#crio "Link to this heading")

If you want to use CRIO, use the instructions below.

Setup Helm repository:

``` {#codecell4}
helm repo add cilium https://helm.cilium.io/
```

Copy Line

Cilium charts are also available via OCI registries (Quay.io and Docker Hub). No setup required - you can install directly using `oci://`{.docutils .literal .notranslate} URLs.

See the [OCI Registry section](../../../installation/k8s-install-helm/#k8s-install-helm) for more information, including chart signing verification and digest-based installations.

Note

The Helm flag `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`bpf.autoMount.enabled=false`{.docutils .literal .notranslate} might not be required for your setup. For more info see [Common CRIO issues](#crio-known-issues).

``` {#codecell5 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system
```

Copy First Line Copy All

``` {#codecell6 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system
```

Copy First Line Copy All

Since CRI-O does not automatically detect that a new CNI plugin has been installed, you will need to restart the CRI-O daemon for it to pick up the Cilium CNI configuration.

First make sure Cilium is running:

``` {#codecell7}
$ kubectl get pods -n kube-system -o wide
NAME               READY     STATUS    RESTARTS   AGE       IP          NODE
cilium-mqtdz       1/1       Running   0          3m       10.0.2.15   minikube
```

Copy First Line Copy Commands Copy All

After that you can restart CRI-O:

``` {#codecell8}
minikube ssh -- sudo systemctl restart crio
```

Copy Line

## Common CRIO issues[](#common-crio-issues "Link to this heading")

Some CRI-O environments automatically mount the bpf filesystem in the pods, which is something that Cilium avoids doing when `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`bpf.autoMount.enabled=false`{.docutils .literal .notranslate} is set. However, some CRI-O environments do not mount the bpf filesystem automatically which causes Cilium to print the following message:

``` {#codecell9}
level=warning msg="BPF system config check: NOT OK." error="CONFIG_BPF kernel parameter is required" subsys=linux-datapath
level=warning msg="================================= WARNING ==========================================" subsys=bpf
level=warning msg="BPF filesystem is not mounted. This will lead to network disruption when Cilium pods" subsys=bpf
level=warning msg="are restarted. Ensure that the BPF filesystem is mounted in the host." subsys=bpf
level=warning msg="https://docs.cilium.io/en/stable/operations/system_requirements/#mounted-ebpf-filesystem" subsys=bpf
level=warning msg="====================================================================================" subsys=bpf
level=info msg="Mounting BPF filesystem at /sys/fs/bpf" subsys=bpf
```

Copy First Line Copy All

If you see this warning in the Cilium pod logs with your CRI-O environment, please remove the flag `--set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`bpf.autoMount.enabled=false`{.docutils .literal .notranslate} from your Helm setup and redeploy Cilium.
