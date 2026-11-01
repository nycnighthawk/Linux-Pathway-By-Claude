---
{"title": "Performing disaster recovery with Identity Management", "guide": "performing_disaster_recovery_with_identity_management", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/performing_disaster_recovery_with_identity_management/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Performing disaster recovery with Identity Management {#performing-disaster-recovery-with-identity-management .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Recovering IdM after a server or data loss {#recovering-idm-after-a-server-or-data-loss .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140624662858304)

**Abstract**

Hardware malfunctions and site outages require a rapid, precise response to restore Identity Management (IdM) services. Identify the specific failure type and evaluate your IdM topology to determine the most effective recovery path.

Use replication to replace lost servers, or apply virtual machine (VM) snapshots and IdM backups to restore corrupted data. After restoration, update client settings for DNS and Kerberos to ensure full connectivity and service functionality across your environment.

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

## [Chapter 1. Disaster scenarios in IdM](#disaster-scenarios-in-idm) {#chapter-1.-disaster-scenarios-in-idm .title}

Prepare and respond to various disaster scenarios in Identity Management (IdM) systems that affect servers, data, or entire infrastructures. Identifying specific disaster scenarios and their impact on domain operations helps determine the appropriate recovery strategy.

+------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Disaster type                                                                                                                                  | Example causes                                                                            | How to prepare                                                                                                                                                                                                                  | How to respond                                                                                                                                                                                                                 |
+:===============================================================================================================================================+:==========================================================================================+:================================================================================================================================================================================================================================+:===============================================================================================================================================================================================================================+
| **Server loss**: The IdM deployment loses one or several servers.                                                                              | -   Hardware malfunction                                                                  | -   [Preparing for server loss with replication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/preparing_for_disaster_recovery_with_identity_management/preparing-for-server-loss-with-replication) | -   [Recovering a single server with replication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/performing_disaster_recovery_with_identity_management/recovering-a-single-server-with-replication) |
+------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Data loss**: IdM data is unexpectedly modified on a server, and the change is propagated to other servers.                                   | -   A user accidentally deletes data                                                      | -   [Preparing for data loss with VM snapshots](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/preparing_for_disaster_recovery_with_identity_management/preparing-for-data-loss-with-vm-snapshots)   | -   [Recovering from data loss with VM snapshots](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/performing_disaster_recovery_with_identity_management/recovering-from-data-loss-with-vm-snapshots) |
|                                                                                                                                                | -   A software bug modifies data                                                          | -   [Planning for data recovery with IdM backups](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/preparing_for_disaster_recovery_with_identity_management/preparing-for-data-loss-with-idm-backups)  | -   [Recovering from data loss with IdM backups](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/performing_disaster_recovery_with_identity_management/recovering-from-data-loss-with-idm-backups)   |
|                                                                                                                                                |                                                                                           |                                                                                                                                                                                                                                 | -   [Managing data loss](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/performing_disaster_recovery_with_identity_management/managing-data-loss)                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Total infrastructure loss**: All IdM servers or Certificate Authority (CA) replicas are lost with no VM snapshots or data backups available. | -   Lack of off-site backups or redundancy prevents recovery after a failure or disaster. | -   [Preparing for data loss with VM snapshots](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/preparing_for_disaster_recovery_with_identity_management/preparing-for-data-loss-with-vm-snapshots)   | This situation is a total loss.                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 1.1. Disaster scenarios in IdM

Show more

Warning

A total loss scenario occurs when all Certificate Authority (CA) replicas or all IdM servers are lost, and no virtual machine (VM) snapshots or backups are available for recovery. Without CA replicas, the IdM environment cannot deploy additional replicas or rebuild itself, making recovery impossible. To avoid such scenarios, ensure backups are stored off-site, maintain multiple geographically redundant CA replicas, and connect each replica to at least two others.

## [Chapter 2. Recovering a single server with replication](#recovering-a-single-server-with-replication) {#chapter-2.-recovering-a-single-server-with-replication .title}

Recover an Identity Management (IdM) server after a failure by reinstallation from a functional replica. Use your existing replication topology to return the failed server to a functional state, ensure data consistency, and maintain high availability across your environment.

If your IdM topology contains an integrated Certificate Authority (CA), the steps for removing and replacing a damaged replica differ for the CA renewal server and other replicas.

### [2.1. Recovering from losing the CA renewal server](#recovering-from-losing-the-ca-renewal-server) {#recovering-from-losing-the-ca-renewal-server .title}

If the Certificate Authority (CA) renewal server is lost, you must first promote another CA replica to fulfill the CA renewal server role, and then deploy a replacement CA replica.

**Prerequisites**

-   Your deployment uses IdM's internal Certificate Authority (CA).
-   Another Replica in the environment has CA services installed.

Warning

An IdM deployment is unrecoverable if:

1.  The CA renewal server has been lost.

2.  No other server has a CA installed.

3.  No backup of a replica with the CA role exists.

    It is critical to make backups from a replica with the CA role so certificate data is protected. For more information about creating and restoring from backups, see [Preparing for data loss with IdM backups](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/preparing_for_disaster_recovery_with_identity_management/preparing-for-data-loss-with-idm-backups).

**Procedure**

1.  From another replica in your environment, promote another CA replica in the environment to act as the new CA renewal server. See [Changing and resetting IdM CA renewal server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_certificates_in_idm/using-idm-ca-renewal-server#changing-and-resetting-idm-ca-renewal-server).
2.  From another replica in your environment, remove replication agreements to the lost CA renewal server. See [Removing server from topology using the CLI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_replication_in_identity_management/managing-replication-topology#managing-topology-remove-cli).
3.  Install a new CA Replica to replace the lost CA replica. See [Installing an IdM replica with a CA](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-idm-replica).
4.  Update DNS to reflect changes in the replica topology. If IdM DNS is used, DNS service records are updated automatically.
5.  Verify IdM clients can reach IdM servers. See [Adjusting IdM clients during recovery](#adjusting-idm-clients-during-recovery "Chapter 8. Adjusting IdM clients during recovery").

**Verification**

1.  Test the Kerberos server on the new replica by successfully retrieving a Kerberos Ticket-Granting-Ticket as an IdM user.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# kinit admin
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password for admin@EXAMPLE.COM:
    ```

2.  Verify the cached ticket by listing the active credentials.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# klist
    ```

    ``` {.language-plaintext tabindex="-1"}
    Ticket cache: KCM:0
    Default principal: admin@EXAMPLE.COM

    Valid starting       Expires              Service principal
    10/31/2019 15:51:37  11/01/2019 15:51:02  HTTP/server.example.com@EXAMPLE.COM
    10/31/2019 15:51:08  11/01/2019 15:51:02  krbtgt/EXAMPLE.COM@EXAMPLE.COM
    ```

3.  Test the Directory Server and SSSD configuration by retrieving user information.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa user-show admin
    ```

    ``` {.language-plaintext tabindex="-1"}
      User login: admin
      Last name: Administrator
      Home directory: /home/admin
      Login shell: /bin/bash
      Principal alias: admin@EXAMPLE.COM
      UID: 1965200000
      GID: 1965200000
      Account disabled: False
      Password: True
      Member of groups: admins, trust admins
      Kerberos keys available: True
    ```

4.  Test the CA configuration with the `ipa cert-show`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa cert-show 1
    ```

    ``` {.language-plaintext tabindex="-1"}
      Issuing CA: ipa
      Certificate: MIIEgjCCAuqgAwIBAgIjoSIP...
      Subject: CN=Certificate Authority,O=EXAMPLE.COM
      Issuer: CN=Certificate Authority,O=EXAMPLE.COM
      Not Before: Thu Oct 31 19:43:29 2019 UTC
      Not After: Mon Oct 31 19:43:29 2039 UTC
      Serial number: 1
      Serial number (hex): 0x1
      Revoked: False
    ```

**Additional resources**

-   [Using IdM CA renewal server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_certificates_in_idm/using-idm-ca-renewal-server)

### [2.2. Recovering from losing a regular replica](#recovering-from-losing-a-regular-replica) {#recovering-from-losing-a-regular-replica .title}

To replace a replica that is not the Certificate Authority (CA) renewal server, remove the lost replica from the topology and install a new replica in its place.

**Prerequisites**

-   The CA renewal server is operating properly. If the CA renewal server has been lost, see [Recovering from losing the CA renewal server](#recovering-from-losing-the-ca-renewal-server "2.1. Recovering from losing the CA renewal server").

**Procedure**

1.  Remove replication agreements to the lost server. See [Uninstalling an IdM server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/uninstalling-an-idm-server).
2.  Deploy a new replica with the corresponding services (CA, KRA, DNS). See [Installing an IdM replica](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-idm-replica).
3.  Update DNS to reflect changes in the replica topology. If IdM DNS is used, DNS service records are updated automatically.
4.  Verify IdM clients can reach IdM servers. See [Adjusting IdM clients during recovery](#adjusting-idm-clients-during-recovery "Chapter 8. Adjusting IdM clients during recovery").

**Verification**

1.  Test the Kerberos server on the new replica by successfully retrieving a Kerberos Ticket-Granting-Ticket as an IdM user.

    ``` {.language-plaintext tabindex="-1"}
    [root@newreplica ~]# kinit admin
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password for admin@EXAMPLE.COM:
    ```

2.  Verify the cached ticket by listing the active credentials.

    ``` {.language-plaintext tabindex="-1"}
    [root@newreplica ~]# klist
    ```

    ``` {.language-plaintext tabindex="-1"}
    Ticket cache: KCM:0
    Default principal: admin@EXAMPLE.COM

    Valid starting       Expires              Service principal
    10/31/2019 15:51:37  11/01/2019 15:51:02  HTTP/server.example.com@EXAMPLE.COM
    10/31/2019 15:51:08  11/01/2019 15:51:02  krbtgt/EXAMPLE.COM@EXAMPLE.COM
    ```

3.  Test the Directory Server and SSSD configuration on the new replica by retrieving user information.

    ``` {.language-plaintext tabindex="-1"}
    [root@newreplica ~]# ipa user-show admin
    ```

    ``` {.language-plaintext tabindex="-1"}
      User login: admin
      Last name: Administrator
      Home directory: /home/admin
      Login shell: /bin/bash
      Principal alias: admin@EXAMPLE.COM
      UID: 1965200000
      GID: 1965200000
      Account disabled: False
      Password: True
      Member of groups: admins, trust admins
      Kerberos keys available: True
    ```

## [Chapter 3. Recovering multiple servers with replication](#recovering-multiple-servers-with-replication) {#chapter-3.-recovering-multiple-servers-with-replication .title}

Restore an Identity Management (IdM) environment after a simultaneous loss of multiple replicas. Identify the correct recovery path based on your CA configuration and the operational status of the renewal server.

### [3.1. Recovering from losing multiple servers in a CA-less deployment](#recovering-from-losing-multiple-servers-in-a-ca-less-deployment) {#recovering-from-losing-multiple-servers-in-a-ca-less-deployment .title}

Rebuild an Identity Management (IdM) environment where all servers are considered equal due to the use of an external Certificate Authority (CA). In this scenario, you can rebuild the environment by removing and replacing lost replicas in any order.

**Prerequisites**

-   Your deployment uses an external Certificate Authority (CA).

**Procedure**

-   See [Recovering from losing a regular replica](#recovering-from-losing-a-regular-replica "2.2. Recovering from losing a regular replica").

### [3.2. Recovering from losing multiple servers when the CA renewal server is unharmed](#recovering-from-losing-multiple-servers-when-the-ca-renewal-server-is-unharmed) {#recovering-from-losing-multiple-servers-when-the-ca-renewal-server-is-unharmed .title}

Restore an Identity Management (IdM) environment where the CA renewal server is intact. Because the critical CA renewal server remains operational, you can recover the lost replicas by replacing them in any order.

**Prerequisites**

-   Your deployment uses the IdM internal Certificate Authority (CA).

**Procedure**

-   See [Recovering from losing a regular replica](#recovering-from-losing-a-regular-replica "2.2. Recovering from losing a regular replica").

### [3.3. Recovering from losing the CA renewal server and other servers](#recovering-from-losing-the-ca-renewal-server-and-other-servers) {#recovering-from-losing-the-ca-renewal-server-and-other-servers .title}

Restore an Identity Management (IdM) environment when the server holding the CA renewal role is lost along with other replicas. In this scenario, you must first promote a functional CA server to the renewal role before rebuilding the rest of the environment.

**Prerequisites**

-   Your deployment uses the IdM internal Certificate Authority (CA).
-   At least one CA replica is unharmed.

**Procedure**

1.  Promote another CA replica to fulfill the CA renewal server role. See [Recovering from losing the CA renewal server](#recovering-from-losing-the-ca-renewal-server "2.1. Recovering from losing the CA renewal server").
2.  Replace all other lost replicas. See [Recovering from losing a regular replica](#recovering-from-losing-a-regular-replica "2.2. Recovering from losing a regular replica").

## [Chapter 4. Recovering from data loss with VM snapshots](#recovering-from-data-loss-with-vm-snapshots) {#chapter-4.-recovering-from-data-loss-with-vm-snapshots .title}

Restore an Identity Management (IdM) environment by deploying a Virtual Machine (VM) snapshot of a server that includes the Certificate Authority (CA) role. You can use a snapshot to recover from data corruption by re-integrating a restored server into your current topology or by rebuilding a new environment from a single point-in-time image.

### [4.1. Recovering from only a VM snapshot](#recovering-from-only-a-vm-snapshot) {#recovering-from-only-a-vm-snapshot .title}

Recreate your Identity Management (IdM) deployment when all servers are lost and only a single Virtual Machine (VM) snapshot of a Certificate Authority (CA) replica remains. You can recreate your environment by booting the snapshot, removing references to the failed servers, and installing new replicas.

**Prerequisites**

-   You have prepared a VM snapshot of a CA replica VM. See [Preparing for data loss with VM snapshots](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/preparing_for_disaster_recovery_with_identity_management/preparing-for-data-loss-with-vm-snapshots).

**Procedure**

1.  Boot the desired snapshot of the CA replica VM.

2.  Remove replication agreements to any lost replicas.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa server-del lost-server1.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa server-del lost-server2.example.com
    ...
    ```

3.  Install a second CA replica. See [Installing an IdM replica](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-idm-replica).

4.  The VM CA replica is now the CA renewal server. Red Hat recommends promoting another CA replica in the environment to act as the CA renewal server. See [Changing and resetting IdM CA renewal server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_certificates_in_idm/using-idm-ca-renewal-server#changing-and-resetting-idm-ca-renewal-server).

5.  Recreate the desired replica topology by deploying additional replicas with the desired services (CA, DNS). See [Installing an IdM replica](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-idm-replica)

6.  Update DNS to reflect the new replica topology. If IdM DNS is used, DNS service records are updated automatically.

7.  Verify that IdM clients can reach the IdM servers. See [Adjusting IdM Clients during recovery](#adjusting-idm-clients-during-recovery "Chapter 8. Adjusting IdM clients during recovery").

**Verification**

1.  Test the Kerberos server on every replica by successfully retrieving a Kerberos ticket-granting ticket as an IdM user.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# kinit admin
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password for admin@EXAMPLE.COM:
    ```

2.  Verify the cached ticket by listing the active credentials.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# klist
    ```

    ``` {.language-plaintext tabindex="-1"}
    Ticket cache: KCM:0
    Default principal: admin@EXAMPLE.COM

    Valid starting       Expires              Service principal
    10/31/2019 15:51:37  11/01/2019 15:51:02  HTTP/server.example.com@EXAMPLE.COM
    10/31/2019 15:51:08  11/01/2019 15:51:02  krbtgt/EXAMPLE.COM@EXAMPLE.COM
    ```

3.  Test the Directory Server and SSSD configuration on every replica by retrieving user information.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa user-show admin
    ```

    ``` {.language-plaintext tabindex="-1"}
      User login: admin
      Last name: Administrator
      Home directory: /home/admin
      Login shell: /bin/bash
      Principal alias: admin@EXAMPLE.COM
      UID: 1965200000
      GID: 1965200000
      Account disabled: False
      Password: True
      Member of groups: admins, trust admins
      Kerberos keys available: True
    ```

4.  Test the CA server on every CA replica with the `ipa cert-show`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa cert-show 1
    ```

    ``` {.language-plaintext tabindex="-1"}
      Issuing CA: ipa
      Certificate: MIIEgjCCAuqgAwIBAgIjoSIP...
      Subject: CN=Certificate Authority,O=EXAMPLE.COM
      Issuer: CN=Certificate Authority,O=EXAMPLE.COM
      Not Before: Thu Oct 31 19:43:29 2019 UTC
      Not After: Mon Oct 31 19:43:29 2039 UTC
      Serial number: 1
      Serial number (hex): 0x1
      Revoked: False
    ```

**Additional resources**

-   [Planning the replica topology](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/planning-the-replica-topology)

### [4.2. Recovering from a VM snapshot among a partially-working environment](#recovering-from-a-vm-snapshot-among-a-partially-working-environment) {#recovering-from-a-vm-snapshot-among-a-partially-working-environment .title}

Restore a specific state of your Identity Management (IdM) deployment when a disaster affects some IdM servers while others are still operating properly. You can bring a Certificate Authority (CA) replica back into the environment from a snapshot, re-synchronize it with the remaining servers, and deploy new replicas to return to full capacity.

**Prerequisites**

-   You have prepared a VM snapshot of a CA replica VM. See [Preparing for data loss with VM snapshots](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/preparing_for_disaster_recovery_with_identity_management/index#preparing-for-data-loss-with-vm-snapshots).

**Procedure**

1.  Remove all replication agreements to the lost servers. See [Uninstalling an IdM server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/uninstalling-an-idm-server).

2.  Boot the desired snapshot of the CA replica VM.

3.  Remove any replication agreements between the restored server and any lost servers.

    ``` {.language-plaintext tabindex="-1"}
    [root@restored-CA-replica ~]# ipa server-del lost-server1.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@restored-CA-replica ~]# ipa server-del lost-server2.example.com
    ...
    ```

4.  If the restored server does not have replication agreements to any of the servers still in production, connect the restored server with one of the other servers to update the restored server.

    ``` {.language-plaintext tabindex="-1"}
    [root@restored-CA-replica ~]# ipa topologysegment-add
    ```

    ``` {.language-plaintext tabindex="-1"}
    Suffix name: domain
    Left node: restored-CA-replica.example.com
    Right node: server3.example.com
    Segment name [restored-CA-replica.com-to-server3.example.com]: new_segment
    ---------------------------
    Added segment "new_segment"
    ---------------------------
      Segment name: new_segment
      Left node: restored-CA-replica.example.com
      Right node: server3.example.com
      Connectivity: both
    ```

5.  Review Directory Server error logs at `/var/log/dirsrv/slapd-YOUR-INSTANCE/errors`{.literal} to see if the CA replica from the snapshot correctly synchronizes with the remaining IdM servers.

6.  If replication on the restored server fails because its database is too outdated, reinitialize the restored server.

    ``` {.language-plaintext tabindex="-1"}
    [root@restored-CA-replica ~]# ipa-replica-manage re-initialize --from server2.example.com
    ```

7.  If the database on the restored server is correctly synchronized, continue by deploying additional replicas with the desired services (CA, DNS) according to [Installing an IdM replica](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-idm-replica).

**Verification**

1.  Test the Kerberos server on every replica by successfully retrieving a Kerberos ticket-granting ticket as an IdM user.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# kinit admin
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password for admin@EXAMPLE.COM:
    ```

2.  Verify the cached ticket by listing the active credentials.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# klist
    ```

    ``` {.language-plaintext tabindex="-1"}
    Ticket cache: KCM:0
    Default principal: admin@EXAMPLE.COM

    Valid starting       Expires              Service principal
    10/31/2019 15:51:37  11/01/2019 15:51:02  HTTP/server.example.com@EXAMPLE.COM
    10/31/2019 15:51:08  11/01/2019 15:51:02  krbtgt/EXAMPLE.COM@EXAMPLE.COM
    ```

3.  Test the Directory Server and SSSD configuration on every replica by retrieving user information.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa user-show admin
    ```

    ``` {.language-plaintext tabindex="-1"}
      User login: admin
      Last name: Administrator
      Home directory: /home/admin
      Login shell: /bin/bash
      Principal alias: admin@EXAMPLE.COM
      UID: 1965200000
      GID: 1965200000
      Account disabled: False
      Password: True
      Member of groups: admins, trust admins
      Kerberos keys available: True
    ```

4.  Test the CA server on every CA replica with the `ipa cert-show`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa cert-show 1
    ```

    ``` {.language-plaintext tabindex="-1"}
      Issuing CA: ipa
      Certificate: MIIEgjCCAuqgAwIBAgIjoSIP...
      Subject: CN=Certificate Authority,O=EXAMPLE.COM
      Issuer: CN=Certificate Authority,O=EXAMPLE.COM
      Not Before: Thu Oct 31 19:43:29 2019 UTC
      Not After: Mon Oct 31 19:43:29 2039 UTC
      Serial number: 1
      Serial number (hex): 0x1
      Revoked: False
    ```

**Additional resources**

-   [Recovering from a VM snapshot to establish a new IdM environment](#recovering-from-a-vm-snapshot-to-establish-a-new-idm-environment "4.3. Recovering from a VM snapshot to establish a new IdM environment")

### [4.3. Recovering from a VM snapshot to establish a new IdM environment](#recovering-from-a-vm-snapshot-to-establish-a-new-idm-environment) {#recovering-from-a-vm-snapshot-to-establish-a-new-idm-environment .title}

If the Certificate Authority (CA) replica from a restored Virtual Machine (VM) snapshot is unable to replicate with other servers, create a new IdM environment from the VM snapshot.

To establish a new IdM environment, isolate the VM server, create additional replicas from it, and switch IdM clients to the new environment.

**Prerequisites**

-   You have prepared a VM snapshot of a CA replica VM. See [Preparing for data loss with VM snapshots](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/preparing_for_disaster_recovery_with_identity_management/preparing-for-data-loss-with-vm-snapshots).

**Procedure**

1.  Boot the desired snapshot of the CA replica VM.

2.  Isolate the restored server from the rest of the current deployment by removing all of its replication topology segments.

    a.  First, display all `domain`{.literal} replication topology segments.

        ``` {.language-plaintext tabindex="-1"}
        [root@restored-CA-replica ~]# ipa topologysegment-find
        ```

        ``` {.language-plaintext tabindex="-1"}
        Suffix name: domain
        ------------------
        8 segments matched
        ------------------
          Segment name: new_segment
          Left node: restored-CA-replica.example.com
          Right node: server2.example.com
          Connectivity: both

        ...
        ----------------------------
        Number of entries returned 8
        ----------------------------
        ```

    b.  Delete all `domain`{.literal} topology segments that involve the restored server.

        ``` {.language-plaintext tabindex="-1"}
        [root@restored-CA-replica ~]# ipa topologysegment-del
        ```

        ``` {.language-plaintext tabindex="-1"}
        Suffix name: domain
        Segment name: new_segment
        -----------------------------
        Deleted segment "new_segment"
        -----------------------------
        ```

    c.  Identify the `ca`{.literal} topology segments that involve the restored server.

        ``` {.language-plaintext tabindex="-1"}
        [root@restored-CA-replica ~]# ipa topologysegment-find
        ```

        ``` {.language-plaintext tabindex="-1"}
        Suffix name: ca
        ------------------
        1 segments matched
        ------------------
          Segment name: ca_segment
          Left node: restored-CA-replica.example.com
          Right node: server4.example.com
          Connectivity: both
        ----------------------------
        Number of entries returned 1
        ----------------------------
        ```

    d.  Delete all `ca`{.literal} topology segments that involve the restored server.

        ``` {.language-plaintext tabindex="-1"}
        [root@restored-CA-replica ~]# ipa topologysegment-del
        ```

        ``` {.language-plaintext tabindex="-1"}
        Suffix name: ca
        Segment name: ca_segment
        -----------------------------
        Deleted segment "ca_segment"
        -----------------------------
        ```

3.  Install a sufficient number of IdM replicas from the restored server to handle the deployment load. There are now two disconnected IdM deployments running in parallel.

4.  Switch the IdM clients to use the new deployment by hard-coding references to the new IdM replicas. See [Adjusting IdM clients during recovery](#adjusting-idm-clients-during-recovery "Chapter 8. Adjusting IdM clients during recovery").

5.  Stop and uninstall IdM servers from the previous deployment. See [Uninstalling an IdM server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/uninstalling-an-idm-server).

**Verification**

1.  Test the Kerberos server on every new replica by successfully retrieving a Kerberos ticket-granting ticket as an IdM user.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# kinit admin
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password for admin@EXAMPLE.COM:
    ```

2.  Verify the cached ticket by listing the active credentials.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# klist
    ```

    ``` {.language-plaintext tabindex="-1"}
    Ticket cache: KCM:0
    Default principal: admin@EXAMPLE.COM

    Valid starting       Expires              Service principal
    10/31/2019 15:51:37  11/01/2019 15:51:02  HTTP/server.example.com@EXAMPLE.COM
    10/31/2019 15:51:08  11/01/2019 15:51:02  krbtgt/EXAMPLE.COM@EXAMPLE.COM
    ```

3.  Test the Directory Server and SSSD configuration on every new replica by retrieving user information.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa user-show admin
    ```

    ``` {.language-plaintext tabindex="-1"}
      User login: admin
      Last name: Administrator
      Home directory: /home/admin
      Login shell: /bin/bash
      Principal alias: admin@EXAMPLE.COM
      UID: 1965200000
      GID: 1965200000
      Account disabled: False
      Password: True
      Member of groups: admins, trust admins
      Kerberos keys available: True
    ```

4.  Test the CA server on every new CA replica with the `ipa cert-show`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa cert-show 1
    ```

    ``` {.language-plaintext tabindex="-1"}
      Issuing CA: ipa
      Certificate: MIIEgjCCAuqgAwIBAgIjoSIP...
      Subject: CN=Certificate Authority,O=EXAMPLE.COM
      Issuer: CN=Certificate Authority,O=EXAMPLE.COM
      Not Before: Thu Oct 31 19:43:29 2019 UTC
      Not After: Mon Oct 31 19:43:29 2039 UTC
      Serial number: 1
      Serial number (hex): 0x1
      Revoked: False
    ```

## [Chapter 5. Recovering from data loss with IdM backups](#recovering-from-data-loss-with-idm-backups) {#chapter-5.-recovering-from-data-loss-with-idm-backups .title}

Restore an Identity Management (IdM) server or its LDAP data to a previous state using the `ipa-restore utility`{.literal}.

### [5.1. Restoring an IdM server from a backup](#restoring-an-idm-server-from-a-backup) {#restoring-an-idm-server-from-a-backup .title}

Using the `ipa-restore`{.literal} utility, you can restore your IdM server or the LDAP content to the state they were in when the backup was created.

**Figure 5.1. Replication topology used in this example**

This example restoration scenario involves the following three servers:

-   `server1.example.com`{.literal}: The server that you want to restore from backup.
-   `caReplica2.example.com`{.literal}: A Certificate Authority (CA) replica connected to the `server1.example.com`{.literal} host.
-   `replica3.example.com`{.literal}: A replica connected to the `caReplica2.example.com`{.literal} host.

**Prerequisites**

-   You have generated a full-server or data-only backup of the IdM server with the `ipa-backup`{.literal} utility. See [Creating a backup](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/preparing_for_disaster_recovery_with_identity_management/backing-up-and-restoring-idm#creating-an-idm-backup).
-   Your backup files are not in the `/tmp`{.literal} or `/var/tmp`{.literal} directories.
-   Before performing a full-server restore from a full-server backup, [uninstall](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/uninstalling-an-idm-server) IdM from the server and [reinstall](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/preparing-the-system-for-idm-server-installation) IdM using the same server configuration as before.

**Procedure**

1.  Use the `ipa-restore`{.literal} utility to restore a full-server or data-only backup.

    -   If the backup directory is in the default `/var/lib/ipa/backup/`{.literal} location, enter only the name of the directory:

        ``` {.language-plaintext tabindex="-1"}
        [root@server1 ~]# ipa-restore ipa-full-2020-01-14-12-02-32
        ```

    -   If the backup directory is not in the default location, enter its full path:

        ``` {.language-plaintext tabindex="-1"}
        [root@server1 ~]# ipa-restore /mybackups/ipa-data-2020-02-01-05-30-00
        ```

        Note

        The `ipa-restore`{.literal} utility automatically detects the type of backup that the directory contains, and performs the same type of restore by default. To perform a data-only restore from a full-server backup, add the `--data`{.literal} option to the `ipa-restore`{.literal} command:

        ``` {.language-plaintext tabindex="-1"}
        [root@server1 ~]# ipa-restore --data ipa-full-2020-01-14-12-02-32
        ```

2.  Enter the Directory Manager password.

    ``` {.language-plaintext tabindex="-1"}
    Directory Manager (existing master) password:
    ```

3.  Enter `yes`{.literal} to confirm overwriting current data with the backup.

    ``` {.language-plaintext tabindex="-1"}
    Preparing restore from /var/lib/ipa/backup/ipa-full-2020-01-14-12-02-32 on server1.example.com
    Performing FULL restore from FULL backup
    Temporary setting umask to 022
    Restoring data will overwrite existing live data. Continue to restore? [no]: yes
    ```

4.  The `ipa-restore`{.literal} utility disables replication on all servers that are available:

    ``` {.language-plaintext tabindex="-1"}
    Each master will individually need to be re-initialized or
    re-created from this one. The replication agreements on
    masters running IPA 3.1 or earlier will need to be manually
    re-enabled. See the man page for details.
    Disabling all replication.
    Disabling replication agreement on server1.example.com to caReplica2.example.com
    Disabling CA replication agreement on server1.example.com to caReplica2.example.com
    Disabling replication agreement on caReplica2.example.com to server1.example.com
    Disabling replication agreement on caReplica2.example.com to replica3.example.com
    Disabling CA replication agreement on caReplica2.example.com to server1.example.com
    Disabling replication agreement on replica3.example.com to caReplica2.example.com
    ```

    The utility then stops IdM services, restores the backup, and restarts the services:

    ``` {.language-plaintext tabindex="-1"}
    Stopping IPA services
    Systemwide CA database updated.
    Restoring files
    Systemwide CA database updated.
    Restoring from userRoot in EXAMPLE-COM
    Restoring from ipaca in EXAMPLE-COM
    Restarting GSS-proxy
    Starting IPA services
    Restarting SSSD
    Restarting oddjobd
    Restoring umask to 18
    The ipa-restore command was successful
    ```

5.  Re-initialize all replicas connected to the restored server:

    a.  List all replication topology segments for the `domain`{.literal} suffix, taking note of topology segments involving the restored server.

        ``` {.language-plaintext tabindex="-1"}
        [root@server1 ~]# ipa topologysegment-find domain
        ```

        ``` {.language-plaintext tabindex="-1"}
        ------------------
        2 segments matched
        ------------------
          Segment name: server1.example.com-to-caReplica2.example.com
          Left node: server1.example.com
          Right node: caReplica2.example.com
          Connectivity: both

          Segment name: caReplica2.example.com-to-replica3.example.com
          Left node: caReplica2.example.com
          Right node: replica3.example.com
          Connectivity: both
        ----------------------------
        Number of entries returned 2
        ----------------------------
        ```

    b.  Re-initialize the `domain`{.literal} suffix for all topology segments with the restored server.

        In this example, perform a re-initialization of `caReplica2`{.literal} with data from `server1`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        [root@caReplica2 ~]# ipa-replica-manage re-initialize --from=server1.example.com
        ```

        ``` {.language-plaintext tabindex="-1"}
        Update in progress, 2 seconds elapsed
        Update succeeded
        ```

    c.  Moving on to Certificate Authority data, list all replication topology segments for the `ca`{.literal} suffix.

        ``` {.language-plaintext tabindex="-1"}
        [root@server1 ~]# ipa topologysegment-find ca
        ```

        ``` {.language-plaintext tabindex="-1"}
        -----------------
        1 segment matched
        -----------------
          Segment name: server1.example.com-to-caReplica2.example.com
          Left node: server1.example.com
          Right node: caReplica2.example.com
          Connectivity: both
        ----------------------------
        Number of entries returned 1
        ----------------------------
        ```

    d.  Re-initialize all CA replicas connected to the restored server.

        In this example, perform a `csreplica`{.literal} re-initialization of `caReplica2`{.literal} with data from `server1`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        [root@caReplica2 ~]# ipa-csreplica-manage re-initialize --from=server1.example.com
        ```

6.  Enter the Directory Manager password.

    ``` {.language-plaintext tabindex="-1"}
    Directory Manager password:
    ```

    ``` {.language-plaintext tabindex="-1"}
    Update in progress, 3 seconds elapsed
    Update succeeded
    ```

7.  Continue moving outward through the replication topology, re-initializing successive replicas, until all servers have been updated with the data from restored server `server1.example.com`{.literal}.

    In this example, we only have to re-initialize the `domain`{.literal} suffix on `replica3`{.literal} with the data from `caReplica2`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [root@replica3 ~]# ipa-replica-manage re-initialize --from=caReplica2.example.com
    ```

8.  Enter the Directory Manager password.

    ``` {.language-plaintext tabindex="-1"}
    Directory Manager password:
    ```

    ``` {.language-plaintext tabindex="-1"}
    Update in progress, 3 seconds elapsed
    Update succeeded
    ```

9.  Clear SSSD's cache on every server to avoid authentication problems due to invalid data:

    a.  Stop the SSSD service:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# systemctl stop sssd
        ```

    b.  Remove all cached content from SSSD:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# sss_cache -E
        ```

    c.  Start the SSSD service:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# systemctl start sssd
        ```

    d.  Reboot the server.

### [5.2. Restoring from an encrypted backup](#restoring-from-an-encrypted-backup) {#restoring-from-an-encrypted-backup .title}

You can restore an IdM server from an encrypted IdM backup. The `ipa-restore`{.literal} utility automatically detects if an IdM backup is encrypted and restores it using the GPG2 root keyring.

**Prerequisites**

-   A GPG-encrypted IdM backup. See [Creating a GPG2-encrypted IdM backup](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/preparing_for_disaster_recovery_with_identity_management/backing-up-and-restoring-idm#creating-a-gpg2-encrypted-idm-backup).
-   The LDAP Directory Manager password
-   The passphrase used when creating the GPG key

**Procedure**

1.  If you used a custom keyring location when creating the GPG2 keys, verify that the `$GNUPGHOME`{.literal} environment variable is set to that directory. See [Creating a GPG2 key](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/preparing_for_disaster_recovery_with_identity_management/backing-up-and-restoring-idm#creating-a-gpg2-key).

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# echo $GNUPGHOME
    ```

    ``` {.language-plaintext tabindex="-1"}
    /root/backup
    ```

2.  Provide the `ipa-restore`{.literal} utility with the backup directory location.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa-restore ipa-full-2020-01-13-18-30-54
    ```

    a.  Enter the Directory Manager password.

        ``` {.language-plaintext tabindex="-1"}
        Directory Manager (existing master) password:
        ```

    b.  Enter the passphrase you used when creating the GPG key.

        ``` {.language-plaintext tabindex="-1"}
        ┌────────────────────────────────────────────────────────────────┐
        │ Please enter the passphrase to unlock the OpenPGP secret key:  │
        │ "GPG User (first key) <root@example.com>"                      │
        │ 2048-bit RSA key, ID BF28FFA302EF4557,                         │
        │ created 2020-01-13.                                            │
        │                                                                │
        │                                                                │
        │ Passphrase: <passphrase>                                       │
        │                                                                │
        │         <OK>                                    <Cancel>       │
        └────────────────────────────────────────────────────────────────┘
        ```

3.  Re-initialize all replicas connected to the restored server. See [Restoring an IdM server from backup](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/performing_disaster_recovery_with_identity_management/recovering-from-data-loss-with-idm-backups#restoring-an-idm-server-from-a-backup).

## [Chapter 6. Restoring IdM servers using Ansible playbooks](#restoring-idm-servers-using-ansible-playbooks) {#chapter-6.-restoring-idm-servers-using-ansible-playbooks .title}

Use the `ipabackup`{.literal} Ansible role to automate restoring an Identity Management (IdM) server from a backup and transfer backup files between servers and your Ansible controller.

### [6.1. Creating an Ansible inventory file for IdM](#creating-an-ansible-inventory-file-for-idm) {#creating-an-ansible-inventory-file-for-idm .title}

Create an Ansible inventory file for Identity Management (IdM) to organize playbook targets and run playbooks from your home directory without root privileges.

When working with Ansible, it is good practice to create, in your home directory, a subdirectory dedicated to Ansible playbooks that you copy and adapt from the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/*`{.literal} and `/usr/share/doc/rhel-system-roles/*`{.literal} subdirectories. This practice has the following advantages:

-   You can find all your playbooks in one place.
-   You can run your playbooks without invoking `root`{.literal} privileges.

**Procedure**

1.  Create a directory for your Ansible configuration and playbooks in your home directory:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir ~/MyPlaybooks/
    ```

2.  Change into the **\~/MyPlaybooks/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks
    ```

3.  Create the **\~/MyPlaybooks/ansible.cfg** file with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [defaults]
    inventory = /home/<username>/MyPlaybooks/inventory

    [privilege_escalation]
    become=True
    ```

4.  Create the **\~/MyPlaybooks/inventory** file with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [eu]
    server.idm.example.com

    [us]
    replica.idm.example.com

    [ipaserver:children]
    eu
    us
    ```

    This configuration defines two host groups, **eu** and **us**, for hosts in these locations. Additionally, this configuration defines the **ipaserver** host group, which contains all hosts from the **eu** and **us** groups.

### [6.2. Using Ansible to restore an IdM server from a backup stored on the server](#using-ansible-to-restore-an-idm-server-from-a-backup-stored-on-the-server) {#using-ansible-to-restore-an-idm-server-from-a-backup-stored-on-the-server .title}

You can use an Ansible playbook to restore an IdM server from a backup stored on that host.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is run, is part of the IdM domain as an IdM client, server or replica.

-   You know the LDAP Directory Manager password.

**Procedure**

1.  Navigate to the `~/MyPlaybooks/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Make a copy of the `restore-server.yml`{.literal} file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/restore-server.yml restore-my-server.yml
    ```

3.  Open the `restore-my-server.yml`{.literal} Ansible playbook file for editing.

4.  Adapt the file by setting the following variables:

    a.  Set the `hosts`{.literal} variable to a host group from your inventory file. In this example, set it to the `ipaserver`{.literal} host group.

    b.  Set the `ipabackup_name`{.literal} variable to the name of the `ipabackup`{.literal} to restore.

    c.  Set the `ipabackup_password`{.literal} variable to the LDAP Directory Manager password.

        ``` {.language-plaintext tabindex="-1"}
        ---
        - name: Playbook to restore an IPA server
          hosts: ipaserver
          become: true

          vars:
            ipabackup_name: ipa-full-2021-04-30-13-12-00
            ipabackup_password: <your_LDAP_DM_password>

          roles:
          - role: freeipa.ansible_freeipa.ipabackup
            state: restored
        ```

5.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/`{.literal} directory on the control node.

6.  Run the Ansible playbook specifying the inventory file and the playbook file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i ~/MyPlaybooks/inventory restore-my-server.yml
    ```

### [6.3. Using Ansible to restore an IdM server from a backup stored on your Ansible controller](#using-ansible-to-restore-an-idm-server-from-a-backup-stored-on-your-ansible-controller) {#using-ansible-to-restore-an-idm-server-from-a-backup-stored-on-your-ansible-controller .title}

You can use an Ansible playbook to restore an IdM server from a backup stored on your Ansible controller.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is run, is part of the IdM domain as an IdM client, server or replica.

-   You know the LDAP Directory Manager password.

**Procedure**

1.  Navigate to the `~/MyPlaybooks/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Make a copy of the `restore-server-from-controller.yml`{.literal} file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/restore-server-from-controller.yml restore-my-server-from-my-controller.yml
    ```

3.  Open the `restore-my-server-from-my-controller.yml`{.literal} file for editing.

4.  Adapt the file by setting the following variables:

    a.  Set the `hosts`{.literal} variable to a host group from your inventory file. In this example, set it to the `ipaserver`{.literal} host group.

    b.  Set the `ipabackup_name`{.literal} variable to the name of the `ipabackup`{.literal} to restore.

    c.  Set the `ipabackup_password`{.literal} variable to the LDAP Directory Manager password.

        ``` {.language-plaintext tabindex="-1"}
        ---
        - name: Playbook to restore IPA server from controller
          hosts: ipaserver
          become: true

          vars:
            ipabackup_name: server.idm.example.com_ipa-full-2021-04-30-13-12-00
            ipabackup_password: <your_LDAP_DM_password>
            ipabackup_from_controller: true

          roles:
          - role: freeipa.ansible_freeipa.ipabackup
            state: restored
        ```

5.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/`{.literal} directory on the control node.

6.  Run the Ansible playbook, specifying the inventory file and the playbook file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i ~/MyPlaybooks/inventory restore-my-server-from-my-controller.yml
    ```

### [6.4. Using Ansible to copy a backup of an IdM server to your Ansible controller](#using-ansible-to-copy-a-backup-of-an-idm-server-to-your-ansible-controller) {#using-ansible-to-copy-a-backup-of-an-idm-server-to-your-ansible-controller .title}

You can use an Ansible playbook to copy an existing backup file of an IdM server from the IdM server to your Ansible controller.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is run, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  To store the backups, create a subdirectory in your home directory on the Ansible controller.

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir ~/ipabackups
    ```

2.  Navigate to the `~/MyPlaybooks/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

3.  Make a copy of the `copy-backup-from-server.yml`{.literal} file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/copy-backup-from-server.yml copy-backup-from-my-server-to-my-controller.yml
    ```

4.  Open the `copy-my-backup-from-my-server-to-my-controller.yml`{.literal} file for editing.

5.  Adapt the file by setting the following variables:

    a.  Set the `hosts`{.literal} variable to a host group from your inventory file. In this example, set it to the `ipaserver`{.literal} host group.

    b.  Set the `ipabackup_name`{.literal} variable to the name of the `ipabackup`{.literal} on your IdM server to copy to your Ansible controller.

    c.  By default, backups are stored in the present working directory of the Ansible controller. To specify the directory you created in Step 1, add the `ipabackup_controller_path`{.literal} variable and set it to the `/home/user/ipabackups`{.literal} directory.

        ``` {.language-plaintext tabindex="-1"}
        ---
        - name: Playbook to copy backup from IPA server
          hosts: ipaserver
          become: true
          vars:
            ipabackup_name: ipa-full-2021-04-30-13-12-00
            ipabackup_to_controller: true
            ipabackup_controller_path: /home/user/ipabackups

          roles:
          - role: freeipa.ansible_freeipa.ipabackup
            state: present
        ```

6.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/`{.literal} directory on the control node.

7.  Run the Ansible playbook, specifying the inventory file and the playbook file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i ~/MyPlaybooks/inventory copy-backup-from-my-server-to-my-controller.yml
    ```

    Note

    To copy **all** IdM backups to your controller, set the `ipabackup_name`{.literal} variable in the Ansible playbook to `all`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
      vars:
        ipabackup_name: all
        ipabackup_to_controller: true
    ```

    For an example, see the `copy-all-backups-from-server.yml`{.literal} Ansible playbook in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks`{.literal} directory.

**Verification**

-   Verify your backup is in the `/home/user/ipabackups`{.literal} directory on your Ansible controller:

    ``` {.language-plaintext tabindex="-1"}
    [user@controller ~]$ ls /home/user/ipabackups
    server.idm.example.com_ipa-full-2021-04-30-13-12-00
    ```

### [6.5. Using Ansible to copy a backup of an IdM server from your Ansible controller to the IdM server](#using-ansible-to-copy-a-backup-of-an-idm-server-from-your-ansible-controller-to-the-idm-server) {#using-ansible-to-copy-a-backup-of-an-idm-server-from-your-ansible-controller-to-the-idm-server .title}

You can use an Ansible playbook to copy an existing backup file of an IdM server from your Ansible controller to the IdM server.

**Prerequisites**

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is run, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to the `~/MyPlaybooks/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Make a copy of the `copy-backup-from-controller.yml`{.literal} file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/copy-backup-from-controller.yml copy-backup-from-my-controller-to-my-server.yml
    ```

3.  Open the `copy-my-backup-from-my-controller-to-my-server.yml`{.literal} file for editing.

4.  Adapt the file by setting the following variables:

    a.  Set the `hosts`{.literal} variable to a host group from your inventory file. In this example, set it to the `ipaserver`{.literal} host group.

    b.  Set the `ipabackup_name`{.literal} variable to the name of the `ipabackup`{.literal} on your Ansible controller to copy to the IdM server.

        ``` {.language-plaintext tabindex="-1"}
        ---
        - name: Playbook to copy a backup from controller to the IPA server
          hosts: ipaserver
          become: true

          vars:
            ipabackup_name: server.idm.example.com_ipa-full-2021-04-30-13-12-00
            ipabackup_from_controller: true

          roles:
          - role: freeipa.ansible_freeipa.ipabackup
            state: copied
        ```

5.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/`{.literal} directory on the control node.

6.  Run the Ansible playbook, specifying the inventory file and the playbook file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i ~/MyPlaybooks/inventory copy-backup-from-my-controller-to-my-server.yml
    ```

### [6.6. Using Ansible to remove a backup from an IdM server](#using-ansible-to-remove-a-backup-from-an-idm-server) {#using-ansible-to-remove-a-backup-from-an-idm-server .title}

You can use an Ansible playbook to automate the removal of old or unnecessary backup files from an IdM server.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is run, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to the \~/MyPlaybooks/ directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Make a copy of the `remove-backup-from-server.yml`{.literal} file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/remove-backup-from-server.yml remove-backup-from-my-server.yml
    ```

3.  Open the `remove-backup-from-my-server.yml`{.literal} file for editing.

4.  Adapt the file by setting the following variables:

    a.  Set the `hosts`{.literal} variable to a host group from your inventory file. In this example, set it to the `ipaserver`{.literal} host group.

    b.  Set the `ipabackup_name`{.literal} variable to the name of the `ipabackup`{.literal} to remove from your IdM server.

        ``` {.language-plaintext tabindex="-1"}
        ---
        - name: Playbook to remove backup from IPA server
          hosts: ipaserver
          become: true

          vars:
            ipabackup_name: ipa-full-2021-04-30-13-12-00

          roles:
          - role: freeipa.ansible_freeipa.ipabackup
            state: absent
        ```

5.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/`{.literal} directory on the control node.

6.  Run the Ansible playbook, specifying the inventory file and the playbook file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i ~/MyPlaybooks/inventory remove-backup-from-my-server.yml
    ```

    Note

    To remove **all** IdM backups from the IdM server, set the `ipabackup_name`{.literal} variable in the Ansible playbook to `all`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
      vars:
        ipabackup_name: all
    ```

    For an example, see the `remove-all-backups-from-server.yml`{.literal} Ansible playbook in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks`{.literal} directory.

## [Chapter 7. Managing data loss](#managing-data-loss) {#chapter-7.-managing-data-loss .title}

Respond to data loss events by isolating affected servers or manually restoring lost information. You can determine the appropriate recovery method based on whether the data loss is isolated to specific replicas or has propagated across the entire environment.

### [7.1. Responding to isolated data loss](#responding-to-isolated-data-loss) {#responding-to-isolated-data-loss .title}

If the data loss occurs, minimize the spread of corrupted data by immediately isolating the affected servers from the replication topology and replacing them with new replicas created from the remaining healthy servers.

**Prerequisites**

-   A robust IdM replication topology with multiple replicas. See [Preparing for server loss with replication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/preparing_for_disaster_recovery_with_identity_management/preparing-for-server-loss-with-replication).

**Procedure**

1.  To limit replicating the data loss, disconnect all affected replicas from the rest of the topology by removing their replication topology segments.

    a.  Display all `domain`{.literal} replication topology segments in the deployment.

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa topologysegment-find
        ```

        ``` {.language-plaintext tabindex="-1"}
        Suffix name: domain
        ------------------
        8 segments matched
        ------------------
          Segment name: segment1
          Left node: server.example.com
          Right node: server2.example.com
          Connectivity: both

        ...

        ----------------------------
        Number of entries returned 8
        ----------------------------
        ```

    b.  Delete all `domain`{.literal} topology segments involving the affected servers.

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa topologysegment-del
        ```

        ``` {.language-plaintext tabindex="-1"}
        Suffix name: domain
        Segment name: segment1
        -----------------------------
        Deleted segment "segment1"
        -----------------------------
        ```

    c.  Identify the `ca`{.literal} topology segments that involve the restored server.

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa topologysegment-find
        ```

        ``` {.language-plaintext tabindex="-1"}
        Suffix name: ca
        ------------------
        1 segments matched
        ------------------
          Segment name: ca_segment
          Left node: server.example.com
          Right node: server2.example.com
          Connectivity: both
        ----------------------------
        Number of entries returned 1
        ----------------------------
        ```

    d.  Delete all `ca`{.literal} topology segments that involve the restored server.

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa topologysegment-del
        ```

        ``` {.language-plaintext tabindex="-1"}
        Suffix name: ca
        Segment name: ca_segment
        -----------------------------
        Deleted segment "ca_segment"
        -----------------------------
        ```

2.  The servers affected by the data loss must be abandoned. To create replacement replicas, see [Recovering multiple servers with replication](#recovering-multiple-servers-with-replication "Chapter 3. Recovering multiple servers with replication").

### [7.2. Responding to limited data loss among all servers](#responding-to-limited-data-loss-among-all-servers) {#responding-to-limited-data-loss-among-all-servers .title}

Respond to known, limited data loss that has propagated to all replicas, such as an accidental deletion. You can manually re-add the missing information to the database using a backup or a Virtual Machine (VM) snapshot.

**Prerequisites**

-   A Virtual VM snapshot or IdM backup of an IdM server that contains the lost data.

**Procedure**

1.  If you need to review any lost data, restore the VM snapshot or backup to an isolated server on a separate network.
2.  Add the missing information to the database using `ipa`{.literal} or `ldapadd`{.literal} commands.

**Additional resources**

-   [Recovering from data loss with VM snapshots](#recovering-from-data-loss-with-vm-snapshots "Chapter 4. Recovering from data loss with VM snapshots")
-   [Backing Up and Restoring IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/preparing_for_disaster_recovery_with_identity_management/backing-up-and-restoring-idm)

### [7.3. Responding to undefined data loss among all servers](#responding-to-undefined-data-loss-among-all-servers) {#responding-to-undefined-data-loss-among-all-servers .title}

Respond to severe or unknown data loss that has affected every replica in the deployment. You can restore an Identity Management (IdM) Certificate Authority (CA) server from a Virtual Machine (VM) snapshot to a known good state and use it to deploy an entirely new environment.

**Prerequisites**

-   A VM snapshot contains the lost data.

**Procedure**

1.  Restore an IdM Certificate Authority (CA) Replica from a VM snapshot to a known good state, and deploy a new IdM environment from it. See [Recovering from only a VM snapshot](#recovering-from-only-a-vm-snapshot "4.1. Recovering from only a VM snapshot").
2.  Add any data created after the snapshot was taken using `ipa`{.literal} or `ldapadd`{.literal} commands.

**Additional resources**

-   [Recovering from data loss with VM snapshots](#recovering-from-data-loss-with-vm-snapshots "Chapter 4. Recovering from data loss with VM snapshots")

## [Chapter 8. Adjusting IdM clients during recovery](#adjusting-idm-clients-during-recovery) {#chapter-8.-adjusting-idm-clients-during-recovery .title}

Update Identity Management (IdM) configurations to reflect changes in the server topology. You can ensure that clients continue to authenticate correctly by pointing them to functional replicas, updating DNS records, and clearing local caches to remove outdated server information.

**Procedure**

1.  Adjusting DNS configuration:

    a.  If `/etc/hosts`{.literal} contains any references to IdM servers, ensure that hard-coded IP-to-hostname mappings are valid.
    b.  If IdM clients are using IdM DNS for name resolution, ensure that the `nameserver`{.literal} entries in `/etc/resolv.conf`{.literal} point to working IdM replicas providing DNS services.

2.  Adjusting Kerberos configuration:

    a.  By default, IdM clients look to DNS Service records for Kerberos servers, and adjust to changes in the replica topology:

        ``` {.language-plaintext tabindex="-1"}
        [root@client ~]# grep dns_lookup_kdc /etc/krb5.conf
        ```

        ``` {.language-plaintext tabindex="-1"}
          dns_lookup_kdc = true
        ```

    b.  If IdM clients have been hard-coded to use specific IdM servers in `/etc/krb5.conf`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        [root@client ~]# grep dns_lookup_kdc /etc/krb5.conf
        ```

        ``` {.language-plaintext tabindex="-1"}
          dns_lookup_kdc = false
        ```

        make sure `kdc`{.literal}, `master_kdc`{.literal} and `admin_server`{.literal} entries in `/etc/krb5.conf`{.literal} are pointing to IdM servers that work properly:

        ``` {.language-plaintext tabindex="-1"}
        [realms]
         EXAMPLE.COM = {
          kdc = functional-server.example.com:88
          master_kdc = functional-server.example.com:88
          admin_server = functional-server.example.com:749
          default_domain = example.com
          pkinit_anchors = FILE:/var/lib/ipa-client/pki/kdc-ca-bundle.pem
          pkinit_pool = FILE:/var/lib/ipa-client/pki/ca-bundle.pem
        }
        ```

3.  Adjusting SSSD configuration:

    a.  By default, IdM clients look to DNS Service records for LDAP servers and adjust to changes in the replica topology:

        ``` {.language-plaintext tabindex="-1"}
        [root@client ~]# grep ipa_server /etc/sssd/sssd.conf
        ```

        ``` {.language-plaintext tabindex="-1"}
        ipa_server = _srv_, functional-server.example.com
        ```

    b.  If IdM clients have been hard-coded to use specific IdM servers in `/etc/sssd/sssd.conf`{.literal}, make sure the `ipa_server`{.literal} entry points to IdM servers that are working properly:

        ``` {.language-plaintext tabindex="-1"}
        [root@client ~]# grep ipa_server /etc/sssd/sssd.conf
        ```

        ``` {.language-plaintext tabindex="-1"}
        ipa_server = functional-server.example.com
        ```

4.  Clearing SSSD's cached information:

    -   The SSSD cache may contain outdated information pertaining to lost servers. If users experience inconsistent authentication problems, purge the SSSD cache :

        ``` {.language-plaintext tabindex="-1"}
        [root@client ~]# sss_cache -E
        ```

**Verification**

1.  Verify the Kerberos configuration by retrieving a Kerberos Ticket-Granting-Ticket as an IdM user.

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# kinit admin
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password for admin@EXAMPLE.COM:
    ```

2.  Verify the cached ticket by listing the active credentials.

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# klist
    ```

    ``` {.language-plaintext tabindex="-1"}
    Ticket cache: KCM:0
    Default principal: admin@EXAMPLE.COM

    Valid starting       Expires              Service principal
    10/31/2019 18:44:58  11/25/2019 18:44:55  krbtgt/EXAMPLE.COM@EXAMPLE.COM
    ```

3.  Verify the SSSD configuration by retrieving IdM user information.

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# id admin
    ```

    ``` {.language-plaintext tabindex="-1"}
    uid=1965200000(admin) gid=1965200000(admins) groups=1965200000(admins)
    ```

## [Legal Notice](#idm140624662858304) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
