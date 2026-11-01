---
{"title": "Accessing Identity Management services", "guide": "accessing_identity_management_services", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/accessing_identity_management_services/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Accessing Identity Management services {#accessing-identity-management-services .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Logging in to IdM and managing its services {#logging-in-to-idm-and-managing-its-services .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140344570969792)

**Abstract**

Before you can perform administration tasks in Red Hat Identity Management (IdM), you must log in to the service. You can use Kerberos and one time passwords as authentication methods in IdM when you log in by using the command line or the IdM Web UI.

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

## [Chapter 1. Logging in to Identity Management from the command line](#logging-in-to-identity-management-from-the-command-line) {#chapter-1.-logging-in-to-identity-management-from-the-command-line .title}

Identity Management (IdM) uses the Kerberos protocol to provide single sign-on (SSO). You can use SSO to authenticate once with a username and password to gain access to all authorized IdM services without the system prompting for the credentials again.

Important

In IdM, the SSSD automatically obtains a ticket-granting ticket (TGT) for a user after the user successfully logs in to the desktop environment on an IdM client machine with the corresponding Kerberos principal name. This means that after logging in, the user is not required to use the **kinit** utility to access IdM resources.

If you have cleared your Kerberos credential cache or your Kerberos TGT has expired, you must manually request a new ticket to maintain access to IdM resources. The following sections present basic user operations when using Kerberos in IdM.

### [1.1. Using kinit to log in to IdM manually](#using-kinit-to-log-in-to-idm-manually_login-cli-krb) {#using-kinit-to-log-in-to-idm-manually .title}

Authenticate to an Identity Management (IdM) environment manually by using the `kinit`{.literal} utility. You can use this utility to obtain and cache a Kerberos ticket-granting ticket (TGT) if your initial ticket has expired or was destroyed.

As an IdM user, when logging onto your local machine you are also automatically logging in to IdM. This means that after logging in, you are not required to use the `kinit`{.literal} utility to access IdM resources.

**Procedure**

-   To authenticate as the current local user, use `kinit`{.literal} without specifying a user name. For example, if you are logged in as *`<example_user>`{.literal}* on the local system:

    ``` {.language-plaintext tabindex="-1"}
    [example_user@server ~]$ kinit
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password for example_user@EXAMPLE.COM:
    [example_user@server ~]$
    ```

    If the user name of the local user does not match any user entry in IdM, the authentication attempt fails:

    ``` {.language-plaintext tabindex="-1"}
    [example_user@server ~]$ kinit
    ```

    ``` {.language-plaintext tabindex="-1"}
    kinit: Client 'example_user@EXAMPLE.COM' not found in Kerberos database while getting initial credentials
    ```

-   To authenticate as a different IdM principal, specify the username with the `kinit`{.literal} command. For example, to log in as the `admin`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    [example_user@server ~]$ kinit admin
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password for admin@EXAMPLE.COM:
    [example_user@server ~]$
    ```

    Note

    Requesting user tickets using `kinit -kt KDB: `{.literal}*`user@EXAMPLE.COM`{.literal}* is disabled. For more information, see the [Why kinit -kt KDB: user@EXAMPLE.COM no longer work after CVE-2024-3183](https://access.redhat.com/solutions/7083713) solution.

**Verification**

-   To verify that the login was successful, use the `klist`{.literal} utility to display the cached TGT. In the following example, the cache contains a ticket for the *`<example_user>`{.literal}* principal, which means that on this particular host, only *`<example_user>`{.literal}* is currently allowed to access IdM services:

    ``` {.language-plaintext tabindex="-1"}
    $ klist
    ```

    ``` {.language-plaintext tabindex="-1"}
    Ticket cache: KEYRING:persistent:0:0
    Default principal: example_user@EXAMPLE.COM

    Valid starting      Expires             Service principal
    11/10/2019 08:35:45     11/10/2019 18:35:45     krbtgt/EXAMPLE.COM@EXAMPLE.COM
    ```

### [1.2. Destroying a user's active Kerberos ticket](#destroying-a-users-active-kerberos-ticket) {#destroying-a-users-active-kerberos-ticket .title}

You can clear the credentials cache by destroying your active Kerberos ticket. Destroying a Kerberos ticket ensures that any subsequent requests for services require a new ticket-granting ticket (TGT).

**Procedure**

-   To destroy your Kerberos ticket:

    ``` {.language-plaintext tabindex="-1"}
    [example_user@server ~]$ kdestroy
    ```

**Verification**

-   To check that the Kerberos ticket has been destroyed:

    ``` {.language-plaintext tabindex="-1"}
    [example_user@server ~]$ klist
    ```

    ``` {.language-plaintext tabindex="-1"}
    klist: Credentials cache keyring 'persistent:0:0' not found
    ```

### [1.3. Configuring an external system for Kerberos authentication](#configuring-an-external-system-for-kerberos-authentication_login-cli-krb) {#configuring-an-external-system-for-kerberos-authentication .title}

Configure a system outside the Identity Management (IdM) domain for Kerberos authentication by defining an IdM-specific Kerberos configuration file and setting the `KRB5_CONFIG`{.literal} environment variable.

Enabling Kerberos authentication on external systems is especially useful when your infrastructure includes multiple realms or overlapping domains. It is also useful if the system has not been enrolled into any IdM domain through `ipa-client-install`{.literal}.

**Prerequisites**

-   The `krb5-workstation`{.literal} package is installed on the external system. To verify the installation, use the following CLI command:

    ``` {.language-plaintext tabindex="-1"}
    # dnf list installed krb5-workstation
    ```

    ``` {.language-plaintext tabindex="-1"}
    Installed Packages
    krb5-workstation.x86_64    1.16.1-19.el8     @BaseOS
    ```

**Procedure**

1.  Copy the `/etc/krb5.conf`{.literal} file from the IdM server to the external system. For example:

    ``` {.language-plaintext tabindex="-1"}
    # scp /etc/krb5.conf root@externalsystem.example.com:/etc/krb5_ipa.conf
    ```

    Warning

    Do not overwrite the existing `krb5.conf`{.literal} file on the external system.

2.  On the external system, set the terminal session to use the copied IdM Kerberos configuration file:

    ``` {.language-plaintext tabindex="-1"}
    $ export KRB5_CONFIG=/etc/krb5_ipa.conf
    ```

    The `KRB5_CONFIG`{.literal} variable exists only temporarily until you log out. To prevent this loss, export the variable with a different file name.

3.  Copy the Kerberos configuration snippets from the `/etc/krb5.conf.d/`{.literal} directory to the external system.

    Users on the external system can now use the `kinit`{.literal} utility to authenticate against the IdM server.

## [Chapter 2. Viewing, starting and stopping the Identity Management services](#viewing-starting-and-stopping-the-identity-management-services) {#chapter-2.-viewing-starting-and-stopping-the-identity-management-services .title}

Monitor Identity Management (IdM) services to ensure domain availability and to apply any changes you make to the system. By using the `systemctl`{.literal} and `ipactl`{.literal} utilities, you can verify service status, restart components after manual configuration changes, and recover from system interruptions.

### [2.1. Overview of IdM server and client services](#overview-of-idm-server-and-client-services) {#overview-of-idm-server-and-client-services .title}

IdM servers and clients run a number of core system services, including Kerberos, LDAP, and DNS. Review the relationship between IdM functions, such as authentication, directory storage, and certificate management, and the corresponding system daemons of these functions.

#### [2.1.1. List of services hosted by IdM servers](#list_of_services_hosted_by_idm_servers) {#list-of-services-hosted-by-idm-servers .title}

Most of the following services are not strictly required to be installed on the IdM server. For example, you can install services such as a certificate authority (CA) or DNS server on an external server outside the IdM domain.

-   **Kerberos**: The `krb5kdc`{.literal} and `kadmin`{.literal} services.

IdM uses the **Kerberos** protocol to support single sign-on. With Kerberos, users only need to present the correct username and password once and can access IdM services without the system prompting for credentials again.

Kerberos is divided into two parts:

-   The `krb5kdc`{.literal} service is the Kerberos Authentication service and Key Distribution Center (KDC) daemon.
-   The `kadmin`{.literal} service is the Kerberos database administration program.

For information about how to authenticate using Kerberos in IdM, see [Logging in to Identity Management from the command line](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-identity-management-from-the-command-line)

[Logging in to IdM in the Web UI: Using a Kerberos ticket](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-idm-in-the-web-ui-using-a-kerberos-ticket).

-   **LDAP directory server**: The `dirsrv`{.literal} service.

The IdM **LDAP directory server** instance stores all IdM information, such as information related to Kerberos, user accounts, host entries, services, policies, DNS, and others. The LDAP directory server instance is based on the same technology as [Red Hat Directory Server](https://docs.redhat.com/en/documentation/red_hat_directory_server). However, it is tuned to IdM-specific tasks.

-   **Certificate Authority**: The `pki-tomcatd`{.literal} service.

The integrated **certificate authority (CA)** is based on the same technology as [Red Hat Certificate System](https://docs.redhat.com/en/documentation/red_hat_certificate_system). `pki`{.literal} is the command line for accessing Certificate System services.

You can also install the server without the integrated CA if you create and provide all required certificates independently.

For more information, see [Planning your CA services](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/planning-your-ca-services).

-   **Domain Name System (DNS)**: The `named`{.literal} service.

IdM uses **DNS** for dynamic service discovery. The IdM client installation utility can use information from DNS to automatically configure the client machine. After the client is enrolled in the IdM domain, it uses DNS to locate IdM servers and services within the domain. The `BIND`{.literal} (Berkeley Internet Name Domain) implementation of the DNS (Domain Name System) protocols in Red Hat Enterprise Linux includes the `named`{.literal} DNS server.

For information, see [Planning your DNS services and host names](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/planning-your-dns-services-and-host-names).

-   **Apache HTTP Server**: The `httpd`{.literal} service.

The **Apache HTTP web server** provides the IdM Web UI, and also manages communication between the Certificate Authority and other IdM services.

-   **Samba / Winbind**: The `smb`{.literal} and `winbind`{.literal} services.

Samba implements the Server Message Block (SMB) protocol, also known as the Common Internet File System (CIFS) protocol, in Red Hat Enterprise Linux. Via the smb service, the SMB protocol enables you to access resources on a server, such as file shares and shared printers. If you have configured a Trust with an Active Directory (AD) environment, the\`Winbind\` service manages communication between IdM servers and AD servers.

-   **One-time password (OTP) authentication**: The `ipa-otpd`{.literal} services.

One-time passwords (OTP) are passwords that are generated by an authentication token for only one session, as part of two-factor authentication. OTP authentication is implemented in Red Hat Enterprise Linux through the `ipa-otpd`{.literal} service.

For more information, see [Logging in to the Identity Management Web UI using one time passwords](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-the-identity-management-web-ui-using-one-time-passwords).

-   **OpenDNSSEC**: The `ipa-dnskeysyncd`{.literal} service.

**OpenDNSSEC** is a DNS manager that automates the process of keeping track of DNS security extensions (DNSSEC) keys and the signing of zones. The `ipa-dnskeysyncd`{.literal} service manages synchronization between the IdM Directory Server and OpenDNSSEC.

Note

DNSSEC is only available as Technology Preview in IdM.

#### [2.1.2. List of services hosted by IdM clients](#list_of_services_hosted_by_idm_clients) {#list-of-services-hosted-by-idm-clients .title}

-   **System Security Services Daemon**: The `sssd`{.literal} service.

The **System Security Services Daemon** (SSSD) is the client-side application that manages user authentication and caching credentials. Caching enables the local system to continue normal authentication operations if the IdM server becomes unavailable or if the client goes offline.

For more information, see [Understanding SSSD and its benefits](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_authentication_and_authorization_in_rhel/understanding-sssd-and-its-benefits).

-   **Certmonger**: The `certmonger`{.literal} service.

The `certmonger`{.literal} service monitors and renews the certificates on the client. It can request new certificates for the services on the system.

For more information, see [Obtaining an IdM certificate for a service using certmonger](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_certificates_in_idm/obtaining-an-idm-certificate-for-a-service-using-certmonger-assembly).

### [2.2. Viewing the status of IdM services](#viewing-the-status-of-idm-services) {#viewing-the-status-of-idm-services .title}

Verify the operational state of Identity Management (IdM) components by using the `ipactl`{.literal} utility. Monitoring these services ensures that core domain functions, such as authentication and directory lookups, are active and responding to requests.

**Procedure**

-   To view the status of the IdM services that are configured on your IdM server, run the `ipactl status`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipactl status
    ```

    ``` {.language-plaintext tabindex="-1"}
    Directory Service: RUNNING
    krb5kdc Service: RUNNING
    kadmin Service: RUNNING
    named Service: RUNNING
    httpd Service: RUNNING
    pki-tomcatd Service: RUNNING
    smb Service: RUNNING
    winbind Service: RUNNING
    ipa-otpd Service: RUNNING
    ipa-dnskeysyncd Service: RUNNING
    ipa: INFO: The ipactl command was successful
    ```

    The output of the `ipactl status`{.literal} command on your server depends on your IdM configuration. For example, if an IdM deployment does not include a DNS server, the `named`{.literal} service is not present in the list.

    Note

    You cannot use the IdM web UI to view the status of all the IdM services running on a particular IdM server. Kerberized services running on different servers can be viewed in the **Identity** → **Services** tab of the IdM web UI.

### [2.3. Starting and stopping the entire Identity Management server](#starting-and-stopping-the-entire-identity-management-server) {#starting-and-stopping-the-entire-identity-management-server .title}

Use the `ipa`{.literal} systemd service to stop, start, or restart the entire IdM server along with all the installed services. Using the `systemctl`{.literal} utility to control the `ipa`{.literal} systemd service ensures all services are stopped, started, or restarted in the appropriate order.

The `ipa`{.literal} systemd service also upgrades the RHEL IdM configuration before starting the IdM services, and it uses the proper SELinux contexts when administrating with IdM services. You do not need to have a valid Kerberos ticket to run the `systemctl ipa`{.literal} commands.

Important

-   Do not directly use the `ipactl`{.literal} utility to start, stop, or restart IdM services. Use the `systemctl ipa`{.literal} commands instead, which call the `ipactl`{.literal} utility in a predictable environment.
-   You cannot use the IdM web UI to perform the `ipactl`{.literal} commands.

**Procedure**

-   To start the entire IdM server:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start ipa
    ```

-   To stop the entire IdM server:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop ipa
    ```

-   To restart the entire IdM server:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart ipa
    ```

**Verification**

-   To show the status of all the IdM services, use the `ipactl`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    # ipactl status
    ```

### [2.4. Starting and stopping an individual Identity Management service](#starting-and-stopping-an-individual-identity-management-service) {#starting-and-stopping-an-individual-identity-management-service .title}

Manage individual Identity Management (IdM) services to apply manual configuration changes when troubleshooting or tuning System Security Services Daemon (SSSD) settings.

Important

To restart multiple IdM domain services, always use `systemctl restart ipa`{.literal}. Because of dependencies between the services installed with the IdM server, the order in which they are started and stopped is critical. The `ipa`{.literal} systemd service ensures that the services are started and stopped in the appropriate order.

**Procedure**

-   To start a particular IdM service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start <name>.service
    ```

-   To stop a particular IdM service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop <name>.service
    ```

    Important

    You cannot use the IdM web UI to start or stop the individual services running on IdM servers. You can only use the web UI to modify the settings of a Kerberized service by navigating to `Identity`{.literal} → `Services`{.literal} and selecting the service.

-   To restart a particular IdM service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart <name>.service
    ```

    For example, to apply the changes you have made in the `/etc/sssd/sssd.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd.service
    ```

    Note that for changes that affect IdM identity ranges, a complete server reboot is recommended.

**Verification**

-   To view the status of a particular IdM service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status <name>.service
    ```

**Additional resources**

-   [Starting and stopping the entire Identity Management server](#starting-and-stopping-the-entire-identity-management-server "2.3. Starting and stopping the entire Identity Management server")

### [2.5. Displaying IdM software version](#displaying-idm-software-version) {#displaying-idm-software-version .title}

Identify the version of your Identity Management (IdM) installation to ensure compatibility with client systems or to provide technical details during troubleshooting.

You can display the IdM version number with:

-   The IdM WebUI
-   `ipa`{.literal} commands
-   `rpm`{.literal} commands

**Procedure**

-   To view the version through the Web UI, select **About** from the user menu in the upper-right corner.

-   To display the version from the command line, use the `ipa --version`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa --version
    ```

    ``` {.language-plaintext tabindex="-1"}
    VERSION: 4.8.0, API_VERSION: 2.233
    ```

-   To display the version when IdM services are not operating properly, use the `rpm`{.literal} utility to determine the version number of the `ipa-server`{.literal} package that is currently installed:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# rpm -q ipa-server
    ```

    ``` {.language-plaintext tabindex="-1"}
    ipa-server-4.8.0-11.module+el8.1.0+4247+9f3fd721.x86_64
    ```

## [Chapter 3. Introduction to the IdM command-line utilities](#introduction-to-the-idm-command-line-utilities) {#chapter-3.-introduction-to-the-idm-command-line-utilities .title}

You can use the Identity Management (IdM) command-line interface (CLI) and utilities to automate basic administrative tasks, such as creating users and managing certificates.

### [3.1. Prerequisites](#prerequisites) {#prerequisites .title}

-   An installed and accessible Identity Management (IdM) server.
-   To use the IPA command-line interface, authenticate to IdM with a valid Kerberos ticket.

### [3.2. What is the IPA command-line interface](#what-is-the-ipa-command-line-interface) {#what-is-the-ipa-command-line-interface .title}

Manage your Identity Management (IdM) environment by using the IPA command-line interface (CLI). The CLI provides a comprehensive set of subcommands to automate the management of users and hosts, security policies, and certificates.

You can use the IPA CLI to perform the following actions:

-   Add, manage, or remove users, groups, hosts and other objects in the network.
-   Manage certificates.
-   Search the directory to find specific entries and view their details.
-   Display and list objects.
-   Set access rights.
-   Access help to find the correct command syntax and options.

### [3.3. What is the IPA help](#what-is-the-ipa-help) {#what-is-the-ipa-help .title}

Access the built-in Identity Management (IdM) documentation for command syntax, usage examples, and available subcommands. The IPA command-line interface (CLI) generates available help topics from loaded IdM plugin modules.

The `ipa help`{.literal} utility follows a specific structure for queries:

``` {.language-plaintext tabindex="-1"}
$ ipa help [TOPIC | COMMAND | topics | commands]
```

-   **`[]`{.literal}** --- Brackets mean that all parameters are optional and you can write just `ipa help`{.literal} and the command will be executed.

-   **`|`{.literal}** --- The pipe character means **or**. Therefore, you can specify a `TOPIC`{.literal}, a `COMMAND`{.literal}, or `topics`{.literal}, or `commands`{.literal}, with the basic `ipa help`{.literal} command:

    -   **`topics`{.literal}** --- You can run the command `ipa help topics`{.literal} to display a list of topics that are covered by the IPA help, such as `user`{.literal}, `cert`{.literal}, `server`{.literal} and many others.
    -   **`TOPIC`{.literal}** --- The **TOPIC** with capital letters is a variable. Therefore, you can specify a particular topic, for example, `ipa help user`{.literal}.
    -   **`commands`{.literal}** --- You can enter the command `ipa help commands`{.literal} to display a list of commands which are covered by the IPA help, for example, `user-add`{.literal}, `ca-enable`{.literal}, `server-show`{.literal} and many others.
    -   **`COMMAND`{.literal}** --- The **COMMAND** with capital letters is a variable. Therefore, you can specify a particular command, for example, `ipa help user-add`{.literal}.

When you enter the `ipa help`{.literal} command without options, the system displays information about basic help usage and the most common command examples.

### [3.4. Using IPA help topics](#using-ipa-help-topics) {#using-ipa-help-topics .title}

You can use the `ipa help topics`{.literal} to discover available plugins and to view specific command examples for objects such as users, hosts, or certificates.

**Procedure**

1.  Open a terminal and connect to the IdM server.

2.  To display a list of topics covered by help, run `ipa help topics`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa help topics
    ```

3.  To view documentation for a specific category, run the `ipa help `{.literal}*`<topic_name>`{.literal}* command. Replace the *`<topic_name>`{.literal}* placeholder with a category listed in the previous step. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa help user
    ```

4.  Optional: To view long help output one screen at a time, pipe the command to the `less`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa help user | less
    ```

    You can then scroll down and read the whole help.

    The IPA CLI displays a help page for the `user`{.literal} topic. After reading the overview, you can see many examples with patterns for working with topic commands.

### [3.5. Using IPA help commands](#using-ipa-help-commands) {#using-ipa-help-commands .title}

You can use `ipa help commands`{.literal} to list every action supported by the Identity Management (IdM) server. You can also display required arguments and optional parameters for specific commands.

**Procedure**

1.  Open a terminal and connect to the IdM server.

2.  To display a list of commands covered by help, run `ipa help commands`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa help commands
    ```

3.  To view documentation for a specific command, run the `ipa help `{.literal}*`<command>`{.literal}* command. Replace the *`<command>`{.literal}* placeholder with a category listed in the previous step. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa help user-add
    ```

### [3.6. Structure of IPA commands](#structure-of-ipa-commands) {#structure-of-ipa-commands .title}

The IPA CLI uses a predictable structure that combines an object with a specific action. You can use this pattern to perform administrative tasks across different functional areas of IdM.

The IPA CLI distinguishes the following types of commands:

-   **Built-in commands** --- Built-in commands available on every IdM server.
-   **Plug-in provided commands** --- Extended functions provided by specific IdM modules.

For most IdM entries, the CLI follows a standard `ipa `{.literal}*`<object>`{.literal}*`-`{.literal}*`<action>`{.literal}* structure.

Common objects:

-   Users
-   Hosts
-   DNS records
-   Certificates
-   And more.

For most of these objects, the IPA CLI includes commands to:

-   Add (`add`{.literal})
-   Modify (`mod`{.literal})
-   Delete (`del`{.literal})
-   Search (`find`{.literal})
-   Display (`show`{.literal})

Commands have the following structure:

`ipa user-add`{.literal}, `ipa user-mod`{.literal}, `ipa user-del`{.literal}, `ipa user-find`{.literal}, `ipa user-show`{.literal}

`ipa host-add`{.literal}, `ipa host-mod`{.literal}, `ipa host-del`{.literal}, `ipa host-find`{.literal}, `ipa host-show`{.literal}

`ipa dnsrecord-add`{.literal}, `ipa dnsrecord-mod`{.literal}, `ipa dnsrecord-del`{.literal}, `ipa dnsrecord-find`{.literal}, `ipa dnrecord-show`{.literal}

You can create a user with the `ipa user-add [options]`{.literal}, where `[options]`{.literal} are optional. If you use just the `ipa user-add`{.literal} command, the script asks you for details one by one.

Note that the `[options]`{.literal} `--raw`{.literal} and `--structured`{.literal} are mutually exclusive and should not be run together.

To change an existing object, you must to define the object, therefore the command also includes an object: `ipa user-mod `{.literal}*`<user_name>`{.literal}*.

### [3.7. Using an IPA command to add a user account to IdM](#using-an-ipa-command-to-add-a-user-account-to-idm) {#using-an-ipa-command-to-add-a-user-account-to-idm .title}

Create new user entries in the Identity Management (IdM) database by using the IPA command-line interface (CLI).

**Prerequisites**

-   You have administrator privileges.

**Procedure**

1.  Open a terminal and connect to the IdM server.

2.  To add a user interactively, run the `ipa user-add`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-add
    ```

    The command prompts you to provide basic data necessary for creating a user account.

3.  In the **First name:** field, enter the first name of the new user and press **Enter**.

4.  In the **Last name:** field, enter the last name of the new user and press **Enter**.

5.  In the **User login \[suggested user name\]:** enter the user name, or just press **Enter** to accept the suggested user name.

    The user name must be unique for the whole IdM database. If an error occurs because that user name already exists, repeat the process with the `ipa user-add`{.literal} command and use a different, unique user name.

    After you add the user name, the user account is added to the IdM database and the IPA command-line interface (CLI) prints the following output:

    ``` {.language-plaintext tabindex="-1"}
    ----------------------
    Added user "euser"
    ----------------------
    User login: euser
    First name: Example
    Last name: User
    Full name: Example User
    Display name: Example User
    Initials: EU
    Home directory: /home/euser
    GECOS: Example User
    Login shell: /bin/sh
    Principal name: euser@IDM.EXAMPLE.COM
    Principal alias: euser@IDM.EXAMPLE.COM
    Email address: euser@idm.example.com
    UID: 427200006
    GID: 427200006
    Password: False
    Member of groups: ipausers
    Kerberos keys available: False
    ```

    Note

    By default, the account does not have a password. To add a password while creating a user account, use the `ipa user-add`{.literal} command with the following syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-add --first=<user_name> --last=<user_surname> --password
    ```

    The IPA CLI then prompts you to add or confirm a user name and password.

    If the user has been created already, you can add the password with the `ipa user-mod`{.literal} command.

### [3.8. Using an IPA command to modify a user account in IdM](#using-an-ipa-command-to-modify-a-user-account-in-idm) {#using-an-ipa-command-to-modify-a-user-account-in-idm .title}

Update existing user attributes and security settings in the Identity Management (IdM) database by using the command-line interface. You can use the `ipa user-mod`{.literal} command to modify parameters such as contact information, login shells, or passwords for any existing user account.

**Prerequisites**

-   You have administrator privileges.

**Procedure**

1.  Open a terminal and connect to the IdM server.

2.  To update a user account, run the `ipa user-mod `{.literal}*`<user_login>`{.literal}* command and include the options for the attributes you want to change. Replace the *`<user_login>`{.literal}* placeholder with the login name of the user:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-mod <user_login> --password
    ```

3.  If you used the `--password`{.literal} option, provide the new password at the prompt and press **Enter**.

    The IPA CLI prints the following output. For example:

    ``` {.language-plaintext tabindex="-1"}
    ----------------------
    Modified user "euser"
    ----------------------
    User login: euser
    First name: Example
    Last name: User
    Home directory: /home/euser
    Principal name: euser@IDM.EXAMPLE.COM
    Principal alias: euser@IDM.EXAMPLE.COM
    Email address: euser@idm.example.com
    UID: 427200006
    GID: 427200006
    Password: True
    Member of groups: ipausers
    Kerberos keys available: True
    ```

    The user password is now set for the account and the user can log into IdM.

### [3.9. Multi-valued attributes in IdM](#multi-valued-attributes-in-idm) {#multi-valued-attributes-in-idm .title}

When you manage Identity Management (IdM) objects with multi-valued attributes, you must provide the complete list of values during updates to prevent unintended data loss.

IdM supports the following methods of supplying multi-valued lists:

-   Using the same command-line argument multiple times within the same command invocation:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa permission-add --right=read --permissions=write --permissions=delete <object_name>
    ```

-   Alternatively, you can enclose the list in curly braces. The shell expands these into individual arguments before execution:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa permission-add --right={read,write,delete} <object_name>
    ```

When you update such multi-valued attributes from the command line, IdM completely overwrites the previous list of values with a new list. Therefore, when updating a multi-valued attribute, you must specify the whole new list, not just a single value you want to add.

**Examples of the overwrite logic**

The following examples illustrate how the IdM database processes modifications to multi-valued attributes. During a modification, the absence of an existing value results in its removal from the record:

-   The **`ipa permission-mod`{.literal}** command updates all previously added permissions:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa permission-mod --right=read --right=write --right=delete <object_name>
    ```

    or

    ``` {.language-plaintext tabindex="-1"}
    $ ipa permission-mod --right={read,write,delete} <object_name>
    ```

-   The **`ipa permission-mod`{.literal}** command deletes the **`--right=delete`{.literal}** argument because it is not included in the command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa permission-mod --right=read --right=write <object_name>
    ```

    or

    ``` {.language-plaintext tabindex="-1"}
    $ ipa permission-mod --right={read,write} <object_name>
    ```

### [3.10. Special characters in the IdM CLI](#special-characters-in-the-idm-cli) {#special-characters-in-the-idm-cli .title}

Handle shell-sensitive characters correctly to ensure command-line arguments are processed as intended. You can use the backslash (`\`{.literal}) escape character to prevent the shell from misinterpreting special symbols within Identity Management (IdM) commands.

For example, to escape an asterisk (\*):

``` {.language-plaintext tabindex="-1"}
$ ipa certprofile-show certificate_profile --out=exported\*profile.cfg
```

Commands with unescaped special characters fail or produce unexpected results because the shell attempts to parse the characters as shell commands rather than literal text.

### [3.11. Server specification in the IdM CLI](#server-specification-in-the-idm-cli) {#server-specification-in-the-idm-cli .title}

The `--force-server`{.literal} global option directs the `ipa`{.literal} tool to a specific Identity Management (IdM) server, bypassing automatic server discovery.

By default, the `ipa`{.literal} tool discovers and connects to an available IdM server automatically.

Specify `--force-server`{.literal} before the subcommand:

``` {.language-plaintext tabindex="-1"}
$ ipa --force-server server.idm.example.com <subcommand> [<options>]
```

Note

If the specified server is unavailable, the command fails without falling back to other servers.

## [Chapter 4. Searching Identity Management entries from the command line](#searching-identity-management-entries-from-the-command-line) {#chapter-4.-searching-identity-management-entries-from-the-command-line .title}

Locate and view Identity Management (IdM) entries by using search filters and display commands.

### [4.1. Overview of listing IdM entries](#overview-of-listing-idm-entries) {#overview-of-listing-idm-entries .title}

Identify specific entries within the Identity Management (IdM) database by using search filters and keywords. You can use `the ipa *-find`{.literal} commands to retrieve lists of objects and to filter results based on user membership or attribute matches.

**Useful search commands**

-   To list all the `find`{.literal} commands, use the `grep`{.literal} utility with the `ipa help`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa help commands | grep find
    ```

-   To list all users in the IdM database, use the following command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-find
    ```

-   To list user groups whose specified attributes contain a keyword, run:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-find <keyword>
    ```

    For example the **`ipa group-find admin`{.literal}** command lists all groups whose names or descriptions include the string `admin`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    ----------------
    3 groups matched
    ----------------
       Group name: admins
       Description: Account administrators group
       GID: 427200002

       Group name: editors
       Description: Limited admins who can edit other users
       GID: 427200002

       Group name: trust admins
       Description: Trusts administrators group
    ```

-   To search for groups that contain a particular user:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-find --user=<user_name>
    ```

-   To search for groups that do not contain a particular user:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa group-find --no-user=<user_name>
    ```

### [4.2. Showing details for a particular entry](#showing-details-for-a-particular-entry) {#showing-details-for-a-particular-entry .title}

Retrieve the full technical configuration and attribute list for a specific Identity Management (IdM) entry. You can use the `ipa `{.literal}*`<object>`{.literal}*`-show`{.literal} command to display detailed information for a single object, such as a host, user, or service, rather than a filtered list of multiple results.

**Procedure**

-   To display details for a specific entry, run the `ipa `{.literal}*`<object>`{.literal}*`-show`{.literal} command followed by the name of the entry. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa host-show server.example.com
    ```

    The CLI displays the full record for the specified object:

    ``` {.language-plaintext tabindex="-1"}
    Host name: server.example.com
    Principal name: host/server.example.com@EXAMPLE.COM
    ...
    ```

### [4.3. Modifying LDAP attribute values for an IPA command option](#modifying-ldap-attribute-values-for-an-ipa-command-option) {#modifying-ldap-attribute-values-for-an-ipa-command-option .title}

You can add or remove values of LDAP attributes for Identity Management (IdM) command options by using the `--addattr`{.literal} and `--delattr`{.literal} options. Unlike passing the full option value directly, these options modify only the specified value without overwriting the remaining existing values.

**Procedure**

1.  Use the `ipa show-mappings`{.literal} command with the IPA command name to display the LDAP attribute mappings:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa show-mappings <command>
    ```

    For example, to list the LDAP attribute mappings for the `config-mod`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa show-mappings config-mod
    -----------------------------
    Number of entries returned 77
    -----------------------------
      ca_renewal_master_server: caRenewalMaster
      enable_migration: ipaMigrationEnabled
      ...
      userobjectclasses: ipauserobjectclasses *
      ...
    ```

2.  Optional: If the output contains too many entries, pipe the command through `grep`{.literal} to filter for the option you need:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa show-mappings <command> | grep <option>
    ```

    For example:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa show-mappings config-mod | grep userobjectclasses
      userobjectclasses: ipauserobjectclasses *
    ```

3.  Note the symbol after the LDAP attribute name, which indicates whether the attribute is required and how many values it can hold:

    +----------------------+-----------------------------------------------+
    | Symbol               | Meaning                                       |
    +:=====================+:==============================================+
    | (none)               | Mandatory, single-valued                      |
    +----------------------+-----------------------------------------------+
    | `+`{.literal}        | Mandatory, multi-valued                       |
    +----------------------+-----------------------------------------------+
    | `?`{.literal}        | Optional, single-valued                       |
    +----------------------+-----------------------------------------------+
    | `*`{.literal}        | Optional, multi-valued                        |
    +----------------------+-----------------------------------------------+

    Show more

    For example, `ipauserobjectclasses *`{.literal} means the attribute is optional and multi-valued.

4.  Use the LDAP attribute name to add or remove a value:

    -   To add a new value, use `--addattr `{.literal}*`<attribute>`{.literal}*`=`{.literal}*`<value>`{.literal}*. For example, to add the `mailRecipient`{.literal} object class to the list of user object classes:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa config-mod --addattr ipauserobjectclasses=mailRecipient
        ```

    -   To remove an existing value, use `--delattr `{.literal}*`<attribute>`{.literal}*`=`{.literal}*`<value>`{.literal}*. For example, to remove the `mailRecipient`{.literal} object class from the list of user object classes:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa config-mod --delattr ipauserobjectclasses=mailRecipient
        ```

        Note

        In this example, `mailRecipient`{.literal} is an object class name. The LDAP attribute `ipauserobjectclasses`{.literal} stores a list of object class names, so each value you add or remove with `--addattr`{.literal} or `--delattr`{.literal} is an object class name, not an LDAP attribute.

**Verification**

-   To verify the change, run the corresponding show command and check that the value is present or absent. For example, after running `ipa config-mod`{.literal}, run:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa config-show | grep objectclasses
      User object classes: top, person, organizationalperson, inetorgperson, inetuser,
                           posixaccount, krbprincipalaux, krbticketpolicyaux, ipaobject,
                           ipasshuser, mepOriginEntry, mailRecipient
    ```

**Additional resources**

-   [Modifying user object classes in the IdM CLI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/modifying-user-and-group-attributes-in-idm#modifying-user-object-classes-in-the-idm-cli)

### [4.4. Adjusting the search size and time limit](#adjusting-the-search-size-and-time-limit) {#adjusting-the-search-size-and-time-limit .title}

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

#### [4.4.1. Adjusting the search size and time limit in the command line](#adjusting-the-search-size-and-time-limit-in-the-command-line) {#adjusting-the-search-size-and-time-limit-in-the-command-line .title}

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

#### [4.4.2. Adjusting the search size and time limit in the Web UI](#adjusting-the-search-size-and-time-limit-in-the-web-ui) {#adjusting-the-search-size-and-time-limit-in-the-web-ui .title}

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

## [Chapter 5. Accessing the IdM Web UI in a web browser](#accessing-the-idm-web-ui-in-a-web-browser) {#chapter-5.-accessing-the-idm-web-ui-in-a-web-browser .title}

Manage Identity Management (IdM) through a graphical interface by accessing the IdM Web UI. You can use a supported web browser to perform administrative tasks, configure user accounts, and manage security settings as an alternative to the command-line interface.

You can access the IdM Web UI as:

IdM users
:   A limited set of operations depending on permissions granted to the user in the IdM server. Basically, active IdM users can log in to the IdM server and configure their own account. They cannot change settings of other users or the IdM server settings.

Administrators
:   Full access rights to the IdM server.

Active Directory users
:   A set of operations depending on permissions granted to the user. Active Directory users can now be administrators for Identity Management.

### [5.1. Prerequisites](#prerequisites_2) {#prerequisites-1 .title}

-   A supported web browser (Mozilla Firefox 38 and later or Google Chrome 46 and later).
-   The DNS name or IP address of the IdM server.

### [5.2. Configuring web browsers for smart card authentication](#configuring-web-browsers-for-smart-card-authentication) {#configuring-web-browsers-for-smart-card-authentication .title}

Enable Post-Handshake Authentication (PHA) in your browser to use smart card access to the Identity Management (IdM) Web UI.

**Procedure**

1.  If you experience problems accessing the IdM Web UI with a smart card, check the logs to see if your browser attempts to use TLS v1.3. The output might look similar to the following:

    ``` {.language-plaintext tabindex="-1"}
    [ssl:error] [pid 125757:tid 140436077168384] [client 999.999.999.999:99999] AH: verify client post handshake
    [ssl:error] [pid 125757:tid 140436077168384] [client 999.999.999.999:99999] AH10158: cannot perform post-handshake authentication
    [ssl:error] [pid 125757:tid 140436077168384] SSL Library Error: error:14268117:SSL routines:SSL_verify_client_post_handshake:extension not received
    ```

2.  Configure your specific browser to resolve the conflict:

    -   For Mozilla Firefox 68 and later, enable TLS PHA:

        a.  Enter `about:config`{.literal} in the address bar to access the Mozilla Firefox preferences menu.
        b.  Enter `security.tls.enable_post_handshake_auth`{.literal} in the search bar.
        c.  Click the toggle button to set the parameter to true.

    -   For Chrome, which currently does not support PHA, disable TLS v1.3:

        a.  Open the `/etc/httpd/conf.d/ssl.conf`{.literal} configuration file.

        b.  Add `-TLSv1.3`{.literal} to the `SSLProtocol`{.literal} option:

            ``` {.language-plaintext tabindex="-1"}
            SSLProtocol all -TLSv1 -TLSv1.1 -TLSv1.3
            ```

3.  Restart the `httpd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    service httpd restart
    ```

    Note that IdM manages the `ssl.conf`{.literal} file and might overwrite its contents during package updates. Verify custom settings after updating IdM packages.

### [5.3. Accessing the Web UI](#accessing-the-web-ui) {#accessing-the-web-ui .title}

Log in to the Identity Management (IdM) Web UI for the first time to begin administrative configuration.

After the first login you can configure your IdM server to authenticate with:

-   Kerberos ticket

    For details, see [Kerberos authentication in Identity Management](#kerberos-authentication-in-identity-management "6.1. Kerberos authentication in Identity Management").

-   Smart card

    For details, see [Configuring the IdM server for smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#configuring-the-idm-server-for-smart-card-authentication).

-   One time password (OTP) --- this can be combined with password and Kerberos authentication.

    For details, see [One time password (OTP) authentication in Identity Management](#one-time-password-otp-authentication-in-identity-management "7.2. One time password (OTP) authentication in Identity Management").

**Procedure**

1.  Type an IdM server URL into the browser address bar. The name will look similarly to the following example:

    ``` {.language-plaintext tabindex="-1"}
    https://server.example.com
    ```

    You just need to change `server.example.com`{.literal} with a DNS name of your IdM server.

    This opens the IdM Web UI login screen in your browser.

    -   If the server does not respond or the login screen does not open, check the DNS settings on the IdM server to which you are connecting.

    -   If you use a self-signed certificate, the browser issues a warning. Check the certificate and accept the security exception to proceed with the login.

        To avoid security exceptions, install a certificate signed by a certificate authority.

2.  On the Web UI login screen, enter the administrator account credentials you added during the IdM server installation.

    For details, see [Installing an Identity Management server: With integrated DNS, with an integrated CA](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-idm-server-with-integrated-dns-with-an-integrated-ca-as-the-root-ca).

    You can enter your personal account credentials as well if they are already entered in the IdM server.

3.  Click Log in.

    After the successful login, you can start configuring the IdM server.

**Additional resources**

-   [Enabling AD users to administer IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/enabling-ad-users-to-administer-idm)

## [Chapter 6. Logging in to IdM in the Web UI: Using a Kerberos ticket](#logging-in-to-idm-in-the-web-ui-using-a-kerberos-ticket) {#chapter-6.-logging-in-to-idm-in-the-web-ui-using-a-kerberos-ticket .title}

Authenticate to the Identity Management (IdM) Web UI automatically with a valid Kerberos ticket from a local system. You can use the single sign-on (SSO) method to access the graphical interface without entering a password in the browser.

### [6.1. Kerberos authentication in Identity Management](#kerberos-authentication-in-identity-management) {#kerberos-authentication-in-identity-management .title}

Identity Management (IdM) uses the Kerberos protocol to support single sign-on (SSO). You can use SSO to provide a username and password only once to obtain a ticket.

The IdM server provides Kerberos authentication immediately after the installation if the DNS and certificate settings have been configured properly.

To use Kerberos authentication on hosts, install:

-   The IdM client
-   The `krb5conf`{.literal} package

**Additional resources**

-   [Preparing the system for IdM client installation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/preparing-the-system-for-idm-client-installation)

### [6.2. Using kinit to log in to IdM manually](#using-kinit-to-log-in-to-idm-manually_login-web-ui-krb) {#using-kinit-to-log-in-to-idm-manually-1 .title}

Authenticate to an Identity Management (IdM) environment manually by using the `kinit`{.literal} utility. You can use this utility to obtain and cache a Kerberos ticket-granting ticket (TGT) if your initial ticket has expired or was destroyed.

As an IdM user, when logging onto your local machine you are also automatically logging in to IdM. This means that after logging in, you are not required to use the `kinit`{.literal} utility to access IdM resources.

**Procedure**

-   To authenticate as the current local user, use `kinit`{.literal} without specifying a user name. For example, if you are logged in as *`<example_user>`{.literal}* on the local system:

    ``` {.language-plaintext tabindex="-1"}
    [example_user@server ~]$ kinit
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password for example_user@EXAMPLE.COM:
    [example_user@server ~]$
    ```

    If the user name of the local user does not match any user entry in IdM, the authentication attempt fails:

    ``` {.language-plaintext tabindex="-1"}
    [example_user@server ~]$ kinit
    ```

    ``` {.language-plaintext tabindex="-1"}
    kinit: Client 'example_user@EXAMPLE.COM' not found in Kerberos database while getting initial credentials
    ```

-   To authenticate as a different IdM principal, specify the username with the `kinit`{.literal} command. For example, to log in as the `admin`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    [example_user@server ~]$ kinit admin
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password for admin@EXAMPLE.COM:
    [example_user@server ~]$
    ```

    Note

    Requesting user tickets using `kinit -kt KDB: `{.literal}*`user@EXAMPLE.COM`{.literal}* is disabled. For more information, see the [Why kinit -kt KDB: user@EXAMPLE.COM no longer work after CVE-2024-3183](https://access.redhat.com/solutions/7083713) solution.

**Verification**

-   To verify that the login was successful, use the `klist`{.literal} utility to display the cached TGT. In the following example, the cache contains a ticket for the *`<example_user>`{.literal}* principal, which means that on this particular host, only *`<example_user>`{.literal}* is currently allowed to access IdM services:

    ``` {.language-plaintext tabindex="-1"}
    $ klist
    ```

    ``` {.language-plaintext tabindex="-1"}
    Ticket cache: KEYRING:persistent:0:0
    Default principal: example_user@EXAMPLE.COM

    Valid starting      Expires             Service principal
    11/10/2019 08:35:45     11/10/2019 18:35:45     krbtgt/EXAMPLE.COM@EXAMPLE.COM
    ```

### [6.3. Configuring the browser for Kerberos authentication](#configuring-the-browser-for-kerberos-authentication) {#configuring-the-browser-for-kerberos-authentication .title}

Configure your web browser for Kerberos authentication to pass your local Kerberos ticket to the Identity Management (IdM) Web UI for automatic single sign-on (SSO) access.

Each browser supports Kerberos in a different way and needs a different configuration. The IdM Web UI includes guidelines for the following browsers:

-   Firefox
-   Chrome

**Procedure**

1.  Open the IdM Web UI login dialog in your web browser.

2.  Click the link for the browser configuration on the Web UI login screen.

3.  Follow the steps on the configuration page.

    After the setup, go back to the IdM Web UI and click **Log in**.

### [6.4. Logging in to the web UI using a Kerberos ticket](#logging-in-to-the-web-ui-using-a-kerberos-ticket) {#logging-in-to-the-web-ui-using-a-kerberos-ticket .title}

Access the Identity Management (IdM) Web UI automatically by using a Kerberos ticket-granting ticket (TGT). The TGT remains valid for a predefined interval, which defaults to 24 hours. You can modify this duration in the IdM Web UI configuration settings.

After the time interval expires, you need to renew the ticket:

-   Using the `kinit`{.literal} command.
-   Using IdM login credentials in the Web UI login dialog.

**Procedure**

-   Open the IdM Web UI.

    If Kerberos authentication works correctly and you have a valid ticket, you can automatically authenticate and the Web UI opens.

    If the ticket is expired, you must authenticate yourself with credentials first. However, next time the IdM Web UI will open automatically without opening the login dialog.

    If you see an error message `Authentication with Kerberos failed`{.literal}, verify that your browser is configured for Kerberos authentication. See [Configuring the browser for Kerberos authentication](#configuring-the-browser-for-kerberos-authentication "6.3. Configuring the browser for Kerberos authentication").

### [6.5. Configuring an external system for Kerberos authentication](#configuring-an-external-system-for-kerberos-authentication_login-web-ui-krb) {#configuring-an-external-system-for-kerberos-authentication-1 .title}

Configure a system outside the Identity Management (IdM) domain for Kerberos authentication by defining an IdM-specific Kerberos configuration file and setting the `KRB5_CONFIG`{.literal} environment variable.

Enabling Kerberos authentication on external systems is especially useful when your infrastructure includes multiple realms or overlapping domains. It is also useful if the system has not been enrolled into any IdM domain through `ipa-client-install`{.literal}.

**Prerequisites**

-   The `krb5-workstation`{.literal} package is installed on the external system. To verify the installation, use the following CLI command:

    ``` {.language-plaintext tabindex="-1"}
    # dnf list installed krb5-workstation
    ```

    ``` {.language-plaintext tabindex="-1"}
    Installed Packages
    krb5-workstation.x86_64    1.16.1-19.el8     @BaseOS
    ```

**Procedure**

1.  Copy the `/etc/krb5.conf`{.literal} file from the IdM server to the external system. For example:

    ``` {.language-plaintext tabindex="-1"}
    # scp /etc/krb5.conf root@externalsystem.example.com:/etc/krb5_ipa.conf
    ```

    Warning

    Do not overwrite the existing `krb5.conf`{.literal} file on the external system.

2.  On the external system, set the terminal session to use the copied IdM Kerberos configuration file:

    ``` {.language-plaintext tabindex="-1"}
    $ export KRB5_CONFIG=/etc/krb5_ipa.conf
    ```

    The `KRB5_CONFIG`{.literal} variable exists only temporarily until you log out. To prevent this loss, export the variable with a different file name.

3.  Copy the Kerberos configuration snippets from the `/etc/krb5.conf.d/`{.literal} directory to the external system.

4.  Configure the browser on the external system, as described in [Configuring the browser for Kerberos authentication](#configuring-the-browser-for-kerberos-authentication "6.3. Configuring the browser for Kerberos authentication").

    Users on the external system can now use the `kinit`{.literal} utility to authenticate against the IdM server.

### [6.6. Enabling Web UI login for Active Directory users](#enabling-web-ui-login-for-active-directory-users) {#enabling-web-ui-login-for-active-directory-users .title}

Configure the Identity Management (IdM) Web UI to verify Active Directory (AD) user credentials through a cross-forest trust to maintain a single source of identity.

To enable Web UI login for Active Directory users, define an ID override for each Active Directory user in the **Default Trust View**.

**Procedure**

-   To define an ID override for `ad_user@ad.example.com`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [admin@server ~]$ ipa idoverrideuser-add 'Default Trust View' ad_user@ad.example.com
    ```

**Additional resources**

-   [Using ID views for Active Directory users](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/using-id-views-for-active-directory-users)

## [Chapter 7. Logging in to the Identity Management Web UI using one time passwords](#logging-in-to-the-identity-management-web-ui-using-one-time-passwords) {#chapter-7.-logging-in-to-the-identity-management-web-ui-using-one-time-passwords .title}

Authenticate to the Identity Management (IdM) Web UI by using a one-time password (OTP) to provide an additional layer of security. You can use this multi-factor authentication method by combining a standard password with a unique code generated by a hardware or software token.

### [7.1. Prerequisites](#prerequisites_3) {#prerequisites-2 .title}

-   Access to the IdM Web UI in a web browser.

**Additional resources**

-   [Accessing the IdM Web UI in a web browser](#accessing-the-idm-web-ui-in-a-web-browser "Chapter 5. Accessing the IdM Web UI in a web browser")

### [7.2. One time password (OTP) authentication in Identity Management](#one-time-password-otp-authentication-in-identity-management) {#one-time-password-otp-authentication-in-identity-management .title}

Identity Management (IdM) provides multi-factor authentication by combining standard passwords with automatically generated one-time password (OTP). You can use the OTP method to protect user accounts and LDAP clients with an additional security layer.

To generate one time passwords, you can use a hardware or software token. IdM supports both software and hardware tokens.

Identity Management supports the following standard OTP mechanisms:

-   The HMAC-Based One-Time Password (HOTP) algorithm is based on a counter. HMAC stands for Hashed Message Authentication Code.
-   The Time-Based One-Time Password (TOTP) algorithm is an extension of HOTP to support time-based moving factor.

Important

IdM does not support OTP logins for Active Directory trust users.

Warning

The following security and other limitations currently relate to the OTP support in IdM:

-   The most important security limitation is the potential vulnerability to replay attacks across the system. Replication is asynchronous, and an OTP code can therefore be reused during the replication period. A user might be able to log on to two servers at the same time. However, this vulnerability is usually difficult to exploit due to comprehensive encryption.
-   It is not possible to obtain a ticket-granting ticket (TGT) using a client that does not support OTP authentication. This might affect certain use cases, such as authentication using the `mod_auth_kerb`{.literal} module or the Generic Security Services API (GSSAPI).

#### [7.2.1. Available OTP authentication methods](#available_otp_authentication_methods) {#available-otp-authentication-methods .title}

When enabling OTP authentication, you can choose from the following authentication methods:

Two-factor authentication (password + OTP)
:   With this method, the user is always required to enter both a standard password and an OTP code.

Password
:   With this method, the user still has the option to authenticate using a standard password only.

RADIUS proxy server authentication
:   You can use a RADIUS server for OTP validation in IdM.

Global and user-specific authentication methods

:   You can configure these authentication methods either globally or for individual users:

    -   By default, user-specific authentication method settings take precedence over global settings. If no authentication method is set for a user, the globally-defined methods apply.
    -   You can disable per-user authentication method settings for any user. This ensures IdM ignores the per-user settings and always applies the global settings for the user.

Combining multiple authentication methods

:   If you configure multiple authentication methods, any one of them will be sufficient to successfully authenticate the user. For example:

    -   If you configure both two-factor and password authentication, the user must provide the password (first factor), but providing the OTP (second factor) is optional when using the command line:

        ``` {.language-plaintext tabindex="-1"}
        First Factor:
        Second Factor (optional):
        ```

    -   In the web UI, the user must still provide both factors.

However, a minor exception exists when RADIUS and another authentication method are configured:

-   Kerberos always uses RADIUS, but LDAP does not. LDAP only recognizes the password and two-factor authentication methods.
-   If you use an external two-factor authentication provider, use Kerberos from your applications. If you want to let users authenticate with a password only, use LDAP. It is recommended that the applications use Apache modules and SSSD, which allows configuring either Kerberos or LDAP.

#### [7.2.2. GNOME Keyring service support](#gnome_keyring_service_support) {#gnome-keyring-service-support .title}

IdM integrates OTP authentication with the GNOME Keyring service. Note that GNOME Keyring integration requires the user to enter the first and second factors separately:

``` {.language-plaintext tabindex="-1"}
First factor: static_password
Second factor: one-time_password
```

#### [7.2.3. Offline authentication with OTP](#offline_authentication_with_otp) {#offline-authentication-with-otp .title}

IdM supports offline OTP authentication. However, to be able to log in offline, the user must first authenticate when the system is online by entering the static password and OTP separately:

``` {.language-plaintext tabindex="-1"}
First factor: static_password
Second factor: one-time_password
```

If the user enters both passwords separately like this when logging in online, the user can subsequently authenticate even if the central authentication server is unavailable. Note that IdM only prompts for the first-factor traditional static password when the user authenticates offline.

IdM also supports entering both the static password and OTP together in one string in the `First factor`{.literal} prompt. However, this method is not compatible with offline OTP authentication. If the user enters both factors in a single prompt, IdM must contact the central authentication server to validate the credentials, which requires the system to be online.

Important

If you use OTP authentication on devices that also operate offline, such as laptops, Red Hat recommends to enter the static password and OTP separately to make sure offline authentication is available. Otherwise, IdM does not allow you to log in after the system goes offline.

If you want to benefit from OTP offline authentication, apart from entering the static and OTP passwords separately, also make sure to meet the following conditions:

-   The `cache_credentials`{.literal} option in the `/etc/sssd/sssd.conf`{.literal} file is set to `True`{.literal}, which enables caching the first factor password.
-   The first-factor static password meets the password length requirement defined in the `cache_credentials_minimal_first_factor_length`{.literal} option set in `/etc/sssd/sssd.conf`{.literal}. The default minimal length is 8 characters. For more information about the option, see the `sssd.conf(5)`{.literal} man page.

Note

Even if the `krb5_store_password_if_offline`{.literal} option is set to true in the `/etc/sssd/sssd.conf`{.literal} file, SSSD does not attempt to refresh the Kerberos ticket-granting ticket (TGT) when the system returns to an online state. This is because the one-time password (OTP) may already be invalid at that point. To obtain a new TGT in this situation, the user must re-authenticate using both factors.

**Additional resources**

-   [Configuring a RADIUS server for OTP validation in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/accessing_identity_management_services/index#configuring-a-radius-server-for-otp-validation-in-idm)

### [7.3. Enabling the one-time password in the Web UI](#enabling-the-one-time-password-in-the-web-ui) {#enabling-the-one-time-password-in-the-web-ui .title}

Identity Management (IdM) administrators can enable two-factor authentication (2FA) for IdM users either globally or individually.

Enabling 2FA is not the same as enforcing it. If you use logins based on LDAP-binds, IdM users can still authenticate by entering a password only. However, if you use `krb5`{.literal}-based logins, the 2FA is enforced.

Note that there is an option to enforce 2FA for LDAP-binds by enforcing OTP usage for all LDAP clients. For more information, see [Enforcing OTP usage for all LDAP clients](#enforcing-otp-usage-for-all-ldap-clients "7.10. Enforcing OTP usage for all LDAP clients").

**Prerequisites**

-   Administrator privileges

**Procedure**

1.  Log in to the IdM Web UI with IdM `admin`{.literal} privileges.

2.  Open the **Identity → Users → Active users** tab.

3.  Select **example.user** to open the user settings.

4.  In the **User authentication types**, select **Two factor authentication (password + OTP)**.

5.  Click **Save**.

    At this point, the OTP authentication is enabled for the IdM user.

    Now you or **example.user** must assign a new token ID to the **example.user** account.

### [7.4. Configuring a RADIUS server for OTP validation in IdM](#configuring-a-radius-server-for-otp-validation-in-idm) {#configuring-a-radius-server-for-otp-validation-in-idm .title}

Configure a RADIUS proxy in Identity Management (IdM) to offload one-time password (OTP) validation to an external third-party server. You can use this configuration to migrate large deployments from proprietary OTP solutions to IdM-native authentication for specific users.

While each proxy references a single RADIUS server, you can combine this setup with a virtual IP solution to address multiple servers for high availability. Assigning a RADIUS proxy set to a user ensures that IdM prioritizes the external provider and bypasses other authentication mechanisms. Such a solution must be built outside of RHEL IdM with the help of the `keepalived`{.literal} daemon, for example. The administrator then assigns one of these proxy sets to a user. As long as the user has a RADIUS proxy set assigned, IdM bypasses all other authentication mechanisms.

Note

IdM does not provide any token management or synchronization support for tokens in the third-party system.

**Prerequisites**

-   The radius user authentication method is enabled. See [Enabling the one-time password in the Web UI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/accessing_identity_management_services/index#enabling-the-one-time-password-in-the-web-ui_logging-in-to-ipa-in-the-web-ui-using-a-password) for details.

**Procedure**

1.  Add a RADIUS proxy:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa radiusproxy-add proxy_name --secret secret
    ```

    The command prompts you for inserting the required information.

    The configuration of the RADIUS proxy requires the use of a common secret between the client and the server to wrap credentials. Specify this secret in the `--secret`{.literal} parameter.

2.  Assign a user to the added proxy:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-mod radiususer --radius=proxy_name
    ```

3.  If required, configure the user name to be sent to RADIUS:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa user-mod radiususer --radius-username=radius_user
    ```

    As a result, the RADIUS proxy server starts to process the user OTP authentication.

    When the user is ready to be migrated to the IdM native OTP system, you can simply remove the RADIUS proxy assignment for the user.

    Note

    In certain situations, such as running a RADIUS proxy in a slow network, the Identity Management (IdM) Kerberos Distribution Center (KDC) closes the connection before the RADIUS server responds because the connection timed out while waiting for the user to enter the token. You can change the timeout settings of the KDC.

4.  Change the value of the `timeout`{.literal} parameter in the `[otp]`{.literal} section in the `/var/kerberos/krb5kdc/kdc.conf`{.literal} file. For example, to set the timeout to `120`{.literal} seconds:

    ``` {.language-plaintext tabindex="-1"}
    [otp]
    DEFAULT = {
      timeout = 120
      ...
    }
    ```

5.  Restart the `krb5kdc`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart krb5kdc
    ```

**Additional resources**

-   [How to configure FreeRADIUS authentication in FIPS mode (Red Hat Knowledgebase)](https://access.redhat.com/solutions/4650511)

### [7.5. Adding OTP tokens in the Web UI](#adding-otp-tokens-in-the-web-ui) {#adding-otp-tokens-in-the-web-ui .title}

Create and manage software or hardware tokens in the Identity Management (IdM) Web UI to provide one-time passwords (OTP). You can use this configuration to generate unique authentication codes that synchronize with a mobile app or a physical device.

**Prerequisites**

-   Active user account on the IdM server.
-   Administrator has enabled OTP for the particular user account in the IdM Web UI.
-   A software device generating OTP tokens, for example FreeOTP.

**Procedure**

1.  Log in to the IdM Web UI with your user name and password.

2.  To create the token in your mobile phone, open the **Authentication → OTP Tokens** tab.

3.  Click **Add**.

4.  In the **Add OTP token** dialog box, leave everything unfilled and click **Add**.

    At this stage, the IdM server creates a token with default parameters at the server and opens a page with a QR code.

5.  Copy the QR code into your mobile phone.

6.  Click **OK** to close the QR code.

    Now you can generate one time passwords and log in with them to the IdM Web UI.

### [7.6. Logging into the Web UI with a one time password](#logging-into-the-web-ui-with-a-one-time-password) {#logging-into-the-web-ui-with-a-one-time-password .title}

Authenticate to the Identity Management (IdM) Web UI by using a combination of your standard password and a one-time password (OTP).

**Prerequisites**

-   OTP configuration enabled on the Identity Management server for the user account you are using for the OTP authentication. Administrators as well as users themselves can enable OTP.

    To enable the OTP configuration, see [Enabling the one time password in the Web UI](#enabling-the-one-time-password-in-the-web-ui "7.3. Enabling the one-time password in the Web UI").

-   A hardware or software device generating OTP tokens configured.

**Procedure**

1.  In the Identity Management login screen, enter your user name or a user name of the IdM server administrator account.

2.  Add the password for the user name entered above.

3.  Generate a one time password on your device.

4.  Enter the one time password right after the password without a space.

5.  Click **Log in**.

    If the authentication fails, synchronize OTP tokens.

    If your CA uses a self-signed certificate, the browser issues a warning. Check the certificate and accept the security exception to proceed with the login.

    If the IdM Web UI does not open, verify the DNS configuration of your Identity Management server.

    After a successful login, the IdM Web UI opens.

### [7.7. Synchronizing OTP tokens using the Web UI](#synchronizing-otp-tokens-using-the-web-ui) {#synchronizing-otp-tokens-using-the-web-ui .title}

Synchronize your one-time password (OTP) token in the Identity Management (IdM) Web UI. If the login with OTP (One Time Password) fails, OTP tokens are not synchronized correctly.

**Prerequisites**

-   A device generating OTP tokens.

**Procedure**

1.  On the IdM Web UI login screen, click **Sync OTP Token**.

2.  In the login screen, enter your username and the Identity Management password.

3.  Generate one time password and enter it in the **First OTP** field.

4.  Generate another one time password and enter it in the **Second OTP** field.

5.  Optional: Enter the token ID.

6.  Click **Sync OTP Token**.

7.  After a successful synchronization, you can log in to the IdM server.

### [7.8. Changing expired passwords](#changing-expired-passwords) {#changing-expired-passwords .title}

Update your expired Identity Management (IdM) password to regain access to the Web UI and other services. Use the password reset prompt to provide your current credentials and set a new, secure password.

Administrators of Identity Management (IdM) can enforce changing your password at the next login. In this case you must follow the instructions on your terminal to create a new password.

**Prerequisites**

-   Active account on the IdM server.

**Procedure**

1.  In the password expiration login screen, enter the user name.

2.  Add the password for the user name entered above.

3.  In the OTP field, generate a one time password, if you use one time password authentication.

4.  Enter the new password twice for verification.

5.  Click **Reset Password**.

    After a successful password change, the usual login dialog displays. Log in with the new password.

### [7.9. Retrieving an IdM ticket-granting ticket as an OTP or RADIUS user](#retrieving-an-idm-ticket-granting-ticket-as-an-otp-or-radius-user) {#retrieving-an-idm-ticket-granting-ticket-as-an-otp-or-radius-user .title}

To retrieve a Kerberos ticket-granting ticket (TGT) as an OTP user, request an anonymous Kerberos ticket and enable Flexible Authentication via Secure Tunneling (FAST) channel to provide a secure connection between the Kerberos client and Kerberos Distribution Center (KDC).

**Prerequisites**

-   You have enabled OTP for the required user account.

**Procedure**

1.  Initialize the credentials cache by running the following command:

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# kinit -n @IDM.EXAMPLE.COM -c FILE:armor.ccache
    ```

    Note that this command creates the `armor.ccache`{.literal} file that you need to point to whenever you request a new Kerberos ticket.

2.  Request a Kerberos ticket by running the command:

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# kinit -T FILE:armor.ccache <username>@IDM.EXAMPLE.COM
    ```

    ``` {.language-plaintext tabindex="-1"}
    Enter your OTP Token Value.
    ```

**Verification**

-   Display your Kerberos ticket information:

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# klist -C
    ```

    ``` {.language-plaintext tabindex="-1"}
    Ticket cache: KCM:0:58420
    Default principal: <username>@IDM.EXAMPLE.COM

    Valid starting     Expires            Service principal
    05/09/22 07:48:23  05/10/22 07:03:07  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
    config: fast_avail(krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM) = yes
    08/17/2022 20:22:45  08/18/2022 20:22:43  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
    config: pa_type(krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM) = 141
    ```

    The `pa_type = 141`{.literal} indicates OTP/RADIUS authentication.

### [7.10. Enforcing OTP usage for all LDAP clients](#enforcing-otp-usage-for-all-ldap-clients) {#enforcing-otp-usage-for-all-ldap-clients .title}

In Identity Management (IdM), you can enforce one-time password (OTP) usage for all LDAP clients to prevent single-factor authentication for users that have OTP tokens configured.

**Procedure**

-   To enforce OTP usage for all LDAP clients, use the following command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa config-mod --addattr ipaconfigstring=EnforceLDAPOTP
    ```

-   To change back to the previous OTP behavior for all LDAP clients, use the following command:

    ``` {.language-plaintext tabindex="-1"}
    $ ipa config-mod --delattr ipaconfigstring=EnforceLDAPOTP
    ```

## [Chapter 8. Securing LDAP access](#securing-ldap-access) {#chapter-8.-securing-ldap-access .title}

Control how clients connect to the Identity Management (IdM) directory and manage anonymous access permissions.

### [8.1. Identity Management default access policy](#identity-management-default-access-policy) {#identity-management-default-access-policy .title}

Identity Management (IdM) applies default security settings by adhering to the RHEL system-wide cryptographic policy. You can use this policy to ensure that all IdM components meet current security standards automatically, which eliminates the need for manual hardening.

Important

Red Hat recommends that you use the system-wide crypto policy. Changing individual security settings can break components of IdM.

For more information see the `crypto-policies(7)`{.literal} man page on your system.

### [8.2. Anonymous LDAP binds in Identity Management](#anonymous-ldap-binds-in-identity-management) {#anonymous-ldap-binds-in-identity-management .title}

Anonymous binds are unauthenticated LDAP connections that legacy utilities, such as `realmd`{.literal}, require for domain discovery when enrolling a client. However, anonymous binds can expose Identity Management (IdM) configuration settings or directory values.

You can control the visibility of your directory by modifying the `nsslapd-allow-anonymous-access`{.literal} attribute on the IdM 389 Directory Server instance.

These are the valid values for the `nsslapd-allow-anonymous-access`{.literal} attribute:

-   `on`{.literal}: allows all anonymous binds (default)
-   `rootdse`{.literal}: allows anonymous binds only for root DSE information
-   `off`{.literal}: disallows any anonymous binds

By changing the value of the `nsslapd-allow-anonymous-access`{.literal} attribute to `rootdse`{.literal}, you allow access to the root DSE and server configuration without any access to the directory data.

Red Hat does not recommend completely disallowing anonymous binds by setting the attribute to `off`{.literal}, because this also blocks external clients from checking the server configuration. LDAP and web clients are not necessarily domain clients, so they connect anonymously to read the root DSE file to get connection information.

### [8.3. Disabling anonymous binds](#disabling-anonymous-binds) {#disabling-anonymous-binds .title}

You can restrict anonymous access to ensure only server configuration is discoverable while protecting sensitive directory data.

Warning

Certain clients rely on anonymous binds to discover IdM settings. Additionally, the compat tree can break for legacy clients that are not using authentication. Perform this procedure only if your clients do not require anonymous binds.

**Prerequisites**

-   You can authenticate as the Directory Manager to write to the LDAP server.
-   You can authenticate as the `root`{.literal} user to restart IdM services.

**Procedure**

1.  Change the `nsslapd-allow-anonymous-access`{.literal} attribute to `rootdse`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    $ ldapmodify -x -D "cn=Directory Manager" -W -h server.example.com -p 389
    ```

    ``` {.language-plaintext tabindex="-1"}
    Enter LDAP Password:
    dn: cn=config
    changetype: modify
    replace: nsslapd-allow-anonymous-access
    nsslapd-allow-anonymous-access: rootdse

    modifying entry "cn=config"
    ```

2.  Restart the 389 Directory Server instance to load the new setting.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart dirsrv.target
    ```

**Verification**

-   Display the value of the `nsslapd-allow-anonymous-access`{.literal} attribute.

    ``` {.language-plaintext tabindex="-1"}
    $ ldapsearch -x -D "cn=Directory Manager" -b cn=config -W -h server.example.com -p 389 nsslapd-allow-anonymous-access | grep nsslapd-allow-anonymous-access
    ```

    ``` {.language-plaintext tabindex="-1"}
    Enter LDAP Password:
    # requesting: nsslapd-allow-anonymous-access
    nsslapd-allow-anonymous-access: rootdse
    ```

**Additional resources**

-   [Red Hat Directory Server documentation: nsslapd-allow-anonymous-access](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuration_and_schema_reference/core-server-configuration-attributes#nsslapd-allow-anonymous-access)

## [Chapter 9. Security hardening of IdM in RHEL](#security-hardening-of-idm-in-rhel) {#chapter-9.-security-hardening-of-idm-in-rhel .title}

Apply recommended security controls to reduce the attack surface of your Identity Management (IdM) deployment and maintain a defensible security posture.

### [9.1. Identity protection in IdM](#identity-protection-in-idm) {#identity-protection-in-idm .title}

Protect Identity Management (IdM) identities against credential theft.

Require MFA for all users, administrative and non-administrative ones
:   Eliminate the risk of credential theft for privileged accounts. This ensures that even if a password is leaked, an attacker cannot authenticate without the second physical or temporal factor. Administrative accounts are the highest-value targets in any IdM deployment and must be protected first. After that, consider extending this protection to the entire user base.

Rotate the Directory Manager password and restrict its use

:   The Directory Manager DN (`cn=Directory Manager`{.literal}) authenticates directly against the underlying 389 Directory Server via a simple LDAP bind, bypassing Kerberos, MFA policies, HBAC rules, and all access controls. It is not an IdM user account and cannot benefit from any MFA policy configured in IdM.

    Note

    Treat it as a break-glass credential, that is, an emergency-access account used only when normal access paths are unavailable: store it in a secrets vault or sealed procedure, prohibit routine use, log every use, and rotate on a defined schedule. Day-to-day administration should always use a named admin account.

Limit `admin`{.literal} group membership
:   Reduces the blast radius. Fewer users with full privileges means a smaller statistical chance of a high-value account being compromised. Review membership periodically and remove accounts that no longer require it.

To implement these recommendations, see the following table:

+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Recommendation                                                        | Documentation                                                                                                                                                                                                                                                                       |
+:======================================================================+:====================================================================================================================================================================================================================================================================================+
| Require MFA for all users, administrative and non-administrative ones | [Enabling the one-time password in the Web UI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-the-identity-management-web-ui-using-one-time-passwords#enabling-the-one-time-password-in-the-web-ui) |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Rotate the Directory Manager password and restrict its use            | [Resetting the Directory Manager user password](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/managing-user-passwords-in-idm#resetting-the-directory-manager-user-password)                    |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Limit `admin`{.literal} group membership                              | [Managing user groups in IdM CLI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/managing-user-groups-in-idm-cli)                                                                               |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 9.1. Identity protection recommendations and links

Show more

### [9.2. Access control hardening in IdM](#access-control-hardening-in-idm) {#access-control-hardening-in-idm .title}

Restrict access in your Identity Management (IdM) deployment to enforce a Zero Trust model.

Disable the `allow_all`{.literal} HBAC rule
:   Shifts the environment to a Zero Trust model. The default `allow_all`{.literal} rule grants every enrolled user login access to every enrolled host, which is a direct violation of least privilege. Disable it immediately and replace it with specific, scoped host-based access control (HBAC) rules that permit only the access each role genuinely requires.

Verify that TLS is used when IdM clients communicate with IdM servers through LDAP

:   Plain LDAP on port 389 transmits credentials and directory data in plain text, making it easy to intercept on the network. Check that trying to initiate STARTTLS results in an error because an SSL/TLS connection is already established:

    ``` {.language-plaintext tabindex="-1"}
    $ ldapsearch -x -ZZ '(uid=admin)'
    ```

    ``` {.language-plaintext tabindex="-1"}
    ldap_start_tls: Operations error (1)
            additional info: SSL connection already established
    ```

Keep SELinux enforcing on all IdM servers and map users to SELinux contexts
:   SELinux must remain in enforcing mode on all IdM servers. Disabling it removes mandatory access controls for the server itself and all enrolled hosts. Beyond keeping SELinux enforcing, map IdM users to confined SELinux users (for example, `staff_u`{.literal}, `user_u`{.literal}) to ensure the Linux kernel restricts what files or processes a user can interact with, even if their account is compromised. Ensure all enrolled users are explicitly mapped and restrict `unconfined_u`{.literal} to accounts that genuinely require it.

Define custom RBAC roles
:   Enforces least privilege. The built-in IdM roles (`User Administrator`{.literal}, `Group Administrator`{.literal}, and so on) are intentionally broad. They are designed to be usable by all RHEL IdM customers and do not match the specific permission boundaries of your deployment. Use them as a reference, then create custom roles that grant only the privileges each administrative function requires.

Disable anonymous LDAP binds

:   Set the `nsslapd-allow-anonymous-access`{.literal} attribute to `rootdse`{.literal} to prevent user enumeration and thereby reduce the risk of brute-force or phishing attacks.

    Do not set the attribute to `off`{.literal}, because this blocks external clients from checking the server configuration. LDAP and web clients are not necessarily domain clients, so they connect anonymously to read the `root`{.literal} Directory Server Entry (DSE) file to get connection information.

Restrict `admin`{.literal} login locations
:   Prevents remote exploitation. Requiring administrators to authenticate from a designated jump host or secure console stops attackers from using stolen credentials over the general network, even if MFA is bypassed through a client-side compromise. In addition, you can use Kerberos authentication indicators to secure access to the jump hosts.

Disable the Schema Compatibility (`compat`{.literal}) plugin when not needed

:   The `compat`{.literal} plugin creates a virtual NIS/RFC 2307-compatible subtree at `cn=compat,dc=…​`{.literal} that is enabled by default. It was designed for backward compatibility with legacy clients that cannot support the native FreeIPA LDAP schema. The security risk is that this subtree exposes user and group information in a broadly readable form and can remain accessible even after anonymous binds are disabled on the root directory tree. If all enrolled clients use SSSD with the `ipa`{.literal} provider, the `compat`{.literal} tree serves no purpose. Disable it with `ipa-compat-manage disable`{.literal} and restart the directory service.

    Note

    If legacy NIS clients still depend on it, isolate those clients at the network level so the compat tree is not reachable from general network segments.

Review `sudo`{.literal} rules regularly
:   `sudo`{.literal} rules are a common and often overlooked privilege escalation vector. An overly broad `sudo`{.literal} rule can grant a regular user effective `root`{.literal} access on enrolled hosts without that access appearing in HBAC or RBAC reviews. Run `ipa sudorule-find --all`{.literal} periodically and audit each rule: confirm the scope of hosts and commands is intentional, remove rules that are no longer needed, and ensure no rules grant unrestricted (ALL) command access without a documented justification.

To implement these recommendations, see the following table:

+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Recommendation                                                              | Documentation                                                                                                                                                                                                                                                                                 |
+:============================================================================+:==============================================================================================================================================================================================================================================================================================+
| Disable the `allow_all`{.literal} HBAC rule                                 | [Configuring HBAC rules in an IdM domain using the CLI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/configuring-host-based-access-control-rules#configuring-hbac-rules-in-an-idm-domain-using-the-cli) |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keep SELinux enforcing on all IdM servers and map users to SELinux contexts | [Mapping SELinux users and IdM users in the IdM CLI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/defining-selinux-user-maps#mapping-selinux-users-and-idm-users-in-the-idm-cli)                        |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Define custom RBAC roles                                                    | [Managing IdM roles in the CLI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/managing-role-based-access-controls-in-idm-using-the-cli#managing-idm-roles-in-the-cli)                                    |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Disable anonymous LDAP binds                                                | [Anonymous LDAP binds in Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/securing-ldap-access#anonymous-ldap-binds-in-identity-management)                                                              |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Restrict `admin`{.literal} login locations                                  | [Configuring host-based access control rules](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/configuring-host-based-access-control-rules)                                                                 |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Review `sudo`{.literal} rules regularly                                     | [Granting `sudo`{.literal} access to an IdM user on an IdM client](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/granting-sudo-access-to-an-idm-user-on-an-idm-client)                                   |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 9.2. Access control hardening recommendations and links

Show more

### [9.3. System integrity in IdM](#system-integrity-in-idm) {#system-integrity-in-idm .title}

Ensure the servers, backups, and cryptographic settings underlying your Identity Management (IdM) deployment remain secure and reliable.

Dedicated IdM servers (no co-located services)
:   Reduces the attack surface. IdM servers hold the Kerberos KDC, LDAP directory, and CA, which are the most sensitive components in your identity infrastructure. Co-locating web servers, databases, or other workloads introduces unrelated vulnerabilities that could be used to pivot directly into the identity store.

Enable FIPS mode during RHEL installation (regulated environments)

:   If operating in a regulated environment (for example, FedRAMP, NIST 800-53, PCI-DSS, or government and defense contexts), enable FIPS 140-2/140-3 mode on the underlying operating system before deploying IdM. FIPS mode restricts the system to approved cryptographic algorithms system-wide, covering Kerberos, TLS, and all OpenSSL consumers.

    Note

    FIPS mode must be enabled before IdM installation. Enabling it post-deployment requires reinstallation. Therefore, verify that all clients and integrated services support FIPS-compliant cipher suites before enabling FIPS mode.

Back up IdM data securely (`ipa-backup`{.literal})
:   A backup of an IdM server is as sensitive as the live server because it contains every password hash, Kerberos key, and certificate private key in your environment. Use the native `ipa-backup`{.literal} utility to produce consistent, application-aware backups. Store them encrypted and in an off-site or air-gapped location, with access strictly limited to personnel who would legitimately perform a restore.

Use OpenSCAP regularly

:   Ensures continuous compliance. Automatically detects if security settings have drifted from the intended baseline due to error or unauthorized changes. Integrate into a scheduled job and treat failures as incidents.

    Note

    This audits the operating system configuration only and does not evaluate internal IdM data, such as user accounts or HBAC rules.

Use `ipa-healthcheck`{.literal}
:   Provides operational security monitoring. Detects technical failures, such as replication lag, expiring certificates, and misconfigured services, that could result in a denial of service or undetected configuration drift. Run regularly and forward output to a monitoring system.

Audit and clean up replication topology
:   Stale replication agreements left over from decommissioned replicas are a persistent risk. Each replica holds a full copy of every password hash, Kerberos key, and group membership. When decommissioning a replica, always use `ipa server-del`{.literal}, not just a power-off, so that agreements and service principals are cleanly removed. Periodically run `ipa topologysegment-find`{.literal} and compare output against your known infrastructure inventory.

Certificate and CA lifecycle management

:   The `ipa-healthcheck`{.literal} tool flags certificate expiry, but additional controls are needed:

    -   Audit which services have certificates issued by the IdM CA and verify that no unexpected certificates exist.
    -   Restrict sub-CA issuance if lightweight sub-CAs are in use.
    -   Review CRL and OCSP configuration to ensure revocation is functional.

To implement these recommendations, see the following table:

+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Recommendation                                                     | Documentation                                                                                                                                                                                                                                                            |
+:===================================================================+:=========================================================================================================================================================================================================================================================================+
| Enable FIPS mode during RHEL installation (regulated environments) | [Installing the system with FIPS mode enabled](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/switching-rhel-to-fips-mode#installing-the-system-with-fips-mode-enabled)                                                    |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Back up IdM data securely (`ipa-backup`{.literal})                 | [Preparing for data loss with IdM backups](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/preparing-for-data-loss-with-idm-backups)                                                                              |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Use OpenSCAP regularly                                             | [Assessing configuration compliance with a specific baseline](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/scanning-the-system-for-configuration-compliance#assessing-configuration-compliance-with-a-specific-baseline) |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Use `ipa-healthcheck`{.literal}                                    | [Installing and running the IdM healthcheck tool](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_idm_healthcheck_to_monitor_your_idm_environment/installing-and-running-the-idm-healthcheck-tool)                                       |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Audit and clean up replication topology                            | [Managing replication topology](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_replication_in_identity_management/managing-replication-topology)                                                                                     |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Certificate and CA lifecycle management                            | [Managing certificates in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_certificates_in_idm/index)                                                                                                                             |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 9.3. System integrity recommendations and links

Show more

### [9.4. Security monitoring and detection in IdM](#security-monitoring-and-detection-in-idm) {#security-monitoring-and-detection-in-idm .title}

Detect and respond to security incidents in your Identity Management (IdM) deployment.

Enable audit logging and forward logs off-host

:   Hardening controls reduce the likelihood of a breach, but do not eliminate it. Audit logs provide the evidence needed to detect a control bypass after the fact. Enable IdM's LDAP audit log, collect Kerberos authentication events, and forward all logs to a centralized security information and event management (SIEM) before they can be tampered with on the IdM host itself.

    Note

    Key signals to monitor: repeated failed LDAP binds, unexpected changes to `admin`{.literal} group membership, Kerberos ticket requests for sensitive service principals, and Directory Manager bind events.

Audit and detect security configuration drift
:   Security posture degrades over time through configuration drift, staff changes, and new enrollments. Schedule a periodic review, at least quarterly, that re-checks `admin`{.literal} group membership, active HBAC rules, custom RBAC role assignments, replication topology, and certificate inventory. Treat deviations from the baseline as incidents.

To implement these recommendations, see the following table:

+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Recommendation                                 | Documentation                                                                                                                                                                                     |
+:===============================================+:==================================================================================================================================================================================================+
| Enable audit logging and forward logs off-host | [IdM log files and directories](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/idm-log-files-and-directories) |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 9.4. Security monitoring and detection recommendations and links

Show more

### [9.5. IdM security hardening implementation phases](#idm-security-hardening-implementation-phases) {#idm-security-hardening-implementation-phases .title}

Use this table to prioritize security controls by deployment phase, from day-one essentials to ongoing maintenance.

+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Phase           | Actions                                                                                                                                                                       |
+:================+:==============================================================================================================================================================================+
| Day 1           | -   [Disable the `allow_all`{.literal} HBAC rule](#disable-the-allow_all-hbac-rule)                                                                                           |
|                 | -   [Require MFA for all users, administrative and non-administrative](#require-mfa-for-all-users-administrative-and-non-administrative-ones)                                 |
|                 | -   [Rotate the Directory Manager password and restrict its use](#rotate-the-directory-manager-password-and-restrict-its-use)                                                 |
|                 | -   [Dedicated IdM servers (no co-located services)](#dedicated-idm-servers-no-co-located-services)                                                                           |
|                 | -   [Verify that TLS is used when IdM clients communicate with IdM servers through LDAP](#verify-that-tls-is-used-when-idm-clients-communicate-with-idm-servers-through-ldap) |
|                 | -   [Keep SELinux enforcing on all IdM servers](#keep-selinux-enforcing-on-all-idm-servers-and-map-users-to-selinux-contexts)                                                 |
|                 | -   [Enable FIPS mode (regulated environments)](#enable-fips-mode-regulated-environments)                                                                                     |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Day 30          | -   [Define custom RBAC roles](#define-custom-rbac-roles)                                                                                                                     |
|                 | -   [Disable anonymous LDAP binds](#disable-anonymous-ldap-binds)                                                                                                             |
|                 | -   [Restrict `admin`{.literal} login locations](#restrict-admin-login-locations)                                                                                             |
|                 | -   [Map users to SELinux contexts](#keep-selinux-enforcing-on-all-idm-servers-and-map-users-to-selinux-contexts)                                                             |
|                 | -   [Back up IdM data securely (`ipa-backup`{.literal})](#back-up-idm-data-securely-ipa-backup)                                                                               |
|                 | -   [Disable the Schema Compatibility (`compat`{.literal}) plugin when not needed](#disable-the-schema-compatibility-compat-plugin-when-not-needed)                           |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ongoing         | -   [Use OpenSCAP regularly](#use-openscap-regularly)                                                                                                                         |
|                 | -   [Use `ipa-healthcheck`{.literal}](#use-ipa-healthcheck)                                                                                                                   |
|                 | -   [Enable audit logging and forward logs off-host](#enable-audit-logging-and-forward-logs-off-host)                                                                         |
|                 | -   [Limit `admin`{.literal} group membership](#limit-admin-group-membership)                                                                                                 |
|                 | -   [Review `sudo`{.literal} rules regularly](#review-sudo-rules-regularly)                                                                                                   |
|                 | -   [Audit and clean up replication topology](#audit-and-clean-up-replication-topology)                                                                                       |
|                 | -   [Certificate and CA lifecycle management](#certificate-and-ca-lifecycle-management)                                                                                       |
|                 | -   [Continue backing up IdM data securely (`ipa-backup`{.literal})](#back-up-idm-data-securely-ipa-backup)                                                                   |
|                 | -   [Audit and detect security configuration drift](#audit-and-detect-security-configuration-drift)                                                                           |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 9.5. IdM security hardening implementation phases and actions

Show more

## [Chapter 10. IdM log files and directories](#idm-log-files-and-directories) {#chapter-10.-idm-log-files-and-directories .title}

Identity Management (IdM) services generate log files that record system activity, service status, and authentication events. These logs are essential for monitoring the health of your IdM environment and performing root-cause analysis when troubleshooting service failures or security incidents.

### [10.1. IdM server and client log files and directories](#idm-server-and-client-log-files-and-directories) {#idm-server-and-client-log-files-and-directories .title}

Identity Management (IdM) generates logs across server, replica, and client systems to record deployment events and service operations. You can locate specific log files and directories for troubleshooting installation errors.

+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Directory or File                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+:===================================================+:========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `/var/log/ipaserver-install.log`{.literal}         | The installation log for the IdM server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/var/log/ipareplica-install.log`{.literal}        | The installation log for the IdM replica.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/var/log/ipaclient-install.log`{.literal}         | The installation log for the IdM client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/var/log/sssd/`{.literal}                         | Log files for SSSD. You can [enable detailed logging for SSSD in the sssd.conf file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_authentication_and_authorization_in_rhel/troubleshooting-authentication-with-sssd-in-idm#enabling-detailed-logging-for-sssd-in-the-sssd-conf-file) or [with the sssctl command](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_authentication_and_authorization_in_rhel/troubleshooting-authentication-with-sssd-in-idm#enabling-detailed-logging-for-sssd-with-the-sssctl-command).                  |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `~/.ipa/log/cli.log`{.literal}                     | The log file for errors returned by remote procedure calls (RPCs) and responses by the `ipa`{.literal} utility. Created in the home directory for the **effective user** that runs the tools. This user might have a different user name than the IdM user principal, that is the IdM user whose ticket granting ticket (TGT) has been obtained before attempting to perform the failed `ipa`{.literal} commands. For example, if you are logged in to the system as `root`{.literal} and have obtained the TGT of IdM `admin`{.literal}, then the errors are logged in to the `/root/.ipa/log/cli.log`{.literal} file. |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/etc/logrotate.d/`{.literal}                      | The log rotation policies for DNS, SSSD, Apache, Tomcat, and Kerberos.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/etc/pki/pki-tomcat/logging.properties`{.literal} | This link points to the default Certificate Authority logging configuration at `/usr/share/pki/server/conf/logging.properties`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 10.1. Identity Management log files

Show more

**Additional resources**

-   [Troubleshooting IdM server installation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/troubleshooting-idm-server-installation)
-   [Troubleshooting IdM client installation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/troubleshooting-idm-client-installation)
-   [Troubleshooting IdM replica installation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/troubleshooting-idm-replica-installation)
-   [Troubleshooting authentication with SSSD in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_authentication_and_authorization_in_rhel/troubleshooting-authentication-with-sssd-in-idm)

### [10.2. Directory Server log files](#directory-server-log-files) {#directory-server-log-files .title}

The Directory Server (DS) instance serves as the central LDAP data store for Identity Management (IdM). Use the following log files to monitor data-level operations, track replication traffic between servers, and diagnose failures specific to the underlying LDAP service.

+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Directory or file                                                             | Description                                                                                                                                                                                                                                                            |
+:==============================================================================+:=======================================================================================================================================================================================================================================================================+
| `/var/log/dirsrv/slapd-`{.literal}*`REALM_NAME`{.literal}*`/`{.literal}       | Log files associated with the DS instance used by the IdM server. Most operational data recorded here are related to server-replica interactions.                                                                                                                      |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/var/log/dirsrv/slapd-`{.literal}*`REALM_NAME`{.literal}*`/audit`{.literal}  | Contains audit trails of all DS operations when auditing is enabled in the DS configuration.                                                                                                                                                                           |
|                                                                               |                                                                                                                                                                                                                                                                        |
|                                                                               | Note                                                                                                                                                                                                                                                                   |
|                                                                               |                                                                                                                                                                                                                                                                        |
|                                                                               | You can also audit the Apache error logs, where the IdM API logs access. However, because changes can be made directly over LDAP too, Red Hat recommends enabling the more comprehensive `/var/log/dirsrv/slapd-REALM_NAME/audit`{.literal} log for auditing purposes. |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/var/log/dirsrv/slapd-`{.literal}*`REALM_NAME`{.literal}*`/access`{.literal} | Contains detailed information about attempted access for the domain DS instance.                                                                                                                                                                                       |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/var/log/dirsrv/slapd-`{.literal}*`REALM_NAME`{.literal}*`/errors`{.literal} | Contains detailed information about failed operations for the domain DS instance.                                                                                                                                                                                      |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 10.2. Directory Server log files

Show more

**Additional resources**

-   [Monitoring Server and Database Activity](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/management_configuration_and_operations/monitoring-server-and-database-activity)
-   [Log File Reference](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuration_and_schema_reference/log-files-reference)

### [10.3. Enabling audit logging on an IdM server](#enabling-audit-logging-on-an-idm-server) {#enabling-audit-logging-on-an-idm-server .title}

Enable audit logging to track administrative changes and data modifications within the Identity Management (IdM) LDAP directory. You can use the detailed audit logs to monitor data, troubleshoot issues, and examine suspicious activity on the network.

Note

The LDAP service might become slower if there are many LDAP changes logged, especially if the values are large.

**Prerequisites**

-   The Directory Manager password

**Procedure**

1.  Bind to the LDAP server:

    ``` {.language-plaintext tabindex="-1"}
    $ ldapmodify -D "cn=Directory Manager" -W << EOF
    ```

2.  Specify all the modifications you want to make, for example:

    ``` {.language-plaintext tabindex="-1"}
    dn: cn=config
    changetype: modify
    replace: nsslapd-auditlog-logging-enabled
    nsslapd-auditlog-logging-enabled: on
    -
    replace:nsslapd-auditlog
    nsslapd-auditlog: /var/log/dirsrv/slapd-REALM_NAME/audit
    -
    replace:nsslapd-auditlog-mode
    nsslapd-auditlog-mode: 600
    -
    replace:nsslapd-auditlog-maxlogsize
    nsslapd-auditlog-maxlogsize: 100
    -
    replace:nsslapd-auditlog-logrotationtime
    nsslapd-auditlog-logrotationtime: 1
    -
    replace:nsslapd-auditlog-logrotationtimeunit
    nsslapd-auditlog-logrotationtimeunit: day
    ```

3.  Indicate the end of the `ldapmodify`{.literal} command by entering **EOF** on a new line.

4.  Press **Enter** twice.

5.  Repeat the previous steps on all the other IdM servers on which you want to enable audit logging.

**Verification**

-   Open the `/var/log/dirsrv/slapd-REALM_NAME/audit`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    389-Directory/1.4.3.231 B2021.322.1803
    server.idm.example.com:636 (/etc/dirsrv/slapd-IDM-EXAMPLE-COM)

    time: 20220607102705
    dn: cn=config
    result: 0
    changetype: modify
    replace: nsslapd-auditlog-logging-enabled
    nsslapd-auditlog-logging-enabled: on
    [...]
    ```

    The fact that the file is not empty anymore confirms that auditing is enabled.

    The system logs the bound LDAP distinguished name (DN) of the entry that makes a change. For this reason, you might have to post-process the log. For example, in the IdM Directory Server, it is an ID override DN that represents the identity of an AD user that modified a record:

    ``` {.language-plaintext tabindex="-1"}
    $ modifiersName: ipaanchoruuid=:sid:s-1-5-21-19610888-1443184010-1631745340-279100,cn=default trust view,cn=views,cn=accounts,dc=idma,dc=idm,dc=example,dc=com
    ```

    Use the `pysss_nss_idmap.getnamebysid`{.literal} Python command to look up an AD user if you have the user SID:

    ``` {.language-plaintext tabindex="-1"}
    >>> import pysss_nss_idmap
    >>> pysss_nss_idmap.getnamebysid('S-1-5-21-1273159419-3736181166-4190138427-500'))
    {'S-1-5-21-1273159419-3736181166-4190138427-500': {'name': 'administrator@ad.vm', 'type': 3}}
    ```

**Additional resources**

-   [Directory Server: Core server configuration attributes](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuration_and_schema_reference/core-server-configuration-attributes)
-   [How to enable Audit logging in IPA/IDM Server and Replica Servers (Red Hat Knowledgebase)](https://access.redhat.com/solutions/772563)
-   [Red Hat Directory Server log files](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuration_and_schema_reference/log-files-reference)

### [10.4. Modifying error logging on an IdM server](#modifying-error-logging-on-an-idm-server) {#modifying-error-logging-on-an-idm-server .title}

Increase the error log level to obtain detailed debugging information for specific Directory Server sub-systems, such as replication. By adjusting the log level from its default state, you can capture more granular data to identify the root cause of service failures.

To record a different type of information, select a different number from the table in [Error Log Logging Levels](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuration_and_schema_reference/log-files-reference#error-logging-levels) in the Red Hat Directory Server documentation.

Note

The LDAP service might become slower if there are many types of LDAP errors logged, especially if the values are large.

**Prerequisites**

-   The Directory Manager password.

**Procedure**

1.  Bind to the LDAP server:

    ``` {.language-plaintext tabindex="-1"}
    $ ldapmodify -x -D "cn=directory manager" -w <password>
    ```

2.  Specify the modifications you want to make. For example to collect only logs related to replication:

    ``` {.language-plaintext tabindex="-1"}
    dn: cn=config
    changetype: modify
    add: nsslapd-errorlog-level
    nsslapd-errorlog-level: 8192
    ```

3.  Press \[Enter\] twice, to indicate the end of the `ldapmodify`{.literal} instruction. This displays the `modifying entry "cn=config"`{.literal} message.

4.  Press \[Ctrl+C\] to exit the `ldapmodify`{.literal} command.

5.  Repeat the previous steps on all the other IdM servers on which you want to collect detailed logs about replication errors.

    Important

    After you finish troubleshooting, set `nsslapd-errorlog-level`{.literal} back to 0 to prevent performance problems.

### [10.5. The IdM Apache server log files](#the-idm-apache-server-log-files) {#the-idm-apache-server-log-files .title}

Identity Management (IdM) uses the Apache HTTP Server to host the Web UI and manage communication for the remote procedure call (RPC) interface. Use the following logs to monitor web-based traffic, audit administrative access to the management console, and troubleshoot issues.

+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Directory or File                     | Description                                                                                                                                                                                                                                                                                                                                     |
+:======================================+:================================================================================================================================================================================================================================================================================================================================================+
| `/var/log/httpd/`{.literal}           | Log files for the Apache web server.                                                                                                                                                                                                                                                                                                            |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/var/log/httpd/access_log`{.literal} |  Standard access and error logs for Apache servers. Messages specific to IdM are recorded along with the Apache messages because the IdM web UI and the RPC command-line interface use Apache. The access logs log mostly only the user principal and the URI used, which is often an RPC endpoint. The error logs contain the IdM server logs. |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/var/log/httpd/error_log`{.literal}  |                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 10.3. Apache Server log files

Show more

**Additional resources**

-   [Log Files](http://httpd.apache.org/docs/current/logs.html)

### [10.6. Certificate System log files in IdM](#certificate-system-log-files-in-idm) {#certificate-system-log-files-in-idm .title}

Use Identity Management (IdM) Certificate System log files to audit certificate issuance, track Key Recovery Authority (KRA) operations, and troubleshoot the internal Certificate Authority (CA).

+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Directory or File                                                                         | Description                                                                                                                                                  |
+:==========================================================================================+:=============================================================================================================================================================+
| `/var/log/pki/pki-ca-spawn.`{.literal}*`time_of_installation`{.literal}*`.log`{.literal}  | The installation log for the IdM certificate authority (CA).                                                                                                 |
+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/var/log/pki/pki-kra-spawn.`{.literal}*`time_of_installation`{.literal}*`.log`{.literal} | The installation log for the IdM Key Recovery Authority (KRA).                                                                                               |
+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/var/log/pki/pki-tomcat/`{.literal}                                                      | The top level directory for PKI operation logs. Contains CA and KRA logs.                                                                                    |
+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/var/log/pki/pki-tomcat/ca/`{.literal}                                                   | Directory with logs related to certificate operations. In IdM, these logs are used for service principals, hosts, and other entities which use certificates. |
+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/var/log/pki/pki-tomcat/kra`{.literal}                                                   | Directory with logs related to KRA.                                                                                                                          |
+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/var/log/messages`{.literal}                                                             | Includes certificate error messages among other system messages.                                                                                             |
+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 10.4. Certificate System log files

Show more

**Additional resources**

-   [Configuring subsystem logs](https://docs.redhat.com/en/documentation/red_hat_certificate_system/9/html/administration_guide/logs)

### [10.7. Kerberos log files in IdM](#kerberos-log-files-in-idm) {#kerberos-log-files-in-idm .title}

Kerberos serves as the primary authentication protocol for Identity Management (IdM). Monitor the Key Distribution Center (KDC) and administration server log files to diagnose ticket-granting failures and credential issues.

+--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Directory or File                                                                                                  | Description                                                  |
+:===================================================================================================================+:=============================================================+
| `/var/log/krb5kdc.log`{.literal}                                                                                   | The primary log file for the Kerberos KDC server.            |
+--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| `/var/log/kadmind.log`{.literal}                                                                                   | The primary log file for the Kerberos administration server. |
+--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Locations for these files are configured in the `krb5.conf`{.literal} file. They can be different on some systems. |                                                              |
+--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

: Table 10.5. Kerberos Log Files

Show more

### [10.8. DNS log files in IdM](#dns-log-files-in-idm) {#dns-log-files-in-idm .title}

Identity Management (IdM) uses integrated DNS to facilitate service discovery and domain routing. Use the following system log to monitor DNS query activity and resolve name resolution issues.

+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Directory or File             | Description                                                                                                                                                                                                                  |
+:==============================+:=============================================================================================================================================================================================================================+
| `/var/log/messages`{.literal} | Includes DNS error messages and other system messages. DNS logging in this file is not enabled by default. To enable it, enter the `# /usr/sbin/rndc querylog`{.literal} command. To disable logging, run the command again. |
+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 10.6. DNS log files

Show more

### [10.9. Custodia log files in IdM](#custodia-log-files-in-idm) {#custodia-log-files-in-idm .title}

The following table presents directories and files that Custodia uses to log information in Identity Management (IdM).

+-----------------------------------+----------------------------------------------+
| Directory or File                 | Description                                  |
+:==================================+:=============================================+
| `/var/log/custodia/`{.literal}    | Log file directory for the Custodia service. |
+-----------------------------------+----------------------------------------------+

: Table 10.7. Custodia Log Files

Show more

### [10.10. Additional resources](#idm-log-files-and-directories_1010-additional-resources) {#additional-resources .title}

-   [Troubleshooting problems by using log files](https://docs.redhat.com/pt-br/documentation/red_hat_enterprise_linux/10/html/risk_reduction_and_recovery_operations/troubleshooting-problems-by-using-log-files)

## [Legal Notice](#idm140344570969792) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
