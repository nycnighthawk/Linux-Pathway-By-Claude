---
{"title": "Tuning performance in Identity Management", "guide": "tuning_performance_in_identity_management", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/tuning_performance_in_identity_management/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Tuning performance in Identity Management {#tuning-performance-in-identity-management .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Optimizing the IdM services, such as Directory Server, KDC, and SSSD, for better performance {#optimizing-the-idm-services-such-as-directory-server-kdc-and-sssd-for-better-performance .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140462320989536)

**Abstract**

Red Hat tunes Identity Management (IdM) to perform well in most deployments. However, in specific scenarios, it can be beneficial to tune IdM components, such as replication agreements, the Directory Server, the Kerberos Key Distribution Center (KDC), or the System Security Services Daemon (SSSD).

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

## [Chapter 1. Important considerations when tuning IdM](#important-considerations-when-tuning-idm) {#chapter-1.-important-considerations-when-tuning-idm .title}

Identity Management's component services are tuned to work in an optimal way for most deployments. As a System Administrator, you may want to adjust the performance of IdM services to suit the demands of your specific environment.

**Important considerations**

-   Each IdM deployment is a unique combination of hardware, software, networking, data, workloads, and many other factors. Adjustments that benefit one environment may be detrimental to another.
-   Performance-tuning is an iterative, experimental process. Make adjustments to only one variable at a time and monitor its impact on your environment. After achieving the desired result with one variable, adjust the next variable while continuing to monitor the performance of previous adjustments.

## [Chapter 2. Hardware recommendations](#hardware-recommendations) {#chapter-2.-hardware-recommendations .title}

RAM is the most important hardware feature to size properly. Make sure your system has enough RAM available.

Typical RAM requirements are:

-   For 10,000 users and 100 groups: at least 4 GB of RAM and 4 GB swap space
-   For 100,000 users and 50,000 groups: at least 16 GB of RAM and 4 GB of swap space

For larger deployments, increasing RAM is more effective than increasing disk space because much of the data is stored in cache. In general, adding more RAM leads to better performance for larger deployments due to caching. In virtualized environments, memory ballooning must be disabled or the complete RAM must be reserved for the guest IdM servers.

Note

A basic user entry or a simple host entry with a certificate is approximately 5---​10 kB in size.

## [Chapter 3. IdM server performance recommendations](#idm-server-performance-recommendations) {#chapter-3.-idm-server-performance-recommendations .title}

To ensure stable performance, Identity Management (IdM) enforces limits on the maximum number of users and clients that you can add or enroll to IdM server simultaneously.

+---------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Action                          | Description                                                                                                                                                                                                                                                                                | Number               |
+:================================+:===========================================================================================================================================================================================================================================================================================+:=====================+
| Client enrollments              | The maximum number of the IdM clients that you can enroll with an IdM server at the same time before enrollment starts failing.                                                                                                                                                            | 130                  |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Adding users                    | The maximum number of users you can add at the same time using the `ipa user-add`{.literal} command from different IdM clients before failing to add a user.                                                                                                                               | 325                  |
|                                 |                                                                                                                                                                                                                                                                                            |                      |
|                                 | You can add more users over the same amount of time by using the IdM API `batch`{.literal} command. We recommend adding users in batches of 100 users.                                                                                                                                     |                      |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Client authentications          | The maximum number of the IdM clients that can authenticate at the same time before authentications start to fail.                                                                                                                                                                         | 800                  |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Adding a member to a user group | The recommended number of members in a group that you can add without exceeding time for adding a new member to a group. IdM has a two-seconds rule as a normal time frame for adding a member to a group. You can add more members, but the time of the action will progressively extend. | 1500                 |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

: Table 3.1. Limits for IdM operations

Show more

**Additional resources**

-   [Using batches for executing IdM API commands](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_idm_api/basics-of-idm-api#using-batches-for-executing-idm-api-commands)

## [Chapter 4. Failover, load-balancing, and high-availability in IdM](#failover-load-balancing-and-high-availability-in-idm) {#chapter-4.-failover-load-balancing-and-high-availability-in-idm .title}

Identity Management (IdM) provides failover mechanisms for IdM clients and load-balancing and high-availability features for IdM servers. IdM clients and SSSD automatically select available servers and server-side architecture provides high availability by using multiple replicas.

### [4.1. Client-side failover capability](#client-side-failover-capability) {#client-side-failover-capability .title}

Client-side failover is the built-in SSSD mechanism on IdM clients that automatically determines and connects to available IdM servers to maintain continuous authentication and access.

The failover mechanism uses DNS SRV records to facilitate the discovery and switching between IdM servers when primary servers become unavailable.

Note

SSSD queries SRV records from the DNS server. By default, SSSD waits for `6`{.literal} seconds for a reply from the DNS resolver before attempting to query another DNS server. If all DNS servers are unreachable, the domain will continue to operate in offline mode. You can use the `dns_resolver_timeout`{.literal} option to increase the time the client waits for a reply from the DNS resolver.

The SSSD failover mechanism treats an IdM server, the machine, and its services independently:

Service failure
:   If the hostname resolution for a server succeeds, SSSD considers the machine online and tries to connect to the required service on that machine. If the connection to the service fails, SSSD considers only that specific service as offline, not the entire machine or other services on it.

Machine failure
:   If hostname resolution fails, SSSD considers the entire machine as offline, and does not attempt to connect to any services on that machine.

**Primary and backup server switching**

SSSD attempts to connect to primary servers first. When all primary servers are unavailable, SSSD switches to a configured backup server.

While connected to a backup server, SSSD periodically attempts to reconnect to one of the primary servers and connects immediately once a primary server becomes available. The interval between these attempts is controlled by the `failover_primary_timeout`{.literal} option, which defaults to 31 seconds.

If all IdM servers become unreachable, SSSD switches to offline mode. In this state, SSSD retries connections every 30 seconds until a server becomes available.

### [4.2. IdM server-side load-balancing and high availability](#idm-server-side-load-balancing-and-high-availability) {#idm-server-side-load-balancing-and-high-availability .title}

You can achieve load-balancing and high-availability in IdM by installing multiple IdM replicas, which provide active/active service availability across the IdM domain. This mechanism secures high service availability and inherent load-balancing across the clients.

-   If you have a geographically dispersed network, you can shorten the path between IdM clients and the nearest accessible server by configuring multiple IdM replicas per data center.
-   Red Hat supports environments with up to 60 replicas.
-   The IdM replication mechanism provides active/active service availability: services at all IdM replicas are readily available at the same time.

Note

Red Hat recommends against combining IdM and other load-balancing or high-availability (HA) software.

Many third-party high availability solutions assume active/passive scenarios and cause unnecessary service interruption to IdM availability. Other solutions use virtual IPs or a single hostname per clustered service. All these methods do not typically work well with the type of service availability provided by the IdM solution. They also integrate very poorly with Kerberos, decreasing the overall security and stability of the deployment.

### [4.3. Configuring SSSD client failover](#configuring-sssd-client-failover) {#configuring-sssd-client-failover .title}

Configure the System Security Services Daemon (SSSD) on an IdM client to manage server failover.

You can set server connection preferences in two ways: enable automatic DNS SRV record discovery or manually specify a prioritized list of primary and backup servers.

**Prerequisites**

-   You have `root`{.literal} privileges on the IdM client machine.
-   You know the Fully Qualified Domain Names (FQDNs) of your IdM servers.
-   If you are using the DNS method, ensure that DNS SRV records for your IdM servers are correctly configured.

**Procedure**

1.  Open the `/etc/sssd/sssd.conf`{.literal} file.

2.  Specify the list of servers using one of the following methods:

    a.  Specify `_srv_`{.literal} as the first value in the `ipa_server`{.literal} parameter, followed by a prioritized list of primary server FQDNs. Then, list any backup server FQDNs in the `ipa_backup_server`{.literal} parameter. For example:

        ``` {.language-plaintext tabindex="-1"}
        [domain/<idm_domain_name>]
        id_provider = ipa
        ipa_server = _srv_, <primary_idm_server1>, <primary_idm_server2>
        ipa_backup_server = <backup_idm_server1>, <backup_idm_server2>
        ...
        ```

        The `_srv_`{.literal} option is not supported for `ipa_backup_server`{.literal}.

    b.  To bypass DNS lookups for performance reasons, remove the `_srv_`{.literal} entry from the `ipa_server`{.literal} parameter and specify which IdM servers the client should connect to, in order of preference:

        ``` {.language-plaintext tabindex="-1"}
        [domain/<idm_domain_name>]
        id_provider = ipa
        ipa_server = <primary_idm_server1>, <primary_idm_server2>
        ipa_backup_server = <backup_idm_server1>, <backup_idm_server2>
        ...
        ```

### [4.4. IdM server configuration and failover parameters](#idm-server-configuration-and-failover-parameters) {#idm-server-configuration-and-failover-parameters .title}

The `ipa_server`{.literal} parameter in `/etc/sssd/sssd.conf`{.literal} controls System Security Services Daemon (SSSD) client failover and server resolution. Specify servers using DNS SRV records or manual addresses.

**Server configuration options**

The `ipa_server`{.literal} parameter and the `srv`{.literal} option define how SSSD on the client resolves and connects to available IdM servers:

-   With the `_srv_`{.literal} option specified, SSSD retrieves a list of IdM servers ordered by preference. If a primary server goes offline, the SSSD service on the IdM client automatically connects to another available IdM server.
-   Primary servers are specified in the `ipa_server`{.literal} parameter. SSSD attempts to connect to primary servers first and switches to backup servers only if no primary servers are available.
-   The `_srv_`{.literal} option is not supported for backup servers.
-   Removing the `_srv_`{.literal} entry and listing servers explicitly, such as `ipa_server = idm_server1.example.com,idm_server2.example.com`{.literal}, bypasses DNS lookups. This configuration ensures the client connects to the specified IdM servers only, using the listed order of preference.

+--------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter                            | Default value        | Description                                                                                                                                                                                     |
+:=====================================+:=====================+:================================================================================================================================================================================================+
| `failover_primary_timeout`{.literal} | **31 seconds**       | The interval between attempts SSSD makes to reconnect to one of the primary servers while it is connected to a backup server.                                                                   |
+--------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `dns_resolver_timeout`{.literal}     | **6 seconds**        | The time the client waits for a reply from the DNS resolver before attempting to query another DNS server. If all DNS servers are unreachable, the domain continues to operate in offline mode. |
+--------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 4.1. Failover and timeout parameters

Show more

## [Chapter 5. Optimizing the replica topology](#optimizing-the-replica-topology) {#chapter-5.-optimizing-the-replica-topology .title}

A robust replica topology distributes workloads and reduces replication delays. Follow these guidelines to optimize the layout of your replica topology.

### [5.1. Guidelines for determining the appropriate number of IdM replicas in a topology](#guidelines-for-determining-the-appropriate-number-of-idm-replicas-in-a-topology) {#guidelines-for-determining-the-appropriate-number-of-idm-replicas-in-a-topology .title}

To ensure optimal performance and service availability, use these guidelines to plan your IdM topology and determine the appropriate number of replicas that meet your organization's specific requirements.

Deploy at least two replicas in each data center
:   Deploy at least two replicas in each data center to ensure that if one server fails, the replica can take over and handle requests.

Deploy a sufficient number of servers to serve your clients
:   One Identity Management (IdM) server can provide services to 2000 - 3000 clients. This assumes the clients query the servers multiple times a day, but not, for example, every minute. If you expect frequent queries, plan for more servers.

Deploy a sufficient number of Certificate Authority (CA) replicas
:   Only replicas with the CA role installed can replicate certificate data. If you use the IdM CA, ensure your environment has at least two CA replicas with certificate replication agreements between them.

Deploy a maximum of 60 replicas in a single IdM domain
:   Red Hat supports environments with up to 60 replicas.

### [5.2. Uninstalling the IdM CA service from an IdM server](#uninstalling-the-idm-ca-service-from-an-idm-server) {#uninstalling-the-idm-ca-service-from-an-idm-server .title}

If you have more than four Identity Management (IdM) replicas with the **CA role** in your topology and you run into performance problems due to redundant certificate replication, remove redundant CA service instances from IdM replicas.

To do this, you must first decommission the affected IdM replicas completely, then reinstall IdM on them without the CA service.

Note

While you can **add** the CA role to an IdM replica, IdM does not provide a method to **remove** only the CA role from an IdM replica: the `ipa-ca-install`{.literal} command does not have an `--uninstall`{.literal} option. This limitation applies to all other IdM server roles, including `DNS server`{.literal}, `KRA server`{.literal}, `AD trust agent`{.literal}, and `AD trust controller`{.literal}. In each case, removing a role requires fully decommissioning the replica and reinstalling it without the unwanted role.

**Prerequisites**

-   You have the IdM CA service installed on more than four IdM servers in your topology.

**Procedure**

1.  Identify the redundant CA service and follow the procedure in [Uninstalling an IdM server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/uninstalling-an-idm-server) on the IdM replica that hosts this service.
2.  On the same host, follow the procedure in [Installing an IdM server: With integrated DNS, without a CA](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-idm-server-with-integrated-dns-without-a-ca).

### [5.3. Additional resources](#optimizing-the-replica-topology_53-additional-resources) {#additional-resources .title}

-   [Planning the replica topology](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/planning-the-replica-topology)
-   [Guidelines for connecting IdM replicas in a topology](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/planning-the-replica-topology#guidelines-for-connecting-idm-replicas-in-a-topology)
-   [Managing replication topology](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_replication_in_identity_management/managing-replication-topology)
-   [Replica topology examples](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/planning-the-replica-topology#replica-topology-examples)

## [Chapter 6. Adjusting the search size and time limit](#adjusting-the-search-size-and-time-limit) {#chapter-6.-adjusting-the-search-size-and-time-limit .title}

Some queries, such as requesting a list of IdM users, can return a very large number of entries. By tuning these search operations, you can improve the overall server performance when running the `ipa *-find`{.literal} commands, such as `ipa user-find`{.literal}, and when displaying corresponding lists in the Web UI.

Search size limit

:   Defines the maximum number of entries returned for a request sent to the server from a client's CLI or from a browser accessing the IdM Web UI.

    Default: 100 entries.

Search time limit

:   Defines the maximum time (in seconds) that the server waits for searches to run. Once the search reaches this limit, the server stops the search and returns the entries discovered in that time.

    Default: 2 seconds.

If you set the values to `-1`{.literal}, IdM does not apply any limits when searching.

Important

Setting search size or time limits too high can negatively affect server performance.

### [6.1. Adjusting the search size and time limit in the command line](#adjusting-the-search-size-and-time-limit-in-the-command-line) {#adjusting-the-search-size-and-time-limit-in-the-command-line .title}

You can adjust the search size and time limits globally or for a specific entry to optimize search performance and responsiveness.

**Procedure**

1.  To display current search time and size limits in CLI, use the `ipa config-show`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa config-show

    Search time limit: 2
    Search size limit: 100
    ```

2.  To adjust the limits **globally** for all queries, use the `ipa config-mod`{.literal} command and add the `--searchrecordslimit`{.literal} and `--searchtimelimit`{.literal} options. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa config-mod --searchrecordslimit=500 --searchtimelimit=5
    ```

3.  To **temporarily** adjust the limits only for a specific query, add the `--sizelimit`{.literal} or `--timelimit`{.literal} options to the command. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-find --sizelimit=200 --timelimit=120
    ```

### [6.2. Adjusting the search size and time limit in the Web UI](#adjusting-the-search-size-and-time-limit-in-the-web-ui) {#adjusting-the-search-size-and-time-limit-in-the-web-ui .title}

You can adjust global search size and time limits using the IdM Web UI to optimize search performance and responsiveness.

**Procedure**

1.  Log in to the IdM Web UI.

2.  Click **IPA Server**.

3.  On the **IPA Server** tab, click **Configuration**.

4.  Set the required values in the **Search Options** area.

    Default values are:

    -   Search size limit: 100 entries
    -   Search time limit: 2 seconds

5.  Click **Save** at the top of the page.

## [Chapter 7. Adjusting IdM Directory Server performance](#adjusting-idm-directory-server-performance) {#chapter-7.-adjusting-idm-directory-server-performance .title}

You can tune the performance of Identity Management's databases by adjusting LDAP attributes controlling the Directory Server's resources and behavior.

You can fine-tune the following:

-   Adjust how the Directory Server **caches data**.
-   Adjust the Directory Server's **resource limits**.
-   Adjust **timeouts** that have the most influence on performance.
-   Install an IdM server or replica with custom Directory Server settings from an LDIF file.

### [7.1. Adjusting the entry cache size in the IdM Directory Server](#adjusting-the-entry-cache-size-in-the-idm-directory-server) {#adjusting-the-entry-cache-size-in-the-idm-directory-server .title}

You can adjust the entry cache size to optimize memory usage for the IdM Directory Server when default auto-sizing does not meet your deployment requirements.

Important

Do not change this settings, unless you have a strong need to apply your custom values. IdM Directory Server uses the built-in cache auto-sizing feature for optimized performance.

The `nsslapd-cachememsize`{.literal} attribute specifies the size, in bytes, for the available memory space for the entry cache. This attribute is one of the most important values for controlling how much physical RAM the Directory Server uses.

If the entry cache size is too small, you might see the following error in the Directory Server error logs in the `/var/log/dirsrv/slapd-`{.literal}*`<instance_name>`{.literal}*`/errors`{.literal} log file:

``` {.language-plaintext tabindex="-1"}
REASON: entry too large (83886080 bytes) for the import buffer size (67108864 bytes).  Try increasing nsslapd-cachememsize.
```

Red Hat recommends fitting the entry cache and the database index entry cache in memory.

+:----------------------------------+:-----------------------------------------------------------------------------------------------+
| **Default value**                 | `209715200`{.literal} *(200 MiB)*                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------------+
| **Valid range**                   | `500000 - 18446744073709551615`{.literal} *(500 kB - (2^64^-1))*                               |
+-----------------------------------+------------------------------------------------------------------------------------------------+
| **Entry DN location**             | `cn=`{.literal}*`<database_name>`{.literal}*`,cn=ldbm database,cn=plugins,cn=config`{.literal} |
+-----------------------------------+------------------------------------------------------------------------------------------------+

: Table 7.1. nsslapd-cachememsize attribute values

Show more

**Prerequisites**

-   The LDAP Directory Manager password

**Procedure**

1.  Disable automatic cache tuning.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> backend config set --cache-autosize=0
    ```

2.  Display the database suffixes and their corresponding back ends.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> backend suffix list
    ```

    ``` {.language-plaintext tabindex="-1"}
    cn=changelog (changelog)
    dc=example,dc=com (userroot)
    o=ipaca (ipaca)
    ```

    This command displays the name of the back end database next to each suffix. Use the suffix's database name in the next step.

3.  Set the entry cache size for the database. This example sets the entry cache for the userroot database to 2 gigabytes.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> backend suffix set --cache-memsize=2147483648 userroot
    ```

4.  Restart the Directory Server.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# systemctl restart dirsrv.target
    ```

5.  Monitor the IdM Directory Server's performance. If it does not improve, repeat this procedure and adjust `cache-memsize`{.literal} to a different value, or re-enable cache auto-sizing.

**Verification**

-   Display the value of the `nsslapd-cachememsize`{.literal} attribute and verify it has been set to your desired value.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ldapsearch -D "cn=Directory Manager" -w <directory_manager_password> -b "cn=userroot,cn=ldbm database,cn=plugins,cn=config" | grep nsslapd-cachememsize
    nsslapd-cachememsize: 2147483648
    ```

**Additional resources**

-   [nsslapd-cachememsize](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuration_and_schema_reference/index#nsslapd-cachememsize)
-   [Re-enabling entry and database cache auto-sizing](#re-enabling-database-and-entry-cache-auto-sizing-in-the-idm-directory-server "7.3. Re-enabling database and entry cache auto-sizing in the IdM Directory Server")

### [7.2. Adjusting the database index cache size in the IdM Directory Server](#adjusting-the-database-index-cache-size-in-the-idm-directory-server) {#adjusting-the-database-index-cache-size-in-the-idm-directory-server .title}

You can adjust the database index cache size to improve search performance when the IdM Directory Server has available RAM beyond the entry cache allocation.

Important

Do not change this settings, unless you have a strong need to apply your custom values. IdM Directory Server uses the built-in cache auto-sizing feature for optimized performance.

The `nsslapd-dbcachesize`{.literal} attribute controls the amount of memory the database indexes use. This cache size has less of an impact on Directory Server performance than the entry cache size does, but if there is available RAM after the entry cache size is set, Red Hat recommends increasing the amount of memory allocated to the database cache.

The database cache is limited to 1.5 GB RAM because higher values do not improve performance.

+:----------------------------------+:------------------------------------------------------------+
| **Default value**                 | `10000000`{.literal} *(10 MB)*                              |
+-----------------------------------+-------------------------------------------------------------+
| **Valid range**                   | `500000 - 1610611911`{.literal} *(500 kB - 1.5GB)*          |
+-----------------------------------+-------------------------------------------------------------+
| **Entry DN location**             | `cn=config,cn=ldbm database,cn=plugins,cn=config`{.literal} |
+-----------------------------------+-------------------------------------------------------------+

: Table 7.2. nsslapd-dbcachesize attribute values

Show more

**Prerequisites**

-   The LDAP Directory Manager password

**Procedure**

1.  Disable automatic cache tuning, and set the database cache size. This example sets the database cache to 256 megabytes.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> backend config set --cache-autosize=0 --dbcachesize=268435456
    ```

2.  Restart the Directory Server.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# systemctl restart dirsrv.target
    ```

3.  Monitor the IdM Directory Server's performance. If it does not improve, repeat this procedure and adjust `dbcachesize`{.literal} to a different value, or re-enable cache auto-sizing.

**Verification**

-   Display the value of the `nsslapd-dbcachesize`{.literal} attribute and verify it has been set to your desired value.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ldapsearch -D "cn=Directory Manager" -w <directory_manager_password> -b "cn=config,cn=ldbm database,cn=plugins,cn=config" | grep nsslapd-dbcachesize
    nsslapd-dbcachesize: 2147483648
    ```

**Additional resources**

-   [nsslapd-dbcachesize](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuration_and_schema_reference/index#nsslapd-dbcachesize)
-   [Re-enabling entry and database cache auto-sizing](#re-enabling-database-and-entry-cache-auto-sizing-in-the-idm-directory-server "7.3. Re-enabling database and entry cache auto-sizing in the IdM Directory Server")

### [7.3. Re-enabling database and entry cache auto-sizing in the IdM Directory Server](#re-enabling-database-and-entry-cache-auto-sizing-in-the-idm-directory-server) {#re-enabling-database-and-entry-cache-auto-sizing-in-the-idm-directory-server .title}

You can restore the default cache auto-sizing settings to let the IdM Directory Server automatically optimize cache sizes based on available hardware resources.

Important

Use the built-in cache auto-sizing feature for optimized performance. Do not set cache sizes manually.

By default, the IdM Directory Server automatically determines the optimal size for the database cache and entry cache. Auto-sizing sets aside a portion of free RAM and optimizes the size of both caches based on the hardware resources of the server when the instance starts.

Use this procedure to undo custom database cache and entry cache values and restore the cache auto-sizing feature to its default values.

+:---------------------------------------+:----------------------------------------------------------------------------------------------------------------------------------------------------+
| **`nsslapd-cache-autosize`{.literal}** | This settings controls how much free RAM is allocated for auto-sizing the database and entry caches. A value of `0`{.literal} disables auto-sizing. |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **Default value**                      | `10`{.literal} *(10% of free RAM)*                                                                                                                  |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **Valid range**                        | `0 - 100`{.literal}                                                                                                                                 |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **Entry DN location**                  | `cn=config,cn=ldbm database,cn=plugins,cn=config`{.literal}                                                                                         |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 7.3. nsslapd-cache-autosize attribute values

Show more

+:---------------------------------------------+:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **`nsslapd-cache-autosize-split`{.literal}** | This value sets the percentage of free memory determined by `nsslapd-cache-autosize`{.literal} that is used for the database cache. The remaining percentage is used for the entry cache. |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Default value**                            | `25`{.literal} *(25% for the database cache, 60% for the entry cache)*                                                                                                                    |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Valid range**                              | `0 - 100`{.literal}                                                                                                                                                                       |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Entry DN location**                        | `cn=config,cn=ldbm database,cn=plugins,cn=config`{.literal}                                                                                                                               |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 7.4. nsslapd-cache-autosize-split attribute values

Show more

**Prerequisites**

-   You have previously disabled database and entry cache auto-tuning.

**Procedure**

1.  Stop the Directory Server instance.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# systemctl stop dirsrv.target
    ```

2.  Backup the `/etc/dirsrv/`{.literal}*`slapd-<instance_name>`{.literal}*`/dse.ldif`{.literal} file before making any further modifications.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# cp /etc/dirsrv/slapd-<instance_name>/dse.ldif \ /etc/dirsrv/slapd-<instance_name>/dse.ldif.bak.$(date "+%F_%H-%M-%S")
    ```

3.  Edit the `/etc/dirsrv/`{.literal}*`slapd-<instance_name>`{.literal}*`/dse.ldif`{.literal} file:

    a.  Set the percentage of free system RAM to use for the database and entry caches back to the default of 10% of free RAM.

        ``` {.language-plaintext tabindex="-1"}
        nsslapd-cache-autosize: 10
        ```

    b.  Set the percentage used from the free system RAM for the database cache to the default of 25%:

        ``` {.language-plaintext tabindex="-1"}
        nsslapd-cache-autosize-split: 25
        ```

4.  Save your changes to the `/etc/dirsrv/`{.literal}*`slapd-<instance_name>`{.literal}*`/dse.ldif`{.literal} file.

5.  Start the Directory Server.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# systemctl start dirsrv.target
    ```

**Verification**

-   Display the values of the `nsslapd-cache-autosize`{.literal} and `nsslapd-cache-autosize-split`{.literal} attributes and verify they have been set to your desired values.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ldapsearch -D "cn=Directory Manager" -w <directory_manager_password> -b "cn=config,cn=ldbm database,cn=plugins,cn=config" | grep nsslapd-cache-autosize nsslapd-cache-autosize: *10
    nsslapd-cache-autosize-split: 25
    ```

**Additional resources**

-   [nsslapd-cache-autosize](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuration_and_schema_reference/index#nsslapd-cache-autosize)
-   [nsslapd-cache-autosize-split](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuration_and_schema_reference/index#nsslapd-cache-autosize-split)

### [7.4. Adjusting the DN cache size in the IdM Directory Server](#adjusting-the-dn-cache-size-in-the-idm-directory-server) {#adjusting-the-dn-cache-size-in-the-idm-directory-server .title}

You can adjust the Distinguished Names (DN) cache size to improve the performance of lookup operations in the IdM Directory Server.

Important

Do not change this settings, unless you have a strong need to apply your custom values. IdM Directory Server uses the built-in cache auto-sizing feature for optimized performance.

The `nsslapd-dncachememsize`{.literal} attribute specifies the size, in bytes, for the available memory space for the Distinguished Names (DN) cache. The DN cache is similar to the entry cache for a database, but its table stores only the entry ID and the entry DN, which allows faster lookups for `rename`{.literal} and `moddn`{.literal} operations.

+:----------------------------------+:---------------------------------------------------------------------------------------------+
| **Default value**                 | `10485760`{.literal} *(10 MB)*                                                               |
+-----------------------------------+----------------------------------------------------------------------------------------------+
| **Valid range**                   | `500000 - 18446744073709551615`{.literal} *(500 kB - (2^64^-1))*                             |
+-----------------------------------+----------------------------------------------------------------------------------------------+
| **Entry DN location**             | `cn=`{.literal}*`database-name`{.literal}*`,cn=ldbm database,cn=plugins,cn=config`{.literal} |
+-----------------------------------+----------------------------------------------------------------------------------------------+

: Table 7.5. nsslapd-dncachememsize attribute values

Show more

**Prerequisites**

-   The LDAP Directory Manager password

**Procedure**

1.  Optional: Display the database suffixes and their corresponding database names.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> backend suffix list
    ```

    ``` {.language-plaintext tabindex="-1"}
    dc=example,dc=com (userroot)
    ```

    This command displays the name of the back end database next to each suffix. Use the suffix's database name in the next step.

2.  Set the DN cache size for the database. This example sets the DN cache to 20 megabytes.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> backend suffix set --dncache-memsize=20971520 userroot
    ```

3.  Restart the Directory Server.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# systemctl restart dirsrv.target
    ```

4.  Monitor the IdM Directory Server's performance. If it does not improve, repeat this procedure and adjust `dncache-memsize`{.literal} to a different value, or back to the default of 10 MB.

**Verification**

-   Display the new value of the `nsslapd-dncachememsize`{.literal} attribute and verify it has been set to your desired value.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ldapsearch -D "cn=Directory Manager" -w <directory_manager_password> -b "cn=userroot,cn=ldbm database,cn=plugins,cn=config" | grep nsslapd-dncachememsize
    nsslapd-dncachememsize: 20971520
    ```

**Additional resources**

-   [nsslapd-dncachememsize](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html-single/configuration_and_schema_reference/index#nsslapd-dncachememsize)

### [7.5. Adjusting the normalized DN cache size in the IdM Directory Server](#adjusting-the-normalized-dn-cache-size-in-the-idm-directory-server) {#adjusting-the-normalized-dn-cache-size-in-the-idm-directory-server .title}

You can adjust the normalized DN cache size to retain more frequently used DNs in memory and improve lookup performance in the IdM Directory Server.

Important

Do not change this settings, unless you have a strong need to apply your custom values. IdM Directory Server uses the built-in cache auto-sizing feature for optimized performance.

The `nsslapd-ndn-cache-max-size`{.literal} attribute controls the size, in bytes, of the cache that stores normalized distinguished names (NDNs). Increasing this value will retain more frequently used DNs in memory.

+:----------------------------------+:----------------------------------+
| **Default value**                 | `20971520`{.literal} *(20 MB)*    |
+-----------------------------------+-----------------------------------+
| **Valid range**                   | `0 - 2147483647`{.literal}        |
+-----------------------------------+-----------------------------------+
| **Entry DN location**             | `cn=config`{.literal}             |
+-----------------------------------+-----------------------------------+

: Table 7.6. nsslapd-ndn-cache-max-size attribute values

Show more

**Procedure**

1.  Ensure the NDN cache is enabled.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config get nsslapd-ndn-cache-enabled
    ```

    ``` {.language-plaintext tabindex="-1"}
    nsslapd-ndn-cache-enabled: on
    ```

    If the cache is `off`{.literal}, enable it with the following command.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config replace nsslapd-ndn-cache-enabled=on
    ```

    ``` {.language-plaintext tabindex="-1"}
    Successfully replaced "nsslapd-ndn-cache-enabled"
    ```

2.  Retrieve the current value of the `nsslapd-ndn-cache-max-size`{.literal} parameter and make a note of it before making any adjustments, in case it needs to be restored.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config get nsslapd-ndn-cache-max-size
    ```

    ``` {.language-plaintext tabindex="-1"}
    nsslapd-ndn-cache-max-size: 20971520
    ```

3.  Modify the value of the `nsslapd-ndn-cache-max-size`{.literal} attribute. This example increases the value to `41943040`{.literal} (40 MB).

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config replace nsslapd-ndn-cache-max-size=41943040
    ```

4.  Monitor the IdM Directory Server's performance. If it does not improve, repeat this procedure and adjust `nsslapd-ndn-cache-max-size`{.literal} to a different value, or re-enable cache auto-sizing.

**Verification**

-   Display the new value of the `nsslapd-ndn-cache-max-size`{.literal} attribute and verify it has been set to your desired value.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config get nsslapd-ndn-cache-max-size
    ```

    ``` {.language-plaintext tabindex="-1"}
    nsslapd-ndn-cache-max-size: 41943040
    ```

**Additional resources**

-   [nsslapd-ndn-cache-max-size](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuration_and_schema_reference/index#nsslapd-ndn-cache-max-size)

### [7.6. Adjusting the maximum message size in the IdM Directory Server](#adjusting-the-maximum-message-size-in-the-idm-directory-server) {#adjusting-the-maximum-message-size-in-the-idm-directory-server .title}

Increase the maximum LDAP message size to support larger legitimate requests in IdM Directory Server. This prevents errors when adding entries or performing operations that exceed the default 2 MB limit.

The `nsslapd-maxbersize`{.literal} attribute sets the maximum size in bytes allowed for an incoming message or LDAP request. Limiting the size of requests prevents some kinds of denial of service attacks.

If the maximum message size is too small, you might see the following error in the Directory Server error logs at `/var/log/dirsrv/slapd-`{.literal}*`<instance_name>`{.literal}*`/errors`{.literal}:

``` {.language-plaintext tabindex="-1"}
Incoming BER Element was too long, max allowable is 2097152 bytes. Change the nsslapd-maxbersize attribute in cn=config to increase.
```

The limit applies to the total size of the LDAP request. For example, if the request is to add an entry and if the entry in the request is larger than the configured value or the default, then the add request is denied. However, the limit is not applied to replication processes. Be cautious before changing this attribute.

+:----------------------------------+:-----------------------------------------+
| **Default value**                 | `2097152`{.literal} *(2 MB)*             |
+-----------------------------------+------------------------------------------+
| **Valid range**                   | `0 - 2147483647`{.literal} *(0 to 2 GB)* |
+-----------------------------------+------------------------------------------+
| **Entry DN location**             | `cn=config`{.literal}                    |
+-----------------------------------+------------------------------------------+

: Table 7.7. nsslapd-maxbersize attribute values

Show more

**Procedure**

1.  Retrieve the current value of the `nsslapd-maxbersize`{.literal} parameter and make a note of it before making any adjustments, in case it needs to be restored.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config get nsslapd-maxbersize
    ```

    ``` {.language-plaintext tabindex="-1"}
    nsslapd-maxbersize: 2097152
    ```

2.  Modify the value of the `nsslapd-maxbersize`{.literal} attribute. This example increases the value to `4194304`{.literal}, 4 MB.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config replace nsslapd-maxbersize=4194304
    ```

    ``` {.language-plaintext tabindex="-1"}
    Successfully replaced "nsslapd-maxbersize"
    ```

3.  Monitor the IdM Directory Server's performance. If it does not improve, repeat this procedure and adjust `nsslapd-maxbersize`{.literal} to a different value, or back to the default of `2097152`{.literal}.

**Verification**

-   Display the value of the `nsslapd-maxbersize`{.literal} attribute and verify it has been set to your desired value.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config get nsslapd-maxbersize
    ```

    ``` {.language-plaintext tabindex="-1"}
    nsslapd-maxbersize: 4194304
    ```

**Additional resources**

-   [nsslapd-maxbersize](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuration_and_schema_reference/index#nsslapd-maxbersize)

### [7.7. Adjusting the maximum number of file descriptors in the IdM Directory Server](#adjusting-the-maximum-number-of-file-descriptors-in-the-idm-directory-server) {#adjusting-the-maximum-number-of-file-descriptors-in-the-idm-directory-server .title}

You can adjust the maximum number of file descriptors to handle more simultaneous client connections, log files, and socket resources in the IdM Directory Server.

A value can be defined for the `DefaultLimitNOFILE`{.literal} parameter in the `/etc/systemd/system.conf`{.literal} file. An administrator with `root`{.literal} privileges can set the `DefaultLimitNOFILE`{.literal} parameter for the `ns-slapd`{.literal} process to a lower value by using the `setrlimit`{.literal} command. This value then takes precedence over what is in `/etc/systemd/system.conf`{.literal} and is accepted by the Identity Management (IdM) Directory Server (DS) as the value for the `nsslapd-maxdescriptors`{.literal} attribute.

The `nsslapd-maxdescriptors`{.literal} attribute sets the maximum, platform-dependent number of file descriptors that the IdM LDAP uses. File descriptors are used for client connections, log files, sockets, and other resources.

If no value is defined in either `/etc/systemd/system.conf`{.literal} or by `setrlimit`{.literal}, then IdM DS sets the `nsslapd-maxdescriptors`{.literal} attribute to 1048576.

If an IdM DS administrator later decides to set a new value for `nsslapd-maxdescriptors`{.literal} manually, then IdM DS compares the new value with what is defined locally, by `setrlimit`{.literal} or in `/etc/systemd/system.conf`{.literal}, with the following result:

-   If the new value for `nsslapd-maxdescriptors`{.literal} is higher than what is defined locally, then the server rejects the new value setting and continues to enforce the local limit value as the high watermark value.
-   If the new value is lower than what is defined locally, then the new value will be used.

This procedure describes how to set a new value for `nsslapd-maxdescriptors`{.literal}.

**Procedure**

1.  Retrieve the current value of the `nsslapd-maxdescriptors`{.literal} parameter and make a note of it before making any adjustments, in case it needs to be restored.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config get nsslapd-maxdescriptors
    ```

    ``` {.language-plaintext tabindex="-1"}
    nsslapd-maxdescriptors: 4096
    ```

2.  Modify the value of the `nsslapd-maxdescriptors`{.literal} attribute. This example increases the value to `8192`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config replace nsslapd-maxdescriptors=8192
    ```

    ``` {.language-plaintext tabindex="-1"}
    Successfully replaced "nsslapd-maxdescriptors"
    ```

3.  Monitor the IdM Directory Server's performance. If it does not improve, repeat this procedure and adjust `nsslapd-maxdescriptors`{.literal} to a different value, or back to the default of `4096`{.literal}.

**Verification**

-   Display the value of the `nsslapd-maxdescriptors`{.literal} attribute and verify it has been set to your desired value.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config get nsslapd-maxdescriptors
    ```

    ``` {.language-plaintext tabindex="-1"}
    nsslapd-maxdescriptors: 8192
    ```

**Additional resources**

-   [nsslapd-maxdescriptors (Maximum File Descriptors)](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuration_and_schema_reference/index#nsslapd-maxdescriptors)

### [7.8. Adjusting the connection backlog size in the IdM Directory Server](#adjusting-the-connection-backlog-size-in-the-idm-directory-server) {#adjusting-the-connection-backlog-size-in-the-idm-directory-server .title}

You can increase the connection backlog size to handle more incoming LDAP requests before the IdM Directory Server starts refusing them.

The listen service sets the number of sockets available to receive incoming connections. The `nsslapd-listen-backlog-size`{.literal} value sets the maximum length of the queue for the `sockfd`{.literal} socket before refusing connections.

If your IdM environment handles a large amount of connections, consider increasing the value of `nsslapd-listen-backlog-size`{.literal}.

+:----------------------------------+:------------------------------------+
| **Default value**                 | `128`{.literal} queue slots         |
+-----------------------------------+-------------------------------------+
| **Valid range**                   | `0 - 9223372036854775807`{.literal} |
+-----------------------------------+-------------------------------------+
| **Entry DN location**             | `cn=config`{.literal}               |
+-----------------------------------+-------------------------------------+

: Table 7.8. nsslapd-listen-backlog-size attribute values

Show more

**Procedure**

1.  Retrieve the current value of the `nsslapd-listen-backlog-size`{.literal} parameter and make a note of it before making any adjustments, in case it needs to be restored.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config get nsslapd-listen-backlog-size
    ```

    ``` {.language-plaintext tabindex="-1"}
    nsslapd-listen-backlog-size: 128
    ```

2.  Modify the value of the `nsslapd-listen-backlog-size`{.literal} attribute. This example increases the value to `192`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config replace nsslapd-listen-backlog-size=192
    ```

    ``` {.language-plaintext tabindex="-1"}
    Successfully replaced "nsslapd-listen-backlog-size"
    ```

**Verification**

-   Display the value of the `nsslapd-listen-backlog-size`{.literal} attribute and verify it has been set to your desired value.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config get nsslapd-listen-backlog-size
    ```

    ``` {.language-plaintext tabindex="-1"}
    nsslapd-listen-backlog-size: 192
    ```

**Additional resources**

-   [nsslapd-listen-backlog-size](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuration_and_schema_reference/index#nsslapd-listen-backlog-size)

### [7.9. Adjusting the maximum number of database locks in the IdM Directory Server](#adjusting-the-maximum-number-of-database-locks-in-the-idm-directory-server) {#adjusting-the-maximum-number-of-database-locks-in-the-idm-directory-server .title}

You can increase the maximum number of database locks to resolve \"out of available locks\" errors in the IdM Directory Server.

Lock mechanisms control how many copies of Directory Server processes can run at the same time, and the `nsslapd-db-locks`{.literal} parameter sets the maximum number of locks.

Increase the maximum number of locks if you see the following error messages in the `/var/log/dirsrv/slapd-`{.literal}*`<instance_name>`{.literal}*`/errors`{.literal} log file:

``` {.language-plaintext tabindex="-1"}
libdb: Lock table is out of available locks
```

+:----------------------------------+:-------------------------------------------------------------------+
| **Default value**                 | `50000`{.literal} locks                                            |
+-----------------------------------+--------------------------------------------------------------------+
| **Valid range**                   | `0 - 2147483647`{.literal}                                         |
+-----------------------------------+--------------------------------------------------------------------+
| **Entry DN location**             | `cn=bdb,cn=config,cn=ldbm database,cn=plugins,cn=config`{.literal} |
+-----------------------------------+--------------------------------------------------------------------+

: Table 7.9. nsslapd-db-locks attribute values

Show more

**Prerequisites**

-   The LDAP Directory Manager password

**Procedure**

1.  Retrieve the current value of the `nsslapd-db-locks`{.literal} parameter and make a note of it before making any adjustments, in case it needs to be restored.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ldapsearch -D "cn=Directory Manager" -w <directory_manager_password> -b "cn=bdb,cn=config,cn=ldbm database,cn=plugins,cn=config" | grep nsslapd-db-locks
    nsslapd-db-locks: 50000
    ```

2.  Modify the value of the `locks`{.literal} attribute. This example doubles the value to `100000`{.literal} locks.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> backend config set --locks=100000
    ```

    ``` {.language-plaintext tabindex="-1"}
    Successfully updated database configuration
    ```

3.  Restart the Directory Server.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# systemctl restart dirsrv.target
    ```

**Verification**

-   Display the value of the `nsslapd-db-locks`{.literal} attribute and verify it has been set to your desired value.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ldapsearch -D "cn=directory manager" -w <directory_manager_password> -b "cn=bdb,cn=config,cn=ldbm database,cn=plugins,cn=config" | grep nsslapd-db-locks
    ```

    ``` {.language-plaintext tabindex="-1"}
    nsslapd-db-locks: 100000
    ```

**Additional resources**

-   [nsslapd-db-locks](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuration_and_schema_reference/index#nsslapd-db-locks)

### [7.10. Disabling the Transparent Huge Pages feature in the IdM Directory Server](#disabling-the-transparent-huge-pages-feature-in-the-idm-directory-server) {#disabling-the-transparent-huge-pages-feature-in-the-idm-directory-server .title}

Disable Transparent Huge Pages (THP) to improve IdM Directory Server performance and reduce latency. THP can slow down directory operations due to how IdM accesses memory.

THP is a Linux memory management feature enabled by default on RHEL. While THP benefits applications with contiguous memory access, it can degrade IdM Directory Server performance because the directory uses sparse memory access patterns.

**Procedure**

-   To disable the feature, see [Disabling the Transparent Huge Pages feature](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/management_configuration_and_operations/performance-tuning-of-rhds#disabling-the-transparent-huge-pages-feature) in Red Hat Directory Server 13 documentation.

**Additional resources**

-   [The negative effects of Transparent Huge Pages (THP) on RHDS](https://access.redhat.com/articles/6979747)

### [7.11. Adjusting the input/output block timeout in the IdM Directory Server](#adjusting-the-input-output-block-timeout-in-the-idm-directory-server) {#adjusting-the-inputoutput-block-timeout-in-the-idm-directory-server .title}

You can adjust the I/O block timeout to close connections to stalled LDAP clients faster and free up resources in the IdM Directory Server.

The `nsslapd-ioblocktimeout`{.literal} attribute sets the amount of time in milliseconds after which the connection to a stalled LDAP client is closed. An LDAP client is considered to be stalled when it has not made any I/O progress for read or write operations.

Lower the value of the `nsslapd-ioblocktimeout`{.literal} attribute to free up connections sooner.

+:----------------------------------+:----------------------------------+
| **Default value**                 | `10000`{.literal} milliseconds    |
+-----------------------------------+-----------------------------------+
| **Valid range**                   | `0 - 2147483647`{.literal}        |
+-----------------------------------+-----------------------------------+
| **Entry DN location**             | `cn=config`{.literal}             |
+-----------------------------------+-----------------------------------+

: Table 7.10. nsslapd-ioblocktimeout attribute values

Show more

**Procedure**

1.  Retrieve the current value of the `nsslapd-ioblocktimeout`{.literal} parameter and make a note of it before making any adjustments, in case it needs to be restored.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config get nsslapd-ioblocktimeout
    ```

    ``` {.language-plaintext tabindex="-1"}
    nsslapd-ioblocktimeout: 10000
    ```

2.  Modify the value of the `nsslapd-ioblocktimeout`{.literal} attribute. This example lowers the value to `8000`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config replace nsslapd-ioblocktimeout=8000
    ```

    ``` {.language-plaintext tabindex="-1"}
    Successfully replaced "nsslapd-ioblocktimeout"
    ```

3.  Monitor the IdM directory server's performance. If it does not improve, repeat this procedure and adjust `nsslapd-ioblocktimeout`{.literal} to a different value, or back to the default of `10000`{.literal}.

**Verification**

-   Display the value of the `nsslapd-ioblocktimeout`{.literal} attribute and verify it has been set to your desired value.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config get nsslapd-ioblocktimeout
    ```

    ``` {.language-plaintext tabindex="-1"}
    nsslapd-ioblocktimeout: 8000
    ```

**Additional resources**

-   [nsslapd-ioblocktimeout](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuration_and_schema_reference/index#nsslapd-ioblocktimeout)

### [7.12. Adjusting the idle connection timeout in the IdM Directory Server](#adjusting-the-idle-connection-timeout-in-the-idm-directory-server) {#adjusting-the-idle-connection-timeout-in-the-idm-directory-server .title}

You can adjust the idle connection timeout to close stale connections while keeping active connections available in the IdM Directory Server.

The `nsslapd-idletimeout`{.literal} attribute sets the amount of time in seconds after which an idle LDAP client connection is closed by the IdM server. A value of `0`{.literal} means that the server never closes idle connections.

Red Hat recommends adjusting this value so stale connections are closed, but active connections are not closed prematurely.

+:----------------------------------+:------------------------------------+
| **Default value**                 | `3600`{.literal} seconds *(1 hour)* |
+-----------------------------------+-------------------------------------+
| **Valid range**                   | `0 - 2147483647`{.literal}          |
+-----------------------------------+-------------------------------------+
| **Entry DN location**             | `cn=config`{.literal}               |
+-----------------------------------+-------------------------------------+

: Table 7.11. nsslapd-idletimeout attribute values

Show more

**Procedure**

1.  Retrieve the current value of the `nsslapd-idletimeout`{.literal} parameter and make a note of it before making any adjustments, in case it needs to be restored.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config get nsslapd-idletimeout
    ```

    ``` {.language-plaintext tabindex="-1"}
    nsslapd-idletimeout: 3600
    ```

2.  Modify the value of the `nsslapd-idletimeout`{.literal} attribute. This example lowers the value to `1800`{.literal} (30 minutes).

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config replace nsslapd-idletimeout=1800
    ```

    ``` {.language-plaintext tabindex="-1"}
    Successfully replaced "nsslapd-idletimeout"
    ```

3.  Monitor the IdM directory server's performance. If it does not improve, repeat this procedure and adjust `nsslapd-idletimeout`{.literal} to a different value, or back to the default of `3600`{.literal}.

**Verification**

-   Display the value of the `nsslapd-idletimeout`{.literal} attribute and verify it has been set to your desired value.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> config get nsslapd-idletimeout
    ```

    ``` {.language-plaintext tabindex="-1"}
    nsslapd-idletimeout: 1800
    ```

**Additional resources**

-   [nsslapd-idletimeout](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuration_and_schema_reference/index#nsslapd-idletimeout)

### [7.13. Adjusting the replication release timeout](#adjusting-the-replication-release-timeout) {#adjusting-the-replication-release-timeout .title}

You can adjust the replication release timeout to balance replication latency and update throughput between IdM replicas.

An IdM replica is exclusively locked during a replication session with another replica. In some environments, a replica is locked for a long time due to large updates or network congestion, which increases replication latency.

You can release a replica after a fixed amount of time by adjusting the `repl-release-timeout`{.literal} parameter. Red Hat recommends setting this value between `30`{.literal} and `120`{.literal}:

-   If the value is set too low, replicas are constantly reacquiring one another and replicas are not able to send larger updates.
-   A longer timeout can improve high-traffic situations where it is best if a server exclusively accesses a replica for longer amounts of time, but a value higher than `120`{.literal} seconds slows down replication.

+:----------------------------------+:----------------------------------+
| **Default value**                 | `60`{.literal} seconds            |
+-----------------------------------+-----------------------------------+
| **Valid range**                   | `0 - 2147483647`{.literal}        |
+-----------------------------------+-----------------------------------+
| **Recommended range**             | `30 - 120`{.literal}              |
+-----------------------------------+-----------------------------------+

: Table 7.12. repl-release-timeout attribute values

Show more

**Prerequisites**

-   The LDAP Directory Manager password

**Procedure**

1.  Display the database suffixes and their corresponding back ends.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> backend suffix list
    ```

    ``` {.language-plaintext tabindex="-1"}
    cn=changelog (changelog)
    dc=example,dc=com (userroot)
    o=ipaca (ipaca)
    ```

    This command displays the names of the back end databases next to their suffix. Use the suffix name in the next step.

2.  Modify the value of the `repl-release-timeout`{.literal} attribute for the main userroot database. This example increases the value to `90`{.literal} seconds.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> replication set --suffix="dc=example,dc=com" --repl-release-timeout=90
    ```

    ``` {.language-plaintext tabindex="-1"}
    Successfully replaced "repl-release-timeout"
    ```

3.  Optional: If your IdM environment uses the IdM Certificate Authority (CA), you can modify the value of the `repl-release-timeout`{.literal} attribute for the CA database. This example increases the value to `90`{.literal} seconds.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dsconf <ds_instance_name> replication set --suffix="o=ipaca" --repl-release-timeout=90
    ```

    ``` {.language-plaintext tabindex="-1"}
    Successfully replaced "repl-release-timeout"
    ```

4.  Restart the Directory Server.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# systemctl restart dirsrv.target
    ```

5.  Monitor the IdM Directory Server's performance. If it does not improve, repeat this procedure and adjust `repl-release-timeout`{.literal} to a different value, or back to the default of `60`{.literal} seconds.

**Verification**

-   Display the value of the `nsds5ReplicaReleaseTimeout`{.literal} attribute and verify it has been set to your desired value.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ldapsearch -D "cn=Directory Manager" -w <directory_manager_password> -b "cn=replica,cn=dc\3Dexample\2Cdc\3Dcom,cn=mapping tree,cn=config" | grep nsds5ReplicaReleaseTimeout
    ```

    ``` {.language-plaintext tabindex="-1"}
    nsds5ReplicaReleaseTimeout: 90
    ```

Note

The Distinguished Name of the suffix in this example is `dc=example,dc=com`{.literal}, but the equals sign (`=`{.literal}) and comma (`,`{.literal}) must be escaped in the `ldapsearch`{.literal} command.

Convert the suffix DN to `cn=dc\3Dexample\2Cdc\3Dcom`{.literal} with the following escape characters:

-   `\3D`{.literal} replacing `=`{.literal}
-   `\2C`{.literal} replacing `,`{.literal}

**Additional resources**

-   [nsDS5ReplicaReleaseTimeout](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuration_and_schema_reference/index#nsds5replicareleasetimeout)

### [7.14. Additional resources](#adjusting-idm-directory-server-performance_714-additional-resources) {#additional-resources-1 .title}

-   [Installing an IdM server or replica with custom Directory Server settings from an LDIF file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-idm-server-or-replica-with-custom-directory-server-and-certificate-authority-settings-from-ldif-and-ini-files#installing-an-idm-server-or-replica-with-custom-directory-server-settings-from-an-ldif-file)
-   [Performance tuning of Red Hat Directory Server 13](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/management_configuration_and_operations/performance-tuning-of-rhds)

## [Chapter 8. Adjusting the performance of the KDC](#adjusting-the-performance-of-the-kdc) {#chapter-8.-adjusting-the-performance-of-the-kdc .title}

To optimize the performance of Kerberos Key Distribution Center (KDC), which is responsible for authenticating users, hosts, and services, adjust key parameters based on your deployment's traffic patterns.

### [8.1. Adjusting the length of the KDC listen queue](#adjusting-the-length-of-the-kdc-listen-queue) {#adjusting-the-length-of-the-kdc-listen-queue .title}

Increase the KDC listen queue size to handle higher volumes of Kerberos authentication requests in busy IdM environments. This prevents connection delays during peak traffic periods.

You can adjust this setting using the `kdc_tcp_listen_backlog`{.literal} option in the `[kdcdefaults]`{.literal} section of the `/var/kerberos/krb5kdc/kdc.conf`{.literal} file. The default listen queue size value of `5`{.literal} may be too low for some IdM deployments that experience high amounts of Kerberos traffic, but setting this value too high degrades performance.

+:----------------------------------+:----------------------------------+
| Default value                     | `5`{.literal}                     |
+-----------------------------------+-----------------------------------+
| Valid range                       | `1 - 10`{.literal}                |
+-----------------------------------+-----------------------------------+

Show more

**Procedure**

1.  Open the `/var/kerberos/krb5kdc/kdc.conf`{.literal} file in a text editor.

2.  Set the TCP listen backlog to your desired value, such as `7`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [kdcdefaults]
     ...
     kdc_tcp_listen_backlog = 7
    ```

3.  Save and close the `/var/kerberos/krb5kdc/kdc.conf`{.literal} file.

4.  Restart the KDC to load the new settings.

### [8.2. Options controlling KDC behavior per realm](#options-controlling-kdc-behavior-per-realm) {#options-controlling-kdc-behavior-per-realm .title}

You can adjust KDC options per realm to improve performance by minimizing how often the KDC writes authentication tracking information to its database.

To track locking and unlocking user accounts for each Kerberos realm, the KDC writes to its database after each successful and failed authentication. By adjusting the following options in the `[dbmodules]`{.literal} section of the `/etc/krb5.conf`{.literal} file, you may be able to improve performance by minimizing how often the KDC writes information.

disable_last_success

:   If set to `true`{.literal}, this option suppresses KDC updates to the `Last successful authentication`{.literal} field of principal entries requiring preauthentication.

    +:----------------------------------+:--------------------------------------+
    | Default value                     | `false`{.literal}                     |
    +-----------------------------------+---------------------------------------+
    | Valid range                       | `true`{.literal} or `false`{.literal} |
    +-----------------------------------+---------------------------------------+

    Show more

disable_lockout

:   If set to `true`{.literal}, this option suppresses KDC updates to the `Last failed authentication`{.literal} and `Failed password attempts`{.literal} fields of principal entries requiring preauthentication. Setting this flag may improve performance, but disabling account lockout may be considered a security risk.

    +:----------------------------------+:--------------------------------------+
    | Default value                     | `false`{.literal}                     |
    +-----------------------------------+---------------------------------------+
    | Valid range                       | `true`{.literal} or `false`{.literal} |
    +-----------------------------------+---------------------------------------+

    Show more

**Additional resources**

-   [Adjusting KDC settings per realm](#adjusting-kdc-settings-per-realm "8.3. Adjusting KDC settings per realm")

### [8.3. Adjusting KDC settings per realm](#adjusting-kdc-settings-per-realm) {#adjusting-kdc-settings-per-realm .title}

Adjust KDC settings for a specific Kerberos realm by modifying the `/etc/krb5.conf`{.literal} file.

**Procedure**

1.  Open the `/etc/krb5.conf`{.literal} file in a text editor.

2.  Specify any options and their desired values within the `[dbmodules]`{.literal} section, and in the respective Kerberos realm. In this example, you are setting the `disable_last_success`{.literal} variable for the *`<kerberos_realm>`{.literal}*, for example EXAMPLE.COM.

    ``` {.language-plaintext tabindex="-1"}
    [dbmodules]
        <kerberos_realm> = {
            disable_last_success = true
        }
    ```

3.  Save and close the `/etc/krb5.conf`{.literal} file.

4.  Restart the KDC to load the new settings.

**Additional resources**

-   [Options controlling KDC behavior per realm](#options-controlling-kdc-behavior-per-realm "8.2. Options controlling KDC behavior per realm")

### [8.4. Adjusting the number of krb5kdc processes](#adjusting-the-number-of-krb5kdc-processes) {#adjusting-the-number-of-krb5kdc-processes .title}

You can manually adjust the number of worker processes that the Key Distribution Center (KDC) starts to handle incoming connections.

By default, the IdM installer detects the number of CPU cores and enters the value in the `/etc/sysconfig/krb5kdc`{.literal} file. For example, the file might contain the following entry:

``` {.language-plaintext tabindex="-1"}
KRB5KDC_ARGS='-w 2'
[...]
```

In this example, with the `KRB5KDC_ARGS`{.literal} parameter set to `-w 2`{.literal}, the KDC starts two separate processes to handle incoming connections from the main process. You might want to adjust this value, especially in virtual environments where you can easily add or remove the number of virtual CPUs based on your requirements. To prevent performance issues or even IdM servers becoming unresponsive due to an ever-increasing TCP/IP queue on port 88, simulate a higher number of processes by manually setting the `KRB5KDC_ARGS`{.literal} parameter to a higher value.

**Procedure**

1.  Open the `/etc/sysconfig/krb5kdc`{.literal} file in a text editor.

2.  Specify the value of the `KRB5KDC_ARGS`{.literal} parameter. In this example, you are setting the number of processes to 10:

    ``` {.language-plaintext tabindex="-1"}
    KRB5KDC_ARGS='-w 10'
    [...]
    ```

3.  Save and close the `/etc/sysconfig/krb5kdc`{.literal} file.

4.  Reload the systemd configuration:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

5.  Restart the `krb5kdc`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart krb5kdc.service
    ```

    Note

    You can use the IdM Healthcheck utility to verify that the KDC is configured to use the optimal number of worker processes. See [Verifying the optimal number of KDC worker processes by using IdM Healthcheck](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_idm_healthcheck_to_monitor_your_idm_environment/verifying-the-optimal-number-of-kdc-worker-processes-by-using-idm-healthcheck).

### [8.5. Additional resources](#adjusting-the-performance-of-the-kdc_85-additional-resources) {#additional-resources-2 .title}

-   [MIT Kerberos Documentation - kdc.conf](https://web.mit.edu/Kerberos/krb5-latest/doc/admin/conf_files/kdc_conf.html)

## [Chapter 9. Tuning SSSD performance for large IdM-AD trust deployments](#tuning-sssd-performance-for-large-idm-ad-trust-deployments) {#chapter-9.-tuning-sssd-performance-for-large-idm-ad-trust-deployments .title}

Retrieving user and group information is a very data-intensive operation for the System Security Services Daemon (SSSD), especially in an IdM deployment with a trust to a large Active Directory (AD) domain. You can improve this performance by adjusting which information SSSD retrieves from identity providers and for how long.

### [9.1. Tuning SSSD in IdM servers for large IdM-AD trust deployments](#tuning-sssd-in-idm-servers-for-large-idm-ad-trust-deployments) {#tuning-sssd-in-idm-servers-for-large-idm-ad-trust-deployments .title}

Apply tuning options to the configuration of the SSSD service in an IdM server to improve its response time when retrieving information from a large AD environment.

**Prerequisites**

-   You need `root`{.literal} permissions to edit the `/etc/sssd/sssd.conf`{.literal} configuration file.

**Procedure**

1.  Open the `/etc/sssd/sssd.conf`{.literal} configuration file in a text editor.

2.  Add the following options to the `[domain]`{.literal} section for your Identity Management (IdM) domain:

    ``` {.language-plaintext tabindex="-1"}
    [domain/<idm_domain_name>]
    ignore_group_members = true
    subdomain_inherit = ignore_group_members
    ...
    ```

    Note

    Settings listed in the `subdomain_inherit`{.literal} options apply to both the main (IdM) domain as well as the trusted AD domain(s).

3.  Save and close the `/etc/sssd/sssd.conf`{.literal} file on the server.

4.  Restart the SSSD service to load the configuration changes.

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# systemctl restart sssd
    ```

**Additional resources**

-   [Options for tuning SSSD in IdM servers and clients for large IdM-AD trust deployments](#options-in-sssd-conf-for-tuning-idm-servers-and-clients-for-large-idm-ad-trust-deployments "9.7. Options in sssd.conf for tuning IdM servers and clients for large IdM-AD trust deployments")

### [9.2. Tuning the config timeout for the ipa-extdom plugin on IdM servers](#tuning-the-config-timeout-for-the-ipa-extdom-plugin-on-idm-servers) {#tuning-the-config-timeout-for-the-ipa-extdom-plugin-on-idm-servers .title}

Adjust the `ipa-extdom`{.literal} plugin timeout to prevent failed lookups when IdM clients request Active Directory user and group information. Proper timeout configuration ensures reliable cross-domain authentication without blocking the Directory Server.

IdM clients cannot receive information about users and groups from Active Directory (AD) directly. Instead, IdM servers use the `ipa-extdom`{.literal} plugin to retrieve information about AD users and groups from SSSD, then forward that information to the requesting client.

The `ipa-extdom`{.literal} plugin sends a request to SSSD for AD user data. If the information is not in the SSSD cache, SSSD requests the data from an AD domain controller (DC). The config timeout value defines how long the `ipa-extdom`{.literal} plugin waits for a reply from SSSD before canceling the connection and returning a timeout error to the caller. The default value is 10000 milliseconds (10 seconds).

The following example adjusts the config timeout to 20 seconds (20000 milliseconds).

Warning

Exercise caution when adjusting the config timeout:

-   If you set a value that is too small, such as 500 milliseconds, SSSD might not have enough time to reply and requests will always return a timeout.
-   If you set a value that is too large, such as 30000 milliseconds (30 seconds), a single request might block the connection to SSSD for this amount of time. Because only one thread can connect to SSSD at a time, all other requests from the plug-in have to wait.
-   If there are many requests sent by IdM clients, they can block all available workers configured for the Directory Server on the IdM server. As a consequence, the server might not be able to reply to any kind of request for some time.

Only change the config timeout in the following situations:

-   If IdM clients frequently receive timeout errors before their own search timeout is reached when requesting information about AD users and groups, the config timeout value is **too small**.
-   If the Directory Server on the IdM server is often locked and the `pstack`{.literal} utility reports that many or all worker threads are handling `ipa-extdom`{.literal} requests at this time, the value is **too large**.

**Prerequisites**

-   The LDAP Directory Manager password

**Procedure**

-   Use the following command to adjust the config timeout to 20000 milliseconds:

    ``` {.language-plaintext tabindex="-1"}
    # ldapmodify -D "cn=Directory Manager" -W
    dn: cn=ipa_extdom_extop,cn=plugins,cn=config
    changetype: modify
    replace: ipaExtdomMaxNssTimeout
    ipaExtdomMaxNssTimeout: 20000
    ```

### [9.3. Tuning the maximum buffer size for the ipa-extdom plugin on IdM servers](#tuning-the-maximum-buffer-size-for-the-ipa-extdom-plugin-on-idm-servers) {#tuning-the-maximum-buffer-size-for-the-ipa-extdom-plugin-on-idm-servers .title}

You can increase the maximum buffer size for the `ipa-extdom`{.literal} plugin to reduce retry attempts when retrieving large amounts of Active Directory user and group data.

IdM clients cannot receive information about users and groups from Active Directory (AD) directly. Instead, IdM servers use the `ipa-extdom`{.literal} plugin to retrieve information about AD users and groups from SSSD, then forward that information to the requesting client.

You can tune the maximum buffer size for the `ipa-extdom`{.literal} plugin, which adjusts the size of the buffer where SSSD can store the data it receives. If the buffer is too small, SSSD returns an `ERANGE`{.literal} error and the plug-in retries the request with a larger buffer. The default buffer size is 134217728 bytes (128 MB).

The following example adjusts the maximum buffer size to 256 MB (268435456 bytes).

**Prerequisites**

-   The LDAP Directory Manager password

**Procedure**

-   Use the following command to set the maximum buffer size to 268435456 bytes:

    ``` {.language-plaintext tabindex="-1"}
    # ldapmodify -D "cn=Directory Manager" -W
    dn: cn=ipa_extdom_extop,cn=plugins,cn=config
    changetype: modify
    replace: ipaExtdomMaxNssBufSize
    ipaExtdomMaxNssBufSize: 268435456
    ```

### [9.4. Tuning the maximum number of instances for the ipa-extdom plugin on IdM servers](#tuning-the-maximum-number-of-instances-for-the-ipa-extdom-plugin-on-idm-servers) {#tuning-the-maximum-number-of-instances-for-the-ipa-extdom-plugin-on-idm-servers .title}

You can adjust the maximum number of `ipa-extdom`{.literal} plugin instances to prevent LDAP service bottlenecks when handling high volumes of Active Directory trust requests.

IdM clients cannot receive information about users and groups from Active Directory (AD) directly. Instead, IdM servers use the `ipa-extdom`{.literal} plugin to retrieve information about AD users and groups from SSSD, then forward that information to the requesting client.

By default, the `ipa-extdom`{.literal} plugin is configured to use up to 80% of the LDAP worker threads to handle requests from IdM clients. If the SSSD service on an IdM client has requested a large amount of information about AD trust users and groups, this operation can halt the LDAP service if it uses most of the LDAP threads. If you experience these issues, you might see similar errors in the SSSD log file for your AD domain, `/var/log/sssd/sssd__<your-ad-domain-name.com>_.log`{.literal}:

``` {.language-plaintext tabindex="-1"}
(2022-05-22  5:00:13): [be[ad.example.com]] [ipa_s2n_get_user_done] (0x0040): s2n exop request failed.
(2022-05-22  5:00:13): [be[ad.example.com]] [ipa_s2n_get_user_done] (0x0040): s2n exop request failed.
(2022-05-22  5:00:13): [be[ad.example.com]] [ipa_s2n_exop_done] (0x0040): ldap_extended_operation result: Server is busy(51), Too many extdom instances running.
```

You can adjust the maximum number of `ipa-extdom`{.literal} instances by setting the value for the `ipaExtdomMaxInstances`{.literal} option, which must be an integer larger than 0 and less than the total number of worker threads.

**Prerequisites**

-   The LDAP Directory Manager password

**Procedure**

1.  Retrieve the total number of worker threads:

    ``` {.language-plaintext tabindex="-1"}
    # ldapsearch -xLLLD cn=Directory\ Manager -W -b cn=config -s base nsslapd-threadnumber
    Enter LDAP Password:
    dn: cn=config
    nsslapd-threadnumber: 16
    ```

    This means that the current value for `ipaExtdomMaxInstances`{.literal} is 13.

2.  Adjust the maximum number of instances. This example changes the value to 14:

    ``` {.language-plaintext tabindex="-1"}
    # ldapmodify -D "cn=Directory Manager" -W
    dn: cn=ipa_extdom_extop,cn=plugins,cn=config
    changetype: modify
    replace: ipaExtdomMaxInstances
    ipaExtdomMaxInstances: 14
    ```

3.  Retrieve the current value of `ipaExtdomMaxInstances`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # ldapsearch -xLLLD "cn=Directory Manager" -W -b "cn=ipa_extdom_extop,cn=plugins,cn=config" |grep ipaextdommaxinstances
    Enter LDAP Password:

    ipaextdommaxinstances: 14
    ```

4.  Monitor the IdM Directory Server's performance and if it does not improve, repeat this procedure and adjust the value of the `ipaExtdomMaxInstances`{.literal} variable.

### [9.5. Tuning SSSD in IdM clients for large IdM-AD trust deployments](#tuning-sssd-in-idm-clients-for-large-idm-ad-trust-deployments) {#tuning-sssd-in-idm-clients-for-large-idm-ad-trust-deployments .title}

Apply tuning options to SSSD service configuration in an IdM client to improve its response time when retrieving information from a large AD environment.

**Prerequisites**

-   You need `root`{.literal} permissions to edit the `/etc/sssd/sssd.conf`{.literal} configuration file.

**Procedure**

1.  Determine the number of seconds a single un-cached login takes.

    a.  Clear the SSSD cache on the IdM client.

        ``` {.language-plaintext tabindex="-1"}
        [root@client_hostname ~]# sss_cache -E
        ```

    b.  Measure login time for an AD user using the `time`{.literal} command. From the IdM client, authenticate locally as an AD user by logging into the same host.

        ``` {.language-plaintext tabindex="-1"}
        [root@client_hostname ~]# time ssh <ad_username>@<ad_domain>@<client_fqdn>
        ```

    c.  Type in the password as soon as possible.

        ``` {.language-plaintext tabindex="-1"}
        Password:
        Last login: Sat Jan 23 06:29:54 2021 from 10.0.2.15
        [ad_username@ad_domain@client_fqdn ~]$
        ```

    d.  Log out as soon as possible to display elapsed time. In this example, a single un-cached login takes about `9`{.literal} seconds.

        ``` {.language-plaintext tabindex="-1"}
        [ad_username@ad_domain@client_fqdn /]$ exit
        logout
        Connection to client.example.com closed.

        real 0m8.755s
        user    0m0.017s
        sys     0m0.013s
        ```

2.  Open the `/etc/sssd/sssd.conf`{.literal} configuration file in a text editor.

3.  Add the following options to the `[domain]`{.literal} section for your Active Directory domain. Set the `pam_id_timeout`{.literal} and `krb5_auth_timeout`{.literal} options to the number of seconds an un-cached login takes. If you do not already have a domain section for your AD domain, create one.

    ``` {.language-plaintext tabindex="-1"}
    [domain/<idm_domain>/<ad_domain>]
    krb5_auth_timeout = 9
    ldap_deref_threshold = 0
    ...
    ```

4.  Add the following option to the `[pam]`{.literal} section:

    ``` {.language-plaintext tabindex="-1"}
    [pam]
    pam_id_timeout = 9
    ```

5.  Save and close the `/etc/sssd/sssd.conf`{.literal} file on the server.

6.  Restart the SSSD service to load the configuration changes.

    ``` {.language-plaintext tabindex="-1"}
    [root@client_hostname ~]# systemctl restart sssd
    ```

**Additional resources**

-   [Options for tuning SSSD in IdM servers and clients for large IdM-AD trust deployments](#options-in-sssd-conf-for-tuning-idm-servers-and-clients-for-large-idm-ad-trust-deployments "9.7. Options in sssd.conf for tuning IdM servers and clients for large IdM-AD trust deployments")

### [9.6. Mounting the SSSD cache in tmpfs](#mounting-the-sssd-cache-in-tmpfs) {#mounting-the-sssd-cache-in-tmpfs .title}

You can mount the SSSD cache in RAM to improve performance by eliminating slow disk write operations for LDAP object caching.

The System Security Services Daemon (SSSD) constantly writes LDAP objects to its cache. These internal SSSD transactions write data to disk, which is much slower than reading and writing from Random-Access Memory (RAM).

To improve this performance, mount the SSSD cache in RAM.

Before you begin, consider the following:

-   Cached information does not persist after a reboot if the SSSD cache is in RAM.
-   It is safe to perform this change on IdM servers, as the SSSD instance on an IdM server cannot lose connectivity with the Directory Server on the same host.
-   If you perform this adjustment on an IdM client and it loses connectivity to IdM servers, users will not be able to authenticate after a reboot until you reestablish connectivity.

**Prerequisites**

-   You need `root`{.literal} permissions to edit the `/etc/fstab`{.literal} configuration file.

**Procedure**

1.  Create a `tmpfs`{.literal} temporary filesystem:

    a.  Confirm that the SSSD user owns the `config.ldb`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        # ls -al /var/lib/sss/db/config.ldb
        -rw-------. 1 sssd sssd 1286144 Jun  8 16:41 /var/lib/sss/db/config.ldb
        ```

    b.  Add the following entry to the `/etc/fstab`{.literal} file as a single line:

        ``` {.language-plaintext tabindex="-1"}
        tmpfs /var/lib/sss/db/ tmpfs size=300M,mode=0700,uid=sssd,gid=sssd,rootcontext=system_u:object_r:sssd_var_lib_t:s0 0 0
        ```

    This example creates a 300MB cache. Tune the `size`{.literal} parameter according to your IdM and AD directory size, estimating 100 MBs per 10,000 LDAP entries.

2.  Mount the new SSSD cache directory.

    ``` {.language-plaintext tabindex="-1"}
    [root@host ~]# mount /var/lib/sss/db/
    ```

3.  Restart SSSD to reflect this configuration change.

    ``` {.language-plaintext tabindex="-1"}
    [root@host ~]# systemctl restart sssd
    ```

### [9.7. Options in sssd.conf for tuning IdM servers and clients for large IdM-AD trust deployments](#options-in-sssd-conf-for-tuning-idm-servers-and-clients-for-large-idm-ad-trust-deployments) {#options-in-sssd.conf-for-tuning-idm-servers-and-clients-for-large-idm-ad-trust-deployments .title}

Optimize SSSD performance in large IdM-AD trust deployments to reduce authentication delays and improve user login times. Tuning specific SSSD options helps manage the overhead of complex group memberships and cross-domain lookups.

The following options in the `/etc/sssd/sssd.conf`{.literal} configuration file control SSSD performance for IdM servers and clients in large IdM-AD trust deployments.

**Tuning options for IdM servers**

ignore_group_members

:   Knowing which groups a user belongs to, as opposed to all the users that belong to a group, is important when authenticating and authorizing a user. When `ignore_group_members`{.literal} is set to `true`{.literal}, SSSD only retrieves information about the group objects themselves and not their members, providing a significant performance boost.

    Note

    The `id `{.literal}[`user@ad-domain.com`{.literal}](mailto:user@ad-domain.com) command still returns the correct list of groups, but `getent group `{.literal}[`ad-group@ad-domain.com`{.literal}](mailto:ad-group@ad-domain.com) returns an empty list.

    +:----------------------------------+:----------------------------------+
    | Default value                     | `false`{.literal}                 |
    +-----------------------------------+-----------------------------------+
    | Recommended value                 | `true`{.literal}                  |
    +-----------------------------------+-----------------------------------+

    Show more

    Note

    You should not set this option to `true`{.literal} when the deployment involves an IdM server with the compat tree.

subdomain_inherit

:   With the `subdomain_inherit`{.literal} option, you can apply the `ignore_group_members`{.literal} setting to the trusted AD domains\' configuration. Settings listed in the `subdomain_inherit`{.literal} options apply to both the main (IdM) domain as well as the AD subdomain.

    +:----------------------------------+:-----------------------------------------------------+
    | Default value                     | `none`{.literal}                                     |
    +-----------------------------------+------------------------------------------------------+
    | Recommended value                 | `subdomain_inherit = ignore_group_members`{.literal} |
    +-----------------------------------+------------------------------------------------------+

    Show more

**Tuning options for IdM clients**

pam_id_timeout

:   This parameter controls how long results from a PAM session are cached, to avoid excessive round-trips to the identity provider during an identity lookup. The default value of `5`{.literal} seconds might not be enough in environments where complex group memberships are populated on the IdM Server and IdM client side. Red Hat recommends setting `pam_id_timeout`{.literal} to the number of seconds a single un-cached login takes.

    +:----------------------------------+:-----------------------------------------------------------------+
    | Default value                     | `5`{.literal}                                                    |
    +-----------------------------------+------------------------------------------------------------------+
    | Recommended value                 | `the number of seconds a single un-cached login takes`{.literal} |
    +-----------------------------------+------------------------------------------------------------------+

    Show more

krb5_auth_timeout

:   Increasing `krb5_auth_timeout`{.literal} allows more time to process complex group information in environments where users are members of a large number of groups. Red Hat recommends setting this value to the number of seconds a single un-cached login takes.

    +:----------------------------------+:-----------------------------------------------------------------+
    | Default value                     | `6`{.literal}                                                    |
    +-----------------------------------+------------------------------------------------------------------+
    | Recommended value                 | `the number of seconds a single un-cached login takes`{.literal} |
    +-----------------------------------+------------------------------------------------------------------+

    Show more

ldap_deref_threshold

:   A dereference lookup is a means of fetching all group members in a single LDAP call. The `ldap_deref_threshold`{.literal} value specifies the number of group members that must be missing from the internal cache to trigger a dereference lookup. If less members are missing, they are looked up individually. Dereference lookups may take a long time in large environments and decrease performance. To disable dereference lookups, set this option to `0`{.literal}.

    +:----------------------------------+:----------------------------------+
    | Default value                     | `10`{.literal}                    |
    +-----------------------------------+-----------------------------------+
    | Recommended value                 | `0`{.literal}                     |
    +-----------------------------------+-----------------------------------+

    Show more

### [9.8. Additional resources](#tuning-sssd-performance-for-large-idm-ad-trust-deployments_98-additional-resources) {#additional-resources-3 .title}

-   [Performance tuning SSSD for large IdM-AD trust deployments](https://access.redhat.com/articles/2133801)

## [Chapter 10. Tuning the WSGI processes](#tuning-the-wsgi-processes) {#chapter-10.-tuning-the-wsgi-processes .title}

If you are seeing request failures due to long-running API processes, tuning the number of Web Server Gateway Interface (WSGI) processes can improve performance and allow more concurrent requests.

By default, IdM allocates 4 WSGI processes for the API service on 64-bit systems. This default limitation is implemented for memory conservation purposes. Any of the longer-running API endpoints can benefit from tuning, particularly in environments with high-volume automated operations.

For example, an OpenStack installation consists of several controllers containing multiple services. Each service requests a certificate so that all internal communication occurs over Transport Layer Security (TLS). When installing or refreshing multiple controllers or compute nodes simultaneously, the volume of certificate requests can become considerable. In such scenarios, increasing the number of WSGI processes allows the installation to complete successfully.

### [10.1. Adjusting the WSGI process count](#adjusting-the-wsgi-process-count) {#adjusting-the-wsgi-process-count .title}

Adjust the number of Web Server Gateway Interface (WSGI) processes to handle more concurrent API requests in your IdM environment. Increasing WSGI processes improves performance for high-volume operations like certificate issuance, at the cost of increased memory consumption.

**Prerequisites**

-   You have `root`{.literal} access to the IdM server.

**Procedure**

1.  Open the `/etc/httpd/conf.d/ipa.conf`{.literal} file and modify the `processes`{.literal} value in the `WSGIDaemonProcess`{.literal} directive:

    ``` {.language-plaintext tabindex="-1"}
    WSGIDaemonProcess ipa processes=<value> threads=1 maximum-requests=500 \
    ```

    By default, IdM uses 4 processes. You can increase this to handle more concurrent requests. The recommended maximum is 16 processes.

    Note

    Each WSGI process consumes approximately 100-110 MB of resident memory. With 16 processes, total memory consumption is approximately 1.3 GB.

2.  Restart the Apache HTTP server to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# systemctl restart httpd
    ```

### [10.2. Optimizing CPU usage for improved IPA server performance](#optimizing-cpu-usage-for-improved-ipa-server-performance) {#optimizing-cpu-usage-for-improved-ipa-server-performance .title}

When encountering performance limitations during high-volume certificate issuance tasks, tuning the CPU and Web Server Gateway Interface (WSGI) process counts can significantly enhance an IPA server's capability to handle simultaneous requests.

With a server configured with 4 CPUs and 70 clients requesting 7 certificates each (490 certificates in total), server timeouts occurred as the request volume exceeded the server's processing capacity.

Increasing the CPU count to 8 and matching the WSGI process count to 8 raised the certificate handling capacity to 630 certificates, a 28% increase over the 4 CPU configuration, despite a 100% increase in CPU count. Further increasing the CPU count to 16 showed no additional performance gains with only 8 WSGI processes. However, by increasing the WSGI process count to 16, the server processed 770 certificates with 110 clients, reflecting a 22% improvement over the 8 CPU setup.

On average, doubling the number of CPUs resulted in a 25% increase in certificate issuance capacity, as long as the WSGI processes were tuned accordingly. This emphasizes the need to scale both CPU and WSGI processes together to prevent bottlenecks and optimize server performance.

## [Legal Notice](#idm140462320989536) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
