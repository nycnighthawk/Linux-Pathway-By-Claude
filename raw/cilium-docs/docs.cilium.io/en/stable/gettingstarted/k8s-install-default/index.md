---
{"title": "Cilium Quick Installation", "url": "https://docs.cilium.io/en/stable/gettingstarted/k8s-install-default/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Cilium Quick Installation[](#cilium-quick-installation "Link to this heading")

This guide will walk you through the quick default installation. It will automatically detect and use the best configuration possible for the Kubernetes distribution you are using. All state is stored using Kubernetes custom resource definitions (CRDs).

This is the best installation method for most use cases. For large environments (\> 500 nodes) or if you want to run specific datapath modes, refer to the [Getting Started](../../#getting-started) guide.

Should you encounter any issues during the installation, please refer to the [Troubleshooting](../../network/kubernetes/troubleshooting/#troubleshooting-k8s) section and/or seek help on [Cilium Slack](https://slack.cilium.io).

## Create the Cluster[](#create-the-cluster "Link to this heading")

If you don't have a Kubernetes Cluster yet, you can use the instructions below to create a Kubernetes cluster locally or using a managed Kubernetes service:

The following commands create a Kubernetes cluster using [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine). See [Installing Google Cloud SDK](https://cloud.google.com/sdk/install) for instructions on how to install `gcloud`{.docutils .literal .notranslate} and prepare your account.

``` {#codecell0}
export NAME="$(whoami)-$RANDOM"
# Create the node pool with the following taint to guarantee that
# Pods are only scheduled/executed in the node when Cilium is ready.
# Alternatively, see the note below.
gcloud container clusters create "${NAME}" \
 --node-taints node.cilium.io/agent-not-ready=true:NoExecute \
 --zone us-west2-a
gcloud container clusters get-credentials "${NAME}" --zone us-west2-a
```

Copy First Line Copy All

Note

Please make sure to read and understand the documentation page on [taint effects and unmanaged pods](../../installation/taints/#taint-effects).

The following commands create a Kubernetes cluster using [Azure Kubernetes Service](https://docs.microsoft.com/en-us/azure/aks/) with no CNI plugin pre-installed (BYOCNI). See [Azure Cloud CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) for instructions on how to install `az`{.docutils .literal .notranslate} and prepare your account, and the [Bring your own CNI documentation](https://docs.microsoft.com/en-us/azure/aks/use-byo-cni?tabs=azure-cli) for more details about BYOCNI prerequisites / implications.

``` {#codecell1}
export NAME="$(whoami)-$RANDOM"
export AZURE_RESOURCE_GROUP="${NAME}-group"
az group create --name "${AZURE_RESOURCE_GROUP}" -l westus2

# Create AKS cluster
az aks create \
  --resource-group "${AZURE_RESOURCE_GROUP}" \
  --name "${NAME}" \
  --network-plugin none \
  --generate-ssh-keys

# Get the credentials to access the cluster with kubectl
az aks get-credentials --resource-group "${AZURE_RESOURCE_GROUP}" --name "${NAME}"
```

Copy First Line Copy All

The following commands create a Kubernetes cluster with `eksctl`{.docutils .literal .notranslate} using [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/). See [eksctl Installation](https://github.com/weaveworks/eksctl) for instructions on how to install `eksctl`{.docutils .literal .notranslate} and prepare your account.

``` {#codecell2}
export NAME="$(whoami)-$RANDOM"
cat <<EOF >eks-config.yaml
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: ${NAME}
  region: eu-west-1

managedNodeGroups:
- name: ng-1
  desiredCapacity: 2
  privateNetworking: true
  # taint nodes so that application pods are
  # not scheduled/executed until Cilium is deployed.
  # Alternatively, see the note below.
  taints:
   - key: "node.cilium.io/agent-not-ready"
     value: "true"
     effect: "NoExecute"
EOF
eksctl create cluster -f ./eks-config.yaml
```

Copy First Line Copy All

Note

Please make sure to read and understand the documentation page on [taint effects and unmanaged pods](../../installation/taints/#taint-effects).

Install `kind`{.docutils .literal .notranslate} \>= v0.7.0 per kind documentation: [Installation and Usage](https://kind.sigs.k8s.io/#installation-and-usage)

``` {#codecell3 .literal-block}
curl -LO https://raw.githubusercontent.com/cilium/cilium/1.20.4/Documentation/installation/kind-config.yaml
kind create cluster --config=kind-config.yaml
```

Copy First Line Copy All

Note

Cilium may fail to deploy due to too many open files in one or more of the agent pods. If you notice this error, you can increase the `inotify`{.docutils .literal .notranslate} resource limits on your host machine (see [Pod errors due to "too many open files"](https://kind.sigs.k8s.io/docs/user/known-issues/#pod-errors-due-to-too-many-open-files)).

Install minikube ≥ v1.28.0 as per minikube documentation: [Install Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/). The following command will bring up a single node minikube cluster prepared for installing cilium.

``` {#codecell4}
minikube start --cni=cilium
```

Copy Line

Note

-   This may not install the latest version of cilium.

-   It might be necessary to add `--host-dns-resolver=false`{.docutils .literal .notranslate} if using the Virtualbox provider, otherwise DNS resolution may not work after Cilium installation.

[Kubespray](https://github.com/kubernetes-sigs/kubespray) requires Python ≥ 3.10 for recent versions. For environment setup and dependencies installation, see the [Kubespray Ansible documentation](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/ansible/ansible.md#installing-ansible).

**Configure cluster:**

``` {#codecell5}
# Enter the already cloned kubespray directory
cd kubespray/

# Copy sample inventory
cp -rfp inventory/sample inventory/mycluster

# Configure your inventory
vi inventory/mycluster/inventory.ini

# Configure Kubernetes networking:
# Use CNI without any network plugin
sed -e 's/^kube_network_plugin:.*$/kube_network_plugin: cni/' \
    -e 's/^kube_owner:.*$/kube_owner: root/' \
    inventory/mycluster/group_vars/k8s_cluster/k8s-cluster.yml > k8s-cluster.tmp
mv k8s-cluster.tmp inventory/mycluster/group_vars/k8s_cluster/k8s-cluster.yml
```

Copy First Line Copy All

Setting `kube_network_plugin:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`cni`{.docutils .literal .notranslate} ensures the cluster deploys without any network plugin, allowing Cilium to be installed separately afterward.

**Deploy cluster:**

``` {#codecell6}
ansible-playbook -i inventory/mycluster/inventory.ini cluster.yml -b -v \
  --private-key=~/.ssh/private_key
```

Copy First Line Copy All

(Adjust the path to your private SSH key.)

Note

For more detailed configuration options, refer to the [Kubespray documentation](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/ansible/vars.md).

Install Rancher Desktop \>= v1.1.0 as per Rancher Desktop documentation: [Install Rancher Desktop](https://docs.rancherdesktop.io/getting-started/installation).

Next you need to configure Rancher Desktop to disable the built-in CNI so you can install Cilium.

Configuring Rancher Desktop is done using a YAML configuration file. This step is necessary in order to disable the default CNI and replace it with Cilium.

Next you need to start Rancher Desktop with `containerd`{.docutils .literal .notranslate} and create a [`override.yaml`{.xref .download .docutils .literal .notranslate}](../../_downloads/cf9ee6e71b2988e2ef225c7d156e31ed/rancher-desktop-override.yaml):

``` {#codecell7}
env:
  # needed for cilium
  INSTALL_K3S_EXEC: '--flannel-backend=none --disable-network-policy'
provision:
  # needs root to mount
  - mode: system
    script: |
      #!/bin/sh
      set -e

      # needed for cilium
      mount bpffs -t bpf /sys/fs/bpf
      mount --make-shared /sys/fs/bpf

      mkdir -p /run/cilium/cgroupv2
      mount -t cgroup2 none /run/cilium/cgroupv2
      mount --make-shared /run/cilium/cgroupv2/
```

Copy First Line Copy All

After the file is created move it into your Rancher Desktop's `lima/_config`{.docutils .literal .notranslate} directory:

``` {#codecell8}
cp override.yaml ~/.local/share/rancher-desktop/lima/_config/override.yaml
```

Copy Line

``` {#codecell9}
cp override.yaml ~/Library/Application\ Support/rancher-desktop/lima/_config/override.yaml
```

Copy Line

Finally, open the Rancher Desktop UI and go to the Troubleshooting panel and click "Reset Kubernetes".

After a few minutes Rancher Desktop will start back up prepared for installing Cilium.

Note

This is a beta feature. Please provide feedback and file a GitHub issue if you experience any problems.

Note

The AlibabaCloud ENI integration with Cilium is subject to the following limitations:

-   It is currently only enabled for IPv4.

-   It only works with instances supporting ENI. Refer to [Instance families](https://www.alibabacloud.com/help/doc-detail/25378.htm) for details.

Setup a Kubernetes on AlibabaCloud. You can use any method you prefer. The quickest way is to create an ACK (Alibaba Cloud Container Service for Kubernetes) cluster and to replace the CNI plugin with Cilium. For more details on how to set up an ACK cluster please follow the [official documentation](https://www.alibabacloud.com/help/doc-detail/86745.htm).

## Install the Cilium CLI[](#install-the-cilium-cli "Link to this heading")

Install the latest version of the Cilium CLI. The Cilium CLI can be used to install Cilium, inspect the state of a Cilium installation, and enable/disable various features (e.g. clustermesh, Hubble).

``` {#codecell10}
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
```

Copy First Line Copy All

``` {#codecell11}
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

Video

To learn more about the Cilium CLI, check out [eCHO episode 8: Exploring the Cilium CLI](https://www.youtube.com/watch?v=ndjmaM1i0WQ&t=1136s).

## Install Cilium[](#install-cilium "Link to this heading")

You can install Cilium on any Kubernetes cluster. Pick one of the options below:

These are the generic instructions on how to install Cilium into any Kubernetes cluster. The installer will attempt to automatically pick the best configuration options for you. Please see the other tabs for distribution/platform specific instructions which also list the ideal default configuration for particular platforms.

**Requirements:**

-   Kubernetes must be configured to use CNI (see [Network Plugin Requirements](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/#network-plugin-requirements))

-   Linux kernel \>= 5.10

Tip

See [System Requirements](../../operations/system_requirements/#admin-system-reqs) for more details on the system requirements.

**Install Cilium**

Install Cilium into the Kubernetes cluster pointed to by your current kubectl context:

``` {#codecell12 .literal-block}
cilium install 1.20.4
```

Copy Line

To install Cilium on [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine), perform the following steps:

**Default Configuration:**

  Datapath         IPAM                 Datastore
  ---------------- -------------------- ----------------
  Direct Routing   Kubernetes PodCIDR   Kubernetes CRD

**Requirements:**

-   The cluster should be created with the taint `node.cilium.io/agent-not-ready=true:NoExecute`{.docutils .literal .notranslate} using `--node-taints`{.docutils .literal .notranslate} option. However, there are other options. Please make sure to read and understand the documentation page on [taint effects and unmanaged pods](../../installation/taints/#taint-effects).

**Install Cilium:**

Install Cilium into the GKE cluster:

``` {#codecell13 .literal-block}
cilium install 1.20.4
```

Copy Line

**Configuration:**

  Datapath        IPAM           Datastore
  --------------- -------------- ----------------
  Encapsulation   Cluster Pool   Kubernetes CRD

**Requirements:**

Note

On AKS, Cilium can be installed either manually by administrators via Bring your own CNI or automatically by AKS via Azure CNI Powered by Cilium. Bring your own CNI offers more flexibility and customization as administrators have full control over the installation, but it does not integrate natively with the Azure network stack and administrators need to handle Cilium upgrades. Azure CNI Powered by Cilium integrates natively with the Azure network stack and upgrades are handled by AKS, but it does not offer as much flexibility and customization as it is controlled by AKS. The following instructions assume Bring your own CNI. For Azure CNI Powered by Cilium, see the external installer guide [Installation using Azure CNI Powered by Cilium in AKS](../../installation/k8s-install-aks/#aks-install) for dedicated instructions.

-   The AKS cluster must be created with `--network-plugin`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`none`{.docutils .literal .notranslate}. See the [Bring your own CNI](https://docs.microsoft.com/en-us/azure/aks/use-byo-cni?tabs=azure-cli) documentation for more details about BYOCNI prerequisites / implications.

-   Make sure that you set a cluster pool IPAM pod CIDR that does not overlap with the default service CIDR of AKS. For example, you can use `--helm-set`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ipam.operator.clusterPoolIPv4PodCIDRList=192.168.0.0/16`{.docutils .literal .notranslate}.

**Install Cilium:**

Install Cilium into the AKS cluster:

``` {#codecell14 .literal-block}
cilium install 1.20.4 --set azure.resourceGroup="${AZURE_RESOURCE_GROUP}"
```

Copy Line

To install Cilium on [Amazon Elastic Kubernetes Service (EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html), perform the following steps:

**Default Configuration:**

  Datapath               IPAM      Datastore
  ---------------------- --------- ----------------
  Direct Routing (ENI)   AWS ENI   Kubernetes CRD

For more information on AWS ENI mode, see [AWS ENI](../../network/concepts/ipam/eni/#ipam-eni).

Tip

To chain Cilium on top of the AWS CNI, see [AWS VPC CNI plugin](../../installation/cni-chaining-aws-cni/#chaining-aws-cni).

You can also bring up Cilium in a Single-Region, Multi-Region, or Multi-AZ environment for EKS.

**Requirements:**

-   The [EKS Managed Nodegroups](https://eksctl.io/usage/eks-managed-nodes) must be properly tainted to ensure applications pods are properly managed by Cilium:

    -   `managedNodeGroups`{.docutils .literal .notranslate} should be tainted with `node.cilium.io/agent-not-ready=true:NoExecute`{.docutils .literal .notranslate} to ensure application pods will only be scheduled once Cilium is ready to manage them. However, there are other options. Please make sure to read and understand the documentation page on [taint effects and unmanaged pods](../../installation/taints/#taint-effects).

        Below is an example on how to use [ClusterConfig](https://eksctl.io/usage/creating-and-managing-clusters/#using-config-files) file to create the cluster:

        ``` {#codecell15}
        apiVersion: eksctl.io/v1alpha5
        kind: ClusterConfig
        # ...
        managedNodeGroups:
        - name: ng-1
          # ...
          #
          # taint nodes so that application pods are
          # not scheduled/executed until Cilium is deployed.
          # Alternatively, see the note above regarding taint effects.
          taints:
           - key: "node.cilium.io/agent-not-ready"
             value: "true"
             effect: "NoExecute"
        ```

        Copy First Line Copy All

**Limitations:**

-   The AWS ENI integration of Cilium is currently only enabled for IPv4. If you want to use IPv6, use a datapath/IPAM mode other than ENI.

**Install Cilium:**

Install Cilium into the EKS cluster.

``` {#codecell16 .literal-block}
cilium install 1.20.4
cilium status --wait
```

Copy First Line Copy All

Note

If you have to uninstall Cilium and later install it again, that could cause connectivity issues due to `aws-node`{.docutils .literal .notranslate} DaemonSet flushing Linux routing tables. The issues can be fixed by restarting all pods, alternatively to avoid such issues you can delete `aws-node`{.docutils .literal .notranslate} DaemonSet prior to installing Cilium.

To install Cilium on [OpenShift](https://www.openshift.com/), perform the following steps:

**Default Configuration:**

  Datapath        IPAM           Datastore
  --------------- -------------- ----------------
  Encapsulation   Cluster Pool   Kubernetes CRD

**Requirements:**

-   OpenShift 4.x

**Install Cilium:**

Cilium is a [Certified OpenShift CNI Plugin](https://access.redhat.com/articles/5436171) and is best installed when an OpenShift cluster is created using the OpenShift installer. Please refer to [Installation on OpenShift OKD](../../installation/k8s-install-openshift-okd/#k8s-install-openshift-okd) for more information.

To install Cilium top of a **standalone** [Rancher Kubernetes Engine 1 (RKE1)](https://rke.docs.rancher.com/) or [Rancher Kubernetes Engine 2 (RKE2)](https://docs.rke2.io/) cluster, follow the installation instructions provided in the dedicated [Installation using Rancher Kubernetes Engine](../../installation/k8s-install-rke/#rke-install) guide.

If your RKE1/2 cluster is managed by Rancher (**non-standalone**), follow the [Installation using Rancher](../../installation/k8s-install-rancher-existing-nodes/#rancher-managed-rke-clusters) guide instead.

**Install Cilium:**

Install Cilium into your newly created RKE cluster:

``` {#codecell17 .literal-block}
cilium install 1.20.4
```

Copy Line

To install Cilium on [k3s](https://rancher.com/docs/k3s/latest/en/quick-start/), perform the following steps:

**Default Configuration:**

  Datapath        IPAM           Datastore
  --------------- -------------- ----------------
  Encapsulation   Cluster Pool   Kubernetes CRD

**Requirements:**

-   Install your k3s cluster as you normally would but making sure to disable support for the default CNI plugin and the built-in network policy enforcer so you can install Cilium on top:

``` {#codecell18}
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC='--flannel-backend=none --disable-network-policy' sh -
```

Copy Line

-   For the Cilium CLI to access the cluster in successive steps you will need to use the `kubeconfig`{.docutils .literal .notranslate} file stored at `/etc/rancher/k3s/k3s.yaml`{.docutils .literal .notranslate} by setting the `KUBECONFIG`{.docutils .literal .notranslate} environment variable:

``` {#codecell19}
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
```

Copy Line

**Install Cilium:**

Install Cilium into your newly created Kubernetes cluster:

``` {#codecell20 .literal-block}
cilium install 1.20.4
```

Copy Line

You can install Cilium using Helm on Alibaba ACK, refer to [Installation using Helm](../../installation/k8s-install-helm/#k8s-install-helm) for details.

If the installation fails for some reason, run `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} to retrieve the overall status of the Cilium deployment and inspect the logs of whatever pods are failing to be deployed.

Tip

You may be seeing `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`install`{.docutils .literal .notranslate} print something like this:

``` {#codecell21}
♻️  Restarted unmanaged pod kube-system/event-exporter-gke-564fb97f9-rv8hg
♻️  Restarted unmanaged pod kube-system/kube-dns-6465f78586-hlcrz
♻️  Restarted unmanaged pod kube-system/kube-dns-autoscaler-7f89fb6b79-fsmsg
♻️  Restarted unmanaged pod kube-system/l7-default-backend-7fd66b8b88-qqhh5
♻️  Restarted unmanaged pod kube-system/metrics-server-v0.3.6-7b5cdbcbb8-kjl65
♻️  Restarted unmanaged pod kube-system/stackdriver-metadata-agent-cluster-level-6cc964cddf-8n2rt
```

Copy First Line Copy All

This indicates that your cluster was already running some pods before Cilium was deployed and the installer has automatically restarted them to ensure all pods get networking provided by Cilium.

## Validate the Installation[](#validate-the-installation "Link to this heading")

To validate that Cilium has been properly installed, you can run

``` {#codecell22}
$ cilium status --wait
   /¯¯\
/¯¯\__/¯¯\    Cilium:         OK
\__/¯¯\__/    Operator:       OK
/¯¯\__/¯¯\    Hubble:         disabled
\__/¯¯\__/    ClusterMesh:    disabled
   \__/

DaemonSet         cilium             Desired: 2, Ready: 2/2, Available: 2/2
Deployment        cilium-operator    Desired: 2, Ready: 2/2, Available: 2/2
Containers:       cilium-operator    Running: 2
                  cilium             Running: 2
Image versions    cilium             quay.io/cilium/cilium:v1.9.5: 2
                  cilium-operator    quay.io/cilium/operator-generic:v1.9.5: 2
```

Copy First Line Copy Commands Copy All

Run the following command to validate that your cluster has proper network connectivity:

``` {#codecell23}
$ cilium connectivity test
ℹ️  Monitor aggregation detected, will skip some flow validation steps
✨ [k8s-cluster] Creating namespace for connectivity check...
(...)
---------------------------------------------------------------------------------------------------------------------
📋 Test Report
---------------------------------------------------------------------------------------------------------------------
✅ 69/69 tests successful (0 warnings)
```

Copy First Line Copy Commands Copy All

Note

The connectivity test may fail to deploy due to too many open files in one or more of the pods. If you notice this error, you can increase the `inotify`{.docutils .literal .notranslate} resource limits on your host machine (see [Pod errors due to "too many open files"](https://kind.sigs.k8s.io/docs/user/known-issues/#pod-errors-due-to-too-many-open-files)).

Congratulations! You have a fully functional Kubernetes cluster with Cilium. 🎉

## Next Steps[](#next-steps "Link to this heading")

> -   [Setting up Hubble Observability](../../observability/hubble/setup/#hubble-setup)
>
> -   [Inspecting Network Flows with the CLI](../../observability/hubble/hubble-cli/#hubble-cli)
>
> -   [Service Map & Hubble UI](../../observability/hubble/hubble-ui/#hubble-ui)
>
> -   [Identity-Aware and HTTP-Aware Policy Enforcement](../../security/http/#gs-http)
>
> -   [Setting up Cluster Mesh](../../network/clustermesh/setup/#clustermesh)
