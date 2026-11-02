---
{"title": "Configuring and managing high availability clusters", "guide": "configuring_and_managing_high_availability_clusters", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_managing_high_availability_clusters/index", "retrieved": "2026-11-02", "license": "CC-BY-SA-3.0"}
---

Streamline your workflow with the new MCP server for Red Hat product documentation.Connect your AI tools and LLMs directly to live Red Hat product documentation. [Connect now](https://docs.redhat.com/en/documentation/mcp_server_for_red_hat_documentation/current%20).

# Configuring and managing high availability clusters {#configuring-and-managing-high-availability-clusters .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Using the Red Hat High Availability Add-On to create and maintain Pacemaker clusters {#using-the-red-hat-high-availability-add-on-to-create-and-maintain-pacemaker-clusters .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140572713346336)

**Abstract**

The Red Hat High Availability Add-On configures high availability clusters that use the Pacemaker cluster resource manager. This title provides procedures to familiarize you with Pacemaker cluster configuration as well as example procedures for configuring active/passive clusters.

------------------------------------------------------------------------

## [Providing feedback on Red Hat documentation](#providing-feedback-on-red-hat-documentation) {#providing-feedback-on-red-hat-documentation .title}

We are committed to providing high-quality documentation and value your feedback. To help us improve, you can submit suggestions or report errors through the Red Hat Jira tracking system.

**Procedure**

1.  Log in to the [Jira](https://redhat.atlassian.net/jira/software/c/projects/RHELDOCS/issues/) website.

    If you do not have an account, select the option to create one.

2.  Click **Create** in the top navigation bar.

3.  Enter a descriptive title in the **Summary** field.

4.  Enter your suggestion for improvement in the **Description** field. Include links to the relevant parts of the documentation.

5.  Click **Create** at the bottom of the window.

## [Chapter 1. High Availability Add-On overview](#overview-of-high-availability) {#chapter-1.-high-availability-add-on-overview .title}

The High Availability Add-On is a clustered system that provides reliability, scalability, and availability to critical production services.

High availability clusters, sometimes called failover clusters, provide highly available services by eliminating single points of failure and by failing over services from one cluster node to another in case a node becomes inoperative. Typically, services in a high availability cluster read and write data by means of read-write mounted file systems. A high availability cluster must maintain data integrity as one cluster node takes over control of a service from another cluster node. Node failures in a high availability cluster are not visible from clients outside the cluster. The High Availability Add-On provides high availability clustering through its high availability service management component, Pacemaker.

Pacemaker is the cluster resource manager for the High Availability Add-On. It achieves maximum availability for your cluster services and resources by making use of the cluster infrastructure's messaging and membership capabilities to deter and recover from node and resource-level failure.

### [1.1. Pacemaker architecture components](#pacemaker_architecture_components) {#pacemaker-architecture-components .title}

A cluster configured with Pacemaker comprises separate component daemons that monitor cluster membership, scripts that manage the services, and resource management subsystems that monitor the disparate resources.

The following components form the Pacemaker architecture:

Cluster Information Base (CIB)
:   The Pacemaker information daemon, which uses XML internally to distribute and synchronize current configuration and status information from the Designated Coordinator (DC) - a node assigned by Pacemaker to store and distribute cluster state and actions by means of the CIB - to all other cluster nodes.

Cluster Resource Management Daemon (CRMd)

:   Pacemaker cluster resource actions are routed through this daemon. Resources managed by CRMd can be queried by client systems, moved, instantiated, and changed when needed.

    Each cluster node also includes a local resource manager daemon (LRMd) that acts as an interface between CRMd and resources. LRMd passes commands from CRMd to agents, such as starting and stopping and relaying status information.

Shoot the Other Node in the Head (STONITH)
:   STONITH is the Pacemaker fencing implementation. It acts as a cluster resource in Pacemaker that processes fence requests, forcefully shutting down nodes and removing them from the cluster to ensure data integrity. STONITH is configured in the CIB and can be monitored as a normal cluster resource.

corosync

:   `corosync`{.literal} is the component and daemon of the same name that serves the core membership and member-communication needs for high availability clusters. It is required for the High Availability Add-On to function.

    In addition to those membership and messaging functions, `corosync`{.literal} also:

    -   Manages quorum rules and determination.
    -   Provides messaging capabilities for applications that coordinate or operate across multiple members of the cluster and thus must communicate stateful or other information between instances.
    -   Uses the `kronosnet`{.literal} library as its network transport to provide multiple redundant links and automatic failover.

### [1.2. Pacemaker configuration and management tools](#pacemaker_configuration_and_management_tools) {#pacemaker-configuration-and-management-tools .title}

The High Availability Add-On features three configuration tools for cluster deployment, monitoring, and management.

`pcs`{.literal} command-line interface

:   The `pcs`{.literal} command-line interface controls and configures Pacemaker and the `corosync`{.literal} heartbeat daemon. A command-line based program, `pcs`{.literal .command} can perform the following cluster management tasks:

    -   Create and configure a Pacemaker cluster
    -   Modify configuration of the cluster while it is running
    -   Start, stop, and display status information of the cluster

HA Cluster Management RHEL web console add-on
:   The HA Cluster Management RHEL web console add-on is a graphical user interface to create and configure Pacemaker clusters. The HA Cluster Management RHEL web console add-on is available through the RHEL web console when the `cockpit-ha-cluster`{.literal} package is installed.

`ha_cluster`{.literal} RHEL system role
:   With the `ha_cluster`{.literal} RHEL system role, you can configure and manage a high-availability cluster that uses the Pacemaker high availability cluster resource manager.

### [1.3. The cluster and Pacemaker configuration files](#the_cluster_and_pacemaker_configuration_files) {#the-cluster-and-pacemaker-configuration-files .title}

The configuration files for the Red Hat High Availability Add-On are `corosync.conf`{.literal} and `cib.xml`{.literal}.

-   The `corosync.conf`{.literal} file provides the cluster parameters used by `corosync`{.literal}, the cluster manager that Pacemaker is built on. In general, you should not edit the `corosync.conf`{.literal} directly but, instead, use the `pcs`{.literal} interface, the HA Cluster Management RHEL web console add-on, or the `ha_cluster`{.literal} RHEL system role.
-   The `cib.xml`{.literal} file is an XML file that represents both the cluster's configuration and the current state of all resources in the cluster. This file is used by Pacemaker's Cluster Information Base (CIB). The contents of the CIB are automatically kept in sync across the entire cluster. Do not edit the `cib.xml`{.literal} file directly; use the `pcs`{.literal} interface, the HA Cluster Management RHEL web console add-on, or the `ha_cluster`{.literal} RHEL system role.

**Additional resources**

-   [Red Hat High Availability Add-On Documentation Guide](https://access.redhat.com/articles/6565761)
-   [Getting started with the HA Cluster Management add-on for the RHEL web console](#getting-started-with-ha-cluster-for-web-console "Chapter 2. Getting started with the HA Cluster Management add-on for the RHEL web console")
-   [Automating system administration by using RHEL system roles](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/index)

## [Chapter 2. Getting started with the HA Cluster Management add-on for the RHEL web console](#getting-started-with-ha-cluster-for-web-console) {#chapter-2.-getting-started-with-the-ha-cluster-management-add-on-for-the-rhel-web-console .title}

The HA Cluster Management RHEL web console add-on is a graphical user interface to create and configure Pacemaker clusters. The HA Cluster Management RHEL web console add-on is available through the RHEL web console when the `cockpit-ha-cluster`{.literal} package is installed.

Note

Previous releases of Red Hat Enterprise Linux used the `pcsd`{.literal} Web UI as the standalone graphical user interface for HA cluster configuration. This interface has been modified to be usable as a RHEL web console add-on and is no longer operated as a standalone interface.

### [2.1. Installing and enabling the HA Cluster Management add-on for the RHEL web console](#installing-ha-cluster-for-web-console) {#installing-and-enabling-the-ha-cluster-management-add-on-for-the-rhel-web-console .title}

To use the HA Cluster Management add-on to configure a high availability cluster, add the HA Cluster Management application to the RHEL web console and install and enable the necessary Red Hat High Availability Add-On software packages and services on each node in your cluster.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

**Procedure**

1.  From the system on which you are running the RHEL web console, log in to the console and install the HA Cluster Management add-on application. See [Add-on applications for the RHEL web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/installing-web-console-add-ons-and-creating-custom-pages#add-ons-for-the-rhel-web-console) in the \"Managing systems in the RHEL web console\" document for details.

2.  On each cluster node, install the Red Hat High Availability fence agents from the High Availability channel.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install fence-agents-all
    ```

    You can install only the fence agent that you require with the following command.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install fence-agents-model
    ```

3.  On each cluster node, ensure that the `pcsd`{.literal} service is running.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status pcsd.service
    ```

    If the `pcsd`{.literal} service is not running on a cluster node, enter the following command to start the `pcsd`{.literal} service and to enable it at system start.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now pcsd.service
    ```

4.  Ensure you are logged in to the RHEL web console. To use the RHEL web console to create clusters, the user account used to sign in to the web console must have sudo access to the system.

    Note

    The `hacluster`{.literal} user account is the Pacemaker service account and you cannot use this account to log in to the RHEL web console.

5.  In the RHEL web console, switch to administrative access mode. For information about administrative access mode, see [Administrative access in the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#administrative-access-in-the-web-console) in the \"Managing systems in the RHEL web console\" document.

    Note

    Only a user with sudo access can create clusters and add nodes to existing ones. After you create a cluster, by default, users in the `haclient`{.literal} group can manage the cluster and change permissions. For information about granting different permissions to any other users and groups that require them, or for modifying the default `haclient`{.literal} permissions, see [Granting HA Cluster Management permissions](#granting-ha-cluster-management-permissions "2.2. Granting HA Cluster Management permissions").

### [2.2. Granting HA Cluster Management permissions](#granting-ha-cluster-management-permissions) {#granting-ha-cluster-management-permissions .title}

Each cluster can have a different set of permissions used for its administration. A user with administrative access or full permissions can grant full permissions to other users and groups for the HA Cluster Management web console add-on.

The following table summarizes the cluster management permissions you can grant for the HA Cluster Management web console add-on.

+-----------------+----------------------------------------------------------------------------------------------------------------+
| Permission      | Allowed administrative task                                                                                    |
+:================+:===============================================================================================================+
| Read            | Viewing cluster settings.                                                                                      |
+-----------------+----------------------------------------------------------------------------------------------------------------+
| Write           | Modifying all cluster settings except permissions and ACLs. Does not allow adding nodes and creating clusters. |
+-----------------+----------------------------------------------------------------------------------------------------------------+
| Grant           | Modifying ACLs and granting read, write, and grant permissions.                                                |
+-----------------+----------------------------------------------------------------------------------------------------------------+
| Full            | Performing all cluster management except adding nodes or creating clusters.                                    |
+-----------------+----------------------------------------------------------------------------------------------------------------+

Show more

**Prerequisites**

-   You have installed and enabled the HA Cluster Management add-on for the RHEL web console, as described in [Installing and enabling the HA Cluster Management add-on for the RHEL web console](#installing-ha-cluster-for-web-console "2.1. Installing and enabling the HA Cluster Management add-on for the RHEL web console").
-   You have created a cluster for which you want to manage permissions and it has been added to the cluster list in the HA Cluster Management add-on.

**Procedure**

1.  Log in to the RHEL web console with an account that has sudo access to the system and ensure that you are in administrative access mode. For information about administrative access mode, see [Administrative access in the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#administrative-access-in-the-web-console) in the \"Managing systems in the RHEL web console\" document.

    Alternatively, log into the RHEL web console with an account that has grant permissions for the cluster you want to manage. The account must be a member of the `haclient`{.literal} group to see the HA Cluster Management web console add-on in limited access mode.

2.  Select a cluster for which you want to manage permissions from the cluster list.

3.  In the cluster detail, click the **Permissions** tab on the top of the page and select **Create Permission**.

4.  Add, remove, or edit the permissions for a user or group.

5.  By default, any user with an account that is a member of the `haclient`{.literal} group has read, write and grant permissions. From the **Permissions** page you can remove this permission if you have administrative access in the web console or if you have grant permissions.

## [Chapter 3. Creating a Red Hat High-Availability cluster with Pacemaker](#creating-high-availability-cluster) {#chapter-3.-creating-a-red-hat-high-availability-cluster-with-pacemaker .title}

To create a Red Hat High Availability two-node cluster use the `pcs`{.literal} command-line interface.

### [3.1. Prerequisites](#prerequisites) {#prerequisites .title}

-   2 RHEL nodes, which will be used to create the cluster. In this example, the nodes used are `z1.example.com`{.literal} and `z2.example.com`{.literal}.
-   Network switches for the private network. We recommend but do not require a private network for communication among the cluster nodes and other cluster hardware such as network power switches and Fibre Channel switches.
-   A fencing device for each node of the cluster. This example uses two ports of the APC power switch with a host name of `zapc.example.com`{.literal}.

### [3.2. Installing cluster software](#installing-cluster-software) {#installing-cluster-software .title}

Install the cluster software and configure your system for cluster creation.

**Procedure**

1.  On each node in the cluster, enable the repository for high availability that corresponds to your system architecture. For example, to enable the high availability repository for an x86_64 system, you can enter the following `subscription-manager`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --enable=rhel-10-for-x86_64-highavailability-rpms
    ```

2.  On each node in the cluster, install the Red Hat High Availability Add-On software packages along with all available fence agents from the High Availability channel.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pcs pacemaker fence-agents-all
    ```

    Alternatively, you can install the Red Hat High Availability Add-On software packages along with only the fence agent that you require with the following command.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pcs pacemaker fence-agents-model
    ```

    The following command displays a list of the available fence agents.

    ``` {.language-plaintext tabindex="-1"}
    # rpm -q -a | grep fence
    ```

    ``` {.language-plaintext tabindex="-1"}
    fence-agents-rhevm-4.0.2-3.el7.x86_64
    fence-agents-ilo-mp-4.0.2-3.el7.x86_64
    fence-agents-ipmilan-4.0.2-3.el7.x86_64
    ...
    ```

    Warning

    After you install the Red Hat High Availability Add-On packages, you should ensure that your software update preferences are set so that nothing is installed automatically. Installation on a running cluster can cause unexpected behaviors. For more information, see the Red Hat Knowledgebase article [Recommended Practices for Applying Software Updates to a RHEL High Availability or Resilient Storage Cluster](https://access.redhat.com/articles/2059253/).

3.  If you are running the `firewalld`{.literal .command} daemon, run the following commands to enable the ports that are required by the Red Hat High Availability Add-On.

    Note

    You can determine whether the `firewalld`{.literal .command} daemon is installed on your system with the `rpm -q firewalld`{.literal .command} command. If it is installed, you can determine whether it is running with the `firewall-cmd --state`{.literal .command} command.

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=high-availability
    # firewall-cmd --add-service=high-availability
    ```

    Note

    The ideal firewall configuration for cluster components depends on the local environment, where you may need to take into account such considerations as whether the nodes have multiple network interfaces or whether off-host firewalling is present. The example here, which opens the ports that are generally required by a Pacemaker cluster, should be modified to suit local conditions. [Enabling ports for the High Availability Add-On](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_managing_high_availability_clusters/index#enabling-ports-for-high-availability) shows the ports to enable for the Red Hat High Availability Add-On and provides an explanation for what each port is used for.

4.  In order to use `pcs`{.literal} to configure the cluster and communicate among the nodes, you must set a password on each node for the user ID `hacluster`{.literal}, which is the `pcs`{.literal} administration account. It is recommended that the password for user `hacluster`{.literal} be the same on each node.

    ``` {.language-plaintext tabindex="-1"}
    # passwd hacluster
    ```

    ``` {.language-plaintext tabindex="-1"}
    Changing password for user hacluster.
    New password:
    Retype new password:
    passwd: all authentication tokens updated successfully.
    ```

5.  Before the cluster can be configured, the `pcsd`{.literal .command} daemon must be started and enabled to start up on boot on each node. This daemon works with the `pcs`{.literal .command} command to manage configuration across the nodes in the cluster.

    On each node in the cluster, run the following commands to start the `pcsd`{.literal} service and to enable `pcsd`{.literal} at system start.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start pcsd.service
    # systemctl enable pcsd.service
    ```

### [3.3. Installing the pcp-zeroconf package (recommended)](#installing-pcp-zeroconf) {#installing-the-pcp-zeroconf-package-recommended .title}

Install the `pcp-zeroconf`{.literal} package to configure Performance Co-Pilot (PCP). PCP collects performance data essential for troubleshooting fencing, resource failures, and cluster disruptions.

Note

Cluster deployments where PCP is enabled will need sufficient space available for PCP's captured data on the file system that contains `/var/log/pcp/`{.literal}. Typical space usage by PCP varies across deployments, but 10Gb is usually sufficient when using the `pcp-zeroconf`{.literal} default settings, and some environments may require less. Monitoring usage in this directory over a 14-day period of typical activity can provide a more accurate usage expectation.

**Procedure**

-   To install the `pcp-zeroconf`{.literal} package, run the following command:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pcp-zeroconf
    ```

    This package enables `pmcd`{.literal} and configures data capture at a 10-second interval.

**Additional resources**

-   [Why did a RHEL High Availability cluster node reboot - and how can I prevent it from happening again?](https://access.redhat.com/solutions/4545111)

### [3.4. Creating a high availability cluster](#creating-a-high-availability-cluster) {#creating-a-high-availability-cluster .title}

You can create a Red Hat High Availability Add-On cluster. This example uses nodes `z1.example.com`{.literal} and `z2.example.com`{.literal}.

**Prerequisites**

-   You have created [a Red Hat account](https://www.redhat.com/wapps/ugc/register.html).

    Note

    To display the parameters of a `pcs`{.literal} command and a description of those parameters, use the `-h`{.literal} option of the `pcs`{.literal} command.

**Procedure**

1.  Authenticate the `pcs`{.literal} user `hacluster`{.literal} for each node in the cluster on the node from which you will be running `pcs`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs host auth z1.example.com z2.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    Username: hacluster
    Password:
    z1.example.com: Authorized
    z2.example.com: Authorized
    ```

    This command authenticates user `hacluster`{.literal} on `z1.example.com`{.literal} for both of the nodes in a two-node cluster that will consist of `z1.example.com`{.literal} and `z2.example.com`{.literal}.

2.  Run the following command from the `z1.example.com`{.literal} node to create the two-node cluster `my_cluster`{.literal} that consists of nodes `z1.example.com`{.literal} and `z2.example.com`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs cluster setup my_cluster --start z1.example.com z2.example.com
    ```

    This will propagate the cluster configuration files to both nodes in the cluster. This command includes the `--start`{.literal} option, which will start the cluster services on both nodes in the cluster.

3.  Enable the cluster services to run on each node in the cluster when the node boots:

    Note

    For your particular environment, you can skip this step by keeping the cluster services disabled. If enabled and a node goes down, any issues with your cluster or your resources are resolved before the node rejoins the cluster. If you keep the cluster services disabled, manually start the services when you reboot a node by running the `pcs cluster start`{.literal} command on that node.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs cluster enable --all
    ```

**Verification**

-   Display the status of the cluster you created:

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs cluster status
    ```

    ``` {.language-plaintext tabindex="-1"}
    Cluster Status:
     Stack: corosync
     Current DC: z2.example.com (version 2.0.0-10.el8-b67d8d0de9) - partition with quorum
     Last updated: Thu Oct 11 16:11:18 2018
     Last change: Thu Oct 11 16:11:00 2018 by hacluster via crmd on z2.example.com
     2 Nodes configured
     0 Resources configured
    ...
    ```

    There could be a slight delay before the cluster is up and running when you start the cluster services with the `--start`{.literal} option of the `pcs cluster setup`{.literal} command. Ensure that the cluster is up and running before performing any subsequent actions.

**Additional resources**

-   [How to set up a Pacemaker cluster for high availability Linux](https://www.redhat.com/en/blog/rhel-pacemaker-cluster)

### [3.5. Creating a high availability cluster with multiple links](#configuring-multiple-ip-cluster) {#creating-a-high-availability-cluster-with-multiple-links .title}

You create a Red Hat High Availability cluster with multiple links by specifying all of the links for each node with the `pcs cluster setup`{.literal} command.

The format for the basic command to create a two-node cluster with two links is as follows.

``` {.language-plaintext tabindex="-1"}
# pcs cluster setup pass:quotes[cluster_name] pass:quotes[node1_name] addr=pass:quotes[node1_link0_address] addr=pass:quotes[node1_link1_address] pass:quotes[node2_name] addr=pass:quotes[node2_link0_address] addr=pass:quotes[node2_link1_address]
```

For the full syntax of this command, see the `pcs`{.literal}(8) man page on your system.

When creating a cluster with multiple links, you take the following caveats into account.

-   The order of the `addr=`{.literal}*`address`{.literal}* parameters is important. The first address specified after a node name is for `link0`{.literal}, the second one for `link1`{.literal}, and so forth.
-   By default, if `link_priority`{.literal} is not specified for a link, the link's priority is equal to the link number. The link priorities are then 0, 1, 2, 3, and so forth, according to the order specified, with 0 being the highest link priority.
-   The default link mode is `passive`{.literal}, meaning the active link with the lowest-numbered link priority is used.
-   With the default values of `link_mode`{.literal} and `link_priority`{.literal}, the first link specified will be used as the highest priority link, and if that link fails the next link specified will be used.
-   It is possible to specify up to eight links using the `knet`{.literal} transport protocol, which is the default transport protocol.
-   All nodes must have the same number of `addr=`{.literal} parameters.
-   It is possible to add, remove, and change links in an existing cluster using the `pcs cluster link add`{.literal}, the `pcs cluster link remove`{.literal}, the `pcs cluster link delete`{.literal}, and the `pcs cluster link update`{.literal} commands.
-   As with single-link clusters, do not mix IPv4 and IPv6 addresses in one link, although you can have one link running IPv4 and the other running IPv6.
-   As with single-link clusters, you can specify addresses as IP addresses or as names as long as the names resolve to IPv4 or IPv6 addresses for which IPv4 and IPv6 addresses are not mixed in one link.

The following example creates a two-node cluster named `my_twolink_cluster`{.literal} with two nodes, `rh80-node1`{.literal} and `rh80-node2`{.literal}. `rh80-node1`{.literal} has two interfaces, IP address 192.168.122.201 as `link0`{.literal} and 192.168.123.201 as `link1`{.literal}. `rh80-node2`{.literal} has two interfaces, IP address 192.168.122.202 as `link0`{.literal} and 192.168.123.202 as `link1`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs cluster setup my_twolink_cluster rh80-node1 addr=192.168.122.201 addr=192.168.123.201 rh80-node2 addr=192.168.122.202 addr=192.168.123.202
```

To set a link priority to a different value than the default value, which is the link number, you can set the link priority with the `link_priority`{.literal} option of the `pcs cluster setup`{.literal} command. Each of the following two example commands creates a two-node cluster with two interfaces where the first link, link 0, has a link priority of 1 and the second link, link 1, has a link priority of 0. Link 1 will be used first and link 0 will serve as the failover link. Since link mode is not specified, it defaults to passive.

These two commands are equivalent. If you do not specify a link number following the `link`{.literal} keyword, the `pcs`{.literal} interface automatically adds a link number, starting with the lowest unused link number.

``` {.language-plaintext tabindex="-1"}
# pcs cluster setup my_twolink_cluster rh80-node1 addr=192.168.122.201 addr=192.168.123.201 rh80-node2 addr=192.168.122.202 addr=192.168.123.202 transport knet link link_priority=1 link link_priority=0

# pcs cluster setup my_twolink_cluster rh80-node1 addr=192.168.122.201 addr=192.168.123.201 rh80-node2 addr=192.168.122.202 addr=192.168.123.202 transport knet link linknumber=1 link_priority=0 link link_priority=1
```

**Additional resources**

-   [Adding a node to a cluster with multiple links](#add-nodes-to-multiple-ip-cluster "20.5. Adding a node to a cluster with multiple links")
-   [Adding and modifying links in an existing cluster](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_managing_high_availability_clusters/index#adding-and-modifying-links-in-an-existing-cluster)

### [3.6. Configuring fencing](#configure-fencing) {#configuring-fencing .title}

You must configure a fencing device for each node in the cluster. For information about the fence configuration commands and options, see [Configuring fencing in a Red Hat High Availability cluster](#configuring-fencing "Chapter 9. Configuring fencing in a Red Hat High Availability cluster").

For general information about fencing and its importance in a Red Hat High Availability cluster, see the Red Hat Knowledgebase solution [Fencing in a Red Hat High Availability Cluster](https://access.redhat.com/solutions/15575).

Note

When configuring a fencing device, attention should be given to whether that device shares power with any nodes or devices in the cluster. If a node and its fence device do share power, then the cluster may be at risk of being unable to fence that node if the power to it and its fence device should be lost. Such a cluster should either have redundant power supplies for fence devices and nodes, or redundant fence devices that do not share power. Alternative methods of fencing such as SBD or storage fencing may also bring redundancy in the event of isolated power losses.

This example fence configuration procedure uses the APC power switch with a host name of `zapc.example.com`{.literal} to fence the nodes, and it uses the `fence_apc_snmp`{.literal} fencing agent. Because both nodes will be fenced by the same fencing agent, you can configure both fencing devices as a single resource, using the `pcmk_host_map`{.literal} option.

You create a fencing device by configuring the device as a `stonith`{.literal} resource with the `pcs stonith create`{.literal} command. The following command configures a `stonith`{.literal} resource named `myapc`{.literal} that uses the `fence_apc_snmp`{.literal} fencing agent for nodes `z1.example.com`{.literal} and `z2.example.com`{.literal}. The `pcmk_host_map`{.literal} option maps `z1.example.com`{.literal} to port 1, and `z2.example.com`{.literal} to port 2. The login value and password for the APC device are both `apc`{.literal}. By default, this device will use a monitor interval of sixty seconds for each node.

**Procedure**

1.  Create the fencing device. Note that you can use an IP address when specifying the host name for the nodes.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs stonith create myapc fence_apc_snmp ipaddr="zapc.example.com" pcmk_host_map="z1.example.com:1;z2.example.com:2" login="apc" passwd="apc"
    ```

2.  Display the parameters of the fence device you created.

    ``` {.language-plaintext tabindex="-1"}
    [root@rh7-1 ~]# pcs stonith config myapc
    ```

    ``` {.language-plaintext tabindex="-1"}
     Resource: myapc (class=stonith type=fence_apc_snmp)
      Attributes: ipaddr=zapc.example.com pcmk_host_map=z1.example.com:1;z2.example.com:2 login=apc passwd=apc
      Operations: monitor interval=60s (myapc-monitor-interval-60s)
    ```

    After configuring your fence device, you should test the device. For information about testing a fence device, see [Testing a fence device](#testing-fence-devices "9.5. Testing a fence device").

    Note

    Do not test your fence device by disabling the network interface, as this will not properly test fencing.

    Note

    Once fencing is configured and a cluster has been started, a network restart will trigger fencing for the node which restarts the network even when the timeout is not exceeded. For this reason, do not restart the network service while the cluster service is running because it will trigger unintentional fencing on the node.

### [3.7. Backing up and restoring a cluster configuration](#cluster-backup) {#backing-up-and-restoring-a-cluster-configuration .title}

You can back up a cluster configuration in a tar archive and restore the cluster configuration files on all nodes from the backup.

**Procedure**

-   Use the following command to back up the cluster configuration in a tar archive. If you do not specify a file name, the standard output will be used.

    ``` {.language-plaintext tabindex="-1"}
    # pcs config backup filename
    ```

    Note

    The `pcs config backup`{.literal} command backs up only the cluster configuration itself as configured in the CIB; the configuration of resource daemons is out of the scope of this command. For example if you have configured an Apache resource in the cluster, the resource settings (which are in the CIB) will be backed up, while the Apache daemon settings (as set in\`/etc/httpd\`) and the files it serves will not be backed up. Similarly, if there is a database resource configured in the cluster, the database itself will not be backed up, while the database resource configuration (CIB) will be.

-   Use the following command to restore the cluster configuration files on all cluster nodes from the backup. Specifying the `--local`{.literal} option restores the cluster configuration files only on the node from which you run this command. If you do not specify a file name, the standard input will be used.

    ``` {.language-plaintext tabindex="-1"}
    # pcs config restore [--local] [filename]
    ```

### [3.8. Enabling ports for the High Availability Add-On](#enabling-ports-for-high-availability) {#enabling-ports-for-the-high-availability-add-on .title}

The ideal firewall configuration for cluster components depends on the local environment, where you need to take into account such considerations as whether the nodes have multiple network interfaces or whether off-host firewalling is present.

**Procedure**

-   If you are running the `firewalld`{.literal} daemon, run the following commands to enable the ports that are required by the Red Hat High Availability Add-On:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=high-availability
    # firewall-cmd --add-service=high-availability
    ```

    You may need to modify which ports are open to suit local conditions.

    Note

    You can determine whether the `firewalld`{.literal .command} daemon is installed on your system with the `rpm -q firewalld`{.literal .command} command. If the `firewalld`{.literal .command} daemon is installed, you can determine whether it is running with the `firewall-cmd --state`{.literal .command} command.

    The following table shows the ports to enable for the Red Hat High Availability Add-On and provides an explanation for what the port is used for.

    +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Port                              | When Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    +:==================================+:======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
    | TCP 2224                          | Default `pcsd`{.literal} port required on all nodes for node-to-node communication). You can configure the `pcsd`{.literal} port by means of the `PCSD_PORT`{.literal} parameter in the `/etc/sysconfig/pcsd`{.literal} file.                                                                                                                                                                                                                                                                                                                                                                                                         |
    |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    |                                   | It is crucial to open port 2224 in such a way that `pcs`{.literal .command} from any node can talk to all nodes in the cluster, including itself. When using the Booth cluster ticket manager or a quorum device you must open port 2224 on all related hosts, such as Booth arbitrators or the quorum device host.                                                                                                                                                                                                                                                                                                                   |
    +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | TCP 3121                          | Required on all nodes if the cluster has any Pacemaker Remote nodes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
    |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    |                                   | Pacemaker's `pacemaker-based`{.literal} daemon on the full cluster nodes will contact the `pacemaker_remoted`{.literal} daemon on Pacemaker Remote nodes at port 3121. If a separate interface is used for cluster communication, the port only needs to be open on that interface. At a minimum, the port should open on Pacemaker Remote nodes to full cluster nodes. Because users may convert a host between a full node and a remote node, or run a remote node inside a container using the host's network, it can be useful to open the port to all nodes. It is not necessary to open the port to any hosts other than nodes. |
    +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | TCP 5403                          | Required on the quorum device host when using a quorum device with `corosync-qnetd`{.literal}. The default value can be changed with the `-p`{.literal} option of the `corosync-qnetd`{.literal} command.                                                                                                                                                                                                                                                                                                                                                                                                                             |
    +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | UDP 5404-5412                     | Required on corosync nodes to facilitate communication between nodes. It is crucial to open ports 5404-5412 in such a way that `corosync`{.literal} from any node can talk to all nodes in the cluster, including itself.                                                                                                                                                                                                                                                                                                                                                                                                             |
    +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | TCP 21064                         | Required on all nodes if the cluster contains any resources requiring DLM (such as `GFS2`{.literal}).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | TCP 9929, UDP 9929                | Required to be open on all cluster nodes and Booth arbitrator nodes to connections from any of those same nodes when the Booth ticket manager is used to establish a multi-site cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
    +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    : Table 3.1. Ports to enable for High Availability Add-On

    Show more

### [3.9. Configuring a Red Hat High Availability cluster with IBM z/VM instances as cluster members](#ibmz) {#configuring-a-red-hat-high-availability-cluster-with-ibm-zvm-instances-as-cluster-members .title}

Red Hat provides several articles that may be useful when designing, configuring, and administering a Red Hat High Availability cluster running on z/VM virtual machines.

-   [Design Guidance for RHEL High Availability Clusters - IBM z/VM Instances as Cluster Members](https://access.redhat.com/articles/1543363)
-   [Administrative Procedures for RHEL High Availability Clusters - Configuring z/VM SMAPI Fencing with fence_zvmip for RHEL 7 or 8 IBM z Systems Cluster Members](https://access.redhat.com/articles/3331981)
-   [RHEL High Availability cluster nodes on IBM z Systems experience STONITH-device timeouts around midnight on a nightly basis](https://access.redhat.com/solutions/3555071) (Red Hat Knowledgebase)
-   [Administrative Procedures for RHEL High Availability Clusters - Preparing a dasd Storage Device for Use by a Cluster of IBM z Systems Members](https://access.redhat.com/articles/3332491)

You may also find the following articles useful when designing a Red Hat High Availability cluster in general.

-   [Support Policies for RHEL High Availability Clusters](https://access.redhat.com/articles/2912891)
-   [Exploring Concepts of RHEL High Availability Clusters - Fencing/STONITH](https://access.redhat.com/articles/3099541)

### [3.10. Additional resources](#creating-high-availability-cluster_310-additional-resources) {#additional-resources .title}

-   [Support Policies for RHEL High Availability Clusters](https://access.redhat.com/articles/2912891/)

## [Chapter 4. Configuring an active/passive Apache HTTP server in a Red Hat High Availability cluster](#configuring-active-passive-http-server-in-a-cluster) {#chapter-4.-configuring-an-activepassive-apache-http-server-in-a-red-hat-high-availability-cluster .title}

Clients access an active/passive Apache HTTP server through a floating IP address. The web server runs on one of two cluster nodes. If the active node becomes inoperative, the web server restarts on the second node with minimal service interruption.

The following illustration shows a high-level overview of the cluster in which the cluster is a two-node Red Hat High Availability cluster which is configured with a network power switch and with shared storage. The cluster nodes are connected to a public network, for client access to the Apache HTTP server through a virtual IP. The Apache server runs on either Node 1 or Node 2, each of which has access to the storage on which the Apache data is kept.

In this illustration, the web server is running on Node 1 while Node 2 is available to run the server if Node 1 becomes inoperative.

**Figure 4.1. Apache in a Red Hat High Availability Two-Node Cluster**

This use case requires that your system include the following components:

-   A two-node Red Hat High Availability cluster with power fencing configured for each node. You should use a private network.
-   A public virtual IP address, required for Apache.
-   Shared storage for the nodes in the cluster, using iSCSI, Fibre Channel, or other shared network block device.

The cluster is configured with an Apache resource group, which contains the cluster components that the web server requires: an LVM resource, a file system resource, an IP address resource, and a web server resource. This resource group can fail over from one node of the cluster to the other, allowing either node to run the web server. Before creating the resource group for this cluster, you will be performing the following procedures:

1.  Configure an XFS file system on the logical volume `my_lv`{.literal}.
2.  Configure a web server.

After performing these steps, you create the resource group and the resources it contains.

### [4.1. Configuring an LVM volume with an XFS file system in a Pacemaker cluster](#configuring-lvm-volume-with-ext4-file-system_httpinacluster) {#configuring-an-lvm-volume-with-an-xfs-file-system-in-a-pacemaker-cluster .title}

You can create an LVM logical volume on storage that is shared between the nodes of the cluster.

Note

LVM volumes and the corresponding partitions and devices used by cluster nodes must be connected to the cluster nodes only.

The following procedure creates an LVM logical volume and then creates an XFS file system on that volume for use in a Pacemaker cluster. In this example, the shared partition `/dev/sdb1`{.literal} is used to store the LVM physical volume from which the LVM logical volume will be created.

**Procedure**

1.  On both nodes of the cluster, perform the following steps to set the value for the LVM system ID to the value of the `uname`{.literal} identifier for the system. The LVM system ID will be used to ensure that only the cluster is capable of activating the volume group.

    a.  Set the `system_id_source`{.literal} configuration option in the `/etc/lvm/lvm.conf`{.literal} configuration file to `uname`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        # Configuration option global/system_id_source.
        system_id_source = "uname"
        ```

    b.  Verify that the LVM system ID on the node matches the `uname`{.literal} for the node.

        ``` {.language-plaintext tabindex="-1"}
        # lvm systemid
        ```

        ``` {.language-plaintext tabindex="-1"}
          system ID: z1.example.com
        ```

        ``` {.language-plaintext tabindex="-1"}
        # uname -n
        ```

        ``` {.language-plaintext tabindex="-1"}
          z1.example.com
        ```

2.  Create the LVM volume and create an XFS file system on that volume. Since the `/dev/sdb1`{.literal} partition is storage that is shared, you perform this part of the procedure on one node only.

    a.  Create an LVM physical volume on partition `/dev/sdb1`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        [root@z1 ~]# pvcreate /dev/sdb1
        ```

        ``` {.language-plaintext tabindex="-1"}
          Physical volume "/dev/sdb1" successfully created
        ```

    b.  Create the volume group `my_vg`{.literal} that consists of the physical volume `/dev/sdb1`{.literal}.

        Specify the `--setautoactivation n`{.literal} flag to ensure that volume groups managed by Pacemaker in a cluster will not be automatically activated on startup. If you are using an existing volume group for the LVM volume you are creating, you can reset this flag with the `vgchange --setautoactivation n`{.literal} command for the volume group.

        ``` {.language-plaintext tabindex="-1"}
        [root@z1 ~]# vgcreate --setautoactivation n my_vg /dev/sdb1
        ```

        ``` {.language-plaintext tabindex="-1"}
          Volume group "my_vg" successfully created
        ```

        Note

        If your LVM volume group contains one or more physical volumes that reside on remote block storage, such as an iSCSI target, Red Hat recommends that you ensure that the service starts before Pacemaker starts. For information about configuring startup order for a remote physical volume used by a Pacemaker cluster, see [Configuring startup order for resource dependencies not managed by Pacemaker](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_managing_high_availability_clusters/index#configuring-nonpacemaker-dependencies).

    c.  Verify that the new volume group has the system ID of the node on which you are running and from which you created the volume group.

        ``` {.language-plaintext tabindex="-1"}
        [root@z1 ~]# vgs -o+systemid
        ```

        ``` {.language-plaintext tabindex="-1"}
          VG    #PV #LV #SN Attr   VSize  VFree  System ID
          my_vg   1   0   0 wz--n- <1.82t <1.82t z1.example.com
        ```

    d.  Create a logical volume using the volume group `my_vg`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        [root@z1 ~]# lvcreate -L450 -n my_lv my_vg
        ```

        ``` {.language-plaintext tabindex="-1"}
          Rounding up size to full physical extent 452.00 MiB
          Logical volume "my_lv" created
        ```

        You can use the `lvs`{.literal} command to display the logical volume.

        ``` {.language-plaintext tabindex="-1"}
        [root@z1 ~]# lvs
        ```

        ``` {.language-plaintext tabindex="-1"}
          LV      VG      Attr      LSize   Pool Origin Data%  Move Log Copy%  Convert
          my_lv   my_vg   -wi-a---- 452.00m
          ...
        ```

    e.  Create an XFS file system on the logical volume `my_lv`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        [root@z1 ~]# mkfs.xfs /dev/my_vg/my_lv
        ```

        ``` {.language-plaintext tabindex="-1"}
        meta-data=/dev/my_vg/my_lv       isize=512    agcount=4, agsize=28928 blks
                 =                       sectsz=512   attr=2, projid32bit=1
        ...
        ```

3.  If the use of a devices file is enabled with the `use_devicesfile = 1`{.literal} parameter in the `lvm.conf`{.literal} file, add the shared device to the devices file on the second node in the cluster. This feature is enabled by default.

    ``` {.language-plaintext tabindex="-1"}
    [root@z2 ~]# lvmdevices --adddev /dev/sdb1
    ```

### [4.2. Configuring an Apache HTTP Server](#configuring-apache-http-web-server) {#configuring-an-apache-http-server .title}

Install and configure the Apache HTTP Server to function as a cluster resource. You must prepare the web server on all nodes, configure server status monitoring for the resource agent, and place web content on the shared file system.

**Procedure**

1.  Ensure that the Apache HTTP Server is installed on each node in the cluster. You also need the `wget`{.literal} tool installed on the cluster to be able to check the status of the Apache HTTP Server.

    On each node, run the following command.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install -y httpd wget
    ```

    If you are running the `firewalld`{.literal} daemon, on each node in the cluster enable the ports that are required by the Red Hat High Availability Add-On and enable the ports you will require for running `httpd`{.literal}. This example enables the `httpd`{.literal} ports for public access, but the specific ports to enable for `httpd`{.literal} may vary for production use.

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=http
    # firewall-cmd --permanent --zone=public --add-service=http
    # firewall-cmd --reload
    ```

2.  In order for the Apache resource agent to get the status of Apache, on each node in the cluster create the following addition to the existing configuration to enable the status server URL.

    ``` {.language-plaintext tabindex="-1"}
    # cat <<-END > /etc/httpd/conf.d/status.conf
    ```

    ``` {.language-plaintext tabindex="-1"}
    <Location /server-status>
        SetHandler server-status
        Require local
    </Location>
    END
    ```

3.  Create a web page for Apache to serve up.

    On one node in the cluster, ensure that the logical volume you created in [Configuring an LVM volume with an XFS file system in a Pacemaker cluster](#configuring-lvm-volume-with-ext4-file-system_httpinacluster "4.1. Configuring an LVM volume with an XFS file system in a Pacemaker cluster") is activated, mount the file system that you created on that logical volume, create the file `index.html`{.literal} on that file system, and then unmount the file system.

    ``` {.language-plaintext tabindex="-1"}
    # lvchange -ay my_vg/my_lv
    # mount /dev/my_vg/my_lv /var/www/
    # mkdir /var/www/html
    # mkdir /var/www/cgi-bin
    # mkdir /var/www/error
    # restorecon -R /var/www
    # cat <<-END >/var/www/html/index.html
    ```

    ``` {.language-plaintext tabindex="-1"}
    <html>
    <body>Hello</body>
    </html>
    END
    ```

    ``` {.language-plaintext tabindex="-1"}
    # umount /var/www
    ```

### [4.3. Creating the resources and resource groups](#configuring-resources-for-http-server-in-a-cluster) {#creating-the-resources-and-resource-groups .title}

You can create the resources for your cluster with the following procedure. To ensure these resources all run on the same node, they are configured as part of the resource group `apachegroup`{.literal}.

The procedure configures the following resources within the cluster:

1.  An `LVM-activate`{.literal} resource named `my_lvm`{.literal} that uses the LVM volume group created in [Configuring an LVM volume with an XFS file system in a Pacemaker cluster](#configuring-lvm-volume-with-ext4-file-system_httpinacluster "4.1. Configuring an LVM volume with an XFS file system in a Pacemaker cluster").
2.  A `Filesystem`{.literal} resource named `my_fs`{.literal} that uses the `/dev/my_vg/my_lv`{.literal} file system device created in [Configuring an LVM volume with an XFS file system in a Pacemaker cluster](#configuring-lvm-volume-with-ext4-file-system_httpinacluster "4.1. Configuring an LVM volume with an XFS file system in a Pacemaker cluster").
3.  An `IPaddr2`{.literal} resource, which provides a floating IP address for the `apachegroup`{.literal} resource group. The IP address must not be associated with a physical node. If the NIC device for the `IPaddr2`{.literal} resource is not specified, the floating IP address must reside on the same network as one of the node's statically assigned IP addresses; otherwise, the NIC device cannot be detected.
4.  An `apache`{.literal} resource named `Website`{.literal} that uses the `index.html`{.literal} file and Apache configuration defined in [Configuring an Apache HTTP server](#configuring-apache-http-web-server "4.2. Configuring an Apache HTTP Server").

The following procedure creates the `apachegroup`{.literal} resource group and its contained resources. Resources start in the order they are added to the group and stop in reverse order. Run this procedure from a single cluster node.

**Procedure**

1.  The following command creates the `LVM-activate`{.literal} resource `my_lvm`{.literal}. Because the resource group `apachegroup`{.literal} does not yet exist, this command creates the resource group.

    Note

    Do not configure more than one `LVM-activate`{.literal} resource that uses the same LVM volume group in an active/passive HA configuration, as this could cause data corruption. Additionally, do not configure an `LVM-activate`{.literal} resource as a clone resource in an active/passive HA configuration.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs resource create my_lvm ocf:heartbeat:LVM-activate vgname=my_vg vg_access_mode=system_id --group apachegroup
    ```

    When you create a resource, the resource is started automatically. You can use the following command to confirm that the resource was created and has started.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource status
    ```

    ``` {.language-plaintext tabindex="-1"}
     Resource Group: apachegroup
         my_lvm (ocf::heartbeat:LVM-activate):  Started
    ```

    You can manually stop and start an individual resource with the `pcs resource disable`{.literal} and `pcs resource enable`{.literal} commands.

2.  The following commands create the remaining resources for the configuration, adding them to the existing resource group `apachegroup`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs resource create my_fs Filesystem device="/dev/my_vg/my_lv" directory="/var/www" fstype="xfs" --group apachegroup

    [root@z1 ~]# pcs resource create VirtualIP IPaddr2 ip=198.51.100.3 cidr_netmask=24 --group apachegroup

    [root@z1 ~]# pcs resource create Website apache configfile="/etc/httpd/conf/httpd.conf" statusurl="http://127.0.0.1/server-status" --group apachegroup
    ```

3.  After creating the resources and the resource group that contains them, you can check the status of the cluster. Note that all four resources are running on the same node.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs status
    ```

    ``` {.language-plaintext tabindex="-1"}
    Cluster name: my_cluster
    Last updated: Wed Jul 31 16:38:51 2013
    Last change: Wed Jul 31 16:42:14 2013 via crm_attribute on z1.example.com
    Stack: corosync
    Current DC: z2.example.com (2) - partition with quorum
    Version: 1.1.10-5.el7-9abe687
    2 Nodes configured
    6 Resources configured

    Online: [ z1.example.com z2.example.com ]

    Full list of resources:
     myapc  (stonith:fence_apc_snmp):   Started z1.example.com
     Resource Group: apachegroup
         my_lvm (ocf::heartbeat:LVM-activate):  Started z1.example.com
         my_fs  (ocf::heartbeat:Filesystem):    Started z1.example.com
         VirtualIP  (ocf::heartbeat:IPaddr2):   Started z1.example.com
         Website    (ocf::heartbeat:apache):    Started z1.example.com
    ```

    Note that if you have not configured a fencing device for your cluster, by default the resources do not start.

4.  Once the cluster is up and running, you can point a browser to the IP address you defined as the `IPaddr2`{.literal} resource to view the sample display, consisting of the simple word \"Hello\".

    ``` {.language-plaintext tabindex="-1"}
    Hello
    ```

    If you find that the resources you configured are not running, you can run the `pcs resource debug-start `{.literal}*`resource`{.literal}* command to test the resource configuration.

5.  When you use the `apache`{.literal} resource agent to manage Apache, it does not use `systemd`{.literal}. Because of this, you must edit the `logrotate`{.literal} script supplied with Apache so that it does not use `systemctl`{.literal} to reload Apache.

    Remove the following line in the `/etc/logrotate.d/httpd`{.literal} file on each node in the cluster.

    ``` {.language-plaintext tabindex="-1"}
    /bin/systemctl reload httpd.service > /dev/null 2>/dev/null || true
    ```

    Replace the line you removed with the following three lines, specifying `/var/run/httpd-`{.literal}*`website`{.literal}*`.pid`{.literal} as the PID file path where *website* is the name of the Apache resource. In this example, the Apache resource name is `Website`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    /usr/bin/test -f /var/run/httpd-Website.pid >/dev/null 2>/dev/null &&
    /usr/bin/ps -q $(/usr/bin/cat /var/run/httpd-Website.pid) >/dev/null 2>/dev/null &&
    /usr/sbin/httpd -f /etc/httpd/conf/httpd.conf -c "PidFile /var/run/httpd-Website.pid" -k graceful > /dev/null 2>/dev/null || true
    ```

### [4.4. Testing the resource configuration](#testing-resource-configuration-in-a-cluster) {#testing-the-resource-configuration .title}

Verify the high availability configuration by simulating a manual failover. By placing the active node into standby mode, you force the cluster to migrate resources to a backup node, confirming that services remain available during a node outage.

In the example configuration, all resources are currently active on `z1.example.com`{.literal}. To test the failover logic, put `z1`{.literal} into `standby`{.literal} mode. This prevents the node from hosting resources and triggers the cluster to relocate the resource group to `z2.example.com`{.literal}.

**Procedure**

1.  The following command puts node `z1.example.com`{.literal} in `standby`{.literal} mode.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs node standby z1.example.com
    ```

2.  After putting node `z1`{.literal} in `standby`{.literal} mode, check the cluster status. Note that the resources should now all be running on `z2`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs status
    ```

    ``` {.language-plaintext tabindex="-1"}
    Cluster name: my_cluster
    Last updated: Wed Jul 31 17:16:17 2013
    Last change: Wed Jul 31 17:18:34 2013 via crm_attribute on z1.example.com
    Stack: corosync
    Current DC: z2.example.com (2) - partition with quorum
    Version: 1.1.10-5.el7-9abe687
    2 Nodes configured
    6 Resources configured

    Node z1.example.com (1): standby
    Online: [ z2.example.com ]

    Full list of resources:

     myapc  (stonith:fence_apc_snmp):   Started z1.example.com
     Resource Group: apachegroup
         my_lvm (ocf::heartbeat:LVM-activate):  Started z2.example.com
         my_fs  (ocf::heartbeat:Filesystem):    Started z2.example.com
         VirtualIP  (ocf::heartbeat:IPaddr2):   Started z2.example.com
         Website    (ocf::heartbeat:apache):    Started z2.example.com
    ```

    The web site at the defined IP address should still display, without interruption.

3.  To remove `z1`{.literal} from `standby`{.literal} mode, enter the following command.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs node unstandby z1.example.com
    ```

    Note

    Removing a node from `standby`{.literal} mode does not in itself cause the resources to fail back over to that node. This will depend on the `resource-stickiness`{.literal} value for the resources. For information about the `resource-stickiness`{.literal} meta attribute, see [Configuring a resource to prefer its current node](#setting-resource-stickiness "12.4. Configuring a resource to prefer its current node").

## [Chapter 5. Configuring an active/passive NFS server in a Red Hat High Availability cluster](#configuring-active-passive-nfs-server-in-a-cluster) {#chapter-5.-configuring-an-activepassive-nfs-server-in-a-red-hat-high-availability-cluster .title}

The Red Hat High Availability Add-On supports active/passive NFS on RHEL clusters using shared storage. Clients connect by a floating IP. If the active node fails, the service fails over to the other node with minimal interruption.

This use case requires that your system include the following components:

-   A two-node Red Hat High Availability cluster with power fencing configured for each node. You should use a private network.
-   A public virtual IP address, required for the NFS server.
-   Shared storage for the nodes in the cluster, using iSCSI, Fibre Channel, or other shared network block device.

Configuring a highly available active/passive NFS server on an existing two-node Red Hat Enterprise Linux High Availability cluster requires that you perform the following steps:

1.  Configure a file system on an LVM logical volume on the shared storage for the nodes in the cluster.
2.  Configure an NFS share on the shared storage on the LVM logical volume.
3.  Create the cluster resources.
4.  Test the NFS server you have configured.

### [5.1. Configuring an LVM volume with an XFS file system in a Pacemaker cluster](#configuring-lvm-volume-with-ext4-file-system_nfsinacluster) {#configuring-an-lvm-volume-with-an-xfs-file-system-in-a-pacemaker-cluster-1 .title}

You can create an LVM logical volume on storage that is shared between the nodes of the cluster.

Note

LVM volumes and the corresponding partitions and devices used by cluster nodes must be connected to the cluster nodes only.

The following procedure creates an LVM logical volume and then creates an XFS file system on that volume for use in a Pacemaker cluster. In this example, the shared partition `/dev/sdb1`{.literal} is used to store the LVM physical volume from which the LVM logical volume will be created.

**Procedure**

1.  On both nodes of the cluster, perform the following steps to set the value for the LVM system ID to the value of the `uname`{.literal} identifier for the system. The LVM system ID will be used to ensure that only the cluster is capable of activating the volume group.

    a.  Set the `system_id_source`{.literal} configuration option in the `/etc/lvm/lvm.conf`{.literal} configuration file to `uname`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        # Configuration option global/system_id_source.
        system_id_source = "uname"
        ```

    b.  Verify that the LVM system ID on the node matches the `uname`{.literal} for the node.

        ``` {.language-plaintext tabindex="-1"}
        # lvm systemid
        ```

        ``` {.language-plaintext tabindex="-1"}
          system ID: z1.example.com
        ```

        ``` {.language-plaintext tabindex="-1"}
        # uname -n
        ```

        ``` {.language-plaintext tabindex="-1"}
          z1.example.com
        ```

2.  Create the LVM volume and create an XFS file system on that volume. Since the `/dev/sdb1`{.literal} partition is storage that is shared, you perform this part of the procedure on one node only.

    a.  Create an LVM physical volume on partition `/dev/sdb1`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        [root@z1 ~]# pvcreate /dev/sdb1
        ```

        ``` {.language-plaintext tabindex="-1"}
          Physical volume "/dev/sdb1" successfully created
        ```

    b.  Create the volume group `my_vg`{.literal} that consists of the physical volume `/dev/sdb1`{.literal}.

        Specify the `--setautoactivation n`{.literal} flag to ensure that volume groups managed by Pacemaker in a cluster will not be automatically activated on startup. If you are using an existing volume group for the LVM volume you are creating, you can reset this flag with the `vgchange --setautoactivation n`{.literal} command for the volume group.

        ``` {.language-plaintext tabindex="-1"}
        [root@z1 ~]# vgcreate --setautoactivation n my_vg /dev/sdb1
        ```

        ``` {.language-plaintext tabindex="-1"}
          Volume group "my_vg" successfully created
        ```

        Note

        If your LVM volume group contains one or more physical volumes that reside on remote block storage, such as an iSCSI target, Red Hat recommends that you ensure that the service starts before Pacemaker starts. For information about configuring startup order for a remote physical volume used by a Pacemaker cluster, see [Configuring startup order for resource dependencies not managed by Pacemaker](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_managing_high_availability_clusters/index#configuring-nonpacemaker-dependencies).

    c.  Verify that the new volume group has the system ID of the node on which you are running and from which you created the volume group.

        ``` {.language-plaintext tabindex="-1"}
        [root@z1 ~]# vgs -o+systemid
        ```

        ``` {.language-plaintext tabindex="-1"}
          VG    #PV #LV #SN Attr   VSize  VFree  System ID
          my_vg   1   0   0 wz--n- <1.82t <1.82t z1.example.com
        ```

    d.  Create a logical volume using the volume group `my_vg`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        [root@z1 ~]# lvcreate -L450 -n my_lv my_vg
        ```

        ``` {.language-plaintext tabindex="-1"}
          Rounding up size to full physical extent 452.00 MiB
          Logical volume "my_lv" created
        ```

        You can use the `lvs`{.literal} command to display the logical volume.

        ``` {.language-plaintext tabindex="-1"}
        [root@z1 ~]# lvs
        ```

        ``` {.language-plaintext tabindex="-1"}
          LV      VG      Attr      LSize   Pool Origin Data%  Move Log Copy%  Convert
          my_lv   my_vg   -wi-a---- 452.00m
          ...
        ```

    e.  Create an XFS file system on the logical volume `my_lv`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        [root@z1 ~]# mkfs.xfs /dev/my_vg/my_lv
        ```

        ``` {.language-plaintext tabindex="-1"}
        meta-data=/dev/my_vg/my_lv       isize=512    agcount=4, agsize=28928 blks
                 =                       sectsz=512   attr=2, projid32bit=1
        ...
        ```

3.  If the use of a devices file is enabled with the `use_devicesfile = 1`{.literal} parameter in the `lvm.conf`{.literal} file, add the shared device to the devices file on the second node in the cluster. This feature is enabled by default.

    ``` {.language-plaintext tabindex="-1"}
    [root@z2 ~]# lvmdevices --adddev /dev/sdb1
    ```

### [5.2. Configuring an NFS share](#configuring-nfs-share) {#configuring-an-nfs-share .title}

You can configure an NFS share to support NFS service failover.

**Procedure**

1.  On both nodes in the cluster, create the `/nfsshare`{.literal} directory.

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /nfsshare
    ```

2.  On one node in the cluster, perform the following procedure.

    a.  Ensure that the logical volume you created in [Configuring an LVM volume with an XFS file system in a Pacemaker cluster](#configuring-lvm-volume-with-ext4-file-system_nfsinacluster "5.1. Configuring an LVM volume with an XFS file system in a Pacemaker cluster") is activated, then mount the file system you created on the logical volume on the `/nfsshare`{.literal} directory.

        ``` {.language-plaintext tabindex="-1"}
        [root@z1 ~]# lvchange -ay my_vg/my_lv
        [root@z1 ~]# mount /dev/my_vg/my_lv /nfsshare
        ```

    b.  Create an `exports`{.literal} directory tree on the `/nfsshare`{.literal} directory.

        ``` {.language-plaintext tabindex="-1"}
        [root@z1 ~]# mkdir -p /nfsshare/exports
        [root@z1 ~]# mkdir -p /nfsshare/exports/export1
        [root@z1 ~]# mkdir -p /nfsshare/exports/export2
        ```

    c.  Place files in the `exports`{.literal} directory for the NFS clients to access. For this example, we are creating test files named `clientdatafile1`{.literal} and `clientdatafile2`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        [root@z1 ~]# touch /nfsshare/exports/export1/clientdatafile1
        [root@z1 ~]# touch /nfsshare/exports/export2/clientdatafile2
        ```

    d.  Unmount the file system and deactivate the LVM volume group.

        ``` {.language-plaintext tabindex="-1"}
        [root@z1 ~]# umount /dev/my_vg/my_lv
        [root@z1 ~]# vgchange -an my_vg
        ```

### [5.3. Configuring the resources and resource group for an NFS server in a cluster](#configuring_resources_for_nfs_server_in_a_cluster) {#configuring-the-resources-and-resource-group-for-an-nfs-server-in-a-cluster .title}

You can configure the cluster resources for an NFS server in a cluster.

Note

If you have not configured a fencing device for your cluster, by default the resources do not start.

If you find that the resources you configured are not running, you can run the `pcs resource debug-start `{.literal}*`resource`{.literal}* command to test the resource configuration. This starts the service outside of the cluster's control and knowledge. At the point the configured resources are running again, run `pcs resource cleanup `{.literal}*`resource`{.literal}* to make the cluster aware of the updates.

The following procedure configures the system resources. To ensure these resources all run on the same node, they are configured as part of the resource group `nfsgroup`{.literal}. The resources will start in the order in which you add them to the group, and they will stop in the reverse order in which they are added to the group. Run this procedure from one node of the cluster only.

**Procedure**

1.  Create the LVM-activate resource named `my_lvm`{.literal}. Because the resource group `nfsgroup`{.literal} does not yet exist, this command creates the resource group.

    Warning

    Do not configure more than one `LVM-activate`{.literal} resource that uses the same LVM volume group in an active/passive HA configuration, as this risks data corruption. Additionally, do not configure an `LVM-activate`{.literal} resource as a clone resource in an active/passive HA configuration.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs resource create my_lvm ocf:heartbeat:LVM-activate vgname=my_vg vg_access_mode=system_id --group nfsgroup
    ```

2.  Check the status of the cluster to verify that the resource is running.

    ``` {.language-plaintext tabindex="-1"}
    root@z1 ~]#  pcs status
    ```

    ``` {.language-plaintext tabindex="-1"}
    Cluster name: my_cluster
    Last updated: Thu Jan  8 11:13:17 2015
    Last change: Thu Jan  8 11:13:08 2015
    Stack: corosync
    Current DC: z2.example.com (2) - partition with quorum
    Version: 1.1.12-a14efad
    2 Nodes configured
    3 Resources configured

    Online: [ z1.example.com z2.example.com ]

    Full list of resources:
     myapc  (stonith:fence_apc_snmp):       Started z1.example.com
     Resource Group: nfsgroup
         my_lvm     (ocf::heartbeat:LVM-activate):   Started z1.example.com

    PCSD Status:
      z1.example.com: Online
      z2.example.com: Online

    Daemon Status:
      corosync: active/enabled
      pacemaker: active/enabled
      pcsd: active/enabled
    ```

3.  Configure a `Filesystem`{.literal} resource for the cluster.

    The following command configures an XFS `Filesystem`{.literal} resource named `nfsshare`{.literal} as part of the `nfsgroup`{.literal} resource group. This file system uses the LVM volume group and XFS file system you created in [Configuring an LVM volume with an XFS file system in a cluster](#configuring-lvm-volume-with-ext4-file-system_nfsinacluster "5.1. Configuring an LVM volume with an XFS file system in a Pacemaker cluster") and will be mounted on the `/nfsshare`{.literal} directory you created in [Configuring an NFS share](#configuring-nfs-share "5.2. Configuring an NFS share").

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs resource create nfsshare Filesystem device=/dev/my_vg/my_lv directory=/nfsshare fstype=xfs --group nfsgroup
    ```

    You can specify mount options as part of the resource configuration for a `Filesystem`{.literal} resource with the `options=`{.literal}*`options`{.literal}* parameter. Run the `pcs resource describe Filesystem`{.literal} command for full configuration options.

4.  Verify that the `my_lvm`{.literal} and `nfsshare`{.literal} resources are running.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs status
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    Full list of resources:
     myapc  (stonith:fence_apc_snmp):       Started z1.example.com
     Resource Group: nfsgroup
         my_lvm     (ocf::heartbeat:LVM-activate):   Started z1.example.com
         nfsshare   (ocf::heartbeat:Filesystem):    Started z1.example.com
    ...
    ```

5.  Create the `nfsserver`{.literal} resource named `nfs-daemon`{.literal} as part of the resource group `nfsgroup`{.literal}.

    Note

    The `nfsserver`{.literal} resource allows you to specify an `nfs_shared_infodir`{.literal} parameter, which is a directory that NFS servers use to store NFS-related stateful information.

    It is recommended that this attribute be set to a subdirectory of one of the `Filesystem`{.literal} resources you created in this collection of exports. This ensures that the NFS servers are storing their stateful information on a device that will become available to another node if this resource group needs to relocate. In this example;

    -   `/nfsshare`{.literal} is the shared-storage directory managed by the `Filesystem`{.literal} resource
    -   `/nfsshare/exports/export1`{.literal} and `/nfsshare/exports/export2`{.literal} are the export directories
    -   `/nfsshare/nfsinfo`{.literal} is the shared-information directory for the `nfsserver`{.literal} resource

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs resource create nfs-daemon nfsserver nfs_shared_infodir=/nfsshare/nfsinfo nfs_no_notify=true --group nfsgroup

    [root@z1 ~]# pcs status
    ...
    ```

6.  Add the `exportfs`{.literal} resources to export the `/nfsshare/exports`{.literal} directory. These resources are part of the resource group `nfsgroup`{.literal}. This builds a virtual directory for NFSv4 clients. NFSv3 clients can access these exports as well.

    Note

    The `fsid=0`{.literal} option is required only if you want to create a virtual directory for NFSv4 clients. For more information, see the Red Hat Knowledgebase solution [How do I configure the fsid option in an NFS server's /etc/exports file?](https://access.redhat.com/solutions/548083).

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs resource create nfs-root exportfs clientspec=192.168.122.0/255.255.255.0 options=rw,sync,no_root_squash directory=/nfsshare/exports fsid=0 --group nfsgroup

    [root@z1 ~]# pcs resource create nfs-export1 exportfs clientspec=192.168.122.0/255.255.255.0 options=rw,sync,no_root_squash directory=/nfsshare/exports/export1 fsid=1 --group nfsgroup

    [root@z1 ~]# pcs resource create nfs-export2 exportfs clientspec=192.168.122.0/255.255.255.0 options=rw,sync,no_root_squash directory=/nfsshare/exports/export2 fsid=2 --group nfsgroup
    ```

7.  Add the floating IP address resource that NFS clients will use to access the NFS share. This resource is part of the resource group `nfsgroup`{.literal}. For this example deployment, we are using 192.168.122.200 as the floating IP address.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs resource create nfs_ip IPaddr2 ip=192.168.122.200 cidr_netmask=24 --group nfsgroup
    ```

8.  Add an `nfsnotify`{.literal} resource for sending NFSv3 reboot notifications once the entire NFS deployment has initialized. This resource is part of the resource group `nfsgroup`{.literal}.

    Note

    For the NFS notification to be processed correctly, the floating IP address must have a host name associated with it that is consistent on both the NFS servers and the NFS client.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs resource create nfs-notify nfsnotify source_host=192.168.122.200 --group nfsgroup
    ```

9.  After creating the resources and the resource constraints, you can check the status of the cluster. Note that all resources are running on the same node.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs status
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    Full list of resources:
     myapc  (stonith:fence_apc_snmp):       Started z1.example.com
     Resource Group: nfsgroup
         my_lvm     (ocf::heartbeat:LVM-activate):   Started z1.example.com
         nfsshare   (ocf::heartbeat:Filesystem):    Started z1.example.com
         nfs-daemon (ocf::heartbeat:nfsserver):     Started z1.example.com
         nfs-root   (ocf::heartbeat:exportfs):      Started z1.example.com
         nfs-export1        (ocf::heartbeat:exportfs):      Started z1.example.com
         nfs-export2        (ocf::heartbeat:exportfs):      Started z1.example.com
         nfs_ip     (ocf::heartbeat:IPaddr2):       Started  z1.example.com
         nfs-notify (ocf::heartbeat:nfsnotify):     Started z1.example.com
    ...
    ```

### [5.4. Testing the NFS resource configuration](#testing-nfs-resource-configuration) {#testing-the-nfs-resource-configuration .title}

You can validate your NFS resource configuration in a high availability cluster. You should be able to mount the exported file system with either NFSv3 or NFSv4.

**Testing the NFS export**

1.  If you are running the `firewalld`{.literal} daemon on your cluster nodes, ensure that the ports that your system requires for NFS access are enabled on all nodes.

2.  On a node outside of the cluster, residing in the same network as the deployment, verify that the NFS share can be seen by mounting the NFS share. For this example, we are using the 192.168.122.0/24 network.

    ``` {.language-plaintext tabindex="-1"}
    # showmount -e 192.168.122.200
    ```

    ``` {.language-plaintext tabindex="-1"}
    Export list for 192.168.122.200:
    /nfsshare/exports/export1 192.168.122.0/255.255.255.0
    /nfsshare/exports         192.168.122.0/255.255.255.0
    /nfsshare/exports/export2 192.168.122.0/255.255.255.0
    ```

3.  To verify that you can mount the NFS share with NFSv4, mount the NFS share to a directory on the client node. After mounting, verify that the contents of the export directories are visible. Unmount the share after testing.

    ``` {.language-plaintext tabindex="-1"}
    # mkdir nfsshare
    # mount -o "vers=4" 192.168.122.200:export1 nfsshare
    # ls nfsshare
    ```

    ``` {.language-plaintext tabindex="-1"}
    clientdatafile1
    ```

    ``` {.language-plaintext tabindex="-1"}
    # umount nfsshare
    ```

4.  Verify that you can mount the NFS share with NFSv3. After mounting, verify that the test file `clientdatafile1`{.literal} is visible. Unlike NFSv4, since NFSv3 does not use the virtual file system, you must mount a specific export. Unmount the share after testing.

    ``` {.language-plaintext tabindex="-1"}
    # mkdir nfsshare
    # mount -o "vers=3" 192.168.122.200:/nfsshare/exports/export2 nfsshare
    # ls nfsshare
    ```

    ``` {.language-plaintext tabindex="-1"}
    clientdatafile2
    ```

    ``` {.language-plaintext tabindex="-1"}
    # umount nfsshare
    ```

**Testing for failover**

1.  On a node outside of the cluster, mount the NFS share and verify access to the `clientdatafile1`{.literal} file you created in [Configuring an NFS share](#configuring-nfs-share "5.2. Configuring an NFS share").

    ``` {.language-plaintext tabindex="-1"}
    # mkdir nfsshare
    # mount -o "vers=4" 192.168.122.200:export1 nfsshare
    # ls nfsshare
    ```

    ``` {.language-plaintext tabindex="-1"}
    clientdatafile1
    ```

2.  From a node within the cluster, determine which node in the cluster is running `nfsgroup`{.literal}. In this example, `nfsgroup`{.literal} is running on `z1.example.com`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs status
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    Full list of resources:
     myapc  (stonith:fence_apc_snmp):       Started z1.example.com
     Resource Group: nfsgroup
         my_lvm     (ocf::heartbeat:LVM-activate):   Started z1.example.com
         nfsshare   (ocf::heartbeat:Filesystem):    Started z1.example.com
         nfs-daemon (ocf::heartbeat:nfsserver):     Started z1.example.com
         nfs-root   (ocf::heartbeat:exportfs):      Started z1.example.com
         nfs-export1        (ocf::heartbeat:exportfs):      Started z1.example.com
         nfs-export2        (ocf::heartbeat:exportfs):      Started z1.example.com
         nfs_ip     (ocf::heartbeat:IPaddr2):       Started  z1.example.com
         nfs-notify (ocf::heartbeat:nfsnotify):     Started z1.example.com
    ...
    ```

3.  From a node within the cluster, put the node that is running `nfsgroup`{.literal} in standby mode.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs node standby z1.example.com
    ```

4.  Verify that `nfsgroup`{.literal} successfully starts on the other cluster node.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs status
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    Full list of resources:
     Resource Group: nfsgroup
         my_lvm     (ocf::heartbeat:LVM-activate):   Started z2.example.com
         nfsshare   (ocf::heartbeat:Filesystem):    Started z2.example.com
         nfs-daemon (ocf::heartbeat:nfsserver):     Started z2.example.com
         nfs-root   (ocf::heartbeat:exportfs):      Started z2.example.com
         nfs-export1        (ocf::heartbeat:exportfs):      Started z2.example.com
         nfs-export2        (ocf::heartbeat:exportfs):      Started z2.example.com
         nfs_ip     (ocf::heartbeat:IPaddr2):       Started  z2.example.com
         nfs-notify (ocf::heartbeat:nfsnotify):     Started z2.example.com
    ...
    ```

5.  From the node outside the cluster on which you have mounted the NFS share, verify that this outside node still continues to have access to the test file within the NFS mount.

    ``` {.language-plaintext tabindex="-1"}
    # ls nfsshare
    ```

    ``` {.language-plaintext tabindex="-1"}
    clientdatafile1
    ```

    Service will be lost briefly for the client during the failover but the client should recover it with no user intervention. By default, clients using NFSv4 may take up to 90 seconds to recover the mount; this 90 seconds represents the NFSv4 file lease grace period observed by the server on startup. NFSv3 clients should recover access to the mount in a matter of a few seconds.

6.  From a node within the cluster, remove the node that was initially running `nfsgroup`{.literal} from standby mode.

    Note

    Removing a node from `standby`{.literal} mode does not in itself cause the resources to fail back over to that node. This will depend on the `resource-stickiness`{.literal} value for the resources. For information about the `resource-stickiness`{.literal} meta attribute, see [Configuring a resource to prefer its current node](#setting-resource-stickiness "12.4. Configuring a resource to prefer its current node").

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs node unstandby z1.example.com
    ```

## [Chapter 6. Saving a configuration change to a working file](#configure-testfile) {#chapter-6.-saving-a-configuration-change-to-a-working-file .title}

Save configuration changes to a file to stage updates without affecting the active CIB. You can then define multiple changes without immediately updating the running cluster.

Note

Although you should not edit the cluster configuration file directly, you can view the raw cluster configuration with the `pcs cluster cib`{.literal} command.

The following is the recommended procedure for pushing changes to the CIB file. This procedure creates a copy of the original saved CIB file and makes changes to that copy. When pushing those changes to the active CIB, this procedure specifies the `diff-against`{.literal} option of the `pcs cluster cib-push`{.literal} command so that only the changes between the original file and the updated file are pushed to the CIB. This allows users to make changes in parallel that do not overwrite each other, and it reduces the load on Pacemaker which does not need to parse the entire configuration file.

**Procedure**

1.  Save the active CIB to a file. This example saves the CIB to a file named `original.xml`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster cib original.xml
    ```

2.  Copy the saved file to the working file you will be using for the configuration updates.

    ``` {.language-plaintext tabindex="-1"}
    # cp original.xml updated.xml
    ```

3.  Update your configuration as needed. The following command creates a resource in the file `updated.xml`{.literal} but does not add that resource to the currently running cluster configuration.

    ``` {.language-plaintext tabindex="-1"}
    # pcs -f updated.xml resource create VirtualIP ocf:heartbeat:IPaddr2 ip=192.168.0.120 op monitor interval=30s
    ```

4.  Push the updated file to the active CIB, specifying that you are pushing only the changes you have made to the original file.

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster cib-push updated.xml diff-against=original.xml
    ```

5.  Alternately, you can push the entire current content of a CIB file with the following command.

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster cib-push filename
    ```

6.  When pushing the entire CIB file, Pacemaker checks the version and does not allow you to push a CIB file which is older than the one already in a cluster. If you need to update the entire CIB file with a version that is older than the one currently in the cluster, you can use the `--config`{.literal} option of the `pcs cluster cib-push`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster cib-push --config filename
    ```

## [Chapter 7. Displaying cluster status](#cluster-status) {#chapter-7.-displaying-cluster-status .title}

There are a variety of commands you can use to display the status of a cluster and its components.

**Displaying the full cluster configuration**

Use the following command to display the full current cluster configuration:

``` {.language-plaintext tabindex="-1"}
# pcs config
```

**Displaying status of cluster and cluster resources**

You can display the status of the cluster and the cluster resources with the following command:

``` {.language-plaintext tabindex="-1"}
# pcs status
```

**Displaying status of a cluster component**

You can display the status of a particular cluster component with the *commands* parameter of the `pcs status`{.literal} command, specifying `resources`{.literal}, `cluster`{.literal}, `nodes`{.literal}, or `pcsd`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs status commands
```

For example, the following command displays the status of the cluster resources:

``` {.language-plaintext tabindex="-1"}
# pcs status resources
```

The following command displays the status of the cluster, but not the cluster resources:

``` {.language-plaintext tabindex="-1"}
# pcs cluster status
```

**Delaying status display until actions are completed**

If you run the `pcs status`{.literal} command before Pacemaker has completed any actions required by changes to the CIB, the cluster state at that time might not match the expected status. You can ensure that Pacemaker does not need to take any further actions by running the `pcs status wait`{.literal} command.

The `pcs status wait`{.literal} command waits until the cluster has completed all current actions before returning a value. If any actions unrelated to your recent changes are in progress, the command waits until those are completed. The `pcs status wait`{.literal} command returns a value of 0 as soon as Pacemaker completes pending actions.

You can specify a period of time to wait. If the current actions have not completed after that time period, the command prints an error and returns a value of 1.

The following command waits until Pacemaker has applied configuration changes:

``` {.language-plaintext tabindex="-1"}
# pcs status wait
```

``` {.language-plaintext tabindex="-1"}
Waiting for the cluster to apply configuration changes...
```

The following command waits up to one minute until Pacemaker has applied configuration changes:

``` {.language-plaintext tabindex="-1"}
# pcs status wait 1min
```

``` {.language-plaintext tabindex="-1"}
Waiting for the cluster to apply configuration changes (timeout: 60 seconds)...
```

## [Chapter 8. Modifying, displaying, and exporting the corosync.conf file](#pcs-operation) {#chapter-8.-modifying-displaying-and-exporting-the-corosync.conf-file .title}

To set cluster parameters, `corosync`{.literal} uses the `corosync.conf`{.literal} file. Do not edit `corosync.conf`{.literal} directly. Use the `pcs`{.literal} interface instead.

### [8.1. Modifying the corosync.conf file with the pcs command](#pcs-corosync-manage) {#modifying-the-corosync.conf-file-with-the-pcs-command .title}

Modify `corosync.conf`{.literal} parameters, such as token timeouts and logging levels, using `pcs`{.literal}. `pcs`{.literal} validates input and synchronizes changes across all nodes, ensuring consistency. While some updates apply immediately, modifying core transport settings requires a cluster restart.

**Procedure**

-   The following command modifies the parameters in the `corosync.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster config update [transport pass:quotes[transport options]] [compression pass:quotes[compression options]] [crypto pass:quotes[crypto options]] [totem pass:quotes[totem options]] [--corosync_conf pass:quotes[path]]
    ```

-   The following example command updates the `knet_pmtud_interval`{.literal} transport value and the `token`{.literal} and `join`{.literal} totem values:

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster config update transport knet_pmtud_interval=35 totem token=10000 join=100
    ```

**Additional resources**

-   [Managing cluster nodes](#clusternode-management "Chapter 20. Managing cluster nodes")
-   [Adding and modifying links in an existing cluster](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_managing_high_availability_clusters/index#adding-and-modifying-links-in-an-existing-cluster)
-   [Configuring cluster quorum](#configuring-cluster-quorum "Chapter 27. Configuring cluster quorum")
-   [Configuring quorum devices](#configuring-quorum-devices "Chapter 28. Configuring quorum devices")

### [8.2. Displaying the corosync.conf file with the pcs command](#pcs-corosync-display) {#displaying-the-corosync.conf-file-with-the-pcs-command .title}

Display the contents of the `corosync.conf`{.literal} configuration file to verify cluster settings, network parameters, and quorum configuration.

**Procedure**

-   Display the contents of the `corosync.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster corosync
    ```

    You can print the contents of the `corosync.conf`{.literal} file in a human-readable format with the `pcs cluster config`{.literal} command, as in the following example.

    The output for this command includes the UUID for the cluster if the UUID was added manually as described in [Identifying clusters by UUID](#identifying-cluster-by-uuid "32.9. Identifying clusters by UUID").

    ``` {.language-plaintext tabindex="-1"}
    [root@r8-node-01 ~]# pcs cluster config
    ```

    ``` {.language-plaintext tabindex="-1"}
    Cluster Name: HACluster
    Cluster UUID: ad4ae07dcafe4066b01f1cc9391f54f5
    Transport: knet
    Nodes:
      r8-node-01:
        Link 0 address: r8-node-01
        Link 1 address: 192.168.122.121
        nodeid: 1
      r8-node-02:
        Link 0 address: r8-node-02
        Link 1 address: 192.168.122.122
        nodeid: 2
    Links:
      Link 1:
        linknumber: 1
        ping_interval: 1000
        ping_timeout: 2000
        pong_count: 5
    Compression Options:
      level: 9
      model: zlib
      threshold: 150
    Crypto Options:
      cipher: aes256
      hash: sha256
    Totem Options:
      downcheck: 2000
      join: 50
      token: 10000
    Quorum Device: net
      Options:
        sync_timeout: 2000
        timeout: 3000
      Model Options:
        algorithm: lms
        host: r8-node-03
      Heuristics:
        exec_ping: ping -c 1 127.0.0.1
    ```

### [8.3. Exporting the corosync.conf file](#pcs-corosync-export) {#exporting-the-corosync.conf-file .title}

You can run the `pcs cluster config show`{.literal} command with the `--output-format=cmd`{.literal} option to display the `pcs`{.literal} configuration commands that can be used to recreate the existing `corosync.conf`{.literal} file on a different system.

**Procedure**

-   Export the `corosync.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    [root@r8-node-01 ~]# pcs cluster config show --output-format=cmd
    ```

    ``` {.language-plaintext tabindex="-1"}
    pcs cluster setup HACluster \
      r8-node-01 addr=r8-node-01 addr=192.168.122.121 \
      r8-node-02 addr=r8-node-02 addr=192.168.122.122 \
      transport \
      knet \
        link \
          linknumber=1 \
          ping_interval=1000 \
          ping_timeout=2000 \
          pong_count=5 \
        compression \
          level=9 \
          model=zlib \
          threshold=150 \
        crypto \
          cipher=aes256 \
          hash=sha256 \
      totem \
        downcheck=2000 \
        join=50 \
        token=10000
    ```

## [Chapter 9. Configuring fencing in a Red Hat High Availability cluster](#configuring-fencing) {#chapter-9.-configuring-fencing-in-a-red-hat-high-availability-cluster .title}

When a node becomes unresponsive, the cluster must isolate it to prevent data corruption. Configure fencing since the node cannot be contacted directly. An external fence device cuts off the node's access to shared resources or performs a hard reboot.

Without a fence device, you do not know if the disconnected node has released its resources. This could prevent services from running on other nodes. Conversely, the system might wrongly assume resources are released, leading to data corruption. As a consequence, data integrity cannot be guaranteed and the cluster configuration will be unsupported.

When fencing is in progress, no other cluster operation is allowed to run. Normal operation of the cluster cannot resume until fencing has completed or the cluster node rejoins the cluster after the cluster node has been rebooted.

### [9.1. Displaying available fence agents and their options](#displaying-fence-agents) {#displaying-available-fence-agents-and-their-options .title}

You can view available fencing agents and the available options for specific fencing agents.

Note

Your system's hardware determines the type of fencing device to use for your cluster. For information about supported platforms and architectures and the different fencing devices, see the Red Hat Knowledgebase article [Cluster Platforms and Architectures](https://access.redhat.com/articles/2912891#platforms) section of the article [Support Policies for RHEL High Availability Clusters](https://access.redhat.com/articles/2912891).

Run the following command to list all available fencing agents. When you specify a filter, this command displays only the fencing agents that match the filter.

``` {.language-plaintext tabindex="-1"}
# pcs stonith list [filter]
```

Run the following command to display the options for the specified fencing agent.

``` {.language-plaintext tabindex="-1"}
# pcs stonith describe [stonith_agent]
```

For example, the following command displays the options for the fence agent for APC over telnet/SSH.

``` {.language-plaintext tabindex="-1"}
# pcs stonith describe fence_apc
```

``` {.language-plaintext tabindex="-1"}
Stonith options for: fence_apc
  ipaddr (required): IP Address or Hostname
  login (required): Login Name
  passwd: Login password or passphrase
  passwd_script: Script to retrieve password
  cmd_prompt: Force command prompt
  secure: SSH connection
  port (required): Physical plug number or name of virtual machine
  identity_file: Identity file for ssh
  switch: Physical switch number on device
  inet4_only: Forces agent to use IPv4 addresses only
  inet6_only: Forces agent to use IPv6 addresses only
  ipport: TCP port to use for connection with device
  action (required): Fencing Action
  verbose: Verbose mode
  debug: Write debug information to given file
  version: Display version information and exit
  help: Display help and exit
  separator: Separator for CSV created by operation list
  power_timeout: Test X seconds for status change after ON/OFF
  shell_timeout: Wait X seconds for cmd prompt after issuing command
  login_timeout: Wait X seconds for cmd prompt after login
  power_wait: Wait X seconds after issuing ON/OFF
  delay: Wait X seconds before fencing is started
  retry_on: Count of attempts to retry power on
```

Warning

For fence agents that provide a `method`{.literal} option, with the exception of the `fence_sbd`{.literal} agent a value of `cycle`{.literal} is unsupported and should not be specified, as it may cause data corruption. Even for `fence_sbd`{.literal}, however. you should not specify a method and instead use the default value.

### [9.2. Creating a fence device](#creating-fence-devices) {#creating-a-fence-device .title}

Create a fence device by using the `pcs stonith create`{.literal} command. To view all available creation options, use the `pcs stonith -h`{.literal} command.

**Procedure**

-   Create a fence device:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith create stonith_id stonith_device_type [stonith_device_options] [op operation_action operation_options]
    ```

-   The following command creates a single fencing device for a single node:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith create MyStonith fence_virt pcmk_host_list=f1 op monitor interval=30s
    ```

    Some fence devices can fence only a single node, while other devices can fence multiple nodes. The parameters you specify when you create a fencing device depend on what your fencing device supports and requires.

-   Some fence devices can automatically decide which nodes they can fence.

-   You can use the `pcmk_host_list`{.literal} parameter when creating a fencing device to specify all of the machines that are controlled by that fencing device.

-   Some fence devices require a mapping of host names to the specifications that the fence device understands. You can map host names with the `pcmk_host_map`{.literal} parameter when creating a fencing device.

**Additional resources**

-   [General properties of fencing devices](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_high_availability_clusters/configuring-fencing#general-fence-device-properties)
-   [Testing a fence device](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_high_availability_clusters/configuring-fencing#testing-fence-devices)

### [9.3. General properties of fencing devices](#general-fence-device-properties) {#general-properties-of-fencing-devices .title}

Configure fencing behavior using device-specific options and cluster-wide properties. Device options define agent settings, such as IP addresses, and metadata like delays. Cluster properties manage global logic, including timeouts and the `stonith-enabled`{.literal} parameter.

Any cluster node can fence any other cluster node with any fence device, regardless of whether the fence resource is started or stopped. Whether the resource is started controls only the recurring monitor for the device, not whether it can be used, with the following exceptions:

-   You can disable a fencing device by running the `pcs stonith disable `{.literal .command}*`stonith_id`{.literal .command}* command. This will prevent any node from using that device.
-   To prevent a specific node from using a fencing device, you can configure location constraints for the fencing resource with the `pcs constraint location …​ avoids`{.literal} command.
-   Configuring `stonith-enabled=false`{.literal} will disable fencing altogether. Note, however, that Red Hat does not support clusters when fencing is disabled, as it is not suitable for a production environment.

The following table describes the general properties you can set for fencing devices.

+-----------------------------+--------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                       | Type   | Default                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+:============================+:=======+:=====================================================================================================+:=======================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `pcmk_host_map`{.literal}   | string |                                                                                                      | A mapping of host names to port numbers for devices that do not support host names. For example: `node1:1;node2:2,3`{.literal} tells the cluster to use port 1 for node1 and ports 2 and 3 for node2. The `pcmk_host_map`{.literal} property supports special characters inside `pcmk_host_map`{.literal} values using a backslash in front of the value. For example, you can specify `pcmk_host_map="node3:plug\ 1"`{.literal} to include a space in the host alias. |
+-----------------------------+--------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_host_list`{.literal}  | string |                                                                                                      | A list of machines controlled by this device (Optional unless `pcmk_host_check=static-list`{.literal}).                                                                                                                                                                                                                                                                                                                                                                |
+-----------------------------+--------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_host_check`{.literal} | string | -   `static-list`{.literal} if either `pcmk_host_list`{.literal} or `pcmk_host_map`{.literal} is set | How to determine which machines are controlled by the device. Allowed values: `dynamic-list`{.literal} (query the device), `static-list`{.literal} (check the `pcmk_host_list`{.literal} attribute), none (assume every device can fence every machine)                                                                                                                                                                                                                |
|                             |        | -   Otherwise, `dynamic-list`{.literal} if the fence device supports the `list`{.literal} action     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                             |        | -   Otherwise, `status`{.literal} if the fence device supports the `status`{.literal} action         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                             |        | -   Otherwise, `none`{.literal}.                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+-----------------------------+--------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 9.1. General Properties of Fencing Devices

Show more

The following table summarizes additional properties you can set for fencing devices. Note that these properties are for advanced use only.

+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                            | Type    | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                          |
+:=================================+:========+:========+:=====================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `pcmk_host_argument`{.literal}   | string  | port    | An alternate parameter to supply instead of port. Some devices do not support the standard port parameter or may provide additional ones. Use this to specify an alternate, device-specific parameter that should indicate the machine to be fenced. A value of `none`{.literal} can be used to tell the cluster not to supply any additional parameters.                                                                            |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_reboot_action`{.literal}   | string  | reboot  | An alternate command to run instead of `reboot`{.literal}. Some devices do not support the standard commands or may provide additional ones. Use this to specify an alternate, device-specific, command that implements the reboot action.                                                                                                                                                                                           |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_reboot_timeout`{.literal}  | time    | 60s     | Specify an alternate timeout to use for reboot actions instead of `stonith-timeout`{.literal}. Some devices need much more/less time to complete than normal. Use this to specify an alternate, device-specific, timeout for reboot actions.                                                                                                                                                                                         |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_reboot_retries`{.literal}  | integer | 2       | The maximum number of times to retry the `reboot`{.literal} command within the timeout period. Some devices do not support multiple connections. Operations may fail if the device is busy with another task so Pacemaker will automatically retry the operation, if there is time remaining. Use this option to alter the number of times Pacemaker retries reboot actions before giving up.                                        |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_off_action`{.literal}      | string  | off     | An alternate command to run instead of `off`{.literal}. Some devices do not support the standard commands or may provide additional ones. Use this to specify an alternate, device-specific, command that implements the off action.                                                                                                                                                                                                 |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_off_timeout`{.literal}     | time    | 60s     | Specify an alternate timeout to use for off actions instead of `stonith-timeout`{.literal}. Some devices need much more or much less time to complete than normal. Use this to specify an alternate, device-specific, timeout for off actions.                                                                                                                                                                                       |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_off_retries`{.literal}     | integer | 2       | The maximum number of times to retry the off command within the timeout period. Some devices do not support multiple connections. Operations may fail if the device is busy with another task so Pacemaker will automatically retry the operation, if there is time remaining. Use this option to alter the number of times Pacemaker retries off actions before giving up.                                                          |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_list_action`{.literal}     | string  | list    | An alternate command to run instead of `list`{.literal}. Some devices do not support the standard commands or may provide additional ones. Use this to specify an alternate, device-specific, command that implements the list action.                                                                                                                                                                                               |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_list_timeout`{.literal}    | time    | 60s     | Specify an alternate timeout to use for list actions. Some devices need much more or much less time to complete than normal. Use this to specify an alternate, device-specific, timeout for list actions.                                                                                                                                                                                                                            |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_list_retries`{.literal}    | integer | 2       | The maximum number of times to retry the `list`{.literal} command within the timeout period. Some devices do not support multiple connections. Operations may fail if the device is busy with another task so Pacemaker will automatically retry the operation, if there is time remaining. Use this option to alter the number of times Pacemaker retries list actions before giving up.                                            |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_monitor_action`{.literal}  | string  | monitor | An alternate command to run instead of `monitor`{.literal}. Some devices do not support the standard commands or may provide additional ones. Use this to specify an alternate, device-specific, command that implements the monitor action.                                                                                                                                                                                         |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_monitor_timeout`{.literal} | time    | 60s     | Specify an alternate timeout to use for monitor actions instead of `stonith-timeout`{.literal}. Some devices need much more or much less time to complete than normal. Use this to specify an alternate, device-specific, timeout for monitor actions.                                                                                                                                                                               |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_monitor_retries`{.literal} | integer | 2       | The maximum number of times to retry the `monitor`{.literal} command within the timeout period. Some devices do not support multiple connections. Operations may fail if the device is busy with another task so Pacemaker will automatically retry the operation, if there is time remaining. Use this option to alter the number of times Pacemaker retries monitor actions before giving up.                                      |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_status_action`{.literal}   | string  | status  | An alternate command to run instead of `status`{.literal}. Some devices do not support the standard commands or may provide additional ones. Use this to specify an alternate, device-specific, command that implements the status action.                                                                                                                                                                                           |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_status_timeout`{.literal}  | time    | 60s     | Specify an alternate timeout to use for status actions instead of `stonith-timeout`{.literal}. Some devices need much more or much less time to complete than normal. Use this to specify an alternate, device-specific, timeout for status actions.                                                                                                                                                                                 |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_status_retries`{.literal}  | integer | 2       | The maximum number of times to retry the status command within the timeout period. Some devices do not support multiple connections. Operations may fail if the device is busy with another task so Pacemaker will automatically retry the operation, if there is time remaining. Use this option to alter the number of times Pacemaker retries status actions before giving up.                                                    |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_delay_base`{.literal}      | string  | 0s      | Enables a base delay for fencing actions and specifies a base delay value. You can specify different values for different nodes with the `pcmk_delay_base`{.literal} parameter. For general information about fencing delay parameters and their interactions, see [Fencing delays](#fence-delays "9.4. Fencing delays").                                                                                                            |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_delay_max`{.literal}       | time    | 0s      | Enables a random delay for fencing actions and specifies the maximum delay, which is the maximum value of the combined base delay and random delay. For example, if the base delay is 3 and `pcmk_delay_max`{.literal} is 10, the random delay will be between 3 and 10. For general information about fencing delay parameters and their interactions, see [Fencing delays](#fence-delays "9.4. Fencing delays").                   |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_action_limit`{.literal}    | integer | 1       | The maximum number of actions that can be performed in parallel on this device. The cluster property `concurrent-fencing=true`{.literal} needs to be configured first (this is the default value). A value of -1 is unlimited.                                                                                                                                                                                                       |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_on_action`{.literal}       | string  | on      | For advanced use only: An alternate command to run instead of `on`{.literal}. Some devices do not support the standard commands or may provide additional ones. Use this to specify an alternate, device-specific, command that implements the `on`{.literal} action.                                                                                                                                                                |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_on_timeout`{.literal}      | time    | 60s     | For advanced use only: Specify an alternate timeout to use for `on`{.literal} actions instead of `stonith-timeout`{.literal}. Some devices need much more or much less time to complete than normal. Use this to specify an alternate, device-specific, timeout for `on`{.literal} actions.                                                                                                                                          |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_on_retries`{.literal}      | integer | 2       | For advanced use only: The maximum number of times to retry the `on`{.literal} command within the timeout period. Some devices do not support multiple connections. Operations may `fail`{.literal} if the device is busy with another task so Pacemaker will automatically retry the operation, if there is time remaining. Use this option to alter the number of times Pacemaker retries `on`{.literal} actions before giving up. |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 9.2. Advanced Properties of Fencing Devices

Show more

In addition to the properties you can set for individual fence devices, there are also cluster properties you can set that determine fencing behavior, as described in the following table.

+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option                               | Default           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+:=====================================+:==================+:=================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `stonith-enabled`{.literal}          | true              | Indicates that failed nodes and nodes with resources that cannot be stopped should be fenced. Protecting your data requires that you set this `true`{.literal}.                                                                                                                                                                                                                                                                                  |
|                                      |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                      |                   | If `true`{.literal}, or unset, the cluster will refuse to start resources unless one or more STONITH resources have been configured also.                                                                                                                                                                                                                                                                                                        |
|                                      |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                      |                   | Red Hat only supports clusters with this value set to `true`{.literal}.                                                                                                                                                                                                                                                                                                                                                                          |
+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `stonith-action`{.literal}           | reboot            | Action to send to fencing device. Allowed values: `reboot`{.literal}, `off`{.literal}. The value `poweroff`{.literal} is also allowed, but is only used for legacy devices.                                                                                                                                                                                                                                                                      |
+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `stonith-timeout`{.literal}          | 60s               | How long to wait for a STONITH action to complete.                                                                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `stonith-max-attempts`{.literal}     | 10                | How many times fencing can fail for a target before the cluster will no longer immediately re-attempt it.                                                                                                                                                                                                                                                                                                                                        |
+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `stonith-watchdog-timeout`{.literal} |                   | The maximum time to wait until a node can be assumed to have been killed by the hardware watchdog. It is recommended that this value be set to twice the value of the hardware watchdog timeout. This option is needed only if watchdog-only SBD configuration is used for fencing.                                                                                                                                                              |
+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `concurrent-fencing`{.literal}       | true              | Allow fencing operations to be performed in parallel.                                                                                                                                                                                                                                                                                                                                                                                            |
+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `fence-reaction`{.literal}           | stop              | Determines how a cluster node should react if notified of its own fencing. A cluster node may receive notification of its own fencing if fencing is misconfigured, or if fabric fencing is in use that does not cut cluster communication. Allowed values are `stop`{.literal} to attempt to immediately stop Pacemaker and stay stopped, or `panic`{.literal} to attempt to immediately reboot the local node, falling back to stop on failure. |
|                                      |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                      |                   | Although the default value for this property is `stop`{.literal}, the safest choice for this value is `panic`{.literal}, which attempts to immediately reboot the local node. If you prefer the stop behavior, as is most likely to be the case in conjunction with fabric fencing, it is recommended that you set this explicitly.                                                                                                              |
+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `priority-fencing-delay`{.literal}   | 0 (disabled)      | Sets a fencing delay that allows you to configure a two-node cluster so that in a split-brain situation the node with the fewest or least important resources running is the node that gets fenced. For general information about fencing delay parameters and their interactions, see [Fencing delays](#fence-delays "9.4. Fencing delays").                                                                                                    |
+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 9.3. Cluster Properties that Determine Fencing Behavior

Show more

For information about setting cluster properties, see [Setting Cluster properties](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_high_availability_clusters/index#setting-cluster-properties).

### [9.4. Fencing delays](#fence-delays) {#fencing-delays .title}

In two-node clusters, simultaneous communication loss can cause nodes to fence each other, shutting down the entire cluster. Configure a fencing delay to prevent this race condition. Delays are unnecessary in larger clusters, where quorum determines fencing authority.

You can set different types of fencing delays, depending on your system requirements.

-   **static fencing delays**

    A static fencing delay is a fixed, predetermined delay. Setting a static delay on one node makes that node more likely to be fenced because it increases the chances that the other node will initiate fencing first after detecting lost communication. In an active/passive cluster, setting a delay on a passive node makes it more likely that the passive node will be fenced when communication breaks down. You configure a static delay by using the `pcmk_delay_base`{.literal} instance attribute. To configure different delays, set this attribute on a separate fence device for each node. If you use a single fence device for all nodes, you can set this attribute to a host map, for example, `node1:0s;node2:5s`{.literal}.

-   **dynamic fencing delays**

    A dynamic fencing delay is random. It can vary and is determined at the time fencing is needed. You configure a random delay and specify a maximum value for the combined base delay and random delay with the `pcmk_delay_max`{.literal} instance attribute. When the fencing delay for each node is random, which node is fenced is also random. You might find this feature useful if your cluster is configured with a single fence device for all nodes in an active/active design.

-   **priority fencing delays**

    A priority fencing delay is based on active resource priorities. If all resources have the same priority, the node with the fewest resources running is the node that gets fenced. In most cases, you use only one delay-related parameter, but it is possible to combine them. Combining delay-related parameters adds the priority values for the resources together to create a total delay. You configure a priority fencing delay with the `priority-fencing-delay`{.literal} cluster property. You may find this feature useful in an active/active cluster design because it can make the node running the fewest resources more likely to be fenced when communication between the nodes is lost.

**The `pcmk_delay_base`{.literal} instance attribute**

The ‎`pcmk_delay_base`{.literal} instance attribute specifies a base delay value for fencing.

When you set the `pcmk_delay_max`{.literal} instance attribute in addition to the `pcmk_delay_base`{.literal} instance attribute, the overall delay combines a random delay value with this static delay, keeping the sum below the maximum delay. When you set `pcmk_delay_base`{.literal} but do not set `pcmk_delay_max`{.literal}, there is no random component to the delay, and the delay is the value of ‎`pcmk_delay_base`{.literal}.

You can specify different values for different nodes with the `pcmk_delay_base`{.literal} instance attribute. This allows a single fence device to be used in a two-node cluster, with a different delay for each node. You do not need to configure two separate devices to use separate delays. To specify different values for different nodes, you map the host names to the delay value for that node using a similar syntax to `pcmk_host_map`{.literal}. For example, `node1:0;node2:10s`{.literal} would use no delay when fencing `node1`{.literal} and a 10-second delay when fencing `node2`{.literal}.

The `pcmk_delay_max`{.literal} instance attribute

:   Use the ‎`pcmk_delay_base`{.literal} instance attribute to specify a base delay for fencing actions and the maximum delay, which is the maximum value of the combined base delay and random delay. For example, if the base delay is 3 and `pcmk_delay_max`{.literal} is 10, the random delay will be between 3 and 10.

    When you set the `pcmk_delay_base`{.literal} instance attribute in addition to the `pcmk_delay_max`{.literal} instance attribute, the overall delay is derived from a random delay value added to this static delay so that the sum is kept below the maximum delay. When you set `pcmk_delay_max`{.literal} but do not set `pcmk_delay_base`{.literal} there is no static component to the delay.

**The `priority-fencing-delay`{.literal} cluster property**

Setting the `priority-fencing-delay`{.literal} cluster property allows you to configure a two-node cluster so that in a split-brain situation the node with the fewest or least important resources running is the node that gets fenced.

The `priority-fencing-delay`{.literal} property can be set to a time duration. The default value for this property is 0 (disabled). If this property is set to a non-zero value, and the priority meta-attribute is configured for at least one resource, then in a split-brain situation the node with the highest combined priority of all resources running on it will be more likely to remain operational. For example, if you set `pcs resource defaults update priority=1`{.literal} and `pcs property set priority-fencing-delay=15s`{.literal} and no other priorities are set, then the node running the most resources will be more likely to remain operational because the other node will wait 15 seconds before initiating fencing. If a particular resource is more important than the rest, you can give it a higher priority.

The node running the promoted role of a promotable clone gets an extra 1 point if a priority has been configured for that clone.

**Interaction of fencing delays**

Setting more than one type of fencing delay yields the following results:

-   Any delay set with the `priority-fencing-delay`{.literal} property is added to any delay from the `pcmk_delay_base`{.literal} and `pcmk_delay_max`{.literal} instance attributes. This behavior allows some delay when both nodes have equal priority, or both nodes need to be fenced for some reason other than node loss, as when `on-fail=fencing`{.literal} is set for a resource monitor operation. When setting these delays in combination, set the `priority-fencing-delay`{.literal} property to a value that is significantly greater than the maximum delay from `pcmk_delay_base`{.literal} and `pcmk_delay_max`{.literal} to be sure the prioritized node is preferred. Setting this property to twice this value is always safe.
-   Only fencing scheduled by Pacemaker itself observes fencing delays. Fencing scheduled by external code such as `dlm_controld`{.literal} and fencing implemented by the `pcs stonith fence`{.literal} command do not provide the necessary information to the fence device.
-   Some individual fence agents implement a delay parameter, with a name determined by the agent. This delay is independent of delays configured with a ‎`pcmk_delay_*`{.literal} instance attribute. If both of these delays are configured, they are added together and would generally not be used in conjunction.

### [9.5. Testing a fence device](#testing-fence-devices) {#testing-a-fence-device .title}

To prevent data corruption and successfully recover a cluster from node failures, validate the fence device. For a complete testing strategy, verify network connectivity, run the fence agent script, trigger the fence action through the cluster manager, and simulate a physical node failure.

**Prerequisites**

-   You have configured fencing so that a Pacemaker cluster node or Pacemaker remote node results in a hard kill, not a graceful shutdown.
-   You have disabled ACPI soft-off in the `/etc/systemd/logind.conf`{.literal} file so that any power-button-pressed signal is ignored in case of a graceful shutdown.

**Procedure**

1.  Use SSH, Telnet, HTTP, or whatever remote protocol is used to connect to the device to manually log in and test the fence device or see what output is given. For example, if you will be configuring fencing for an IPMI-enabled device,then try to log in remotely with `ipmitool`{.literal}. Take note of the options used when logging in manually because those options might be needed when using the fencing agent.

    If you are unable to log in to the fence device, verify that the device is pingable, there is nothing such as a firewall configuration that is preventing access to the fence device, remote access is enabled on the fencing device, and the credentials are correct.

2.  Run the fence agent manually, using the fence agent script. This does not require that the cluster services are running, so you can perform this step before the device is configured in the cluster. This can ensure that the fence device is responding properly before proceeding.

    Note

    These examples use the `fence_ipmilan`{.literal} fence agent script for an iLO device. The actual fence agent you will use and the command that calls that agent will depend on your server hardware. You should consult the man page for the fence agent you are using to determine which options to specify. You will usually need to know the login and password for the fence device and other information related to the fence device.

    The following example shows the format you would use to run the `fence_ipmilan`{.literal} fence agent script with `-o status`{.literal} parameter to check the status of the fence device interface on another node without actually fencing it. This allows you to test the device and get it working before attempting to reboot the node. When running this command, you specify the name and password of an iLO user that has power on and off permissions for the iLO device.

    ``` {.language-plaintext tabindex="-1"}
    # fence_ipmilan -a ipaddress -l username -p password -o status
    ```

    The following example shows the format you would use to run the `fence_ipmilan`{.literal} fence agent script with the `-o reboot`{.literal} parameter. Running this command on one node reboots the node managed by this iLO device.

    ``` {.language-plaintext tabindex="-1"}
    # fence_ipmilan -a ipaddress -l username -p password -o reboot
    ```

    If the fence agent failed to properly do a status, off, on, or reboot action, you should check the hardware, the configuration of the fence device, and the syntax of your commands. In addition, you can run the fence agent script with the debug output enabled. The debug output is useful for some fencing agents to see where in the sequence of events the fencing agent script is failing when logging into the fence device.

    ``` {.language-plaintext tabindex="-1"}
    # fence_ipmilan -a ipaddress -l username -p password -o status -D /tmp/$(hostname)-fence_agent.debug
    ```

    When diagnosing a failure that has occurred, you should ensure that the options you specified when manually logging in to the fence device are identical to what you passed on to the fence agent with the fence agent script.

    For fence agents that support an encrypted connection, you may see an error due to certificate validation failing, requiring that you trust the host or that you use the fence agent's `ssl-insecure`{.literal} parameter. Similarly, if SSL/TLS is disabled on the target device, you may need to account for this when setting the SSL parameters for the fence agent.

    Note

    If the fence agent that is being tested is a `fence_drac`{.literal}, `fence_ilo`{.literal}, or some other fencing agent for a systems management device that continues to fail, then fall back to trying `fence_ipmilan`{.literal}. Most systems management cards support IPMI remote login and the only supported fencing agent is `fence_ipmilan`{.literal}.

3.  Once the fence device has been configured in the cluster with the same options that worked manually and the cluster has been started, test fencing with the `pcs stonith fence`{.literal} command from any node (or even multiple times from different nodes), as in the following example. The `pcs stonith fence`{.literal} command reads the cluster configuration from the CIB and calls the fence agent as configured to start the fence action. This verifies that the cluster configuration is correct.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith fence node_name
    ```

    If the `pcs stonith fence`{.literal} command works properly, that means the fencing configuration for the cluster should work when a fence event occurs. If the command fails, it means that cluster management cannot invoke the fence device through the configuration it has retrieved. Check for the following issues and update your cluster configuration as needed.

    -   Check your fence configuration. For example, if you have used a host map you should ensure that the system can find the node using the host name you have provided.

    -   Check whether the password and user name for the device include any special characters that could be misinterpreted by the bash shell. Making sure that you enter passwords and user names surrounded by quotation marks could address this issue.

    -   Check whether you can connect to the device using the exact IP address or host name you specified in the `pcs stonith`{.literal} command. For example, if you give the host name in the stonith command but test by using the IP address, that is not a valid test.

    -   If the protocol that your fence device uses is accessible to you, use that protocol to try to connect to the device. For example many agents use ssh or telnet. You should try to connect to the device with the credentials you provided when configuring the device, to see if you get a valid prompt and can log in to the device.

        If you determine that all your parameters are appropriate but you still have trouble connecting to your fence device, you can check the logging on the fence device itself, if the device provides that, which will show if the user has connected and what command the user issued. You can also search through the `/var/log/messages`{.literal} file for instances of stonith and error, which could give some idea of what is transpiring, but some agents can provide additional information.

4.  Once the fence device tests are working and the cluster is up and running, test an actual failure. To do this, take an action in the cluster that should initiate a token loss.

    -   Take down a network. How you take a network depends on your specific configuration. In many cases, you can physically pull the network or power cables out of the host. For information about simulating a network failure, see the Red Hat Knowledgebase solution [What is the proper way to simulate a network failure on a RHEL Cluster?](https://access.redhat.com/solutions/79523/).

        Note

        Disabling the network interface on the local host rather than physically disconnecting the network or power cables is not recommended as a test of fencing because it does not accurately simulate a typical real-world failure.

    -   Block corosync traffic both inbound and outbound using the local firewall.

        The following example blocks corosync, assuming the default corosync port is used, `firewalld`{.literal} is used as the local firewall, and the network interface used by corosync is in the default firewall zone:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --direct --add-rule ipv4 filter OUTPUT 2 -p udp --dport=5405 -j DROP
        # firewall-cmd --add-rich-rule='rule family="ipv4" port port="5405" protocol="udp" drop'
        ```

    -   Simulate a crash and panic your machine with `sysrq-trigger`{.literal}. Note, however, that triggering a kernel panic can cause data loss; it is recommended that you disable your cluster resources first.

        ``` {.language-plaintext tabindex="-1"}
        # echo c > /proc/sysrq-trigger
        ```

**Additional resources**

-   [Disabling ACPI soft-off in the logind.conf file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_managing_high_availability_clusters/index#disabling_acpi_soft_off_in_the_logind_conf_file)

### [9.6. Configuring fencing levels](#configuring-fencing-levels) {#configuring-fencing-levels .title}

Pacemaker supports fencing nodes with multiple devices through a feature called fencing topologies. To implement topologies, create the individual devices as you normally would and then define one or more fencing levels in the fencing topology section in the configuration.

Pacemaker processes fencing levels as follows:

-   Each level is attempted in ascending numeric order, starting at 1.
-   If a device fails, processing terminates for the current level. No further devices in that level are exercised and the next level is attempted instead.
-   If all devices are successfully fenced, then that level has succeeded and no other levels are tried.
-   The operation is finished when a level has passed (success), or all levels have been attempted (failed).

Use the following command to add a fencing level to a node. The devices are given as a comma-separated list of `stonith`{.literal} ids, which are attempted for the node at that level.

``` {.language-plaintext tabindex="-1"}
# pcs stonith level add level node devices
```

The following example configures fence levels so that if the device `my_ilo`{.literal} fails and is unable to fence the node, then Pacemaker attempts to use the device `my_apc`{.literal}.

**Prerequisites**

-   You have configured an ilo fence device called `my_ilo`{.literal} for node `rh7-2`{.literal}.
-   You have configured an apc fence device called `my_apc`{.literal} for node `rh7-2`{.literal}.

**Procedure**

1.  Add a fencing level of 1 for fence device `my_ilo`{.literal} on node `rh7-2`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level add 1 rh7-2 my_ilo
    ```

2.  Add a fencing level of 2 for fence device `my_apc`{.literal} on node `rh7-2`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level add 2 rh7-2 my_apc
    ```

3.  List the currently configured fencing levels.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level
    ```

    ``` {.language-plaintext tabindex="-1"}
     Node: rh7-2
      Level 1 - my_ilo
      Level 2 - my_apc
    ```

**Additional resources**

-   [Configuring node-specific values using node attributes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_managing_high_availability_clusters/index#node-attributes)

### [9.7. Removing a fence level](#removing-a-fence-level) {#removing-a-fence-level .title}

You can remove the fence level for the specified node and device. If no nodes or devices are specified then the fence level you specify is removed from all nodes.

**Procedure**

-   Remove the fence level for the specified node and device:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level remove level [node_id] [stonith_id] ... [stonith_id]
    ```

### [9.8. Clearing fence levels](#clearing-fence-levels) {#clearing-fence-levels .title}

You can clear the fence levels on the specified node or stonith id. If you do not specify a node or stonith id, all fence levels are cleared.

**Procedure**

-   Clear the fence levels on the specified node or stonith id:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level clear [node]|stonith_id(s)]
    ```

-   If you specify more than one stonith id, they must be separated by a comma and no spaces, as in the following example.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level clear dev_a,dev_b
    ```

### [9.9. Verifying nodes and devices in fence levels](#verifying-nodes-and-devices-in-fence-levels_general-fence) {#verifying-nodes-and-devices-in-fence-levels .title}

You can verify that all fence devices and nodes specified in fence levels exist.

**Procedure**

-   Use the following command to verify that all fence devices and nodes specified in fence levels exist:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level verify
    ```

### [9.10. Specifying nodes in fencing topology](#specifying-nodes-in-fencing-topology) {#specifying-nodes-in-fencing-topology .title}

You can specify nodes in fencing topology by a regular expression applied on a node name and by a node attribute and its value.

**Procedure**

-   The following commands configure nodes `node1`{.literal}, `node2`{.literal}, and `node3`{.literal} to use fence devices `apc1`{.literal} and `apc2`{.literal}, and nodes `node4`{.literal}, `node5`{.literal}, and `node6`{.literal} to use fence devices `apc3`{.literal} and `apc4`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level add 1 "regexp%node[1-3]" apc1,apc2
    # pcs stonith level add 1 "regexp%node[4-6]" apc3,apc4
    ```

-   The following commands yield the same results by using node attribute matching:

    ``` {.language-plaintext tabindex="-1"}
    # pcs node attribute node1 rack=1
    # pcs node attribute node2 rack=1
    # pcs node attribute node3 rack=1
    # pcs node attribute node4 rack=2
    # pcs node attribute node5 rack=2
    # pcs node attribute node6 rack=2
    # pcs stonith level add 1 attrib%rack=1 apc1,apc2
    # pcs stonith level add 1 attrib%rack=2 apc3,apc4
    ```

### [9.11. Configuring fencing for redundant power supplies](#configuring-fencing-for-redundant-power) {#configuring-fencing-for-redundant-power-supplies .title}

When configuring fencing for redundant power supplies, the cluster must ensure that when attempting to reboot a host, both power supplies are turned off before either power supply is turned back on.

If the node never completely loses power, the node may not release its resources. This opens up the possibility of nodes accessing these resources simultaneously and corrupting them.

You need to define each device only once and to specify that both are required to fence the node.

**Procedure**

1.  Create the first fence device.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith create apc1 fence_apc_snmp ipaddr=apc1.example.com login=user passwd='7a4D#1j!pz864' pcmk_host_map="node1.example.com:1;node2.example.com:2"
    ```

2.  Create the second fence device.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith create apc2 fence_apc_snmp ipaddr=apc2.example.com login=user passwd='7a4D#1j!pz864' pcmk_host_map="node1.example.com:1;node2.example.com:2"
    ```

3.  Specify that both devices are required to fence the node.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level add 1 node1.example.com apc1,apc2
    # pcs stonith level add 1 node2.example.com apc1,apc2
    ```

### [9.12. Administering fence devices](#administering-fence-devices) {#administering-fence-devices .title}

The `pcs`{.literal} command-line interface provides a variety of commands you can use to administer your fence devices after you have configured them.

#### [9.12.1. Displaying configured fence devices](#displaying_configured_fence_devices) {#displaying-configured-fence-devices .title}

The following command shows all currently configured fence devices. If a *stonith_id* is specified, the command shows the options for that configured fencing device only. If the `--full`{.literal} option is specified, all configured fencing options are displayed.

``` {.language-plaintext tabindex="-1"}
# pcs stonith config [stonith_id] [--full]
```

#### [9.12.2. Exporting fence devices as pcs commands](#exporting_fence_devices_as_pcs_commands) {#exporting-fence-devices-as-pcs-commands .title}

You can display the `pcs`{.literal} commands that can be used to re-create configured fence devices on a different system using the `--output-format=cmd`{.literal} option of the `pcs stonith config`{.literal} command.

The following commands create a `fence_apc_snmp`{.literal} fence device and display the `pcs`{.literal} command you can use to re-create the device.

``` {.language-plaintext tabindex="-1"}
# pcs stonith create myapc fence_apc_snmp ip="zapc.example.com" pcmk_host_map="z1.example.com:1;z2.example.com:2" username="apc" password="apc"
# pcs stonith config --output-format=cmd
```

``` {.language-plaintext tabindex="-1"}
Warning: Only 'text' output format is supported for stonith levels
pcs stonith create --no-default-ops --force -- myapc fence_apc_snmp \
  ip=zapc.example.com password=apc 'pcmk_host_map=z1.example.com:1;z2.example.com:2' username=apc \
  op \
    monitor interval=60s id=myapc-monitor-interval-60s
```

#### [9.12.3. Exporting fence level configuration](#exporting_fence_level_configuration) {#exporting-fence-level-configuration .title}

The `pcs stonith config`{.literal} and the `pcs stonith level config`{.literal} commands support the `--output-format=`{.literal} option to export the fencing level configuration in JSON format and as `pcs`{.literal} commands.

-   Specifying `--output-format=cmd`{.literal} displays the `pcs`{.literal} commands created from the current cluster configuration that configure fencing levels. You can use these commands to re-create configured fencing levels on a different system.
-   Specifying `--output-format=json`{.literal} displays the fencing level configuration in JSON format, which is suitable for machine parsing.

#### [9.12.4. Modifying and deleting fence devices](#modifying_and_deleting_fence_devices) {#modifying-and-deleting-fence-devices .title}

Modify or add options to a currently configured fencing device with the following command.

``` {.language-plaintext tabindex="-1"}
# pcs stonith update stonith_id [stonith_device_options]
```

Updating a SCSI fencing device with the `pcs stonith update`{.literal} command causes a restart of all resources running on the same node where the fencing resource was running. You can use either version of the following command to update SCSI devices without causing a restart of other cluster resources. SCSI fencing devices can be configured as multipath devices.

``` {.language-plaintext tabindex="-1"}
# pcs stonith update-scsi-devices stonith_id set device-path1 device-path2
# pcs stonith update-scsi-devices stonith_id add device-path1 remove device-path2
```

Use the following command to remove a fencing device from the current configuration.

``` {.language-plaintext tabindex="-1"}
# pcs stonith delete stonith_id
```

#### [9.12.5. Manually fencing a cluster node](#manually_fencing_a_cluster_node) {#manually-fencing-a-cluster-node .title}

You can fence a node manually with the following command. If you specify the `--off`{.literal} option this will use the `off`{.literal} API call to stonith which will turn the node off instead of rebooting it.

``` {.language-plaintext tabindex="-1"}
# pcs stonith fence node [--off]
```

In a situation where no fence device is able to fence a node even if it is no longer active, the cluster may not be able to recover the resources on the node. If this occurs, after manually ensuring that the node is powered down you can enter the following command to confirm to the cluster that the node is powered down and free its resources for recovery.

Warning

If the node you specify is not actually off, but running the cluster software or services normally controlled by the cluster, data corruption and cluster failure occurs.

``` {.language-plaintext tabindex="-1"}
# pcs stonith confirm node
```

#### [9.12.6. Disabling a fence device](#disabling_a_fence_device) {#disabling-a-fence-device .title}

To disable a fencing device, run the `pcs stonith disable`{.literal} command.

The following command disables the fence device `myapc`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs stonith disable myapc
```

#### [9.12.7. Preventing a node from using a fencing device](#preventing_a_node_from_using_a_fencing_device) {#preventing-a-node-from-using-a-fencing-device .title}

To prevent a specific node from using a fencing device, you can configure location constraints for the fencing resource.

The following example prevents fence device `node1-ipmi`{.literal} from running on `node1`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs constraint location node1-ipmi avoids node1
```

### [9.13. Additional resources](#configuring-fencing_913-additional-resources) {#additional-resources-1 .title}

-   [Fencing in a Red Hat High Availability Cluster (Red Hat Knowledgebase)](https://access.redhat.com/solutions/15575)

## [Chapter 10. Configuring SBD fencing in a high-availability cluster](#configuring-sbd-fencing-in-a-high-availability-cluster) {#chapter-10.-configuring-sbd-fencing-in-a-high-availability-cluster .title}

Storage-based death (SBD) is a fencing mechanism that provides an alternative to traditional "power fencing" agents. SBD uses a watchdog timer, and optionally shared storage to make nodes self-fence if they become unresponsive or lose quorum.

You can use this approach in environments where network-based power management is unavailable, or where you want to ensure a node reboots if it loses access to the shared storage fabric.

### [10.1. Overview of SBD fencing](#overview-of-sbd-fencing) {#overview-of-sbd-fencing .title}

Storage-based death (SBD) fencing provides a mechanism for nodes to self-fence in the event certain health checks fail or can't be performed in time or a reboot is requested by disk-based messaging. You can implement SBD in one of two ways, depending on your hardware and storage availability.

+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Feature                 | Watchdog-only fencing                                                                                                                                                                                                                                                                 | Poison-pill fencing                                                                                                                                                                                                                                                                                                                                                                                                                          |
+:========================+:======================================================================================================================================================================================================================================================================================+:=============================================================================================================================================================================================================================================================================================================================================================================================================================================+
| **Mechanism**           | Relies on health and quorum monitoring. If a node loses quorum or cannot verify its own health, it stops resetting the watchdog timer. The cluster assumes fencing is successful only after the `stonith-watchdog-timeout`{.literal} expires.                                         | Uses shared storage to send explicit \"poison pill\" messages by the `fence_sbd`{.literal} agent. If the target node is responsive, it reads the message and reboots immediately. If the node is unresponsive or storage is inaccessible, it relies on the watchdog timer to trigger the reboot.                                                                                                                                             |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Storage requirement** | None.                                                                                                                                                                                                                                                                                 | Requires 1 to 3 shared block devices (minimum 4 MB each). Devices must be accessible by all nodes and cannot host a filesystem, be managed by LVM, or be part of a RAID/mirroring layer managed by the cluster.                                                                                                                                                                                                                              |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Reliability**         | Reliability is derived from a watchdog device (hardware WDT or `softdog`{.literal}) supervising the software timer. Hardware WDTs are preferred; `softdog`{.literal} (kernel-space) is a supported fallback but might fail if the kernel completely hangs or is starved of resources. | Reliability is derived from the same watchdog device mechanism. Although disks facilitate communication, the watchdog device is the responsible for guarantying a reboot. Because Pacemaker awareness keeps a cluster accessible when disks are not available, even a single shared disk does not represent a single point of failure (SPOF). However, use three disks if you want to be able to fence when a storage device is unavailable. |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Performance**         | Can be configured for faster recovery by reducing network latency blips. However, the cluster must wait for the full `stonith-watchdog-timeout`{.literal} to expire before recovering resources.                                                                                      | Potentially provides faster reboot because a responsive target node might react to the fence message immediately. However, it might require higher storage-layer timeouts, such as 30s, to account for storage maintenance or firmware updates. If a node comes back quickly resource recovery time might be short otherwise resource recovery is held back by these storage timeout requirements.                                           |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Common use case**     | Environments without shared storage. Preferred for clusters with at least 3 quorum voters (or 2 nodes and a QDevice).                                                                                                                                                                 | Primarily used in 2-node clusters to bypass the 3-vote quorum limitation of watchdog-only setups. Also useful for multi-site clusters where the network link between members might be severed but storage remains accessible.                                                                                                                                                                                                                |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 10.1. Comparison of watchdog-only and poison-pill fencing

Show more

### [10.2. Configuring watchdog-only SBD fencing](#configuring-watchdog-only-sbd-fencing) {#configuring-watchdog-only-sbd-fencing .title}

In a watchdog-only configuration nodes monitor quorum state and their health as seen by the cluster. If a node is unable to retrieve the cluster view (CIB) or if the cluster determines the node is in an unhealthy state, the local watchdog timer on that node to expire, triggering a reboot.

**Prerequisites**

-   A running high-availability cluster.
-   A functional watchdog timer (WDT) device available on all nodes at `/dev/watchdog`{.literal} or another device path configured on a per node basis.
-   No other fencing devices are active, or if other fencing devices are available in the cluster watchdog-fencing can be limited to those nodes that can't be fenced by those or a fencing topology can be configured to have watchdog-fencing as fallback

Note

SBD implementation is modular and can be deployed selectively within a cluster. In heterogeneous environments, such as those containing `pacemaker-remote`{.literal} nodes or hardware lacking functional watchdog devices, SBD remains a viable fencing solution for compatible members. The absence of universal SBD support does not preclude its selective implementation on supported nodes.

**Procedure**

1.  On all nodes in the cluster, install the `sbd`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install sbd
    ```

2.  On each node, list the available watchdog devices to identify the proper device path:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith sbd watchdog list
    ```

3.  On each node, verify that the watchdog device functions correctly by triggering a test:

    Warning

    This command reboots the system to confirm the watchdog can successfully trigger a hardware reset. Perform this test only before enabling the SBD daemon; the command does not work after the daemon has taken control of the watchdog device.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith sbd watchdog test
    ```

4.  On one node, enable SBD fencing to update `/etc/sysconfig/sbd`{.literal} on all nodes and enables the `sbd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith sbd enable sbd_watchdog_timeout=5
    ```

5.  Set the cluster `stonith-watchdog-timeout`{.literal} property. This value determines how long the remaining cluster nodes do wait before assuming a missing node has successfully self-fenced:

    ``` {.language-plaintext tabindex="-1"}
    # pcs property set stonith-watchdog-timeout=10
    ```

    Important

    Each node verifies this property individually before bringing up resources. To prevent split-brain scenarios, `stonith-watchdog-timeout`{.literal} must be at least as large as the value of `SBD_WATCHDOG_TIMEOUT`{.literal}. Do not set this property to `-1`{.literal} for automated calculation, as inconsistent `SBD_WATCHDOG_TIMEOUT`{.literal} values across nodes would then lead to different calculations of stonith-watchdog-timeout (a value that needs to be consistent for both the fencing originator and the target - lower for originator than target leads to split-brain) for different nodes.

6.  Restart the cluster to initialize the SBD processes:

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster stop --all
    # pcs cluster start --all
    ```

**Verification**

1.  Verify that the SBD status is active:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith sbd status
    ```

2.  Manually trigger a fence test to ensure the configuration works:

    Warning

    This command reboots the target node immediately.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith fence node_name
    ```

### [10.3. Creating a visible watchdog device for selective fencing](#creating-a-visible-watchdog-device-for-selective-fencing) {#creating-a-visible-watchdog-device-for-selective-fencing .title}

In heterogeneous clusters where some nodes lack a functional hardware watchdog, you can create a visible fencing resource to ensure watchdog-only fencing is applied only to supported nodes.

**Prerequisites**

-   SBD is enabled in watchdog-only mode on the supported nodes.
-   A functional hardware watchdog device is available on the target nodes.

**Procedure**

1.  Create the watchdog fencing resource. Use the `pcmk_host_list`{.literal} attribute to specify only the nodes that possess a functional watchdog device:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith create watchdog_fencing fence_watchdog pcmk_host_list="node-01,node-02"
    ```

2.  If the cluster contains nodes that are not in the `pcmk_host_list`{.literal}, configure an alternative fencing method (such as IPMI or a power-based agent) for those specific nodes.

3.  Configure fencing levels to use the watchdog as a fallback. Set the primary fencing agent at level 1 and the watchdog agent at level 2.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level add 1 node-01 ipmi_fencing
    # pcs stonith level add 2 node-01 watchdog_fencing
    ```

**Verification**

1.  Confirm that the resource is restricted to the specified hosts:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith config watchdog_fencing
    ```

2.  Verify that the cluster recognizes the fencing topology:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level
    ```

### [10.4. Configuring watchdog-only SBD fencing in a 2-node cluster with a QDevice](#configuring-watchdog-only-sbd-fencing-in-a-2-node-cluster-with-a-qdevice) {#configuring-watchdog-only-sbd-fencing-in-a-2-node-cluster-with-a-qdevice .title}

When using a 2-node cluster, adding a quorum device (`corosync-qdevice`{.literal}) provides an additional vote to quorum, making its behavior closer to odd-numbered member clusters. This allows the cluster to bypass the standard 3-node minimum quorum vote limitation for watchdog-only SBD fencing.

When combining a QDevice with watchdog-only SBD fencing, you must strictly align your timeout values, otherwise SBD prevents startup.

**Procedure**

1.  Determine the required timeout values for your cluster:

    -   `qdevice-sync_timeout`{.literal}: The default value is `30s`{.literal}.
    -   `SBD_WATCHDOG_TIMEOUT`{.literal}: If this value is less than the `qdevice-sync_timeout`{.literal}, a quorum state update can be delayed long enough to cause a split-brain situation.
    -   `stonith-watchdog-timeout`{.literal}: This value must be higher than the `SBD_WATCHDOG_TIMEOUT`{.literal} to ensure the cluster waits long enough for a node to self-fence. Set this to double the value of the `SBD_WATCHDOG_TIMEOUT`{.literal}. Therefore, if `SBD_WATCHDOG_TIMEOUT`{.literal} is 30, this should be `60`{.literal}.

2.  Enable SBD and configure the watchdog timeout. By not specifying any block devices, SBD will automatically defaults to watchdog-only fencing:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith sbd enable SBD_WATCHDOG_TIMEOUT=30
    ```

3.  Configure the `stonith-watchdog-timeout`{.literal} cluster property to enable the implicit, \"hidden\" watchdog STONITH device:

    ``` {.language-plaintext tabindex="-1"}
    # pcs property set stonith-watchdog-timeout=60
    ```

4.  Optional: Create a visible watchdog fencing device. Incorporate this device into a fencing topology, such as configuring it as a fallback for other fencing devices that have failed, or limiting it to a certain list of nodes. Configure the device using the `fence_watchdog`{.literal} agent:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith create sbd_watchdog fence_watchdog
    ```

### [10.5. Configuring poison-pill SBD fencing](#configuring-poison-pill-sbd-fencing) {#configuring-poison-pill-sbd-fencing .title}

To communicate fencing instructions, the poison-pill fencing uses shared block devices. To fence a node, the cluster writes a message to the shared device. Then, the target node reads this message and reboots itself.

**Prerequisites**

-   A running high-availability cluster.
-   A functional watchdog timer (WDT) device available on all nodes configured to be fenced by using the poison-pill fencing, for example at `/dev/watchdog`{.literal}. You can configure this path on a per-node basis.
-   One to three shared block devices (minimum 4 MB each) accessible by all nodes.
-   The shared devices must not contain a filesystem or be managed by LVM.

**Procedure**

1.  On all nodes in the cluster, install the SBD and fence agent packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install sbd fence-agents-sbd
    ```

2.  On each node, verify that the watchdog device functions correctly by triggering a test:

    Warning

    This command reboots the system to confirm the watchdog can successfully trigger a hardware reset. Perform this test only before enabling the SBD daemon; the command does not work after the daemon takes control of the watchdog device.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith sbd watchdog test
    ```

3.  Initialize the shared SBD block device. Replace *`/dev/sdb`{.literal}* with the path to your shared device:

    Note

    If you are using multiple shared block devices for redundancy, repeat the `device=`{.literal} parameter for each device (for example, `device=/dev/sdb device=/dev/sdc`{.literal}).

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith sbd device setup device=/dev/sdb
    ```

4.  Enable SBD with the shared device:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith sbd enable device=/dev/sdb sbd_watchdog_timeout=5
    ```

5.  Create the fencing device in the cluster. This example uses `fence_sbd_storage`{.literal} as the resource name:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith create fence_sbd_storage fence_sbd devices=/dev/sdb
    ```

6.  Adjust the `pcmk_reboot_timeout`{.literal} to ensure the cluster waits long enough for the disk message to be processed. This value should be at least 5 seconds higher than the `msgwait`{.literal} value stored on the disk:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith update sbd_fence pcmk_reboot_timeout=15
    ```

**Verification**

1.  Verify that the service is enabled and running, the nodes are correctly registered on the SBD device and check their slot status:

    ``` {.language-plaintext tabindex="-1"}
    # pcs sbd status --full
    ```

2.  Check the `stonith-watchdog-timeout`{.literal} cluster property:

    ``` {.language-plaintext tabindex="-1"}
    # pcs property show stonith-watchdog-timeout
    ```

    For a standard poison-pill deployment, this value should be `0`{.literal} (disabled) to prevent the cluster from prematurely assuming a node has self-fenced before the poison-pill message is acknowledged. In advanced setups where this property is nonzero, ensure that all targets used for poison-pill fencing are explicitly excluded from watchdog-only fencing to avoid split-brain risks.

3.  Manually trigger a fence test to ensure the configuration works:

    Warning

    This command reboots the target node immediately.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith fence node_name
    ```

### [10.6. Timing configuration considerations in poison-pill fencing](#timing-configuration-considerations-in-poison-pill-fencing) {#timing-configuration-considerations-in-poison-pill-fencing .title}

When deploying a Red Hat High Availability cluster by using poison-pill fencing with Storage-based Death (SBD), configure timing carefully. Proper timeouts ensure that nodes are safely fenced during failures, preventing split-brain conditions while allowing cluster services to stabilize.

Here are the primary considerations for timing configurations in a poison-pill fencing scenario:

`SBD_WATCHDOG_TIMEOUT`{.literal}

:   Keep this at the default of 5 seconds. A higher value gives the cluster more time to resolve temporary connectivity blips without reacting harshly, but it increases the time it takes to recover from legitimate failures. Setting it below the default 5 seconds is cautioned against, as it can make the cluster overly aggressive and lead to instability during high load or brief unresponsiveness.

    If your cluster uses a QDevice, set the `SBD_WATCHDOG_TIMEOUT`{.literal} parameter higher than `qdevice-sync_timeout`{.literal} (which defaults to 30s). Set a difference of 3 to 5 seconds to prevent delayed quorum updates from causing a split-brain situation.

`msgwait`{.literal} timeout

:   The duration that `fence_sbd`{.literal} waits after writing the poison-pill message before the fencing action is considered complete. Set this to twice the value of `SBD_WATCHDOG_TIMEOUT`{.literal}, for example, 10 seconds, if the watchdog timeout is 5 seconds. If `msgwait`{.literal} is set lower than the watchdog timeout, the cluster can prematurely declare the fencing operation successful while the target node is still processing the action or waiting for its hardware watchdog to expire, resulting in a split-brain scenario.

    The `msgwait`{.literal} duration must be appropriately sized to securely cover three distinct scenarios:

    1.  **The target successfully reads the message and self-fences:** The intended scenario where the target node is still responsive, successfully reads the poison-pill message from the shared block device, and initiates a self-fence.

    2.  **The target loses access to the disks:** The target node is still running but finds that it is not capable of reading from a quorate number of shared disks, causing it to recognize this loss of access and self-fence.

    3.  **The target is completely unresponsive:** The target node is frozen and incapable of doing anything. Because it cannot run actions, it will not be able to reset the (hardware)-watchdog, which in turn leads to a reboot as well.

        If `msgwait`{.literal} is set lower than the timeout derived from preceding considerations, the cluster can prematurely declare the fencing operation successful while the target node is still processing the action or waiting for its hardware watchdog to expire, allowing a split-brain scenario.

`pcmk_reboot_timeout`{.literal}

:   The generic timeout where the cluster waits for a fencing device, such as `fence_sbd`{.literal}, to complete a reboot action.

    This value should be raised so that it is at least 5 seconds higher than the `msgwait`{.literal} attribute. If it is not raised accordingly, the cluster might give up on the fencing operation and report a failure before the `msgwait`{.literal} period has been fully exhausted.

`SBD_DELAY_START`{.literal} and startup delays

:   Setting a delay on startup gives the cluster extra time to stabilize and allows storage devices to fully come online before monitoring begins. Furthermore, a generic Pacemaker issue can occur after a quick recovery: a fenced node that rejoins the cluster too soon can still receive the broadcast message about its own successful fencing. Pacemaker interprets this message as evidence of an error in the fencing sublayer and places the node into a permanent error state. This issue occurs especially in virtual environments, where nodes boot quickly.

    -   **With SBD:** An increase of `SBD_DELAY_START`{.literal} can be used to mitigate this behavior, purposefully slowing the node's re-entry so the old broadcast clears.
    -   **Without SBD:** For environments not using SBD, there is the hint to delay the corosync startup directly in the unit-file to achieve the same result.

## [Chapter 11. Configuring cluster resources](#configuring-cluster-resources) {#chapter-11.-configuring-cluster-resources .title}

A *cluster resource* is an instance of a program, an application, or data to be managed by the cluster service. These resources are abstracted by agents that provide a standard interface for managing the resource in a cluster environment.

To ensure that resources remain healthy, you can add a monitoring operation to a resource's definition. If you do not specify a monitoring operation for a resource, one is added by default. You can determine the behavior of a resource in a cluster by configuring constraints for that resource. You can configure the following categories of constraints:

-   `location`{.literal} constraints - A location constraint determines which nodes a resource can run on. Determining which nodes a resource can run on.
-   `order`{.literal} constraints - An ordering constraint determines the order in which the resources run.
-   `colocation`{.literal} constraints - A colocation constraint determines where resources will be placed relative to other resources.

As a shorthand for configuring a set of constraints that will locate a set of resources together and ensure that the resources start sequentially and stop in reverse order, Pacemaker supports the concept of resource groups. After you have created a resource group, you can configure constraints on the group itself just as you configure constraints for individual resources.

The format for the command to create a cluster resource is as follows:

``` {.language-plaintext tabindex="-1"}
# pcs resource create resource_id [standard:[provider:]]type [resource_options] [op operation_action operation_options [operation_action operation options]...] [meta meta_options...] [clone [clone_id] [clone_options] | promotable [clone_id] [clone_options] [--wait[=n]]
```

Key cluster resource creation options include the following:

-   The `--before`{.literal .option} and `--after`{.literal .option} options specify the position of the added resource relative to a resource that already exists in a resource group.
-   Specifying the `--disabled`{.literal .option} option indicates that the resource is not started automatically.

There is no limit to the number of resources you can create in a cluster.

### [11.1. Resource creation examples](#resource_creation_examples) {#resource-creation-examples .title}

The following command creates a resource with the name `VirtualIP`{.literal} of standard `ocf`{.literal}, provider `heartbeat`{.literal}, and type `IPaddr2`{.literal}. The floating address of this resource is 192.168.0.120, and the system checks whether the resource is running every 30 seconds.

``` {.language-plaintext tabindex="-1"}
# pcs resource create VirtualIP ocf:heartbeat:IPaddr2 ip=192.168.0.120 cidr_netmask=24 op monitor interval=30s
```

Alternately, you can omit the *standard* and *provider* fields and use the following command. This will default to a standard of `ocf`{.literal} and a provider of `heartbeat`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs resource create VirtualIP IPaddr2 ip=192.168.0.120 cidr_netmask=24 op monitor interval=30s
```

### [11.2. Deleting a configured resource](#deleting_a_configured_resource) {#deleting-a-configured-resource .title}

Delete a configured resource with the following command.

``` {.language-plaintext tabindex="-1"}
# pcs resource delete resource_id
```

For example, the following command deletes an existing resource with a resource ID of `VirtualIP`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs resource delete VirtualIP
```

You can delete multiple resources with a single command. The following command deletes an existing resource with a resource ID of `resource1`{.literal} and an existing resource with a resource ID of `resource2`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs resource delete resource1 resource2
```

### [11.3. Resource agent identifiers](#resource-properties) {#resource-agent-identifiers .title}

The identifiers that you define for a resource tell the cluster which agent to use for the resource, where to find that agent and what standards it conforms to.

The following table describes these properties of a resource agent.

+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                | Description                                                                                                                                                                                                                                                                                                                                                                                  |
+:=====================+:=============================================================================================================================================================================================================================================================================================================================================================================================+
| standard             | The standard the agent conforms to. Allowed values and their meaning:                                                                                                                                                                                                                                                                                                                        |
|                      |                                                                                                                                                                                                                                                                                                                                                                                              |
|                      | \* `ocf`{.literal} - The specified *type* is the name of an executable file conforming to the Open Cluster Framework Resource Agent API and located beneath `/usr/lib/ocf/resource.d/`{.literal}*`provider`{.literal}*                                                                                                                                                                       |
|                      |                                                                                                                                                                                                                                                                                                                                                                                              |
|                      | \* `lsb`{.literal} - The specified *type* is the name of an executable file conforming to Linux Standard Base Init Script Actions. If the type does not specify a full path, the system will look for it in the `/etc/init.d`{.literal} directory.                                                                                                                                           |
|                      |                                                                                                                                                                                                                                                                                                                                                                                              |
|                      | \* `systemd`{.literal} - The specified *type* is the name of an installed `systemd`{.literal} unit                                                                                                                                                                                                                                                                                           |
|                      |                                                                                                                                                                                                                                                                                                                                                                                              |
|                      | \* `service`{.literal} - Pacemaker will search for the specified *type*, first as an `lsb`{.literal} agent, then as a `systemd`{.literal} agent                                                                                                                                                                                                                                              |
|                      |                                                                                                                                                                                                                                                                                                                                                                                              |
|                      | \* `nagios`{.literal} - The specified *type* is the name of an executable file conforming to the Nagios Plugin API and located in the `/usr/libexec/nagios/plugins`{.literal} directory, with OCF-style metadata stored separately in the `/usr/share/nagios/plugins-metadata`{.literal} directory (available in the `nagios-agents-metadata`{.literal} package for certain common plugins). |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| type                 | The name of the resource agent you want to use, for example `IPaddr`{.literal} or `Filesystem`{.literal}                                                                                                                                                                                                                                                                                     |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| provider             | The OCF spec allows multiple vendors to supply the same resource agent. Most of the agents shipped by Red Hat use `heartbeat`{.literal} as the provider.                                                                                                                                                                                                                                     |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 11.1. Resource Agent Identifiers

Show more

### [11.4. Displaying resources and resource parameters](#displaying-resource-specific-parameters) {#displaying-resources-and-resource-parameters .title}

Inspect and monitor cluster resources using `pcs`{.literal} display commands. You can verify resource status, review configuration parameters, and list available resource agents, providers, and standards to ensure your cluster is configured correctly.

+--------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| pcs Display Command                                                                                                            | Output                                                                                                                                                                                                                                                                       |
+:===============================================================================================================================+:=============================================================================================================================================================================================================================================================================+
| `pcs resource describe [`{.literal}*`standard`{.literal}*`:[`{.literal}*`provider`{.literal}*`:]]`{.literal}*`type`{.literal}* | Displays a description of an individual resource, the parameters you can set for that resource, and the default values for the resource. For example, `pcs resource describe ocf:heartbeat:apache`{.literal} displays information for a resource of type `apache`{.literal}. |
+--------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcs resource status`{.literal}                                                                                                | Displays a list of all configured resources.                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcs resource config `{.literal}*`resource_id`{.literal}*                                                                      | Displays the configured parameters for a resource.                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcs resource status `{.literal}*`resource_id`{.literal}*                                                                      | Displays the status of an individual resource.                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcs resource status node=`{.literal}*`node_id`{.literal}*                                                                     | Displays the status of the resources running on a specific node, use the following command. You can use this command to display the status of resources on both cluster and remote nodes.                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcs resource list`{.literal}                                                                                                  | Displays a list of all available resources.                                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcs resource standards`{.literal}                                                                                             | Displays a list of available resource agent standards.                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcs resource providers`{.literal}                                                                                             | Displays a list of available resource agent providers.                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcs resource list `{.literal}*`string`{.literal}*                                                                             | Displays a list of available resources filtered by the specified string. You can use this command to display resources filtered by the name of a standard, a provider, or a type.                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Show more

### [11.5. Adding descriptions to cluster resources and elements](#adding-descriptions-to-cluster-resources-and-elements_general-fence) {#adding-descriptions-to-cluster-resources-and-elements .title}

You can add brief text descriptions to cluster resources and other Cluster Information Base (CIB) elements. Supplemental text documents your cluster configuration, provides context for specific elements, and aids administrators during troubleshooting.

Elements that support the description attribute include primitive resources, groups, clones, bundles, Access Control List (ACL) permissions, ACL roles, alerts, alert recipients, and nodes.

**Procedure**

-   To add a description to a general CIB element, use the `pcs cib element description`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # pcs cib element description <element_id> "<description_text>"
    ```

    For convenience, you can also use the `pcs resource description`{.literal} and `pcs stonith description`{.literal} aliases.

**Verification**

-   Verify that the description was applied by viewing the configuration of the modified element:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource config <resource_id>
    ```

### [11.6. Configuring resource meta options](#configuring-resource-meta-options) {#configuring-resource-meta-options .title}

In addition to the resource-specific parameters, you can configure additional resource options for any resource. These options are used by the cluster to decide how your resource should behave.

The following table describes the resource meta options.

+-----------------------------------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                             | Default                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+:==================================+:=========================+:========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `priority`{.literal}              | `0`{.literal}            | If not all resources can be active, the cluster will stop lower priority resources in order to keep higher priority ones active.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+-----------------------------------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `target-role`{.literal}           | `Started`{.literal}      | Indicates what state the cluster should attempt to keep this resource in. Allowed values:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                   |                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   |                          | \* `Stopped`{.literal} - Force the resource to be stopped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                   |                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   |                          | \* `Started`{.literal} - Allow the resource to be started (and in the case of promotable clones, promoted if appropriate)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                   |                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   |                          | \* `Promoted`{.literal} - Allow the resource to be started and, if appropriate, promoted                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                   |                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   |                          | \* `Unpromoted`{.literal} - Allow the resource to be started, but only in unpromoted mode if the resource is promotable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+-----------------------------------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `is-managed`{.literal}            | `true`{.literal}         | Indicates whether the cluster is allowed to start and stop the resource. Allowed values: `true`{.literal}, `false`{.literal}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+-----------------------------------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `resource-stickiness`{.literal}   | 1                        | Value to indicate how much the resource prefers to stay where it is.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+-----------------------------------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `requires`{.literal}              | Calculated               | Indicates under what conditions the resource can be started.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                   |                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   |                          | Possible values of defaults to `fencing`{.literal} except under these conditions. Possible values:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                   |                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   |                          | \* `nothing`{.literal} - The cluster can always start the resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                   |                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   |                          | \* `quorum`{.literal} - The cluster can only start this resource if a majority of the configured nodes are active. This is the default value if `stonith-enabled`{.literal} is `false`{.literal} or the resource's `standard`{.literal} is `stonith`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   |                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   |                          | \* `fencing`{.literal} - The cluster can only start this resource if a majority of the configured nodes are active *and* any failed or unknown nodes have been fenced.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                   |                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   |                          | \* `unfencing`{.literal} - The cluster can only start this resource if a majority of the configured nodes are active *and* any failed or unknown nodes have been fenced *and* only on nodes that have been *unfenced*. This is the default value if the `provides=unfencing`{.literal} `stonith`{.literal} meta option has been set for a fencing device.                                                                                                                                                                                                                                                                                                                                                                                               |
+-----------------------------------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `migration-threshold`{.literal}   | `INFINITY`{.literal}     | How many failures may occur for this resource on a node before this node is marked ineligible to host this resource. A value of 0 indicates that this feature is disabled (the node will never be marked ineligible); by contrast, the cluster treats `INFINITY`{.literal} (the default) as a very large but finite number. This option has an effect only if the failed operation has `on-fail=restart`{.literal} (the default), and additionally for failed start operations if the cluster property `start-failure-is-fatal`{.literal} is `false`{.literal}.                                                                                                                                                                                         |
+-----------------------------------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `failure-timeout`{.literal}       | `0`{.literal} (disabled) | Used in conjunction with the `migration-threshold`{.literal} option, indicates how many seconds to wait before acting as if the failure had not occurred, and potentially allowing the resource back to the node on which it failed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+-----------------------------------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `multiple-active`{.literal}       | `stop_start`{.literal}   | Indicates what the cluster should do if it ever finds the resource active on more than one node. Allowed values:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                   |                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   |                          | \* `block`{.literal} - mark the resource as unmanaged                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                   |                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   |                          | \* `stop_only`{.literal} - stop all active instances and leave them that way                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                   |                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   |                          | \* `stop_start`{.literal} - stop all active instances and start the resource in one location only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                   |                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                   |                          | \* `stop_unexpected`{.literal} - stop only unexpected instances of the resource, without requiring a full restart. It is the user's responsibility to verify that the service and its resource agent can function with extra active instances without requiring a full restart.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+-----------------------------------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `critical`{.literal}              | `true`{.literal}         | Sets the default value for the `influence`{.literal} option for all colocation constraints involving the resource as a dependent resource (*target_resource*), including implicit colocation constraints created when the resource is part of a resource group. The `influence`{.literal} colocation constraint option determines whether the cluster will move both the primary and dependent resources to another node when the dependent resource reaches its migration threshold for failure, or whether the cluster will leave the dependent resource offline without causing a service switch. The `critical`{.literal} resource meta option can have a value of `true`{.literal} or `false`{.literal}, with a default value of `true`{.literal}. |
+-----------------------------------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `allow-unhealthy-nodes`{.literal} | `false`{.literal}        | When set to `true`{.literal}, the resource is not forced off a node due to degraded node health. When health resources have this attribute set, the cluster can automatically detect if the node's health recovers and move resources back to it. A node's health is determined by a combination of the health attributes set by health resource agents based on local conditions, and the strategy-related options that determine how the cluster reacts to those conditions.                                                                                                                                                                                                                                                                          |
+-----------------------------------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 11.2. Resource meta options

Show more

### [11.7. Setting meta options](#setting-meta-options) {#setting-meta-options .title}

You can set a resource option for a particular resource to a value other than the default when you create the resource. You can also set the value of a resource meta option for an existing resource, group, or cloned resource.

The following procedure provides example commands that set the value of resource meta options both on resource creation and on an existing resource.

**Procedure**

1.  Create a resource with a `resource-stickiness`{.literal} value of 50.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create VirtualIP ocf:heartbeat:IPaddr2 ip=192.168.0.120 meta resource-stickiness=50
    ```

2.  For the existing resource named `dummy_resource`{.literal}, set the `failure-timeout`{.literal} meta option to 20 seconds, so that the resource can attempt to restart on the same node in 20 seconds.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource meta dummy_resource failure-timeout=20s
    ```

3.  Display the values for the resource to verify that `failure-timeout=20s`{.literal} is set.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource config dummy_resource
    ```

    ``` {.language-plaintext tabindex="-1"}
     Resource: dummy_resource (class=ocf provider=heartbeat type=Dummy)
      Meta Attrs: failure-timeout=20s
      ...
    ```

### [11.8. Changing the default value of a resource option](#changing-the-default-value-of-a-resource-option) {#changing-the-default-value-of-a-resource-option .title}

You can change the default value of a resource option for all resources with the `pcs resource defaults update`{.literal} command.

**Procedure**

-   The following command resets the default value of `resource-stickiness`{.literal} to 100:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource defaults update resource-stickiness=100
    ```

    The original `pcs resource defaults `{.literal}*`name`{.literal}*`=`{.literal}*`value`{.literal}* command, which set defaults for all resources in previous releases, remains supported unless there is more than one set of defaults configured. However, `pcs resource defaults update`{.literal} is now the preferred version of the command.

### [11.9. Changing the default value of a resource option for sets of resources](#changing-the-default-value-of-a-resource-option-for-sets-of-resources) {#changing-the-default-value-of-a-resource-option-for-sets-of-resources .title}

You can create multiple sets of resource defaults with the `pcs resource defaults set create`{.literal} command, which allows you to specify a rule that contains `resource`{.literal} expressions. Only `resource`{.literal} and `date`{.literal} expressions, including `and`{.literal}, `or`{.literal} and parentheses, are allowed in rules that you specify with this command.

With the `pcs resource defaults set create`{.literal} command, you can configure a default resource value for all resources of a particular type. If, for example, you are running databases which take a long time to stop, you can increase the `resource-stickiness`{.literal} default value for all resources of the database type to prevent those resources from moving to other nodes more often than you want.

**Procedure**

-   The following command sets the default value of `resource-stickiness`{.literal} to 100 for all resources of type `pqsql`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource defaults set create id=pgsql-stickiness meta resource-stickiness=100 rule resource ::pgsql
    ```

-   In this example, `::pgsql`{.literal} means a resource of any class, any provider, of type `pgsql`{.literal}.

    -   Specifying `ocf:heartbeat:pgsql`{.literal} would indicate class `ocf`{.literal}, provider `heartbeat`{.literal}, type `pgsql`{.literal},
    -   Specifying `ocf:pacemaker:`{.literal} would indicate all resources of class `ocf`{.literal}, provider `pacemaker`{.literal}, of any type.

-   The `id`{.literal} option, which names the set of resource defaults, is not mandatory. If you do not set this option `pcs`{.literal} will generate an ID automatically. Setting this value allows you to provide a more descriptive name.

    To change the default values in an existing set, use the `pcs resource defaults set update`{.literal} command.

### [11.10. Displaying currently configured resource defaults](#displaying-currently-configured-resource-defaults) {#displaying-currently-configured-resource-defaults .title}

The `pcs resource defaults [config]`{.literal} command displays currently configured default values for resource options, including specified rules. Output can be displayed in text, JSON, or command format.

The `pcs resource defaults [config]`{.literal} command supports the following output formats:

-   Specifying `--output-format=text`{.literal} displays the configured resource defaults in plain text format, which is the default format for this option.
-   Specifying `--output-format=cmd`{.literal} displays the `pcs resource defaults`{.literal} commands created from the current cluster defaults configuration. Use these commands to re-create configured resource defaults on another system.
-   Specifying `--output-format=json`{.literal} displays the configured resource defaults in JSON format, which is suitable for machine parsing.

The following example procedure demonstrates the output formats of the `pcs resource defaults config`{.literal} command after configuring default values for a resource.

**Procedure**

1.  Set default values for an `ocf:pacemaker:pgsql`{.literal} resource:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource defaults set create id=set-1 score=100 meta resource-stickiness=10 rule resource ocf:pacemaker:pgsql
    ```

2.  Display the configured resource default values in plain text:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource defaults config
    Meta Attrs: build-resource-defaults
      resource-stickiness=1
    Meta Attrs: set-1 score=100
      resource-stickiness=10
      Rule: boolean-op=and score=INFINITY
        Expression: resource ocf:pacemaker:pgsql
    ```

3.  Display the `pcs resource defaults`{.literal} commands created from the current cluster defaults configuration:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource defaults config --output-format=cmd
    ```

    ``` {.language-plaintext tabindex="-1"}
    pcs -- resource defaults set create id=build-resource-defaults \
      meta resource-stickiness=1;
    pcs -- resource defaults set create id=set-1 score=100 \
      meta resource-stickiness=10 \
      rule 'resource ocf:pacemaker:pgsql'
    ```

4.  Display the configured resource default values in JSON format:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource defaults config --output-format=json
    ```

    ``` {.language-plaintext tabindex="-1"}
    {"instance_attributes": [], "meta_attributes": [{"id": "build-resource-defaults", "options": {}, "rule": null, "nvpairs": [{"id": "build-resource-stickiness", "name": "resource-stickiness", "value": "1"}]}, {"id": "set-1", "options": {"score": "100"}, "rule": {"id": "set-1-rule", "type": "RULE", "in_effect": "UNKNOWN", "options": {"boolean-op": "and", "score": "INFINITY"}, "date_spec": null, "duration": null, "expressions": [{"id": "set-1-rule-rsc-ocf-pacemaker-pgsql", "type": "RSC_EXPRESSION", "in_effect": "UNKNOWN", "options": {"class": "ocf", "provider": "pacemaker", "type": "pgsql"}, "date_spec": null, "duration": null, "expressions": [], "as_string": "resource ocf:pacemaker:pgsql"}], "as_string": "resource ocf:pacemaker:pgsql"}, "nvpairs": [{"id": "set-1-resource-stickiness", "name": "resource-stickiness", "value": "10"}]}]}
    ```

### [11.11. Configuring resource groups](#creating-resource-groups) {#configuring-resource-groups .title}

One of the most common elements of a cluster is a set of resources that need to be located together, start sequentially, and stop in the reverse order. To simplify this configuration, Pacemaker supports the concept of resource groups.

**Creating a resource group**

You can create a resource group with the following command, specifying the resources to include in the group. If the group does not exist, this command creates the group. If the group exists, this command adds additional resources to the group. The resources will start in the order you specify them with this command, and will stop in the reverse order of their starting order.

``` {.language-plaintext tabindex="-1"}
# pcs resource group add group_name resource_id [resource_id] ... [resource_id] [--before resource_id | --after resource_id]
```

You can use the `--before`{.literal .option} and `--after`{.literal .option} options of this command to specify the position of the added resources relative to a resource that already exists in the group.

You can also add a new resource to an existing group when you create the resource, using the following command. The resource you create is added to the group named *group_name*. If the group *group_name* does not exist, it will be created.

``` {.language-plaintext tabindex="-1"}
# pcs resource create resource_id [standard:[provider:]]type [resource_options] [op operation_action operation_options] --group group_name
```

There is no limit to the number of resources a group can contain. The fundamental properties of a group are as follows.

-   Resources are colocated within a group.
-   Resources are started in the order in which you specify them. If a resource in the group cannot run anywhere, then no resource specified after that resource is allowed to run.
-   Resources are stopped in the reverse order in which you specify them.

Additional properties of a group are as follows:

-   You can set the following options for a resource group, and they maintain the same meaning as when they are set for a single resource: `priority`{.literal}, `target-role`{.literal}, `is-managed`{.literal}. For information about resource meta options, see [Configuring resource meta options](#configuring-resource-meta-options "11.6. Configuring resource meta options").
-   Stickiness, the measure of how much a resource wants to stay where it is, is additive in groups. Every active resource of the group will contribute its stickiness value to the group's total. So if the default `resource-stickiness`{.literal} is 100, and a group has seven members, five of which are active, then the group as a whole will prefer its current location with a score of 500.

The following example creates a resource group named `shortcut`{.literal} that contains the existing resources `IPaddr`{.literal} and `Email`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs resource group add shortcut IPaddr Email
```

In this example:

-   The `IPaddr`{.literal} is started first, then `Email`{.literal}.
-   The `Email`{.literal} resource is stopped first, then `IPAddr`{.literal}.
-   If `IPaddr`{.literal} cannot run anywhere, neither can `Email`{.literal}.
-   If `Email`{.literal} cannot run anywhere, however, this does not affect `IPaddr`{.literal}.

**Removing a resource group**

You remove a resource from a group with the following command. If there are no remaining resources in the group, this command removes the group itself.

``` {.language-plaintext tabindex="-1"}
# pcs resource group remove group_name resource_id...
```

**Displaying resource groups**

The following command lists all currently configured resource groups.

``` {.language-plaintext tabindex="-1"}
# pcs resource group list
```

### [11.12. Displaying resource dependencies](#displaying-resource-dependencies) {#displaying-resource-dependencies .title}

You can display the relations between cluster resources in a tree structure.

``` {.language-plaintext tabindex="-1"}
# pcs resource relations resource [--full]
```

If the `--full`{.literal} option is used, the command displays additional information, including the constraint IDs and the resource types.

In the following example, there are 3 configured resources: C, D, and E.

``` {.language-plaintext tabindex="-1"}
# pcs constraint order start C then start D
```

``` {.language-plaintext tabindex="-1"}
Adding C D (kind: Mandatory) (Options: first-action=start then-action=start)
```

``` {.language-plaintext tabindex="-1"}
# pcs constraint order start D then start E
```

``` {.language-plaintext tabindex="-1"}
Adding D E (kind: Mandatory) (Options: first-action=start then-action=start)
```

``` {.language-plaintext tabindex="-1"}
# pcs resource relations C
```

``` {.language-plaintext tabindex="-1"}
C
`- order
   |  start C then start D
   `- D
      `- order
         |  start D then start E
         `- E
# *pcs resource relations D*
D
|- order
|  |  start C then start D
|  `- C
`- order
   |  start D then start E
   `- E
# pcs *resource relations E*
E
`- order
   |  start D then start E
   `- D
      `- order
         |  start C then start D
         `- C
```

In the following example, there are 2 configured resources: A and B. Resources A and B are part of resource group G.

``` {.language-plaintext tabindex="-1"}
# pcs resource relations A
```

``` {.language-plaintext tabindex="-1"}
A
`- outer resource
   `- G
      `- inner resource(s)
         |  members: A B
         `- B
# *pcs resource relations B*
B
`- outer resource
   `- G
      `- inner resource(s)
         |  members: A B
         `- A
# *pcs resource relations G*
G
`- inner resource(s)
   |  members: A B
   |- A
   `- B
```

### [11.13. Additional resources](#configuring-cluster-resources_1113-additional-resources) {#additional-resources-2 .title}

-   [Determining which nodes a resource can run on](#determining-which-node-a-resource-runs-on "Chapter 12. Determining which nodes a resource can run on")
-   [Determining the order in which cluster resources are run](#determining-resource-order "Chapter 13. Determining the order in which cluster resources are run")
-   [Colocating cluster resources](#colocating-cluster-resources "Chapter 14. Colocating cluster resources")

## [Chapter 12. Determining which nodes a resource can run on](#determining-which-node-a-resource-runs-on) {#chapter-12.-determining-which-nodes-a-resource-can-run-on .title}

Location constraints determine which nodes a resource can run on. You can configure location constraints to determine whether a resource will prefer or avoid a specified node.

In addition to location constraints, the node on which a resource runs is influenced by the `resource-stickiness`{.literal} value for that resource, which determines to what degree a resource prefers to remain on the node where it is currently running.

### [12.1. Configuring location constraints](#configuring-location-constraints) {#configuring-location-constraints .title}

You can configure a location constraint to control which nodes a cluster resource can run on in a cluster. You can use a location constraint to make a resource prefer a specific node or to prevent it from running on certain nodes.

#### [12.1.1. Configuring a basic location constraint](#configuring-a-basic-location-constraint) {#configuring-a-basic-location-constraint .title}

You can configure a basic location constraint to specify whether a resource prefers or avoids a node, with an optional `score`{.literal} value to indicate the relative degree of preference for the constraint.

**Procedure**

-   The following command creates a location constraint for a resource to prefer the specified node or nodes. Note that it is possible to create constraints on a particular resource for more than one node with a single command:

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint location rsc prefers node[=score] [node[=score]] ...
    ```

-   The following command creates a location constraint for a resource to avoid the specified node or nodes:

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint location rsc avoids node[=score] [node[=score]] ...
    ```

-   The following table summarizes the meanings of the basic options for configuring location constraints:

    +----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Field                | Description                                                                                                                                                                                                                                                                                                                                                                      |
    +:=====================+:=================================================================================================================================================================================================================================================================================================================================================================================+
    | `rsc`{.literal}      | A resource name                                                                                                                                                                                                                                                                                                                                                                  |
    +----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | `node`{.literal}     | A node's name                                                                                                                                                                                                                                                                                                                                                                    |
    +----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | `score`{.literal}    | Positive integer value to indicate the degree of preference for whether the given resource should prefer or avoid the given node. `INFINITY`{.literal} is the default `score`{.literal} value for a resource location constraint.                                                                                                                                                |
    |                      |                                                                                                                                                                                                                                                                                                                                                                                  |
    |                      | A value of `INFINITY`{.literal} for `score`{.literal} in a `pcs constraint location `{.literal}*`rsc`{.literal}*` prefers`{.literal} command indicates that the resource will prefer that node if the node is available, but does not prevent the resource from running on another node if the specified node is unavailable.                                                    |
    |                      |                                                                                                                                                                                                                                                                                                                                                                                  |
    |                      | A value of `INFINITY`{.literal} for `score`{.literal} in a `pcs constraint location `{.literal}*`rsc`{.literal}*` avoids`{.literal} command indicates that the resource will never run on that node, even if no other node is available. This is the equivalent of setting a `pcs constraint location add`{.literal} command with a score of `-INFINITY`{.literal}.              |
    |                      |                                                                                                                                                                                                                                                                                                                                                                                  |
    |                      | A numeric score (that is, not `INFINITY`{.literal}) means the constraint is optional, and will be honored unless some other factor outweighs it. For example, if the resource is already placed on a different node, and its `resource-stickiness`{.literal} score is higher than a `prefers`{.literal} location constraint's score, then the resource will be left where it is. |
    +----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    : Table 12.1. Location Constraint Options

    Show more

#### [12.1.2. Configuring a location constraint with regular expressions](#configuring-a-location-constraint-with-regular-expressions_general-fence) {#configuring-a-location-constraint-with-regular-expressions .title}

`pcs`{.literal} supports regular expressions in location constraints to match resource names. Use this feature to configure multiple location constraints with a single command.

**Procedure**

-   The following command creates a location constraint to specify that resources `dummy0`{.literal} to `dummy9`{.literal} prefer `node1`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint location 'regexp%dummy[0-9]' prefers node1
    ```

#### [12.1.3. Configuring a location constraint with extended regular expressions](#configuring-a-location-constraint-with-extended-regular-expressions) {#configuring-a-location-constraint-with-extended-regular-expressions .title}

Since Pacemaker uses POSIX extended regular expressions as documented at [9.4 Extended Regular Expressions](http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html#tag_09_04) section of the The Open Group Base Specifications Issue 7, you can specify the same constraint with the following command.

**Procedure**

-   To configure a location constraint with extended regular expressions:

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint location 'regexp%dummy[[:digit:]]' prefers node1
    ```

#### [12.1.4. Displaying location constraints](#displaying-location-constraints) {#displaying-location-constraints .title}

View location constraints to verify resource placement logic. You can organize the display by resource or node, filter for specific items, and include expired constraints or internal IDs for troubleshooting.

**Procedure**

-   To list all current location constraints:

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint location [config [resources [resource...]] | [nodes [node...]]] [--full]
    ```

    -   If `resources`{.literal} is specified, the command displays constraints per resource (default).
    -   If `nodes`{.literal} is specified, the command displays constraints per node.
    -   If you specify specific resources or nodes, the command displays only that information.

-   To display all current location, order, and colocation constraints, use the following command. To show the internal constraint IDS, specify the `--full`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint [config] [--full]
    ```

    By default, listing resource constraints does not display expired constraints. To include expired constraints in the listing, use the `--all`{.literal} option of the `pcs constraint`{.literal} command. This will list expired constraints, noting the constraints and their associated rules as `(expired)`{.literal} in the display.

-   To list the constraints that reference specific resources:

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint ref resource ...
    ```

### [12.2. Limiting resource discovery to a subset of nodes](#limiting-resource-discovery-to-a-subset-of-nodes) {#limiting-resource-discovery-to-a-subset-of-nodes .title}

Before Pacemaker starts a resource anywhere, it first runs a one-time monitor operation (often referred to as a \"probe\") on every node, to learn whether the resource is already running. This process of resource discovery can result in errors on nodes that are unable to run the monitor.

When configuring a location constraint on a node, you can use the `resource-discovery`{.literal} option of the `pcs constraint location`{.literal} command to indicate a preference for whether Pacemaker should perform resource discovery on this node for the specified resource. Limiting resource discovery to a subset of nodes the resource is physically capable of running on can significantly boost performance when a large set of nodes is present. When `pacemaker_remote`{.literal} is in use to expand the node count into the hundreds of nodes range, this option should be considered.

The following command shows the format for specifying the `resource-discovery`{.literal} option of the `pcs constraint location`{.literal} command. In this command, a positive value for *score* corresponds to a basic location constraint that configures a resource to prefer a node, while a negative value for *score* corresponds to a basic location\`constraint that configures a resource to avoid a node. As with basic location constraints, you can use regular expressions for resources with these constraints as well.

``` {.language-plaintext tabindex="-1"}
# pcs constraint location add id rsc node score [resource-discovery=option]
```

The following table summarizes the meanings of the basic parameters for configuring constraints for resource discovery.

+:---------------------------------------+:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `id`{.literal}                         | A user-chosen name for the constraint itself.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rsc`{.literal}                        | A resource name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `node`{.literal}                       | A node's name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `score`{.literal}                      | Integer value to indicate the degree of preference for whether the given resource should prefer or avoid the given node. A positive value for score corresponds to a basic location constraint that configures a resource to prefer a node, while a negative value for score corresponds to a basic location constraint that configures a resource to avoid a node.                                                                                                                                                  |
|                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                        | A value of `INFINITY`{.literal} for `score`{.literal} indicates that the resource will prefer that node if the node is available, but does not prevent the resource from running on another node if the specified node is unavailable. A value of `-INFINITY`{.literal} for `score`{.literal} indicates that the resource will never run on that node, even if no other node is available.                                                                                                                           |
|                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                        | A numeric score (that is, not `INFINITY`{.literal} or `-INFINITY`{.literal}) means the constraint is optional, and will be honored unless some other factor outweighs it. For example, if the resource is already placed on a different node, and its `resource-stickiness`{.literal} score is higher than a `prefers`{.literal} location constraint's score, then the resource will be left where it is.                                                                                                            |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `resource-discovery`{.literal} options | \* `always`{.literal} - Always perform resource discovery for the specified resource on this node. This is the default `resource-discovery`{.literal} value for a resource location constraint.                                                                                                                                                                                                                                                                                                                      |
|                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                        | \* `never`{.literal} - Never perform resource discovery for the specified resource on this node.                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                        | \* `exclusive`{.literal} - Perform resource discovery for the specified resource only on this node (and other nodes similarly marked as `exclusive`{.literal}). Multiple location constraints using `exclusive`{.literal} discovery for the same resource across different nodes creates a subset of nodes `resource-discovery`{.literal} is exclusive to. If a resource is marked for `exclusive`{.literal} discovery on one or more nodes, that resource is only allowed to be placed within that subset of nodes. |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 12.2. Resource discovery constraint parameters

Show more

Warning

Setting `resource-discovery`{.literal} to `never`{.literal} or `exclusive`{.literal} removes Pacemaker's ability to detect and stop unwanted instances of a service running where it is not supposed to be. It is up to the system administrator to ensure that the service can never be active on nodes without resource discovery (such as by leaving the relevant software uninstalled).

### [12.3. Configuring a location constraint strategy](#configuring-location-constraint-strategy) {#configuring-a-location-constraint-strategy .title}

When using location constraints, you can configure a general strategy for specifying which nodes a resource can run on.

-   Opt-in clusters - Configure a cluster in which, by default, no resource can run anywhere and then selectively enable allowed nodes for specific resources.
-   Opt-out clusters - Configure a cluster in which, by default, all resources can run anywhere and then create location constraints for resources that are not allowed to run on specific nodes.

Whether you should choose to configure your cluster as an opt-in or opt-out cluster depends on both your personal preference and the make-up of your cluster. If most of your resources can run on most of the nodes, then an opt-out arrangement is likely to result in a simpler configuration. On the other hand, if most resources can only run on a small subset of nodes an opt-in configuration might be simpler.

**Configuring an \"Opt-In\" cluster**

To create an opt-in cluster, set the `symmetric-cluster`{.literal} cluster property to `false`{.literal} to prevent resources from running anywhere by default.

``` {.language-plaintext tabindex="-1"}
# pcs property set symmetric-cluster=false
```

Enable nodes for individual resources. The following commands configure location constraints so that the resource `Webserver`{.literal} prefers node `example-1`{.literal}, the resource `Database`{.literal} prefers node `example-2`{.literal}, and both resources can fail over to node `example-3`{.literal} if their preferred node fails. When configuring location constraints for an opt-in cluster, setting a score of zero allows a resource to run on a node without indicating any preference to prefer or avoid the node.

``` {.language-plaintext tabindex="-1"}
# pcs constraint location Webserver prefers example-1=200
# pcs constraint location Webserver prefers example-3=0
# pcs constraint location Database prefers example-2=200
# pcs constraint location Database prefers example-3=0
```

**Configuring an \"Opt-Out\" cluster**

To create an opt-out cluster, set the `symmetric-cluster`{.literal} cluster property to `true`{.literal} to allow resources to run everywhere by default. This is the default configuration if `symmetric-cluster`{.literal} is not set explicitly.

``` {.language-plaintext tabindex="-1"}
# pcs property set symmetric-cluster=true
```

The following commands will then yield a configuration that is equivalent to the example in \"Configuring an \"Opt-In\" cluster\". Both resources can fail over to node `example-3`{.literal} if their preferred node fails, since every node has an implicit score of 0.

``` {.language-plaintext tabindex="-1"}
# pcs constraint location Webserver prefers example-1=200
# pcs constraint location Webserver avoids example-2=INFINITY
# pcs constraint location Database avoids example-1=INFINITY
# pcs constraint location Database prefers example-2=200
```

Note that it is not necessary to specify a score of INFINITY in these commands, since that is the default value for the score.

### [12.4. Configuring a resource to prefer its current node](#setting-resource-stickiness) {#configuring-a-resource-to-prefer-its-current-node .title}

Configure resource-stickiness to define a resource's preference for remaining on its current node. Pacemaker compares this value against other scores, such as location constraints, to prevent unnecessary migrations.

With a `resource-stickiness`{.literal} value of 0, a cluster may move resources as needed to balance resources across nodes. This may result in resources moving when unrelated resources start or stop. With a positive stickiness, resources have a preference to stay where they are, and move only if other circumstances outweigh the stickiness. This may result in newly-added nodes not getting any resources assigned to them without administrator intervention.

Newly-created clusters set the default value for `resource-stickiness`{.literal} to 1. This small value can easily be overridden by other constraints that you create, but it is enough to prevent Pacemaker from needlessly moving healthy resources around the cluster. If you prefer cluster behavior that results from a `resource-stickiness`{.literal} value of 0, you can change the `resource-stickiness`{.literal} default value to 0 with the following command:

**Example 12.1. Example command**

``` {.language-plaintext tabindex="-1"}
# pcs resource defaults update resource-stickiness=0
```

With a positive `resource-stickiness`{.literal} value, no resources will move to a newly-added node. If resource balancing is wanted at that point, you can temporarily set the `resource-stickiness`{.literal} value to 0.

Note that if a location constraint score is higher than the `resource-stickiness`{.literal} value, the cluster may still move a healthy resource to the node where the location constraint points.

**Additional resources**

-   [Configuring a node placement strategy](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_managing_high_availability_clusters/index#configuring-node-placement-strategy)
-   [Configuring resource meta options](#configuring-resource-meta-options "11.6. Configuring resource meta options")

## [Chapter 13. Determining the order in which cluster resources are run](#determining-resource-order) {#chapter-13.-determining-the-order-in-which-cluster-resources-are-run .title}

To determine the order in which the resources run, you must configure an ordering constraint.

The following shows the format for the command to configure an ordering constraint.

``` {.language-plaintext tabindex="-1"}
# pcs constraint order [action] resource_id then [action] resource_id [options]
```

For example the following command configures an ordering constraint to ensure that the resource `firstresource`{.literal} starts first, before the resource `secondresource`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs constraint order start firstresource then secondresource
```

The following table summarizes the properties and options for configuring ordering constraints.

+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                          | Description                                                                                                                                                                                                                                                                                                                                                                                 |
+:===============================+:============================================================================================================================================================================================================================================================================================================================================================================================+
| resource_id                    | The name of a resource on which an action is performed.                                                                                                                                                                                                                                                                                                                                     |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| action                         | The action to be ordered on the resource. Possible values of the *action* property are as follows:                                                                                                                                                                                                                                                                                          |
|                                |                                                                                                                                                                                                                                                                                                                                                                                             |
|                                | \* `start`{.literal} - Order start actions of the resource.                                                                                                                                                                                                                                                                                                                                 |
|                                |                                                                                                                                                                                                                                                                                                                                                                                             |
|                                | \* `stop`{.literal} - Order stop actions of the resource.                                                                                                                                                                                                                                                                                                                                   |
|                                |                                                                                                                                                                                                                                                                                                                                                                                             |
|                                | \* `promote`{.literal} - Promote the resource from an unpromoted resource to a promoted resource.                                                                                                                                                                                                                                                                                           |
|                                |                                                                                                                                                                                                                                                                                                                                                                                             |
|                                | \* `demote`{.literal} - Demote the resource from a promoted resource to an unpromoted resource.                                                                                                                                                                                                                                                                                             |
|                                |                                                                                                                                                                                                                                                                                                                                                                                             |
|                                | If no action is specified, the default action is `start`{.literal}.                                                                                                                                                                                                                                                                                                                         |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `kind`{.literal} option        | How to enforce the constraint. The possible values of the `kind`{.literal} option are as follows:                                                                                                                                                                                                                                                                                           |
|                                |                                                                                                                                                                                                                                                                                                                                                                                             |
|                                | \* `Optional`{.literal} - Only applies if both resources are executing the specified action.                                                                                                                                                                                                                                                                                                |
|                                |                                                                                                                                                                                                                                                                                                                                                                                             |
|                                | \* `Mandatory`{.literal} - Always enforce the constraint (default value). If the first resource you specified is stopping or cannot be started, the second resource you specified must be stopped.                                                                                                                                                                                          |
|                                |                                                                                                                                                                                                                                                                                                                                                                                             |
|                                | \* `Serialize`{.literal} - Ensure that no two stop/start actions occur concurrently for the resources you specify. The first and second resource you specify can start in either order, but one must complete starting before the other can be started. A typical use case is when resource startup puts a high load on the host.                                                           |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `symmetrical`{.literal} option | If true, the reverse of the constraint applies for the opposite action (for example, if B starts after A starts, then B stops before A stops). Ordering constraints for which `kind`{.literal} is `Serialize`{.literal} cannot be symmetrical. The default value is `true`{.literal} for `Mandatory`{.literal} and `Optional`{.literal} kinds, `false`{.literal} for `Serialize`{.literal}. |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 13.1. Properties of an Order Constraint

Show more

Displaying ordering constraints

:   The following command lists all current ordering constraints.

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint order [config]
    ```

    You can display all current location, order, and colocation constraints with the following command. To show the internal constraint IDS, specify the `--full`{.literal} option.

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint [config] [--full]
    ```

    By default, listing resource constraints does not display expired constraints. To include expired constraints in the listing, use the `--all`{.literal} option of the `pcs constraint`{.literal} command. This will list expired constraints, noting the constraints and their associated rules as `(expired)`{.literal} in the display.

    The following command lists the constraints that reference specific resources.

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint ref resource ...
    ```

Removing resources from an ordering constraint

:   Use the following command to remove resources from any ordering constraint.

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint order remove resource1 [resourceN]...
    ```

### [13.1. Configuring mandatory ordering](#configuring-mandatory-ordering) {#configuring-mandatory-ordering .title}

A mandatory ordering constraint ensures a resource waits for another to complete an action, such as `start`{.literal}, `stop`{.literal}, `promote`{.literal}, or `demote`{.literal}. For example, ordering resource A before B prevents B from starting until A succeeds. Set the `kind`{.literal} option to `Mandatory`{.literal} or use the default.

If the `symmetrical`{.literal} option is set to `true`{.literal} or left to default, the opposite actions will be ordered in reverse. The `start`{.literal} and `stop`{.literal} actions are opposites, and `demote`{.literal} and `promote`{.literal} are opposites. For example, a symmetrical \"promote A then start B\" ordering implies \"stop B then demote A\", which means that A cannot be demoted until and unless B successfully stops. A symmetrical ordering means that changes in A's state can cause actions to be scheduled for B. For example, given \"A then B\", if A restarts due to failure, B will be stopped first, then A will be stopped, then A will be started, then B will be started.

Note that the cluster reacts to each state change. If the first resource is restarted and is in a started state again before the second resource initiated a stop operation, the second resource will not need to be restarted.

### [13.2. Configuring advisory ordering](#configuring-advisory-ordering) {#configuring-advisory-ordering .title}

When the `kind=Optional`{.literal} option is specified for an ordering constraint, the constraint is considered optional and only applies if both resources are running the specified actions. Any change in state by the first resource you specify will have no effect on the second resource you specify.

**Procedure**

-   Configure an advisory ordering constraint for the resources named `VirtualIP`{.literal} and `dummy_resource`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint order VirtualIP then dummy_resource kind=Optional
    ```

### [13.3. Configuring ordered resource sets](#configuring-ordered-resource-sets) {#configuring-ordered-resource-sets .title}

If a configuration requires creating a set of colocated resources that start in order, such as resource A before B, and B before C, configure a resource group containing those resources.

There are some situations, however, where configuring the resources that need to start in a specified order as a resource group is not appropriate:

-   You may need to configure resources to start in order and the resources are not necessarily colocated.
-   You may have a resource C that must start after either resource A or B has started but there is no relationship between A and B.
-   You may have resources C and D that must start after both resources A and B have started, but there is no relationship between A and B or between C and D.

In these situations, you can create an ordering constraint on a set or sets of resources with the `pcs constraint order set`{.literal} command.

You can set the following options for a set of resources with the `pcs constraint order set`{.literal} command.

-   `sequential`{.literal}, which can be set to `true`{.literal} or `false`{.literal} to indicate whether the set of resources must be ordered relative to each other. The default value is `true`{.literal}.

    Setting `sequential`{.literal} to `false`{.literal} allows a set to be ordered relative to other sets in the ordering constraint, without its members being ordered relative to each other. Therefore, this option makes sense only if multiple sets are listed in the constraint; otherwise, the constraint has no effect.

-   `require-all`{.literal}, which can be set to `true`{.literal} or `false`{.literal} to indicate whether all of the resources in the set must be active before continuing. Setting `require-all`{.literal} to `false`{.literal} means that only one resource in the set needs to be started before continuing on to the next set. Setting `require-all`{.literal} to `false`{.literal} has no effect unless used in conjunction with unordered sets, which are sets for which `sequential`{.literal} is set to `false`{.literal}. The default value is `true`{.literal}.

-   `action`{.literal}, which can be set to `start`{.literal}, `promote`{.literal}, `demote`{.literal} or `stop`{.literal}.

-   `role`{.literal}, which can be set to `Stopped`{.literal}, `Started`{.literal}, `Promoted`{.literal}, or `Unpromoted`{.literal}.

You can set the following constraint options for a set of resources following the `setoptions`{.literal} parameter of the `pcs constraint order set`{.literal} command.

-   `id`{.literal}, to provide a name for the constraint you are defining.
-   `kind`{.literal}, which indicates how to enforce the constraint.
-   `symmetrical`{.literal}, to set whether the reverse of the constraint applies for the opposite action.

``` {.language-plaintext tabindex="-1"}
# pcs constraint order set resource1 resource2 [resourceN]... [options] [set resourceX resourceY ... [options]] [setoptions [constraint_options]]
```

If you have three resources named `D1`{.literal}, `D2`{.literal}, and `D3`{.literal}, the following command configures them as an ordered resource set.

``` {.language-plaintext tabindex="-1"}
# pcs constraint order set D1 D2 D3
```

If you have six resources named `A`{.literal}, `B`{.literal}, `C`{.literal}, `D`{.literal}, `E`{.literal}, and `F`{.literal}, this example configures an ordering constraint for the set of resources that will start as follows:

-   `A`{.literal} and `B`{.literal} start independently of each other
-   `C`{.literal} starts once either `A`{.literal} or `B`{.literal} has started
-   `D`{.literal} starts once `C`{.literal} has started
-   `E`{.literal} and `F`{.literal} start independently of each other once `D`{.literal} has started

Stopping the resources is not influenced by this constraint since `symmetrical=false`{.literal} is set.

``` {.language-plaintext tabindex="-1"}
# pcs constraint order set A B sequential=false require-all=false set C D set E F sequential=false setoptions symmetrical=false
```

**Additional resources**

-   [Determining the order in which cluster resources are run](#determining-resource-order "Chapter 13. Determining the order in which cluster resources are run")

### [13.4. Configuring startup order for resource dependencies not managed by Pacemaker](#configuring-startup-order-for-resource-dependencies-not-managed-by-pacemaker) {#configuring-startup-order-for-resource-dependencies-not-managed-by-pacemaker .title}

It is possible for a cluster to include resources with dependencies that are not themselves managed by the cluster. In this case, you must ensure that those dependencies are started before Pacemaker is started and stopped after Pacemaker is stopped.

You can configure your startup order to account for this situation by means of the `systemd`{.literal} `resource-agents-deps`{.literal} target. You can create a `systemd`{.literal} drop-in unit for this target and Pacemaker will order itself appropriately relative to this target.

#### [13.4.1. Configuring startup order for an external service](#configuring-startup-order-for-an-external-service) {#configuring-startup-order-for-an-external-service .title}

If a cluster includes a resource that depends on the external service `foo`{.literal} that is not managed by the cluster, you can configure a startup order for an external service.

**Procedure**

1.  Create the drop-in unit `/etc/systemd/system/resource-agents-deps.target.d/foo.conf`{.literal} that contains the following:

    ``` {.language-plaintext tabindex="-1"}
    [Unit]
    Requires=foo.service
    After=foo.service
    ```

2.  Run the `systemctl daemon-reload`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

#### [13.4.2. Configuring startup order for an external dependency](#configuring-startup-order-for-an-external-dependency) {#configuring-startup-order-for-an-external-dependency .title}

Cluster dependencies extend beyond services. For example, you can configure a dependency on mounting a file system at `/srv`{.literal}.

**Procedure**

1.  Ensure that `/srv`{.literal} is listed in the `/etc/fstab`{.literal} file. This will be converted automatically to the `systemd`{.literal} file `srv.mount`{.literal} at boot when the configuration of the system manager is reloaded. For more information, see the `systemd.mount`{.literal}(5) and the `systemd-fstab-generator`{.literal}(8) man pages on your system.

2.  To ensure that Pacemaker starts after the disk is mounted, create the drop-in unit `/etc/systemd/system/resource-agents-deps.target.d/srv.conf`{.literal} that contains the following:

    ``` {.language-plaintext tabindex="-1"}
    [Unit]
    Requires=srv.mount
    After=srv.mount
    ```

3.  Run the `systemctl daemon-reload`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

#### [13.4.3. Configuring startup order for remote block storage](#configuring-startup-order-for-remote-block-storage) {#configuring-startup-order-for-remote-block-storage .title}

If an LVM volume group used by a Pacemaker cluster contains physical volumes on remote block storage, such as an iSCSI target, configure a `systemd resource-agents-deps`{.literal} target and a `systemd`{.literal} drop-in unit to ensure that the service starts before Pacemaker.

The following procedure configures `blk-availability.service`{.literal} as a dependency. The `blk-availability.service`{.literal} service is a wrapper that includes `iscsi.service`{.literal}, among other services. If your deployment requires it, you could configure `iscsi.service`{.literal} (for iSCSI only) or `remote-fs.target`{.literal} as the dependency instead of `blk-availability`{.literal}.

**Procedure**

1.  Create the drop-in unit `/etc/systemd/system/resource-agents-deps.target.d/blk-availability.conf`{.literal} that contains the following:

    ``` {.language-plaintext tabindex="-1"}
    [Unit]
    Requires=blk-availability.service
    After=blk-availability.service
    ```

2.  Run the `systemctl daemon-reload`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

## [Chapter 14. Colocating cluster resources](#colocating-cluster-resources) {#chapter-14.-colocating-cluster-resources .title}

To specify that the location of one resource depends on the location of another resource, you configure a colocation constraint.

There is an important side effect of creating a colocation constraint between two resources: it affects the order in which resources are assigned to a node. This is because you cannot place resource A relative to resource B unless you know where resource B is. So when you are creating colocation constraints, it is important to consider whether you should colocate resource A with resource B or resource B with resource A.

Another thing to keep in mind when creating colocation constraints is that, assuming resource A is colocated with resource B, the cluster will also take into account resource A's preferences when deciding which node to choose for resource B.

The following command creates a colocation constraint:

``` {.language-plaintext tabindex="-1"}
# pcs constraint colocation add [promoted|unpromoted] source_resource with [promoted|unpromoted] target_resource [score] [options]
```

The following table summarizes the properties and options for configuring colocation constraints:

Parameters of a colocation constraint

:   

+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter                    | Description                                                                                                                                                                                                                                                                                                                                                                                                            |
+:=============================+:=======================================================================================================================================================================================================================================================================================================================================================================================================================+
| source_resource              | The colocation source. If the constraint cannot be satisfied, the cluster may decide not to allow the resource to run at all.                                                                                                                                                                                                                                                                                          |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| target_resource              | The colocation target. The cluster will decide where to put this resource first and then decide where to put the source resource.                                                                                                                                                                                                                                                                                      |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| score                        | Positive values indicate the resource should run on the same node. Negative values indicate the resources should not run on the same node. A value of +`INFINITY`{.literal}, the default value, indicates that the *source_resource* must run on the same node as the *target_resource*. A value of -`INFINITY`{.literal} indicates that the *source_resource* must not run on the same node as the *target_resource*. |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `influence`{.literal} option | Determines whether the cluster will move both the primary resource (*source_resource*) and dependent resources (*target_resource)* to another node when the dependent resource reaches its migration threshold for failure, or whether the cluster will leave the dependent resource offline without causing a service switch.                                                                                         |
|                              |                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                              | The `influence`{.literal} colocation constraint option can have a value of `true`{.literal} or `false`{.literal}. The default value for this option is determined by the value of the dependent resource's `critical`{.literal} resource meta option, which has a default value of `true`{.literal}.                                                                                                                   |
|                              |                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                              | When this option has a value of `true`{.literal}, Pacemaker will attempt to keep both the primary and dependent resource active. If the dependent resource reaches its migration threshold for failures, both resources will move to another node if possible.                                                                                                                                                         |
|                              |                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                              | When this option has a value of `false`{.literal}, Pacemaker will avoid moving the primary resource as a result of the status of the dependent resource. In this case, if the dependent resource reaches its migration threshold for failures, it will stop if the primary resource is active and can remain on its current node.                                                                                      |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Show more

Displaying colocation constraints

:   The following command lists all current colocation constraints.

    ``` {.language-plaintext tabindex="-1"}
    pcs constraint colocation [config]
    ```

    You can display all current location, order, and colocation constraints with the following command. To show the internal constraint IDS, specify the `--full`{.literal} option.

    ``` {.language-plaintext tabindex="-1"}
    pcs constraint [config] [--full]
    ```

    By default, listing resource constraints does not display expired constraints. To include expired constraints in the listing, use the `--all`{.literal} option of the `pcs constraint`{.literal} command. This will list expired constraints, noting the constraints and their associated rules as `(expired)`{.literal} in the display.

    The following command lists the constraints that reference specific resources:

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint ref resource ...
    ```

### [14.1. Specifying mandatory placement of resources](#specifying-mandatory-placement) {#specifying-mandatory-placement-of-resources .title}

Mandatory placement occurs any time the constraint's score is `+INFINITY`{.literal} or `-INFINITY`{.literal}. In such cases, if the constraint cannot be satisfied, then the *source_resource* is not permitted to run. For `score=INFINITY`{.literal}, this includes cases where the *target_resource* is not active.

**Procedure**

-   If you need `myresource1`{.literal} to always run on the same machine as `myresource2`{.literal}, you would add the following constraint:

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint colocation add myresource1 with myresource2 score=INFINITY
    ```

    Because `INFINITY`{.literal} was used, if `myresource2`{.literal} cannot run on any of the cluster nodes (for whatever reason) then `myresource1`{.literal} will not be allowed to run.

-   Alternatively, you may want to configure the opposite, a cluster in which `myresource1`{.literal} cannot run on the same machine as `myresource2`{.literal}. In this case use `score=-INFINITY`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint colocation add myresource1 with myresource2 score=-INFINITY
    ```

    Again, by specifying `-INFINITY`{.literal}, the constraint is binding. So if the only place left to run is where `myresource2`{.literal} already is, then `myresource1`{.literal} may not run anywhere.

### [14.2. Specifying advisory placement of resources](#specifying-advisory-placement) {#specifying-advisory-placement-of-resources .title}

Advisory placement of resources indicates a preference rather than a mandatory rule. For constraints with scores greater than `-INFINITY`{.literal} and less than `INFINITY`{.literal}, the cluster attempts to honor the preference, but can ignore it to avoid stopping cluster resources.

### [14.3. Colocating sets of resources](#colocating-resource-sets) {#colocating-sets-of-resources .title}

If a configuration requires creating a set of colocated resources that start in order, configure a resource group containing those resources. However, in some situations, configuring colocated resources as a resource group is not appropriate.

These situation are:

-   You may need to colocate a set of resources but the resources do not necessarily need to start in order.
-   You may have a resource C that must be colocated with either resource A or B, but there is no relationship between A and B.
-   You may have resources C and D that must be colocated with both resources A and B, but there is no relationship between A and B or between C and D.

In these situations, you can create a colocation constraint on a set or sets of resources with the `pcs constraint colocation set`{.literal} command.

You can set the following options for a set of resources with the `pcs constraint colocation set`{.literal} command.

-   `sequential`{.literal}, which can be set to `true`{.literal} or `false`{.literal} to indicate whether the members of the set must be colocated with each other.

    Setting `sequential`{.literal} to `false`{.literal} allows the members of this set to be colocated with another set listed later in the constraint, regardless of which members of this set are active. Therefore, this option makes sense only if another set is listed after this one in the constraint; otherwise, the constraint has no effect.

-   `role`{.literal}, which can be set to `Stopped`{.literal}, `Started`{.literal}, `Promoted`{.literal}, or `Unpromoted`{.literal}.

You can set the following constraint option for a set of resources following the `setoptions`{.literal} parameter of the `pcs constraint colocation set`{.literal} command.

-   `id`{.literal}, to provide a name for the constraint you are defining.
-   `score`{.literal}, to indicate the degree of preference for this constraint. For information about this option, see the \"Location Constraint Options\" table in [Configuring Location Constraints](#configuring-location-constraints "12.1. Configuring location constraints")

When listing members of a set, each member is colocated with the one before it. For example, \"set A B\" means \"B is colocated with A\". However, when listing multiple sets, each set is colocated with the one after it. For example, \"set C D sequential=false set A B\" means \"set C D (where C and D have no relation between each other) is colocated with set A B (where B is colocated with A)\".

The following command creates a colocation constraint on a set or sets of resources:

``` {.language-plaintext tabindex="-1"}
# pcs constraint colocation set resource1 resource2] [resourceN]... [options] [set resourceX resourceY] ... [options]] [setoptions [constraint_options]]
```

Use the following command to remove colocation constraints with *source_resource*:

``` {.language-plaintext tabindex="-1"}
# pcs constraint colocation remove source_resource target_resource
```

## [Chapter 15. Exporting resource constraints as pcs commands](#exporting-constraints) {#chapter-15.-exporting-resource-constraints-as-pcs-commands .title}

You can display the `pcs`{.literal} commands that can be used to re-create configured resource constraints on a different system using the `--output-format=cmd`{.literal} option of the `pcs constraint`{.literal} command.

The following example procedures creates two resources, configures three resource constraints, and displays the xi\`pcs\` commands you can use to re-create the constraints on a different system.

**Procedure**

1.  Create an `IPaddr2`{.literal} resource named `VirtualIP`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create VirtualIP IPaddr2 ip=198.51.100.3 cidr_netmask=24
    ```

    ``` {.language-plaintext tabindex="-1"}
    Assumed agent name 'ocf:heartbeat:IPaddr2' (deduced from 'IPaddr2')
    ```

2.  Create an `apache`{.literal} resource named `Website`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create Website apache configfile="/etc/httpd/conf/httpd.conf" statusurl="http://127.0.0.1/server-status"
    ```

    ``` {.language-plaintext tabindex="-1"}
    Assumed agent name 'ocf:heartbeat:apache' (deduced from 'apache')
    ```

3.  Configure a location constraint for the `Website`{.literal} resource.

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint location Website avoids node1
    ```

4.  Configure a colocation constraint for the `Website`{.literal} and `VirtualIP`{.literal} resources.

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint colocation add Website with VirtualIP
    ```

5.  Configure an order constraint for the `Website`{.literal} and `VirtualIP`{.literal} resources.

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint order VirtualIP then Website
    ```

    ``` {.language-plaintext tabindex="-1"}
    Adding VirtualIP Website (kind: Mandatory) (Options: first-action=start then-action=start)
    ```

6.  Display the `pcs`{.literal} commands you can use to re-create the constraints on a different system.

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint --output-format=cmd
    ```

    ``` {.language-plaintext tabindex="-1"}
    pcs -- constraint location add location-Website-node1--INFINITY resource%Website node1 -INFINITY;
    pcs -- constraint colocation add Website with VirtualIP INFINITY \
      id=colocation-Website-VirtualIP-INFINITY;
    pcs -- constraint order start VirtualIP then start Website \
      id=order-VirtualIP-Website-mandatory
    ```

## [Chapter 16. Configuring node-specific values using node attributes](#node-attributes) {#chapter-16.-configuring-node-specific-values-using-node-attributes .title}

Pacemaker supports configuring node-specific values using *node attributes* to track node information. For example, use node attributes to specify how much RAM and disk space a node has, which operating system it runs, or its location in a server room rack.

There are three primary uses for node attributes:

-   In Pacemaker rules for the cluster configuration

    For example, you can set a node attribute named `department`{.literal} to `accounting`{.literal} or `IT`{.literal} on each node, depending on which department that node is dedicated to. You can then configure a location rule to ensure that an accounting database runs only on servers where `department`{.literal} is set to `accounting`{.literal}.

    For information about node attribute expressions in Pacemaker rules, see [Pacemaker rules](#pacemaker-rules "17.1. Pacemaker rules").

-   In resource agents for the specific resource requirements

    For example, a database resource agent can use a node attribute to track the latest replication position for use in a `promote`{.literal} action.

-   In external scripts for use outside Pacemaker

    For example, you can set `data-center`{.literal} and `rack`{.literal} attributes for each node, for use by an external inventory script.

**Defining a node attribute**

You define a node attribute with the pcs node attribute command. A node attribute has a name and a value, and can have a distinct value for each node.

When you define a node attribute with the `pcs node attribute`{.literal} command, the node attribute is *permanent*. Permanent node attributes keep their values even when the cluster restarts on a node.

Note

You can define a *transient node* attribute, which is kept in the CIB's status section, and does not remain when the cluster stops on the node. For information about defining transient node attributes, see the `crm_attribute`{.literal}(8) and `attrd_updater`{.literal}(8) man pages on your system.

-   Run the following commands to define a node attribute with the name `rack`{.literal} for `node1`{.literal} and `node2`{.literal}, setting a value of 1 for the `rack`{.literal} attribute of `node1`{.literal} and a value of 2 for the `rack`{.literal} attribute of `node2`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # pcs node attribute node1 rack=1
    # pcs node attribute node2 rack=2
    ```

**Displaying node attributes as pcs commands**

You can export node attributes as a series of `pcs`{.literal} commands by using the `--output-format=cmd`{.literal} option. This is useful for scripting, automation, or replicating the same configuration on a different system.

Note

You can display the configured node attributes in one of three formats:

-   `text`{.literal}: Displays the output in plain text. This is the default format.
-   `json`{.literal}: Displays the output in a machine-readable JSON format, which is useful for scripting and automation.
-   `cmd`{.literal}: Displays the output as a series of `pcs`{.literal} commands, which you can use to recreate the same node attributes on a different system.

-   To display the configured node attributes as a series of `pcs`{.literal} commands:

    ``` {.language-plaintext tabindex="-1"}
    # pcs node attribute --output-format=cmd
    ```

    **Example output**

    ``` {.language-plaintext tabindex="-1"}
    pcs node attribute node1 location=rack1
    pcs node attribute node2 location=rack2
    ```

## [Chapter 17. Determining resource location with rules](#determining-resource-location-with-rules) {#chapter-17.-determining-resource-location-with-rules .title}

For more complicated location constraints, you can use Pacemaker rules to determine a resource's location.

### [17.1. Pacemaker rules](#pacemaker-rules) {#pacemaker-rules .title}

Pacemaker rules can be used to make your configuration more dynamic. One use of rules might be to assign machines to different processing groups, such as using a node attribute, based on time and to then use that attribute when creating location constraints.

Each rule can contain a number of expressions, date-expressions and even other rules. The results of the expressions are combined based on the rule's `boolean-op`{.literal} field to determine if the rule ultimately evaluates to `true`{.literal} or `false`{.literal}. What happens next depends on the context in which the rule is being used.

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                             | Description                                                                                                                                                                                                                                                                                                                          |
+:==================================+:=====================================================================================================================================================================================================================================================================================================================================+
| `role`{.literal}                  | Limits the rule to apply only when the resource is in that role. Allowed values: `Started`{.literal}, `Unpromoted,`{.literal} and `Promoted`{.literal}. NOTE: A rule with `role="Promoted"`{.literal} cannot determine the initial location of a clone instance. It will only affect which of the active instances will be promoted. |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `score`{.literal}                 | The score to apply if the rule evaluates to `true`{.literal}. Limited to use in rules that are part of location constraints.                                                                                                                                                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `score-attribute`{.literal}       | The node attribute to look up and use as a score if the rule evaluates to `true`{.literal}. Limited to use in rules that are part of location constraints.                                                                                                                                                                           |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `boolean-op`{.literal}            | How to combine the result of multiple expression objects. Allowed values: `and`{.literal} and `or`{.literal}. The default value is `and`{.literal}.                                                                                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 17.1. Properties of a Rule

Show more

#### [17.1.1. Node attribute expressions](#node_attribute_expressions) {#node-attribute-expressions .title}

Node attribute expressions are used to control a resource based on the attributes defined by a node or nodes. For general information about node attributes, see [Configuring node-specific values using node attributes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_managing_high_availability_clusters/index#node-attributes).

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                             | Description                                                                                                                                                                              |
+:==================================+:=========================================================================================================================================================================================+
| `attribute`{.literal}             | The node attribute to test                                                                                                                                                               |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `type`{.literal}                  | Determines how the value(s) should be tested. Allowed values: `string`{.literal}, `integer`{.literal}, `number`{.literal}, `version`{.literal}. The default value is `string`{.literal}. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `operation`{.literal}             | The comparison to perform. Allowed values:                                                                                                                                               |
|                                   |                                                                                                                                                                                          |
|                                   | \* `lt`{.literal} - True if the node attribute's value is less than `value`{.literal}                                                                                                    |
|                                   |                                                                                                                                                                                          |
|                                   | \* `gt`{.literal} - True if the node attribute's value is greater than `value`{.literal}                                                                                                 |
|                                   |                                                                                                                                                                                          |
|                                   | \* `lte`{.literal} - True if the node attribute's value is less than or equal to `value`{.literal}                                                                                       |
|                                   |                                                                                                                                                                                          |
|                                   | \* `gte`{.literal} - True if the node attribute's value is greater than or equal to `value`{.literal}                                                                                    |
|                                   |                                                                                                                                                                                          |
|                                   | \* `eq`{.literal} - True if the node attribute's value is equal to `value`{.literal}                                                                                                     |
|                                   |                                                                                                                                                                                          |
|                                   | \* `ne`{.literal} - True if the node attribute's value is not equal to `value`{.literal}                                                                                                 |
|                                   |                                                                                                                                                                                          |
|                                   | \* `defined`{.literal} - True if the node has the named attribute                                                                                                                        |
|                                   |                                                                                                                                                                                          |
|                                   | \* `not_defined`{.literal} - True if the node does not have the named attribute                                                                                                          |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `value`{.literal}                 | User supplied value for comparison (required unless `operation`{.literal} is `defined`{.literal} or `not_defined`{.literal})                                                             |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 17.2. Properties of an Expression

Show more

In addition to any attributes added by the administrator, the cluster defines special, built-in node attributes for each node that can also be used, as described in the following table.

+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                              | Description                                                                                                                                                                                                                                                                                                                |
+:==================================+:===========================================================================================================================================================================================================================================================================================================================+
| `#uname`{.literal}                | Node name                                                                                                                                                                                                                                                                                                                  |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `#id`{.literal}                   | Node ID                                                                                                                                                                                                                                                                                                                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `#kind`{.literal}                 | Node type. Possible values are `cluster`{.literal}, `remote`{.literal}, and `container`{.literal}. The value of `kind`{.literal} is `remote`{.literal} for Pacemaker Remote nodes created with the `ocf:pacemaker:remote`{.literal} resource, and `container`{.literal} for Pacemaker Remote guest nodes and bundle nodes. |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `#is_dc`{.literal}                | `true`{.literal} if this node is a Designated Controller (DC), `false`{.literal} otherwise                                                                                                                                                                                                                                 |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `#cluster_name`{.literal}         | The value of the `cluster-name`{.literal} cluster property, if set                                                                                                                                                                                                                                                         |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `#site_name`{.literal}            | The value of the `site-name`{.literal} node attribute, if set, otherwise identical to `#cluster-name`{.literal}                                                                                                                                                                                                            |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `#role`{.literal}                 | The role the relevant promotable clone has on this node. Valid only within a rule for a location constraint for a promotable clone.                                                                                                                                                                                        |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 17.3. Built-in Node Attributes

Show more

#### [17.1.2. Time/date based expressions](#time_date_based_expressions) {#timedate-based-expressions .title}

Date expressions are used to control a resource or cluster option based on the current date/time. They can contain an optional date specification.

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Field                             | Description                                                                                                                             |
+:==================================+:========================================================================================================================================+
| `start`{.literal}                 | A date/time conforming to the ISO8601 specification.                                                                                    |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| `end`{.literal}                   | A date/time conforming to the ISO8601 specification.                                                                                    |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| `operation`{.literal}             | Compares the current date/time with the start or the end date or both the start and end date, depending on the context. Allowed values: |
|                                   |                                                                                                                                         |
|                                   | \* `gt`{.literal} - True if the current date/time is after `start`{.literal}                                                            |
|                                   |                                                                                                                                         |
|                                   | \* `lt`{.literal} - True if the current date/time is before `end`{.literal}                                                             |
|                                   |                                                                                                                                         |
|                                   | \* `in_range`{.literal} - True if the current date/time is after `start`{.literal} and before `end`{.literal}                           |
|                                   |                                                                                                                                         |
|                                   | \* `date-spec`{.literal} - performs a cron-like comparison to the current date/time                                                     |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

: Table 17.4. Properties of a Date Expression

Show more

#### [17.1.3. Date specifications](#date_specifications) {#date-specifications .title}

Date specifications are used to create cron-like expressions relating to time. Each field can contain a single number or a single range. Instead of defaulting to zero, any field not supplied is ignored.

For example, `monthdays="1"`{.literal} matches the first day of every month and `hours="09-17"`{.literal} matches the hours between 9 am and 5 pm (inclusive). However, you cannot specify `weekdays="1,2"`{.literal} or `weekdays="1-2,5-6"`{.literal} since they contain multiple ranges.

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                             | Description                                                                                                                                               |
+:==================================+:==========================================================================================================================================================+
| `id`{.literal}                    | A unique name for the date                                                                                                                                |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| `seconds`{.literal}               | Allowed values: 0-59                                                                                                                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| `minutes`{.literal}               | Allowed values: 0-59                                                                                                                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| `hours`{.literal}                 | Allowed values: 0-23                                                                                                                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| `monthdays`{.literal}             | Allowed values: 0-31 (depending on month and year)                                                                                                        |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| `weekdays`{.literal}              | Allowed values: 1-7 (1=Monday, 7=Sunday)                                                                                                                  |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| `yeardays`{.literal}              | Allowed values: 1-366 (depending on the year)                                                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| `months`{.literal}                | Allowed values: 1-12                                                                                                                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| `weeks`{.literal}                 | Allowed values: 1-53 (depending on `weekyear`{.literal})                                                                                                  |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| `years`{.literal}                 | Year according the Gregorian calendar                                                                                                                     |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| `weekyears`{.literal}             | May differ from Gregorian years; for example, `2005-001 Ordinal`{.literal} is also `2005-01-01 Gregorian`{.literal} is also `2004-W53-6 Weekly`{.literal} |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 17.5. Properties of a Date Specification

Show more

### [17.2. Configuring a Pacemaker location constraint using rules](#configuring-constraint-using-rules) {#configuring-a-pacemaker-location-constraint-using-rules .title}

Configure location constraints with rules to determine resource placement based on complex conditions, such as time, date, or node attributes. You can combine multiple expressions to create sophisticated placement logic.

``` {.language-plaintext tabindex="-1"}
# pcs constraint location rsc rule[resource-discovery=option] [role=promoted|unpromoted] [score=score | score-attribute=attribute] expression
```

-   If `score`{.literal} is omitted, it defaults to INFINITY.
-   When using rules to configure location constraints, the value of `score`{.literal} can be positive or negative, with a positive value indicating \"prefers\" and a negative value indicating \"avoids\".
-   If `resource-discovery`{.literal} is omitted, it defaults to `always`{.literal}. For information about the `resource-discovery`{.literal} option, see [Limiting resource discovery to a subset of nodes](#limiting-resource-discovery-to-a-subset-of-nodes "12.2. Limiting resource discovery to a subset of nodes").
-   As with basic location constraints, you can use regular expressions for resources with these constraints as well.

**The *expression* option in Pacemaker rules**

The *expression* option can be one of the following where *duration_options* and *date_spec_options* are: hours, months, weeks, and years as described in the \"Properties of a Date Specification\" table in [Pacemaker rules](#pacemaker-rules "17.1. Pacemaker rules").

-   `defined|not_defined `{.literal}*`attribute`{.literal}*
-   *`attribute`{.literal}*` lt|gt|lte|gte|eq|ne [string|integer|number|version] `{.literal}*`value`{.literal}*
-   `date gt|lt `{.literal}*`date`{.literal}*
-   `date in_range `{.literal}*`date`{.literal}*` to `{.literal}*`date`{.literal}*
-   `date in_range `{.literal}*`date`{.literal}*` to duration `{.literal}*`duration_options`{.literal}*` …​`{.literal}
-   `date-spec `{.literal}*`date_spec_options`{.literal}*
-   *`expression`{.literal}*` and|or `{.literal}*`expression`{.literal}*
-   `(`{.literal}*`expression`{.literal}*`)`{.literal}

**Durations in Pacemaker rules**

Note that durations are an alternative way to specify an end for `in_range`{.literal} operations by means of calculations. For example, you can specify a duration of 19 months. The supported values for `duration`{.literal} options are `seconds`{.literal}, `minutes`{.literal}, `hours`{.literal}, `days`{.literal}, `weeks`{.literal}, `months`{.literal}, and `years`{.literal}.

The following location constraint configures an expression that is true if now is any time in the year 2018.

``` {.language-plaintext tabindex="-1"}
# pcs constraint location Webserver rule score=INFINITY date-spec years=2018
```

The following command configures an expression that is true from 9 am to 5 pm, Monday through Friday. Note that the hours value of 16 matches up to 16:59:59, as the numeric value (hour) still matches.

``` {.language-plaintext tabindex="-1"}
# pcs constraint location Webserver rule score=INFINITY date-spec hours="9-16" weekdays="1-5"
```

The following command configures an expression that is true on Friday the thirteenth.

``` {.language-plaintext tabindex="-1"}
# pcs constraint location Webserver rule date-spec weekdays=5 monthdays=13
```

### [17.3. Removing a Pacemaker rule](#removing-pacemaker-rule) {#removing-a-pacemaker-rule .title}

You can remove a Pacemaker rule. If the rule that you are removing is the last rule in its constraint, the constraint will be removed.

**Procedure**

-   Remove a Pacemaker rule:

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint rule remove rule_id
    ```

## [Chapter 18. Managing cluster resources](#managing-cluster-resources) {#chapter-18.-managing-cluster-resources .title}

There are a variety of commands you can use to display, modify, and administer cluster resources.

### [18.1. Exporting cluster resources as pcs commands](#exporting-resources) {#exporting-cluster-resources-as-pcs-commands .title}

You can display the `pcs`{.literal} commands that can be used to re-create configured cluster resources on a different system using the `--output-format=cmd`{.literal} option of the `pcs resource config`{.literal} command.

The following example procedure creates four resources for an active/passive Apache HTTP server in a Red Hat high availability cluster and then displays the `pcs`{.literal} commands you can use to recreate those resources.

**Procedure**

1.  Create an `LVM-activate`{.literal} resource.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create my_lvm ocf:heartbeat:LVM-activate vgname=my_vg vg_access_mode=system_id --group apachegroup
    ```

2.  Create a `Filesystem`{.literal} resource.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create my_fs Filesystem device="/dev/my_vg/my_lv" directory="/var/www" fstype="xfs" --group apachegroup
    ```

3.  Create an `IPaddr2`{.literal} resource.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create VirtualIP IPaddr2 ip=198.51.100.3 cidr_netmask=24 --group apachegroup
    ```

4.  Create an `Apache`{.literal} resource.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create Website apache configfile="/etc/httpd/conf/httpd.conf" statusurl="http://127.0.0.1/server-status" --group apachegroup
    ```

5.  Display the `pcs`{.literal} commands you can use to re-create the four resources you created on a different system.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource config --output-format=cmd
    ```

    ``` {.language-plaintext tabindex="-1"}
    pcs resource create --no-default-ops --force -- my_lvm ocf:heartbeat:LVM-activate \
      vg_access_mode=system_id vgname=my_vg \
      op \
        monitor interval=30s id=my_lvm-monitor-interval-30s timeout=90s \
        start interval=0s id=my_lvm-start-interval-0s timeout=90s \
        stop interval=0s id=my_lvm-stop-interval-0s timeout=90s;
    pcs resource create --no-default-ops --force -- my_fs ocf:heartbeat:Filesystem \
      device=/dev/my_vg/my_lv directory=/var/www fstype=xfs \
      op \
        monitor interval=20s id=my_fs-monitor-interval-20s timeout=40s \
        start interval=0s id=my_fs-start-interval-0s timeout=60s \
        stop interval=0s id=my_fs-stop-interval-0s timeout=60s;
    pcs resource create --no-default-ops --force -- VirtualIP ocf:heartbeat:IPaddr2 \
      cidr_netmask=24 ip=198.51.100.3 \
      op \
        monitor interval=10s id=VirtualIP-monitor-interval-10s timeout=20s \
        start interval=0s id=VirtualIP-start-interval-0s timeout=20s \
        stop interval=0s id=VirtualIP-stop-interval-0s timeout=20s;
    pcs resource create --no-default-ops --force -- Website ocf:heartbeat:apache \
      configfile=/etc/httpd/conf/httpd.conf statusurl=http://127.0.0.1/server-status \
      op \
        monitor interval=10s id=Website-monitor-interval-10s timeout=20s \
        start interval=0s id=Website-start-interval-0s timeout=40s \
        stop interval=0s id=Website-stop-interval-0s timeout=60s;
    pcs resource group add apachegroup \
      my_lvm my_fs VirtualIP Website
    ```

6.  Display the `pcs`{.literal} command you can use to re-create only the `IPaddr2`{.literal} resource. To display only one configured resource, specify the resource ID for that resource.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource config VirtualIP --output-format=cmd
    ```

    ``` {.language-plaintext tabindex="-1"}
    pcs resource create --no-default-ops --force -- VirtualIP ocf:heartbeat:IPaddr2 \
      cidr_netmask=24 ip=198.51.100.3 \
      op \
        monitor interval=10s id=VirtualIP-monitor-interval-10s timeout=20s \
        start interval=0s id=VirtualIP-start-interval-0s timeout=20s \
        stop interval=0s id=VirtualIP-stop-interval-0s timeout=20s
    ```

### [18.2. Modifying resource parameters](#modify-resource-parameters) {#modifying-resource-parameters .title}

To modify the parameters of a configured cluster resource, use the `pcs resource update`{.literal} command.

To modify the options or parameters of a cluster resource, use the following syntax:

``` {.language-plaintext tabindex="-1"}
# pcs resource update resource_id [resource_options]
```

Note

When updating a resource operation with the `pcs resource update`{.literal} command, options that are not explicitly specified reset to their default values.

The following example procedure modifies the `ip`{.literal} parameter of the `VirtualIP`{.literal} resource.

**Procedure**

1.  Display the current configuration parameters for the `VirtualIP`{.literal} resource:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource config VirtualIP
    ```

    ``` {.language-plaintext tabindex="-1"}
     Resource: VirtualIP (type=IPaddr2 class=ocf provider=heartbeat)
      Attributes: ip=192.168.0.120 cidr_netmask=24
      Operations: monitor interval=30s
    ```

2.  Update the value of the `ip`{.literal} parameter for the `VirtualIP`{.literal} resource:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource update VirtualIP ip=192.169.0.120
    ```

3.  Verify the updated parameter values for the `VirtualIP`{.literal} resource:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource config VirtualIP
    ```

    ``` {.language-plaintext tabindex="-1"}
     Resource: VirtualIP (type=IPaddr2 class=ocf provider=heartbeat)
      Attributes: ip=192.169.0.120 cidr_netmask=24
      Operations: monitor interval=30s
    ```

### [18.3. Clearing failure status of cluster resources](#cleanup-cluster-resources) {#clearing-failure-status-of-cluster-resources .title}

When a resource fails, a failure message appears in the `pcs status`{.literal} command output. After resolving the issue, verify the resource status by running `pcs status`{.literal} again, and check the failure count by using the `pcs resource failcount show --full`{.literal} command.

After you resolve the cause of a resource failure, you may want to remove the failure message from the status display by removing the failure operation history.

Resetting the failure status and removing the failure operation history

:   You can clear that failure status of a resource with the `pcs resource cleanup`{.literal} command. The `pcs resource cleanup`{.literal} command resets the resource status and `failcount`{.literal} value for the resource. This command also removes the operation history for the resource and re-detects its current state. The `pcs resource cleanup`{.literal} command operates only on resources with failed actions as shown in the cluster status.

    The following command resets the resource status and `failcount`{.literal} value for the resource specified by *resource_id*.

    For example, you can reset the resource status and `failcount`{.literal} value for the resource specified by *resource_id* by using the `pcs resource cleanup `{.literal}*`resource_id`{.literal}* command.

    If you do not specify *resource_id*, the `pcs resource cleanup`{.literal} command resets the resource status and `failcount`{.literal} value for all resources with a failure count.

Resetting the resource status and removing the full resource operation history

:   You can reset the resource status and clear the entire operation history of a resource with the `pcs resource refresh `{.literal}*`resource_id`{.literal}* command. Run the `pcs resource refresh`{.literal} command with no options specified to reset the resource status and `failcount`{.literal} value for all resources.

    The `pcs resource refresh`{.literal} command operates on resources regardless of their current state. This requires that Pacemaker reprobe the resources on all nodes, which increases the workload. To remove the operation history only of resources with failed actions, use the `pcs resource cleanup`{.literal} command.

### [18.4. Moving resources in a cluster](#moving-cluster-resources) {#moving-resources-in-a-cluster .title}

Move cluster resources manually between nodes or configure automatic relocation based on failure thresholds and connectivity changes.

Move resources manually in a cluster using the `pcs resource move`{.literal} and `pcs resource relocate`{.literal} commands, as described in [Manually moving cluster resources](#manually-move-resources "32.2. Manually moving cluster resources"). Additionally, control resource placement and behavior by disabling, enabling, or banning resources, as described in [Disabling, enabling, and banning cluster resources](#disabling-resources "32.3. Disabling, enabling, and banning cluster resources").

Resources can also be configured to move automatically to a new node after a specified number of failures or when external network connectivity is lost.

**Moving resources due to failure**

When creating a resource, configure it to move to a new node after a specified number of failures by setting the `migration-threshold`{.literal} resource option. When the threshold is reached, the node cannot run the failed resource until:

-   The `failure-timeout`{.literal} value of the resource expires.
-   An administrator manually resets the resource failure count using the `pcs resource cleanup`{.literal} command.

The default value of `migration-threshold`{.literal} is `INFINITY`{.literal}, which is defined internally as a large but finite number. Setting `migration-threshold`{.literal} to `0`{.literal} disables the feature.

Note

Setting a `migration-threshold`{.literal} for a resource differs from configuring live resource migration, where a resource moves to another node without state loss.

The following command adds a migration threshold of 10 to the `dummy_resource`{.literal} resource, causing it to move to a new node after 10 failures:

``` {.language-plaintext tabindex="-1"}
# pcs resource meta dummy_resource migration-threshold=10
```

To add a migration threshold to the defaults for the entire cluster, run the following command:

``` {.language-plaintext tabindex="-1"}
# pcs resource defaults update migration-threshold=10
```

To check current resource failure status and limits, run the `pcs resource failcount show`{.literal} command.

Two exceptions apply to the migration threshold concept: start failures and stop failures. If the `start-failure-is-fatal`{.literal} cluster property is set to `true`{.literal} (the default), a start failure immediately sets the failure count to `INFINITY`{.literal} and moves the resource. For details about cluster properties, see [Summary of cluster properties and options](#cluster-properties-options "23.1. Summary of cluster properties and options").

If a resource fails to stop and STONITH is enabled, the cluster fences the node to allow the resource to start elsewhere. If STONITH is disabled, the cluster cannot migrate the resource and retries stopping it after the failure timeout.

**Moving resources due to connectivity changes**

Configuring a cluster to move resources when external connectivity is lost is a two-step process:

1.  Add a `ping`{.literal} resource to the cluster. The `ping`{.literal} resource checks whether specified machines (by host name or IP address) are reachable and maintains the `pingd`{.literal} node attribute.
2.  Configure a location constraint rule to move resources to a connected node when connectivity is lost.

The following table describes the properties of a `ping`{.literal} resource.

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                             | Description                                                                                                                                                                                         |
+:==================================+:====================================================================================================================================================================================================+
| `dampen`{.literal}                | The time to wait (dampening) before applying connectivity changes. This prevents resources from rapidly flapping across the cluster if nodes detect connection changes at slightly different times. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `multiplier`{.literal}            | The factor multiplied by the number of connected ping targets to generate a score. Useful when multiple ping targets are configured.                                                                |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `host_list`{.literal}             | A space-separated list of resolvable DNS host names, IPv4 addresses, or IPv6 addresses to contact to determine connectivity.                                                                        |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 18.1. Properties of a ping resource

Show more

The following example procedure creates a `ping`{.literal} resource that checks connectivity to `gateway.example.com`{.literal}. In production environments, specify the network gateway or router address.

**Procedure**

1.  Configure a `ping`{.literal} resource as a clone so that it runs on all cluster nodes:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create ping ocf:pacemaker:ping dampen=5s multiplier=1000 host_list=gateway.example.com clone
    ```

2.  Configure a location constraint rule for the `Webserver`{.literal} resource to move it to a node that can reach `gateway.example.com`{.literal} if the current node loses connectivity:

    ``` {.language-plaintext tabindex="-1"}
    # pcs constraint location Webserver rule score=-INFINITY pingd lt 1 or not_defined pingd
    ```

### [18.5. Configuring and managing cluster resource tags](#tagging-cluster-resources) {#configuring-and-managing-cluster-resource-tags .title}

You can use the `pcs`{.literal} command to tag cluster resources. This allows you to enable, disable, manage, or unmanage a specified set of resources with a single command.

#### [18.5.1. Tagging cluster resources for administration by category](#tagging-cluster-resources-for-administration-by-category) {#tagging-cluster-resources-for-administration-by-category .title}

You can tag two resources with a resource tag and disable the tagged resources. In this example, the existing resources to be tagged are named `d-01`{.literal} and `d-02`{.literal}.

**Procedure**

1.  Create a tag named `special-resources`{.literal} for resources `d-01`{.literal} and `d-02`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [root@node-01]# pcs tag create special-resources d-01 d-02
    ```

2.  Display the resource tag configuration.

    ``` {.language-plaintext tabindex="-1"}
    [root@node-01]# pcs tag config
    ```

    ``` {.language-plaintext tabindex="-1"}
    special-resources
      d-01
      d-02
    ```

3.  Disable all resources that are tagged with the `special-resources`{.literal} tag.

    ``` {.language-plaintext tabindex="-1"}
    [root@node-01]# pcs resource disable special-resources
    ```

4.  Display the status of the resources to confirm that resources `d-01`{.literal} and `d-02`{.literal} are disabled.

    ``` {.language-plaintext tabindex="-1"}
    [root@node-01]# pcs resource
    ```

    ``` {.language-plaintext tabindex="-1"}
      * d-01        (ocf::pacemaker:Dummy): Stopped (disabled)
      * d-02        (ocf::pacemaker:Dummy): Stopped (disabled)
    ```

    In addition to the `pcs resource disable`{.literal} command, the `pcs resource enable`{.literal}, `pcs resource manage`{.literal}, and `pcs resource unmanage`{.literal} commands support the administration of tagged resources.

    After you have created a resource tag:

    -   You can delete a resource tag with the `pcs tag delete`{.literal} command.
    -   You can modify resource tag configuration for an existing resource tag with the `pcs tag update`{.literal} command.

#### [18.5.2. Deleting a tagged cluster resource](#deleting-a-tagged-cluster-resource) {#deleting-a-tagged-cluster-resource .title}

You cannot delete a tagged cluster resource using `pcs`{.literal}. Instead, remove the tag before deleting the resource.

**Procedure**

1.  Remove the resource tag.

    a.  The following command removes the resource tag `special-resources`{.literal} from all resources with that tag,

        ``` {.language-plaintext tabindex="-1"}
        [root@node-01]# pcs tag remove special-resources
        [root@node-01]# pcs tag
        ```

        ``` {.language-plaintext tabindex="-1"}
         No tags defined
        ```

    b.  The following command removes the resource tag `special-resources`{.literal} from the resource `d-01`{.literal} only.

        ``` {.language-plaintext tabindex="-1"}
        [root@node-01]# pcs tag update special-resources remove d-01
        ```

2.  Delete the resource.

    ``` {.language-plaintext tabindex="-1"}
    [root@node-01]# pcs resource delete d-01
    ```

    ``` {.language-plaintext tabindex="-1"}
    Attempting to stop: d-01... Stopped
    ```

#### [18.5.3. Displaying and exporting cluster resource tags](#displaying-and-exporting-cluster-resource-tags) {#displaying-and-exporting-cluster-resource-tags .title}

The `pcs tag [config]`{.literal} command supports the `--output-format`{.literal} option.

-   Specifying `--output-format=text`{.literal} displays the configured tags in plain text format, which is the default value for this option.
-   Specifying `--output-format=cmd`{.literal} displays the commands created from the current cluster tags configuration. You can use these commands to re-create configured tags on a different system.
-   Specifying `--output-format=json`{.literal} displays the configured tags in JSON format, which is suitable for machine parsing.

## [Chapter 19. Creating cluster resources that are active on multiple nodes (cloned resources)](#Creating-multinode-resources) {#chapter-19.-creating-cluster-resources-that-are-active-on-multiple-nodes-cloned-resources .title}

Clone a cluster resource or resource group to run it on multiple nodes, provided the resource agent supports cloning. For example, use cloned resources to distribute multiple IP resource instances throughout a cluster for node balancing.

Note

Only resources that can be active on multiple nodes at the same time are suitable for cloning. For example, a `Filesystem`{.literal} resource mounting a non-clustered file system such as `ext4`{.literal} from a shared memory device should not be cloned. Since the `ext4`{.literal} partition is not cluster aware, this file system is not suitable for read/write operations occurring from multiple nodes at the same time.

### [19.1. Creating and removing a cloned resource](#creating-cloned-resource) {#creating-and-removing-a-cloned-resource .title}

Create a cluster resource and a clone of that resource simultaneously, or clone an existing resource or resource group.

To create a resource and its clone in a single command, use the following syntax:

``` {.language-plaintext tabindex="-1"}
# pcs resource create resource_id [standard:[provider:]]type [resource_options] [meta resource_meta_options] clone [clone_id] [clone_options]
```

To clone an existing resource or resource group, use the following syntax:

``` {.language-plaintext tabindex="-1"}
# pcs resource clone resource_id | group_id [clone_id] [clone_options]
```

By default, the system names the clone *`resource_id`{.literal}*`-clone`{.literal}. To set a custom name for the clone, specify a value for the *clone_id* option.

A resource group and a clone of that resource group cannot be created in a single command.

Note

When creating a resource or resource group clone that is ordered after another clone, set the `interleave=true`{.literal} option. This ensures that copies of the dependent clone can stop or start when the primary clone stops or starts on the same node.

If this option is not set and cloned resource B depends on cloned resource A, stopping or starting resource A on a node that rejoins the cluster causes all instances of resource B across all nodes to restart. Without `interleave=true`{.literal}, every instance of a dependent clone depends on all running instances of the primary clone.

To remove a clone configuration without removing the underlying resource or resource group, use the following syntax:

``` {.language-plaintext tabindex="-1"}
# pcs resource unclone resource_id | clone_id | group_name
```

The following table describes the configuration options available for a cloned resource.

+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                                         | Description                                                                                                                                                                                                            |
+:==============================================+:=======================================================================================================================================================================================================================+
| `priority, target-role, is-managed`{.literal} | Options inherited from the resource being cloned, as described in [Configuring resource meta options](#configuring-resource-meta-options "11.6. Configuring resource meta options").                                   |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `clone-max`{.literal}                         | Maximum number of resource copies to start across the cluster. The default is the number of nodes in the cluster.                                                                                                      |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `clone-node-max`{.literal}                    | Maximum number of resource copies that can run on a single node. The default value is `1`{.literal}.                                                                                                                   |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `notify`{.literal}                            | Notifies all other copies before and after stopping or starting an instance. Allowed values: `true`{.literal}, `false`{.literal}. The default value is `false`{.literal}.                                              |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `globally-unique`{.literal}                   | Specifies whether each copy of the clone performs a distinct function. Allowed values: `true`{.literal}, `false`{.literal}.\                                                                                           |
|                                               | If set to `false`{.literal}, instances behave identically on all nodes and only one copy can run per machine.\                                                                                                         |
|                                               | If set to `true`{.literal}, each instance is distinct even on the same node. The default is `true`{.literal} if `clone-node-max`{.literal} is greater than `1`{.literal}; otherwise, the default is `false`{.literal}. |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `ordered`{.literal}                           | Specifies whether copies start sequentially rather than in parallel. Allowed values: `true`{.literal}, `false`{.literal}. The default value is `false`{.literal}.                                                      |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `interleave`{.literal}                        | Modifies ordering constraints so clone copies start or stop as soon as the copy on the same node starts or stops. Allowed values: `true`{.literal}, `false`{.literal}. The default value is `false`{.literal}.         |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `clone-min`{.literal}                         | Minimum number of running instances required before dependent clones (ordered after this clone) can start, even if `interleave=true`{.literal}.                                                                        |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 19.1. Resource clone options

Show more

To maintain a stable allocation pattern, clones have a default `resource-stickiness`{.literal} value of `1`{.literal}, giving them a slight preference to remain on their active node. This value prevents Pacemaker from unnecessarily moving copies across the cluster while minimizing disruption to score calculations for other resources. For details on setting resource stickiness, see [Configuring resource meta options](#configuring-resource-meta-options "11.6. Configuring resource meta options").

**Prerequisites**

-   An active Pacemaker cluster configured with `pcs`{.literal}.
-   Root or administrative access on at least one cluster node.

**Procedure**

1.  On one node of the cluster, create a resource and its clone. By default, the clone takes the resource name with `-clone`{.literal} appended.

    The following command creates an `apache`{.literal} resource named `webfarm`{.literal} and a clone named `webfarm-clone`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create webfarm apache clone
    ```

2.  Optional: Remove the clone configuration from a resource or resource group without removing the underlying resource:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource unclone webfarm
    ```

**Verification**

-   Display the active cluster resources to verify the status of the clone:

    ``` {.language-plaintext tabindex="-1"}
    # pcs status resources
    ```

### [19.2. Configuring clone resource constraints](#configuring-clone-constraints) {#configuring-clone-resource-constraints .title}

Configure constraints to determine the behavior of a clone resource in a cluster. Clone constraints are written like regular resource constraints, but require specifying the clone ID. For details, see [Configuring cluster resources](#configuring-cluster-resources "Chapter 11. Configuring cluster resources").

**Clone resource location constraints**

In most cases, a clone will have a single copy on each active cluster node. You can, however, set `clone-max`{.literal} for the resource clone to a value that is less than the total number of nodes in the cluster. If this is the case, you can indicate which nodes the cluster should preferentially assign copies to with resource location constraints. For general information about location constraints, see [Determining which node a resource can run on](#determining-which-node-a-resource-runs-on "Chapter 12. Determining which nodes a resource can run on").

The following command creates a location constraint for the cluster to preferentially assign resource clone `webfarm-clone`{.literal} to `node1`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs constraint location webfarm-clone prefers node1
```

**Clone resource ordering constraints**

Ordering constraints behave slightly differently for clones. In the following example, because the `interleave`{.literal} clone option is left to default as `false`{.literal}, no instance of `webfarm-stats`{.literal} will start until all instances of `webfarm-clone`{.literal} that need to be started have done so. Only if no copies of `webfarm-clone`{.literal} can be started then `webfarm-stats`{.literal} will be prevented from being active. Additionally, `webfarm-clone`{.literal} will wait for `webfarm-stats`{.literal} to be stopped before stopping itself.

``` {.language-plaintext tabindex="-1"}
# pcs constraint order start webfarm-clone then webfarm-stats
```

For general information about resource ordering constraints, see [Determining the order in which cluster resources are run](#determining-resource-order "Chapter 13. Determining the order in which cluster resources are run").

**Clone resource colocation constraints**

Colocation of a regular (or group) resource with a clone means that the resource can run on any machine with an active copy of the clone. The cluster will choose a copy based on where the clone is running and the resource's own location preferences. For information about colocation constraints, see xref colocating-cluster-resources\[Colocating cluster resources\].

Colocation between clones is also possible. In such cases, the set of allowed locations for the clone is limited to nodes on which the clone is (or will be) active. Allocation is then performed as normally.

The following command creates a colocation constraint to ensure that the resource `webfarm-stats`{.literal} runs on the same node as an active copy of `webfarm-clone`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs constraint colocation add webfarm-stats with webfarm-clone
```

### [19.3. Promotable clone resources](#promotable-clone-resources) {#promotable-clone-resources .title}

Promotable clone resources have the `promotable`{.literal} meta attribute set to `true`{.literal} and operate in two modes: `promoted`{.literal} and `unpromoted`{.literal}. When an instance starts, it must initialize in the `Unpromoted`{.literal} state.

Note

The Promoted and Unpromoted role names are the functional equivalent of the Master and Slave Pacemaker roles in previous RHEL releases.

#### [19.3.1. Creating a promotable clone resource](#creating-a-promotable-clone-resource) {#creating-a-promotable-clone-resource .title}

Configure a promotable clone resource to manage services that run in different modes, such as active and passive. You can create a new promotable resource or convert an existing resource or group to support promoted and unpromoted roles.

**Procedure**

-   Create a resource as a promotable clone:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create resource_id [standard:[provider:]]type [resource options] promotable [clone_id] [clone options]
    ```

    By default, the name of the promotable clone is *`resource_id`{.literal}*`-clone`{.literal}. You can set a custom name for the clone by specifying a value for the *clone_id* option.

-   Alternately, you can create a promotable resource from a previously-created resource or resource group with the following command:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource promotable resource_id [clone_id] [clone options]
    ```

    By default, the name of the promotable clone is *`resource_id`{.literal}*`-clone`{.literal} or *`group_name`{.literal}*`-clone`{.literal}. You can set a custom name for the clone by specifying a value for the *clone_id* option.

    The following table describes the extra clone options you can specify for a promotable resource.

    +-----------------------------------+------------------------------------------------------------------------------+
    | Field                             | Description                                                                  |
    +:==================================+:=============================================================================+
    | `promoted-max`{.literal}          | How many copies of the resource can be promoted; default 1.                  |
    +-----------------------------------+------------------------------------------------------------------------------+
    | `promoted-node-max`{.literal}     | How many copies of the resource can be promoted on a single node; default 1. |
    +-----------------------------------+------------------------------------------------------------------------------+

    : Table 19.2. Extra Clone Options Available for Promotable Clones

    Show more

#### [19.3.2. Configuring promotable resource constraints](#configuring-promotable-resource-constraints) {#configuring-promotable-resource-constraints .title}

You can determine the behavior of a promotable resource in a cluster by configuring constraints for that resource. For general information about resource constraints, see [Configuring cluster resources](#configuring-cluster-resources "Chapter 11. Configuring cluster resources").

**Promotable resource location constraints**

In most cases, a promotable resource will have a single copy on each active cluster node. If this is not the case, you can indicate which nodes the cluster should preferentially assign copies to with resource location constraints. These constraints are written no differently than those for regular resources. For information about location constraints, see [Determining which node a resource can run on](#determining-which-node-a-resource-runs-on "Chapter 12. Determining which nodes a resource can run on").

**Promotable resource colocation constraints**

You can create a colocation constraint which specifies whether the resources are operating in a promoted or unpromoted role. The following command creates a resource colocation constraint:

``` {.language-plaintext tabindex="-1"}
# pcs constraint colocation add [promoted|unpromoted] source_resource with [promoted|unpromoted] target_resource [score] [options]
```

For information about colocation constraints, see [Colocating cluster resources](#colocating-cluster-resources "Chapter 14. Colocating cluster resources").

**Promotable resource ordering constraints**

When configuring an ordering constraint that includes promotable resources, one of the actions that you can specify for the resources is `promote`{.literal}, indicating that the resource be promoted from unpromoted role to promoted role. Additionally, you can specify an action of `demote`{.literal}, indicated that the resource be demoted from promoted role to unpromoted role.

The command for configuring an order constraint is as follows:

``` {.language-plaintext tabindex="-1"}
# pcs constraint order [action] resource_id then [action] resource_id [options]
```

**Additional resources**

-   [Determining the order in which cluster resources are run](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_managing_high_availability_clusters/index#determining-resource-order)

#### [19.3.3. Demoting a promoted resource on failure](#demoting-a-promoted-resource-on-failure) {#demoting-a-promoted-resource-on-failure .title}

Configure a promotable resource so that when a `promote`{.literal} or `monitor`{.literal} action fails, or the partition loses quorum, the resource is demoted rather than fully stopped. This prevents manual intervention in scenarios where fully stopping the resource requires manual action.

**Procedure**

-   To configure a promotable resource to be demoted when a `promote`{.literal} action fails, set the `on-fail`{.literal} operation meta option to `demote`{.literal}, as in the following example:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource op add my-rsc promote on-fail="demote"
    ```

-   To configure a promotable resource to be demoted when a `monitor`{.literal} action fails, set `interval`{.literal} to a nonzero value, set the `on-fail`{.literal} operation meta option to `demote`{.literal}, and set `role`{.literal} to `Promoted`{.literal}, as in the following example.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource op add my-rsc monitor interval="10s" on-fail="demote" role="Promoted"
    ```

-   To configure a cluster so that when a cluster partition loses quorum any promoted resources will be demoted but left running and all other resources will be stopped, set the `no-quorum-policy`{.literal} cluster property to `demote`{.literal}

    Setting the `on-fail`{.literal} meta-attribute to `demote`{.literal} for an operation does not affect how promotion of a resource is determined. If the affected node still has the highest promotion score, it will be selected to be promoted again.

## [Chapter 20. Managing cluster nodes](#clusternode-management) {#chapter-20.-managing-cluster-nodes .title}

To manage cluster nodes, use `pcs`{.literal} commands to start and stop cluster services and to add or remove nodes.

### [20.1. Stopping cluster services](#cluster-stop) {#stopping-cluster-services .title}

You can stop cluster services on the specified node or nodes. As with the `pcs cluster start`{.literal}, the `--all`{.literal} option stops cluster services on all nodes and if you do not specify any nodes, cluster services are stopped on the local node only.

**Procedure**

-   Stop cluster services on the specified node or nodes:

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster stop [--all | node] [...]
    ```

-   You can force a stop of cluster services on the local node with the following command, which performs a `kill -9`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster kill
    ```

### [20.2. Enabling and disabling cluster services](#cluster-enable) {#enabling-and-disabling-cluster-services .title}

Enable the cluster services with the following command. This configures the cluster services to run on startup on the specified node or nodes.

Enabling cluster services allows nodes to automatically rejoin the cluster after being fenced, minimizing cluster downtime. If cluster services remain disabled, administrators can investigate failures before manually restarting the services, preventing nodes with hardware issues from rejoining prematurely.

**Procedure**

-   Enable the cluster services:

    -   If you specify the `--all`{.literal} option, the command enables cluster services on all nodes.

    -   If you do not specify any nodes, cluster services are enabled on the local node only.

        ``` {.language-plaintext tabindex="-1"}
        # pcs cluster enable [--all | node] [...]
        ```

-   Use the following command to configure the cluster services not to run on startup on the specified node or nodes:

    -   If you specify the `--all`{.literal} option, the command disables cluster services on all nodes.

    -   If you do not specify any nodes, cluster services are disabled on the local node only.

        ``` {.language-plaintext tabindex="-1"}
        # pcs cluster disable [--all | node] [...]
        ```

### [20.3. Adding cluster nodes](#cluster-nodeadd) {#adding-cluster-nodes .title}

You can add a new node to an existing cluster with the following procedure.

This procedure adds standard clusters nodes running `corosync`{.literal}. For information about integrating non-corosync nodes into a cluster, see [Integrating non-corosync nodes into a cluster: the pacemaker_remote service](#remote-node-management "Chapter 31. Integrating non-corosync nodes into a cluster: the pacemaker_remote service").

Note

It is recommended that you add nodes to existing clusters only during a production maintenance window. This allows you to perform appropriate resource and deployment testing for the new node and its fencing configuration.

In this example, the existing cluster nodes are `clusternode-01.example.com`{.literal}, `clusternode-02.example.com`{.literal}, and `clusternode-03.example.com`{.literal}. The new node is `newnode.example.com`{.literal}.

**Procedure**

1.  On the new node to add to the cluster, perform the following tasks:

    a.  Install the cluster packages. If the cluster uses SBD, the Booth ticket manager, or a quorum device, you must manually install the respective packages (`sbd`{.literal}, `booth-site`{.literal}, `corosync-qdevice`{.literal}) on the new node as well.

        ``` {.language-plaintext tabindex="-1"}
        [root@newnode ~]# dnf install -y pcs fence-agents-all
        ```

        In addition to the cluster packages, you will also need to install and configure all of the services that you are running in the cluster, which you have installed on the existing cluster nodes. For example, if you are running an Apache HTTP server in a Red Hat high availability cluster, you will need to install the server on the node you are adding, as well as the `wget`{.literal} tool that checks the status of the server.

    b.  If you are running the `firewalld`{.literal} daemon, run the following commands to enable the ports that are required by the Red Hat High Availability Add-On.

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --permanent --add-service=high-availability
        # firewall-cmd --add-service=high-availability
        ```

    c.  Set a password for the user ID `hacluster`{.literal}. It is recommended that you use the same password for each node in the cluster.

        ``` {.language-plaintext tabindex="-1"}
        [root@newnode ~]# passwd hacluster
        ```

        ``` {.language-plaintext tabindex="-1"}
        Changing password for user hacluster.
        New password:
        Retype new password:
        passwd: all authentication tokens updated successfully.
        ```

    d.  Run the following commands to start the `pcsd`{.literal} service and to enable `pcsd`{.literal} at system start.

        ``` {.language-plaintext tabindex="-1"}
        # systemctl start pcsd.service
        # systemctl enable pcsd.service
        ```

2.  On a node in the existing cluster, perform the following tasks.

    a.  Authenticate user `hacluster`{.literal} on the new cluster node.

        ``` {.language-plaintext tabindex="-1"}
        [root@clusternode-01 ~]# pcs host auth newnode.example.com
        ```

        ``` {.language-plaintext tabindex="-1"}
        Username: hacluster
        Password:
        newnode.example.com: Authorized
        ```

    b.  Add the new node to the existing cluster. This command also syncs the cluster configuration file `corosync.conf`{.literal} to all nodes in the cluster, including the new node you are adding.

        ``` {.language-plaintext tabindex="-1"}
        [root@clusternode-01 ~]# pcs cluster node add newnode.example.com
        ```

3.  On the new node to add to the cluster, perform the following tasks.

    a.  Start and enable cluster services on the new node.

        ``` {.language-plaintext tabindex="-1"}
        [root@newnode ~]# pcs cluster start
        Starting Cluster...
        [root@newnode ~]# pcs cluster enable
        ```

    b.  Ensure that you configure and test a fencing device for the new cluster node.

### [20.4. Removing cluster nodes](#cluster-noderemove) {#removing-cluster-nodes .title}

You can shut down the specified node and remove it from the cluster configuration file, `corosync.conf`{.literal}, on all of the other nodes in the cluster.

**Procedure**

-   Remove the cluster node:

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster node remove node
    ```

### [20.5. Adding a node to a cluster with multiple links](#add-nodes-to-multiple-ip-cluster) {#adding-a-node-to-a-cluster-with-multiple-links .title}

When adding a node to a multi-link cluster, you must specify an address for every link. This example adds `rh80-node3`{.literal}, using `192.168.122.203`{.literal} for the first link and `192.168.123.203`{.literal} for the second.

**Procedure**

-   Add a node to a cluster with multiple links:

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster node add rh80-node3 addr=192.168.122.203 addr=192.168.123.203
    ```

### [20.6. Adding and modifying links in an existing cluster](#adding-and-modifying-links-in-an-existing-cluster) {#adding-and-modifying-links-in-an-existing-cluster .title}

In most cases, you can add or modify the links in an existing cluster without restarting the cluster.

#### [20.6.1. Adding and removing links in an existing cluster](#adding-and-removing-links-in-an-existing-cluster_general-fence) {#adding-and-removing-links-in-an-existing-cluster .title}

To add a new link to a running cluster, use the `pcs cluster link add`{.literal} command.

When adding or managing links in a cluster, consider the following requirements and conditions:

-   When adding a link, specify an address for each node.
-   Adding and removing a link is possible only when using the `knet`{.literal} transport protocol.
-   At least one link in the cluster must be defined at all times.
-   The maximum number of links in a cluster is 8, numbered 0 to 7. Any combination of link numbers can be defined (for example, links 3, 6, and 7).
-   When adding a link without specifying its link number, `pcs`{.literal} uses the lowest available link number.
-   The link numbers of currently configured links are stored in the `corosync.conf`{.literal} file. To display the `corosync.conf`{.literal} file, run the `pcs cluster corosync`{.literal} command or the `pcs cluster config [show]`{.literal} command.

**Procedure**

-   The following command adds link number 5 to a three node cluster.

    ``` {.language-plaintext tabindex="-1"}
    [root@node1 ~] # pcs cluster link add node1=10.0.5.11 node2=10.0.5.12 node3=10.0.5.31 options linknumber=5
    ```

-   To remove an existing link, use the `pcs cluster link delete`{.literal} or `pcs cluster link remove`{.literal} command. Either of the following commands will remove link number 5 from the cluster.

    ``` {.language-plaintext tabindex="-1"}
    [root@node1 ~] # pcs cluster link delete 5

    [root@node1 ~] # pcs cluster link remove 5
    ```

#### [20.6.2. Modifying a link in a cluster with multiple links](#modifying-a-link-in-a-cluster-with-multiple-links) {#modifying-a-link-in-a-cluster-with-multiple-links .title}

Modify a specific link in a multi-link cluster configuration.

**Procedure**

1.  Remove the link you want to change.

    ``` {.language-plaintext tabindex="-1"}
    [root@node1 ~] # pcs cluster link remove 2
    ```

2.  Add the link back to the cluster with the updated addresses and options.

    ``` {.language-plaintext tabindex="-1"}
    [root@node1 ~] # pcs cluster link add node1=10.0.5.11 node2=10.0.5.12 node3=10.0.5.31 options linknumber=2
    ```

#### [20.6.3. Modifying the link addresses in a cluster with a single link](#modifying-the-link-addresses-in-a-cluster-with-a-single-link) {#modifying-the-link-addresses-in-a-cluster-with-a-single-link .title}

Update network addresses for cluster communication when migrating to a new subnet or replacing network infrastructure For single-link clusters, add a new link before removing the original to maintain cluster connectivity.

1.  Add a new link with the updated addresses and options:

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster link add node1=10.0.5.11 node2=10.0.5.12 node3=10.0.5.31 options linknumber=2
    ```

2.  Remove the original link:

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster link remove 1
    ```

Addresses currently in use cannot be re-specified when adding links to a cluster. Updating the address for only one node in a single-link cluster requires adding a temporary link before removing the original link and re-adding it with the updated address.

**Example scenario:**

-   Existing single-link cluster: `linknumber=1`{.literal} using address `10.0.5.11`{.literal} for `node1`{.literal} and `10.0.5.12`{.literal} for `node2`{.literal}.
-   Target modification: Change the address for `node2`{.literal} to `10.0.5.31`{.literal}.

**Procedure**

1.  Add a temporary link using addresses that are not currently in use:

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster link add node1=10.0.5.13 node2=10.0.5.14 options linknumber=2
    ```

2.  Remove the original link:

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster link remove 1
    ```

3.  Add the modified link with the updated node address:

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster link add node1=10.0.5.11 node2=10.0.5.31 options linknumber=1
    ```

4.  Remove the temporary link:

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster link remove 2
    ```

#### [20.6.4. Modifying the link options for a link in a cluster with a single link](#modifying-the-link-options-for-a-link-in-a-cluster-with-a-single-link) {#modifying-the-link-options-for-a-link-in-a-cluster-with-a-single-link .title}

If your cluster uses only one link and you want to modify the options for that link but you do not want to change the address to use, you can add a temporary link before removing and updating the link to modify.

In this example:

-   The link for the existing cluster is link 1, which uses the address 10.0.5.11 for node 1 and the address 10.0.5.12 for node 2.
-   You would like to change the link option `link_priority`{.literal} to 11.

**Procedure**

1.  Add a new temporary link to the existing cluster, using addresses that are not currently in use.

    ``` {.language-plaintext tabindex="-1"}
    [root@node1 ~] # pcs cluster link add node1=10.0.5.13 node2=10.0.5.14 options linknumber=2
    ```

2.  Remove the original link.

    ``` {.language-plaintext tabindex="-1"}
    [root@node1 ~] # pcs cluster link remove 1
    ```

3.  Add back the original link with the updated options.

    ``` {.language-plaintext tabindex="-1"}
    [root@node1 ~] # pcs cluster link add node1=10.0.5.11 node2=10.0.5.12 options linknumber=1 link_priority=11
    ```

4.  Remove the temporary link.

    ``` {.language-plaintext tabindex="-1"}
    [root@node1 ~] # pcs cluster link remove 2
    ```

#### [20.6.5. Modifying a link when adding a new link is not possible](#modifying-a-link-when-adding-a-new-link-is-not-possible) {#modifying-a-link-when-adding-a-new-link-is-not-possible .title}

If you cannot add a new link and must modify the single existing link, you must shut down the cluster.

The following example procedure updates link number 1 in the cluster and sets the `link_priority`{.literal} option for the link to 11.

**Procedure**

1.  Stop the cluster services for the cluster.

    ``` {.language-plaintext tabindex="-1"}
    [root@node1 ~] # pcs cluster stop --all
    ```

2.  Update the link addresses and options.

    The `pcs cluster link update`{.literal} command does not require that you specify all of the node addresses and options. Instead, you can specify only the addresses to change. This example modifies the addresses for `node1`{.literal} and `node3`{.literal} and the `link_priority`{.literal} option only.

    ``` {.language-plaintext tabindex="-1"}
    [root@node1 ~] # pcs cluster link update 1 node1=10.0.5.11 node3=10.0.5.31 options link_priority=11
    ```

    To remove an option, you can set the option to a null value with the *`option`{.literal}*`=`{.literal} format.

3.  Restart the cluster

    ``` {.language-plaintext tabindex="-1"}
    [root@node1 ~] # pcs cluster start --all
    ```

### [20.7. Configuring a node health strategy](#tracking-node-health) {#configuring-a-node-health-strategy .title}

A node might be functioning well enough to maintain its cluster membership and yet be unhealthy in some respect that makes it an undesirable location for resources. For example, a disk drive might be reporting SMART errors, or the CPU might be highly loaded.

You can use a node health strategy in Pacemaker to automatically move resources off unhealthy nodes.

You can monitor a node's health with the following health node resource agents, which set node attributes based on CPU and disk status:

-   `ocf:pacemaker:HealthCPU`{.literal}, which monitors CPU idling
-   `ocf:pacemaker:HealthIOWait`{.literal}, which monitors the CPU I/O wait
-   `ocf:pacemaker:HealthSMART`{.literal}, which monitors SMART status of a disk drive
-   `ocf:pacemaker:SysInfo`{.literal}, which sets a variety of node attributes with local system information and also functions as a health agent monitoring disk space usage

Additionally, any resource agent might provide node attributes that can be used to define a health node strategy.

The following procedure configures a health node strategy for a cluster that will move resources off of any node whose CPU I/O wait goes above 15%.

**Procedure**

1.  Set the `health-node-strategy`{.literal} cluster property to define how Pacemaker responds to changes in node health.

    ``` {.language-plaintext tabindex="-1"}
    # pcs property set node-health-strategy=migrate-on-red
    ```

2.  Create a cloned cluster resource that uses a health node resource agent, setting the `allow-unhealthy-nodes`{.literal} resource meta option to define whether the cluster will detect if the node's health recovers and move resources back to the node. Configure this resource with a recurring monitor action, to continually check the health of all nodes.

    This example creates a `HealthIOWait`{.literal} resource agent to monitor the CPU I/O wait, setting a red limit for moving resources off a node to 15%. This command sets the `allow-unhealthy-nodes`{.literal} resource meta option to `true`{.literal} and configures a recurring monitor interval of 10 seconds.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create io-monitor ocf:pacemaker:HealthIOWait red_limit=15 op monitor interval=10s meta allow-unhealthy-nodes=true clone
    ```

### [20.8. Configuring a large cluster with many resources](#Configuring-large-clusters) {#configuring-a-large-cluster-with-many-resources .title}

For clusters with a large number of nodes and resources, modify the default values of the following parameters.

The `cluster-ipc-limit`{.literal} cluster property

:   The `cluster-ipc-limit`{.literal} cluster property is the maximum Inter-Process Communication (IPC) message backlog before one cluster daemon will disconnect another. When a large number of resources are cleaned up or otherwise modified simultaneously in a large cluster, a large number of CIB updates arrive at once. This could cause slower clients to be evicted if the Pacemaker service does not have time to process all of the configuration updates before the CIB event queue threshold is reached.

    The recommended value of `cluster-ipc-limit`{.literal} for use in large clusters is the number of resources in the cluster multiplied by the number of nodes. This value can be raised if you see \"Evicting client\" messages for cluster daemon PIDs in the logs.

    You can increase the value of `cluster-ipc-limit`{.literal} from its default value of 500 with the `pcs property set`{.literal} command. For example, for a ten-node cluster with 200 resources you can set the value of `cluster-ipc-limit`{.literal} to 2000 with the following command.

    ``` {.language-plaintext tabindex="-1"}
    # pcs property set cluster-ipc-limit=2000
    ```

The `PCMK_ipc_buffer`{.literal} Pacemaker parameter

:   On very large deployments, internal Pacemaker messages may exceed the size of the message buffer. When this occurs, you will see a message in the system logs of the following format:

    ``` {.language-plaintext tabindex="-1"}
    Compressed message exceeds X% of configured IPC limit (X bytes); consider setting PCMK_ipc_buffer to X or higher
    ```

    When you see this message, you can increase the value of `PCMK_ipc_buffer`{.literal} in the `/etc/sysconfig/pacemaker`{.literal} configuration file on each node. For example, to increase the value of `PCMK_ipc_buffer`{.literal} from its default value to 13396332 bytes, change the uncommented `PCMK_ipc_buffer`{.literal} field in the `/etc/sysconfig/pacemaker`{.literal} file on each node in the cluster as follows.

    ``` {.language-plaintext tabindex="-1"}
    PCMK_ipc_buffer=13396332
    ```

    To apply this change, run the following command.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart pacemaker
    ```

## [Chapter 21. Setting user permissions for a Pacemaker cluster](#cluster-permissions) {#chapter-21.-setting-user-permissions-for-a-pacemaker-cluster .title}

You can grant permission for specific users other than user `hacluster`{.literal} to manage a Pacemaker cluster.

There are two sets of permissions that you can grant to individual users:

-   Permissions that allow individual users to manage the cluster through the Web UI and to run `pcs`{.literal} commands that connect to nodes over a network. Commands that connect to nodes over a network include commands to configure a cluster, or to add or remove nodes from a cluster.
-   Permissions for local users to allow read-only or read-write access to the cluster configuration. Commands that do not require connecting over a network include commands that edit the cluster configuration, such as those that create resources and configure constraints.

In situations where both sets of permissions have been assigned, the permissions for commands that connect over a network are applied first, and then permissions for editing the cluster configuration on the local node are applied. Most `pcs`{.literal} commands do not require network access and in those cases the network permissions will not apply.

### [21.1. Setting permissions for node access over a network](#setting-cluster-access-over-network) {#setting-permissions-for-node-access-over-a-network .title}

To grant permission for specific users to run `pcs`{.literal} commands that connect to nodes over a network, add those users to the group `haclient`{.literal}. This must be done on every node in the cluster.

**Procedure**

1.  On every node in the cluster, add the user to the `haclient`{.literal} group:

    ``` {.language-plaintext tabindex="-1"}
    # usermod -a -G haclient <username>
    ```

    Replace *`<username>`{.literal}* with the name of the user to whom you are granting permission.

### [21.2. Setting local permissions using ACLs](#setting-local-cluster-permissions) {#setting-local-permissions-using-acls .title}

You can use the `pcs acl`{.literal} command to set permissions for local users to allow read-only or read-write access to the cluster configuration by using access control lists (ACLs).

By default, ACLs are not enabled. When ACLs are not enabled, any user who is a member of the group `haclient`{.literal} on all nodes has full local read/write access to the cluster configuration while users who are not members of `haclient`{.literal} have no access. When ACLs are enabled, however, even users who are members of the `haclient`{.literal} group have access only to what has been granted to that user by the ACLs. The root and `hacluster`{.literal} user accounts always have full access to the cluster configuration, even when ACLs are enabled.

Setting permissions for local users is a two step process:

1.  Run the `pcs acl role create…​`{.literal} command to create a *role* which defines the permissions for that role.
2.  Assign the role you created to a user with the `pcs acl user create`{.literal} command. If you assign multiple roles to the same user, any `deny`{.literal} permission takes precedence, then `write`{.literal}, then `read`{.literal}.

The following example procedure provides read-only access for a cluster configuration to a local user named `rouser`{.literal}. Note that it is also possible to restrict access to certain portions of the configuration only.

Warning

It is important to perform this procedure as root or to save all of the configuration updates to a working file which you can then push to the active CIB when you are finished. Otherwise, you can lock yourself out of making any further changes. For information about saving configuration updates to a working file, see [Saving a configuration change to a working file](#configure-testfile "Chapter 6. Saving a configuration change to a working file").

**Procedure**

1.  This procedure requires that the user `rouser`{.literal} exists on the local system and that the user `rouser`{.literal} is a member of the group `haclient`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # adduser rouser
    # usermod -a -G haclient rouser
    ```

2.  Enable Pacemaker ACLs with the `pcs acl enable`{.literal .command} command.

    ``` {.language-plaintext tabindex="-1"}
    # pcs acl enable
    ```

3.  Create a role named `read-only`{.literal} with read-only permissions for the cib.

    ``` {.language-plaintext tabindex="-1"}
    # pcs acl role create read-only description="Read access to cluster" read xpath /cib
    ```

4.  Create the user `rouser`{.literal} in the pcs ACL system and assign that user the `read-only`{.literal} role.

    ``` {.language-plaintext tabindex="-1"}
    # pcs acl user create rouser read-only
    ```

5.  View the current ACLs.

    ``` {.language-plaintext tabindex="-1"}
    # pcs acl
    ```

    ``` {.language-plaintext tabindex="-1"}
    User: rouser
      Roles: read-only
    Role: read-only
      Description: Read access to cluster
      Permission: read xpath /cib (read-only-read)
    ```

6.  On each node where `rouser`{.literal} will run `pcs`{.literal} commands, log in as `rouser`{.literal} and authenticate to the local `pcsd`{.literal} service. This is required in order to run certain `pcs`{.literal} commands, such as `pcs status`{.literal}, as the ACL user.

    ``` {.language-plaintext tabindex="-1"}
    [rouser ~]$ pcs client local-auth
    ```

## [Chapter 22. Resource monitoring operations](#resource-monitoring-operations) {#chapter-22.-resource-monitoring-operations .title}

Configure monitoring operations to track resource health. If you do not specify one, `pcs`{.literal} creates a default. The interval is determined by the resource agent, or defaults to 60 seconds if the agent provides none.

The following table summarizes the properties of a resource monitoring operation.

+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+:=====================+:===============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `id`{.literal}       | Unique name for the action. The system assigns this when you configure an operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `name`{.literal}     | The action to perform. Common values: `monitor`{.literal}, `start`{.literal}, `stop`{.literal}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `interval`{.literal} | If set to a nonzero value, a recurring operation is created that repeats at this frequency, in seconds. A nonzero value makes sense only when the action `name`{.literal} is set to `monitor`{.literal}. A recurring monitor action will be executed immediately after a resource start completes, and subsequent monitor actions are scheduled starting at the time the previous monitor action completed. For example, if a monitor action with `interval=20s`{.literal} is executed at 01:00:00, the next monitor action does not occur at 01:00:20, but at 20 seconds after the first monitor action completes.                                                            |
|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                      | If set to zero, which is the default value, this parameter allows you to provide values to be used for operations created by the cluster. For example, if the `interval`{.literal} is set to zero, the `name`{.literal} of the operation is set to `start`{.literal}, and the `timeout`{.literal} value is set to 40, then Pacemaker will use a timeout of 40 seconds when starting this resource. A `monitor`{.literal} operation with a zero interval allows you to set the `timeout`{.literal}/`on-fail`{.literal}/`enabled`{.literal} values for the probes that Pacemaker does at startup to get the current status of all resources when the defaults are not desirable. |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `timeout`{.literal}  | If the operation does not complete in the amount of time set by this parameter, stop the operation and consider it failed. The default value is the value of `timeout`{.literal} if set with the `pcs resource op defaults`{.literal} command, or 20 seconds if it is not set. If you find that your system includes a resource that requires more time than the system allows to perform an operation (such as `start`{.literal}, `stop`{.literal}, or `monitor`{.literal}), investigate the cause and if the lengthy execution time is expected you can increase this value.                                                                                                 |
|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                      | The `timeout`{.literal} value is not a delay of any kind, nor does the cluster wait the entire timeout period if the operation returns before the timeout period has completed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `on-fail`{.literal}  | The action to take if this action ever fails. Allowed values:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                      | \* `ignore`{.literal} - Pretend the resource did not fail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                      | \* `block`{.literal} - Do not perform any further operations on the resource                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                      | \* `stop`{.literal} - Stop the resource and do not start it elsewhere                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                      | \* `restart`{.literal} - Stop the resource and start it again (possibly on a different node)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                      | \* `fence`{.literal} - STONITH the node on which the resource failed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                      | \* `standby`{.literal} - Move *all* resources away from the node on which the resource failed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                      | \* `demote`{.literal} - When a `promote`{.literal} action fails for the resource, the resource will be demoted but will not be fully stopped. When a `monitor`{.literal} action fails for a resource, if `interval`{.literal} is set to a nonzero value and `role`{.literal} is set to `Promoted`{.literal} the resource will be demoted but will not be fully stopped.                                                                                                                                                                                                                                                                                                        |
|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                      | The default for the `stop`{.literal} operation is `fence`{.literal} when STONITH is enabled and `block`{.literal} otherwise. All other operations default to `restart`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `enabled`{.literal}  | If `false`{.literal}, the operation is treated as if it does not exist. Allowed values: `true`{.literal}, `false`{.literal}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 22.1. Properties of an Operation

Show more

### [22.1. Configuring resource monitoring operations](#configuring-resource-monitoring-operations) {#configuring-resource-monitoring-operations .title}

You can configure monitoring operations when you create a resource.

``` {.language-plaintext tabindex="-1"}
# pcs resource create resource_id standard:provider:type|type [resource_options] [op operation_action operation_options [operation_type operation_options]...]
```

For example, the following command creates an `IPaddr2`{.literal} resource with a monitoring operation. The new resource is called `VirtualIP`{.literal} with an IP address of 192.168.0.99 and a netmask of 24 on `eth2`{.literal}. A monitoring operation will be performed every 30 seconds.

``` {.language-plaintext tabindex="-1"}
# pcs resource create VirtualIP ocf:heartbeat:IPaddr2 ip=192.168.0.99 cidr_netmask=24 nic=eth2 op monitor interval=30s
```

**Adding a monitoring operation to an existing resource**

Add a monitoring operation to an existing resource with the following command.

``` {.language-plaintext tabindex="-1"}
# pcs resource op add resource_id operation_action [operation_properties]
```

**Deleting a configured resource operation**

Use the following command to delete a configured resource operation.

``` {.language-plaintext tabindex="-1"}
# pcs resource op remove resource_id operation_name operation_properties
```

Note

You must specify the exact operation properties to properly remove an existing operation.

### [22.2. Modifying resource monitoring options](#modifying-resource-monitoring-options) {#modifying-resource-monitoring-options .title}

To change the values of a monitoring option, you can update the resource.

**Procedure**

1.  Create an `IPaddr2`{.literal} resource named `VirtualIP`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create VirtualIP ocf:heartbeat:IPaddr2 ip=192.168.0.99 cidr_netmask=24 nic=eth2
    ```

    By default, this command creates these operations.

    ``` {.language-plaintext tabindex="-1"}
    Operations: start interval=0s timeout=20s (VirtualIP-start-timeout-20s)
                stop interval=0s timeout=20s (VirtualIP-stop-timeout-20s)
                monitor interval=10s timeout=20s (VirtualIP-monitor-interval-10s)
    ```

2.  Change the stop timeout option for the stop operation.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource update VirtualIP op stop interval=0s timeout=40s
    ```

3.  Display the configured parameters for the resource.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource config VirtualIP
    ```

    ``` {.language-plaintext tabindex="-1"}
     Resource: VirtualIP (class=ocf provider=heartbeat type=IPaddr2)
      Attributes: ip=192.168.0.99 cidr_netmask=24 nic=eth2
      Operations: start interval=0s timeout=20s (VirtualIP-start-timeout-20s)
                  monitor interval=10s timeout=20s (VirtualIP-monitor-interval-10s)
                  stop interval=0s timeout=40s (VirtualIP-name-stop-interval-0s-timeout-40s)
    ```

### [22.3. Configuring global resource operation defaults](#configuring-global-resource-operation-defaults) {#configuring-global-resource-operation-defaults .title}

You can change the default value of a resource operation for all resources with the `pcs resource op defaults update`{.literal} command.

The following command sets a global default of a `timeout`{.literal} value of 240 seconds for all monitoring operations.

``` {.language-plaintext tabindex="-1"}
# pcs resource op defaults update timeout=240s
```

The original `pcs resource op defaults `{.literal}*`name`{.literal}*`=`{.literal}*`value`{.literal}* command, which set resource operation defaults for all resources in previous releases, remains supported unless there is more than one set of defaults configured. However, `pcs resource op defaults update`{.literal} is now the preferred version of the command.

**Overriding resource-specific operation values**

Note that a cluster resource will use the global default only when the option is not specified in the cluster resource definition. By default, resource agents define the `timeout`{.literal} option for all operations. For the global operation timeout value to be honored, you must create the cluster resource without the `timeout`{.literal} option explicitly or you must remove the `timeout`{.literal} option by updating the cluster resource, as in the following command.

``` {.language-plaintext tabindex="-1"}
# pcs resource update VirtualIP op monitor interval=10s
```

For example, after setting a global default of a `timeout`{.literal} value of 240 seconds for all monitoring operations and updating the cluster resource `VirtualIP`{.literal} to remove the timeout value for the `monitor`{.literal} operation, the resource `VirtualIP`{.literal} will then have timeout values for `start`{.literal}, `stop`{.literal}, and `monitor`{.literal} operations of 20s, 40s and 240s, respectively. The global default value for timeout operations is applied here only on the `monitor`{.literal} operation, where the default `timeout`{.literal} option was removed by the previous command.

``` {.language-plaintext tabindex="-1"}
# pcs resource config VirtualIP
```

``` {.language-plaintext tabindex="-1"}
 Resource: VirtualIP (class=ocf provider=heartbeat type=IPaddr2)
   Attributes: ip=192.168.0.99 cidr_netmask=24 nic=eth2
   Operations: start interval=0s timeout=20s (VirtualIP-start-timeout-20s)
               monitor interval=10s (VirtualIP-monitor-interval-10s)
               stop interval=0s timeout=40s (VirtualIP-name-stop-interval-0s-timeout-40s)
```

**Changing the default value of a resource operation for sets of resources**

You can create multiple sets of resource operation defaults with the `pcs resource op defaults set create`{.literal} command, which allows you to specify a rule that contains `resource`{.literal} and operation expressions. All of the rule expressions supported by Pacemaker are allowed.

With this command, you can configure a default resource operation value for all resources of a particular type. For example, it is now possible to configure implicit `podman`{.literal} resources created by Pacemaker when bundles are in use.

The following command sets a default timeout value of 90s for all operations for all `podman`{.literal} resources. In this example, `::podman`{.literal} means a resource of any class, any provider, of type `podman`{.literal}.

The `id`{.literal} option, which names the set of resource operation defaults, is not mandatory. If you do not set this option, `pcs`{.literal} will generate an ID automatically. Setting this value allows you to provide a more descriptive name.

``` {.language-plaintext tabindex="-1"}
# pcs resource op defaults set create id=podman-timeout meta timeout=90s rule resource ::podman
```

The following command sets a default timeout value of 120s for the `stop`{.literal} operation for all resources.

``` {.language-plaintext tabindex="-1"}
# pcs resource op defaults set create id=stop-timeout meta timeout=120s rule op stop
```

It is possible to set the default timeout value for a specific operation for all resources of a particular type. The following example sets a default timeout value of 120s for the `stop`{.literal} operation for all `podman`{.literal} resources.

``` {.language-plaintext tabindex="-1"}
# pcs resource op defaults set create id=podman-stop-timeout meta timeout=120s rule resource ::podman and op stop
```

**Displaying currently configured resource operation default values**

The `pcs resource op defaults`{.literal} command displays a list of currently configured default values for resource operations, including any rules you specified.

The following command displays the default operation values for a cluster which has been configured with a default timeout value of 90s for all operations for all `podman`{.literal} resources, and for which an ID for the set of resource operation defaults has been set as `podman-timeout`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs resource op defaults
```

``` {.language-plaintext tabindex="-1"}
Meta Attrs: podman-timeout
  timeout=90s
  Rule: boolean-op=and score=INFINITY
    Expression: resource ::podman
```

The following command displays the default operation values for a cluster which has been configured with a default timeout value of 120s for the `stop`{.literal} operation for all `podman`{.literal} resources, and for which an ID for the set of resource operation defaults has been set as `podman-stop-timeout`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs resource op defaults]
```

``` {.language-plaintext tabindex="-1"}
Meta Attrs: podman-stop-timeout
  timeout=120s
  Rule: boolean-op=and score=INFINITY
    Expression: resource ::podman
    Expression: op stop
```

### [22.4. Configuring multiple monitoring operations](#configuring-multiple-monitoring-operations) {#configuring-multiple-monitoring-operations .title}

You can configure a single resource with as many monitor operations as a resource agent supports. In this way you can do a superficial health check every minute and progressively more intense ones at higher intervals.

Note

When configuring multiple monitor operations, you must ensure that no two operations are performed at the same interval.

**Procedure**

1.  To configure additional monitoring operations for a resource that supports more in-depth checks at different levels, add an `OCF_CHECK_LEVEL=`{.literal}*`n`{.literal}* option.

    For example, if you configure the following `IPaddr2`{.literal} resource, by default this creates a monitoring operation with an interval of 10 seconds and a timeout value of 20 seconds.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create VirtualIP ocf:heartbeat:IPaddr2 ip=192.168.0.99 cidr_netmask=24 nic=eth2
    ```

2.  If the Virtual IP supports a different check with a depth of 10, the following command causes Pacemaker to perform the more advanced monitoring check every 60 seconds in addition to the normal Virtual IP check every 10 seconds. (As noted, you should not configure the additional monitoring operation with a 10-second interval as well.)

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource op add VirtualIP monitor interval=60s OCF_CHECK_LEVEL=10
    ```

### [22.5. Disabling a monitoring operation](#disabling-monitor-operation) {#disabling-a-monitoring-operation .title}

To temporarily disable a recurring monitor instead of deleting it, set `enabled="false"`{.literal} in the operation definition. To reinstate monitoring, set `enabled="true"`{.literal}.

When you update a resource's operation with the `pcs resource update`{.literal} command, any options you do not specifically call out are reset to their default values. For example, if you have configured a monitoring operation with a custom timeout value of 600, running the following commands will reset the timeout value to the default value of 20 (or whatever you have set the default value to with the `pcs resource op defaults`{.literal} command).

**Procedure**

-   Temporarily disable and reinstate the monitoring operation:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource update resourceXZY op monitor enabled=false
    # pcs resource update resourceXZY op monitor enabled=true
    ```

-   In order to maintain the original value of 600 for this option, when you reinstate the monitoring operation you must specify that value, as in the following example:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource update resourceXZY op monitor timeout=600 enabled=true
    ```

## [Chapter 23. Pacemaker cluster properties](#controlling-cluster-behavior) {#chapter-23.-pacemaker-cluster-properties .title}

Cluster properties control how the cluster behaves when confronted with situations that might occur during cluster operation.

### [23.1. Summary of cluster properties and options](#cluster-properties-options) {#summary-of-cluster-properties-and-options .title}

This table summaries the Pacemaker cluster properties, showing the default values of the properties and the possible values you can set for those properties.

There are additional cluster properties that determine fencing behavior. For information about these properties, see the table of cluster properties that determine fencing behavior in [General properties of fencing devices](#general-fence-device-properties "9.3. General properties of fencing devices").

Note

In addition to the properties described in this table, there are additional cluster properties that are exposed by the cluster software. For these properties, it is recommended that you not change their values from their defaults.

+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option                               | Default           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+:=====================================+:==================+:================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `batch-limit`{.literal}              | 0                 | The number of resource actions that the cluster is allowed to run in parallel. The \"correct\" value will depend on the speed and load of your network and cluster nodes. The default value of 0 means that the cluster will dynamically impose a limit when any node has a high CPU load.                                                                                                                                                                                                                      |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `migration-limit`{.literal}          | -1 (unlimited)    | The number of migration jobs that the cluster is allowed to run in parallel on a node.                                                                                                                                                                                                                                                                                                                                                                                                                          |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `no-quorum-policy`{.literal}         | stop              | What to do when the cluster does not have quorum. Allowed values:                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                      |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                      |                   | \* ignore - continue all resource management                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                      |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                      |                   | \* freeze - continue resource management, but do not recover resources from nodes not in the affected partition                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                      |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                      |                   | \* stop - stop all resources in the affected cluster partition                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                      |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                      |                   | \* suicide - fence all nodes in the affected cluster partition                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                      |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                      |                   | \* demote - if a cluster partition loses quorum, demote any promoted resources and stop all other resources                                                                                                                                                                                                                                                                                                                                                                                                     |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `symmetric-cluster`{.literal}        | true              | Indicates whether resources can run on any node by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `cluster-delay`{.literal}            | 60s               | Round trip delay over the network (excluding action execution). The \"correct\" value will depend on the speed and load of your network and cluster nodes.                                                                                                                                                                                                                                                                                                                                                      |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `dc-deadtime`{.literal}              | 20s               | How long to wait for a response from other nodes during startup. The \"correct\" value will depend on the speed and load of your network and the type of switches used.                                                                                                                                                                                                                                                                                                                                         |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `stop-orphan-resources`{.literal}    | true              | Indicates whether deleted resources should be stopped.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `stop-orphan-actions`{.literal}      | true              | Indicates whether deleted actions should be canceled.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `start-failure-is-fatal`{.literal}   | true              | Indicates whether a failure to start a resource on a particular node prevents further start attempts on that node. When set to `false`{.literal}, the cluster will decide whether to try starting on the same node again based on the resource's current failure count and migration threshold. For information about setting the `migration-threshold`{.literal} option for a resource, see [Configuring resource meta options](#configuring-resource-meta-options "11.6. Configuring resource meta options"). |
|                                      |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                      |                   | Setting `start-failure-is-fatal`{.literal} to `false`{.literal} incurs the risk that this will allow one faulty node that is unable to start a resource to hold up all dependent actions. This is why `start-failure-is-fatal`{.literal} defaults to true. The risk of setting `start-failure-is-fatal=false`{.literal} can be mitigated by setting a low migration threshold so that other actions can proceed after that many failures.                                                                       |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pe-error-series-max`{.literal}      | -1 (all)          | The number of scheduler inputs resulting in ERRORs to save. Used when reporting problems.                                                                                                                                                                                                                                                                                                                                                                                                                       |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pe-warn-series-max`{.literal}       | -1 (all)          | The number of scheduler inputs resulting in WARNINGs to save. Used when reporting problems.                                                                                                                                                                                                                                                                                                                                                                                                                     |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pe-input-series-max`{.literal}      | -1 (all)          | The number of \"normal\" scheduler inputs to save. Used when reporting problems.                                                                                                                                                                                                                                                                                                                                                                                                                                |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `cluster-infrastructure`{.literal}   |                   | The messaging stack on which Pacemaker is currently running. Used for informational and diagnostic purposes; not user-configurable.                                                                                                                                                                                                                                                                                                                                                                             |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `dc-version`{.literal}               |                   | Version of Pacemaker on the cluster's Designated Controller (DC). Used for diagnostic purposes; not user-configurable.                                                                                                                                                                                                                                                                                                                                                                                          |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `cluster-recheck-interval`{.literal} | 15 minutes        | Pacemaker is primarily event-driven, and looks ahead to know when to recheck the cluster for failure timeouts and most time-based rules. Pacemaker will also recheck the cluster after the duration of inactivity specified by this property. This cluster recheck has two purposes: rules with `date-spec`{.literal} are guaranteed to be checked this often, and it serves as a fail-safe for some kinds of scheduler bugs. A value of 0 disables this polling; positive values indicate a time interval.     |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `maintenance-mode`{.literal}         | false             | Maintenance Mode tells the cluster to go to a \"hands off\" mode, and not start or stop any services until told otherwise. When maintenance mode is completed, the cluster does a sanity check of the current state of any services, and then stops or starts any that need it.                                                                                                                                                                                                                                 |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `shutdown-escalation`{.literal}      | 20min             | The time after which to give up trying to shut down gracefully and just exit. Advanced use only.                                                                                                                                                                                                                                                                                                                                                                                                                |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `stop-all-resources`{.literal}       | false             | Should the cluster stop all resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `enable-acl`{.literal}               | false             | Indicates whether the cluster can use access control lists, as set with the `pcs acl`{.literal} command.                                                                                                                                                                                                                                                                                                                                                                                                        |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `placement-strategy`{.literal}       | default           | Indicates whether and how the cluster will take utilization attributes into account when determining resource placement on cluster nodes.                                                                                                                                                                                                                                                                                                                                                                       |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `node-health-strategy`{.literal}     | none              | When used in conjunction with a health resource agent, controls how Pacemaker responds to changes in node health. Allowed values:                                                                                                                                                                                                                                                                                                                                                                               |
|                                      |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                      |                   | \* `none`{.literal} - Do not track node health.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                      |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                      |                   | \* `migrate-on-red`{.literal} - Resources are moved off any node where a health agent has determined that the node's status is `red`{.literal}, based on the local conditions that the agent monitors.                                                                                                                                                                                                                                                                                                          |
|                                      |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                      |                   | \* `only-green`{.literal} - Resources are moved off any node where a health agent has determined that the node's status is `yellow`{.literal} or `red`{.literal}, based on the local conditions that the agent monitors.                                                                                                                                                                                                                                                                                        |
|                                      |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                      |                   | \* `progressive`{.literal}, `custom`{.literal} - Advanced node health strategies that offer finer-grained control over the cluster's response to health conditions according to the internal numeric values of health attributes.                                                                                                                                                                                                                                                                               |
+--------------------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 23.1. Cluster Properties

Show more

### [23.2. Setting and removing cluster properties](#setting-cluster-properties) {#setting-and-removing-cluster-properties .title}

Modify cluster behavior by setting or removing global properties. These settings determine how the cluster manages resource placement, fencing, and node failures. When you remove a specific configuration, the property reverts to its default system value.

**Procedure**

-   Set the value of a cluster property:

    ``` {.language-plaintext tabindex="-1"}
    # pcs property set property=value
    ```

-   For example, set the value of `symmetric-cluster`{.literal} to `false`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # pcs property set symmetric-cluster=false
    ```

-   Remove a cluster property from the configuration:

    ``` {.language-plaintext tabindex="-1"}
    # pcs property unset property
    ```

-   Alternately, you can remove a cluster property from a configuration by leaving the value field of the `pcs property set`{.literal} command blank. This restores that property to its default value. For example, if you have previously set the `symmetric-cluster`{.literal} property to `false`{.literal}, the following command removes the value you have set from the configuration and restores the value of `symmetric-cluster`{.literal} to `true`{.literal}, which is its default value:

    ``` {.language-plaintext tabindex="-1"}
    # pcs property set symmetic-cluster=
    ```

### [23.3. Querying cluster property settings](#querying-cluster-property-settings) {#querying-cluster-property-settings .title}

Query cluster properties to audit global configuration settings, such as fencing defaults, migration thresholds, and resource constraints. You can view explicitly configured values, specific properties, or the complete list of defaults to understand how the cluster manages resources and nodes.

**Procedure**

-   Display the values of the property settings that have been set for the cluster:

    ``` {.language-plaintext tabindex="-1"}
    # pcs property config
    ```

-   Display all of the values of the property settings for the cluster, including the default values of the property settings that have not been explicitly set:

    ``` {.language-plaintext tabindex="-1"}
    # pcs property config --all
    ```

-   Display the current value of a specific cluster property:

    ``` {.language-plaintext tabindex="-1"}
    # pcs property config property
    ```

-   For example, to display the current value of the `cluster-infrastructure`{.literal} property, run the following command:

    ``` {.language-plaintext tabindex="-1"}
    # pcs property config cluster-infrastructure
    ```

    ``` {.language-plaintext tabindex="-1"}
    Cluster Properties:
     cluster-infrastructure: cman
    ```

-   For informational purposes, you can display a list of all of the default values for the properties, whether they have been set to a value other than the default or not, by using the following command.

    ``` {.language-plaintext tabindex="-1"}
    # pcs property [config] --defaults
    ```

### [23.4. Exporting cluster properties as pcs commands](#exporting-properties) {#exporting-cluster-properties-as-pcs-commands .title}

You can display the `pcs`{.literal} commands that can be used to re-create configured cluster properties on a different system using the `--output-format=cmd`{.literal} option of the `pcs property config`{.literal} command.

**Procedure**

1.  The following command sets the `migration-limit`{.literal} cluster property to 10:

    ``` {.language-plaintext tabindex="-1"}
    # pcs property set migration-limit=10
    ```

2.  After you set the cluster property, the following command displays the `pcs`{.literal} command you can use to set the cluster property on a different system.

    ``` {.language-plaintext tabindex="-1"}
    # pcs property config --output-format=cmd
    ```

    ``` {.language-plaintext tabindex="-1"}
    pcs property set --force -- \
     migration-limit=10 \
     placement-strategy=minimal
    ```

## [Chapter 24. Configuring resources to remain stopped on clean node shutdown](#configuring-resources-to-remain-stopped) {#chapter-24.-configuring-resources-to-remain-stopped-on-clean-node-shutdown .title}

Pacemaker defaults to failing over resources during shutdown. However, you can configure resources to lock to a node during a clean shutdown. This prevents failover, allowing you to power down nodes for maintenance when service outages are acceptable.

### [24.1. Cluster properties to configure resources to remain stopped on clean node shutdown](#cluster-properties-shutdown-lock) {#cluster-properties-to-configure-resources-to-remain-stopped-on-clean-node-shutdown .title}

The ability to prevent resources from failing over on a clean node shutdown is implemented by means of the following cluster properties.

`shutdown-lock`{.literal}

:   When this cluster property is set to the default value of `false`{.literal}, the cluster will recover resources that are active on nodes being cleanly shut down. When this property is set to `true`{.literal}, resources that are active on the nodes being cleanly shut down are unable to start elsewhere until they start on the node again after it rejoins the cluster.

    The `shutdown-lock`{.literal} property will work for either cluster nodes or remote nodes, but not guest nodes.

    If `shutdown-lock`{.literal} is set to `true`{.literal}, you can remove the lock on one cluster resource when a node is down so that the resource can start elsewhere by performing a manual refresh on the node with the following command.

    `pcs resource refresh `{.literal}*`resource`{.literal}*` node=`{.literal}*`nodename`{.literal}*

    Note that once the resources are unlocked, the cluster is free to move the resources elsewhere. You can control the likelihood of this occurring by using stickiness values or location preferences for the resource.

    Note

    A manual refresh will work with remote nodes only if you first run the following commands:

    1.  Run the `systemctl stop pacemaker_remote`{.literal} command on the remote node to stop the node.
    2.  Run the `pcs resource disable `{.literal}*`remote-connection-resource`{.literal}* command.

    You can then perform a manual refresh on the remote node.

`shutdown-lock-limit`{.literal}

:   When this cluster property is set to a time other than the default value of 0, resources will be available for recovery on other nodes if the node does not rejoin within the specified time since the shutdown was initiated.

    Note

    The `shutdown-lock-limit`{.literal} property will work with remote nodes only if you first run the following commands:

    1.  Run the `systemctl stop pacemaker_remote`{.literal} command on the remote node to stop the node.
    2.  Run the `pcs resource disable `{.literal}*`remote-connection-resource`{.literal}* command.

    After you run these commands, the resources that had been running on the remote node will be available for recovery on other nodes when the amount of time specified as the `shutdown-lock-limit`{.literal} has passed.

### [24.2. Setting the shutdown-lock cluster property](#setting-shutdown-lock) {#setting-the-shutdown-lock-cluster-property .title}

Set the `shutdown-lock`{.literal} cluster property to `true`{.literal} in an example cluster and show the effect this has when the node is shut down and started again. This example cluster consists of three nodes: `z1.example.com`{.literal}, `z2.example.com`{.literal}, and `z3.example.com`{.literal}.

**Procedure**

1.  Set the `shutdown-lock`{.literal} property to `true`{.literal} and verify its value. In this example the `shutdown-lock-limit`{.literal} property maintains its default value of 0.

    ``` {.language-plaintext tabindex="-1"}
    [root@z3 ~]# pcs property set shutdown-lock=true
    [root@z3 ~]# pcs property list --all | grep shutdown-lock
    ```

    ``` {.language-plaintext tabindex="-1"}
     shutdown-lock: true
     shutdown-lock-limit: 0
    ```

2.  Check the status of the cluster. In this example, resources `third`{.literal} and `fifth`{.literal} are running on `z1.example.com`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [root@z3 ~]# pcs status
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    Full List of Resources:
    ...
     * first    (ocf::pacemaker:Dummy): Started z3.example.com
     * second   (ocf::pacemaker:Dummy): Started z2.example.com
     * third    (ocf::pacemaker:Dummy): Started z1.example.com
     * fourth   (ocf::pacemaker:Dummy): Started z2.example.com
     * fifth    (ocf::pacemaker:Dummy): Started z1.example.com
    ...
    ```

3.  Shut down `z1.example.com`{.literal}, which will stop the resources that are running on that node.

    ``` {.language-plaintext tabindex="-1"}
    [root@z3 ~] # pcs cluster stop z1.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    Stopping Cluster (pacemaker)...
    Stopping Cluster (corosync)...
    ```

4.  Running the `pcs status`{.literal} command shows that node `z1.example.com`{.literal} is offline and that the resources that had been running on `z1.example.com`{.literal} are `LOCKED`{.literal} while the node is down.

    ``` {.language-plaintext tabindex="-1"}
    [root@z3 ~]# pcs status
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...

    Node List:
     * Online: [ z2.example.com z3.example.com ]
     * OFFLINE: [ z1.example.com ]

    Full List of Resources:
    ...
     * first    (ocf::pacemaker:Dummy): Started z3.example.com
     * second   (ocf::pacemaker:Dummy): Started z2.example.com
     * third    (ocf::pacemaker:Dummy): Stopped z1.example.com (LOCKED)
     * fourth   (ocf::pacemaker:Dummy): Started z3.example.com
     * fifth    (ocf::pacemaker:Dummy): Stopped z1.example.com (LOCKED)

    ...
    ```

5.  Start cluster services again on `z1.example.com`{.literal} so that it rejoins the cluster. Locked resources should get started on that node, although once they start they will not necessarily remain on the same node.

    ``` {.language-plaintext tabindex="-1"}
    [root@z3 ~]# pcs cluster start z1.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    Starting Cluster...
    ```

6.  In this example, resources `third`{.literal} and `fifth`{.literal} are recovered on node `z1.example.com`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [root@z3 ~]# pcs status
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...

    Node List:
     * Online: [ z1.example.com z2.example.com z3.example.com ]

    Full List of Resources:
    ..
     * first    (ocf::pacemaker:Dummy): Started z3.example.com
     * second   (ocf::pacemaker:Dummy): Started z2.example.com
     * third    (ocf::pacemaker:Dummy): Started z1.example.com
     * fourth   (ocf::pacemaker:Dummy): Started z3.example.com
     * fifth    (ocf::pacemaker:Dummy): Started z1.example.com

    ...
    ```

## [Chapter 25. Configuring a node placement strategy](#configuring-node-placement-strategy) {#chapter-25.-configuring-a-node-placement-strategy .title}

Pacemaker allocates a resource to the node with the highest allocation score. This score is calculated from factors such as resource constraints, `resource-stickiness`{.literal} settings, previous failure history, and node utilization.

If the resource allocation scores on all the nodes are equal, by the default placement strategy Pacemaker will choose a node with the least number of allocated resources for balancing the load. If the number of resources on each node is equal, the first eligible node listed in the CIB will be chosen to run the resource.

Often, however, different resources use significantly different proportions of a node's capacities (such as memory or I/O). You cannot always balance the load ideally by taking into account only the number of resources allocated to a node. In addition, if resources are placed such that their combined requirements exceed the provided capacity, they may fail to start completely or they may run with degraded performance. To take these factors into account, Pacemaker allows you to configure the following components:

-   the capacity a particular node provides
-   the capacity a particular resource requires
-   an overall strategy for placement of resources

### [25.1. Utilization attributes and placement strategy](#utilization-attributes) {#utilization-attributes-and-placement-strategy .title}

To configure node capacity or resource requirements, use *utilization attributes*. Assign a utilization variable and value to a resource to specify its requirements, and assign the same variable and value to a node to specify what it provides.

You can name utilization attributes according to your preferences and define as many name and value pairs as your configuration needs. The values of utilization attributes must be integers.

**Configuring node and resource capacity**

The following example procedure configures utilization attributes for two nodes and then specifies the same utilization attributes that three different resources require. A node is considered eligible for a resource if it has sufficient free capacity to satisfy the resource's requirements, as defined by the utilization attributes.

**Displaying node utilization as pcs commands**

You can export node utilization as a series of `pcs`{.literal} commands by using the `--output-format=cmd`{.literal} option. This is useful for scripting, automation, or replicating the same configuration on a different system.

Note

You can display the configured node utilization in one of three formats:

-   `text`{.literal}: Displays the output in plain text. This is the default format.
-   `json`{.literal}: Displays the output in a machine-readable JSON format, which is useful for scripting and automation.
-   `cmd`{.literal}: Displays the output as a series of `pcs`{.literal} commands, which you can use to recreate the same node utilization on a different system.

-   To display the configured node utilization as a series of `pcs`{.literal} commands:

    ``` {.language-plaintext tabindex="-1"}
    # pcs node utilization --output-format=cmd
    ```

    **Example output**

    ``` {.language-plaintext tabindex="-1"}
    pcs node utilization node1 cpu=2
    pcs node utilization node2 cpu=4
    ```

**Configuring placement strategy**

After you have configured the capacities your nodes provide and the capacities your resources require, you need to set the `placement-strategy`{.literal} cluster property, otherwise the capacity configurations have no effect.

Four values are available for the `placement-strategy`{.literal} cluster property:

-   `default`{.literal} - Utilization values are not taken into account at all. Resources are allocated according to allocation scores. If scores are equal, resources are evenly distributed across nodes.
-   `utilization`{.literal} - Utilization values are taken into account only when deciding whether a node is considered eligible (that is, whether it has sufficient free capacity to satisfy the resource's requirements). Load-balancing is still done based on the number of resources allocated to a node.
-   `balanced`{.literal} - Utilization values are taken into account when deciding whether a node is eligible to serve a resource and when load-balancing, so an attempt is made to spread the resources in a way that optimizes resource performance.
-   `minimal`{.literal} - Utilization values are taken into account only when deciding whether a node is eligible to serve a resource. For load-balancing, an attempt is made to concentrate the resources on as few nodes as possible, thereby enabling possible power savings on the remaining nodes.

The following example command sets the value of `placement-strategy`{.literal} to `balanced`{.literal}. After running this command, Pacemaker will ensure the load from your resources will be distributed evenly throughout the cluster, without the need for complicated sets of colocation constraints.

``` {.language-plaintext tabindex="-1"}
# pcs property set placement-strategy=balanced
```

**Procedure**

1.  Configure utilization attributes for `node1`{.literal}. This command configures a node attribute of CPU capacity, setting this attribute as the variable `cpu`{.literal} and defining `node1`{.literal} as providing a CPU capacity of two. This command also defines a utilization attribute of RAM capacity, setting this attribute as the variable `memory`{.literal} and defining `node1`{.literal} as providing a RAM capacity of 2048.

    ``` {.language-plaintext tabindex="-1"}
    # pcs node utilization node1 cpu=2 memory=2048
    ```

2.  Configure utilization attributes for `node2`{.literal}. This command configures a node attribute of CPU capacity, setting this attribute as the variable `cpu`{.literal} and defining `node2`{.literal} as providing a CPU capacity of four. This command also defines a utilization attribute of RAM capacity, setting this attribute as the variable `memory`{.literal} and defining `node2`{.literal} as providing a RAM capacity of 2048.

    ``` {.language-plaintext tabindex="-1"}
    # pcs node utilization node2 cpu=4 memory=2048
    ```

3.  Specify the utilization attributes that resource `dummy-small`{.literal} requires. In this example, `dummy-small`{.literal} requires a CPU capacity of 1 and a RAM capacity of 1024.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource utilization dummy-small cpu=1 memory=1024
    ```

4.  Specify the utilization attributes that resource `dummy-medium`{.literal} requires. In this example, `dummy-medium`{.literal} requires a CPU capacity of 2 and a RAM capacity of 2048.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource utilization dummy-medium cpu=2 memory=2048
    ```

5.  Specify the utilization attributes that resource `dummy-large`{.literal} requires. In this example, `dummy-requires`{.literal} requires a CPU capacity of 1 and a RAM capacity of 3072.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource utilization dummy-large cpu=3 memory=3072
    ```

### [25.2. Pacemaker resource allocation](#pacemaker-resource-allocation) {#pacemaker-resource-allocation .title}

Pacemaker allocates resources according to node preference, node capacity, and resource allocation preference.

#### [25.2.1. Node preference](#node_preference) {#node-preference .title}

Pacemaker determines which node is preferred when allocating resources according to the following strategy.

-   The node with the highest node weight gets consumed first. Node weight is a score maintained by the cluster to represent node health.

-   If multiple nodes have the same node weight:

    -   If the `placement-strategy`{.literal} cluster property is `default`{.literal} or `utilization`{.literal}:

        -   The node that has the least number of allocated resources gets consumed first.
        -   If the numbers of allocated resources are equal, the first eligible node listed in the CIB gets consumed first.

    -   If the `placement-strategy`{.literal} cluster property is `balanced`{.literal}:

        -   The node that has the most free capacity gets consumed first.
        -   If the free capacities of the nodes are equal, the node that has the least number of allocated resources gets consumed first.
        -   If the free capacities of the nodes are equal and the number of allocated resources is equal, the first eligible node listed in the CIB gets consumed first.

    -   If the `placement-strategy`{.literal} cluster property is `minimal`{.literal}, the first eligible node listed in the CIB gets consumed first.

#### [25.2.2. Node capacity](#node_capacity) {#node-capacity .title}

Pacemaker determines which node has the most free capacity according to the following strategy.

-   If only one type of utilization attribute has been defined, free capacity is a simple numeric comparison.

-   If multiple types of utilization attributes have been defined, then the node that is numerically highest in the most attribute types has the most free capacity. For example:

    -   If NodeA has more free CPUs, and NodeB has more free memory, then their free capacities are equal.
    -   If NodeA has more free CPUs, while NodeB has more free memory and storage, then NodeB has more free capacity.

#### [25.2.3. Resource allocation preference](#resource_allocation_preference) {#resource-allocation-preference .title}

Pacemaker determines which resource is allocated first according to the following strategy.

-   The resource that has the highest priority gets allocated first. You can set a resource's priority when you create the resource.
-   If the priorities of the resources are equal, the resource that has the highest score on the node where it is running gets allocated first, to prevent resource shuffling.
-   If the resource scores on the nodes where the resources are running are equal or the resources are not running, the resource that has the highest score on the preferred node gets allocated first. If the resource scores on the preferred node are equal in this case, the first runnable resource listed in the CIB gets allocated first.

### [25.3. Resource placement strategy guidelines](#resource-placement-strategy-guidelines) {#resource-placement-strategy-guidelines .title}

Optimize Pacemaker's resource placement strategy by ensuring sufficient physical capacity, configuring buffers for overcommitment, and defining clear resource priorities.

-   Ensure that you have sufficient physical capacity.

    If the physical capacity of your nodes is being used to near maximum under normal conditions, then problems could occur during failover. Even without the utilization feature, you may start to experience timeouts and secondary failures.

-   Build some buffer into the capabilities you configure for the nodes.

    Advertise slightly more node resources than you physically have, on the assumption the that a Pacemaker resource will not use 100% of the configured amount of CPU, memory, and so forth all the time. This practice is sometimes called overcommit.

-   Specify resource priorities.

    If the cluster is going to sacrifice services, it should be the ones you care about least. Ensure that resource priorities are properly set so that your most important resources are scheduled first.

### [25.4. The NodeUtilization resource agent](#node-utilization-resource-agent) {#the-nodeutilization-resource-agent .title}

The `NodeUtilization`{.literal} resource agent can detect the system parameters of available CPU, host memory availability, and hypervisor memory availability and add these parameters into the CIB. You can run the agent as a clone resource to have it automatically populate these parameters on each node.

For information about the `NodeUtilization`{.literal} resource agent and the resource options for this agent, run the `pcs resource describe NodeUtilization`{.literal} command.

## [Chapter 26. Configuring a virtual domain as a resource](#configuring-virtual-domain-as-a-resource) {#chapter-26.-configuring-a-virtual-domain-as-a-resource .title}

You can configure a virtual domain that is managed by the `libvirt`{.literal} virtualization framework as a cluster resource with the `pcs resource create`{.literal} command, specifying `VirtualDomain`{.literal} as the resource type.

When configuring a virtual domain as a resource, take the following considerations into account:

-   A virtual domain should be stopped before you configure it as a cluster resource.
-   Once a virtual domain is a cluster resource, it should not be started, stopped, or migrated except through the cluster tools.
-   Do not configure a virtual domain that you have configured as a cluster resource to start when its host boots.
-   All nodes allowed to run a virtual domain must have access to the necessary configuration files and storage devices for that virtual domain.

If you want the cluster to manage services within the virtual domain itself, you can configure the virtual domain as a guest node.

### [26.1. Virtual domain resource options](#virtual-domain-resource-options) {#virtual-domain-resource-options .title}

Configure options for a `VirtualDomain`{.literal} resource to control virtual machine behavior.

+-------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                                     | Default          | Description                                                                                                                                                                                                                                                                                                                                                                                                              |
+:==========================================+:=================+:=========================================================================================================================================================================================================================================================================================================================================================================================================================+
| `config`{.literal}                        |                  | (required) Absolute path to the `libvirt`{.literal} configuration file for this virtual domain.                                                                                                                                                                                                                                                                                                                          |
+-------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `hypervisor`{.literal}                    | System dependent | Hypervisor URI to connect to. You can determine the system's default URI by running the `virsh --quiet uri`{.literal} command.                                                                                                                                                                                                                                                                                           |
+-------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `force_stop`{.literal}                    | `0`{.literal}    | Always forcefully shut down (\"destroy\") the domain on stop. The default behavior is to resort to a forceful shutdown only after a graceful shutdown attempt has failed. You should set this to `true`{.literal} only if your virtual domain (or your virtualization back end) does not support graceful shutdown.                                                                                                      |
+-------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `migration_transport`{.literal}           | System dependent | Transport used to connect to the remote hypervisor while migrating. If this parameter is omitted, the resource will use `libvirt`{.literal}\'s default transport to connect to the remote hypervisor.                                                                                                                                                                                                                    |
+-------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `migration_network_suffix`{.literal}      |                  | Use a dedicated migration network. The migration URI is composed by adding this parameter's value to the end of the node name. If the node name is a fully qualified domain name (FQDN), insert the suffix immediately before the first period (.) in the FQDN. Ensure that this composed host name is locally resolvable and the associated IP address is reachable through the favored network.                        |
+-------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `monitor_scripts`{.literal}               |                  | To additionally monitor services within the virtual domain, add this parameter with a list of scripts to monitor. *Note*: When monitor scripts are used, the `start`{.literal} and `migrate_from`{.literal} operations will complete only when all monitor scripts have completed successfully. Be sure to set the timeout of these operations to accommodate this delay                                                 |
+-------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `autoset_utilization_cpu`{.literal}       | `true`{.literal} | If set to `true`{.literal}, the agent will detect the number of `domainU`{.literal}\'s `vCPU`{.literal}s from `virsh`{.literal}, and put it into the CPU utilization of the resource when the monitor is executed.                                                                                                                                                                                                       |
+-------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `autoset_utilization_hv_memory`{.literal} | `true`{.literal} | If set it true, the agent will detect the number of `Max memory`{.literal} from `virsh`{.literal}, and put it into the `hv_memory`{.literal} utilization of the source when the monitor is executed.                                                                                                                                                                                                                     |
+-------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `migrateport`{.literal}                   | random highport  | This port will be used in the `qemu`{.literal} migrate URI. If unset, the port will be a random highport.                                                                                                                                                                                                                                                                                                                |
+-------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `snapshot`{.literal}                      |                  | Path to the snapshot directory where the virtual machine image will be stored. When this parameter is set, the virtual machine's RAM state will be saved to a file in the snapshot directory when stopped. If on start a state file is present for the domain, the domain will be restored to the same state it was in right before it stopped last. This option is incompatible with the `force_stop`{.literal} option. |
+-------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 26.1. Resource Options for Virtual Domain Resources

Show more

In addition to the `VirtualDomain`{.literal} resource options, you can configure the `allow-migrate`{.literal} metadata option to allow live migration of the resource to another node. When this option is set to `true`{.literal}, the resource can be migrated without loss of state. When this option is set to `false`{.literal}, which is the default state, the virtual domain will be shut down on the first node and then restarted on the second node when it is moved from one node to the other.

### [26.2. Creating the virtual domain resource](#creating-virtual-domain-resource) {#creating-the-virtual-domain-resource .title}

Create a `VirtualDomain`{.literal} resource in a cluster for a virtual machine you have previously created.

**Procedure**

1.  To create the `VirtualDomain`{.literal} resource agent for the management of the virtual machine, Pacemaker requires the virtual machine's `xml`{.literal} configuration file to be dumped to a file on disk. For example, if you created a virtual machine named `guest1`{.literal}, dump the `xml`{.literal} file to a file somewhere on one of the cluster nodes that will be allowed to run the guest. You can use a file name of your choosing; this example uses `/etc/pacemaker/guest1.xml`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # virsh dumpxml guest1 > /etc/pacemaker/guest1.xml
    ```

2.  Copy the virtual machine's `xml`{.literal} configuration file to all of the other cluster nodes that will be allowed to run the guest, in the same location on each node.

3.  Ensure that all of the nodes allowed to run the virtual domain have access to the necessary storage devices for that virtual domain.

4.  Separately test that the virtual domain can start and stop on each node that will run the virtual domain.

5.  If it is running, shut down the guest node. Pacemaker will start the node when it is configured in the cluster. The virtual machine should not be configured to start automatically when the host boots.

6.  Configure the `VirtualDomain`{.literal} resource with the `pcs resource create`{.literal} command. For example, the following command configures a `VirtualDomain`{.literal} resource named `VM`{.literal}. Since the `allow-migrate`{.literal} option is set to `true`{.literal} a `pcs resource move VM `{.literal}*`nodeX`{.literal}* command would be done as a live migration.

    In this example `migration_transport`{.literal} is set to `ssh`{.literal}. Note that for SSH migration to work properly, keyless logging must work between nodes.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create VM VirtualDomain config=/etc/pacemaker/guest1.xml migration_transport=ssh meta allow-migrate=true
    ```

## [Chapter 27. Configuring cluster quorum](#configuring-cluster-quorum) {#chapter-27.-configuring-cluster-quorum .title}

To maintain cluster integrity, systems use quorum to prevent data corruption. A cluster has quorum when more than half of its nodes are online. By default, Pacemaker stops all resources if the cluster loses quorum.

Quorum is established using a voting system. When a cluster node does not function as it should or loses communication with the rest of the cluster, the majority working nodes can vote to isolate and, if needed, fence the node for servicing.

For example, in a 6-node cluster, quorum is established when at least 4 cluster nodes are functioning. If the majority of nodes go offline or become unavailable, the cluster no longer has quorum and Pacemaker stops clustered services.

The quorum features in Pacemaker prevent what is also known as *split-brain*, a phenomenon where the cluster is separated from communication but each part continues working as separate clusters, potentially writing to the same data and possibly causing corruption or loss.

A Red Hat Enterprise Linux High Availability Add-On cluster uses the `votequorum`{.literal} service, in conjunction with fencing, to avoid split brain situations. A number of votes is assigned to each system in the cluster, and cluster operations are allowed to proceed only when a majority of votes is present. The service must be loaded into all nodes or none; if it is loaded into a subset of cluster nodes, the results will be unpredictable. For information about the configuration and operation of the `votequorum`{.literal} service, see the `votequorum`{.literal}(5) man page on your system.

### [27.1. Configuring quorum options](#quorum-options) {#configuring-quorum-options .title}

There are some special features of quorum configuration that you can set when you create a cluster with the `pcs cluster setup`{.literal} command.

+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option                               | Description                                                                                                                                                                                                                                                                                                                                                           |
+:=====================================+:======================================================================================================================================================================================================================================================================================================================================================================+
| `auto_tie_breaker`{.literal}         | When enabled, the cluster can suffer up to 50% of the nodes failing at the same time, in a deterministic fashion. The cluster partition, or the set of nodes that are still in contact with the `nodeid`{.literal} configured in `auto_tie_breaker_node`{.literal} (or lowest `nodeid`{.literal} if not set), will remain quorate. The other nodes will be inquorate. |
|                                      |                                                                                                                                                                                                                                                                                                                                                                       |
|                                      | The `auto_tie_breaker`{.literal .option} option is principally used for clusters with an even number of nodes, as it allows the cluster to continue operation with an even split. For more complex failures, such as multiple, uneven splits, it is recommended that you use a quorum device.                                                                         |
|                                      |                                                                                                                                                                                                                                                                                                                                                                       |
|                                      | The `auto_tie_breaker`{.literal .option} option is incompatible with quorum devices.                                                                                                                                                                                                                                                                                  |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `wait_for_all`{.literal}             | When enabled, the cluster will be quorate for the first time only after all nodes have been visible at least once at the same time.                                                                                                                                                                                                                                   |
|                                      |                                                                                                                                                                                                                                                                                                                                                                       |
|                                      | The `wait_for_all`{.literal .option} option is primarily used for two-node clusters and for even-node clusters using the quorum device `lms`{.literal} (last man standing) algorithm.                                                                                                                                                                                 |
|                                      |                                                                                                                                                                                                                                                                                                                                                                       |
|                                      | The `wait_for_all`{.literal .option} option is automatically enabled when a cluster has two nodes, does not use a quorum device, and `auto_tie_breaker`{.literal .option} is disabled. You can override this by explicitly setting `wait_for_all`{.literal .option} to 0.                                                                                             |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `last_man_standing`{.literal}        | When enabled, the cluster can dynamically recalculate `expected_votes`{.literal} and quorum under specific circumstances. You must enable `wait_for_all`{.literal} when you enable this option. The `last_man_standing`{.literal} option is incompatible with quorum devices.                                                                                         |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `last_man_standing_window`{.literal} | The time, in milliseconds, to wait before recalculating `expected_votes`{.literal} and quorum after a cluster loses nodes.                                                                                                                                                                                                                                            |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 27.1. Quorum Options

Show more

For further information about configuring and using these options, see the `votequorum`{.literal}(5) man page on your system.

### [27.2. Modifying quorum options](#modifying-quorum-options) {#modifying-quorum-options .title}

You can modify general quorum options for your cluster with the `pcs quorum update`{.literal} command. Running this command requires that the cluster be stopped. For information on the quorum options, see the `votequorum`{.literal}(5) man page on your system.

The format of the `pcs quorum update`{.literal} command is as follows.

``` {.language-plaintext tabindex="-1"}
# pcs quorum update [auto_tie_breaker=[0|1]] [last_man_standing=[0|1]] [last_man_standing_window=[time-in-ms] [wait_for_all=[0|1]]
```

The following example procedure modifies the `wait_for_all`{.literal} quorum option and displays the updated status of the option. Note that the system does not allow you to modify this option while the cluster is running.

**Procedure**

1.  Attempt to modify the `wait_for_all`{.literal} quorum option on a running system.

    ``` {.language-plaintext tabindex="-1"}
    [root@node1:~]# pcs quorum update wait_for_all=1
    ```

    ``` {.language-plaintext tabindex="-1"}
    Checking corosync is not running on nodes...
    Error: node1: corosync is running
    Error: node2: corosync is running
    ```

2.  Stop the cluster processes to modify the `wait_for_all`{.literal} quorum option.

    ``` {.language-plaintext tabindex="-1"}
    [root@node1:~]# pcs cluster stop --all
    ```

    ``` {.language-plaintext tabindex="-1"}
    node2: Stopping Cluster (pacemaker)...
    node1: Stopping Cluster (pacemaker)...
    node1: Stopping Cluster (corosync)...
    node2: Stopping Cluster (corosync)...
    ```

3.  Modify the `wait_for_all`{.literal} quorum option on a stopped system.

    ``` {.language-plaintext tabindex="-1"}
    [root@node1:~]# pcs quorum update wait_for_all=1
    ```

    ``` {.language-plaintext tabindex="-1"}
    Checking corosync is not running on nodes...
    node2: corosync is not running
    node1: corosync is not running
    Sending updated corosync.conf to nodes...
    node1: Succeeded
    node2: Succeeded
    ```

4.  Display the quorum configuration

    ``` {.language-plaintext tabindex="-1"}
    [root@node1:~]# pcs quorum config
    ```

    ``` {.language-plaintext tabindex="-1"}
    Options:
      wait_for_all: 1
    ```

### [27.3. Displaying quorum configuration and status](#displaying-quorum-configuration-status) {#displaying-quorum-configuration-and-status .title}

Once a cluster is running, you can enter the following cluster quorum commands to display the quorum configuration and status.

**Procedure**

-   Display the quorum configuration:

    ``` {.language-plaintext tabindex="-1"}
    # pcs quorum [config]
    ```

-   Display the quorum runtime status:

    ``` {.language-plaintext tabindex="-1"}
    # pcs quorum status
    ```

### [27.4. Running inquorate clusters](#running-inquorate-clusters) {#running-inquorate-clusters .title}

If removing nodes from a cluster causes quorum loss, adjust the `expected_votes`{.literal} parameter on the running cluster by using the `pcs quorum expected-votes`{.literal} command. This allows the cluster to continue operating without quorum.

Warning

Changing the expected votes in a live cluster should be done with extreme caution. If less than 50% of the cluster is running because you have manually changed the expected votes, then the other nodes in the cluster could be started separately and run cluster services, causing data corruption and other unexpected results. If you change this value, you should ensure that the `wait_for_all`{.literal} parameter is enabled.

**Procedure**

-   The following command sets the expected votes in the live cluster to the specified value. This affects the live cluster only and does not change the configuration file; the value of `expected_votes`{.literal} is reset to the value in the configuration file in the event of a reload.

    ``` {.language-plaintext tabindex="-1"}
    # pcs quorum expected-votes votes
    ```

-   In a situation in which you know that the cluster is inquorate but you want the cluster to proceed with resource management, you can use the `pcs quorum unblock`{.literal .command} command to prevent the cluster from waiting for all nodes when establishing quorum.

    Note

    This command should be used with extreme caution. Before issuing this command, it is imperative that you ensure that nodes that are not currently in the cluster are switched off and have no access to shared resources.

    ``` {.language-plaintext tabindex="-1"}
    # pcs quorum unblock
    ```

### [27.5. Additional resources](#configuring-cluster-quorum_275-additional-resources) {#additional-resources-3 .title}

-   [Exploring Concepts of RHEL High Availability Clusters - Quorum](https://access.redhat.com/articles/2824071)

## [Chapter 28. Configuring quorum devices](#configuring-quorum-devices) {#chapter-28.-configuring-quorum-devices .title}

Configure a quorum device to act as a third-party arbitrator, allowing the cluster to sustain more node failures. This is recommended for clusters with an even number of nodes. In two-node clusters, the device determines which node survives a split-brain scenario.

You must take the following into account when configuring a quorum device.

-   It is recommended that a quorum device be run on a different physical network at the same site as the cluster that uses the quorum device. Ideally, the quorum device host should be in a separate rack than the main cluster, or at least on a separate PSU and not on the same network segment as the corosync ring or rings.
-   You cannot use more than one quorum device in a cluster at the same time.
-   Although you cannot use more than one quorum device in a cluster at the same time, a single quorum device may be used by several clusters at the same time. Each cluster using that quorum device can use different algorithms and quorum options, as those are stored on the cluster nodes themselves. For example, a single quorum device can be used by one cluster with an `ffsplit`{.literal} (fifty/fifty split) algorithm and by a second cluster with an `lms`{.literal} (last man standing) algorithm.
-   A quorum device should not be run on an existing cluster node.

### [28.1. Installing quorum device packages](#installing-quorum-device-packages) {#installing-quorum-device-packages .title}

Install the packages you require for configuring a quorum device for a cluster.

**Procedure**

1.  Install `corosync-qdevice`{.literal} on the nodes of an existing cluster.

    ``` {.language-plaintext tabindex="-1"}
    [root@node1:~]# dnf install corosync-qdevice
    [root@node2:~]# dnf install corosync-qdevice
    ```

2.  Install `pcs`{.literal} and `corosync-qnetd`{.literal} on the quorum device host.

    ``` {.language-plaintext tabindex="-1"}
    [root@qdevice:~]# dnf install pcs corosync-qnetd
    ```

3.  Start the `pcsd`{.literal} service and enable `pcsd`{.literal} at system start on the quorum device host.

    ``` {.language-plaintext tabindex="-1"}
    [root@qdevice:~]# systemctl start pcsd.service
    [root@qdevice:~]# systemctl enable pcsd.service
    ```

### [28.2. Configuring a quorum device](#configuring-quorum-device) {#configuring-a-quorum-device .title}

You can configure a quorum device and add it to the cluster.

In this example:

-   The node used for a quorum device is `qdevice`{.literal}.

-   The quorum device model is `net`{.literal}, which is currently the only supported model. The `net`{.literal} model supports the following algorithms:

    -   `ffsplit`{.literal}: fifty-fifty split. This provides exactly one vote to the partition with the highest number of active nodes.

    -   `lms`{.literal}: last-man-standing. If the node is the only one left in the cluster that can see the `qnetd`{.literal} server, then it returns a vote.

        Warning

        The LMS algorithm allows the cluster to remain quorate even with only one remaining node, but it also means that the voting power of the quorum device is great since it is the same as number_of_nodes - 1. Losing connection with the quorum device means losing number_of_nodes - 1 votes, which means that only a cluster with all nodes active can remain quorate (by overvoting the quorum device); any other cluster becomes inquorate.

        For more detailed information about the implementation of these algorithms, see the `corosync-qdevice`{.literal}(8) man page on your system.

-   The cluster nodes are `node1`{.literal} and `node2`{.literal}.

**Procedure**

1.  On the node that you will use to host your quorum device, configure the quorum device with the following command. This command configures and starts the quorum device model `net`{.literal} and configures the device to start on boot.

    ``` {.language-plaintext tabindex="-1"}
    [root@qdevice:~]# pcs qdevice setup model net --enable --start
    ```

    ``` {.language-plaintext tabindex="-1"}
    Quorum device 'net' initialized
    quorum device enabled
    Starting quorum device...
    quorum device started
    ```

    After configuring the quorum device, you can check its status. This should show that the `corosync-qnetd`{.literal} daemon is running and, at this point, there are no clients connected to it. The `--full`{.literal} command option provides detailed output.

    ``` {.language-plaintext tabindex="-1"}
    [root@qdevice:~]# pcs qdevice status net --full
    ```

    ``` {.language-plaintext tabindex="-1"}
    QNetd address:                  *:5403
    TLS:                            Supported (client certificate required)
    Connected clients:              0
    Connected clusters:             0
    Maximum send/receive size:      32768/32768 bytes
    ```

2.  Enable the ports on the firewall needed by the `pcsd`{.literal} daemon and the `net`{.literal} quorum device by enabling the `high-availability`{.literal} service on `firewalld`{.literal} with following commands.

    ``` {.language-plaintext tabindex="-1"}
    [root@qdevice:~]# firewall-cmd --permanent --add-service=high-availability
    [root@qdevice:~]# firewall-cmd --add-service=high-availability
    ```

3.  From one of the nodes in the existing cluster, authenticate user `hacluster`{.literal} on the node that is hosting the quorum device. This allows `pcs`{.literal} on the cluster to connect to `pcs`{.literal} on the `qdevice`{.literal} host, but does not allow `pcs`{.literal} on the `qdevice`{.literal} host to connect to `pcs`{.literal} on the cluster.

    ``` {.language-plaintext tabindex="-1"}
    [root@node1:~] # pcs host auth qdevice
    ```

    ``` {.language-plaintext tabindex="-1"}
    Username: hacluster
    Password:
    qdevice: Authorized
    ```

4.  Add the quorum device to the cluster.

    Before adding the quorum device, you can check the current configuration and status for the quorum device for later comparison. The output for these commands indicates that the cluster is not yet using a quorum device, and the `Qdevice`{.literal} membership status for each node is `NR`{.literal} (Not Registered).

    ``` {.language-plaintext tabindex="-1"}
    [root@node1:~]# pcs quorum config
    ```

    ``` {.language-plaintext tabindex="-1"}
    Options:
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@node1:~]# pcs quorum status
    ```

    ``` {.language-plaintext tabindex="-1"}
    Quorum information
    ------------------
    Date:             Wed Jun 29 13:15:36 2016
    Quorum provider:  corosync_votequorum
    Nodes:            2
    Node ID:          1
    Ring ID:          1/8272
    Quorate:          Yes

    Votequorum information
    ----------------------
    Expected votes:   2
    Highest expected: 2
    Total votes:      2
    Quorum:           1
    Flags:            2Node Quorate

    Membership information
    ----------------------
        Nodeid      Votes    Qdevice Name
             1          1         NR node1 (local)
             2          1         NR node2
    ```

    The following command adds the quorum device that you have previously created to the cluster. You cannot use more than one quorum device in a cluster at the same time. However, one quorum device can be used by several clusters at the same time. This example command configures the quorum device to use the `ffsplit`{.literal} algorithm. For information about the configuration options for the quorum device, see the `corosync-qdevice`{.literal}(8) man page on your system.

    ``` {.language-plaintext tabindex="-1"}
    [root@node1:~]# pcs quorum device add model net host=qdevice algorithm=ffsplit
    ```

    ``` {.language-plaintext tabindex="-1"}
    Setting up qdevice certificates on nodes...
    node2: Succeeded
    node1: Succeeded
    Enabling corosync-qdevice...
    node1: corosync-qdevice enabled
    node2: corosync-qdevice enabled
    Sending updated corosync.conf to nodes...
    node1: Succeeded
    node2: Succeeded
    Corosync configuration reloaded
    Starting corosync-qdevice...
    node1: corosync-qdevice started
    node2: corosync-qdevice started
    ```

5.  Check the configuration status of the quorum device.

    From the cluster side, you can run the following commands to see how the configuration has changed.

    The `pcs quorum config`{.literal} shows the quorum device that has been configured.

    ``` {.language-plaintext tabindex="-1"}
    [root@node1:~]# pcs quorum config
    ```

    ``` {.language-plaintext tabindex="-1"}
    Options:
    Device:
      Model: net
        algorithm: ffsplit
        host: qdevice
    ```

    The `pcs quorum status`{.literal} command shows the quorum runtime status, indicating that the quorum device is in use. The meanings of the `Qdevice`{.literal} membership information status values for each cluster node are as follows:

    -   `A/NA`{.literal} - The quorum device is alive or not alive, indicating whether there is a heartbeat between `qdevice`{.literal} and `corosync`{.literal}. This should always indicate that the quorum device is alive.

    -   `V/NV`{.literal} - `V`{.literal} is set when the quorum device has given a vote to a node. In this example, both nodes are set to `V`{.literal} since they can communicate with each other. If the cluster were to split into two single-node clusters, one of the nodes would be set to `V`{.literal} and the other node would be set to `NV`{.literal}.

    -   `MW/NMW`{.literal} - The internal quorum device flag is set (`MW`{.literal}) or not set (`NMW`{.literal}). By default the flag is not set and the value is `NMW`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        [root@node1:~]# pcs quorum status
        ```

        ``` {.language-plaintext tabindex="-1"}
        Quorum information
        ------------------
        Date:             Wed Jun 29 13:17:02 2016
        Quorum provider:  corosync_votequorum
        Nodes:            2
        Node ID:          1
        Ring ID:          1/8272
        Quorate:          Yes

        Votequorum information
        ----------------------
        Expected votes:   3
        Highest expected: 3
        Total votes:      3
        Quorum:           2
        Flags:            Quorate Qdevice

        Membership information
        ----------------------
            Nodeid      Votes    Qdevice Name
                 1          1    A,V,NMW node1 (local)
                 2          1    A,V,NMW node2
                 0          1            Qdevice
        ```

        The `pcs quorum device status`{.literal} shows the quorum device runtime status.

        ``` {.language-plaintext tabindex="-1"}
        [root@node1:~]# pcs quorum device status
        ```

        ``` {.language-plaintext tabindex="-1"}
        Qdevice information
        -------------------
        Model:                  Net
        Node ID:                1
        Configured node list:
            0   Node ID = 1
            1   Node ID = 2
        Membership node list:   1, 2

        Qdevice-net information
        ----------------------
        Cluster name:           mycluster
        QNetd host:             qdevice:5403
        Algorithm:              ffsplit
        Tie-breaker:            Node with lowest node ID
        State:                  Connected
        ```

        From the quorum device side, you can run the following status command, which shows the status of the `corosync-qnetd`{.literal} daemon.

        ``` {.language-plaintext tabindex="-1"}
        [root@qdevice:~]# pcs qdevice status net --full
        ```

        ``` {.language-plaintext tabindex="-1"}
        QNetd address:                  *:5403
        TLS:                            Supported (client certificate required)
        Connected clients:              2
        Connected clusters:             1
        Maximum send/receive size:      32768/32768 bytes
        Cluster "mycluster":
            Algorithm:          ffsplit
            Tie-breaker:        Node with lowest node ID
            Node ID 2:
                Client address:         ::ffff:192.168.122.122:50028
                HB interval:            8000ms
                Configured node list:   1, 2
                Ring ID:                1.2050
                Membership node list:   1, 2
                TLS active:             Yes (client certificate verified)
                Vote:                   ACK (ACK)
            Node ID 1:
                Client address:         ::ffff:192.168.122.121:48786
                HB interval:            8000ms
                Configured node list:   1, 2
                Ring ID:                1.2050
                Membership node list:   1, 2
                TLS active:             Yes (client certificate verified)
                Vote:                   ACK (ACK)
        ```

### [28.3. Managing the quorum device service](#managing-quorum-device-service) {#managing-the-quorum-device-service .title}

PCS provides the ability to manage the quorum device service on the local host (`corosync-qnetd`{.literal}) with the `pcs qdevice`{.literal} command. Note that these commands affect only the `corosync-qnetd`{.literal} service.

``` {.language-plaintext tabindex="-1"}
[root@qdevice:~]# pcs qdevice start net
[root@qdevice:~]# pcs qdevice stop net
[root@qdevice:~]# pcs qdevice enable net
[root@qdevice:~]# pcs qdevice disable net
[root@qdevice:~]# pcs qdevice kill net
```

### [28.4. Managing a quorum device in a cluster](#managing-quorum-device-settings) {#managing-a-quorum-device-in-a-cluster .title}

There are a variety of `pcs`{.literal} commands that you can use to change the quorum device settings in a cluster, disable a quorum device, and remove a quorum device.

**Changing quorum device settings**

You can change the setting of a quorum device with the `pcs quorum device update`{.literal} command.

Warning

To change the `host`{.literal} option of quorum device model `net`{.literal}, use the `pcs quorum device remove`{.literal} and the `pcs quorum device add`{.literal} commands to configure the configuration properly, unless the old and the new host are the same machine.

The following command changes the quorum device algorithm to `lms`{.literal}:

``` {.language-plaintext tabindex="-1"}
[root@node1:~]# pcs quorum device update model algorithm=lms
```

``` {.language-plaintext tabindex="-1"}
Sending updated corosync.conf to nodes...
node1: Succeeded
node2: Succeeded
Corosync configuration reloaded
Reloading qdevice configuration on nodes...
node1: corosync-qdevice stopped
node2: corosync-qdevice stopped
node1: corosync-qdevice started
node2: corosync-qdevice started
```

**Removing a quorum device**

The following command removes a quorum device configured on a cluster node:

``` {.language-plaintext tabindex="-1"}
[root@node1:~]# pcs quorum device remove
```

``` {.language-plaintext tabindex="-1"}
Sending updated corosync.conf to nodes...
node1: Succeeded
node2: Succeeded
Corosync configuration reloaded
Disabling corosync-qdevice...
node1: corosync-qdevice disabled
node2: corosync-qdevice disabled
Stopping corosync-qdevice...
node1: corosync-qdevice stopped
node2: corosync-qdevice stopped
Removing qdevice certificates from nodes...
node1: Succeeded
node2: Succeeded
```

After you have removed a quorum device, you should see the following error message when displaying the quorum device status.

``` {.language-plaintext tabindex="-1"}
[root@node1:~]# pcs quorum device status
```

``` {.language-plaintext tabindex="-1"}
Error: Unable to get quorum status: corosync-qdevice-tool: Can't connect to QDevice socket (is QDevice running?): No such file or directory
```

**Destroying a quorum device**

The following command disables and stops a quorum device on the quorum device host and deletes all of its configuration files.

``` {.language-plaintext tabindex="-1"}
[root@qdevice:~]# pcs qdevice destroy net
```

``` {.language-plaintext tabindex="-1"}
Stopping quorum device...
quorum device stopped
quorum device disabled
Quorum device 'net' configuration files removed
```

## [Chapter 29. Triggering scripts for cluster events](#configuring-pacemaker-alert-agents) {#chapter-29.-triggering-scripts-for-cluster-events .title}

Configure Pacemaker cluster alerts to trigger external actions when cluster events occur, such as node failures, configuration changes, or resource state changes. Alert agents run these external programs similarly to resource agents.

The cluster passes information about the event to the agent by means of environment variables. Agents can do anything with this information, such as send an email message or log to a file or update a monitoring system.

-   Pacemaker provides several sample alert agents, which are installed in `/usr/share/pacemaker/alerts`{.literal} by default. These sample scripts may be copied and used as is, or they may be used as templates to be edited to suit your purposes. See the source code of the sample agents for the full set of attributes they support.
-   If the sample alert agents do not meet your needs, you can write your own alert agents for a Pacemaker alert to call.

### [29.1. Installing and configuring sample alert agents](#using-sample-alert-agents) {#installing-and-configuring-sample-alert-agents .title}

When you use one of the sample alert agents, you should review the script to ensure that it suits your needs. These sample agents are provided as a starting point for custom scripts for specific cluster environments.

Warning

While Red Hat supports the interfaces that the alert agents scripts use to communicate with Pacemaker, Red Hat does not provide support for the custom agents themselves.

#### [29.1.1. Prerequisites](#prerequisites_2) {#prerequisites-1 .title}

-   Install the agent on each node in the cluster

    ``` {.language-plaintext tabindex="-1"}
    # install --mode=0755 /usr/share/pacemaker/alerts/alert_file.sh.sample /var/lib/pacemaker/alert_file.sh
    ```

    After you have installed the script, you can create an alert that uses the script.

#### [29.1.2. Configuring an alert that uses the alert_file.sh alert agent](#configuring-an-alert-that-uses-the-alert-file-alert-agent) {#configuring-an-alert-that-uses-the-alert_file.sh-alert-agent .title}

You can install the `alert_file.sh`{.literal} alert agent and configure an alert to log events to a file. Alert agents run as the user `hacluster`{.literal}, which has a minimal set of permissions.

**Procedure**

1.  On each node in the cluster, install the `alert_file.sh.sample`{.literal} script as `alert_file.sh`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # install --mode=0755 /usr/share/pacemaker/alerts/alert_file.sh.sample /var/lib/pacemaker/alert_file.sh
    ```

2.  On each node in the cluster, create the log file that will be used to record the events.

    ``` {.language-plaintext tabindex="-1"}
    # touch /var/log/pcmk_alert_file.log
    ```

    a.  Change the ownership of the file `pcmk_alert_file.log`{.literal} to user `hacluster`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        # chown hacluster:haclient /var/log/pcmk_alert_file.log
        ```

    b.  Change the permissions for the file `pcmk_alert_file.log`{.literal} to read and write for the user `hacluster`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        # chmod 600 /var/log/pcmk_alert_file.log
        ```

3.  On one node in the cluster, create the alert.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert create id=alert_file description="Log events to a file." path=/var/lib/pacemaker/alert_file.sh
    ```

4.  Add the path to the log file as the recipient for the alert.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert recipient add alert_file id=my-alert_logfile value=/var/log/pcmk_alert_file.log
    ```

#### [29.1.3. Configuring an alert that uses the alert_snmp.sh alert agent](#configuring-an-alert-that-uses-the-alert-snmp-alert-agent) {#configuring-an-alert-that-uses-the-alert_snmp.sh-alert-agent .title}

You can install the `alert_snmp.sh.sample`{.literal} script as `alert_snmp.sh`{.literal} and configure an alert that uses the installed `alert_snmp.sh`{.literal} alert agent to send cluster events as SNMP traps. By default, the script will send all events except successful monitor calls to the SNMP server.

**Procedure**

1.  On each node in the cluster, install the `alert_snmp.sh.sample`{.literal} script as `alert_snmp.sh`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # install --mode=0755 /usr/share/pacemaker/alerts/alert_snmp.sh.sample /var/lib/pacemaker/alert_snmp.sh
    ```

2.  On one node in the cluster, configure an alert that uses the `alert_snmp.sh`{.literal} agent, configuring the timestamp format as a meta option.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert create id=snmp_alert path=/var/lib/pacemaker/alert_snmp.sh meta timestamp-format="%Y-%m-%d,%H:%M:%S.%01N"
    ```

3.  Configure a recipient for the alert

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert recipient add snmp_alert value=192.168.1.2
    ```

4.  Display the alert configuration.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert
    ```

    ``` {.language-plaintext tabindex="-1"}
    Alerts:
     Alert: snmp_alert (path=/var/lib/pacemaker/alert_snmp.sh)
      Meta options: timestamp-format=%Y-%m-%d,%H:%M:%S.%01N.
      Recipients:
       Recipient: snmp_alert-recipient (value=192.168.1.2)
    ```

#### [29.1.4. Configuring an alert that uses the alert_smtp.sh alert agent](#configuring-an-alert-that-uses-the-alert-smtp-alert-agent) {#configuring-an-alert-that-uses-the-alert_smtp.sh-alert-agent .title}

You can install the `alert_smtp.sh`{.literal} agent and then configure an alert that uses the installed alert agent to send cluster events as email messages.

**Procedure**

1.  On each node in the cluster, install the `alert_smtp.sh.sample`{.literal} script as `alert_smtp.sh`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # install --mode=0755 /usr/share/pacemaker/alerts/alert_smtp.sh.sample /var/lib/pacemaker/alert_smtp.sh
    ```

2.  On one node in the cluster, configure an alert to send cluster events as email messages.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert create id=smtp_alert path=/var/lib/pacemaker/alert_smtp.sh options email_sender=donotreply@example.com
    ```

3.  Configure a recipient for the alert.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert recipient add smtp_alert value=admin@example.com
    ```

4.  Display the alert configuration.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert
    ```

    ``` {.language-plaintext tabindex="-1"}
    Alerts:
     Alert: smtp_alert (path=/var/lib/pacemaker/alert_smtp.sh)
      Options: email_sender=donotreply@example.com
      Recipients:
       Recipient: smtp_alert-recipient (value=admin@example.com)
    ```

### [29.2. Creating a cluster alert](#creating-cluster-alert) {#creating-a-cluster-alert .title}

You can create a cluster alert. The options that you configure are agent-specific configuration values that are passed to the alert agent script at the path you specify as additional environment variables. If you do not specify a value for `id`{.literal}, one will be generated.

**Procedure**

-   Create a cluster alert:

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert create path=path [id=alert-id] [description=description] [options [option=value]...] [meta [meta-option=value]...]
    ```

    Multiple alert agents may be configured; the cluster will call all of them for each event. Alert agents will be called only on cluster nodes. They will be called for events involving Pacemaker Remote nodes, but they will never be called on those nodes.

-   The following example creates a simple alert that will call `myscript.sh`{.literal} for each event.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert create id=my_alert path=/path/to/myscript.sh
    ```

**Additional resources**

-   [Creating and modifying a cluster alert](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_managing_high_availability_clusters/index#cluster-alert-configuration)

### [29.3. Displaying, modifying, and removing cluster alerts](#managing-cluster-alert) {#displaying-modifying-and-removing-cluster-alerts .title}

There are a variety of `pcs`{.literal} commands you can use to display, modify, and remove cluster alerts.

**Displaying configured cluster alerts**

The following command shows all configured alerts along with the values of the configured options:

``` {.language-plaintext tabindex="-1"}
# pcs alert [config]
```

**Modifying a configured cluster alert**

The following command updates an existing alert with the specified *alert-id* value:

``` {.language-plaintext tabindex="-1"}
# pcs alert update alert-id [path=path] [description=description] [options [option=value]...] [meta [meta-option=value]...]
```

**Removing a cluster alert**

The following command removes an alert with the specified *alert-id* value:

``` {.language-plaintext tabindex="-1"}
# pcs alert remove alert-id
```

Alternately, you can run the `pcs alert delete`{.literal} command, which is identical to the `pcs alert remove`{.literal} command. Both the `pcs alert delete`{.literal} and the `pcs alert remove`{.literal} commands allow you to specify more than one alert to be deleted.

### [29.4. Configuring cluster alert recipients](#configuring-alert-recipients) {#configuring-cluster-alert-recipients .title}

Configure alerts with one or more recipients. The cluster calls the agent separately for each recipient. The recipient may be anything the alert agent can recognize: an IP address, an email address, a file name, or whatever the particular agent supports.

**Adding a recipient to a configured cluster alert**

The following command adds a new recipient to the specified alert.

``` {.language-plaintext tabindex="-1"}
# pcs alert recipient add alert-id value=recipient-value [id=recipient-id] [description=description] [options [option=value]...] [meta [meta-option=value]...]
```

The following example command adds the alert recipient `my-alert-recipient`{.literal} with a recipient ID of `my-recipient-id`{.literal} to the alert `my-alert`{.literal}. This will configure the cluster to call the alert script that has been configured for `my-alert`{.literal} for each event, passing the recipient `some-address`{.literal} as an environment variable.

``` {.language-plaintext tabindex="-1"}
#  pcs alert recipient add my-alert value=my-alert-recipient id=my-recipient-id options value=some-address
```

**Updating an existing alert recipient**

The following command updates an existing alert recipient.

``` {.language-plaintext tabindex="-1"}
# pcs alert recipient update recipient-id [value=recipient-value] [description=description] [options [option=value]...] [meta [meta-option=value]...]
```

**Removing an alert recipient**

The following command removes the specified alert recipient.

``` {.language-plaintext tabindex="-1"}
# pcs alert recipient remove recipient-id
```

Alternately, you can run the `pcs alert recipient delete`{.literal} command, which is identical to the `pcs alert recipient remove`{.literal} command. Both the `pcs alert recipient remove`{.literal} and the `pcs alert recipient delete`{.literal} commands allow you to remove more than one alert recipient.

### [29.5. Configuring cluster alert meta options](#cluster-alert-meta-options) {#configuring-cluster-alert-meta-options .title}

Configure alert meta options to control how the cluster invokes alert agents, including timeout values, timestamp formats, and enable/disable settings per agent or recipient.

+------------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Meta-Attribute               | Default                   | Description                                                                                                                                                                               |
+:=============================+:==========================+:==========================================================================================================================================================================================+
| `enabled`{.literal}          | `true`{.literal}          | If set to `false`{.literal} for an alert, the alert is not used. If set to `true`{.literal} for an alert and `false`{.literal} for a recipient of that alert, that recipient is not used. |
+------------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `timestamp-format`{.literal} | `%H:%M:%S.%06N`{.literal} | Format the cluster uses when sending the event timestamp to the agent. Specify this string as used with the `date`{.literal}(1) command.                                                  |
+------------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `timeout`{.literal}          | `30s`{.literal}           | Time limit for the alert agent to complete execution before termination.                                                                                                                  |
+------------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 29.1. Alert meta options

Show more

The following example procedure configures cluster alert meta options for an alert agent and its recipients. The procedure configures an alert that calls the `myscript.sh`{.literal} script and adds two recipients to the alert, causing the script to be called twice for each event.

**Procedure**

1.  Configure an alert that calls the script `myscript.sh`{.literal} and that uses a 15-second timeout.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert create id=my-alert path=/path/to/myscript.sh meta timeout=15s
    ```

2.  Add an alert recipient that has an ID of `my-alert-recipient1`{.literal}, passing the call to the recipient `someuser@example.com`{.literal} with a timestamp in the format %D %H:%M.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert recipient add my-alert value=someuser@example.com id=my-alert-recipient1 meta timestamp-format="%D %H:%M"
    ```

3.  Add an alert recipient that has an ID of `my-alert-recipient2`{.literal}, passing the call to the recipient `otheruser@example.com`{.literal} with a timestamp in the format %c.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert recipient add my-alert value=otheruser@example.com id=my-alert-recipient2 meta timestamp-format="%c"
    ```

### [29.6. Displaying configured cluster alerts as pcs commands](#displaying-cluster-alert-configurations-as-pcs-commands) {#displaying-configured-cluster-alerts-as-pcs-commands .title}

You can export cluster alerts as a series of `pcs`{.literal} commands by using the `--output-format=cmd`{.literal} option. This is useful for scripting, automation, or replicating the same configuration on a different system.

Note

You can display the configured cluster alerts in one of three formats:

-   `text`{.literal}: Displays the output in plain text. This is the default format.
-   `json`{.literal}: Displays the output in a machine-readable JSON format, which is useful for scripting and automation.
-   `cmd`{.literal}: Displays the output as a series of `pcs`{.literal} commands, which you can use to recreate the same alert or other cluster configuration part on a different system.

**Procedure**

-   To display the configured alerts as a series of `pcs`{.literal} commands:

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert config --output-format=cmd
    ```

    **Example output**

    ``` {.language-plaintext tabindex="-1"}
    pcs alert create smtp alert_id_1 host=smtp.example.com to=admin@example.com
    pcs alert create snmp alert_id_2 host=snmp.example.com community=public
    ```

### [29.7. Creating and modifying a cluster alert](#cluster-alert-configuration) {#creating-and-modifying-a-cluster-alert .title}

You can create alerts, add recipients, modify an alert, remove an alert, and display the configured alerts at each step.

While you must install the alert agents themselves on each node in a cluster, you need to run the `pcs`{.literal} commands only once.

**Procedure**

1.  Create a simple alert. Since no alert ID value is specified, the system creates an alert ID value of `alert`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert create path=/my/path
    ```

2.  Add a recipient of `rec_value`{.literal} to the alert. Since this command does not specify a recipient ID, the value of `alert-recipient`{.literal} is used as the recipient ID.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert recipient add alert value=rec_value
    ```

3.  Add a second recipient of `rec_value2`{.literal} to the alert. This command specifies a recipient ID of `my-recipient`{.literal} for the recipient.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert recipient add alert value=rec_value2 id=my-recipient
    ```

4.  Add a second alert, with an alert ID of `my-alert`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert create id=my-alert path=/path/to/script description=alert_description options option1=value1 opt=val meta timeout=50s timestamp-format="%H%B%S"
    ```

5.  Add a recipient for that alert for the second alert with a recipient value of `my-other-recipient`{.literal}. Since no recipient ID is specified, the system provides a recipient id of `my-alert-recipient`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert recipient add my-alert value=my-other-recipient
    ```

6.  Modify the alert values for the alert `my-alert`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert update my-alert options option1=newvalue1 meta timestamp-format="%H%M%S"
    ```

7.  Modify the alert values for the recipient `my-alert-recipient`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert recipient update my-alert-recipient options option1=new meta timeout=60s
    ```

8.  Remove the recipient `my-alert-recipient`{.literal} from `alert`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert recipient remove my-recipient
    ```

9.  Remove the alert `myalert`{.literal} from the configuration.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert remove myalert
    ```

**Verification**

1.  Display the alert configuration.

    ``` {.language-plaintext tabindex="-1"}
    # pcs alert
    ```

    ``` {.language-plaintext tabindex="-1"}
    Alerts:
     Alert: alert (path=/my/path)
      Recipients:
       Recipient: alert-recipient (value=rec_value)
    ```

### [29.8. Writing a cluster alert agent](#writing-cluster-alert-agent) {#writing-a-cluster-alert-agent .title}

There are three types of Pacemaker cluster alerts: node alerts, fencing alerts, and resource alerts. The environment variables that are passed to the alert agents can differ, depending on the type of alert.

Environment variables passed to alert agents

:   

+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Environment Variable                | Description                                                                                                                                                                                                                                                                                                                                             |
+:====================================+:========================================================================================================================================================================================================================================================================================================================================================+
| `CRM_alert_kind`{.literal}          | The type of alert (node, fencing, or resource)                                                                                                                                                                                                                                                                                                          |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CRM_alert_version`{.literal}       | The version of Pacemaker sending the alert                                                                                                                                                                                                                                                                                                              |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CRM_alert_recipient`{.literal}     | The configured recipient                                                                                                                                                                                                                                                                                                                                |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CRM_alert_node_sequence`{.literal} | A sequence number increased whenever an alert is being issued on the local node, which can be used to reference the order in which alerts have been issued by Pacemaker. An alert for an event that happened later in time reliably has a higher sequence number than alerts for earlier events. Be aware that this number has no cluster-wide meaning. |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CRM_alert_timestamp`{.literal}     | A timestamp created before running the agent, in the format specified by the `timestamp-format`{.literal} meta option. This allows the agent to have a reliable, high-precision time of when the event occurred, regardless of when the agent itself was invoked (which could potentially be delayed due to system load or other circumstances).        |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CRM_alert_node`{.literal}          | Name of affected node                                                                                                                                                                                                                                                                                                                                   |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CRM_alert_desc`{.literal}          | Detail about event. For node alerts, this is the node's current state (member or lost). For fencing alerts, this is a summary of the requested fencing operation, including origin, target, and fencing operation error code, if any. For resource alerts, this is a readable string equivalent of `CRM_alert_status`{.literal}.                        |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CRM_alert_nodeid`{.literal}        | ID of node whose status changed (provided with node alerts only)                                                                                                                                                                                                                                                                                        |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CRM_alert_task`{.literal}          | The requested fencing or resource operation (provided with fencing and resource alerts only)                                                                                                                                                                                                                                                            |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CRM_alert_rc`{.literal}            | The numerical return code of the fencing or resource operation (provided with fencing and resource alerts only)                                                                                                                                                                                                                                         |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CRM_alert_rsc`{.literal}           | The name of the affected resource (resource alerts only)                                                                                                                                                                                                                                                                                                |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CRM_alert_interval`{.literal}      | The interval of the resource operation (resource alerts only)                                                                                                                                                                                                                                                                                           |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CRM_alert_target_rc`{.literal}     | The expected numerical return code of the operation (resource alerts only)                                                                                                                                                                                                                                                                              |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CRM_alert_status`{.literal}        | A numerical code used by Pacemaker to represent the operation result (resource alerts only)                                                                                                                                                                                                                                                             |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Show more

When writing an alert agent, you must take the following concerns into account.

-   Alert agents may be called with no recipient (if none is configured), so the agent must be able to handle this situation, even if it only exits in that case. Users may modify the configuration in stages, and add a recipient later.
-   If more than one recipient is configured for an alert, the alert agent will be called once per recipient. If an agent is not able to run concurrently, it should be configured with only a single recipient. The agent is free, however, to interpret the recipient as a list.
-   When a cluster event occurs, all alerts are fired off at the same time as separate processes. Depending on how many alerts and recipients are configured and on what is done within the alert agents, a significant load burst may occur. The agent could be written to take this into consideration, for example by queueing resource-intensive actions into some other instance, instead of directly running them.
-   Alert agents are run as the `hacluster`{.literal} user, which has a minimal set of permissions. If an agent requires additional privileges, it is recommended to configure `sudo`{.literal .command} to allow the agent to run the necessary commands as another user with the appropriate privileges.
-   Take care to validate and sanitize user-configured parameters, such as `CRM_alert_timestamp`{.literal} (whose content is specified by the user-configured `timestamp-format`{.literal}), `CRM_alert_recipient`{.literal}, and all alert options. This is necessary to protect against configuration errors. In addition, if some user can modify the CIB without having `hacluster`{.literal}-level access to the cluster nodes, this is a potential security concern as well, and you should avoid the possibility of code injection.
-   If a cluster contains resources with operations for which the `on-fail`{.literal} parameter is set to `fence`{.literal}, there will be multiple fence notifications on failure, one for each resource for which this parameter is set plus one additional notification. Both the `pacemaker-fenced`{.literal} and `pacemaker-controld`{.literal} will send notifications. Pacemaker performs only one actual fence operation in this case, however, no matter how many notifications are sent.

Note

The alerts interface is designed to be backward compatible with the external scripts interface used by the `ocf:pacemaker:ClusterMon`{.literal} resource. To preserve this compatibility, the environment variables passed to alert agents are available prepended with `CRM_notify_`{.literal} as well as `CRM_alert_`{.literal}. One break in compatibility is that the `ClusterMon`{.literal} resource ran external scripts as the root user, while alert agents are run as the `hacluster`{.literal} user.

## [Chapter 30. Multi-site Pacemaker clusters](#assembly_configuring-multisite-cluster) {#chapter-30.-multi-site-pacemaker-clusters .title}

Network issues between sites can cause split-brain scenarios, as nodes cannot verify remote status. Distance also complicates synchronous HA. To address this, Pacemaker supports multi-site clusters using the Booth cluster ticket manager.

### [30.1. Overview of Booth cluster ticket manager](#booth-cluster-ticket-manager) {#overview-of-booth-cluster-ticket-manager .title}

Booth is a distributed ticket manager that operates on a network separate from the networks connecting the site clusters. It creates a loose overlay cluster, the Booth formation, above the site clusters. This layer facilitates consensus-based decisions for individual Booth tickets.

A Booth *ticket* is a singleton in the Booth formation and represents a time-sensitive, movable unit of authorization. Resources can be configured to require a certain ticket to run. This can ensure that resources are run at only one site at a time, for which a ticket or tickets have been granted.

You can think of a Booth formation as an overlay cluster consisting of clusters running at different sites, where all the original clusters are independent of each other. It is the Booth service which communicates to the clusters whether they have been granted a ticket, and it is Pacemaker that determines whether to run resources in a cluster based on a Pacemaker ticket constraint. This means that when using the ticket manager, each of the clusters can run its own resources as well as shared resources. For example there can be resources A, B and C running only in one cluster, resources D, E, and F running only in the other cluster, and resources G and H running in either of the two clusters as determined by a ticket. It is also possible to have an additional resource J that could run in either of the two clusters as determined by a separate ticket.

### [30.2. Configuring multi-site clusters with Pacemaker](#configuring-multisite-with-booth) {#configuring-multi-site-clusters-with-pacemaker .title}

You can configure a multi-site configuration that uses the Booth ticket manager with the following procedure.

These example commands use the following arrangement:

-   Cluster 1 consists of the nodes `cluster1-node1`{.literal} and `cluster1-node2`{.literal}
-   Cluster 1 has a floating IP address assigned to it of 192.168.11.100
-   Cluster 2 consists of `cluster2-node1`{.literal} and `cluster2-node2`{.literal}
-   Cluster 2 has a floating IP address assigned to it of 192.168.22.100
-   The arbitrator node is `arbitrator-node`{.literal} with an ip address of 192.168.99.100
-   The name of the Booth ticket that this configuration uses is `apacheticket`{.literal}

These example commands assume that the cluster resources for an Apache service have been configured as part of the resource group `apachegroup`{.literal} for each cluster. It is not required that the resources and resource groups be the same on each cluster to configure a ticket constraint for those resources, since the Pacemaker instance for each cluster is independent, but that is a common failover scenario.

Note that at any time in the configuration procedure you can run the `pcs booth config`{.literal} command to display the booth configuration for the current node or cluster or the `pcs booth status`{.literal} command to display the current status of booth on the local node.

**Procedure**

1.  Install the `booth-site`{.literal} Booth ticket manager package on each node of both clusters:

    ``` {.language-plaintext tabindex="-1"}
    [root@cluster1-node1 ~]# dnf install -y booth-site
    [root@cluster1-node2 ~]# dnf install -y booth-site
    [root@cluster2-node1 ~]# dnf install -y booth-site
    [root@cluster2-node2 ~]# dnf install -y booth-site
    ```

2.  Install the `pcs`{.literal}, `booth-core`{.literal}, and `booth-arbitrator`{.literal} packages on the arbitrator node:

    ``` {.language-plaintext tabindex="-1"}
    [root@arbitrator-node ~]# dnf install -y pcs booth-core booth-arbitrator
    ```

3.  If you are running the `firewalld`{.literal} daemon, run the following commands on all nodes in both clusters as well as on the arbitrator node to enable the ports that are required by the Red Hat High Availability Add-On:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=high-availability
    # firewall-cmd --add-service=high-availability
    ```

    You might need to modify which ports are open to suit local conditions. For more information about the ports that are required by the Red Hat High-Availability Add-On, see [Enabling ports for the High Availability Add-On](#enabling-ports-for-high-availability "3.8. Enabling ports for the High Availability Add-On").

4.  Create a Booth configuration on one node of one cluster. The addresses you specify for each cluster and for the arbitrator must be IP addresses. For each cluster, you specify a floating IP address:

    ``` {.language-plaintext tabindex="-1"}
    [cluster1-node1 ~] # pcs booth setup sites 192.168.11.100 192.168.22.100 arbitrators 192.168.99.100
    ```

    This command creates the configuration files `/etc/booth/booth.conf`{.literal} and `/etc/booth/booth.key`{.literal} on the node from which it is run.

5.  Create a ticket for the Booth configuration. This is the ticket that you will use to define the resource constraint that will allow resources to run only when this ticket has been granted to the cluster.

    This basic failover configuration procedure uses only one ticket, but you can create additional tickets for more complicated scenarios where each ticket is associated with a different resource or resources:

    ``` {.language-plaintext tabindex="-1"}
    [cluster1-node1 ~] # pcs booth ticket add apacheticket
    ```

6.  Synchronize the Booth configuration to all nodes in the current cluster:

    ``` {.language-plaintext tabindex="-1"}
    [cluster1-node1 ~] # pcs booth sync
    ```

7.  From the arbitrator node, pull the Booth configuration to the arbitrator. If you have not previously done so, you must first authenticate `pcs`{.literal} to the node from which you are pulling the configuration:

    ``` {.language-plaintext tabindex="-1"}
    [arbitrator-node ~] # pcs host auth cluster1-node1
    [arbitrator-node ~] # pcs booth pull cluster1-node1
    ```

8.  Pull the Booth configuration to the other cluster and synchronize to all the nodes of that cluster. As with the arbitrator node, if you have not previously done so, you must first authenticate `pcs`{.literal} to the node from which you are pulling the configuration:

    ``` {.language-plaintext tabindex="-1"}
    [cluster2-node1 ~] # pcs host auth cluster1-node1
    [cluster2-node1 ~] # pcs booth pull cluster1-node1
    [cluster2-node1 ~] # pcs booth sync
    ```

9.  Start and enable Booth on the arbitrator:

    Note

    You must not manually start or enable Booth on any of the nodes of the clusters since Booth runs as a Pacemaker resource in those clusters.

    ``` {.language-plaintext tabindex="-1"}
    [arbitrator-node ~] # pcs booth start
    [arbitrator-node ~] # pcs booth enable
    ```

10. Configure Booth to run as a cluster resource on both cluster sites, using the floating IP addresses assigned to each cluster. This creates a resource group with `booth-ip`{.literal} and `booth-service`{.literal} as members of that group:

    ``` {.language-plaintext tabindex="-1"}
    [cluster1-node1 ~] # pcs booth create ip 192.168.11.100
    [cluster2-node1 ~] # pcs booth create ip 192.168.22.100
    ```

11. Add a ticket constraint to the resource group you have defined for each cluster:

    ``` {.language-plaintext tabindex="-1"}
    [cluster1-node1 ~] # pcs constraint ticket add apacheticket apachegroup
    [cluster2-node1 ~] # pcs constraint ticket add apacheticket apachegroup
    ```

    Enter the following command to display the currently configured ticket constraints:

    ``` {.language-plaintext tabindex="-1"}
    pcs constraint ticket [config]
    ```

12. Grant the ticket you created for this setup to the first cluster:

    Note

    It is not necessary to have defined ticket constraints before granting a ticket. Once you have initially granted a ticket to a cluster, then Booth takes over ticket management unless you override this manually with the `pcs booth ticket revoke`{.literal} command. For information about the `pcs booth`{.literal} administration commands, use the `pcs booth --help`{.literal} command on your system.

    ``` {.language-plaintext tabindex="-1"}
    [cluster1-node1 ~] # pcs booth ticket grant apacheticket
    ```

    It is possible to add or remove tickets at any time, even after completing this procedure. After adding or removing a ticket, however, you must synchronize the configuration files to the other nodes and clusters as well as to the arbitrator and grant the ticket as is shown in this procedure.

    For a full procedure to remove a Booth ticket, see [Removing a Booth ticket](#removing-booth-ticket "30.3. Removing a Booth ticket"). For information about additional Booth administration commands, use the `pcs booth --help`{.literal} command.

### [30.3. Removing a Booth ticket](#removing-booth-ticket) {#removing-a-booth-ticket .title}

After removing a Booth cluster ticket with `pcs booth ticket remove`{.literal}, or pulling an updated configuration with `pcs booth pull`{.literal}, the ticket state remains loaded in the Cluster Information Base (CIB).

This might cause problems when you configure a ticket constraint, because a ticket constraint can be granted even after a ticket has been removed. As a consequence, the cluster might freeze or fence a node. To prevent this, you can remove a Booth ticket from the CIB with the `pcs booth ticket cleanup`{.literal} command.

**Prerequisites**

-   You have configured a multi-site configuration that uses the Booth ticket manager. For instructions, see [Configuring multi-site clusters with Pacemaker](#configuring-multisite-with-booth "30.2. Configuring multi-site clusters with Pacemaker").

-   The configured example uses the following arrangement:

    -   Cluster 1 consists of the nodes `cluster1-node1`{.literal} and `cluster1-node2`{.literal}.
    -   Cluster 2 consists of the nodes `cluster2-node1`{.literal} and `cluster2-node2`{.literal}.
    -   The arbitrator node is named `arbitrator-node`{.literal}.
    -   The name of the Booth ticket that this configuration uses is `apacheticket`{.literal}.

**Procedure**

1.  From a cluster node in one cluster site of the Booth configuration:

    a.  Put the ticket to remove in `standby`{.literal} mode. The ticket that this example uses is named `apacheticket`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        [cluster1-node1 ~]# pcs booth ticket standby apacheticket
        ```

    b.  Remove the ticket from the Booth configuration.

        ``` {.language-plaintext tabindex="-1"}
        [cluster1-node1 ~]# pcs booth ticket remove apacheticket
        ```

    c.  Synchronize the Booth configuration to all nodes in the current cluster.

        ``` {.language-plaintext tabindex="-1"}
        [cluster1-node1 ~]# pcs booth sync
        ```

    d.  Restart the Booth resource in the current cluster.

        ``` {.language-plaintext tabindex="-1"}
        [cluster1-node1 ~]# pcs booth restart
        ```

    e.  Remove the ticket from the CIB in the current cluster.

        ``` {.language-plaintext tabindex="-1"}
        [cluster1-node1 ~]# pcs booth ticket cleanup
        ```

2.  From a cluster node in each remaining cluster site of the Booth configuration:

    a.  Put the ticket to remove in `standby`{.literal} mode.

        ``` {.language-plaintext tabindex="-1"}
        [cluster2-node1 ~]# pcs booth ticket standby apacheticket
        ```

    b.  Download the Booth configuration file from a node with the updated configuration.

        ``` {.language-plaintext tabindex="-1"}
        [cluster2-node1 ~]# pcs booth pull cluster1-node1
        ```

    c.  Synchronize the Booth configuration to all nodes in the current cluster.

        ``` {.language-plaintext tabindex="-1"}
        [cluster2-node1 ~]# pcs booth sync
        ```

    d.  Restart the Booth resource in the current cluster.

        ``` {.language-plaintext tabindex="-1"}
        [cluster2-node1 ~]# pcs booth restart
        ```

    e.  Remove the ticket from the CIB in the current cluster.

        ``` {.language-plaintext tabindex="-1"}
        [cluster2-node1 ~]# pcs booth ticket cleanup
        ```

3.  From the arbitrator node, download the updated Booth configuration file from a node with the updated configuration:

    ``` {.language-plaintext tabindex="-1"}
    [arbitrator-node ~]# pcs booth pull clusternode-node1
    ```

**Verification**

1.  To check whether a Booth ticket was removed from the Booth configuration, run the `pcs booth config`{.literal} command on each cluster node and the arbitrator node.

    For example, after configuring a ticket named `apacheticket`{.literal} using the procedure described in [Configuring multi-site clusters with Pacemaker](#configuring-multisite-with-booth "30.2. Configuring multi-site clusters with Pacemaker"), the command displays the following output:

    ``` {.language-plaintext tabindex="-1"}
    [cluster1-node1 ~]# pcs booth config
    ```

    ``` {.language-plaintext tabindex="-1"}
    authfile = /etc/booth/booth.key/
    site = 192.168.11.100
    site = 192.168.22.100
    arbitrator = 192.168.99.100
    ticket = "apacheticket"
    ```

    After you remove the ticket from the Booth configuration, the command no longer displays `ticket= "apacheticket"`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [cluster1-node1 ~]# pcs booth config
    ```

    ``` {.language-plaintext tabindex="-1"}
    authfile = /etc/booth/booth.key
    site = 192.168.11.100
    site = 192.168.22.100
    arbitrator = 192.168.99.100
    ```

2.  To check whether a Booth ticket was removed from the CIB on a cluster node, use the `--query-xml`{.literal} option of the `crm_ticket`{.literal} utility on any node in the cluster. For example, after you have configured a Booth ticket named `apacheticket`{.literal}, the utility displays the following output:

    ``` {.language-plaintext tabindex="-1"}
    [cluster1-node1 ~]# crm_ticket --query-xml
    ```

    ``` {.language-plaintext tabindex="-1"}
    State XML:

    <tickets>
      <ticket_state id="apacheticket" granted="true" booth-cfg-name="booth" owner="0" expires="1740986835" term="0" standby="false"/>
    </tickets>
    ```

    After you have removed the ticket from the CIB, the output no longer displays a `ticket_state`{.literal} element with `id="apacheticket"`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [cluster1-node1 ~]# crm_ticket --query-xml
    ```

    ``` {.language-plaintext tabindex="-1"}
    State XML:

    <tickets/>
    ```

## [Chapter 31. Integrating non-corosync nodes into a cluster: the pacemaker_remote service](#remote-node-management) {#chapter-31.-integrating-non-corosync-nodes-into-a-cluster-the-pacemaker_remote-service .title}

The `pacemaker_remote`{.literal} service integrates nodes that do not run `corosync`{.literal} into the cluster. Pacemaker manages `pacemaker_remote`{.literal} resources as it does on any other cluster node.

Among the capabilities that the `pacemaker_remote`{.literal} service provides are the following:

-   The `pacemaker_remote`{.literal} service allows you to scale beyond the Red Hat support limit of 32 nodes.
-   The `pacemaker_remote`{.literal} service allows you to manage a virtual environment as a cluster resource and also to manage individual services within the virtual environment as cluster resources.

The following terms are used to describe the `pacemaker_remote`{.literal} service.

-   *cluster node* - A node running the High Availability services (`pacemaker`{.literal} and `corosync`{.literal}).
-   *remote node* - A node running `pacemaker_remote`{.literal} to remotely integrate into the cluster without requiring `corosync`{.literal} cluster membership. A remote node is configured as a cluster resource that uses the `ocf:pacemaker:remote`{.literal} resource agent.
-   *guest node* - A virtual guest node running the `pacemaker_remote`{.literal} service. The virtual guest resource is managed by the cluster; it is both started by the cluster and integrated into the cluster as a remote node.
-   *pacemaker_remote* - A service daemon capable of performing remote application management within remote nodes and KVM guest nodes in a Pacemaker cluster environment. This service is an enhanced version of Pacemaker's local executor daemon (`pacemaker-execd`{.literal}) that is capable of managing resources remotely on a node not running corosync.

A Pacemaker cluster running the `pacemaker_remote`{.literal} service has the following characteristics.

-   Remote nodes and guest nodes run the `pacemaker_remote`{.literal} service (with very little configuration required on the virtual machine side).
-   The cluster stack (`pacemaker`{.literal} and `corosync`{.literal}), running on the cluster nodes, connects to the `pacemaker_remote`{.literal} service on the remote nodes, allowing them to integrate into the cluster.
-   The cluster stack (`pacemaker`{.literal} and `corosync`{.literal}), running on the cluster nodes, launches the guest nodes and immediately connects to the `pacemaker_remote`{.literal} service on the guest nodes, allowing them to integrate into the cluster.

The key difference between the cluster nodes and the remote and guest nodes that the cluster nodes manage is that the remote and guest nodes are not running the cluster stack. This means the remote and guest nodes have the following limitations:

-   they do not take place in quorum
-   they do not run fencing device actions
-   they are not eligible to be the cluster's Designated Controller (DC)
-   they do not themselves run the full range of `pcs`{.literal .command} commands

On the other hand, remote nodes and guest nodes are not bound to the scalability limits associated with the cluster stack.

Other than these noted limitations, the remote and guest nodes behave just like cluster nodes in respect to resource management, and the remote and guest nodes can themselves be fenced. The cluster is fully capable of managing and monitoring resources on each remote and guest node: You can build constraints against them, put them in standby, or perform any other action you perform on cluster nodes with the `pcs`{.literal} commands. Remote and guest nodes appear in cluster status output just as cluster nodes do.

### [31.1. Host and guest authentication of pacemaker_remote nodes](#host-and-guest-authentication-of-remote-nodes) {#host-and-guest-authentication-of-pacemaker_remote-nodes .title}

Pacemaker supports securing connections between cluster nodes and `pacemaker_remote`{.literal} nodes using either Transport Layer Security (TLS) with pre-shared keys (PSK) or TLS with X.509 certificates.

**TLS with PSK encryption**

Connections between cluster nodes and `pacemaker_remote`{.literal} nodes are secured using Transport Layer Security (TLS) with pre-shared key (PSK) encryption and authentication over TCP (port 3121 by default) in the following scenarios:

-   When configuring a guest node with the `pcs cluster node add-guest`{.literal} command
-   When configuring a remote node with the `pcs cluster node add-remote`{.literal} command

This configuration requires both the cluster node and the node running `pacemaker_remote`{.literal} to share the same private key. By default, this key resides at `/etc/pacemaker/authkey`{.literal} on all cluster nodes and remote nodes.

The first execution of `pcs cluster node add-guest`{.literal} or `pcs cluster node add-remote`{.literal} creates the `authkey`{.literal} file and installs it across all existing cluster nodes. When subsequently adding a new node of any type, the existing `authkey`{.literal} is automatically copied to the new node.

**Configuring SSL/TLS certificates**

Pacemaker Remote connections can be encrypted using X.509 (SSL/TLS) certificates. This method allows reusing existing host certificates for Pacemaker Remote connections rather than relying on private shared keys.

To configure SSL/TLS certificates, create a remote connection with the `pcs cluster node add-guest`{.literal} or `pcs cluster node add-remote`{.literal} command, and then convert the connection to use certificates.

**Procedure**

1.  Create a remote connection using the `pcs cluster node add-guest`{.literal} or `pcs cluster node add-remote`{.literal} command. This configures the `authkey`{.literal} for guest or remote nodes. The following example creates a remote node and configures its `authkey`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [root@clusternode1 ~]# pcs cluster node add-remote remote1
    ```

2.  Convert the created connection to use SSL/TLS certificates by setting the following variables in the `/etc/sysconfig/pacemaker`{.literal} file on all cluster nodes and Pacemaker remote nodes:

    `PCMK_ca_file`{.literal}
    :   The location of a PEM-formatted file containing trusted Certificate Authorities used to verify client or server certificates. Read permissions must be granted to either the `hacluster`{.literal} user or the `haclient`{.literal} group.

    `PCMK_cert_file`{.literal}
    :   The location of a PEM-formatted file containing the signed certificate for the server side of the connection. Read permissions must be granted to either the `hacluster`{.literal} user or the `haclient`{.literal} group.

    `PCMK_crl_file`{.literal} (Optional)
    :   The location of a PEM-formatted Certificate Revocation List file.

    `PCMK_key_file`{.literal}
    :   The location of a PEM-formatted file containing the private key matching `PCMK_cert_file`{.literal}. Read permissions must be granted to either the `hacluster`{.literal} user or the `haclient`{.literal} group.

3.  Optional: Remove any `/etc/pacemaker/authkey`{.literal} files from the cluster and remote nodes. Pacemaker prioritizes certificates when configured, but removing the `authkey`{.literal} files prevents fallback to PSK encryption if certificates are not properly configured on a node.

**Additional resources**

-   [Configuring Pacemaker remote nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_managing_high_availability_clusters/index#configuring-remote-nodes)

### [31.2. Configuring KVM guest nodes](#configuring-kvm-guest-nodes) {#configuring-kvm-guest-nodes .title}

A Pacemaker guest node is a virtual guest node running the `pacemaker_remote`{.literal} service. The virtual guest node is managed by the cluster.

**Guest node resource options**

When configuring a virtual machine to act as a guest node, create a `VirtualDomain`{.literal} resource to manage the virtual machine. For descriptions of the options available for a `VirtualDomain`{.literal} resource, see [Virtual domain resource options](#virtual-domain-resource-options "26.1. Virtual domain resource options").

In addition to `VirtualDomain`{.literal} resource options, metadata options define the resource as a guest node and specify connection parameters. Set these resource options by using the `pcs cluster node add-guest`{.literal} command. The following table describes these metadata options.

+------------------------------------+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                              | Default                                                       | Description                                                                                                                                                                                                       |
+:===================================+:==============================================================+:==================================================================================================================================================================================================================+
| `remote-node`{.literal}            | \<none\>                                                      | The name of the guest node defined by this resource. This setting enables the resource as a guest node and defines its unique identifier. **WARNING**: This value must not overlap with any resource or node IDs. |
+------------------------------------+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `remote-port`{.literal}            | 3121                                                          | Configures a custom port to use for the guest connection to `pacemaker_remote`{.literal}.                                                                                                                         |
+------------------------------------+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `remote-addr`{.literal}            | The address provided in the `pcs host auth`{.literal} command | The IP address or host name to connect to.                                                                                                                                                                        |
+------------------------------------+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `remote-connect-timeout`{.literal} | 60s                                                           | Amount of time before a pending guest connection times out.                                                                                                                                                       |
+------------------------------------+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 31.1. Metadata options for configuring KVM resources as remote nodes

Show more

**Integrating a virtual machine as a guest node**

The following procedure provides a high-level overview of the steps required to launch a virtual machine with Pacemaker and integrate it as a guest node using `libvirt`{.literal} and KVM virtual guests.

**Procedure**

1.  Configure the `VirtualDomain`{.literal} resources.

2.  Enter the following commands on every virtual machine to install `pacemaker_remote`{.literal} packages, start the `pcsd`{.literal} service and enable it to run on startup, and allow TCP port 3121 through the firewall.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pacemaker-remote resource-agents pcs
    # systemctl start pcsd.service
    # systemctl enable pcsd.service
    # firewall-cmd --add-port 3121/tcp --permanent
    # firewall-cmd --add-port 2224/tcp --permanent
    # firewall-cmd --reload
    ```

3.  Give each virtual machine a static network address and unique host name, which should be known to all nodes.

4.  If you have not already done so, authenticate `pcs`{.literal} to the node you will be integrating as a quest node.

    ``` {.language-plaintext tabindex="-1"}
    # pcs host auth nodename
    ```

5.  Use the following command to convert an existing `VirtualDomain`{.literal} resource into a guest node. This command must be run on a cluster node and not on the guest node which is being added. In addition to converting the resource, this command copies the `/etc/pacemaker/authkey`{.literal} to the guest node and starts and enables the `pacemaker_remote`{.literal} daemon on the guest node. The node name for the guest node, which you can define arbitrarily, can differ from the host name for the node.

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster node add-guest nodename resource_id [options]
    ```

6.  After creating the `VirtualDomain`{.literal} resource, you can treat the guest node just as you would treat any other node in the cluster. For example, you can create a resource and place a resource constraint on the resource to run on the guest node as in the following commands, which are run from a cluster node. You can include guest nodes in groups, which allows you to group a storage device, file system, and VM.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create webserver apache configfile=/etc/httpd/conf/httpd.conf op monitor interval=30s
    # pcs constraint location webserver prefers nodename
    ```

### [31.3. Configuring Pacemaker remote nodes](#configuring-remote-nodes) {#configuring-pacemaker-remote-nodes .title}

A remote node is defined as a cluster resource with `ocf:pacemaker:remote`{.literal} as the resource agent. You create this resource with the `pcs cluster node add-remote`{.literal} command.

The following table describes the resource options you can configure for a `remote`{.literal} resource.

+--------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                          | Default                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                 |
+:===============================+:=========================================================+:============================================================================================================================================================================================================================================================================================================================================================================================================================+
| `reconnect_interval`{.literal} | 0                                                        | Time in seconds to wait before attempting to reconnect to a remote node after an active connection to the remote node has been severed. This wait is recurring. If reconnect fails after the wait period, a new reconnect attempt will be made after observing the wait time. When this option is in use, Pacemaker will keep attempting to reach out and connect to the remote node indefinitely after each wait interval. |
+--------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `server`{.literal}             | Address specified with `pcs host auth`{.literal} command | Server to connect to. This can be an IP address or host name.                                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `port`{.literal}               |                                                          | TCP port to connect to.                                                                                                                                                                                                                                                                                                                                                                                                     |
+--------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 31.2. Resource options for remote nodes

Show more

### [31.4. Remote node configuration overview](#remote-node-configuration-overview) {#remote-node-configuration-overview .title}

Configure a Pacemaker Remote node and integrate it into the existing cluster.

**Procedure**

1.  On the node that you will be configuring as a remote node, allow cluster-related services through the local firewall.

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=high-availability
    ```

    ``` {.language-plaintext tabindex="-1"}
    success
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

    ``` {.language-plaintext tabindex="-1"}
    success
    ```

    Note

    If you are using `iptables`{.literal} directly, or some other firewall solution besides `firewalld`{.literal}, open the following ports: TCP ports 2224 and 3121.

2.  Install the `pacemaker_remote`{.literal} daemon on the remote node.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install -y pacemaker-remote resource-agents pcs
    ```

3.  Start and enable `pcsd`{.literal} on the remote node.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start pcsd.service
    # systemctl enable pcsd.service
    ```

4.  If you have not already done so, authenticate `pcs`{.literal} to the node you will be adding as a remote node.

    ``` {.language-plaintext tabindex="-1"}
    # pcs host auth remote1
    ```

5.  Add the remote node resource to the cluster with the following command. This command also syncs all relevant configuration files to the new node, starts the node, and configures it to start `pacemaker_remote`{.literal} on boot. This command must be run on a cluster node and not on the remote node which is being added.

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster node add-remote remote1
    ```

6.  After adding the `remote`{.literal} resource to the cluster, you can treat the remote node just as you would treat any other node in the cluster. For example, you can create a resource and place a resource constraint on the resource to run on the remote node as in the following commands, which are run from a cluster node.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create webserver apache configfile=/etc/httpd/conf/httpd.conf op monitor interval=30s
    # pcs constraint location webserver prefers remote1
    ```

    Warning

    Never involve a remote node connection resource in a resource group, colocation constraint, or order constraint.

7.  Configure fencing resources for the remote node. Remote nodes are fenced the same way as cluster nodes. Configure fencing resources for use with remote nodes the same as you would with cluster nodes. Note, however, that remote nodes can never initiate a fencing action. Only cluster nodes are capable of actually running a fencing operation against another node.

### [31.5. Changing the default port location](#changing-default-port-location) {#changing-the-default-port-location .title}

If you need to change the default port location for either Pacemaker or `pacemaker_remote`{.literal}, you can set the `PCMK_remote_port`{.literal} environment variable that affects both of these daemons.

**Procedure**

-   Enable the environment variable by placing it in the `/etc/sysconfig/pacemaker`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    \#==#==# Pacemaker Remote
    ...
    #
    # Specify a custom port for Pacemaker Remote connections
    PCMK_remote_port=3121
    ```

    When changing the default port used by a particular guest node or remote node, the `PCMK_remote_port`{.literal} variable must be set in that node's `/etc/sysconfig/pacemaker`{.literal} file, and the cluster resource creating the guest node or remote node connection must also be configured with the same port number (using the `remote-port`{.literal} metadata option for guest nodes, or the `port`{.literal} option for remote nodes).

### [31.6. Upgrading systems with pacemaker_remote nodes](#upgrading-systems-with-pacemaker-remote) {#upgrading-systems-with-pacemaker_remote-nodes .title}

Stopping the `pacemaker_remote`{.literal} service on an active node triggers a graceful resource migration for maintenance. After shutdown, the cluster attempts to reconnect immediately. If the service does not restart before the monitor timeout expires, the cluster marks the resource as failed.

If you want to avoid monitor failures when the `pacemaker_remote`{.literal} service is stopped on an active Pacemaker Remote node, you can use the following procedure to take the node out of the cluster before performing any system administration that might stop `pacemaker_remote`{.literal}.

**Procedure**

1.  Stop the node's connection resource with the `pcs resource disable `{.literal}*`resourcename`{.literal}* command, which will move all services off the node. The connection resource would be the `ocf:pacemaker:remote`{.literal} resource for a remote node or, commonly, the `ocf:heartbeat:VirtualDomain`{.literal} resource for a guest node. For guest nodes, this command will also stop the VM, so the VM must be started outside the cluster (for example, using `virsh`{.literal}) to perform any maintenance.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource disable resourcename
    ```

2.  Perform the required maintenance.

3.  When ready to return the node to the cluster, re-enable the resource with the `pcs resource enable`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource enable resourcename
    ```

### [31.7. Verifying that Pacemaker remote nodes are no longer fenced unnecessarily](#verifying-that-pacemaker-remote-nodes-are-no-longer-fenced-unnecessarily) {#verifying-that-pacemaker-remote-nodes-are-no-longer-fenced-unnecessarily .title}

On RHEL 10, the `fence-remote-without-quorum`{.literal} cluster property is set to `false`{.literal} by default. This ensures that a remote node is not fenced unnecessarily when its managing partition loses quorum. You can verify this behavior by temporarily changing the configuration to allow fencing.

**Prerequisites**

-   A running RHEL High-Availability cluster with at least three cluster nodes and one remote node.
-   A resource configured to run on the remote node.
-   Fencing configured for all nodes.

**Procedure**

1.  Configure the cluster to replicate the original behavior:

    a.  Set the `no-quorum-policy`{.literal} property to `freeze`{.literal}.

    b.  Set the `fence-remote-without-quorum`{.literal} property to `true`{.literal}.

        Note

        On RHEL 10, the default value is `false`{.literal}. This step explicitly overrides the default to simulate the legacy behavior for verification purposes.

        ``` {.language-plaintext tabindex="-1"}
        [root@node1 ~]# pcs property set no-quorum-policy=freeze

        [root@node1 ~]# pcs property set fence-remote-without-quorum=true
        ```

2.  Isolate one of the cluster nodes from the other nodes. In this example, `hvirt-325`{.literal} is the node that manages the remote node `hvirt-292`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [root@hvirt-325 ~]# iptables -I INPUT -p udp --dport=5405 -j DROP
    ```

3.  Observe the cluster's behavior.

    -   Check the logs on the isolated node. You'll see that the node initiates fencing for the remote node.
    -   Check the fencing history for the cluster. You'll see successful fencing actions for both the isolated cluster node and the remote node.

4.  Rejoin the isolated node to the cluster and ensure all nodes and resources are online:

    ``` {.language-plaintext tabindex="-1"}
    [root@hvirt-325 ~]# iptables -D INPUT -p udp --dport=5405 -j DROP
    ```

5.  Restore the default behavior. Set the `fence-remote-without-quorum`{.literal} property to `false`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [root@node1 ~]# pcs property set fence-remote-without-quorum=false
    ```

6.  Repeat the network isolation test from step 2:

    ``` {.language-plaintext tabindex="-1"}
    [root@hvirt-325 ~]# iptables -I INPUT -p udp --dport=5405 -j DROP
    ```

**Verification**

-   Check the cluster status and logs after isolating the node with `fence-remote-without-quorum=false`{.literal}.

-   The logs on the isolated node now show that the remote node is not fenced.

    ``` {.language-plaintext tabindex="-1"}
    Jul 14 11:55:30 hvirt-325 pacemaker-schedulerd[2934]: warning: Node hvirt-292 is unclean but cannot be fenced
    ```

## [Chapter 32. Performing cluster maintenance](#cluster-maintenance) {#chapter-32.-performing-cluster-maintenance .title}

To perform maintenance on cluster nodes, you might need to stop or move the resources and services running on the cluster. In some cases, you can stop the cluster software without affecting services. Pacemaker provides several methods to support system maintenance.

### [32.1. Putting a node into standby mode](#stopping-individual-node) {#putting-a-node-into-standby-mode .title}

When a cluster node is in standby mode, the node is no longer able to host resources. Any resources currently active on the node will be moved to another node.

The following command puts the specified node into standby mode. If you specify the `--all`{.literal} option, this command puts all nodes into standby mode.

You can use this command when updating a resource's packages. You can also use this command when testing a configuration, to simulate recovery without actually shutting down a node.

**Procedure**

-   Put the specified node into standby mode:

    ``` {.language-plaintext tabindex="-1"}
    # pcs node standby node | --all
    ```

-   Remove the specified node from standby mode. After running this command, the specified node is then able to host resources. If you specify the `--all`{.literal} option, this command removes all nodes from standby mode:

    ``` {.language-plaintext tabindex="-1"}
    # pcs node unstandby node | --all
    ```

    Note that when you run the `pcs node standby`{.literal} command, this prevents resources from running on the indicated node. When you run the `pcs node unstandby`{.literal .command} command, this allows resources to run on the indicated node. This does not necessarily move the resources back to the indicated node; where the resources can run at that point depends on how you have configured your resources initially.

### [32.2. Manually moving cluster resources](#manually-move-resources) {#manually-moving-cluster-resources .title}

You can override the cluster and force resources to move from their current location. There are two occasions when you would want to do this.

-   When a node is under maintenance, and you need to move all resources running on that node to a different node
-   When individually specified resources needs to be moved

To move all resources running on a node to a different node, you put the node in standby mode. For information about putting a cluster node in standby node, see [Putting a node in standby mode](#stopping-individual-node "32.1. Putting a node into standby mode").

You can move individually specified resources in either of the following ways.

-   You can use the `pcs resource move`{.literal} command to move a resource off a node on which it is currently running, as described in [Moving a resource from its current node](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_managing_high_availability_clusters/index#moving_a_resource_from_its_current_node).
-   You can use the `pcs resource relocate run`{.literal} command to move a resource to its preferred node, as determined by current cluster status, constraints, location of resources and other settings. For information about this command, see [Moving a resource to its preferred node](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_managing_high_availability_clusters/index#moving_a_resource_to_its_preferred_node).

**Moving a resource from its current node**

To move a resource off the node on which it is currently running, use the following command, specifying the *resource_id* of the resource as defined. Specify the *destination_node* if you want to indicate on which node to run the resource that you are moving.

``` {.language-plaintext tabindex="-1"}
# pcs resource move resource_id [destination_node] [--promoted] [--strict] [--wait[=n]]
```

When you run the `pcs resource move`{.literal} command, this adds a constraint to the resource to prevent it from running on the node on which it is currently running. By default, the location constraint that the command creates is automatically removed once the resource has been moved. If removing the constraint would cause the resource to move back to the original node, as might happen if the `resource-stickiness`{.literal} value for the resource is 0, the `pcs resource move`{.literal} command fails. If you would like to move a resource and leave the resulting constraint in place, use the `pcs resource move-with-constraint`{.literal} command.

-   If you specify the `--promoted`{.literal} parameter of the `pcs resource move`{.literal .command} command, the constraint applies only to promoted instances of the resource.

-   If you specify the `--strict`{.literal} parameter of the `pcs resource move`{.literal .command} command, the command will fail if other resources than the one specified in the command would be affected.

-   You can optionally configure a `--wait[=`{.literal}*`n`{.literal}*`]`{.literal} parameter for the `pcs resource move`{.literal} command to indicate the number of seconds to wait for the resource to start on the destination node before returning 0 if the resource is started or 1 if the resource has not yet started. If you do not specify n, it defaults to a value of 60 minutes.

    For more information about location constraints, see [Determining which nodes a resource can run on](#determining-which-node-a-resource-runs-on "Chapter 12. Determining which nodes a resource can run on").

**Moving a resource to its preferred node**

After a resource has moved, either due to a failover or to an administrator manually moving the node, it will not necessarily move back to its original node even after the circumstances that caused the failover have been corrected. To relocate resources to their preferred node, use the following command. A preferred node is determined by the current cluster status, constraints, resource location, and other settings and may change over time.

``` {.language-plaintext tabindex="-1"}
# pcs resource relocate run [resource1] [resource2] ...
```

If you do not specify any resources, all resource are relocated to their preferred nodes.

This command calculates the preferred node for each resource while ignoring resource stickiness. After calculating the preferred node, it creates location constraints which will cause the resources to move to their preferred nodes. Once the resources have been moved, the constraints are deleted automatically. To remove all constraints created by the `pcs resource relocate run`{.literal} command, you can enter the `pcs resource relocate clear`{.literal} command. To display the current status of resources and their optimal node ignoring resource stickiness, enter the `pcs resource relocate show`{.literal} command.

### [32.3. Disabling, enabling, and banning cluster resources](#disabling-resources) {#disabling-enabling-and-banning-cluster-resources .title}

In addition to the `pcs resource move`{.literal} and `pcs resource relocate`{.literal} commands, there are a variety of other commands you can use to control the behavior of cluster resources.

#### [32.3.1. Disabling a cluster resource](#disabling-a-cluster-resource) {#disabling-a-cluster-resource .title}

Disable cluster resources for maintenance, troubleshooting, or configuration changes without removing them from the cluster. Disabling stops the resource and prevents automatic restart until re-enabled.

**Simulating resource disable operations**

When complex resource relationships exist, manually evaluating the impact of disabling a resource can be difficult. To determine the impact before modifying the cluster configuration, run the `pcs resource disable --simulate`{.literal} command.

**Safely disabling resources**

To disable a resource only when no other resources are impacted, use safe disable options:

-   The `pcs resource disable --safe`{.literal} command disables a resource only if no other resources are affected (for example, migrated to another node). The `pcs resource safe-disable`{.literal} command is an alias for this command.
-   The `pcs resource disable --safe --no-strict`{.literal} command disables a resource only if no other resources are stopped or demoted.

**Displaying affected resource IDs**

If a safe disable operation fails, the resulting error output includes the affected resource IDs. To display only the affected resource IDs without full simulation output, append the `--brief`{.literal} option to the `pcs resource disable --safe`{.literal} command.

**Procedure**

-   Stop a running resource and prevent the cluster from restarting it:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource disable resource_id [--wait[=n]]
    ```

#### [32.3.2. Enabling a cluster resource](#enabling-a-cluster-resource) {#enabling-a-cluster-resource .title}

Enable a resource to allow the cluster to start it. Depending on the configuration, the resource might remain stopped. Use `--wait=n`{.literal} to pause until the resource starts (returns 0) or the timeout expires (returns 1). The default timeout is 60 minutes.

**Procedure**

-   Use the following command to allow the cluster to start a resource:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource enable resource_id [--wait[=n]]
    ```

#### [32.3.3. Preventing a resource from running on a particular node](#preventing-a-resource-from-running-on-a-particular-node) {#preventing-a-resource-from-running-on-a-particular-node .title}

You can prevent a resource from running on a specified node, or on the current node if no node is specified.

**Procedure**

-   Prevent a resource from running on a specified node, or on the current node if no node is specified:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource ban resource_id [node] [--promoted] [lifetime=lifetime] [--wait[=n]]
    ```

    Note

    When you run the `pcs resource ban`{.literal} command, this adds a -INFINITY location constraint to the resource to prevent it from running on the indicated node. You can run the `pcs resource clear`{.literal} or the `pcs constraint delete`{.literal} command to remove the constraint. This does not necessarily move the resources back to the indicated node; where the resources can run at that point depends on how you have configured your resources initially. For information about resource constraints, see [Determining which nodes a resource can run on](#determining-which-node-a-resource-runs-on "Chapter 12. Determining which nodes a resource can run on").

-   If you specify the `--promoted`{.literal} parameter of the `pcs resource ban`{.literal .command} command, the scope of the constraint is limited to the promoted role and you must specify *promotable_id* rather than *resource_id*.

-   You can optionally configure a `lifetime`{.literal} parameter for the `pcs resource ban`{.literal} command to indicate a period of time the constraint should remain.

-   You can optionally configure a `--wait[=`{.literal}*`n`{.literal}*`]`{.literal} parameter for the `pcs resource ban`{.literal} command to indicate the number of seconds to wait for the resource to start on the destination node before returning 0 if the resource is started or 1 if the resource has not yet started. If you do not specify *n*, the default resource timeout is used.

#### [32.3.4. Forcing a resource to start on the current node](#forcing-a-resource-to-start-on-the-current-node) {#forcing-a-resource-to-start-on-the-current-node .title}

Use `pcs resource debug-start`{.literal} to force a resource to start on the current node for debugging. This command prints the output and ignores cluster recommendations. Do not use this for normal operations; Pacemaker manages starting cluster resources.

**Procedure**

-   Use the `debug-start`{.literal} command to force a specified resource to start on the current node:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource debug-start resource_id
    ```

### [32.4. Setting a resource to unmanaged mode](#unmanaging-resources) {#setting-a-resource-to-unmanaged-mode .title}

When a resource is in `unmanaged`{.literal} mode, the resource is still in the configuration but Pacemaker does not manage the resource.

**Procedure**

-   Set the indicated resources to `unmanaged`{.literal} mode:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource unmanage resource1 [resource2] ...
    ```

-   Set resources to `managed`{.literal} mode, which is the default state:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource manage resource1 [resource2] ...
    ```

    You can specify the name of a resource group with the `pcs resource manage`{.literal} or `pcs resource unmanage`{.literal} command. The command will act on all of the resources in the group, so that you can set all of the resources in a group to `managed`{.literal} or `unmanaged`{.literal} mode with a single command and then manage the contained resources individually.

### [32.5. Putting a cluster in maintenance mode](#setting-maintenance-mode) {#putting-a-cluster-in-maintenance-mode .title}

When a cluster is in maintenance mode, the cluster does not start or stop any services until told otherwise. When maintenance mode is completed, the cluster does a sanity check of the current state of any services, and then stops or starts any that need it.

To put a cluster in maintenance mode, use the following command to set the `maintenance-mode`{.literal} cluster property to `true`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs property set maintenance-mode=true
```

To remove a cluster from maintenance mode, use the following command to set the `maintenance-mode`{.literal} cluster property to `false`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs property set maintenance-mode=false
```

For general information on setting and removing cluster properties, see [Setting and removing cluster properties](#setting-cluster-properties "23.2. Setting and removing cluster properties").

### [32.6. Updating a RHEL high availability cluster](#updating-cluster-packages) {#updating-a-rhel-high-availability-cluster .title}

Updating packages that make up the RHEL High Availability Add-On, either individually or as a whole, can be done in one of two general ways:

-   *Rolling Updates*: Remove one node at a time from service, update its software, then integrate it back into the cluster. This allows the cluster to continue providing service and managing resources while each node is updated.
-   *Entire Cluster Update*: Stop the entire cluster, apply updates to all nodes, then start the cluster back up.

Warning

It is critical that when performing software update procedures for Red Hat Enterprise Linux High Availability clusters, you ensure that any node that will undergo updates is not an active member of the cluster before those updates are initiated.

**Additional resources**

-   [Recommended Practices for Applying Software Updates to a RHEL High Availability or Resilient Storage Cluster](https://access.redhat.com/articles/2059253/)

### [32.7. Upgrading remote nodes and guest nodes](#upgrading-remote-nodes) {#upgrading-remote-nodes-and-guest-nodes .title}

Stopping the `pacemaker_remote`{.literal} service on an active node triggers a graceful resource migration, enabling seamless maintenance. However, the cluster attempts to reconnect immediately. If the service does not restart within the monitor timeout, the cluster detects a failure.

To avoid monitor failures when the `pacemaker_remote`{.literal} service is stopped on an active Pacemaker Remote node, use the following procedure to take the node out of the cluster before performing any system administration that might stop `pacemaker_remote`{.literal}.

**Procedure**

1.  Stop the node's connection resource with the `pcs resource disable `{.literal}*`resourcename`{.literal}* command, which will move all services off the node. The connection resource would be the `ocf:pacemaker:remote`{.literal} resource for a remote node or, commonly, the `ocf:heartbeat:VirtualDomain`{.literal} resource for a guest node. For guest nodes, this command will also stop the VM, so the VM must be started outside the cluster (for example, using `virsh`{.literal}) to perform any maintenance.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource disable resourcename
    ```

2.  Perform the required maintenance.

3.  When ready to return the node to the cluster, re-enable the resource with the `pcs resource enable`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource enable resourcename
    ```

### [32.8. Migrating VMs in a RHEL cluster](#migrating-cluster-vms) {#migrating-vms-in-a-rhel-cluster .title}

Red Hat does not support live migration of active cluster nodes. To migrate a VM, stop cluster services to take the node offline, migrate the VM, and restart services. For details, see [Support Policies for RHEL High Availability Clusters - General Conditions with Virtualized Cluster Members](https://access.redhat.com/articles/3131111/).

The following steps outline the procedure for removing a VM from a cluster, migrating the VM, and restoring the VM to the cluster.

This procedure applies to VMs that are used as full cluster nodes, not to VMs managed as cluster resources (including VMs used as guest nodes) which can be live-migrated without special precautions. For general information about the fuller procedure required for updating packages that make up the RHEL High Availability and Resilient Storage Add-Ons, either individually or as a whole, see the Red Hat Knowledgebase article [Recommended Practices for Applying Software Updates to a RHEL High Availability or Resilient Storage Cluster](https://access.redhat.com/articles/2059253/).

Note

Before performing this procedure, consider the effect on cluster quorum of removing a cluster node. For example, if you have a three-node cluster and you remove one node, your cluster cannot withstand any node failure. This is because if one node of a three-node cluster is already down, removing a second node will lose quorum.

**Procedure**

1.  If any preparations need to be made before stopping or moving the resources or software running on the VM to migrate, perform those steps.

2.  Run the following command on the VM to stop the cluster software on the VM.

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster stop
    ```

3.  Perform the live migration of the VM.

4.  Start cluster services on the VM.

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster start
    ```

### [32.9. Identifying clusters by UUID](#identifying-cluster-by-uuid) {#identifying-clusters-by-uuid .title}

When creating a cluster, it receives a unique UUID that third-party tools, such as configuration management databases, use to distinguish clusters with identical names. Display the cluster UUID by using the `pcs cluster config [show]`{.literal} command.

**Procedure**

-   Add a UUID to an existing cluster:

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster config uuid generate
    ```

-   Regenerate a UUID for a cluster with an existing UUID:

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster config uuid generate --force
    ```

### [32.10. Renaming a cluster](#renaming-a-cluster) {#renaming-a-cluster .title}

You can change the name of an existing cluster using the `pcs cluster rename`{.literal} command.

**Procedure**

-   To rename your cluster, run the `pcs cluster rename`{.literal} command from any cluster node. Replace `<new-name>`{.literal} with the new name you want to assign to the cluster:

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster rename <new-name>
    ```

## [Chapter 33. Removing the cluster configuration](#removing-cluster-configuration) {#chapter-33.-removing-the-cluster-configuration .title}

Permanently remove all Pacemaker and Corosync cluster configuration from a system when a cluster is no longer needed or must be rebuilt from scratch.

**Prerequisites**

-   You have root access or a non-root user account with `sudo`{.literal} privileges.
-   The `pcs`{.literal} command-line tool is installed.

Important

Removing the cluster configuration is irreversible. After completion, the node is no longer part of any cluster and cannot be recovered without reconfiguration.

**Procedure**

1.  Optional: Stop the cluster cleanly on the node.

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster stop
    ```

    Stopping the cluster reduces the risk of incomplete cleanup.

2.  Remove all cluster configuration and disable cluster services.

    ``` {.language-plaintext tabindex="-1"}
    # pcs cluster destroy
    ```

**Verification**

1.  Verify that cluster services are no longer running.

    ``` {.language-plaintext tabindex="-1"}
    # pcs status
    ```

    If the cluster is removed successfully, the command reports that no cluster is configured.

2.  Optional: Confirm that cluster services are stopped.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status pacemaker corosync
    ```

    Both services should be inactive or not found.

## [Chapter 34. Configuring disaster recovery clusters](#configuring-disaster-recovery) {#chapter-34.-configuring-disaster-recovery-clusters .title}

To provide disaster recovery for a high availability cluster, configure two clusters: a primary site cluster and a disaster recovery cluster.

In normal circumstances, the primary cluster is running resources in production mode. The disaster recovery cluster has all the resources configured as well and is either running them in demoted mode or not at all. For example, there may be a database running in the primary cluster in promoted mode and running in the disaster recovery cluster in demoted mode. The database in this setup would be configured so that data is synchronized from the primary to disaster recovery site. This is done through the database configuration itself rather than through the `pcs`{.literal} command interface.

When the primary cluster goes down, users can use the `pcs`{.literal} command interface to manually fail the resources over to the disaster recovery site. They can then log in to the disaster site and promote and start the resources there. Once the primary cluster has recovered, users can use the `pcs`{.literal} command interface to manually move resources back to the primary site.

You can use the `pcs`{.literal} command to display the status of both the primary and the disaster recovery site cluster from a single node on either site.

### [34.1. Considerations for disaster recovery clusters](#recovery-considerations) {#considerations-for-disaster-recovery-clusters .title}

When planning and configuring a disaster recovery site that you will manage and monitor with the `pcs`{.literal} command interface, note the following considerations.

-   The disaster recovery site must be a cluster. This makes it possible to configure it with same tools and similar procedures as the primary site.
-   The primary and disaster recovery clusters are created by independent `pcs cluster setup`{.literal} commands.
-   The clusters and their resources must be configured so that the data is synchronized and failover is possible.
-   The cluster nodes in the recovery site cannot have the same names as the nodes in the primary site.
-   The pcs user `hacluster`{.literal} must be authenticated for each node in both clusters on the node from which you will be running `pcs`{.literal} commands.

### [34.2. Displaying status of recovery clusters](#disaster-recovery-display) {#displaying-status-of-recovery-clusters .title}

You can configure a primary and a disaster recovery cluster so that you can display the status of both clusters.

Note

Configuring a disaster recovery cluster does not automatically configure resources or replicate data. Those items must be configured manually by the user.

In this example:

-   The primary cluster will be named `PrimarySite`{.literal} and will consist of the nodes `z1.example.com`{.literal}. and `z2.example.com`{.literal}.
-   The disaster recovery site cluster will be named `DRsite`{.literal} and will consist of the nodes `z3.example.com`{.literal} and `z4.example.com`{.literal}.

This example configures a basic cluster with no resources or fencing configured.

**Procedure**

1.  Authenticate all of the nodes that will be used for both clusters.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs host auth z1.example.com z2.example.com z3.example.com z4.example.com -u hacluster -p password
    ```

    ``` {.language-plaintext tabindex="-1"}
    z1.example.com: Authorized
    z2.example.com: Authorized
    z3.example.com: Authorized
    z4.example.com: Authorized
    ```

2.  Create the cluster that will be used as the primary cluster and start cluster services for the cluster.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs cluster setup PrimarySite z1.example.com z2.example.com --start
    ```

    ``` {.language-plaintext tabindex="-1"}
    {...}
    Cluster has been successfully set up.
    Starting cluster on hosts: 'z1.example.com', 'z2.example.com'...
    ```

3.  Create the cluster that will be used as the disaster recovery cluster and start cluster services for the cluster.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs cluster setup DRSite z3.example.com z4.example.com --start
    ```

    ``` {.language-plaintext tabindex="-1"}
    {...}
    Cluster has been successfully set up.
    Starting cluster on hosts: 'z3.example.com', 'z4.example.com'...
    ```

4.  From a node in the primary cluster, configure the second cluster as the recovery site. The recovery site is defined by a name of one of its nodes.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs dr set-recovery-site z3.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    Sending 'disaster-recovery config' to 'z3.example.com', 'z4.example.com'
    z3.example.com: successful distribution of the file 'disaster-recovery config'
    z4.example.com: successful distribution of the file 'disaster-recovery config'
    Sending 'disaster-recovery config' to 'z1.example.com', 'z2.example.com'
    z1.example.com: successful distribution of the file 'disaster-recovery config'
    z2.example.com: successful distribution of the file 'disaster-recovery config'
    ```

5.  Check the disaster recovery configuration.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs dr config
    ```

    ``` {.language-plaintext tabindex="-1"}
    Local site:
      Role: Primary
    Remote site:
      Role: Recovery
      Nodes:
        z3.example.com
        z4.example.com
    ```

6.  Check the status of the primary cluster and the disaster recovery cluster from a node in the primary cluster.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs dr status
    ```

    ``` {.language-plaintext tabindex="-1"}
    --- Local cluster - Primary site ---
    Cluster name: PrimarySite

    WARNINGS:
    No stonith devices and stonith-enabled is not false

    Cluster Summary:
      * Stack: corosync
      * Current DC: z2.example.com (version 2.0.3-2.el8-2c9cea563e) - partition with quorum
      * Last updated: Mon Dec  9 04:10:31 2019
      * Last change:  Mon Dec  9 04:06:10 2019 by hacluster via crmd on z2.example.com
      * 2 nodes configured
      * 0 resource instances configured

    Node List:
      * Online: [ z1.example.com z2.example.com ]

    Full List of Resources:
      * No resources

    Daemon Status:
      corosync: active/disabled
      pacemaker: active/disabled
      pcsd: active/enabled

    --- Remote cluster - Recovery site ---
    Cluster name: DRSite

    WARNINGS:
    No stonith devices and stonith-enabled is not false

    Cluster Summary:
      * Stack: corosync
      * Current DC: z4.example.com (version 2.0.3-2.el8-2c9cea563e) - partition with quorum
      * Last updated: Mon Dec  9 04:10:34 2019
      * Last change:  Mon Dec  9 04:09:55 2019 by hacluster via crmd on z4.example.com
      * 2 nodes configured
      * 0 resource instances configured

    Node List:
      * Online: [ z3.example.com z4.example.com ]

    Full List of Resources:
      * No resources

    Daemon Status:
      corosync: active/disabled
      pacemaker: active/disabled
      pcsd: active/enabled
    ```

    For additional display options for a disaster recovery configuration, see the help screen for the `pcs dr`{.literal} command.

## [Appendix A. Interpreting resource agent OCF return codes](#interpreting-resource-exit-codes) {#appendix-a.-interpreting-resource-agent-ocf-return-codes .title}

Pacemaker resource agents conform to the Open Cluster Framework (OCF) Resource Agent API.

The first thing the cluster does when an agent returns a code is to check the return code against the expected result. If the result does not match the expected value, then the operation is considered to have failed, and recovery action is initiated.

For any invocation, resource agents must exit with a defined return code that informs the caller of the outcome of the invoked action.

There are three types of failure recovery, as described in the following table.

+---------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| Type    | Description                                                                                                               | Action Taken by the Cluster                                                        |
+:========+:==========================================================================================================================+:===================================================================================+
| soft    | A transient error occurred.                                                                                               | Restart the resource or move it to a new location .                                |
+---------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| hard    | A non-transient error that may be specific to the current node occurred.                                                  | Move the resource elsewhere and prevent it from being retried on the current node. |
+---------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| fatal   | A non-transient error that will be common to all cluster nodes occurred (for example, a bad configuration was specified). | Stop the resource and prevent it from being started on any cluster node.           |
+---------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

: Table A.1. Types of Recovery Performed by the Cluster

Show more

The following table provides The OCF return codes and the type of recovery the cluster will initiate when a failure code is received.Note that even actions that return 0 (OCF alias `OCF_SUCCESS`{.literal}) can be considered to have failed, if 0 was not the expected return value.

+-------------+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Return Code | OCF Label                         | Description                                                                                                                                                                                                                             |
+:============+:==================================+:========================================================================================================================================================================================================================================+
| 0           | `OCF_SUCCESS`{.literal}           | \* The action completed successfully. This is the expected return code for any successful start, stop, promote, and demote command.                                                                                                     |
|             |                                   |                                                                                                                                                                                                                                         |
|             |                                   | \* Type if unexpected: soft                                                                                                                                                                                                             |
+-------------+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1           | `OCF_ERR_GENERIC`{.literal}       | \* The action returned a generic error.                                                                                                                                                                                                 |
|             |                                   |                                                                                                                                                                                                                                         |
|             |                                   | \* Type: soft                                                                                                                                                                                                                           |
|             |                                   |                                                                                                                                                                                                                                         |
|             |                                   | \* The resource manager will attempt to recover the resource or move it to a new location.                                                                                                                                              |
+-------------+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2           | `OCF_ERR_ARGS`{.literal}          | \* The resource's configuration is not valid on this machine. For example, it refers to a location not found on the node.                                                                                                               |
|             |                                   |                                                                                                                                                                                                                                         |
|             |                                   | \* Type: hard                                                                                                                                                                                                                           |
|             |                                   |                                                                                                                                                                                                                                         |
|             |                                   | \* The resource manager will move the resource elsewhere and prevent it from being retried on the current node                                                                                                                          |
+-------------+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3           | `OCF_ERR_UNIMPLEMENTED`{.literal} | \* The requested action is not implemented.                                                                                                                                                                                             |
|             |                                   |                                                                                                                                                                                                                                         |
|             |                                   | \* Type: hard                                                                                                                                                                                                                           |
+-------------+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 4           | `OCF_ERR_PERM`{.literal}          | \* The resource agent does not have sufficient privileges to complete the task. This may be due, for example, to the agent not being able to open a certain file, to listen on a specific socket, or to write to a directory.           |
|             |                                   |                                                                                                                                                                                                                                         |
|             |                                   | \* Type: hard                                                                                                                                                                                                                           |
|             |                                   |                                                                                                                                                                                                                                         |
|             |                                   | \* Unless specifically configured otherwise, the resource manager will attempt to recover a resource which failed with this error by restarting the resource on a different node (where the permission problem may not exist).          |
+-------------+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 5           | `OCF_ERR_INSTALLED`{.literal}     | \* A required component is missing on the node where the action was executed. This may be due to a required binary not being executable, or a vital configuration file being unreadable.                                                |
|             |                                   |                                                                                                                                                                                                                                         |
|             |                                   | \* Type: hard                                                                                                                                                                                                                           |
|             |                                   |                                                                                                                                                                                                                                         |
|             |                                   | \* Unless specifically configured otherwise, the resource manager will attempt to recover a resource which failed with this error by restarting the resource on a different node (where the required files or binaries may be present). |
+-------------+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 6           | `OCF_ERR_CONFIGURED`{.literal}    | \* The resource's configuration on the local node is invalid.                                                                                                                                                                           |
|             |                                   |                                                                                                                                                                                                                                         |
|             |                                   | \* Type: fatal                                                                                                                                                                                                                          |
|             |                                   |                                                                                                                                                                                                                                         |
|             |                                   | \* When this code is returned, Pacemaker will prevent the resource from running on any node in the cluster, even if the service configuration is valid on some other node.                                                              |
+-------------+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 7           | `OCF_NOT_RUNNING`{.literal}       | \* The resource is safely stopped. This implies that the resource has either gracefully shut down, or has never been started.                                                                                                           |
|             |                                   |                                                                                                                                                                                                                                         |
|             |                                   | \* Type if unexpected: soft                                                                                                                                                                                                             |
|             |                                   |                                                                                                                                                                                                                                         |
|             |                                   | \* The cluster will not attempt to stop a resource that returns this for any action.                                                                                                                                                    |
+-------------+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 8           | `OCF_RUNNING_PROMOTED`{.literal}  | \* The resource is running in promoted role.                                                                                                                                                                                            |
|             |                                   |                                                                                                                                                                                                                                         |
|             |                                   | \* Type if unexpected: soft                                                                                                                                                                                                             |
+-------------+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 9           | `OCF_FAILED_PROMOTED`{.literal}   | \* The resource is (or might be) in promoted role but has failed.                                                                                                                                                                       |
|             |                                   |                                                                                                                                                                                                                                         |
|             |                                   | \* Type: soft                                                                                                                                                                                                                           |
|             |                                   |                                                                                                                                                                                                                                         |
|             |                                   | \* The resource will be demoted, stopped and then started (and possibly promoted) again.                                                                                                                                                |
+-------------+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 190         |                                   | \* The service is found to be properly active, but in such a condition that future failures are more likely.                                                                                                                            |
+-------------+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 191         |                                   | \* The resource agent supports roles and the service is found to be properly active in the promoted role, but in such a condition that future failures are more likely.                                                                 |
+-------------+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| other       | N/A                               | Custom error code.                                                                                                                                                                                                                      |
+-------------+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table A.2. OCF Return Codes

Show more

## [Legal Notice](#idm140572713346336) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
