---
{"title": "AKS-to-AKS Clustermesh Preparation", "url": "https://docs.cilium.io/en/stable/network/clustermesh/aks-clustermesh-prep/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# AKS-to-AKS Clustermesh Preparation[](#aks-to-aks-clustermesh-preparation "Link to this heading")

This is a step-by-step guide on how to install and prepare AKS (Azure Kubernetes Service) clusters in BYOCNI mode to meet the requirements for the clustermesh feature.

This guide describes how to install two AKS clusters in BYOCNI (Bring Your Own CNI) mode and connect them together via clustermesh. This guide is not applicable for cross-cloud clustermesh since this guide doesn't expose the node IPs outside of the Azure cloud.

Note

BYOCNI requires the `aks-preview`{.docutils .literal .notranslate} CLI extension with version \>= 0.5.55, which itself requires an `az`{.docutils .literal .notranslate} CLI version \>= 2.32.0.

## Install cluster one[](#install-cluster-one "Link to this heading")

1.  Create a resource group for the cluster (or set the environment variables to an existing resource group).

    ``` {#codecell0}
    export NAME="$(whoami)-$RANDOM"
    export AZURE_RESOURCE_GROUP="${NAME}-group"

    #  westus2 can be changed to any available location (`az account list-locations`)
    az group create --name "${AZURE_RESOURCE_GROUP}" -l westus2
    ```

    Copy First Line Copy All

2.  Create a VNet (virtual network). Creating a custom VNet is required to ensure that the Node, Pod, and Service CIDRs are unique and they don't overlap with other clusters.

    Note

    The example below uses range `192.168.10.0/24`{.docutils .literal .notranslate} range, but you could use any range except for `169.254.0.0/16`{.docutils .literal .notranslate}, `172.30.0.0/16`{.docutils .literal .notranslate}, `172.31.0.0/16`{.docutils .literal .notranslate}, or `192.0.2.0/24`{.docutils .literal .notranslate} which are [reserved by Azure](https://docs.microsoft.com/en-us/azure/aks/configure-azure-cni#prerequisites).

    ``` {#codecell1}
    az network vnet create \
        --resource-group "${AZURE_RESOURCE_GROUP}" \
        --name "${NAME}-cluster-net" \
        --address-prefixes 192.168.10.0/24 \
        --subnet-name "${NAME}-node-subnet" \
        --subnet-prefix 192.168.10.0/24

    # Store the ID of the created subnet
    export NODE_SUBNET_ID=$(az network vnet subnet show \
        --resource-group "${AZURE_RESOURCE_GROUP}" \
        --vnet-name "${NAME}-cluster-net" \
        --name "${NAME}-node-subnet" \
        --query id \
        -o tsv)
    ```

    Copy First Line Copy All

3.  You now have a virtual network and a subnet with the same CIDR. Create an AKS cluster without a CNI and request to use a custom VNet and subnet.

    During creation request to use `"10.10.0.0/16"`{.docutils .literal .notranslate} as the pod CIDR and `"10.11.0.0/16"`{.docutils .literal .notranslate} as the services CIDR. These can be changed to any range except for Azure reserved ranges and ranges used by other clusters you intend to add to the clustermesh.

    ``` {#codecell2}
    az aks create \
        --resource-group "${AZURE_RESOURCE_GROUP}" \
        --name "${NAME}" \
        --network-plugin none \
        --pod-cidr "10.10.0.0/16" \
        --service-cidr "10.11.0.0/16" \
        --dns-service-ip "10.11.0.10" \
        --vnet-subnet-id "${NODE_SUBNET_ID}"

    # Get kubectl credentials, the command will merge the new credentials
    # with the existing ~/.kube/config
    az aks get-credentials \
        --resource-group "${AZURE_RESOURCE_GROUP}" \
        --name "${NAME}"
    ```

    Copy First Line Copy All

4.  Install Cilium, it is important to give the cluster a unique cluster ID and to tell Cilium to use our custom pod CIDR.

    ``` {#codecell3 .literal-block}
    cilium install 1.20.4 \
        --set azure.resourceGroup="${AZURE_RESOURCE_GROUP}" \
        --set cluster.id=1 \
        --set ipam.operator.clusterPoolIPv4PodCIDRList='{10.10.0.0/16}'
    ```

    Copy First Line Copy All

5.  Check the status of Cilium.

    ``` {#codecell4}
    cilium status
    ```

    Copy Line

6.  Before configuring cluster two, store the name of the current cluster.

    ``` {#codecell5}
    export CLUSTER1=${NAME}
    ```

    Copy Line

## Install cluster two[](#install-cluster-two "Link to this heading")

Installing the second cluster uses the same commands but with slightly different arguments.

1.  Create a new resource group.

    ``` {#codecell6}
    export NAME="$(whoami)-$RANDOM"
    export AZURE_RESOURCE_GROUP="${NAME}-group"

    # eastus2 can be changed to any available location (`az account list-locations`)
    az group create --name "${AZURE_RESOURCE_GROUP}" -l eastus2
    ```

    Copy First Line Copy All

2.  Create a VNet in this resource group. Make sure to use a non-overlapping prefix.

    Note

    The example below uses range `192.168.20.0/24`{.docutils .literal .notranslate}, but you could use any range except for `169.254.0.0/16`{.docutils .literal .notranslate}, `172.30.0.0/16`{.docutils .literal .notranslate}, `172.31.0.0/16`{.docutils .literal .notranslate}, or `192.0.2.0/24`{.docutils .literal .notranslate} which are [reserved by Azure](https://docs.microsoft.com/en-us/azure/aks/configure-azure-cni#prerequisites).

    ``` {#codecell7}
    az network vnet create \
        --resource-group "${AZURE_RESOURCE_GROUP}" \
        --name "${NAME}-cluster-net" \
        --address-prefixes 192.168.20.0/24 \
        --subnet-name "${NAME}-node-subnet" \
        --subnet-prefix 192.168.20.0/24

    # Store the ID of the created subnet
    export NODE_SUBNET_ID=$(az network vnet subnet show \
        --resource-group "${AZURE_RESOURCE_GROUP}" \
        --vnet-name "${NAME}-cluster-net" \
        --name "${NAME}-node-subnet" \
        --query id \
        -o tsv)
    ```

    Copy First Line Copy All

3.  Create an AKS cluster without CNI and request to use your custom VNet and subnet.

    During creation use `"10.20.0.0/16"`{.docutils .literal .notranslate} as the pod CIDR and `"10.21.0.0/16"`{.docutils .literal .notranslate} as the services CIDR. These can be changed to any range except for Azure reserved ranges and ranges used by other clusters you intend to add to the clustermesh.

    ``` {#codecell8}
    az aks create \
        --resource-group "${AZURE_RESOURCE_GROUP}" \
        --name "${NAME}" \
        --network-plugin none \
        --pod-cidr "10.20.0.0/16" \
        --service-cidr "10.21.0.0/16" \
        --dns-service-ip "10.21.0.10" \
        --vnet-subnet-id "${NODE_SUBNET_ID}"

    # Get kubectl credentials and add them to ~/.kube/config
    az aks get-credentials \
        --resource-group "${AZURE_RESOURCE_GROUP}" \
        --name "${NAME}"
    ```

    Copy First Line Copy All

4.  Install Cilium, it is important to give the cluster a unique cluster ID and to tell Cilium to use your custom pod CIDR.

    ``` {#codecell9 .literal-block}
    cilium install 1.20.4 \
        --set azure.resourceGroup="${AZURE_RESOURCE_GROUP}" \
        --set cluster.id=2 \
        --set ipam.operator.clusterPoolIPv4PodCIDRList='{10.20.0.0/16}'
    ```

    Copy First Line Copy All

5.  Check the status of Cilium.

    ``` {#codecell10}
    cilium status
    ```

    Copy Line

6.  Before configuring peering and clustermesh, store the current cluster name.

    ``` {#codecell11}
    export CLUSTER2=${NAME}
    ```

    Copy Line

## Peering virtual networks[](#peering-virtual-networks "Link to this heading")

Virtual networks can't connect to each other by default. You can enable cross VNet communication by creating bi-directional "peering".

Create a peering from cluster one to cluster two using the following commands.

``` {#codecell12}
export VNET_ID=$(az network vnet show \
    --resource-group "${CLUSTER2}-group" \
    --name "${CLUSTER2}-cluster-net" \
    --query id -o tsv)

az network vnet peering create \
    -g "${CLUSTER1}-group" \
    --name "peering-${CLUSTER1}-to-${CLUSTER2}" \
    --vnet-name "${CLUSTER1}-cluster-net" \
    --remote-vnet "${VNET_ID}" \
    --allow-vnet-access
```

Copy First Line Copy All

This allows outbound traffic from cluster one to cluster two. To allow bi-directional traffic, add a peering to the other direction as well.

``` {#codecell13}
export VNET_ID=$(az network vnet show \
    --resource-group "${CLUSTER1}-group" \
    --name "${CLUSTER1}-cluster-net" \
    --query id -o tsv)

az network vnet peering create \
    -g "${CLUSTER2}-group" \
    --name "peering-${CLUSTER2}-to-${CLUSTER1}" \
    --vnet-name "${CLUSTER2}-cluster-net" \
    --remote-vnet "${VNET_ID}" \
    --allow-vnet-access
```

Copy First Line Copy All

Node-to-node traffic between clusters is now possible. All requirements for clustermesh are met. Enabling clustermesh is explained in [Setting up Cluster Mesh](../setup/#gs-clustermesh).
