---
{"title": "Configuring and using network file services", "guide": "configuring_and_using_network_file_services", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_using_network_file_services/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

Streamline your workflow with the new MCP server for Red Hat product documentation.Connect your AI tools and LLMs directly to live Red Hat product documentation. [Connect now](https://docs.redhat.com/en/documentation/mcp_server_for_red_hat_documentation/current%20).

# Configuring and using network file services {#configuring-and-using-network-file-services .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## A guide to configuring and using network file services in Red Hat Enterprise Linux 10 {#a-guide-to-configuring-and-using-network-file-services-in-red-hat-enterprise-linux-10 .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm139622278273056)

**Abstract**

This document describes how to configure and run network file services on Red Hat Enterprise Linux 10, including Samba server and NFS server.

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

## [Chapter 1. Using Samba as a server](#using-samba-as-a-server) {#chapter-1.-using-samba-as-a-server .title}

Samba implements the Server Message Block (SMB) protocol in Red Hat Enterprise Linux. SMB is used to access server resources such as file shares and printers. Samba also implements Distributed Computing Environment Remote Procedure Call (DCE RPC) used by Microsoft Windows.

For more information refer to the:

-   `smb.conf(5)`{.literal} man page on your system
-   `/usr/share/docs/samba-version/`{.literal} directory that contains general documentation, example scripts, and LDAP schema files, provided by the Samba project

You can run Samba as:

-   An Active Directory (AD) or NT4 domain member

-   A standalone server

-   An NT4 Primary Domain Controller (PDC) or Backup Domain Controller (BDC)

    Note

    Red Hat supports the PDC and BDC modes only in existing installations with Windows versions which support NT4 domains. Avoid setting up a new Samba NT4 domain. Microsoft operating systems later than Windows 7 and Windows Server 2008 R2 do not support NT4 domains.

    Red Hat does not support running Samba as an AD domain controller (DC).

Independently of the installation mode, you can optionally share directories and printers. This enables Samba to act as a file and print server.

### [1.1. Understanding the different Samba services and modes](#understanding-the-different-samba-services-and-modes) {#understanding-the-different-samba-services-and-modes .title}

The `samba`{.literal} package provides multiple services. Depending on your environment and the scenario you want to configure, you require one or more of these services and configure Samba in different modes.

#### [1.1.1. The Samba services](#the-samba-services) {#the-samba-services .title}

Samba services in Linux include `smbd`{.literal}, `nmbd`{.literal}, `winbindd`{.literal}, and `samba-bgqd`{.literal}. Their roles cover file and printer sharing, name resolution, domain integration, and printer management.

Samba provides the following services:

`smbd`{.literal}

:   This service provides file sharing and printing services by using the SMB protocol. Additionally, the service is responsible for resource locking and for authenticating connecting users. For authenticating domain members, `smbd`{.literal} requires `winbindd`{.literal}. The `smb`{.literal} `systemd`{.literal} service starts and stops the `smbd`{.literal} daemon.

    To use the `smbd`{.literal} service, install the `samba`{.literal} package.

`nmbd`{.literal}

:   This service provides host name and IP resolution by using the NetBIOS over IPv4 protocol. Additionally, the `nmbd`{.literal} service enables browsing the SMB network to locate domains, work groups, hosts, file shares, and printers. The service either reports this information directly to the broadcasting client or forwards it to a local or master browser. The `nmb`{.literal} `systemd`{.literal} service starts and stops the `nmbd`{.literal} daemon.

    Note that modern SMB networks use DNS to resolve clients and IP addresses. For Kerberos a working DNS set up is required. When using Samba with Active Directory, `nmbd`{.literal} is not required for interoperability, as DNS handles name resolution in AD environments.

    To use the `nmbd`{.literal} service, install the `samba`{.literal} package.

`winbindd`{.literal}

:   This service provides an interface for the Name Service Switch (NSS). It enables using AD or NT4 domain users and groups on the local system. This enables, for example, domain users to authenticate to services hosted on a Samba server or to other local services. The `winbind`{.literal} `systemd`{.literal} service starts and stops the `winbindd`{.literal} daemon.

    If you set up Samba as a domain member, `winbindd`{.literal} must be started before the `smbd`{.literal} service. Otherwise, domain users and groups are not available to the local system.

    To use the `winbindd`{.literal} service, install the `samba-winbind`{.literal} package.

    Important

    Red Hat only supports running Samba as a server with the `winbindd`{.literal} service to provide domain users and groups locally. Due to limitations, such as missing Windows access control list (ACL) support and NT LAN Manager (NTLM) fallback, SSSD is unsupported.

`samba-bgqd`{.literal}
:   The Samba background queue daemon regularly updates the printer list with printers from CUPS. For print servers with multiple printers, run this daemon. It is managed by the `samba-bgqd`{.literal} `systemd`{.literal} service. If it fails to run, `rpcd_spoolss`{.literal} starts it on demand.

#### [1.1.2. The Samba security services](#the-samba-security-services) {#the-samba-security-services .title}

The `security`{.literal} parameter in the `[global]`{.literal} section in the `/etc/samba/smb.conf`{.literal} file manages how Samba authenticates users that are connecting to the service.

Depending on the mode you install Samba in, the parameter must be set to different values:

On an Active Directory (AD) domain member, set `security = ads`{.literal}
:   In this mode, Samba uses Kerberos to authenticate AD users.

On a standalone server, set `security = user`{.literal}
:   In this mode, Samba uses a local database to authenticate connecting users.

On an NT4 Primary Domain Controller (PDC) or Backup Domain Controller (BDC), set `security = user`{.literal}
:   In this mode, Samba authenticates users to a local or Lightweight Directory Access Protocol (LDAP) database.

On an NT4 domain member, set `security = domain`{.literal}
:   In this mode, Samba authenticates connecting users to an NT4 PDC or BDC. You cannot use this mode on AD domain members.

**Additional resources**

-   [Setting up Samba as an AD domain member server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-samba-as-an-ad-domain-member-server)
-   [Setting up Samba as a standalone server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-samba-as-a-standalone-server)
-   [Setting up Samba as an AD domain member server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-samba-as-an-ad-domain-member-server)

#### [1.1.3. Scenarios when Samba services and Samba client utilities load and reload their configuration](#scenarios-when-samba-services-and-samba-client-utilities-load-and-reload-their-configuration) {#scenarios-when-samba-services-and-samba-client-utilities-load-and-reload-their-configuration .title}

When Samba services and client utilities load or reload configuration files, details triggers for automatic and manual reloads. Certain settings require a full service restart for configuration changes to become effective.

The following describes when Samba services and utilities load and reload their configuration:

-   Samba services reload their configuration:

    -   Automatically every 3 minutes
    -   On manual request, for example, when you run the `smbcontrol all reload-config`{.literal} command.

-   Samba client utilities read their configuration only when you start them.

Certain parameters, such as `security`{.literal} require a restart of the `smb`{.literal} service to take effect. A reload is not sufficient. For more information, refer to:

-   The `How configuration changes are applied`{.literal} section in the `smb.conf(5)`{.literal} man page on your system
-   `smbd(8)`{.literal}, `nmbd(8)`{.literal}, and `winbindd(8)`{.literal} man pages on your system

#### [1.1.4. Editing the Samba configuration in a safe way](#editing-the-samba-configuration-in-a-safe-way) {#editing-the-samba-configuration-in-a-safe-way .title}

Samba services automatically reload their configuration every 3 minutes. To prevent services from reloading changes before you verify the configuration, you can edit the Samba configuration in a safe way. Use the `testparm`{.literal} utility to verify the configuration.

**Prerequisites**

-   Samba is installed.

**Procedure**

1.  Create a copy of the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # cp /etc/samba/smb.conf /etc/samba/samba.conf.copy
    ```

2.  Edit the copied file and make the required changes.

3.  Verify the configuration in the `/etc/samba/samba.conf.`{.literal}*`copy`{.literal}* file:

    ``` {.language-plaintext tabindex="-1"}
    # testparm -s /etc/samba/samba.conf.copy
    ```

    If `testparm`{.literal} reports errors, fix them and run the command again.

4.  Override the `/etc/samba/smb.conf`{.literal} file with the new configuration:

    ``` {.language-plaintext tabindex="-1"}
    # mv /etc/samba/samba.conf.copy /etc/samba/smb.conf
    ```

5.  Wait until the Samba services automatically reload their configuration or manually reload the configuration:

    ``` {.language-plaintext tabindex="-1"}
    # smbcontrol all reload-config
    ```

### [1.2. Verifying the smb.conf file by using the testparm utility](#verifying-the-smb-conf-file-by-using-the-testparm-utility) {#verifying-the-smb.conf-file-by-using-the-testparm-utility .title}

The `testparm`{.literal} utility verifies the Samba configuration in `/etc/samba/smb.conf`{.literal}. It detects invalid parameters, values, and incorrect ID mapping. If no errors are reported, Samba services load the configuration successfully. `testparm`{.literal} cannot verify service availability or runtime behavior.

Important

Verify the `/etc/samba/smb.conf`{.literal} file by using `testparm`{.literal} after each modification of this file.

**Prerequisites**

-   You installed Samba.
-   The `/etc/samba/smb.conf`{.literal} file exists.

**Procedure**

1.  Run the `testparm`{.literal} utility as the `root`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    # testparm
    ```

    ``` {.language-plaintext tabindex="-1"}
    Load smb config files from /etc/samba/smb.conf
    rlimit_max: increasing rlimit_max (1024) to minimum Windows limit (16384)
    Unknown parameter encountered: "log level"
    Processing section "[example_share]"
    Loaded services file OK.
    ERROR: The idmap range for the domain * (tdb) overlaps with the range of DOMAIN (ad)!

    Server role: ROLE_DOMAIN_MEMBER

    Press enter to see a dump of your service definitions

    # Global parameters
    [global]
        ...

    [example_share]
        ...
    ```

    The previous example output reports a non-existent parameter and an incorrect ID mapping configuration.

2.  If `testparm`{.literal} reports incorrect parameters, values, or other errors in the configuration, fix the problem and run the utility again.

### [1.3. Setting up Samba as a standalone server](#setting-up-samba-as-a-standalone-server) {#setting-up-samba-as-a-standalone-server .title}

You can configure Samba as a standalone server outside a domain. In this mode, Samba authenticates users against a local database instead of a Domain Controller (DC). You can also enable guest access to services without authentication.

#### [1.3.1. Setting up the server configuration for the standalone server](#setting-up-the-server-configuration-for-the-standalone-server) {#setting-up-the-server-configuration-for-the-standalone-server .title}

You can set up the server configuration for a Samba standalone server. For more information, see the `smb.conf(5)`{.literal} man page on your system.

**Procedure**

1.  Install the `samba`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install samba
    ```

2.  Edit the `/etc/samba/smb.conf`{.literal} file and set the following parameters:

    ``` {.language-plaintext tabindex="-1"}
    [global]
        workgroup = Example-WG
        netbios name = Server
        security = user

        log file = /var/log/samba/%m.log
        log level = 1
    ```

    This configuration defines a standalone server named `Server`{.literal} within the `Example-WG`{.literal} work group. Additionally, this configuration enables logging on a minimal level (`1`{.literal}) and stores log files in the `/var/log/samba/`{.literal} directory. Samba expands the `%m`{.literal} macro in the `log file`{.literal} parameter to the NetBIOS name of connecting clients, enabling individual log files.

3.  Optional: Configure file or printer sharing. See:

    -   [Setting up a Samba file share that uses POSIX ACLs](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-a-samba-file-share-that-uses-posix-acls)
    -   [Setting up a share that uses Windows ACLs](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-a-share-that-uses-windows-acls)
    -   [Setting up Samba as a Print Server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-samba-as-a-print-server)

4.  Verify the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # testparm
    ```

5.  If you set up shares that require authentication, create the user accounts.

    For details, see [Creating and enabling local user accounts](#creating-and-enabling-local-user-accounts "1.3.2. Creating and enabling local user accounts").

6.  Open the required ports and reload the firewall configuration by using the `firewall-cmd`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=samba
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

7.  Enable and start the `smb`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now smb
    ```

#### [1.3.2. Creating and enabling local user accounts](#creating-and-enabling-local-user-accounts) {#creating-and-enabling-local-user-accounts .title}

To authenticate users connecting to a share, create accounts on the Samba host. Create accounts in both the operating system and Samba database. Operating system accounts validate ACLs, and Samba accounts authenticate users.

If you use the `passdb backend = tdbsam`{.literal} default setting, Samba stores user accounts in the `/var/lib/samba/private/passdb.tdb`{.literal} database.

You can create a local Samba user named `example`{.literal}.

**Prerequisites**

-   Samba is installed and configured as a standalone server.

**Procedure**

1.  Create the operating system account:

    ``` {.language-plaintext tabindex="-1"}
    # useradd -M -s /sbin/nologin example
    ```

    This command adds the `example`{.literal} account without creating a home directory. If the account is only used to authenticate to Samba, assign the `/sbin/nologin`{.literal} command as shell. This prevents the account from logging in locally.

2.  Set a password to the operating system account to enable it:

    ``` {.language-plaintext tabindex="-1"}
    # passwd example
    ```

    ``` {.language-plaintext tabindex="-1"}
    Enter new UNIX password: password
    Retype new UNIX password: password
    passwd: password updated successfully
    ```

    Samba does not use the password set on the operating system account to authenticate. However, you need to set a password to enable the account. If an account is disabled, Samba denies access if this user connects.

3.  Add the user to the Samba database and set a password to the account:

    ``` {.language-plaintext tabindex="-1"}
    # smbpasswd -a example
    ```

    ``` {.language-plaintext tabindex="-1"}
    New SMB password: password
    Retype new SMB password: password
    Added user example.
    ```

    Use this password to authenticate when using this account to connect to a Samba share.

4.  Enable the Samba account:

    ``` {.language-plaintext tabindex="-1"}
    # smbpasswd -e example
    ```

    ``` {.language-plaintext tabindex="-1"}
    Enabled user example.
    ```

### [1.4. Understanding and configuring Samba ID mapping](#understanding-and-configuring-samba-id-mapping) {#understanding-and-configuring-samba-id-mapping .title}

Windows domains identify users and groups by Security Identifiers (SIDs). Linux requires unique User Identifiers (UIDs) and Group Identifiers (GIDs). On Samba domain members, `winbindd`{.literal} provides domain user and group information to the operating system.

To enable the `winbindd`{.literal} service to provide unique IDs for users and groups to Linux, configure ID mapping in `/etc/samba/smb.conf`{.literal} for:

-   The local database (default domain)
-   The Active Directory (AD) or NT4 domain the Samba server is a member of
-   Each trusted domain from which users must be able to access resources on this Samba server

Samba provides different ID mapping back ends for specific configurations. The most frequently used back ends are:

Frequently used back ends

:   

+---------------------+--------------------------------------------------------+
| Back end            | Use case                                               |
+:====================+:=======================================================+
| `tdb`{.literal}     | The `*`{.literal} default domain only                  |
+---------------------+--------------------------------------------------------+
| `ad`{.literal}      | AD domains only                                        |
+---------------------+--------------------------------------------------------+
| `rid`{.literal}     | AD and NT4 domains                                     |
+---------------------+--------------------------------------------------------+
| `autorid`{.literal} | AD, NT4, and the `*`{.literal} default domain          |
+---------------------+--------------------------------------------------------+

Show more

#### [1.4.1. Planning Samba ID ranges](#planning-samba-id-ranges) {#planning-samba-id-ranges .title}

Each domain configuration requires a unique ID range that must not overlap with other domains. This applies whether you store Linux User Identifiers (UIDs) and Group Identifiers (GIDs) in Active Directory (AD) or generate them by using Samba.

Warning

If you set overlapping ID ranges, Samba fails to work correctly.

**Example 1.1. Unique ID Ranges**

The following shows non-overlapping ID mapping ranges for the default (`*`{.literal}), `AD-DOM`{.literal}, and the `TRUST-DOM`{.literal} domains.

``` {.language-plaintext tabindex="-1"}
[global]
...
idmap config * : backend = tdb
idmap config * : range = 10000-999999

idmap config AD-DOM:backend = rid
idmap config AD-DOM:range = 2000000-2999999

idmap config TRUST-DOM:backend = rid
idmap config TRUST-DOM:range = 4000000-4999999
```

Important

You can only assign one range per domain. Therefore, leave enough space between the domain ranges. This enables you to extend the range later if your domain grows.

If you later assign a different range to a domain, ownership is lost. This affects files and directories previously created by these users and groups.

#### [1.4.2. The \* default domain](#the-asterisk-default-domain) {#the-default-domain .title}

You can configure the default Samba ID mapping domain to ensure proper ID assignment for local users, groups, and built-in accounts. Select and manage appropriate back ends to maintain system security, scalability, and compliance in domain environments.

In a domain environment, you add one ID mapping configuration for each of the following:

-   The domain the Samba server is a member of
-   Each trusted domain that should be able to access the Samba server

However, for all other objects, Samba assigns IDs from the default domain. This includes:

-   Local Samba users and groups
-   Samba built-in accounts and groups, such as `BUILTIN\Administrators`{.literal}

Important

You must configure the default domain as described to enable Samba to operate correctly.

The default domain back end must be writable to permanently store the assigned IDs.

For the default domain, you can use one of the following back ends:

`tdb`{.literal}

:   When you configure the default domain to use the `tdb`{.literal} back end, set an ID range that is big enough to include future objects. These objects must not be part of a defined domain ID mapping configuration.

    For example, set the following in the `[global]`{.literal} section in the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    idmap config * : backend = tdb
    idmap config * : range = 10000-999999
    ```

`autorid`{.literal}

:   When you configure the default domain to use the `autorid`{.literal} back end, adding additional ID mapping configurations for domains is optional.

    Note

    The range should be a multiple of the `rangesize`{.literal} and must be at least twice its value. This ensures sufficient ID range space for the mandatory `BUILTIN`{.literal} domain. With a default `rangesize`{.literal} of 100000, the range must span at least 200000. For example, range = 100000 - 299999.

    For example, set the following in the `[global]`{.literal} section in the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    idmap config * : backend = autorid
    idmap config * : range = 10000-999999
    ```

**Additional resources**

-   [Using the TDB ID mapping back end](#using-the-tdb-id-mapping-back-end "1.4.3. Using the tdb ID mapping back end")
-   [Using the autorid ID mapping back end](#using-the-autorid-id-mapping-back-end "1.4.6. Using the autorid ID mapping back end")

#### [1.4.3. Using the tdb ID mapping back end](#using-the-tdb-id-mapping-back-end) {#using-the-tdb-id-mapping-back-end .title}

The `winbindd`{.literal} service uses the writable `tdb`{.literal} ID mapping back end by default. It stores Security Identifier (SID), User Identifier (UID), and Group Identifier (GID) mapping tables. This includes local users, groups, and built-in principals.

Use this back end only for the `*`{.literal} default domain. For example:

``` {.language-plaintext tabindex="-1"}
idmap config * : backend = tdb
idmap config * : range = 10000-999999
```

#### [1.4.4. Using the ad ID mapping back end](#using-the-ad-id-mapping-back-end) {#using-the-ad-id-mapping-back-end .title}

You can configure a Samba Active Directory (AD) member to use the `ad`{.literal} ID mapping back end. The `ad`{.literal} ID mapping back end implements a read-only API to read account and group information from AD.

Using the `ad`{.literal} ID mapping back end provides the following benefits:

-   All user and group settings are stored centrally in AD.
-   User and group IDs are consistent on all Samba servers that use this back end.
-   The IDs are not stored in a local database, preventing corruption and loss of file ownership.

Note

The `ad`{.literal} ID mapping back end does not support {AD} domains with one-way trusts. If you configure a domain member in an {AD} with one-way trusts, use instead one of the following ID mapping back ends: `tdb`{.literal}, `rid`{.literal}, or `autorid`{.literal}.

The ad back end reads the following attributes from AD:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------------------+
| AD attribute name                                                                                                                                               | Object type     | Mapped to                                   |
+:================================================================================================================================================================+:================+:============================================+
| `sAMAccountName`{.literal}                                                                                                                                      | User and group  | User or group name, depending on the object |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------------------+
| `uidNumber`{.literal}                                                                                                                                           | User            | User ID (UID)                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------------------+
| `gidNumber`{.literal}                                                                                                                                           | Group           | Group ID (GID)                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------------------+
| `loginShell`{.literal} [^\[a\]^](#ftn.sambaloginshell)                                                                                                          | User            | Path to the shell of the user               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------------------+
| `unixHomeDirectory`{.literal} [^\[a\]^](#ftn.sambaloginshell)                                                                                                   | User            | Path to the home directory of the user      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------------------+
| `primaryGroupID`{.literal} [^\[b\]^](#ftn.samba_primarygroupid)                                                                                                 | User            | Primary group ID                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------------------+
| [^\[a\]^](#sambaloginshell) Samba only reads this attribute if you set `idmap config `{.literal}*`DOMAIN`{.literal}*`:unix_nss_info = yes`{.literal}.           |                 |                                             |
|                                                                                                                                                                 |                 |                                             |
| [^\[b\]^](#samba_primarygroupid) Samba only reads this attribute if you set `idmap config `{.literal}*`DOMAIN`{.literal}*`:unix_primary_group = yes`{.literal}. |                 |                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+---------------------------------------------+

Show more

**Prerequisites**

-   Both users and groups must have unique IDs set in AD, and the IDs must be within the range configured in the `/etc/samba/smb.conf`{.literal} file. Objects with IDs outside this range are not available on the Samba server.
-   Users and groups must have all required attributes set in AD. Missing attributes make the user or group unavailable on the Samba server, depending on the configuration.
-   You installed Samba.
-   The Samba configuration, except ID mapping, exists in the `/etc/samba/smb.conf`{.literal} file.

**Procedure**

1.  Edit the `[global]`{.literal} section in the `/etc/samba/smb.conf`{.literal} file:

    a.  Add an ID mapping configuration for the default domain (`*`{.literal}) if it does not exist. For example:

        ``` {.language-plaintext tabindex="-1"}
        idmap config * : backend = tdb
        idmap config * : range = 10000-999999
        ```

    b.  Enable the `ad`{.literal} ID mapping back end for the AD domain:

        ``` {.language-plaintext tabindex="-1"}
        idmap config DOMAIN : backend = ad
        ```

    c.  Set the range of IDs that is assigned to users and groups in the AD domain. For example:

        ``` {.language-plaintext tabindex="-1"}
        idmap config DOMAIN : range = 2000000-2999999
        ```

        Important

        The range must not overlap with any other domain configuration on this server. Additionally, the range must be set big enough to include all IDs assigned in the future. For further details, see [Planning Samba ID ranges](#planning-samba-id-ranges "1.4.1. Planning Samba ID ranges").

    d.  Set that Samba uses the [RFC 2307](https://tools.ietf.org/html/rfc2307) schema when reading attributes from AD:

        ``` {.language-plaintext tabindex="-1"}
        idmap config DOMAIN : schema_mode = rfc2307
        ```

    e.  To enable Samba to read the login shell and the path to the users home directory from the corresponding AD attribute, set:

        ``` {.language-plaintext tabindex="-1"}
        idmap config DOMAIN : unix_nss_info = yes
        ```

        Alternatively, you can set a uniform domain-wide home directory path and login shell that is applied to all users. For example:

        ``` {.language-plaintext tabindex="-1"}
        template shell = /bin/bash
        template homedir = /home/%U
        ```

    f.  By default, Samba uses the `primaryGroupID`{.literal} attribute of a user object as the user's primary group on Linux. Alternatively, you can configure Samba to use the value set in the `gidNumber`{.literal} attribute instead:

        ``` {.language-plaintext tabindex="-1"}
        idmap config DOMAIN : unix_primary_group = yes
        ```

2.  Verify the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # testparm
    ```

3.  Reload the Samba configuration:

    ``` {.language-plaintext tabindex="-1"}
    # smbcontrol all reload-config
    ```

#### [1.4.5. Using the rid ID mapping back end](#using-the-rid-id-mapping-back-end) {#using-the-rid-id-mapping-back-end .title}

You can configure a Samba domain member to use the `rid`{.literal} ID mapping back end. Samba can use the relative identifier (RID) of a Windows Security Identifier (SID) to generate an ID on Red Hat Enterprise Linux.

Note

The RID is the last part of a SID. For example, if the SID of a user is `S-1-5-21-5421822485-1151247151-421485315-30014`{.literal}, then `30014`{.literal} is the corresponding RID.

The `rid`{.literal} ID mapping back end implements a read-only API to calculate account and group information based on an algorithmic mapping scheme for AD and NT4 domains. When you configure the back end, you must set the lowest and highest RID in the `idmap config `{.literal}*`DOMAIN`{.literal}*` : `{.literal}*`range`{.literal}* parameter. Samba does not map users or groups with a lower or higher RID than set in this parameter.

Important

As a read-only back end, `rid`{.literal} cannot assign new IDs, such as for `BUILTIN`{.literal} groups. Therefore, do not use this back end for the `*`{.literal} default domain.

**Benefits of using the rid back end**

-   All domain users and groups that have an RID within the configured range are automatically available on the domain member.
-   You do not need to manually assign IDs, home directories, and login shells.

**Drawbacks of using the rid back end**

-   All domain users get the same login shell and home directory assigned. However, you can use variables.
-   User and group IDs are only the same across Samba domain members if all use the `rid`{.literal} back end. They must also have the same ID range settings.
-   You cannot exclude individual users or groups from being available on the domain member. Only users and groups outside of the configured range are excluded.
-   Duplicate IDs can occur in multi-domain environments if objects in different domains have the same RID. This is based on the formulas winbindd uses to calculate IDs.

**Prerequisites**

-   You installed Samba.
-   The Samba configuration, except ID mapping, exists in the `/etc/samba/smb.conf`{.literal} file.

**Procedure**

1.  Edit the `[global]`{.literal} section in the `/etc/samba/smb.conf`{.literal} file:

    a.  Add an ID mapping configuration for the default domain (`*`{.literal}) if it does not exist. For example:

        ``` {.language-plaintext tabindex="-1"}
        idmap config * : backend = tdb
        idmap config * : range = 10000-999999
        ```

    b.  Enable the `rid`{.literal} ID mapping back end for the domain:

        ``` {.language-plaintext tabindex="-1"}
        idmap config DOMAIN : backend = rid
        ```

    c.  Set a range that is big enough to include all RIDs that will be assigned in the future. For example:

        ``` {.language-plaintext tabindex="-1"}
        idmap config DOMAIN : range = 2000000-2999999
        ```

        Samba ignores users and groups whose RIDs in this domain are not within the range.

        Important

        The range must not overlap with any other domain configuration on this server. Additionally, the range must be set big enough to include all IDs assigned in the future.

    d.  Set a shell and home directory path that will be assigned to all mapped users. For example:

        ``` {.language-plaintext tabindex="-1"}
        template shell = /bin/bash
        template homedir = /home/%U
        ```

2.  Verify the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # testparm
    ```

3.  Reload the Samba configuration:

    ``` {.language-plaintext tabindex="-1"}
    # smbcontrol all reload-config
    ```

    For more information, see:

    -   `VARIABLE SUBSTITUTIONS`{.literal} section in the `smb.conf(5)`{.literal} man page on your system
    -   Calculation of the local ID from a RID, see the `idmap_rid(8)`{.literal} man page on your system

**Additional resources**

-   [Planning Samba ID ranges](#planning-samba-id-ranges "1.4.1. Planning Samba ID ranges")
-   [The \* default domain](#the-asterisk-default-domain "1.4.2. The * default domain")

#### [1.4.6. Using the autorid ID mapping back end](#using-the-autorid-id-mapping-back-end) {#using-the-autorid-id-mapping-back-end .title}

You can configure a Samba domain member to use the `autorid`{.literal} ID mapping back end. The `autorid`{.literal} back end works similarly to the `rid`{.literal} ID mapping back end, but automatically assigns IDs for different domains.

The `autorid`{.literal} ID mapping back end supports the following deployment scenarios:

-   Only for the `*`{.literal} default domain
-   For the `*`{.literal} default domain and additional domains, without the need to create ID mapping configurations for each of the additional domains
-   Only for specific domains

Note

If you use `autorid`{.literal} for the default domain, adding additional ID mapping configuration for domains is optional.

Parts of this section were adopted from the [idmap config autorid](https://wiki.samba.org/index.php/Idmap_config_autorid) documentation published in the Samba Wiki. License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Authors and contributors: See the [history](https://wiki.samba.org/index.php?title=Idmap_config_autorid&action=history) tab on the Wiki page.

**Benefits of using the autorid back end**

-   All domain users and groups whose calculated User Identifier (UID) and Group Identifier (GID) are within the configured range are available. They are automatically available on the domain member.
-   You do not need to manually assign IDs, home directories, and login shells.
-   No duplicate IDs, even if multiple objects in a multi-domain environment have the same Relative Identifier (RID).

**Drawbacks**

-   User and group IDs are not the same across Samba domain members.
-   All domain users get the same login shell and home directory assigned. However, you can use variables.
-   You cannot exclude individual users or groups from being available on the domain member. Only users and groups whose calculated UID or GID is outside of the configured range are excluded.

**Prerequisites**

-   You installed Samba.
-   The Samba configuration, except ID mapping, exists in the `/etc/samba/smb.conf`{.literal} file.

**Procedure**

1.  Edit the `[global]`{.literal} section in the `/etc/samba/smb.conf`{.literal} file:

    a.  Enable the `autorid`{.literal} ID mapping back end for the `*`{.literal} default domain:

        ``` {.language-plaintext tabindex="-1"}
        idmap config * : backend = autorid
        ```

    b.  Set a range that is big enough to assign IDs for all existing and future objects. For example:

        ``` {.language-plaintext tabindex="-1"}
        idmap config * : range = 10000-999999
        ```

        Samba ignores users and groups whose calculated IDs in this domain are not within the range.

        Warning

        After you set the range and Samba starts using it, you can only increase the upper limit of the range. Any other change to the range can result in new ID assignments, and thus in losing file ownerships.

    c.  Optional: Set a range size. For example:

        ``` {.language-plaintext tabindex="-1"}
        idmap config * : rangesize = 200000
        ```

        Samba assigns this number of continuous IDs for each domain's object until all IDs from the range set in the `idmap config * : `{.literal}*`range`{.literal}* parameter are taken.

        Note

        If you set a rangesize, you need to adapt the range accordingly. The range needs to be a multiple of the rangesize.

    d.  Set a shell and home directory path that will be assigned to all mapped users. For example:

        ``` {.language-plaintext tabindex="-1"}
        template shell = /bin/bash
        template homedir = /home/%U
        ```

    e.  Optional: Add additional ID mapping configuration for domains. If no configuration for an individual domain is available, Samba calculates the ID using the `autorid`{.literal} back end settings in the previously configured `*`{.literal} default domain.

        Important

        The range must not overlap with any other domain configuration on this server. Additionally, the range must be set big enough to include all IDs assigned in the future. For further details, see [Planning Samba ID ranges](#planning-samba-id-ranges "1.4.1. Planning Samba ID ranges").

2.  Verify the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # testparm
    ```

3.  Reload the Samba configuration:

    ``` {.language-plaintext tabindex="-1"}
    # smbcontrol all reload-config
    ```

    For more information, see:

    -   `THE MAPPING FORMULAS`{.literal} section in the `idmap_autorid(8)`{.literal} man page on your system
    -   `rangesize`{.literal} parameter description in the `idmap_autorid(8)`{.literal} man page on your system
    -   `VARIABLE SUBSTITUTIONS`{.literal} section in the `smb.conf(5)`{.literal} man page on your system

### [1.5. Setting up Samba as an AD domain member server](#setting-up-samba-as-an-ad-domain-member-server) {#setting-up-samba-as-an-ad-domain-member-server .title}

If you are running an AD or NT4 domain, use Samba to add your Red Hat Enterprise Linux server as a member to the domain.

This helps you to gain the following:

-   Access domain resources on other domain members
-   Authenticate domain users to local services, such as `sshd`{.literal}
-   Share directories and printers hosted on the server to act as a file and print server

#### [1.5.1. Joining a RHEL system to an AD domain](#joining-a-rhel-system-to-an-ad-domain) {#joining-a-rhel-system-to-an-ad-domain .title}

Samba Winbind is an alternative to the System Security Services Daemon (SSSD). It connects a Red Hat Enterprise Linux (RHEL) system with Active Directory (AD). You can join a RHEL system to an AD domain by using `realmd`{.literal} to configure Samba Winbind.

**Procedure**

1.  If your AD requires the deprecated RC4 encryption type for Kerberos authentication, enable support for these ciphers in RHEL:

    ``` {.language-plaintext tabindex="-1"}
    # update-crypto-policies --set DEFAULT:AD-SUPPORT
    ```

2.  Install the following packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install realmd oddjob-mkhomedir oddjob samba-winbind-clients \
           samba-winbind samba-common-tools samba-winbind-krb5-locator krb5-workstation
    ```

3.  To share directories or printers on the domain member, install the `samba`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install samba
    ```

4.  Backup the existing `/etc/samba/smb.conf`{.literal} Samba configuration file:

    ``` {.language-plaintext tabindex="-1"}
    # mv /etc/samba/smb.conf /etc/samba/smb.conf.bak
    ```

5.  Join the domain. For example, to join a domain named `ad.example.com`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # realm join --membership-software=samba --client-software=winbind ad.example.com
    ```

    Using the previous command, the `realm`{.literal} utility automatically:

    -   Creates a `/etc/samba/smb.conf`{.literal} file for a membership in the `ad.example.com`{.literal} domain
    -   Adds the `winbind`{.literal} module for user and group lookups to the `/etc/nsswitch.conf`{.literal} file
    -   Updates the Pluggable Authentication Module (PAM) configuration files in the `/etc/pam.d/`{.literal} directory
    -   Starts the `winbind`{.literal} service and enables the service to start when the system boots

6.  Optional: Set an alternative ID mapping back end or customized ID mapping settings in the `/etc/samba/smb.conf`{.literal} file.

    For details, see [Understanding and configuring Samba ID mapping](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#understanding-and-configuring-samba-id-mapping).

7.  Edit the `/etc/krb5.conf`{.literal} file and add the following section:

    ``` {.language-plaintext tabindex="-1"}
    [plugins]
        localauth = {
            module = winbind:/usr/lib64/samba/krb5/winbind_krb5_localauth.so
            enable_only = winbind
        }
    ```

8.  Verify that the `winbind`{.literal} service is running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status winbind
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
        Active: active (running) since Tue 2018-11-06 19:10:40 CET; 15s ago
    ```

    Important

    To enable Samba to query domain user and group information, the `winbind`{.literal} service must be running before you start `smb`{.literal}.

9.  If you installed the `samba`{.literal} package to share directories and printers, enable and start the `smb`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now smb
    ```

10. If you are authenticating local logins to {AD}, enable the `winbind_krb5_localauth`{.literal} plug-in. See [Using the local authorization plug-in for MIT Kerberos](#using-the-local-authorization-plug-in-for-mit-kerberos "1.5.2. Using the local authorization plug-in for MIT Kerberos").

**Verification**

1.  Display an AD user's details, such as the AD administrator account in the AD domain:

    ``` {.language-plaintext tabindex="-1"}
    # getent passwd "AD\administrator"
    ```

    ``` {.language-plaintext tabindex="-1"}
    AD\administrator:*:10000:10000::/home/administrator@AD:/bin/bash
    ```

2.  Query the members of the domain users group in the AD domain:

    ``` {.language-plaintext tabindex="-1"}
    # getent group "AD\Domain Users"
    ```

    ``` {.language-plaintext tabindex="-1"}
    AD\domain users:x:10000:user1,user2
    ```

3.  Optional: Verify that you can use domain users and groups when you set permissions on files and directories. For example, to set the owner of the `/srv/samba/example.txt`{.literal} file to `AD\administrator`{.literal} and the group to `AD\Domain Users`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # chown "AD\administrator":"AD\Domain Users" /srv/samba/example.txt
    ```

4.  Verify that Kerberos authentication works as expected:

    a.  On the AD domain member, obtain a ticket for the `administrator@AD.EXAMPLE.COM`{.literal} principal:

        ``` {.language-plaintext tabindex="-1"}
        # kinit administrator@AD.EXAMPLE.COM
        ```

    b.  Display the cached Kerberos ticket:

        ``` {.language-plaintext tabindex="-1"}
        # klist
        ```

        ``` {.language-plaintext tabindex="-1"}
        Ticket cache: KCM:0
        Default principal: administrator@AD.EXAMPLE.COM

        Valid starting       Expires              Service principal
        01.11.2018 10:00:00  01.11.2018 20:00:00  krbtgt/AD.EXAMPLE.COM@AD.EXAMPLE.COM
                renew until 08.11.2018 05:00:00
        ```

5.  Display the available domains:

    ``` {.language-plaintext tabindex="-1"}
    # wbinfo --all-domains
    ```

    ``` {.language-plaintext tabindex="-1"}
    BUILTIN
    SAMBA-SERVER
    AD
    ```

If you do not want to use the deprecated RC4 ciphers, you can enable the AES encryption type in AD. See [Enabling the AES encryption type in Active Directory using a GPO](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_trust_between_idm_and_ad/ensuring-support-for-common-encryption-types-in-ad-and-rhel#enabling-the-aes-encryption-type-in-active-directory-using-a-gpo).

#### [1.5.2. Using the local authorization plug-in for MIT Kerberos](#using-the-local-authorization-plug-in-for-mit-kerberos) {#using-the-local-authorization-plug-in-for-mit-kerberos .title}

The `winbind`{.literal} service provides {AD} users to a domain member. To authenticate domain users to local services, use the `winbind_krb5_localauth`{.literal} plug-in. This maps Kerberos principals to {AD} accounts through `winbind`{.literal}.

Authentication can fail when Kerberos and {AD} use different account name formats. Consider an {AD} user with the sAMAccountName attribute is set to `EXAMPLE`{.literal}. If the user tries to log in with the lowercase user name, Kerberos returns the user name in uppercase. As a consequence, the entries do not match and authentication fails.

Using the `winbind_krb5_localauth`{.literal} plug-in, the account names are mapped correctly. Note that this only applies to GSSAPI authentication and not for getting the initial ticket granting ticket (TGT).

**Prerequisites**

-   Samba is configured as a member of an {AD}.
-   Red Hat Enterprise Linux authenticates log in attempts against {AD}.
-   The `winbind`{.literal} service is running.

**Procedure**

-   Edit the `/etc/krb5.conf`{.literal} file and add the following section:

    ``` {.language-plaintext tabindex="-1"}
    [plugins]
    localauth = {
         module = winbind:/usr/lib64/samba/krb5/winbind_krb5_localauth.so
         enable_only = winbind
    }
    ```

    For more information, see the `winbind_krb5_localauth(8)`{.literal} man page on your system.

#### [1.5.3. Enabling certificate auto-enrollment on a Samba client](#enabling-certificate-auto-enrollment-on-a-samba-client) {#enabling-certificate-auto-enrollment-on-a-samba-client .title}

Enable certificate auto-enrollment on a Samba client to automate certificate requests and renewals from an Active Directory (AD) certificate authority (CA). This feature helps you prevent outages by managing certificates without manual monitoring or user interaction.

Certificate auto-enrollment is available if an AD provides a certificate authority (CA) and a RHEL host is a member of the AD. Enable this feature on the RHEL host. Samba then applies the auto-enrollment group policy from AD, and configures the `certmonger`{.literal} service to request and manage certificates.

**Prerequisites**

-   [Samba is configured as a member of an AD](#joining-a-rhel-system-to-an-ad-domain "1.5.1. Joining a RHEL system to an AD domain").

-   A Windows server in the AD has the **Active Directory Certificate Services** server role with the following services installed:

    -   Certificate Authority
    -   Certificate Enrollment
    -   Policy Web Service

-   Internet Information Services (ISS) is configured to provide the certificate auto-enrollment feature over HTTPS.

-   ISS uses a certificate issued by the AD CA.

-   The Certificate Enrollment service supports Kerberos Authentication.

-   A group policy object (GPO) for certificate auto-enrollment is configured in AD.

**Procedure**

1.  Install the `samba-gpupdate`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install samba-gpupdate
    ```

2.  Append the following settings to the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    kerberos method = secrets and keytab
    sync machine password to keytab = "/etc/krb5.keytab:account_name:sync_spns:spn_prefixes=host:sync_kvno:machine_password", "/etc/samba/cepces.keytab:account_name:machine_password"
    apply group policies = yes
    ```

    The settings specified in the Samba configuration include the following configuration:

    `kerberos method = secrets and keytab`{.literal}
    :   Configures Samba to use the `/var/lib/samba/private/secrets.tdb`{.literal} file first to verify Kerberos tickets and then the `/etc/krb5.keytab`{.literal} file.

    `sync machine password to keytab = `{.literal}*`<list_of_keytab_files_and_their_principals>`{.literal}*
    :   Defines paths to keytab files that Samba maintains and the Kerberos principals in these files. With the shown value, Samba continues maintaining the `/etc/krb5.keytab`{.literal} system keytab and, additionally, a `/etc/samba/cepces.keytab`{.literal} file. The `cepces-submit`{.literal} submission helper for `certmonger`{.literal} uses this file to authenticate to the CA.

    `apply group policies = yes`{.literal}
    :   Configures the `winbind`{.literal} service to run the `gpupdate`{.literal} command in intervals. The update interval is 90 minutes, plus a random offset between 0 and 30 minutes.

3.  Create the `/etc/samba/cepces.keytab`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # net ads keytab create
    ```

4.  Edit the `/etc/cepces/cepces.conf`{.literal} file, and make the following changes:

    a.  In the `[global]`{.literal} section, set the `server`{.literal} variable to the fully-qualified domain name (FQDN) of the Windows server running the CA service:

        ``` {.language-plaintext tabindex="-1"}
        [global]
        server=win-server.ad.example.com
        ```

    b.  In the `[kerberos]`{.literal} section, set the `keytab`{.literal} variable to `/etc/samba/cepces.keytab`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        [kerberos]
        keytab=/etc/samba/cepces.keytab
        ```

5.  Enable and start the `certmonger`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now certmonger
    ```

    The `certmonger`{.literal} service requests the certificates from the CA and automatically renews them before they expire.

6.  Manually run `samba-gpupdate`{.literal} to ensure that the group policies have been loaded from AD:

    ``` {.language-plaintext tabindex="-1"}
    # samba-gpupdate
    ```

7.  The `certmonger`{.literal} service stores the keys and certificates in the following directories:

    -   Private keys: `/var/lib/samba/private/certs/`{.literal}

    -   Issued certificates: `/var/lib/samba/certs/`{.literal}

        You can now start using the keys and certificates in services on the same host.

8.  Optional: Display the certificates that `certmonger`{.literal} manages:

    ``` {.language-plaintext tabindex="-1"}
    # getcert list
    ```

    ``` {.language-plaintext tabindex="-1"}
    Number of certificates and requests being tracked: 1.
    Request ID 'AD-ROOT-CA.Machine':
        status: MONITORING
        stuck: no
        key pair storage: type=FILE,location='/var/lib/samba/private/certs/AD-ROOT-CA.Machine.key'
        certificate: type=FILE,location='/var/lib/samba/certs/AD-ROOT-CA.Machine.crt'
        CA: AD-ROOT-CA
        issuer: CN=AD-ROOT-CA,DC=ad,DC=example,DC=com
        subject: CN=rhel9.ad.example.com
        issued: 2025-03-25 14:22:07 CET
        expires: 2026-03-25 14:22:07 CET
        dns: rhel9.ad.example.com
        key usage: digitalSignature,keyEncipherment
        eku: id-kp-clientAuth,id-kp-serverAuth
        certificate template/profile: Machine
        profile: Machine
        pre-save command:
        post-save command:
        track: yes
        auto-renew: yes
    ```

    By default, the Windows CA issues only a certificate by using the `Machine`{.literal} certificate template. If you configured additional templates in the Windows CA that apply for this host, `certmonger`{.literal} requests certificates for these templates. The `getcert list`{.literal} output also includes entries for them.

### [1.6. Setting up Samba on an IdM domain member](#setting-up-samba-on-an-idm-domain-member) {#setting-up-samba-on-an-idm-domain-member .title}

You can configure Samba on a host that is joined to a Red Hat Identity Management (IdM) domain. Users from IdM and also, if available, from trusted Active Directory (AD) domains, can access shares and printer services provided by Samba.

Important

Using Samba on an IdM domain member is an unsupported Technology Preview feature and contains certain limitations. For example, IdM trust controllers do not support the Active Directory Global Catalog service. They also do not support resolving IdM groups by using the Distributed Computing Environment / Remote Procedure Calls (DCE/RPC) protocols. As a consequence, AD users can only access Samba shares and printers hosted on IdM clients when logged in to other IdM clients. AD users logged into a Windows machine cannot access Samba shares hosted on an IdM domain member.

Customers deploying Samba on IdM domain members are encouraged to provide feedback to Red Hat.

If users from AD domains access shares and printer services by Samba, ensure Advanced Encryption Standard (AES) is enabled in AD.

#### [1.6.1. Prerequisites](#prerequisites) {#prerequisites .title}

-   The host is joined as a client to the IdM domain.
-   Both the IdM servers and the client must run on RHEL 10.

#### [1.6.2. Preparing the IdM domain for installing Samba on domain members](#preparing-the-idm-domain-for-installing-samba-on-domain-members) {#preparing-the-idm-domain-for-installing-samba-on-domain-members .title}

Before you can configure Samba on an IdM client, you must prepare the IdM domain by using the `ipa-adtrust-install`{.literal} utility on an IdM server.

Any system where you run the `ipa-adtrust-install`{.literal} command automatically becomes an AD trust controller. However, you must run `ipa-adtrust-install`{.literal} only once on an IdM server.

**Prerequisites**

-   IdM server is installed.
-   You have root privileges to install packages and restart IdM services.

**Procedure**

1.  Install the required packages:

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# dnf install ipa-server-trust-ad samba-client
    ```

2.  Authenticate as the IdM administrative user:

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# kinit admin
    ```

3.  Run the `ipa-adtrust-install`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# ipa-adtrust-install
    ```

    The DNS service records are created automatically if IdM was installed with an integrated DNS server.

    If you installed IdM without an integrated DNS server, `ipa-adtrust-install`{.literal} prints a list of service records that you must manually add to DNS before you can continue.

4.  The script prompts you that the `/etc/samba/smb.conf`{.literal} already exists and will be rewritten:

    ``` {.language-plaintext tabindex="-1"}
    WARNING: The smb.conf already exists. Running ipa-adtrust-install will break your existing Samba configuration.

    Do you wish to continue? [no]: yes
    ```

5.  The script prompts you to configure the `slapi-nis`{.literal} plug-in, a compatibility plug-in that allows older Linux clients to work with trusted users:

    ``` {.language-plaintext tabindex="-1"}
    Do you want to enable support for trusted domains in Schema Compatibility plugin?
    This will allow clients older than SSSD 1.9 and non-Linux clients to work with trusted users.

    Enable trusted domains support in slapi-nis? [no]: yes
    ```

6.  You are prompted to run the SID generation task to create a SID for any existing users:

    ``` {.language-plaintext tabindex="-1"}
    Do you want to run the ipa-sidgen task? [no]: yes
    ```

    This is a resource-intensive task, so if you have a high number of users, you can run this at another time.

7.  Optional: By default, the Dynamic RPC port range is defined as `49152-65535`{.literal} for Windows Server 2008 and later. If you need to define a different Dynamic RPC port range for your environment, configure Samba to use different ports and open those ports in your firewall settings. The following example sets the port range to `55000-65000`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# net conf setparm global 'rpc server dynamic port range' 55000-65000
    [root@ipaserver ~]# firewall-cmd --add-port=55000-65000/tcp
    [root@ipaserver ~]# firewall-cmd --runtime-to-permanent
    ```

8.  Restart the `ipa`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# ipactl restart
    ```

9.  Use the `smbclient`{.literal} utility to verify that Samba responds to Kerberos authentication from the IdM side:

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# smbclient -L ipaserver.idm.example.com -U user_name --use-kerberos=required
    ```

    ``` {.language-plaintext tabindex="-1"}
    lp_load_ex: changing to config backend registry
        Sharename       Type      Comment
        ---------       ----      -------
        IPC$            IPC       IPC Service (Samba 4.15.2)
    ...
    ```

#### [1.6.3. Installing and configuring a Samba server on an IdM client](#installing-and-configuring-a-samba-server-on-an-idm-client) {#installing-and-configuring-a-samba-server-on-an-idm-client .title}

You can install and configure Samba on an IdM client to securely share files with integrated authentication. This leverages IdM domain accounts for access. Ensure proper prerequisites and configuration to enable seamless resource sharing across your network.

**Prerequisites**

-   Both the IdM servers and the client must run on RHEL 10 or later.
-   The IdM domain is prepared as described in [Preparing the IdM domain for installing Samba on domain members](#preparing-the-idm-domain-for-installing-samba-on-domain-members "1.6.2. Preparing the IdM domain for installing Samba on domain members").
-   If IdM has a trust configured with AD, enable the AES encryption type for Kerberos. For example, use a group policy object (GPO) to enable the AES encryption type. For details, see [Enabling AES encryption in Active Directory using a GPO](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_trust_between_idm_and_ad/ensuring-support-for-common-encryption-types-in-ad-and-rhel#enabling-the-aes-encryption-type-in-active-directory-using-a-gpo).

**Procedure**

1.  Install the `ipa-client-samba`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    [root@idm_client]# dnf install ipa-client-samba
    ```

2.  Use the `ipa-client-samba`{.literal} utility to prepare the client and create an initial Samba configuration:

    ``` {.language-plaintext tabindex="-1"}
    [root@idm_client]# ipa-client-samba
    ```

    ``` {.language-plaintext tabindex="-1"}
    Searching for IPA server...
    IPA server: DNS discovery
    Chosen IPA master: idm_server.idm.example.com
    SMB principal to be created: cifs/idm_client.idm.example.com@IDM.EXAMPLE.COM
    NetBIOS name to be used: IDM_CLIENT
    Discovered domains to use:

     Domain name: idm.example.com
    NetBIOS name: IDM
             SID: S-1-5-21-525930803-952335037-206501584
        ID range: 212000000 - 212199999

     Domain name: ad.example.com
    NetBIOS name: AD
             SID: None
        ID range: 1918400000 - 1918599999

    Continue to configure the system with these values? [no]: yes
    Samba domain member is configured. Please check configuration at /etc/samba/smb.conf and start smb and winbind services
    ```

3.  By default, `ipa-client-samba`{.literal} automatically adds the `[homes]`{.literal} section to the `/etc/samba/smb.conf`{.literal} file. This section dynamically shares the home directory of a user when the user connects. If users do not have home directories on this server, or you do not want to share them, remove these from `/etc/samba/smb.conf`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [homes]
        read only = no
    ```

4.  Share directories and printers. For details, see:

    -   [Setting up a Samba file share that uses POSIX ACLs](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-a-samba-file-share-that-uses-posix-acls)
    -   [Setting up a share that uses Windows ACLs](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-a-share-that-uses-windows-acls)
    -   [Setting up Samba as a print server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-samba-as-a-print-server)

5.  Open the ports required for a Samba client in the local firewall:

    ``` {.language-plaintext tabindex="-1"}
    [root@idm_client]# firewall-cmd --permanent --add-service=samba-client
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@idm_client]# firewall-cmd --reload
    ```

6.  Enable and start the `smb`{.literal} and `winbind`{.literal} services:

    ``` {.language-plaintext tabindex="-1"}
    [root@idm_client]# systemctl enable --now smb winbind
    ```

    Note

    Do not start the `nmbd`{.literal} service. When using Samba with Active Directory, NetBIOS is not required for interoperability --- DNS handles name resolution in AD environments.

**Verification**

-   Run the following verification step on a different IdM domain member that has the `samba-client`{.literal} package installed:

    -   List the shares on the Samba server using Kerberos authentication:

        ``` {.language-plaintext tabindex="-1"}
        $ smbclient -L idm_client.idm.example.com -U user_name --use-kerberos=required
        ```

        ``` {.language-plaintext tabindex="-1"}
        lp_load_ex: changing to config backend registry

            Sharename       Type      Comment
            ---------       ----      -------
            example         Disk
            IPC$            IPC       IPC Service (Samba 4.15.2)
        ...
        ```

        For more information, see the `ipa-client-samba(1)`{.literal} man page on your system.

#### [1.6.4. Manually adding an ID mapping configuration if IdM trusts a new domain](#manually-adding-an-id-mapping-configuration-if-idm-trusts-a-new-domain) {#manually-adding-an-id-mapping-configuration-if-idm-trusts-a-new-domain .title}

Samba requires an ID mapping configuration for each domain that accesses resources. On an existing Samba server running on an IdM client, manually add the configuration. Do this after adding a new trust to an AD domain.

**Prerequisites**

-   You configured Samba on an IdM client. Afterward, a new trust was added to IdM.
-   The Data Encryption Standard (DES) and RC4 encryption types for Kerberos must be disabled in the trusted AD domain. For security reasons, RHEL 10 does not support these weak encryption types.

**Procedure**

1.  Authenticate by using the host's keytab:

    ``` {.language-plaintext tabindex="-1"}
    [root@idm_client]# kinit -k
    ```

2.  Use the `ipa idrange-find`{.literal} command to display both the base ID and the ID range size of the new domain. For example, the following command displays the values for the `ad.example.com`{.literal} domain:

    ``` {.language-plaintext tabindex="-1"}
    [root@idm_client]# ipa idrange-find --name="AD.EXAMPLE.COM_id_range" --raw
    ```

    ``` {.language-plaintext tabindex="-1"}
    ---------------
    1 range matched
    ---------------
      cn: AD.EXAMPLE.COM_id_range
      ipabaseid: 1918400000
      ipaidrangesize: 200000
      ipabaserid: 0
      ipanttrusteddomainsid: S-1-5-21-968346183-862388825-1738313271
      iparangetype: ipa-ad-trust
    ----------------------------
    Number of entries returned 1
    ----------------------------
    ```

    You need the values from the `ipabaseid`{.literal} and `ipaidrangesize`{.literal} attributes in the next steps.

3.  To calculate the highest usable ID, use the following formula:

    ``` {.language-plaintext tabindex="-1"}
    maximum_range = ipabaseid + ipaidrangesize - 1
    ```

    With the values from the previous step, the highest usable ID for the `ad.example.com`{.literal} domain is `1918599999`{.literal} (1918400000 + 200000 - 1).

4.  Edit the `/etc/samba/smb.conf`{.literal} file, and add the ID mapping configuration for the domain to the `[global]`{.literal} section:

    ``` {.language-plaintext tabindex="-1"}
    idmap config AD : range = 1918400000 - 1918599999
    idmap config AD : backend = sss
    ```

    Specify the value from `ipabaseid`{.literal} attribute as the lowest and the computed value from the previous step as the highest value.

5.  Restart the `smb`{.literal} and `winbind`{.literal} services:

    ``` {.language-plaintext tabindex="-1"}
    [root@idm_client]# systemctl restart smb winbind
    ```

**Verification**

-   List the shares on the Samba server using Kerberos authentication:

    ``` {.language-plaintext tabindex="-1"}
    $ smbclient -L idm_client.idm.example.com -U user_name --use-kerberos=required
    ```

    ``` {.language-plaintext tabindex="-1"}
    lp_load_ex: changing to config backend registry

        Sharename       Type      Comment
        ---------       ----      -------
        example         Disk
        IPC$            IPC       IPC Service (Samba 4.15.2)
    ...
    ```

#### [1.6.5. Additional resources](#setting-up-samba-on-an-idm-domain-member_165-additional-resources) {#additional-resources .title}

-   [Installing an Identity Management client](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-idm-client)
-   [Enabling the AES encryption type in Active Directory using a GPO](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_trust_between_idm_and_ad/ensuring-support-for-common-encryption-types-in-ad-and-rhel#enabling-the-aes-encryption-type-in-active-directory-using-a-gpo)

### [1.7. Setting up a Samba file share that uses POSIX ACLs](#setting-up-a-samba-file-share-that-uses-posix-acls) {#setting-up-a-samba-file-share-that-uses-posix-acls .title}

Samba supports shares with POSIX Access Control Lists (ACLs). Manage permissions locally on the Samba server by using utilities such as `chmod`{.literal}. On file systems with extended attributes, ACLs can include multiple users and groups.

Note

You can also use fine-granular Windows ACLs instead.

#### [1.7.1. Adding a share that uses POSIX ACLs](#adding-a-share-that-uses-posix-acls) {#adding-a-share-that-uses-posix-acls .title}

You can create a share named `example`{.literal} that provides the content of the `/srv/samba/example/`{.literal} directory and uses POSIX ACLs.

**Prerequisites**

Samba has been set up in one of the following modes:

-   [Standalone server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-samba-as-a-standalone-server)
-   [Domain member](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-samba-as-an-ad-domain-member-server)

**Procedure**

1.  Create the directory if it does not exist. For example:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir -p /srv/samba/example/
    ```

2.  If you run SELinux in `enforcing`{.literal} mode, set the `samba_share_t`{.literal} context on the directory:

    ``` {.language-plaintext tabindex="-1"}
    # semanage fcontext -a -t samba_share_t "/srv/samba/example(/.*)?"
    ```

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Rv /srv/samba/example/
    ```

3.  Set file system ACLs on the directory. For details, see:

    -   [Setting standard ACLs on a Samba Share that uses POSIX ACLs](#setting-standard-linux-acls-on-a-samba-share-that-uses-posix-acls "1.7.2. Setting standard Linux ACLs on a Samba share that uses POSIX ACLs")
    -   [Setting extended ACLs on a share that uses POSIX ACLs](#setting-extended-acls-on-a-samba-share-that-uses-posix-acls "1.7.3. Setting extended ACLs on a Samba share that uses POSIX ACLs").

4.  Add the example share to the `/etc/samba/smb.conf`{.literal} file. For example, to add the share write-enabled:

    ``` {.language-plaintext tabindex="-1"}
    [example]
        path = /srv/samba/example/
        read only = no
    ```

    Note

    Regardless of the file system ACLs; if you do not set `read only = no`{.literal}, Samba shares the directory in read-only mode.

5.  Verify the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # testparm
    ```

6.  Open the required ports and reload the firewall configuration by using the `firewall-cmd`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=samba
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

7.  Restart the `smb`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart smb
    ```

#### [1.7.2. Setting standard Linux ACLs on a Samba share that uses POSIX ACLs](#setting-standard-linux-acls-on-a-samba-share-that-uses-posix-acls) {#setting-standard-linux-acls-on-a-samba-share-that-uses-posix-acls .title}

The standard ACLs on Linux support setting permissions for one owner, one group, and for all other undefined users. You can use the `chown`{.literal}, `chgrp`{.literal}, and `chmod`{.literal} utility to update the ACLs. If you require precise control, use the more complex POSIX ACLs.

The following procedure sets the owner of the `/srv/samba/example/`{.literal} directory to the `root`{.literal} user. It grants read and write permissions to the `Domain Users`{.literal} group, and denies access to all other users.

**Prerequisites**

-   The Samba share on which you want to set the ACLs exists.

**Procedure**

-   Run the following command to initialize the process:

    ``` {.language-plaintext tabindex="-1"}
    # chown root:"Domain Users" /srv/samba/example/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # chmod 2770 /srv/samba/example/
    ```

    Note

    Enabling the set-group-ID (SGID) bit on a directory automatically sets the default group to the directory group. This applies to all new files and subdirectories. It differs from the usual behavior of setting it to the primary group of the user who created the new directory entry.

#### [1.7.3. Setting extended ACLs on a Samba share that uses POSIX ACLs](#setting-extended-acls-on-a-samba-share-that-uses-posix-acls) {#setting-extended-acls-on-a-samba-share-that-uses-posix-acls .title}

If the file system the shared directory is stored on supports extended ACLs, you can use them to set complex permissions. Extended ACLs can contain permissions for multiple users and groups.

Extended POSIX ACLs enable you to configure complex ACLs with multiple users and groups. However, you can only set the following permissions:

-   No access
-   Read access
-   Write access
-   Full control

If you require the fine-granular Windows permissions, such as `Create folder / append data`{.literal}, configure the share to use Windows ACLs. See [Setting up a share that uses Windows ACLs](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-a-share-that-uses-windows-acls).

The following procedure shows how to enable extended ACLs on a share. Additionally, it contains an example about setting extended ACLs.

**Prerequisites**

-   The Samba share on which you want to set the ACLs exists.

**Procedure**

1.  Enable the following parameter in the share's section in the `/etc/samba/smb.conf`{.literal} file to enable ACL inheritance of extended ACLs:

    ``` {.language-plaintext tabindex="-1"}
    inherit acls = yes
    ```

    For details, see the parameter description in the `smb.conf(5`{.literal}) man page.

2.  Restart the `smb`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart smb
    ```

3.  Set the ACLs on the directory. For example:

**Example 1.2. Setting Extended ACLs**

The following procedure sets read, write, and execute permissions for the `Domain Admins`{.literal} group, read, and execute permissions for the `Domain Users`{.literal} group, and deny access to everyone else on the `/srv/samba/example/`{.literal} directory:

1.  Disable auto-granting permissions to the primary group of user accounts:

    ``` {.language-plaintext tabindex="-1"}
    # setfacl -m group::--- /srv/samba/example/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # setfacl -m default:group::--- /srv/samba/example/
    ```

    The primary group of the directory is additionally mapped to the dynamic `CREATOR GROUP`{.literal} principal. When you use extended POSIX ACLs on a Samba share, this principal is automatically added and you cannot remove it.

2.  Set the permissions on the directory:

    a.  Grant read, write, and execute permissions to the `Domain Admins`{.literal} group:

        ``` {.language-plaintext tabindex="-1"}
        # setfacl -m group:"DOMAIN\Domain Admins":rwx /srv/samba/example/
        ```

    b.  Grant read and execute permissions to the `Domain Users`{.literal} group:

        ``` {.language-plaintext tabindex="-1"}
        # setfacl -m group:"DOMAIN\Domain Users":r-x /srv/samba/example/
        ```

    c.  Set permissions for the `other`{.literal} ACL entry to deny access to users that do not match the other ACL entries:

        ``` {.language-plaintext tabindex="-1"}
        # setfacl -R -m other::--- /srv/samba/example/
        ```

    These settings apply only to this directory. In Windows, these ACLs are mapped to the `This folder only`{.literal} mode.

3.  To enable the permissions set in the previous step to be inherited by new file system objects created in this directory:

    ``` {.language-plaintext tabindex="-1"}
    # setfacl -m default:group:"DOMAIN\Domain Admins":rwx /srv/samba/example/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # setfacl -m default:group:"DOMAIN\Domain Users":r-x /srv/samba/example/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # setfacl -m default:other::--- /srv/samba/example/
    ```

    With these settings, the `This folder only`{.literal} mode for the principals is now set to `This folder, subfolders, and files`{.literal}.

Samba maps the permissions set in the procedure to the following Windows ACLs:

+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------+
| Principal                                                                                                                                        | Access         | Applies to                         |
+:=================================================================================================================================================+:===============+:===================================+
| *Domain*\\Domain Admins                                                                                                                          | Full control   | This folder, subfolders, and files |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------+
| *Domain*\\Domain Users                                                                                                                           | Read & execute | This folder, subfolders, and files |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------+
| `Everyone`{.literal} [^\[a\]^](#ftn.idm139622278927472)                                                                                          | None           | This folder, subfolders, and files |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------+
| *owner* (*Unix User\\owner*) [^\[b\]^](#ftn.idm139622275195344)                                                                                  | Full control   | This folder only                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------+
| *primary_group* (*Unix User\\primary_group*) [^\[c\]^](#ftn.idm139622275188240)                                                                  | None           | This folder only                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------+
| `CREATOR OWNER`{.literal} [^\[d\]^](#ftn.idm139622278746000) [^\[e\]^](#ftn.sambawinaclcreatorowner)                                             | Full control   | Subfolders and files only          |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------+
| `CREATOR GROUP`{.literal} [^\[e\]^](#ftn.sambawinaclcreatorowner) [^\[f\]^](#ftn.idm139622278737152)                                             | None           | Subfolders and files only          |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------+
| [^\[a\]^](#idm139622278927472) Samba maps the permissions for this principal from the `other`{.literal} ACL entry.                               |                |                                    |
|                                                                                                                                                  |                |                                    |
| [^\[b\]^](#idm139622275195344) Samba maps the owner of the directory to this entry.                                                              |                |                                    |
|                                                                                                                                                  |                |                                    |
| [^\[c\]^](#idm139622275188240) Samba maps the primary group of the directory to this entry.                                                      |                |                                    |
|                                                                                                                                                  |                |                                    |
| [^\[d\]^](#idm139622278746000) On new file system objects, the creator inherits automatically the permissions of this principal.                 |                |                                    |
|                                                                                                                                                  |                |                                    |
| [^\[e\]^](#sambawinaclcreatorowner) Configuring or removing these principals from the ACLs not supported on shares that use POSIX ACLs.          |                |                                    |
|                                                                                                                                                  |                |                                    |
| [^\[f\]^](#idm139622278737152) On new file system objects, the creator's primary group inherits automatically the permissions of this principal. |                |                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------+------------------------------------+

Show more

**Additional resources**

-   [Setting up a share that uses Windows ACLs](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-a-share-that-uses-windows-acls)

### [1.8. Setting permissions on a share that uses POSIX ACLs](#setting-permissions-on-a-share-that-uses-posix-acls) {#setting-permissions-on-a-share-that-uses-posix-acls .title}

To limit or grant access to a Samba share, you can set certain parameters in the share's section in the `/etc/samba/smb.conf`{.literal} file.

Note

Share-based permissions manage if a user, group, or host is able to access a share. These settings do not affect file system Access Control Lists (ACLs).

Use share-based settings to restrict access to shares, for example, to deny access from specific hosts.

#### [1.8.1. Prerequisites](#prerequisites_2) {#prerequisites-1 .title}

-   A share with POSIX ACLs has been set up.

#### [1.8.2. Configuring user and group-based share access](#configuring-user-and-group-based-share-access) {#configuring-user-and-group-based-share-access .title}

User and group-based access control enables you to grant or deny access to a share for certain users and groups. For more information, see the `smb.conf(5)`{.literal} man page on your system.

**Prerequisites**

-   The Samba share on which you want to set user or group-based access exists.

**Procedure**

1.  For example, you can enable all members of the `Domain Users`{.literal} group to access a share and deny access for the `user`{.literal} account. To do so, add the following parameters to the share configuration:

    ``` {.language-plaintext tabindex="-1"}
    valid users = +DOMAIN\"Domain Users"
    invalid users = DOMAIN\user
    ```

    The `invalid users`{.literal} parameter has a higher priority than the `valid users`{.literal} parameter. For example, if the `user`{.literal} account is a member of the `Domain Users`{.literal} group, access is denied in the previous example.

2.  Reload the Samba configuration:

    ``` {.language-plaintext tabindex="-1"}
    # smbcontrol all reload-config
    ```

#### [1.8.3. Configuring host-based share access](#configuring-host-based-share-access) {#configuring-host-based-share-access .title}

You can grant or deny access to a share based on client host names, IP addresses, or IP range. You can do this by using host-based access control. For more information, see the `smb.conf(5)`{.literal} man page on your system.

The following procedure explains enabling the `127.0.0.1`{.literal} IP address, the `192.0.2.0/24`{.literal} IP range, and the `client1.example.com`{.literal} host to access a share. It also denies access for the `client2.example.com`{.literal} host.

**Prerequisites**

-   The Samba share on which you want to set host-based access exists.

**Procedure**

1.  Add the following parameters to the configuration of the share in the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    hosts allow = 127.0.0.1 192.0.2.0/24 client1.example.com
    hosts deny = client2.example.com
    ```

    The `hosts deny`{.literal} parameter has a higher priority than `hosts allow`{.literal}. For example, if `client1.example.com`{.literal} resolves to an IP address listed in the `hosts allow`{.literal} parameter, access for this host is denied.

2.  Reload the Samba configuration:

    ``` {.language-plaintext tabindex="-1"}
    # smbcontrol all reload-config
    ```

### [1.9. Setting up a share that uses Windows ACLs](#setting-up-a-share-that-uses-windows-acls) {#setting-up-a-share-that-uses-windows-acls .title}

Samba supports setting Windows Access Control Lists (ACLs) on shares and file system objects.

This feature enables you to:

-   Use the fine-granular Windows ACLs
-   Manage share permissions and file system ACLs using Windows

Alternatively, you can configure a share to use POSIX ACLs.

#### [1.9.1. Granting the SeDiskOperatorPrivilege privilege](#granting-the-sediskoperatorprivilege-privilege) {#granting-the-sediskoperatorprivilege-privilege .title}

Only users and groups having the `SeDiskOperatorPrivilege`{.literal} privilege granted can configure permissions on shares that use Windows ACLs.

**Procedure**

1.  For example, to grant the `SeDiskOperatorPrivilege`{.literal} privilege to the *`DOMAIN`{.literal}*`\Domain Admins`{.literal} group:

    ``` {.language-plaintext tabindex="-1"}
    # net rpc rights grant "DOMAIN\Domain Admins" SeDiskOperatorPrivilege -U "DOMAIN\administrator"
    ```

    ``` {.language-plaintext tabindex="-1"}
    Enter DOMAIN\administrator's password:
    Successfully granted rights.
    ```

    Note

    In a domain environment, grant `SeDiskOperatorPrivilege`{.literal} to a domain group. This enables you to centrally manage the privilege by updating a user's group membership.

2.  To list all users and groups having `SeDiskOperatorPrivilege`{.literal} granted:

    ``` {.language-plaintext tabindex="-1"}
    # net rpc rights list privileges SeDiskOperatorPrivilege -U "DOMAIN\administrator"
    ```

    ``` {.language-plaintext tabindex="-1"}
    Enter administrator's password:
    SeDiskOperatorPrivilege:
      BUILTIN\Administrators
      DOMAIN\Domain Admins
    ```

#### [1.9.2. Enabling Windows ACL support](#enabling-windows-acl-support) {#enabling-windows-acl-support .title}

To configure shares that support Windows ACLs, you must enable this feature in Samba.

**Prerequisites**

-   A user share is configured on the Samba server.

**Procedure**

1.  To enable it globally for all shares, add the following settings to the `[global]`{.literal} section of the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    vfs objects = acl_xattr
    map acl inherit = yes
    store dos attributes = yes
    ```

    Alternatively, you can enable Windows ACL support for individual shares, by adding the same parameters to a share's section instead.

2.  Restart the `smb`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart smb
    ```

#### [1.9.3. Adding a share that uses Windows ACLs](#adding-a-share-that-uses-windows-acls) {#adding-a-share-that-uses-windows-acls .title}

You can create a share named `example`{.literal} that shares the content of the `/srv/samba/example/`{.literal} directory and uses Windows ACLs.

**Procedure**

1.  Create the folder if it does not exist. For example:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir -p /srv/samba/example/
    ```

2.  If you run SELinux in `enforcing`{.literal} mode, set the `samba_share_t`{.literal} context on the directory:

    ``` {.language-plaintext tabindex="-1"}
    # semanage fcontext -a -t samba_share_t "/srv/samba/example(/.*)?"
    ```

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Rv /srv/samba/example/
    ```

3.  Add the example share to the `/etc/samba/smb.conf`{.literal} file. For example, to add the share write-enabled:

    ``` {.language-plaintext tabindex="-1"}
    [example]
        path = /srv/samba/example/
        read only = no
    ```

    Note

    Regardless of the file system ACLs; if you do not set `read only = no`{.literal}, Samba shares the directory in read-only mode.

4.  If you have not enabled Windows ACL support in the \[global\] section, add the following parameters to the \[example\] section to enable this feature:

    ``` {.language-plaintext tabindex="-1"}
    vfs objects = acl_xattr
    map acl inherit = yes
    store dos attributes = yes
    ```

5.  Verify the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # testparm
    ```

6.  Open the required ports and reload the firewall configuration by using the `firewall-cmd`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=samba
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

7.  Restart the `smb`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart smb
    ```

#### [1.9.4. Managing share permissions and file system ACLs of a share that uses Windows ACLs](#managing-share-permissions-and-file-system-acls-of-a-share-that-uses-windows-acls) {#managing-share-permissions-and-file-system-acls-of-a-share-that-uses-windows-acls .title}

To manage share permissions and file system ACLs on a Samba share with Windows ACLs, use Windows applications, like `Computer Management`{.literal}. For details, see the Windows documentation. Alternatively, use the `smbcacls`{.literal} utility to manage ACLs.

Note

To modify the file system permissions from Windows, you must use an account that has the `SeDiskOperatorPrivilege`{.literal} privilege granted.

**Additional resources**

-   [Setting up a Samba file share that uses POSIX ACLs](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-a-samba-file-share-that-uses-posix-acls)

### [1.10. Managing ACLs on an SMB share by using smbcacls](#managing-acls-on-an-smb-share-using-smbcacls) {#managing-acls-on-an-smb-share-by-using-smbcacls .title}

The `smbcacls`{.literal} utility lists, sets, and deletes Access Control Lists (ACLs) of files and directories. It works on resources stored on a Server Message Block (SMB) share.

You can use `smbcacls`{.literal} to manage file system ACLs:

-   On a local or remote Samba server that uses advanced Windows ACLs or POSIX ACLs
-   On Red Hat Enterprise Linux to remotely manage ACLs on a share hosted on Windows

#### [1.10.1. Access control entries](#access-control-entries) {#access-control-entries .title}

Access Control Entries (ACEs) define permissions, inheritance, and access rights for files and directories. ACEs help interpret and manage file system access through Access Control Lists (ACLs). This is especially relevant in SMB environments.

Each ACL entry of a file system object contains Access ACE in the following format:

``` {.language-plaintext tabindex="-1"}
security_principal:access_right/inheritance_information/permissions
```

**Example 1.3. Access control entries**

If the `AD\Domain Users`{.literal} group has `Modify`{.literal} permissions applicable to `This folder, subfolders, and files`{.literal} on Windows, the ACL contains the following ACE:

``` {.language-plaintext tabindex="-1"}
AD\Domain Users:ALLOWED/OI|CI/CHANGE
```

An ACE contains the following parts:

Security principal
:   The security principal is the user, group, or Security Identifier (SID) the permissions in the ACL are applied to.

Access right
:   Defines if access to an object is granted or denied. The value can be `ALLOWED`{.literal} or `DENIED`{.literal}.

Inheritance information

:   The following values exist:

    +----------------+-------------------+---------------------------------------------------------+
    | Value          | Description       | Maps to                                                 |
    +:===============+:==================+:========================================================+
    | `OI`{.literal} | Object Inherit    | This folder and files                                   |
    +----------------+-------------------+---------------------------------------------------------+
    | `CI`{.literal} | Container Inherit | This folder and subfolders                              |
    +----------------+-------------------+---------------------------------------------------------+
    | `IO`{.literal} | Inherit Only      | The ACE does not apply to the current file or directory |
    +----------------+-------------------+---------------------------------------------------------+
    | `ID`{.literal} | Inherited         | The ACE was inherited from the parent directory         |
    +----------------+-------------------+---------------------------------------------------------+

    : Table 1.1. Inheritance settings

    Show more

    Additionally, the values can be combined as follows:

    +----------------------+----------------------------------------------------+
    | Value combinations   | Maps to the Windows `Applies to`{.literal} setting |
    +:=====================+:===================================================+
    | `OI|CI`{.literal}    | This folder, subfolders, and files                 |
    +----------------------+----------------------------------------------------+
    | `OI|CI|IO`{.literal} | Subfolders and files only                          |
    +----------------------+----------------------------------------------------+
    | `CI|IO`{.literal}    | Subfolders only                                    |
    +----------------------+----------------------------------------------------+
    | `OI|IO`{.literal}    | Files only                                         |
    +----------------------+----------------------------------------------------+

    : Table 1.2. Inheritance settings combinations

    Show more

Permissions

:   This value can be either a hex value that represents one or more Windows permissions or an `smbcacls`{.literal} alias:

    -   A hex value that represents one or more Windows permissions.

        The following table displays the advanced Windows permissions and their corresponding value in hex format:

        +-----------------------------------------------+------------------------+
        | Windows permissions                           | Hex values             |
        +:==============================================+:=======================+
        | Full control                                  | `0x001F01FF`{.literal} |
        +-----------------------------------------------+------------------------+
        | Traverse folder / execute file                | `0x00100020`{.literal} |
        +-----------------------------------------------+------------------------+
        | List folder / read data                       | `0x00100001`{.literal} |
        +-----------------------------------------------+------------------------+
        | Read attributes                               | `0x00100080`{.literal} |
        +-----------------------------------------------+------------------------+
        | Read extended attributes                      | `0x00100008`{.literal} |
        +-----------------------------------------------+------------------------+
        | Create files / write data                     | `0x00100002`{.literal} |
        +-----------------------------------------------+------------------------+
        | Create folders / append data                  | `0x00100004`{.literal} |
        +-----------------------------------------------+------------------------+
        | Write attributes                              | `0x00100100`{.literal} |
        +-----------------------------------------------+------------------------+
        | Write extended attributes                     | `0x00100010`{.literal} |
        +-----------------------------------------------+------------------------+
        | Delete subfolders and files                   | `0x00100040`{.literal} |
        +-----------------------------------------------+------------------------+
        | Delete                                        | `0x00110000`{.literal} |
        +-----------------------------------------------+------------------------+
        | Read permissions                              | `0x00120000`{.literal} |
        +-----------------------------------------------+------------------------+
        | Change permissions                            | `0x00140000`{.literal} |
        +-----------------------------------------------+------------------------+
        | Take ownership                                | `0x00180000`{.literal} |
        +-----------------------------------------------+------------------------+

        : Table 1.3. Windows permissions and their corresponding smbcacls value in hex format

        Show more

        Multiple permissions can be combined as a single hex value by using the bit-wise `OR`{.literal} operation.

    -   An `smbcacls`{.literal} alias. The following table displays the available aliases:

        +----------------------------+-----------------------------------------------+
        | `smbcacls`{.literal} alias | Maps to Windows permission                    |
        +:===========================+:==============================================+
        | `R`{.literal}              | Read                                          |
        +----------------------------+-----------------------------------------------+
        | `READ`{.literal}           | Read & execute                                |
        +----------------------------+-----------------------------------------------+
        | `W`{.literal}              | Special:                                      |
        |                            |                                               |
        |                            | -   Create files / write data                 |
        |                            | -   Create folders / append data              |
        |                            | -   Write attributes                          |
        |                            | -   Write extended attributes                 |
        |                            | -   Read permissions                          |
        +----------------------------+-----------------------------------------------+
        | `D`{.literal}              | Delete                                        |
        +----------------------------+-----------------------------------------------+
        | `P`{.literal}              | Change permissions                            |
        +----------------------------+-----------------------------------------------+
        | `O`{.literal}              | Take ownership                                |
        +----------------------------+-----------------------------------------------+
        | `X`{.literal}              | Traverse / execute                            |
        +----------------------------+-----------------------------------------------+
        | `CHANGE`{.literal}         | Modify                                        |
        +----------------------------+-----------------------------------------------+
        | `FULL`{.literal}           | Full control                                  |
        +----------------------------+-----------------------------------------------+

        : Table 1.4. Existing smbcacls aliases and their corresponding Windows permission

        Show more

        Note

        You can combine single-letter aliases when you set permissions. For example, you can set `RD`{.literal} to apply the Windows permission `Read`{.literal} and `Delete`{.literal}. However, you can neither combine multiple non-single-letter aliases nor combine aliases and hex values.

**Additional resources**

-   [ACE mask calculation](#ace-mask-calculation "1.10.3. ACE mask calculation")

#### [1.10.2. Displaying ACLs by using smbcacls](#displaying-acls-using-smbcacls) {#displaying-acls-by-using-smbcacls .title}

To display ACLs on an SMB share, use the `smbcacls`{.literal} utility. If you run `smbcacls`{.literal} without any operation parameter, such as `--add`{.literal}, the utility displays the ACLs of a file system object.

**Procedure**

-   For example, to list the ACLs of the root directory of the `//server/example`{.literal} share:

    ``` {.language-plaintext tabindex="-1"}
    # smbcacls //server/example / -U "DOMAIN\administrator"
    ```

    ``` {.language-plaintext tabindex="-1"}
    Enter DOMAIN\administrator's password:
    REVISION:1
    CONTROL:SR|PD|DI|DP
    OWNER:AD\Administrators
    GROUP:AD\Domain Users
    ACL:AD\Administrator:ALLOWED/OI|CI/FULL
    ACL:AD\Domain Users:ALLOWED/OI|CI/CHANGE
    ACL:AD\Domain Guests:ALLOWED/OI|CI/0x00100021
    ```

    The output of the command displays:

-   `REVISION`{.literal}: The internal Windows NT ACL revision of the security descriptor

-   `CONTROL`{.literal}: Security descriptor control

-   `OWNER`{.literal}: Name or SID of the security descriptor's owner

-   `GROUP`{.literal}: Name or SID of the security descriptor's group

-   `ACL`{.literal} entries. For details, see [Access control entries](#access-control-entries "1.10.1. Access control entries").

#### [1.10.3. ACE mask calculation](#ace-mask-calculation) {#ace-mask-calculation .title}

In most situations, when you add or update an ACE, you use the `smbcacls`{.literal} aliases.

However, if you want to set advanced Windows permissions, you must use the bit-wise `OR`{.literal} operation to calculate the correct value. You can use the following shell command to calculate the value:

``` {.language-plaintext tabindex="-1"}
# echo $(printf '0x%X' $(( hex_value_1 | hex_value_2 | ... )))
```

**Example 1.4. Calculating an ACE Mask**

You want to set the following permissions:

-   Traverse folder / execute file (0x00100020)
-   List folder / read data (0x00100001)
-   Read attributes (0x00100080)

To calculate the hex value for the previous permissions, enter:

``` {.language-plaintext tabindex="-1"}
# echo $(printf '0x%X' $(( 0x00100020 | 0x00100001 | 0x00100080 )))
```

``` {.language-plaintext tabindex="-1"}
0x1000A1
```

Use the returned value when you set or update an ACE.

**Additional resources**

-   [Existing smbcacls aliases and their corresponding Windows permission](#table_smbcacls-aliases "Table 1.4. Existing smbcacls aliases and their corresponding Windows permission")
-   [Windows permissions and their corresponding smbcacls value in hex format](#table_windows-permissions-hex-values "Table 1.3. Windows permissions and their corresponding smbcacls value in hex format")

#### [1.10.4. Adding, updating, and removing an ACL by using smbcacls](#adding-updating-and-removing-an-acl-using-smbcacls) {#adding-updating-and-removing-an-acl-by-using-smbcacls .title}

Depending on the parameter you pass to the `smbcacls`{.literal} utility, you can add, update, and remove ACLs from a file or directory.

**Adding an ACL**

To add an ACL to the `//server/example`{.literal} share root that grants `CHANGE`{.literal} permissions for `This folder, subfolders, and files`{.literal} to the `AD\Domain Users`{.literal} group:

``` {.language-plaintext tabindex="-1"}
# smbcacls //server/example / -U "DOMAIN\administrator --add ACL:"AD\Domain Users":ALLOWED/OI|CI/CHANGE
```

**Updating an ACL**

Updating an ACL is similar to adding a new ACL. You update an ACL by overriding the ACL by using the `--modify`{.literal} parameter with an existing security principal. If `smbcacls`{.literal} finds the security principal in the ACL list, the utility updates the permissions. Otherwise the command fails with an error:

``` {.language-plaintext tabindex="-1"}
ACL for SID principal_name not found
```

For example, to update the permissions of the `AD\Domain Users`{.literal} group and set them to `READ`{.literal} for `This folder, subfolders, and files`{.literal}:

``` {.language-plaintext tabindex="-1"}
# smbcacls //server/example / -U "DOMAIN\administrator --modify ACL:"AD\Domain Users":ALLOWED/OI|CI/READ
```

**Deleting an ACL**

To delete an ACL, pass the `--delete`{.literal} parameter with the exact ACL to the `smbcacls`{.literal} utility. For example:

``` {.language-plaintext tabindex="-1"}
# smbcacls //server/example / -U "DOMAIN\administrator --delete ACL:"AD\Domain Users":ALLOWED/OI|CI/READ
```

### [1.11. Enabling users to share directories on a Samba server](#enabling-users-to-share-directories-on-a-samba-server) {#enabling-users-to-share-directories-on-a-samba-server .title}

On a Samba server, you can configure that users can share directories without root permissions.

#### [1.11.1. Enabling the user shares feature](#enabling-the-user-shares-feature) {#enabling-the-user-shares-feature .title}

Before users can share directories, the administrator must enable user shares in Samba.

**Procedure**

1.  Create the local `example`{.literal} group, if it does not exist:

    ``` {.language-plaintext tabindex="-1"}
    # groupadd example
    ```

2.  Prepare the directory for Samba to store the user share definitions and set its permissions properly. For example:

    a.  Create the directory:

        ``` {.language-plaintext tabindex="-1"}
        # mkdir -p /var/lib/samba/usershares/
        ```

    b.  Set write permissions for the `example`{.literal} group:

        ``` {.language-plaintext tabindex="-1"}
        # chgrp example /var/lib/samba/usershares/
        ```

        ``` {.language-plaintext tabindex="-1"}
        # chmod 1770 /var/lib/samba/usershares/
        ```

    c.  Set the sticky bit to prevent users to rename or delete files stored by other users in this directory.

3.  Edit the `/etc/samba/smb.conf`{.literal} file and add the following to the `[global]`{.literal} section:

    a.  Set the path to the directory you configured to store the user share definitions. For example:

        ``` {.language-plaintext tabindex="-1"}
        usershare path = /var/lib/samba/usershares/
        ```

    b.  Set how many user shares Samba allows to be created on this server. For example:

        ``` {.language-plaintext tabindex="-1"}
        usershare max shares = 100
        ```

        If you use the default of `0`{.literal} for the `usershare max shares`{.literal} parameter, user shares are disabled.

    c.  Optional: Set a list of absolute directory paths. For example, to configure that Samba only allows to share subdirectories of the `/data`{.literal} and `/srv`{.literal} directory to be shared, set:

        ``` {.language-plaintext tabindex="-1"}
        usershare prefix allow list = /data /srv
        ```

    For a list of further user share-related parameters you can set, see the `USERSHARES`{.literal} section in the `smb.conf(5)`{.literal} man page on your system.

4.  Verify the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # testparm
    ```

5.  Reload the Samba configuration:

    ``` {.language-plaintext tabindex="-1"}
    # smbcontrol all reload-config
    ```

    Users are now able to create user shares.

#### [1.11.2. Adding a user share](#adding-a-user-share) {#adding-a-user-share .title}

After you enable the user share feature in Samba, users can share directories on the Samba server without `root`{.literal} permissions by using `net usershare add`{.literal}.

Synopsis of the `net usershare add`{.literal} command:

`net usershare add`{.literal} share_name path \[\[ comment \] \| \[ ACLs \]\] \[ guest_ok=y\|n \]

Important

If you set ACLs when you create a user share, you must specify the comment parameter prior to the ACLs. To set an empty comment, use an empty string in double quotes.

Users can only enable guest access on a user share, if the administrator set `usershare allow guests = yes`{.literal} in the `[global]`{.literal} section. This setting is in the `/etc/samba/smb.conf`{.literal} file.

**Example 1.5. Adding a user share**

A user wants to share the `/srv/samba/`{.literal} directory on a Samba server. The share should be named `example`{.literal}, have no comment set, and should be accessible by guest users. Additionally, the share permissions should be set to full access for the `AD\Domain Users`{.literal} group and read permissions for other users. To add this share, run as the user:

``` {.language-plaintext tabindex="-1"}
$ net usershare add example /srv/samba/ "" "AD\Domain Users":F,Everyone:R guest_ok=yes
```

#### [1.11.3. Updating settings of a user share](#updating-settings-of-a-user-share) {#updating-settings-of-a-user-share .title}

To update settings of a user share, override the share by using the `net usershare add`{.literal} command. Use the same share name and the new settings. See [Adding a user share](#adding-a-user-share "1.11.2. Adding a user share").

#### [1.11.4. Displaying information about existing user shares](#displaying-information-about-existing-user-shares) {#displaying-information-about-existing-user-shares .title}

Users can enter the `net usershare info`{.literal} command on a Samba server to display user shares and their settings.

**Prerequisites**

-   A user share is configured on the Samba server.

**Procedure**

1.  To display all user shares created by any user:

    ``` {.language-plaintext tabindex="-1"}
    $ net usershare info -l
    ```

    ``` {.language-plaintext tabindex="-1"}
    [share_1]
    ```

    ``` {.language-plaintext tabindex="-1"}
    path=/srv/samba/
    comment=
    usershare_acl=Everyone:R,host_name\user:F,
    guest_ok=y
    ...
    ```

    To list only shares created by the user who runs the command, omit the `-l`{.literal} parameter.

2.  To display only the information about specific shares, pass the share name or wild cards to the command. For example, to display the information about shares whose name starts with `share_`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ net usershare info -l share_* 
    ```

#### [1.11.5. Listing user shares](#listing-user-shares) {#listing-user-shares .title}

If you want to list only the available user shares without their settings on a Samba server, use the `net usershare list`{.literal} command.

**Prerequisites**

-   A user share is configured on the Samba server.

**Procedure**

1.  To list the shares created by any user:

    ``` {.language-plaintext tabindex="-1"}
    $ net usershare list -l
    ```

    ``` {.language-plaintext tabindex="-1"}
    share_1
    share_2
    ...
    ```

    To list only shares created by the user who runs the command, omit the `-l`{.literal} parameter.

2.  To list only specific shares, pass the share name or wild cards to the command. For example, to list only shares whose name starts with `share_`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ net usershare list -l share_* 
    ```

#### [1.11.6. Deleting a user share](#deleting-a-user-share) {#deleting-a-user-share .title}

To delete a user share, use the `net usershare delete`{.literal} command. Use this command as the user who created the share or as the `root`{.literal} user.

**Prerequisites**

-   A user share is configured on the Samba server.

**Procedure**

-   Delete a user:

    ``` {.language-plaintext tabindex="-1"}
    $ net usershare delete share_name
    ```

### [1.12. Configuring a share to allow access without authentication](#configuring-a-share-to-allow-access-without-authentication) {#configuring-a-share-to-allow-access-without-authentication .title}

In certain situations, you want to share a directory to which users can connect without authentication. To configure this, enable guest access on a share.

Warning

Shares that do not require authentication can be a security risk.

#### [1.12.1. Enabling guest access to a share](#enabling-guest-access-to-a-share) {#enabling-guest-access-to-a-share .title}

If guest access is enabled on a share, Samba maps guest connections to the operating system account set in the `guest account`{.literal} parameter. Guest users can access files on this share if the account is listed in file system ACLs or POSIX permissions allow it.

**Example 1.6. Guest share permissions**

If you configured Samba to map the guest account to `nobody`{.literal}, which is the default, the ACLs in the following example:

-   Allow guest users to read `file1.txt`{.literal}
-   Allow guest users to read and modify `file2.txt`{.literal}
-   Prevent guest users to read or modify `file3.txt`{.literal}

``` {.language-plaintext tabindex="-1"}
-rw-r--r--. 1 root       root      1024 1. Sep 10:00 file1.txt
-rw-r-----. 1 nobody     root      1024 1. Sep 10:00 file2.txt
-rw-r-----. 1 root       root      1024 1. Sep 10:00 file3.txt
```

**Procedure**

1.  Edit the `/etc/samba/smb.conf`{.literal} file:

    a.  If this is the first guest share you set up on this server:

        i.  Set `map to guest = Bad User`{.literal} in the `[global]`{.literal} section:

            ``` {.language-plaintext tabindex="-1"}
            [global]
                    ...
                    map to guest = Bad User
            ```

            With this setting, Samba rejects login attempts that use an incorrect password unless the user name does not exist. If the specified user name does not exist and guest access is enabled on a share, Samba treats the connection as a guest login.

        ii. By default, Samba maps the guest account to the `nobody`{.literal} account on Red Hat Enterprise Linux. Alternatively, you can set a different account. For example:

            ``` {.language-plaintext tabindex="-1"}
            [global]
                    ...
                    guest account = user_name
            ```

            The account set in this parameter must exist locally on the Samba server. For security reasons, use an account that does not have a valid shell assigned.

    b.  Add the `guest ok = yes`{.literal} setting to the `[example]`{.literal} share section:

        ``` {.language-plaintext tabindex="-1"}
        [example]
                ...
                guest ok = yes
        ```

2.  Verify the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # testparm
    ```

3.  Reload the Samba configuration:

    ``` {.language-plaintext tabindex="-1"}
    # smbcontrol all reload-config
    ```

### [1.13. Configuring Samba for macOS clients](#configuring-samba-for-macos-clients) {#configuring-samba-for-macos-clients .title}

The `fruit`{.literal} virtual file system (VFS) Samba module provides enhanced compatibility with Apple server message block (SMB) clients.

#### [1.13.1. Optimizing the Samba configuration for providing file shares for macOS clients](#optimizing-the-samba-configuration-for-providing-file-shares-for-macos-clients) {#optimizing-the-samba-configuration-for-providing-file-shares-for-macos-clients .title}

The `fruit`{.literal} module provides enhanced compatibility of Samba with macOS clients. You can configure the module for all shares hosted on a Samba server to optimize the file shares for macOS clients. For more information, see the `vfs_fruit(8)`{.literal} man page on your system.

Note

Enable the `fruit`{.literal} module globally. Clients using macOS negotiate the server message block version 2 (SMB2) Apple (AAPL) protocol extensions when the client establishes the first connection. If the client first connects to a share without AAPL extensions enabled, it does not use the extensions for any server share.

**Prerequisites**

-   Samba is configured as a file server.

**Procedure**

1.  Edit the `/etc/samba/smb.conf`{.literal} file, and enable the `fruit`{.literal} and `streams_xattr`{.literal} Virtual File System (VFS) modules in the `[global]`{.literal} section:

    ``` {.language-plaintext tabindex="-1"}
    vfs objects = fruit streams_xattr
    ```

    Important

    You must enable the `fruit`{.literal} module before enabling `streams_xattr`{.literal}. The `fruit`{.literal} module uses alternate data streams (ADS). For this reason, you must also enable the `streams_xattr`{.literal} module.

2.  Optional: To provide macOS Time Machine support on a share, add the following setting to the share configuration in `/etc/samba/smb.conf`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    fruit:time machine = yes
    ```

3.  Verify the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # testparm
    ```

4.  Reload the Samba configuration:

    ``` {.language-plaintext tabindex="-1"}
    # smbcontrol all reload-config
    ```

**Additional resources**

-   [Setting up a Samba file share that uses POSIX ACLs](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-a-samba-file-share-that-uses-posix-acls)
-   [Setting up a share that uses Windows ACLs](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-a-share-that-uses-windows-acls)

### [1.14. Using the smbclient utility to access an SMB share](#using-the-smbclient-utility-to-access-an-smb-share) {#using-the-smbclient-utility-to-access-an-smb-share .title}

The `smbclient`{.literal} utility enables you to access file shares on a Server Message Block (SMB). Similarly you can access a command-line File Transfer Protocol (FTP) client. You can use it, for example, to upload and download files to and from a share.

#### [1.14.1. Prerequisites](#prerequisites_3) {#prerequisites-2 .title}

-   The `samba-client`{.literal} package is installed.

#### [1.14.2. How the smbclient interactive mode works](#how-the-smbclient-interactive-mode-works) {#how-the-smbclient-interactive-mode-works .title}

The interactive mode of `smbclient`{.literal} enables connection to Server Message Block/Common Internet File System (SMB/CIFS) shares and navigation of files and directories. You can also run common file operations securely by using built-in commands.

To authenticate to the `example`{.literal} share hosted on `server`{.literal} by using the *`DOMAIN\user`{.literal}* account:

``` {.language-plaintext tabindex="-1"}
# smbclient -U "DOMAIN\user" //server/example
```

``` {.language-plaintext tabindex="-1"}
Enter domain\user's password:
Try "help" to get a list of possible commands.
smb: \>
```

After `smbclient`{.literal} connected successfully to the share, the utility enters the interactive mode and shows the following prompt:

``` {.language-plaintext tabindex="-1"}
smb: \>
```

To display all available commands in the interactive shell, enter:

``` {.language-plaintext tabindex="-1"}
smb: \> help
```

To display the help for a specific command, enter:

``` {.language-plaintext tabindex="-1"}
smb: \> help command_name
```

#### [1.14.3. Using smbclient in interactive mode](#using-smbclient-in-interactive-mode) {#using-smbclient-in-interactive-mode .title}

If you use `smbclient`{.literal} without the `-c`{.literal} parameter, the utility enters the interactive mode. The following procedure shows how to connect to an SMB share and download a file from a subdirectory.

**Procedure**

1.  Connect to the share:

    ``` {.language-plaintext tabindex="-1"}
    # smbclient -U "DOMAIN\user_name" //server_name/share_name
    ```

2.  Change into the `/example/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    smb: \> d /example/
    ```

3.  List the files in the directory:

    ``` {.language-plaintext tabindex="-1"}
    smb: \example\> ls
    ```

    ``` {.language-plaintext tabindex="-1"}
      .                    D         0  Thu Nov 1 10:00:00 2018
      ..                   D         0  Thu Nov 1 10:00:00 2018
      example.txt          N   1048576  Thu Nov 1 10:00:00 2018

             9950208 blocks of size 1024. 8247144 blocks available
    ```

4.  Download the `example.txt`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    smb: \example\> get example.txt
    ```

    ``` {.language-plaintext tabindex="-1"}
    getting file \directory\subdirectory\example.txt of size 1048576 as example.txt (511975,0 KiloBytes/sec) (average 170666,7 KiloBytes/sec)
    ```

5.  Disconnect from the share:

    ``` {.language-plaintext tabindex="-1"}
    smb: \example\> exit
    ```

#### [1.14.4. Using smbclient in scripting mode](#using-smbclient-in-scripting-mode) {#using-smbclient-in-scripting-mode .title}

If you pass the `-c`{.literal} parameter to `smbclient`{.literal}, you can automatically run the commands on the remote SMB share. This enables you to use `smbclient`{.literal} in scripts.

The following procedure shows how to connect to an SMB share and download a file from a subdirectory.

**Procedure**

-   Use the following command to connect to the share, change into the `example`{.literal} directory, download the `example.txt`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # smbclient -U DOMAIN\user_name //server_name/share_name -c "cd /example/ ; get example.txt ; exit"
    ```

### [1.15. Setting up Samba as a print server](#setting-up-samba-as-a-print-server) {#setting-up-samba-as-a-print-server .title}

If you set up Samba as a print server, clients in your network can use Samba to print. Additionally, Windows clients can, if configured, download the driver from the Samba server.

#### [1.15.1. Prerequisites](#prerequisites_4) {#prerequisites-3 .title}

Samba has been set up in one of the following modes:

-   Standalone server
-   Domain member

#### [1.15.2. Enabling print server support in Samba](#enabling-print-server-support-in-samba) {#enabling-print-server-support-in-samba .title}

By default, print server support is not enabled in Samba. To use Samba as a print server, you must configure Samba accordingly.

Note

Print jobs and printer operations require remote procedure calls (RPCs). By default, Samba starts the `rpcd_spoolss`{.literal} service on demand to manage RPCs. During the first RPC call, or when you update the printer list in Common UNIX Printing System (CUPS), Samba retrieves the printer information. This can require approximately 1 second per printer. Therefore, if you have more than 50 printers, tune the `rpcd_spoolss`{.literal} settings.

**Prerequisites**

-   The printers are configured in a CUPS server.

    For details about configuring printers in CUPS, see the documentation provided in the CUPS web console (https://*printserver*:631/help) on the print server.

**Procedure**

1.  Edit the `/etc/samba/smb.conf`{.literal} file:

    a.  Add the `[printers]`{.literal} section to enable the printing back end in Samba:

        ``` {.language-plaintext tabindex="-1"}
        [printers]
                comment = All Printers
                path = /var/tmp/
                printable = yes
                create mask = 0600
        ```

        Important

        The `[printers]`{.literal} share name is hard-coded and cannot be changed.

    b.  If the CUPS server runs on a different host or port, specify the setting in the `[printers]`{.literal} section:

        ``` {.language-plaintext tabindex="-1"}
        cups server = printserver.example.com:631
        ```

    c.  If you have many printers, set the number of idle seconds higher than the number of printers connected to CUPS. For example, if you have 100 printers, set in the `[global]`{.literal} section:

        ``` {.language-plaintext tabindex="-1"}
        rpcd_spoolss:idle_seconds = 200
        ```

        If this setting does not scale in your environment, also increase the number of `rpcd_spoolss`{.literal} workers in the `[global]`{.literal} section:

        ``` {.language-plaintext tabindex="-1"}
        rpcd_spoolss:num_workers = 10
        ```

        By default, `rpcd_spoolss`{.literal} starts 5 workers.

2.  Verify the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # testparm
    ```

3.  Open the required ports and reload the firewall configuration by using the `firewall-cmd`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=samba
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

4.  Restart the `smb`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart smb
    ```

    After restarting the service, Samba automatically shares all printers that are configured in the CUPS back end. If you want to manually share only specific printers, see [Manually sharing specific printers](#manually-sharing-specific-printers "1.15.3. Manually sharing specific printers").

**Verification**

-   Submit a print job. For example, to print a PDF file, enter:

    ``` {.language-plaintext tabindex="-1"}
    # smbclient -Uuser //sambaserver.example.com/printer_name -c "print example.pdf"
    ```

#### [1.15.3. Manually sharing specific printers](#manually-sharing-specific-printers) {#manually-sharing-specific-printers .title}

If you configure Samba as a print server, it shares all printers configured in the Common UNIX Printing System (CUPS) back end. The following procedure explains how to share only specific printers.

**Prerequisites**

-   Samba is set up as a print server

**Procedure**

1.  Edit the `/etc/samba/smb.conf`{.literal} file:

    a.  In the `[global]`{.literal} section, disable automatic printer sharing by setting:

        ``` {.language-plaintext tabindex="-1"}
        load printers = no
        ```

    b.  Add a section for each printer you want to share. For example, to share the printer named `example`{.literal} in the CUPS back end as `Example-Printer`{.literal} in Samba, add the following section:

        ``` {.language-plaintext tabindex="-1"}
        [Example-Printer]
                path = /var/tmp/
                printable = yes
                printer name = example
        ```

        You do not need individual spool directories for each printer. You can set the same spool directory in the `path`{.literal} parameter for the printer as you set in the `[printers]`{.literal} section.

2.  Verify the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # testparm
    ```

3.  Reload the Samba configuration:

    ``` {.language-plaintext tabindex="-1"}
    # smbcontrol all reload-config
    ```

**Additional resources**

-   [Standalone server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-samba-as-a-standalone-server)
-   [Domain member](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-samba-as-an-ad-domain-member-server)

### [1.16. Setting up automatic printer driver downloads for Windows clients on Samba print servers](#setting-up-automatic-printer-driver-downloads-for-windows-clients-on-samba-print-servers) {#setting-up-automatic-printer-driver-downloads-for-windows-clients-on-samba-print-servers .title}

If you are running a Samba print server for Windows clients, you can upload drivers and preconfigure printers.

If a user connects to a printer, Windows automatically downloads and installs the driver locally on the client. The user does not require local administrator permissions for the installation. Additionally, Windows applies preconfigured driver settings, such as the number of trays.

#### [1.16.1. Prerequisites](#prerequisites_5) {#prerequisites-4 .title}

-   Samba is set up as a print server

#### [1.16.2. Basic information about printer drivers](#basic-information-about-printer-drivers) {#basic-information-about-printer-drivers .title}

Key concepts about printer drivers in Samba include supported versions and limitations. Driver preparation and providing compatible drivers for both 32-bit and 64-bit Windows clients apply in different environments.

**Supported driver model version**

Samba only supports the printer driver model version 3. This version is supported in Windows 2000 and later, and Windows Server 2000 and later. Samba does not support the driver model version 4, introduced in Windows 8 and Windows Server 2012. However, these and later Windows versions also support version 3 drivers.

**Package-aware drivers**

Samba does not support package-aware drivers.

**Preparing a printer driver for being uploaded**

Before you can upload a driver to a Samba print server:

-   Unpack the driver if it is provided in a compressed format.

-   Some drivers require to start a set up application that installs the driver locally on a Windows host. In certain situations, the installer extracts the individual files into the operating system's temporary folder during the set up runs. To use the driver files for uploading:

    a.  Start the installer.
    b.  Copy the files from the temporary folder to a new location.
    c.  Cancel the installation.

Ask your printer manufacturer for drivers that support uploading to a print server.

**Providing 32-bit and 64-bit drivers for a printer to a client**

To provide printer drivers for 32-bit and 64-bit Windows clients, you must upload a driver with the same name for both architectures. For example, if you upload the 32-bit driver named `Example PostScript`{.literal} and 64-bit driver named `Example PostScript (v1.0)`{.literal}, it is a mismatch. Consequently, you can only assign one of the drivers to a printer making it unavailable for both architectures.

#### [1.16.3. Enabling users to upload and preconfigure drivers](#enabling-users-to-upload-and-preconfigure-drivers) {#enabling-users-to-upload-and-preconfigure-drivers .title}

To upload and preconfigure printer drivers, grant the `SePrintOperatorPrivilege`{.literal} privilege. Users also require membership in the `printadmin`{.literal} group. Red Hat Enterprise Linux creates this group when installing `samba`{.literal} and assigns a dynamic system GID below 1000.

**Procedure**

1.  For example, to grant the `SePrintOperatorPrivilege`{.literal} privilege to the `printadmin`{.literal} group:

    ``` {.language-plaintext tabindex="-1"}
    # net rpc rights grant "printadmin" SePrintOperatorPrivilege -U "DOMAIN\administrator"
    ```

    ``` {.language-plaintext tabindex="-1"}
    Enter DOMAIN\administrator's password:
    Successfully granted rights.
    ```

    Note

    In a domain environment, grant `SePrintOperatorPrivilege`{.literal} to a domain group. This enables you to centrally manage the privilege by updating a user's group membership.

2.  To list all users and groups having `SePrintOperatorPrivilege`{.literal} granted:

    ``` {.language-plaintext tabindex="-1"}
    # net rpc rights list privileges SePrintOperatorPrivilege -U "DOMAIN\administrator"
    ```

    ``` {.language-plaintext tabindex="-1"}
    Enter administrator's password:
    SePrintOperatorPrivilege:
      BUILTIN\Administrators
      DOMAIN\printadmin
    ```

#### [1.16.4. Setting up the print\$ share](#setting-up-the-print-share) {#setting-up-the-print-share .title}

Windows downloads printer drivers from the `print$`{.literal} share on a print server. The `print$`{.literal} share name is fixed and cannot be changed. You can share `/var/lib/samba/drivers/`{.literal} as `print$`{.literal} and allow `printadmin`{.literal} members to upload drivers.

**Procedure**

1.  Add the `[print$]`{.literal} section to the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    [print$]
            path = /var/lib/samba/drivers/
            read only = no
            write list = printadmin
            force group = printadmin
            create mask = 0664
            directory mask = 2775
    ```

    Using these settings:

    -   Only members of the `printadmin`{.literal} group can upload printer drivers to the share.

    -   The group of newly created files and directories will be set to `printadmin`{.literal}.

    -   The permissions of new files will be set to `664`{.literal}.

    -   The permissions of new directories will be set to `2775`{.literal}.

        For more information, see [Enabling users to upload and preconfigure drivers](#enabling-users-to-upload-and-preconfigure-drivers "1.16.3. Enabling users to upload and preconfigure drivers").

2.  To upload only 64-bit drivers for all printers, include this setting in the `[global]`{.literal} section in the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    spoolss: architecture = Windows x64
    ```

    Without this setting, Windows only displays drivers for which you have uploaded at least the 32-bit version.

3.  Verify the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # testparm
    ```

4.  Reload the Samba configuration

    ``` {.language-plaintext tabindex="-1"}
    # smbcontrol all reload-config
    ```

5.  Create the `printadmin`{.literal} group if it does not exist:

    ``` {.language-plaintext tabindex="-1"}
    # groupadd printadmin
    ```

6.  Grant the `SePrintOperatorPrivilege`{.literal} privilege to the `printadmin`{.literal} group.

    ``` {.language-plaintext tabindex="-1"}
    # net rpc rights grant "printadmin" SePrintOperatorPrivilege -U "DOMAIN\administrator"
    ```

    ``` {.language-plaintext tabindex="-1"}
    Enter DOMAIN\administrator's password:
    Successfully granted rights.
    ```

7.  If you run SELinux in `enforcing`{.literal} mode, set the `samba_share_t`{.literal} context on the directory:

    ``` {.language-plaintext tabindex="-1"}
    # semanage fcontext -a -t samba_share_t "/var/lib/samba/drivers(/.*)?"
    ```

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Rv /var/lib/samba/drivers/
    ```

8.  Set the permissions on the `/var/lib/samba/drivers/`{.literal} directory:

    -   If you use POSIX Access Control Lists (ACLs), set:

        ``` {.language-plaintext tabindex="-1"}
        # chgrp -R "printadmin" /var/lib/samba/drivers/
        ```

        ``` {.language-plaintext tabindex="-1"}
        # chmod -R 2775 /var/lib/samba/drivers/
        ```

    -   If you use Windows ACLs, set:

        +---------------------------------+--------------------------------------------+------------------------------------+
        | Principal                       | Access                                     | Apply to                           |
        +:================================+:===========================================+:===================================+
        | `CREATOR OWNER`{.literal}       | Full control                               | Subfolders and files only          |
        +---------------------------------+--------------------------------------------+------------------------------------+
        | `Authenticated Users`{.literal} | Read & execute, List folder contents, Read | This folder, subfolders, and files |
        +---------------------------------+--------------------------------------------+------------------------------------+
        | `printadmin`{.literal}          | Full control                               | This folder, subfolders, and files |
        +---------------------------------+--------------------------------------------+------------------------------------+

        Show more

        For details about setting ACLs on Windows, see the Windows documentation.

#### [1.16.5. Creating a GPO to enable clients to trust the Samba print server](#creating-a-gpo-to-enable-clients-to-trust-the-samba-print-server) {#creating-a-gpo-to-enable-clients-to-trust-the-samba-print-server .title}

Recent Windows versions block downloads of non-package-aware printer drivers from untrusted servers. In an AD domain, create a Group Policy Object (GPO). The GPO enables clients to trust the Samba server.

**Prerequisites**

-   The Samba print server is a member of an AD domain.
-   The Windows computer you are using to create the GPO must have the Windows Remote Server Administration Tools (RSAT) installed. For details, see the Windows documentation.

**Procedure**

1.  Log into a Windows computer with an account that is allowed to edit group policies, such as the AD domain `Administrator`{.literal} user.

2.  Open the `Group Policy Management Console`{.literal}.

3.  Right-click to your AD domain and select `Create a GPO in this domain, and Link it here`{.literal}.

4.  Enter a name for the GPO, such as `Legacy Printer Driver Policy`{.literal} and click `OK`{.literal}. The new GPO will be displayed under the domain entry.

5.  Right-click to the newly-created GPO and select `Edit`{.literal} to open the `Group Policy Management Editor`{.literal}.

6.  Navigate to Computer Configuration → Policies → Administrative Templates → Printers.

7.  On the right side of the window, double-click `Point and Print Restriction`{.literal} to edit the policy:

    a.  Enable the policy and set the following options:

        i.  Select `Users can only point and print to these servers`{.literal}. Then enter the fully-qualified domain name (FQDN) of the Samba print server to the field next to this option.

        ii. In both checkboxes under `Security Prompts`{.literal}, select `Do not show warning or elevation prompt`{.literal}.

    b.  Click OK.

8.  Double-click `Package Point and Print - Approved servers`{.literal} to edit the policy:

    a.  Enable the policy and click the `Show`{.literal} button.

    b.  Enter the FQDN of the Samba print server.

    c.  Close both the `Show Contents`{.literal} and the policy's properties window by clicking `OK`{.literal}.

9.  Close the `Group Policy Management Editor`{.literal}.

10. Close the `Group Policy Management Console`{.literal}.

    After the Windows domain members apply the group policy, printer drivers are automatically downloaded from the Samba server. This occurs when a user connects to a printer.

    For using group policies, see the Windows documentation.

#### [1.16.6. Uploading drivers and preconfiguring printers](#uploading-drivers-and-preconfiguring-printers) {#uploading-drivers-and-preconfiguring-printers .title}

Use the `Print Management`{.literal} application on a Windows client to upload drivers and preconfigure printers hosted on the Samba print server. For further details, see the Windows documentation.

### [1.17. Running Samba on a server with FIPS mode enabled](#running-samba-on-a-server-with-fips-mode-enabled) {#running-samba-on-a-server-with-fips-mode-enabled .title}

There are limitations of running Samba with FIPS mode enabled. You can also enable FIPS mode on a Red Hat Enterprise Linux host running Samba.

#### [1.17.1. Limitations of using Samba in FIPS mode](#limitations-of-using-samba-in-fips-mode) {#limitations-of-using-samba-in-fips-mode .title}

Samba features have specific limitations when running in Federal Information Processing Standards (FIPS) mode. Some modes work under certain conditions while others are restricted for security compliance.

The following Samba modes and features work in FIPS mode under the indicated conditions:

-   Samba as a domain member only in Active Directory (AD) or Red Hat Enterprise Linux Identity Management (IdM) with Kerberos using Advanced Encryption Standard (AES) ciphers.
-   Samba as a file server on an Active Directory domain member. However, this requires that clients use Kerberos to authenticate to the server.

Due to the increased security of FIPS, the following Samba features and modes do not work if FIPS mode is enabled:

-   NT LAN Manager (NTLM) authentication because RC4 ciphers are blocked
-   The server message block version 1 (SMB1) protocol
-   The stand-alone file server mode because it uses NTLM authentication
-   NT4-style domain controllers
-   NT4-style domain members. Note that Red Hat continues supporting the primary domain controller (PDC) functionality IdM uses in the background.
-   Password changes against the Samba server. You can only perform password changes by using Kerberos against an Active Directory domain controller.

The following feature is not tested in FIPS mode and, therefore, is not supported by Red Hat:

-   Running Samba as a print server

#### [1.17.2. Using Samba in FIPS mode](#using-samba-in-fips-mode) {#using-samba-in-fips-mode .title}

You can enable the FIPS mode on a RHEL host that runs Samba.

**Prerequisites**

-   Samba is configured on the Red Hat Enterprise Linux host.
-   Samba runs in a mode that is supported in FIPS mode.

**Procedure**

1.  Enable the FIPS mode on RHEL:

    ``` {.language-plaintext tabindex="-1"}
    # fips-mode-setup --enable
    ```

2.  Reboot the server:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

3.  Use the `testparm`{.literal} utility to verify the configuration:

    ``` {.language-plaintext tabindex="-1"}
    # testparm -s
    ```

    If the command displays any errors or incompatibilities, fix them to ensure that Samba works correctly.

**Additional resources**

-   [Section 1.17.1, "Limitations of using Samba in FIPS mode"](#limitations-of-using-samba-in-fips-mode "1.17.1. Limitations of using Samba in FIPS mode")

### [1.18. Tuning the performance of a Samba server](#tuning-the-performance-of-a-samba-server) {#tuning-the-performance-of-a-samba-server .title}

Settings that improve Samba performance in certain situations and those that can negatively impact performance.

#### [1.18.1. Prerequisites](#prerequisites_6) {#prerequisites-5 .title}

-   Samba is set up as a file or print server.

#### [1.18.2. Setting the SMB protocol version](#setting-the-smb-protocol-version) {#setting-the-smb-protocol-version .title}

New SMB versions add features and improve protocol performance. Windows clients support the latest SMB versions and benefit when Samba does the same. By default, Samba uses the latest supported stable SMB protocol version.

Note

To ensure the latest stable SMB protocol version is enabled, do not set the `server max protocol`{.literal} parameter. Manual configuration requires updating the setting with each new SMB protocol version. This approach keeps the latest protocol version enabled.

The following procedure explains how to use the default value in the `server max protocol`{.literal} parameter.

**Procedure**

1.  Remove the `server max protocol`{.literal} parameter from the `[global]`{.literal} section in the `/etc/samba/smb.conf`{.literal} file.

2.  Reload the Samba configuration

    ``` {.language-plaintext tabindex="-1"}
    # smbcontrol all reload-config
    ```

#### [1.18.3. Tuning shares with directories that contain a large number of files](#tuning-shares-with-directories-that-contain-a-large-number-of-files) {#tuning-shares-with-directories-that-contain-a-large-number-of-files .title}

Linux supports case-sensitive file names. For this reason, Samba needs to scan directories for uppercase and lowercase file names when searching or accessing a file. You can configure a share to create new files only in lowercase or uppercase, which improves the performance.

**Prerequisites**

-   Samba is configured as a file server

**Procedure**

1.  Rename all files on the share to lowercase.

    Note

    Using the settings in this procedure, files with names other than in lowercase will no longer be displayed.

2.  Set the following parameters in the share's section:

    ``` {.language-plaintext tabindex="-1"}
    case sensitive = true
    default case = lower
    preserve case = no
    short preserve case = no
    ```

    For details about the parameters, see their descriptions in the `smb.conf(5)`{.literal} man page on your system.

3.  Verify the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # testparm
    ```

4.  Reload the Samba configuration:

    ``` {.language-plaintext tabindex="-1"}
    # smbcontrol all reload-config
    ```

    After you applied these settings, the names of all newly created files on this share use lowercase. Because of these settings, Samba no longer needs to scan the directory for uppercase and lowercase, which improves the performance.

#### [1.18.4. Settings that can have a negative performance impact](#settings-that-can-have-a-negative-performance-impact) {#settings-that-can-have-a-negative-performance-impact .title}

By default, the Red Hat Enterprise Linux kernel is tuned for high network performance. The kernel uses auto-tuning for buffer sizes. Setting `socket options`{.literal} in `smb.conf`{.literal} overrides these settings and often reduces Samba performance.

To use the optimized settings from the Kernel, remove the `socket options`{.literal} parameter from the `[global]`{.literal} section in the `/etc/samba/smb.conf`{.literal}.

### [1.19. Configuring Samba to be compatible with clients that require an SMB version lower than the default](#configuring-samba-to-be-compatible-with-clients-that-require-an-smb-version-lower-than-the-default) {#configuring-samba-to-be-compatible-with-clients-that-require-an-smb-version-lower-than-the-default .title}

Samba uses a reasonable and secure default value for the minimum server message block (SMB) version it supports. However, if you have clients that require an older SMB version, you can configure Samba to support it.

#### [1.19.1. Setting the minimum SMB protocol version supported by a Samba server](#setting-the-minimum-smb-protocol-version-supported-by-a-samba-server) {#setting-the-minimum-smb-protocol-version-supported-by-a-samba-server .title}

In Samba, the `server min protocol`{.literal} parameter in `/etc/samba/smb.conf`{.literal} defines the minimum server message block (SMB) protocol version the Samba server supports. You can change the minimum SMB protocol version. For more information, see the `smb.conf(5)`{.literal} man page on your system.

Note

By default, Samba on RHEL 8.2 and later supports only SMB2 and newer protocol versions. Avoid using the deprecated SMB1 protocol. If your environment requires SMB1, set the `server min protocol`{.literal} parameter to `NT1`{.literal} to re-enable it.

**Prerequisites**

-   Samba is installed and configured.

**Procedure**

1.  Edit the `/etc/samba/smb.conf`{.literal} file, add the `server min protocol`{.literal} parameter, and set it to the minimum SMB protocol version the server should support. For example, to set the minimum SMB protocol version to `SMB3`{.literal}, add:

    ``` {.language-plaintext tabindex="-1"}
    server min protocol = SMB3
    ```

2.  Restart the `smb`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart smb
    ```

### [1.20. Frequently used Samba command-line utilities](#frequently-used-samba-command-line-utilities) {#frequently-used-samba-command-line-utilities .title}

This chapter describes frequently used commands when working with a Samba server.

#### [1.20.1. Using the net ads join and net rpc join commands](#using-the-net-ads-join-and-net-rpc-join-commands) {#using-the-net-ads-join-and-net-rpc-join-commands .title}

Using the `join`{.literal} subcommand of the `net`{.literal} utility, you can join Samba to an Active Directory (AD) or NT4 domain. To join the domain, you must create the `/etc/samba/smb.conf`{.literal} file manually. Optionally update additional configurations, such as Pluggable Authentication Modules (PAM).

The `realm`{.literal} utility is the preferred method to join a domain. The `realm`{.literal} utility automatically updates all involved configuration files.

**Procedure**

1.  Manually create the `/etc/samba/smb.conf`{.literal} file with the following settings:

    -   For an AD domain member:

        ``` {.language-plaintext tabindex="-1"}
        [global]
        workgroup = domain_name
        security = ads
        passdb backend = tdbsam
        realm = AD_REALM
        ```

    -   For an NT4 domain member:

        ``` {.language-plaintext tabindex="-1"}
        [global]
        workgroup = domain_name
        security = user
        passdb backend = tdbsam
        ```

2.  Add an ID mapping configuration for the `*`{.literal} default domain and for the domain you want to join. Add this to the `[global`{.literal}\] section in the `/etc/samba/smb.conf`{.literal} file.

3.  Verify the `/etc/samba/smb.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # testparm
    ```

4.  Join the domain as the domain administrator:

    -   To join an AD domain:

        ``` {.language-plaintext tabindex="-1"}
        # net ads join -U "DOMAIN\administrator"
        ```

    -   To join an NT4 domain:

        ``` {.language-plaintext tabindex="-1"}
        # net rpc join -U "DOMAIN\administrator"
        ```

5.  Configure the system profile to use `winbind`{.literal} for name resolution and authentication:

    ``` {.language-plaintext tabindex="-1"}
    # authselect select winbind
    ```

6.  Enable and start the `winbind`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now winbind
    ```

7.  Optional: Configure PAM by using the `authselect`{.literal} utility.

    For details, see the `authselect(8)`{.literal} man page on your system.

8.  Optional: For AD environments, configure the Kerberos client.

    For details, see the documentation of your Kerberos client.

#### [1.20.2. Using the net rpc rights command](#using-the-net-rpc-rights-command) {#using-the-net-rpc-rights-command .title}

In Windows, you can assign privileges to accounts and groups to perform special operations. Examples include setting Access Control Lists (ACLs) on a share or uploading printer drivers. On a Samba server, you can use the `net rpc rights`{.literal} command to manage privileges.

**Listing privileges you can set**

To list all available privileges and their owners, use the `net rpc rights list`{.literal} command. For example:

``` {.language-plaintext tabindex="-1"}
# net rpc rights list -U "DOMAIN\administrator"
```

``` {.language-plaintext tabindex="-1"}
Enter DOMAIN\administrator's password:
     SeMachineAccountPrivilege  Add machines to domain
      SeTakeOwnershipPrivilege  Take ownership of files or other objects
             SeBackupPrivilege  Back up files and directories
            SeRestorePrivilege  Restore files and directories
     SeRemoteShutdownPrivilege  Force shutdown from a remote system
      SePrintOperatorPrivilege  Manage printers
           SeAddUsersPrivilege  Add users and groups to the domain
       SeDiskOperatorPrivilege  Manage disk shares
           SeSecurityPrivilege  System security
```

**Granting privileges**

To grant a privilege to an account or group, use the `net rpc rights grant`{.literal} command.

For example, grant the `SePrintOperatorPrivilege`{.literal} privilege to the *`DOMAIN`{.literal}*`\printadmin`{.literal} group:

``` {.language-plaintext tabindex="-1"}
# net rpc rights grant "DOMAIN\printadmin" SePrintOperatorPrivilege -U "DOMAIN\administrator"
```

``` {.language-plaintext tabindex="-1"}
Enter DOMAIN\administrator's password:
Successfully granted rights.
```

**Revoking privileges**

To revoke a privilege from an account or group, use the `net rpc rights revoke`{.literal} command.

For example, to revoke the `SePrintOperatorPrivilege`{.literal} privilege from the *`DOMAIN`{.literal}*`\printadmin`{.literal} group:

``` {.language-plaintext tabindex="-1"}
# net rpc rights remoke "DOMAIN\printadmin" SePrintOperatorPrivilege -U "DOMAIN\administrator"
```

``` {.language-plaintext tabindex="-1"}
Enter DOMAIN\administrator's password:
Successfully revoked rights.
```

#### [1.20.3. Using the net rpc share command](#using-the-net-rpc-share-command) {#using-the-net-rpc-share-command .title}

The `net rpc share`{.literal} command provides the capability to list, add, and remove shares on a local or remote Samba or Windows server.

**Listing shares**

To list the shares on an SMB server, use the `net rpc share list`{.literal} command. Optionally, pass the `-S `{.literal}*`server_name`{.literal}* parameter to the command to list the shares of a remote server. For example:

``` {.language-plaintext tabindex="-1"}
# net rpc share list -U "DOMAIN\administrator" -S server_name
```

``` {.language-plaintext tabindex="-1"}
Enter DOMAIN\administrator's password:
IPC$
share_1
share_2
...
```

Note

Shares hosted on a Samba server that have `browseable = no`{.literal} set in their section in the `/etc/samba/smb.conf`{.literal} file are not displayed in the output.

**Adding a share**

The `net rpc share add`{.literal} command enables you to add a share to an SMB server.

For example, to add a share named `example`{.literal} on a remote Windows server that shares the `C:\example\`{.literal} directory:

``` {.language-plaintext tabindex="-1"}
# net rpc share add example="C:\example" -U "DOMAIN\administrator" -S server_name
```

Note

You must omit the trailing backslash in the path when specifying a Windows directory name.

To use the command to add a share to a Samba server:

-   The user specified in the `-U`{.literal} parameter must have the `SeDiskOperatorPrivilege`{.literal} privilege granted on the destination server.
-   You must write a script that adds a share section to the `/etc/samba/smb.conf`{.literal} file and reloads Samba. The script must be set in the `add share command`{.literal} parameter in the `[global]`{.literal} section in `/etc/samba/smb.conf`{.literal}. For further details, see the `add share command`{.literal} description in the `smb.conf(5)`{.literal} man page on your system.

**Removing a share**

The `net rpc share delete`{.literal} command enables you to remove a share from an SMB server.

For example, to remove the share named example from a remote Windows server:

``` {.language-plaintext tabindex="-1"}
# net rpc share delete example -U "DOMAIN\administrator" -S server_name
```

To use the command to remove a share from a Samba server:

-   The user specified in the `-U`{.literal} parameter must have the `SeDiskOperatorPrivilege`{.literal} privilege granted.
-   You must write a script that removes the share's section from the `/etc/samba/smb.conf`{.literal} file and reloads Samba. The script must be set in the `delete share command`{.literal} parameter in the `[global]`{.literal} section in `/etc/samba/smb.conf`{.literal}. For further details, see the `delete share command`{.literal} description in the `smb.conf(5)`{.literal} man page on your system.

#### [1.20.4. Using the net user command](#using-the-net-user-command) {#using-the-net-user-command .title}

The `net user`{.literal} command manages user accounts on an Active Directory (AD) Domain Controller (DC) or an NT4 Primary Domain Controller (PDC). It allows you to list all user accounts, add users, and remove users

Note

Specifying a connection method, such as `ads`{.literal} for AD domains or `rpc`{.literal} for NT4 domains, is only required when you list domain user accounts. Other user-related subcommands can auto-detect the connection method.

Pass the `-U `{.literal}*`user_name`{.literal}* parameter to the command to specify a user that is allowed to perform the requested action.

**Listing domain user accounts**

To list all users in an AD domain:

``` {.language-plaintext tabindex="-1"}
# net ads user -U "DOMAIN\administrator"
```

To list all users in an NT4 domain:

``` {.language-plaintext tabindex="-1"}
# net rpc user -U "DOMAIN\administrator"
```

**Adding a user account to the domain**

On a Samba domain member, you can use the `net user add`{.literal} command to add a user account to the domain.

For example, add the `user`{.literal} account to the domain:

1.  Add the account:

    ``` {.language-plaintext tabindex="-1"}
    # net user add user password -U "DOMAIN\administrator"
    ```

    ``` {.language-plaintext tabindex="-1"}
    User user added
    ```

2.  Optional: Use the remote procedure call (RPC) shell to enable the account on the AD DC or NT4 PDC. For example:

    ``` {.language-plaintext tabindex="-1"}
    # net rpc shell -U DOMAIN\administrator -S DC_or_PDC_name
    ```

    ``` {.language-plaintext tabindex="-1"}
    Talking to domain DOMAIN (S-1-5-21-1424831554-512457234-5642315751)

    net rpc> user edit disabled user: no
    Set user's disabled flag from [yes] to [no]

    net rpc> exit
    ```

**Deleting a user account from the domain**

On a Samba domain member, you can use the `net user delete`{.literal} command to remove a user account from the domain.

For example, to remove the `user`{.literal} account from the domain:

``` {.language-plaintext tabindex="-1"}
# net user delete user -U "DOMAIN\administrator"
```

``` {.language-plaintext tabindex="-1"}
User user deleted
```

#### [1.20.5. Using the rpcclient utility](#using-the-rpcclient-utility) {#using-the-rpcclient-utility .title}

The `rpcclient`{.literal} utility runs client-side Microsoft Remote Procedure Call (MS-RPC) functions. It works with local and remote SMB servers. Most features exist in other Samba utilities, so use `rpcclient`{.literal} mainly for testing.

**Prerequisites**

-   The `samba-client`{.literal} package is installed.

**Procedure**

-   You can use the `rpcclient`{.literal} utility to:

    -   Manage the printer Spool Subsystem (SPOOLSS) by assigning a driver to a printer:

        ``` {.language-plaintext tabindex="-1"}
        # rpcclient server_name -U "DOMAIN\administrator" -c 'setdriver "printer_name" "driver_name"'
        ```

        ``` {.language-plaintext tabindex="-1"}
        Enter DOMAIN\administrators password:
        Successfully set printer_name to driver driver_name.
        ```

    -   Retrieve information about an SMB server by listing all file shares and shared printers:

        ``` {.language-plaintext tabindex="-1"}
        # rpcclient server_name -U "DOMAIN\administrator" -c 'netshareenum'
        ```

        ``` {.language-plaintext tabindex="-1"}
        Enter DOMAIN\administrators password:
        netname: Example_Share
            remark:
            path:   C:\srv\samba\example_share\
            password:
        netname: Example_Printer
            remark:
            path:   C:\var\spool\samba\
            password:
        ```

    -   Perform actions by using the Security Account Manager Remote (SAMR) protocol by listing Users on an SMB Server:

        ``` {.language-plaintext tabindex="-1"}
        # rpcclient server_name -U "DOMAIN\administrator" -c 'enumdomusers'
        ```

        ``` {.language-plaintext tabindex="-1"}
        Enter DOMAIN\administrators password:
        user:[user1] rid:[0x3e8]
        user:[user2] rid:[0x3e9]
        ```

        If you run the command against a standalone server or a domain member, it lists the users in the local database. Running the command against an AD DC or NT4 PDC lists the domain users.

        For more information, see the `rpcclient(1)`{.literal} man page on your system.

#### [1.20.6. Using the samba-regedit application](#using-the-samba-regedit-application) {#using-the-samba-regedit-application .title}

Certain settings, such as printer configurations, are stored in the registry on the Samba server. You can use the ncurses-based `samba-regedit`{.literal} application to edit the registry of a Samba server.

**Prerequisites**

-   The `samba-client`{.literal} package is installed.

**Procedure**

-   To start the application, enter:

    ``` {.language-plaintext tabindex="-1"}
    # samba-regedit
    ```

    Use the following keys:

-   Cursor up and cursor down: Navigate through the registry tree and the values.

-   Enter: Opens a key or edits a value.

-   Tab: Switches between the `Key`{.literal} and `Value`{.literal} pane.

-   Ctrl+C: Closes the application.

#### [1.20.7. Using the smbcontrol utility](#using-the-smbcontrol-utility) {#using-the-smbcontrol-utility .title}

The `smbcontrol`{.literal} utility enables you to send command messages to the `smbd`{.literal}, `nmbd`{.literal}, `winbindd`{.literal}, or all of these services. These control messages instruct the service, for example, to reload its configuration.

**Prerequisites**

-   The `samba-common-tools`{.literal} package is installed.

**Procedure**

-   Reload the configuration of the `smbd`{.literal}, `nmbd`{.literal}, `winbindd`{.literal} services by sending the `reload-config`{.literal} message type to the `all`{.literal} destination:

    ``` {.language-plaintext tabindex="-1"}
    # smbcontrol all reload-config
    ```

    For more information, see the `smbcontrol(1)`{.literal} man page on your system.

#### [1.20.8. Using the smbpasswd utility](#using-the-smbpasswd-utility) {#using-the-smbpasswd-utility .title}

The `smbpasswd`{.literal} utility manages user accounts and passwords in the local Samba database. For more information, see the `smbpasswd(8)`{.literal} man page on your system.

**Prerequisites**

-   The `samba-common-tools`{.literal} package is installed.

**Procedure**

1.  If you run the command as a user, `smbpasswd`{.literal} changes the Samba password of the user who run the command. For example:

    ``` {.language-plaintext tabindex="-1"}
    [user@server ~]$ smbpasswd
    New SMB password: password
    Retype new SMB password: password
    ```

2.  If you run `smbpasswd`{.literal} as the `root`{.literal} user, you can use the utility, for example, to:

    -   Create a new user:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# smbpasswd -a user_name
        New SMB password: password
        Retype new SMB password: password
        Added user user_name.
        ```

        Note

        Before you can add a user to the Samba database, you must create the account in the local operating system.

    -   Enable a Samba user:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# smbpasswd -e user_name
        Enabled user user_name.
        ```

    -   Disable a Samba user:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# smbpasswd -x user_name
        Disabled user user_name
        ```

    -   Delete a user:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# smbpasswd -x user_name
        Deleted user user_name.
        ```

#### [1.20.9. Using the smbstatus utility](#using-the-smbstatus-utility) {#using-the-smbstatus-utility .title}

The `smbstatus`{.literal} utility reports the current state of a Samba server, including active connections and file locks. It provides details per `smbd`{.literal} process and per share, such as user, IP address, and security settings. It also lists locked files with `oplock`{.literal} details.

**Prerequisites**

-   The `samba`{.literal} package is installed.
-   The `smbd`{.literal} service is running.

**Procedure**

-   Run the `smbstatus`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    # smbstatus
    ```

    ``` {.language-plaintext tabindex="-1"}
    Samba version 4.15.2
    PID  Username              Group                Machine                            Protocol Version  Encryption  Signing
    ....-------------------------------------------------------------------------------------------------------------------------
    963  DOMAIN\administrator  DOMAIN\domain users  client-pc  (ipv4:192.0.2.1:57786)  SMB3_02           -           AES-128-CMAC

    Service  pid  Machine    Connected at                  Encryption  Signing:
    ....---------------------------------------------------------------------------
    example  969  192.0.2.1  Thu Nov  1 10:00:00 2018 CEST  -           AES-128-CMAC

    Locked files:
    Pid  Uid    DenyMode   Access    R/W     Oplock      SharePath           Name      Time
    ....--------------------------------------------------------------------------------------------------------
    969  10000  DENY_WRITE 0x120089  RDONLY  LEASE(RWH)  /srv/samba/example  file.txt  Thu Nov  1 10:00:00 2018
    ```

    For more information, see the `smbstatus(1)`{.literal} man page on your system.

#### [1.20.10. Using the smbtar utility](#using-the-smbtar-utility) {#using-the-smbtar-utility .title}

The `smbtar`{.literal} utility backs up content of a Server Message Block (SMB) share or its subdirectory. It stores it in a `tar`{.literal} archive. Alternatively, you can write the content to a tape device. For more information, see the `smbtar(1)`{.literal} man page on your system.

**Prerequisites**

-   The `samba-client`{.literal} package is installed.

**Procedure**

-   Use the following command to back up the `demo`{.literal} directory content on the `//server/example/`{.literal} share and store it in `/root/example.tar`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # smbtar -s server -x example -u user_name -p password -t /root/example.tar
    ```

#### [1.20.11. Using the wbinfo utility](#using-the-wbinfo-utility) {#using-the-wbinfo-utility .title}

The `wbinfo`{.literal} utility queries and returns information created and used by the `winbindd`{.literal} service. For more information, see the `wbinfo(1)`{.literal} man page on your system.

**Prerequisites**

-   The `samba-winbind-clients`{.literal} package is installed.

**Procedure**

-   You can use `wbinfo`{.literal}, for example, to:

    -   List domain users:

        ``` {.language-plaintext tabindex="-1"}
        # wbinfo -u
        ```

        ``` {.language-plaintext tabindex="-1"}
        AD\administrator
        AD\guest
        ...
        ```

    -   List domain groups:

        ``` {.language-plaintext tabindex="-1"}
        # wbinfo -g
        ```

        ``` {.language-plaintext tabindex="-1"}
        AD\domain computers
        AD\domain admins
        AD\domain users
        ...
        ```

    -   Display the Security Identifier (SID) of a user:

        ``` {.language-plaintext tabindex="-1"}
        # wbinfo --name-to-sid="AD\administrator"
        ```

        ``` {.language-plaintext tabindex="-1"}
        S-1-5-21-1762709870-351891212-3141221786-500 SID_USER (1)
        ```

    -   Display information about domains and trusts:

        ``` {.language-plaintext tabindex="-1"}
        # wbinfo --trusted-domains --verbose
        ```

        ``` {.language-plaintext tabindex="-1"}
        Domain Name   DNS Domain            Trust Type  Transitive  In   Out
        BUILTIN                             None        Yes         Yes  Yes
        server                              None        Yes         Yes  Yes
        DOMAIN1       domain1.example.com   None        Yes         Yes  Yes
        DOMAIN2       domain2.example.com   External    No          Yes  Yes
        ```

### [1.21. Additional resources](#using-samba-as-a-server_121-additional-resources) {#additional-resources-1 .title}

-   [Setting up Samba and the Clustered Trivial Database (CDTB) to share directories stored on an GlusterFS volume](https://docs.redhat.com/en/documentation/red_hat_gluster_storage/3.5/html/administration_guide/sect-smb)
-   [Mounting an SMB Share](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_file_systems/mounting-an-smb-share)

## [Chapter 2. Deploying an NFS server](#deploying-an-nfs-server) {#chapter-2.-deploying-an-nfs-server .title}

By using the Network File System (NFS) protocol, remote users can mount shared directories over a network. They can use them as if mounted locally. This enables you to consolidate resources onto centralized servers on the network.

### [2.1. Key features of minor NFSv4 versions](#key-features-of-minor-nfsv4-versions) {#key-features-of-minor-nfsv4-versions .title}

Each minor NFSv4 version brings enhancements aimed at improving performance and security. Use these improvements to use the full potential of NFSv4, ensuring efficient and reliable file sharing across networks.

**Key features of NFSv4.2**

Server-side copy
:   Server-side copy is a capability of the NFS server to copy files without transferring the data back and forth over the network.

Sparse files
:   Enables files to have one or more empty spaces, or gaps, which are unallocated or uninitialized data blocks consisting of zeros. This enables applications to map out the location of holes in the sparse file.

Space reservation
:   Clients can reserve or allocate space on the storage server before writing data. This prevents the server from running out of space.

Labeled NFS
:   Enforces data access rights and enables SELinux labels between a client and server for individual files on an NFS file system.

Layout enhancements
:   Provides functionality to enable Parallel NFS (pNFS) servers to collect better performance statistics.

**Key features of NFSv4.1**

Client-side support for pNFS
:   High-speed I/O support to clustered servers enables you to store data on multiple machines and provide direct access to data. It also synchronizes updates to metadata.

Sessions

:   Sessions maintain the state of the server relative to the connections belonging to a client. They provide two key features.

    -   `exactly-once-semantics`{.literal} (EOS) which helps to distinguish between the response of an old and new operation.
    -   Bind multiple network connections for NFS operations, improving performance

**Key features of NFSv4.0**

RPC and security
:   The `RPCSEC_GSS`{.literal} framework enhances Remote Procedure Call (RPC) security. The NFSv4 protocol introduces a new operation for in-band security negotiation. This enables clients to query server policies for accessing file system resources securely.

Procedure and operation structure
:   NFS 4.0 introduces the `COMPOUND`{.literal} procedure, which enables clients to merge multiple operations into a single request to reduce RPCs.

File system model

:   NFS 4.0 retains the hierarchical file system model, treating files as byte streams and encoding names with UTF-8 for internationalization.

    -   **File handle types**

        With volatile file handles, servers can adjust to file system changes and enable clients to adapt as needed without requiring permanent handles.

    -   **Attribute types**

        The file attribute structure includes required, recommended, and named attributes, each serving distinct purposes. Required attributes, derived from NFSv3, are essential for distinguishing file types. Recommended attributes, such as Access Control Lists (ACLs), provide enhanced access control.

    -   **Multi-server namespace**

        Namespaces span across multiple servers, simplify file system transfers based on attributes, support referrals, redundancy, and seamless server migration.

OPEN and CLOSE operations
:   These operations can combine file lookup, creation, and semantic sharing at a single point, ensuring correct file sharing semantics.

File locking
:   File locking is part of the protocol, eliminating the need for RPC callbacks. File lock state is managed by the server under a lease-based model. Failure to renew the lease may result in state release by the server.

Client caching and delegation
:   Caching resembles previous versions, with client-determined timeouts for attribute and directory caching. Delegations in NFS 4.0 allow the server to assign certain responsibilities to the client. This guarantees specific file sharing semantics and enables local file operations without immediate server interaction.

### [2.2. The AUTH_SYS authentication method](#the-authsys-authentication-method) {#the-auth_sys-authentication-method .title}

The `AUTH_SYS`{.literal} method, which is also known as `AUTH_UNIX`{.literal}, is a client authentication mechanism. With `AUTH_SYS`{.literal}, the client sends the User ID (UID) and Group ID (GID) of the user to the server to verify its identity and permissions when accessing files.

It is considered less secure as it relies on the client-provided information, making it susceptible to unauthorized access if misconfigured.

Mapping mechanisms ensure that NFS clients can access files with the appropriate permissions on the server, even if the UID and GID assignments differ between systems. UIDs and GIDs are mapped between NFS client and server by the following mechanisms:

Direct mapping

:   UIDs and GIDs are directly mapped by NFS servers and clients between local and remote systems. This requires consistent UID and GID assignments across all systems participating in NFS file sharing. For example, a user with UID 1000 on a client can only access the files on a share that a user with UID 1000 on the server has access to.

    For a simplified ID management in an NFS environment, administrators often rely on centralized services, such as LDAP or Network Information Service (NIS) to manage UID and GID mappings across multiple systems.

User and Group ID mapping
:   NFS servers and clients can use the `idmapd`{.literal} service to translate UIDs and GIDs between different systems for consistent identification and permission assignment.

### [2.3. The AUTH_GSS authentication method](#the-authgss-authentication-method) {#the-auth_gss-authentication-method .title}

Kerberos is a network authentication protocol that allows secure authentication for clients and servers over a non-secure network. It uses symmetric key cryptography and requires a trusted Key Distribution Center (KDC) to authenticate users and services.

Unlike `AUTH_SYS`{.literal}, `RPCSEC_GSS`{.literal} Kerberos mechanism ensures the server does not depend on the client to correctly represent which user accesses the file. Instead, the system uses cryptography to authenticate users to the server. This prevents a malicious client from impersonating a user without having the Kerberos credentials of that user.

In the `/etc/exports`{.literal} file, the `sec`{.literal} option defines one or multiple methods of Kerberos security that the share should provide. Clients can mount the share with one of these methods where The `sec`{.literal} option supports the following values:

-   `sys`{.literal}: no cryptographic protection (default)
-   `krb5`{.literal}: authentication only
-   `krb5i`{.literal}: authentication and integrity protection
-   `krb5p`{.literal}: authentication, integrity checking, and traffic encryption

Note that the more cryptographic functionality a method provides, the lower is the performance.

### [2.4. File permissions on exported file systems](#file-permissions-on-exported-file-systems) {#file-permissions-on-exported-file-systems .title}

File permissions on exported file systems determine access rights to files and directories for clients accessing them over NFS.

Once a remote host mounts the NFS file system, the only protection each shared file has is its file system permissions. If two users share the same User ID (UID) value, they can mount the same NFS file system on different client systems. In this case, they can modify each other's files.

NFS treats the `root`{.literal} user on the client as equivalent to the `root`{.literal} user on the server. However, by default, the NFS server maps `root`{.literal} to the `nobody`{.literal} account when accessing an NFS share. The `root_squash`{.literal} option controls this behavior.

For more information about this option, see the `exports(5)`{.literal} man page on your system.

### [2.5. Services required on an NFS server](#services-required-on-an-nfs-server) {#services-required-on-an-nfs-server .title}

Red Hat Enterprise Linux (RHEL) uses a combination of a kernel module and user-space processes to provide NFS file shares. Principal services used by NFS servers include kernel modules and user-space processes that provide access to NFS file shares.

The following table includes details of their functions and configuration.

+-------------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Service Name            | NFS versions | Description                                                                                                                                                                                                                                                                                          |
+:========================+:=============+:=====================================================================================================================================================================================================================================================================================================+
| `rpcbind`{.literal}     | 3            | This process accepts port reservations from local remote procedure call (RPC) services, makes them available or advertised. This allows corresponding remote RPC services to access them. The `rpcbind`{.literal} service responds to requests and sets up connections to the specified RPC service. |
+-------------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rpc.mountd`{.literal}  | 3, 4         | This service processes `MOUNT`{.literal} requests from NFSv3 clients, and NFSv4 servers use internal functions of this service.                                                                                                                                                                      |
|                         |              |                                                                                                                                                                                                                                                                                                      |
|                         |              | It checks that the requested NFS share is currently exported by the NFS server and that the client has access permissions.                                                                                                                                                                           |
+-------------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rpc.nfsd`{.literal}    | 3, 4         | This process advertises explicit NFS versions and protocols the server defines. It works with the kernel to meet the dynamic demands of NFS clients. For example, providing server threads each time an NFS client connects.                                                                         |
|                         |              |                                                                                                                                                                                                                                                                                                      |
|                         |              | The `nfs-server`{.literal} service starts this process.                                                                                                                                                                                                                                              |
+-------------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rpc.rquotad`{.literal} | 3, 4         | This service provides user quota information for remote users.                                                                                                                                                                                                                                       |
+-------------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rpc.idmapd`{.literal}  | 4            | This process provides NFSv4 client and server upcalls, mapping between NFSv4 names (strings in *\`user@domain\`* form) and local user and group IDs.                                                                                                                                                 |
+-------------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `gssproxy`{.literal}    | 3, 4         | This service handles `krb5`{.literal} authentication on behalf of `rpc.nfsd`{.literal}.                                                                                                                                                                                                              |
+-------------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `nfsdcld`{.literal}     | 4            | This service provides a NFSv4 client tracking daemon that prevents the server from granting lock reclaims. It prevents reclaims when other clients have taken conflicting locks during a network partition combined with a server reboot.                                                            |
+-------------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rpc.statd`{.literal}   | 3            | This service notifies other NFSv3 clients when the local host reboots, and notifies the kernel when a remote NFSv3 host reboots.                                                                                                                                                                     |
+-------------------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 2.1. Services required on an NFS server

Show more

+-------------------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Module Name       | NFS versions | Description                                                                                                                                                                             |
+:==================+:=============+:========================================================================================================================================================================================+
| `nfsd`{.literal}  | 3, 4         | The NFS kernel module that services requests for shared NFS file systems.                                                                                                               |
+-------------------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `lockd`{.literal} | 3            | This kernel module implements the Network Lock Manager (NLM) protocol, which enables clients to lock files on the server. RHEL loads the module automatically when the NFS server runs. |
+-------------------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 2.2. Modules required on an NFS server

Show more

For more information, see the following man pages in your system:

-   `rpcbind(8)`{.literal}
-   `rpc.mountd(8)`{.literal}
-   `rpc.nfsd(8)`{.literal}
-   `rpc.statd(8)`{.literal}
-   `rpc.rquotad(8)`{.literal}
-   `rpc.idmapd(8)`{.literal}
-   `gssproxy(8)`{.literal}
-   `nfsdcld(8)`{.literal}

### [2.6. The /etc/exports configuration file](#the--etc-exports-configuration-file) {#the-etcexports-configuration-file .title}

The `/etc/exports`{.literal} file controls which directories the server exports. Each line contains an export point, a whitespace-separated list of clients allowed to mount the directory, and options for each client.

The following is the format for an `/etc/exports`{.literal} entry:

``` {.language-plaintext tabindex="-1"}
<directory> <host_or_network_1>(<options_1>) <host_or_network_n>(<options_n>)...
```

The following are the individual parts of an `/etc/exports`{.literal} entry:

**\<directory\>**
:   The directory that is being exported.

**\<host_or_network\>**
:   The host or network to which the export is being shared. For example, you can specify a hostname, an IP address, or an IP network.

**\<options\>**
:   The options for the host or network.

Adding a space between a client and options, changes the behavior. For example, the following lines do not have the same meaning:

``` {.language-plaintext tabindex="-1"}
/projects    client.example.com(rw)
/projects   client.example.com (rw)
```

In the first line, the server allows only `client.example.com`{.literal} to mount the `/projects`{.literal} directory in read-write mode. No other hosts can mount the share. However, the space between `client.example.com`{.literal} and `(rw)`{.literal} in the second line changes the behavior. The server exports the directory to `client.example.com`{.literal} in read-only mode (default setting). All other hosts can mount the share in read-write mode.

The NFS server uses the following default settings for each exported directory:

+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default setting         | Description                                                                                                                                                                                                                          |
+:========================+:=====================================================================================================================================================================================================================================+
| `ro`{.literal}          | Exports the directory in read-only mode.                                                                                                                                                                                             |
+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `sync`{.literal}        | The NFS server does not reply to requests before changes made by previous requests are written to disk.                                                                                                                              |
+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `wdelay`{.literal}      | The server delays writing to the disk if it suspects another write request is pending.                                                                                                                                               |
+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `root_squash`{.literal} | Prevents that the `root`{.literal} user on clients has `root`{.literal} permissions on an exported directory. With `root_squash`{.literal} enabled, the NFS server maps access from `root`{.literal} to the user `nobody`{.literal}. |
+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 2.3. Default options of entries in /etc/exports

Show more

You can view and manage exported file systems by using the `exportfs`{.literal} command. For details see the `exportfs(8)`{.literal} man page on your system.

### [2.7. Configuring an NFSv4-only server](#configuring-an-nfsv4-only-server) {#configuring-an-nfsv4-only-server .title}

If you do not have any NFSv3 clients in your network, you can configure the NFS server to support only NFSv4. You can also support specific minor protocol versions. Using only NFSv4 on the server reduces the number of ports that are open to the network.

**Procedure**

1.  Install the `nfs-utils`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install nfs-utils
    ```

2.  Edit the `/etc/nfs.conf`{.literal} file, and make the following changes:

    a.  Disable the `vers3`{.literal} parameter in the `[nfsd]`{.literal} section to disable NFSv3:

        ``` {.language-plaintext tabindex="-1"}
        [nfsd]
        vers3=n
        ```

    b.  Optional: If you require only specific NFSv4 minor versions, uncomment all `vers4.<minor_version>`{.literal} parameters and set them accordingly, for example:

        ``` {.language-plaintext tabindex="-1"}
        [nfsd]
        vers3=n
        # vers4=y
        vers4.0=n
        vers4.1=n
        vers4.2=y
        ```

        With this configuration, the server provides only NFS version 4.2.

        Important

        If you require only a specific NFSv4 minor version, set only the parameters for the minor versions. Do not uncomment the `vers4`{.literal} parameter to avoid an unpredictable activation or deactivation of minor versions. By default, the `vers4`{.literal} parameter enables or disables all NFSv4 minor versions. However, this behavior changes if you set `vers4`{.literal} in conjunction with other `vers`{.literal} parameters.

3.  Disable all NFSv3-related services:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl mask --now rpc-statd.service rpcbind.service rpcbind.socket
    ```

4.  Configure the `rpc.mountd`{.literal} daemon to not listen for NFSv3 mount requests. Create a `/etc/systemd/system/nfs-mountd.service.d/v4only.conf`{.literal} file with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [Service]
    ExecStart=
    ExecStart=/usr/sbin/rpc.mountd --no-tcp --no-udp
    ```

5.  Reload the `systemd`{.literal} manager configuration and restart the `nfs-mountd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart nfs-mountd
    ```

6.  Optional: Create a directory that you want to share, for example:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir -p /nfs/projects/
    ```

    If you want to share an existing directory, skip this step.

7.  Set the permissions you require on the `/nfs/projects/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # chmod 2770 /nfs/projects/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # chgrp users /nfs/projects/
    ```

    These commands set write permissions for the `users`{.literal} group on the `/nfs/projects/`{.literal} directory. They ensure that the same group is automatically set on new entries created in this directory.

8.  Add an export point to the `/etc/exports`{.literal} file for each directory that you want to share:

    ``` {.language-plaintext tabindex="-1"}
    /nfs/projects/     192.0.2.0/24(rw) 2001:db8::/32(rw)
    ```

    This entry shares the `/nfs/projects/`{.literal} directory to be accessible with read and write access to clients in the `192.0.2.0/24`{.literal} and `2001:db8::/32`{.literal} subnets.

9.  Open the relevant ports in `firewalld`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service nfs
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

10. Enable and start the NFS server:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now nfs-server
    ```

**Verification**

-   On the server, verify that the server provides only the NFS versions that you have configured:

    ``` {.language-plaintext tabindex="-1"}
    # cat /proc/fs/nfsd/versions
    ```

    ``` {.language-plaintext tabindex="-1"}
    -3 +4 -4.0 -4.1 +4.2
    ```

-   On a client, perform the following steps:

    1.  Install the `nfs-utils`{.literal} package:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install nfs-utils
        ```

    2.  Mount an exported NFS share:

        ``` {.language-plaintext tabindex="-1"}
        # mount server.example.com:/nfs/projects/ /mnt/
        ```

    3.  As a user which is a member of the `users`{.literal} group, create a file in `/mnt/`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # touch /mnt/file
        ```

    4.  List the directory to verify that the file was created:

        ``` {.language-plaintext tabindex="-1"}
        # ls -l /mnt/
        ```

        ``` {.language-plaintext tabindex="-1"}
        total 0
        -rw-r--r--. 1 demo users 0 Jan 16 14:18 file
        ```

### [2.8. Configuring an NFSv3 server with optional NFSv4 support](#configuring-an-nfsv3-server-with-optional-nfsv4-support) {#configuring-an-nfsv3-server-with-optional-nfsv4-support .title}

In a network which still uses NFSv3 clients, configure the server to provide shares by using the NFSv3 protocol. If you also have newer clients in your network, you can, additionally, enable NFSv4. By default, Red Hat Enterprise Linux NFS clients use the latest NFS version that the server provides.

**Procedure**

1.  Install the `nfs-utils`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install nfs-utils
    ```

2.  Optional: By default, NFSv3 and NFSv4 are enabled. If you do not require NFSv4 or only specific minor versions, uncomment all `vers4.<minor_version>`{.literal} parameters and set them accordingly:

    ``` {.language-plaintext tabindex="-1"}
    [nfsd]
    # vers3=y
    # vers4=y
    vers4.0=n
    vers4.1=n
    vers4.2=y
    ```

    With this configuration, the server provides only the NFS version 3 and 4.2.

    Important

    If you require only a specific NFSv4 minor version, set only the parameters for the minor versions. Do not uncomment the `vers4`{.literal} parameter to avoid an unpredictable activation or deactivation of minor versions. By default, the `vers4`{.literal} parameter enables or disables all NFSv4 minor versions. However, this behavior changes if you set `vers4`{.literal} in conjunction with other `vers`{.literal} parameters.

3.  By default, NFSv3 RPC services use random ports. To enable a firewall configuration, configure fixed port numbers in the `/etc/nfs.conf`{.literal} file:

    a.  In the `[lockd]`{.literal} section, set a fixed port number for the `nlockmgr`{.literal} RPC service, for example:

        ``` {.language-plaintext tabindex="-1"}
        [lockd]
        port=5555
        ```

        With this setting, the service automatically uses this port number for both the UDP and TCP protocol.

    b.  In the `[statd]`{.literal} section, set a fixed port number for the `rpc.statd`{.literal} service, for example:

        ``` {.language-plaintext tabindex="-1"}
        [statd]
        port=6666
        ```

        With this setting, the service automatically uses this port number for both the UDP and TCP protocol.

4.  Optional: Create a directory that you want to share, for example:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir -p /nfs/projects/
    ```

    If you want to share an existing directory, skip this step.

5.  Set the permissions you require on the `/nfs/projects/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # chmod 2770 /nfs/projects/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # chgrp users /nfs/projects/
    ```

    These commands set write permissions for the `users`{.literal} group on the `/nfs/projects/`{.literal} directory. They ensure that the same group is automatically set on new entries created in this directory.

6.  Add an export point to the `/etc/exports`{.literal} file for each directory that you want to share:

    ``` {.language-plaintext tabindex="-1"}
    /nfs/projects/     192.0.2.0/24(rw) 2001:db8::/32(rw)
    ```

    This entry shares the `/nfs/projects/`{.literal} directory to be accessible with read and write access to clients in the `192.0.2.0/24`{.literal} and `2001:db8::/32`{.literal} subnets.

7.  Open the relevant ports in `firewalld`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service={nfs,rpc-bind,mountd}
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port={5555/tcp,5555/udp,6666/tcp,6666/udp}
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

8.  Enable and start the NFS server:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now rpc-statd nfs-server
    ```

**Verification**

-   On the server, verify that the server provides only the NFS versions that you have configured:

    ``` {.language-plaintext tabindex="-1"}
    # cat /proc/fs/nfsd/versions
    ```

    ``` {.language-plaintext tabindex="-1"}
    +3 +4 -4.0 -4.1 +4.2
    ```

-   On a client, perform the following steps:

    1.  Install the `nfs-utils`{.literal} package:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install nfs-utils
        ```

    2.  Mount an exported NFS share:

        ``` {.language-plaintext tabindex="-1"}
        # mount -o vers=<version> server.example.com:/nfs/projects/ /mnt/
        ```

    3.  Verify that the share was mounted with the specified NFS version:

        ``` {.language-plaintext tabindex="-1"}
        # mount | grep "/mnt"
        ```

        ``` {.language-plaintext tabindex="-1"}
        server.example.com:/nfs/projects/ on /mnt type nfs (rw,relatime,vers=3,...
        ```

    4.  As a user which is a member of the `users`{.literal} group, create a file in `/mnt/`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # touch /mnt/file
        ```

    5.  List the directory to verify that the file was created:

        ``` {.language-plaintext tabindex="-1"}
        # ls -l /mnt/
        total 0
        -rw-r--r--. 1 demo users 0 Jan 16 14:18 file
        ```

### [2.9. Enabling quota support on an NFS server](#enabling-quota-support-on-an-nfs-server) {#enabling-quota-support-on-an-nfs-server .title}

You can restrict the amount of data a user or a group can store by configuring quotas on the file system. On an NFS server, the `rpc-rquotad`{.literal} service ensures that the quota is also applied to users on NFS clients. For more information, see the `quota(1)`{.literal} and `xfs_quota(8)`{.literal} man pages on your system.

**Prerequisites**

-   The NFS server is running and configured.
-   Quotas have been configured on the [ext](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_file_systems/limiting-storage-space-usage-on-ext4-with-quotas#doc-wrapper) or [XFS](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_file_systems/limiting-storage-space-usage-on-xfs-with-quotas) file system.

**Procedure**

1.  Verify that quotas are enabled on the directories that you export:

    -   For ext file system, enter:

        ``` {.language-plaintext tabindex="-1"}
        # quotaon -p /nfs/projects/
        ```

        ``` {.language-plaintext tabindex="-1"}
        group quota on /nfs/projects (/dev/sdb1) is on
        user quota on /nfs/projects (/dev/sdb1) is on
        project quota on /nfs/projects (/dev/sdb1) is off
        ```

    -   For an XFS file system, enter:

        ``` {.language-plaintext tabindex="-1"}
        # findmnt /nfs/projects
        ```

        ``` {.language-plaintext tabindex="-1"}
        TARGET       SOURCE  FSTYPE OPTIONS
        /nfs/projects /dev/sdb1 xfs rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,usrquota,grpquota
        ```

2.  Install the `quota-rpc`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install quota-rpc
    ```

3.  Optional: By default, the quota RPC service runs on port 875. You can run the service on a different port. Append `-p <port_number>`{.literal} to the `RPCRQUOTADOPTS`{.literal} variable in the `/etc/sysconfig/rpc-rquotad`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    RPCRQUOTADOPTS="-p __<port_number>__"
    ```

4.  Optional: By default, remote hosts can only read quotas. To allow clients to set quotas, append the `-S`{.literal} option to the `RPCRQUOTADOPTS`{.literal} variable in `/etc/sysconfig/rpc-rquotad`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    RPCRQUOTADOPTS="-S"
    ```

5.  Open the port in `firewalld`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port=875/udp
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

6.  Enable and start the `rpc-rquotad`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now rpc-rquotad
    ```

**Verification**

1.  On the client:

    a.  Mount the exported share:

        ``` {.language-plaintext tabindex="-1"}
        # mount server.example.com:/nfs/projects/ /mnt/
        ```

    b.  Display the quota. The command depends on the file system of the exported directory. For example:

        -   To display the quota of a specific user on all mounted ext file systems, enter:

            ``` {.language-plaintext tabindex="-1"}
            # quota -u <user_name>
            ```

            ``` {.language-plaintext tabindex="-1"}
            Disk quotas for user demo (uid 1000):
                 Filesystem     space     quota     limit     grace     files     quota      limit     grace
            server.example.com:/nfs/projects
                         0K       100M      200M                  0         0         0
            ```

        -   To display the user and group quota on an XFS file system, enter:

            ``` {.language-plaintext tabindex="-1"}
            # xfs_quota -x -c "report -h" /mnt/
            ```

            ``` {.language-plaintext tabindex="-1"}
            User quota on /nfs/projects (/dev/vdb1)
                        Blocks
            User ID     Used     Soft     Hard     Warn/Grace
            ---------- ---------------------------------
            root        0        0        0        00 [------]
            demo        0        100M     200M     00 [------]
            ```

### [2.10. Enabling NFS over RDMA on an NFS server](#enabling-nfs-over-rdma-on-an-nfs-server) {#enabling-nfs-over-rdma-on-an-nfs-server .title}

Remote Direct Memory Access (RDMA) enables direct data transfer between systems. It improves throughput, reduces latency, and lowers CPU usage on servers and clients. When connected over RDMA, NFS clients can use NFSoRDMA to mount exported directories.

**Prerequisites**

-   The NFS service is running and configured
-   An InfiniBand or RDMA over Converged Ethernet (RoCE) device is installed on the server.
-   IP over InfiniBand (IPoIB) is configured on the server, and the InfiniBand device has an IP address assigned.

**Procedure**

1.  Install the `rdma-core`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install rdma-core
    ```

2.  If the package was already installed, verify that the `xprtrdma`{.literal} and `svcrdma`{.literal} modules in the `/etc/rdma/modules/rdma.conf`{.literal} file are uncommented:

    ``` {.language-plaintext tabindex="-1"}
    # NFS over RDMA client support
    xprtrdma
    # NFS over RDMA server support
    svcrdma
    ```

3.  Optional: By default, NFS over RDMA uses port 20049. If you want to use a different port, set the `rdma-port`{.literal} setting in the `[nfsd]`{.literal} section of the `/etc/nfs.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    rdma-port=<port>
    ```

4.  Open the NFSoRDMA port in `firewalld`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port={20049/tcp,20049/udp}
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

    Adjust the port numbers if you set a different port than 20049.

5.  Restart the `nfs-server`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart nfs-server
    ```

**Verification**

1.  On a client with InfiniBand hardware, perform the following steps:

    a.  Install the following packages:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install nfs-utils rdma-core
        ```

    b.  Mount an exported NFS share over RDMA:

        ``` {.language-plaintext tabindex="-1"}
        # mount -o rdma server.example.com:/nfs/projects/ /mnt/
        ```

        If you set a port number other than the default (20049), pass `port=`{.literal}*`<port_number>`{.literal}* to the command:

        ``` {.language-plaintext tabindex="-1"}
        # mount -o rdma,port=<port_number> server.example.com:/nfs/projects/ /mnt/
        ```

    c.  Verify that the share was mounted with the `rdma`{.literal} option:

        ``` {.language-plaintext tabindex="-1"}
        # mount | grep "/mnt"
        server.example.com:/nfs/projects/ on /mnt type nfs (...,proto=rdma,...)
        ```

### [2.11. Setting up an NFS server with Kerberos in an Identity Management domain](#setting-up-an-nfs-server-with-kerberos-in-a-rhel-identity-management-domain) {#setting-up-an-nfs-server-with-kerberos-in-an-identity-management-domain .title}

If you use Red Hat Enterprise Linux Identity Management (IdM), you can join your NFS server to the IdM domain. This enables you to centrally manage users and groups and to use Kerberos for authentication, integrity protection, and traffic encryption.

**Prerequisites**

-   The NFS server is [enrolled](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-idm-client) in a Red Hat Enterprise Linux Identity Management (IdM) domain.
-   The NFS server is running and configured.

**Procedure**

1.  Obtain a kerberos ticket as an IdM administrator:

    ``` {.language-plaintext tabindex="-1"}
    # kinit admin
    ```

2.  Create a `nfs/<FQDN>`{.literal} service principal:

    ``` {.language-plaintext tabindex="-1"}
    # ipa service-add nfs/nfs_server.idm.example.com
    ```

3.  Retrieve the `nfs`{.literal} service principal from IdM, and store it in the `/etc/krb5.keytab`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-getkeytab -s idm_server.idm.example.com -p nfs/nfs_server.idm.example.com -k /etc/krb5.keytab
    ```

4.  Optional: Display the principals in the `/etc/krb5.keytab`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # klist -k /etc/krb5.keytab
    ```

    ``` {.language-plaintext tabindex="-1"}
    Keytab name: FILE:/etc/krb5.keytab
    KVNO Principal
    ---- --------------------------------------------------------------------------
       1 nfs/nfs_server.idm.example.com@IDM.EXAMPLE.COM
       1 nfs/nfs_server.idm.example.com@IDM.EXAMPLE.COM
       1 nfs/nfs_server.idm.example.com@IDM.EXAMPLE.COM
       1 nfs/nfs_server.idm.example.com@IDM.EXAMPLE.COM
       7 host/nfs_server.idm.example.com@IDM.EXAMPLE.COM
       7 host/nfs_server.idm.example.com@IDM.EXAMPLE.COM
       7 host/nfs_server.idm.example.com@IDM.EXAMPLE.COM
       7 host/nfs_server.idm.example.com@IDM.EXAMPLE.COM
    ```

    By default, the IdM client adds the host principal to the `/etc/krb5.keytab`{.literal} file when you join the host to IdM. If the host principal is missing, use the **`ipa-getkeytab -s`{.literal}**` `{.literal}*`idm_server.idm.example.com`{.literal}*` `{.literal}**`-p`{.literal}**` `{.literal}*`host/nfs_server.idm.example.com`{.literal}*` `{.literal}**`-k /etc/krb5.keytab`{.literal}** command to add it.

5.  Use the `ipa-client-automount`{.literal} utility to configure mapping of IdM IDs.

    a.  If the client is not in the IdM DNS domain, use the `--domain`{.literal} option to specify the primary DNS domain of the IdM deployment. Alternatively, use the `--server`{.literal} option to specify the IdM server to connect to:

        ``` {.language-plaintext tabindex="-1"}
        # ipa-client-automount --domain idm.example.com
        ```

        The `--domain`{.literal} option triggers DNS discovery to determine the IdM servers to use.

    b.  If the client is already in the IdM DNS domain, run the command without the `--domain`{.literal} option:

        ``` {.language-plaintext tabindex="-1"}
        # ipa-client-automount
        ```

        ``` {.language-plaintext tabindex="-1"}
        Searching for IPA server...
        IPA server: DNS discovery
        Location: default
        Continue to configure the system with these values? [no]: yes
        Configured /etc/idmapd.conf
        Restarting sssd, waiting for it to become available.
        Started autofs
        ```

6.  Update your `/etc/exports`{.literal} file, and add the Kerberos security method to the client options. For example:

    ``` {.language-plaintext tabindex="-1"}
    /nfs/projects/       192.0.2.0/24(rw,sec=krb5i)
    ```

    If you want that your clients can select from multiple security methods, specify them separated by colons:

    ``` {.language-plaintext tabindex="-1"}
    /nfs/projects/       192.0.2.0/24(rw,sec=krb5:krb5i:krb5p)
    ```

7.  Reload the exported file systems:

    ``` {.language-plaintext tabindex="-1"}
    # exportfs -r
    ```

### [2.12. Configuring an NFS server with TLS support](#configuring-an-nfs-server-with-tls-support) {#configuring-an-nfs-server-with-tls-support .title}

Without the `RPCSEC_GSS`{.literal} protocol, Network File System (NFS) traffic is unencrypted by default. Starting with Red Hat Enterprise Linux 10, it is possible to configure NFS with Transport Layer Security (TLS). This allows NFS traffic to be encrypted by default.

**Prerequisites**

-   You have configured an NFSv4 server. For instructions, see [Configuring an NFSv4-only server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/deploying-an-nfs-server#configuring-an-nfsv4-only-server).
-   You have a Certificate Authority (CA) certificate.
-   You have installed the `ktls-utils`{.literal} package.

**Procedure**

1.  Create a private key and a certificate signing request (CSR):

    ``` {.language-plaintext tabindex="-1"}
    # openssl req -new -newkey rsa:4096 -noenc \
    -keyout /etc/pki/tls/private/server.example.com.key \
    -out /etc/pki/tls/private/server.example.com.csr \
    -subj "/C=US/ST=State/L=City/O=Organization/CN=server.example.com" \
    -addext "subjectAltName=DNS:server.example.com,IP:192.0.2.1"
    ```

    Important

    Common Name (CN) and Domain Name System (DNS) must match the hostname. IP must match IP of the host.

2.  Send the `/etc/pki/tls/private/server.example.com.csr`{.literal} file to a CA and request a server certificate. Store the received CA certificate and the server certificate on the host.

3.  Import the CA certificate to the system's truststore:

    ``` {.language-plaintext tabindex="-1"}
    # cp ca.crt /etc/pki/ca-trust/source/anchors
    ```

    ``` {.language-plaintext tabindex="-1"}
    # update-ca-trust
    ```

4.  Move the server certificate to the `/etc/pki/tls/certs/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mv server.example.com.crt /etc/pki/tls/certs/
    ```

5.  Ensure the SELinux context is correct on the private key and certificates:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Rv /etc/pki/tls/certs/
    ```

6.  Add the server certificate and private key to the `[authenticate.server]`{.literal} section in the `/etc/tlshd.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    x509.certificate= /etc/pki/tls/certs/server.example.com.crt
    x509.private_key= /etc/pki/tls/private/server.example.com.key
    ```

    Leave the `x509.truststore`{.literal} parameter unset.

7.  Enable and start the `tlshd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now tlshd.service
    ```

**Next steps**

-   [Configuring an NFS client with TLS support](#configuring-an-nfs-client-with-tls-support "2.13. Configuring an NFS client with TLS support")
-   [Configuring an NFS client with mutual TLS support](#configuring-an-nfs-client-with-mutual-tls-support "2.14. Configuring an NFS client with mutual TLS support")

### [2.13. Configuring an NFS client with TLS support](#configuring-an-nfs-client-with-tls-support) {#configuring-an-nfs-client-with-tls-support .title}

If the server supports NFS with TLS, configure the client and mount using `xprtsec=tls`{.literal}. Import the CA certificate, enable the TLS daemon, and mount the share with encryption. TLS helps protect data in transit between client and server.

**Prerequisites**

-   You have configured the NFS server with TLS encryption. For details, see [Configuring an NFS server with TLS support](#configuring-an-nfs-server-with-tls-support "2.12. Configuring an NFS server with TLS support").
-   You have installed the `ktls-utils`{.literal} package.

**Procedure**

1.  Import the Certificate Authority (CA) certificate to the system's truststore:

    ``` {.language-plaintext tabindex="-1"}
    # cp ca.crt /etc/pki/ca-trust/source/anchors
    ```

    ``` {.language-plaintext tabindex="-1"}
    # update-ca-trust
    ```

2.  Enable and start the `tlshd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now tlshd.service
    ```

3.  Mount an NFS share by using TLS encryption:

    ``` {.language-plaintext tabindex="-1"}
    # mount -o xprtsec=tls server.example.com:/nfs/projects/ /mnt/
    ```

**Verification**

-   Verify that the client successfully mounted NFS share with TLS support:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -u tlshd
    ```

    ``` {.language-plaintext tabindex="-1"}
    …
    Apr 01 08:37:56 client.example.com tlshd[10688]: Handshake with server.example.com (192.0.2.1) was successful
    ```

### [2.14. Configuring an NFS client with mutual TLS support](#configuring-an-nfs-client-with-mutual-tls-support) {#configuring-an-nfs-client-with-mutual-tls-support .title}

If the server supports NFS with TLS encryption, configure both the server and client. TLS provides mutual authentication between systems. Configuration includes certificates, TLS daemon setup, and encrypted NFS mounts.

**Prerequisites**

-   You have configured the NFS server with TLS encryption. For details, see [Configuring an NFS server with TLS support](#configuring-an-nfs-server-with-tls-support "2.12. Configuring an NFS server with TLS support").
-   You have installed the `ktls-utils`{.literal} package.

**Procedure**

1.  Create a private key and a certificate signing request (CSR):

    ``` {.language-plaintext tabindex="-1"}
    # openssl req -new -newkey rsa:4096 -noenc \
    -keyout /etc/pki/tls/private/client.example.com.key \
    -out /etc/pki/tls/private/client.example.com.csr \
    -subj "/C=US/ST=State/L=City/O=Organization/CN=client.example.com" \
    -addext "subjectAltName=DNS:client.example.com,IP:192.0.2.2"
    ```

    Important

    Common Name (CN) and Domain Name System (DNS) must match the hostname. IP must match IP of the host.

2.  Send the `/etc/pki/tls/private/client.example.com.csr`{.literal} file to a Certificate Authority (CA) and request a client certificate. Store the received CA certificate and the client certificate on the host.

3.  Import the CA certificate to the system's truststore:

    ``` {.language-plaintext tabindex="-1"}
    # cp ca.crt /etc/pki/ca-trust/source/anchors
    ```

    ``` {.language-plaintext tabindex="-1"}
    # update-ca-trust
    ```

4.  Move the client certificate to the `/etc/pki/tls/certs/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mv client.example.com.crt /etc/pki/tls/certs/
    ```

5.  Ensure the SELinux context is correct on the private key and certificates:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Rv /etc/pki/tls/certs/
    ```

6.  Add the client certificate and private key to the `[authenticate.client]`{.literal} section in the `/etc/tlshd.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    x509.certificate= /etc/pki/tls/certs/client.example.com.crt
    x509.private_key= /etc/pki/tls/private/client.example.com.key
    ```

    Leave the `x509.truststore`{.literal} parameter unset.

7.  Enable and start the `tlshd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now tlshd.service
    ```

8.  Mount an NFS share by using TLS encryption:

    ``` {.language-plaintext tabindex="-1"}
    # mount -o xprtsec=mtls server.example.com:/nfs/projects/ /mnt/
    ```

**Verification**

-   Verify that the client successfully mounted NFS share with TLS support:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -u tlshd
    ```

    ``` {.language-plaintext tabindex="-1"}
    …
    Apr 01 08:37:56 client.example.com tlshd[10688]: Handshake with server.example.com (192.0.2.1) was successful
    ```

## [Legal Notice](#idm139622278273056) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
