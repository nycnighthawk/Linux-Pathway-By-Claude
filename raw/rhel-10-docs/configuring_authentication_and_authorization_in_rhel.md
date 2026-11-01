---
{"title": "Configuring authentication and authorization in RHEL", "guide": "configuring_authentication_and_authorization_in_rhel", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_authentication_and_authorization_in_rhel/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Configuring authentication and authorization in RHEL {#configuring-authentication-and-authorization-in-rhel .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Using SSSD, authselect, and sssctl to configure authentication and authorization {#using-sssd-authselect-and-sssctl-to-configure-authentication-and-authorization .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140250342294304)

**Abstract**

You can configure Red Hat Enterprise Linux (RHEL) to authenticate and authorize users to Identity Management (IdM), Active Directory (AD), and LDAP directories RHEL uses the System Security Services Daemon (SSSD) to communicate with these services. The \`authselect\` and \`sssctl\` utilities assist you in configuring SSSD, Pluggable Authentication Modules (PAM) and the Name Service Switch (NSS).

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

## [Chapter 1. Introduction to system authentication](#introduction-to-system-authentication) {#chapter-1.-introduction-to-system-authentication .title}

Secure networks require verifying user identities before granting access. Red Hat Enterprise Linux provides tools to manage these identities, ranging from local system files to external domains like Kerberos and Samba.

### [1.1. Authentication methods in RHEL](#authentication-methods-in-rhel) {#authentication-methods-in-rhel .title}

Authentication verifies identity using credentials, while authorization determines access rights. RHEL supports multiple verification mechanisms, including passwords, certificates, and tokens, to ensure secure network interactions.

Authentication requires that an entity presents some kind of credential to verify its identity. The kind of credential that is required is defined by the authentication mechanism being used.

#### [1.1.1. Types of authentication for local users on a system](#types_of_authentication_for_local_users_on_a_system) {#types-of-authentication-for-local-users-on-a-system .title}

Password-based authentication
:   Almost all software permits the user to authenticate by providing a recognized username and password. This is also called simple authentication.

Certificate-based authentication
:   Client authentication based on certificates is part of the Secure Sockets Layer (SSL) protocol. The client digitally signs a randomly generated piece of data and sends both the certificate and the signed data across the network. The server validates the signature and confirms the validity of the certificate.

Kerberos authentication
:   Kerberos establishes a system of short-lived credentials, called ticket-granting tickets (TGTs). The user presents credentials, that is, user name and password, that identify the user and indicate to the system that the user can be issued a ticket. TGT can then be repeatedly used to request access tickets to other services, like websites and email. Authentication using Kerberos allows the user to undergo only a single authentication process in this way.

Smart card-based authentication

:   This is a variant of certificate-based authentication. The smart card (or token) stores user certificates; when a user inserts the token into a system, the system reads the certificates and grants access. Single sign-on using smart cards goes through three steps:

    1.  A user inserts a smart card into the card reader. Pluggable authentication modules (PAMs) on Red Hat Enterprise Linux detect the inserted smart card.
    2.  The system maps the certificate to the user entry and then compares the presented certificates on the smart card, which are encrypted with a private key as explained under the certificate-based authentication, to the certificates stored in the user entry.
    3.  If the certificate is successfully validated against the key distribution center (KDC), then the user is allowed to log in.

    Smart card-based authentication builds on the simple authentication layer established by Kerberos by adding certificates as additional identification mechanisms as well as by adding physical access requirements.

One-time password authentication
:   One-time passwords bring an additional step to your authentication security. The authentication uses your password in combination with an automatically generated one time password.

Passkey authentication
:   A passkey is a FIDO2 authentication device that is supported by the libfido2 library, such as Yubikey 5 and Nitrokey. It allows passwordless and multi-factor authentication. If your system is enrolled and connected to an IdM environment, this authentication method issues a Kerberos ticket automatically, which enables single sign-on (SSO) for an Identity Management (IdM) user.

External identity providers
:   You can associate users with external identity providers (IdP) that support the OAuth 2 device authorization flow. When these users authenticate with the SSSD version available in RHEL 9.1 or later, they receive RHEL Identity Management (IdM) single sign-on capabilities with Kerberos tickets after performing authentication and authorization at the external IdP.

Generic identity providers
:   The System Security Services Daemon (SSSD) supports a direct integration with modern identity providers (IdP) that use the OAuth 2.0 and OpenID Connect (OIDC) protocols. This currently allows you to authenticate users against Red Hat build of Keycloak or Microsoft Entra ID without requiring a traditional LDAP or Active Directory infrastructure. SSSD uses the OAuth 2.0 Device Authorization Grant flow to handle authentication with a generic IdP where a web browser cannot be directory rendered, such as RHEL terminal sessions.

**Additional resources**

-   [Managing smart card authentication](https://docs.redhat.com/documentation/en-us/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/index)
-   [One time password (OTP) authentication in Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-the-identity-management-web-ui-using-one-time-passwords#one-time-password-otp-authentication-in-identity-management)
-   [Enabling passkey authentication in IdM environment](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/enabling-passkey-authentication-in-idm-environment)
-   [Using external identity providers to authenticate to IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/using-external-identity-providers-to-authenticate-to-idm)
-   [Configuring SSSD to use a generic identity provider](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/configuring-sssd-to-use-a-generic-identity-provider)

### [1.2. Overview of single sign-on in RHEL](#overview-of-single-sign-on-in-rhel) {#overview-of-single-sign-on-in-rhel .title}

Single sign-on (SSO) consolidates credentials, allowing users to log in once for access to all network resources. RHEL implements SSO through Kerberos and smart cards, creating a centralized identity store that improves both convenience and security.

Red Hat Enterprise Linux supports SSO for several resources, including logging into workstations, unlocking screen savers, and accessing secured web pages using Mozilla Firefox. With other available system services such as Privileged Access Management (PAM), Name Service Switch (NSS), and Kerberos, other system applications can be configured to use those identity sources.

SSO is both a convenience to users and another layer of security for the server and the network. SSO hinges on secure and effective authentication. RHEL provides two authentication mechanisms to enable SSO:

-   Kerberos-based authentication, through both Kerberos realms and Active Directory domains
-   Smart card-based authentication

Both methods create a centralized identity store (either through a Kerberos realm or a certificate authority in a public key infrastructure), and the local system services then use those identity domains rather than maintaining multiple local stores.

### [1.3. Services available for local user authentication](#services-available-for-local-user-authentication) {#services-available-for-local-user-authentication .title}

Red Hat Enterprise Linux provides specific services to configure local user authentication. Use these tools to manage identity backends, control low-level system calls, and enforce authentication policies.

Authentication setup

:   -   The Authentication Configuration tool `authselect`{.literal} sets up different identity back ends and means of authentication (such as passwords, fingerprints, or smart cards) for the system.

Identity back end setup

:   -   The Security System Services Daemon (SSSD) sets up multiple identity providers, primarily LDAP-based directories such as Microsoft Active Directory or IdM. Both the local system and applications can use these identity providers for authentication. SSSD caches passwords and tickets, allowing offline authentication and single sign-on by reusing credentials.
    -   The `realmd`{.literal} service is a command-line utility that allows you to configure an authentication back end, which is SSSD for IdM. The `realmd`{.literal} service detects available IdM domains based on the DNS records, configures SSSD, and then joins the system as an account to a domain.
    -   Name Service Switch (NSS) is a mechanism for low-level system calls that return information about users, groups, or hosts. NSS determines what source, that is, which modules, should be used to obtain the required information. For example, user information can be located in traditional UNIX files, such as the `/etc/passwd`{.literal} file, or in LDAP-based directories, while host addresses can be read from files, such as the `/etc/hosts`{.literal} file, or the DNS records; NSS locates where the information is stored.

Authentication mechanisms

:   -   Pluggable Authentication Modules (PAM) provide a system to configure authentication policies. An application using PAM for authentication loads different modules that control different aspects of authentication; which PAM module an application uses is based on how the application is configured. The available PAM modules include Kerberos, Winbind, SSSD, or local UNIX file-based authentication.

Other services and applications are also available, but these are common ones.

## [Chapter 2. Configuring user authentication using authselect](#configuring-user-authentication-using-authselect) {#chapter-2.-configuring-user-authentication-using-authselect .title}

The `authselect`{.literal} utility simplifies system identity and authentication configuration. Utilize specific profiles to automatically manage PAM and NSS settings, ensuring consistent access controls for local and remote users.

### [2.1. What is authselect used for](#what-is-authselect-used-for) {#what-is-authselect-used-for .title}

Authselect simplifies system identity management by providing ready-made configuration profiles. Select a profile to automatically generate the necessary PAM and NSS settings, ensuring consistent authentication across local and remote sources.

You can use the default profile set or create a custom profile. Note that you must manually update custom profiles to keep them up to date with your system.

**Authselect profiles**

local
:   Configures authentication to handle local users without SSSD by using traditional system files such as `/etc/passwd`{.literal} and `/etc/shadow`{.literal}. This is the default profile.

sssd
:   Enables SSSD for systems that use LDAP authentication. Use this profile to integrate remote identity providers and support features such as smart cards, GSSAPI, and session recording.

winbind
:   Enables the Winbind utility for systems directly integrated with Microsoft Active Directory.

After selecting an `authselect`{.literal} profile for a given host, the profile applies to all users logging into the host.

Red Hat recommends using `authselect`{.literal} to manage authentication settings in semi-centralized identity management environments, for example if your organization utilizes LDAP or Winbind databases to authenticate users to use services in your domain.

If the provided profile set is not sufficient, you can create a custom profile.

Warning

You do not need to use `authselect`{.literal} if:

-   Your host is part of Red Hat Enterprise Linux Identity Management (IdM). Joining your host to an IdM domain with the `ipa-client-install`{.literal} command automatically configures SSSD authentication on your host.
-   Your host is joined to Active Directory through SSSD. Calling the `realm join`{.literal} command to join your host to an Active Directory domain automatically configures SSSD authentication on your host.

Red Hat recommends against changing the `authselect`{.literal} profiles configured by `ipa-client-install`{.literal} or `realm join`{.literal}. If you need to modify them, display the current settings before making any modifications, so you can revert back to them if necessary:

``` {.language-plaintext tabindex="-1"}
$ authselect current
Profile ID: sssd
Enabled features:
- with-sudo
- with-mkhomedir
- with-smartcard
```

#### [2.1.1. Files and directories modified by authselect](#files_and_directories_modified_by_authselect) {#files-and-directories-modified-by-authselect .title}

`authselect`{.literal} modifies only a limited set of configuration files, making it easier to manage and troubleshoot authentication settings.

+:-------------------------------------------+:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/etc/nsswitch.conf`{.literal}             | The GNU C Library and other applications use this Name Service Switch (NSS) configuration file to determine the sources from which to obtain name-service information in a range of categories, and in what order. Each category of information is identified by a database name.                                           |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/etc/pam.d/*`{.literal} files             | Linux-PAM (Pluggable Authentication Modules) is a system of modules that handle the authentication tasks of applications (services) on the system. The nature of the authentication is dynamically configurable: the system administrator can choose how individual service-providing applications will authenticate users. |
|                                            |                                                                                                                                                                                                                                                                                                                             |
|                                            | The configuration files in the `/etc/pam.d/`{.literal} directory list the PAMs that will perform authentication tasks required by a service, and the appropriate behavior of the PAM-API in the event that individual PAMs fail.                                                                                            |
|                                            |                                                                                                                                                                                                                                                                                                                             |
|                                            | Among other things, these files contain information about:                                                                                                                                                                                                                                                                  |
|                                            |                                                                                                                                                                                                                                                                                                                             |
|                                            | -   User password lockout rules                                                                                                                                                                                                                                                                                             |
|                                            | -   The ability to authenticate with a smart card                                                                                                                                                                                                                                                                           |
|                                            | -   The ability to authenticate with a fingerprint reader                                                                                                                                                                                                                                                                   |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/etc/dconf/db/distro.d/*`{.literal} files | This directory holds configuration profiles for the `dconf`{.literal} utility, which you can use to manage settings for the GNOME Desktop Graphical User Interface (GUI).                                                                                                                                                   |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Show more

**Additional resources**

-   [Creating and deploying your own `authselect`{.literal} profile](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_authentication_and_authorization_in_rhel/configuring-user-authentication-using-authselect#creating-and-deploying-your-own-authselect-profile)

### [2.2. Choosing an authselect profile](#choosing-an-authselect-profile) {#choosing-an-authselect-profile .title}

Select specific `authselect`{.literal} profiles to enforce authentication policies on a host. This process configures the system to use the chosen identity provider for all user logins.

**Prerequisites**

-   You need `root`{.literal} credentials to run `authselect`{.literal} commands

Note

Make sure that the configuration files that are relevant for your profile are configured properly before finishing the `authselect select`{.literal} procedure. For example, if the `sssd`{.literal} daemon is not configured correctly and active, running `authselect select`{.literal} results in only local users being able to authenticate, using `pam_unix`{.literal}.

**Procedure**

-   Select the `authselect`{.literal} profile that is appropriate for your authentication provider. Replace *`<profile>`{.literal}* with the profile name that you want to use:

    ``` {.language-plaintext tabindex="-1"}
    # authselect select <profile>
    ```

-   Optional: You can modify the default profile settings by enabling or disabling features that the selected profile provides.

    ``` {.language-plaintext tabindex="-1"}
    # authselect select <profile> <feature>
    ```

    For example to select the `sssd`{.literal} profile and enable smart card authentication in addition to password authentication:

    ``` {.language-plaintext tabindex="-1"}
    # authselect select sssd with-smartcard
    ```

**Verification**

1.  Verify `sss`{.literal} entries for SSSD are present in `/etc/nsswitch.conf`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    passwd:     sss files
    group:      sss files
    netgroup:   sss files
    automount:  sss files
    services:   sss files
    ...
    ```

2.  Review the contents of the `/etc/pam.d/system-auth`{.literal} file for `pam_sss.so`{.literal} entries:

    ``` {.language-plaintext tabindex="-1"}
    # Do not modify this file manually, use authselect instead. Any user changes will be overwritten.
    # You can stop authselect from managing your configuration by calling 'authselect opt-out'.
    # See authselect(8) for more details.

    auth        required        pam_env.so
    auth        required        pam_faildelay.so delay=2000000
    auth        [default=1 ignore=ignore success=ok]    pam_succeed_if.so uid >= 1000 quiet
    auth        [default=1 ignore=ignore success=ok]    pam_localuser.so
    auth        sufficient      pam_unix.so nullok try_first_pass
    auth        requisite       pam_succeed_if.so uid >= 1000 quiet_success
    auth        sufficient      pam_sss.so forward_pass
    auth        required        pam_deny.so

    account     required        pam_unix.so
    account     sufficient      pam_localuser.so
    ...
    ```

**Additional resources**

-   [What is authselect used for](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_authentication_and_authorization_in_rhel/configuring-user-authentication-using-authselect#what-is-authselect-used-for)
-   [Creating and deploying your own authselect profile](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_authentication_and_authorization_in_rhel/configuring-user-authentication-using-authselect#creating-and-deploying-your-own-authselect-profile)

### [2.3. Creating and deploying your own authselect profile](#creating-and-deploying-your-own-authselect-profile) {#creating-and-deploying-your-own-authselect-profile .title}

Create custom profiles by duplicating default templates to accommodate specific requirements. This approach permits detailed configuration changes while maintaining system compatibility. Applying the profile enforces these settings for all users.

**Procedure**

1.  To create your custom profile, run the `authselect create-profile`{.literal} command. Replace *`<custom_profile>`{.literal}* with the desired profile name. For example, to create a profile based on the ready-made `sssd`{.literal} profile with the option to configure the items in the `/etc/nsswitch.conf`{.literal} file yourself, use the following command:

    ``` {.language-plaintext tabindex="-1"}
    # authselect create-profile <custom_profile> -b sssd --symlink-meta --symlink-pam
    ```

    ``` {.language-plaintext tabindex="-1"}
    New profile was created at /etc/authselect/custom/<custom_profile>
    ```

    Warning

    If you are planning to modify `/etc/authselect/custom/<custom_profile>/{password-auth,system-auth,fingerprint-auth,smartcard-auth,postlogin}`{.literal}, then enter the command above without the `--symlink-pam`{.literal} option. This is to ensure that the modification persists during the upgrade of `authselect-libs`{.literal}.

    Including the `--symlink-pam`{.literal} option in the command means that PAM templates are symbolic links to the origin profile files instead of their copy; including the `--symlink-meta`{.literal} option means that meta files, such as README and REQUIREMENTS are symbolic links to the origin profile files instead of their copy. This ensures that all future updates to the PAM templates and meta files in the original profile are reflected in your custom profile, too.

    The command creates a copy of the `/etc/nsswitch.conf`{.literal} file in the `/etc/authselect/custom/`{.literal}*`<custom_profile>`{.literal}*`/`{.literal} directory.

2.  Configure the `/etc/authselect/custom/`{.literal}*`<custom_profile>`{.literal}*`/nsswitch.conf`{.literal} file.

3.  Select the custom profile by running the `authselect select`{.literal} command with `custom/`{.literal}*`<custom_profile>`{.literal}* as a parameter:

    ``` {.language-plaintext tabindex="-1"}
    # authselect select custom/<custom_profile>
    ```

    Selecting the *`<custom_profile>`{.literal}* profile for your machine means that if the `sssd`{.literal} profile is subsequently updated by Red Hat, you benefit from all the updates with the exception of updates made to the `/etc/nsswitch.conf`{.literal} file.

    **Example creating a custom profile based on the sssd profile:**

    You can create a profile based on the `sssd`{.literal} profile which only consults the local static table lookup for hostnames in the `/etc/hosts`{.literal} file, not in the `dns`{.literal} or `myhostname`{.literal} databases.

    1.  Edit the `/etc/nsswitch.conf`{.literal} file by editing the following line:

        ``` {.language-plaintext tabindex="-1"}
        hosts:      files
        ```

    2.  Create a custom profile based on `sssd`{.literal} that excludes changes to `/etc/nsswitch.conf`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # authselect create-profile custom-sssd-profile -b sssd --symlink-meta --symlink-pam
        ```

    3.  Select the profile:

        ``` {.language-plaintext tabindex="-1"}
        # authselect select custom/custom-sssd-profile
        ```

    4.  Optional: Check that selecting the custom profile has

        -   created the `/etc/pam.d/system-auth`{.literal} file according to the chosen `sssd`{.literal} profile

        -   left the configuration in the `/etc/nsswitch.conf`{.literal} unchanged:

            ``` {.language-plaintext tabindex="-1"}
            hosts:      files
            ```

            Note

            Running `authselect select`{.literal} `sssd`{.literal} would, in contrast, result in `hosts: files dns myhostname`{.literal}

**Additional resources**

-   [What is authselect used for](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_authentication_and_authorization_in_rhel/configuring-user-authentication-using-authselect#what-is-authselect-used-for)

### [2.4. Opting out of using authselect](#opting-out-of-using-authselect) {#opting-out-of-using-authselect .title}

You cannot uninstall `authselect`{.literal} but can opt out to stop it from managing configurations. This action restores PAM and NSS files to their default locations, returning full manual control over authentication settings.

Important

Authselect ensures consistent and supported management of system authentication and identity configuration. Opting out might lead to unsupported or inconsistent configurations, which can cause authentication issues. If you require a special configuration, consider creating a custom profile within the `authselect`{.literal} framework.

**Procedure**

-   To stop `authselect`{.literal} from managing your system's configuration:

    ``` {.language-plaintext tabindex="-1"}
    # authselect opt-out
    ```

    To start using `authselect`{.literal} again, run `authselect select `{.literal}*`<profile_name>`{.literal}*.

## [Chapter 3. Understanding SSSD and its benefits](#understanding-sssd-and-its-benefits) {#chapter-3.-understanding-sssd-and-its-benefits .title}

The System Security Services Daemon (SSSD) connects local systems to remote identity providers, including LDAP and Active Directory. It retrieves and caches credentials to enable offline authentication, reduce network traffic, and streamline access control for system services.

### [3.1. How SSSD works](#how-sssd-works) {#how-sssd-works .title}

SSSD functions by linking a local client to an external backend provider. The service operates in two stages: connecting to the remote source to retrieve identity data, then creating a local cache to verify credentials without creating permanent local accounts.

SSSD supports multiple identity and authentication providers, such as:

-   LDAP directories
-   Identity Management (IdM) domains
-   Active Directory (AD) domains
-   Kerberos realms

SSSD works in two stages:

1.  It connects the client to a remote provider to retrieve identity and authentication information.
2.  It uses the obtained authentication information to create a local cache of users and credentials on the client.

Users on the local system are then able to authenticate using the user accounts stored in the remote provider.

SSSD does not create user accounts on the local system. However, SSSD can be configured to create home directories for IdM users. Once created, an IdM user home directory and its contents on the client are not deleted when the user logs out.

**Figure 3.1. How SSSD works**

SSSD can also provide caches for several system services, such as Name Service Switch (NSS) or Pluggable Authentication Modules (PAM).

Note

Only use the SSSD service for caching user information. Running both Name Service Caching Daemon (NSCD) and SSSD for caching on the same system might lead to performance issues and conflicts.

### [3.2. Benefits of using SSSD](#benefits-of-using-sssd) {#benefits-of-using-sssd .title}

The System Security Services Daemon (SSSD) enhances system efficiency by caching credentials locally. This capability enables offline authentication, minimizes traffic to remote providers, and consolidates network access into a single user account.

Offline authentication
:   SSSD optionally keeps a cache of user identities and credentials retrieved from remote providers. In this setup, a user - provided they have already authenticated once against the remote provider at the start of the session - can successfully authenticate to resources even if the remote provider or the client are offline.

A single user account: improved consistency of the authentication process

:   With SSSD, it is not necessary to maintain both a central account and a local user account for offline authentication. The conditions are:

    -   In a particular session, the user must have logged in at least once: the client must be connected to the remote provider when the user logs in for the first time.

    -   Caching must be enabled in SSSD.

        Without SSSD, remote users often have multiple user accounts. For example, to connect to a virtual private network (VPN), remote users have one account for the local system and another account for the VPN system. In this scenario, you must first authenticate on the private network to fetch the user from the remote server and cache the user credentials locally.

        With SSSD, thanks to caching and offline authentication, remote users can connect to network resources simply by authenticating to their local machine. SSSD then maintains their network credentials.

Reduced load on identity and authentication providers
:   When requesting information, the clients first check the local SSSD cache. SSSD contacts the remote providers only if the information is not available in the cache.

### [3.3. Multiple SSSD configuration files on a per-client basis](#multiple-sssd-configuration-files-on-a-per-client-basis) {#multiple-sssd-configuration-files-on-a-per-client-basis .title}

The System Security Services Daemon (SSSD) builds its configuration by combining the primary file with modular files in the `conf.d`{.literal} directory. This structure helps you to maintain global defaults while applying specific overrides or extensions for individual clients.

The default configuration file for SSSD is `/etc/sssd/sssd.conf`{.literal}. Apart from this file, SSSD can read its configuration from all `*.conf`{.literal} files in the `/etc/sssd/conf.d/`{.literal} directory.

This combination allows you to use the default `/etc/sssd/sssd.conf`{.literal} file on all clients and add additional settings in further configuration files to extend the functionality individually on a per-client basis.

SSSD reads the configuration files in this order:

1.  The primary `/etc/sssd/sssd.conf`{.literal} file.
2.  Other `*.conf`{.literal} files in `/etc/sssd/conf.d/`{.literal}, processed in alphabetical order.

If the same parameter appears in multiple configuration files, SSSD uses the last read parameter.

Note

SSSD does not read hidden files (files starting with `.`{.literal}) in the `conf.d`{.literal} directory.

### [3.4. Identity and authentication providers for SSSD](#identity-and-authentication-providers-for-sssd) {#identity-and-authentication-providers-for-sssd .title}

SSSD links local clients to external backends like LDAP, Identity Management (IdM), Active Directory (AD), and Kerberos. Configure these connections as domains, assigning specific providers to handle identity, authentication, or access control tasks.

#### [3.4.1. Identity and authentication providers as SSSD domains](#identity_and_authentication_providers_as_sssd_domains) {#identity-and-authentication-providers-as-sssd-domains .title}

Define SSSD domains in `/etc/sssd/sssd.conf`{.literal} to map backends to specific functions. You can configure a single domain to handle identity lookups, authentication requests, and access control either separately or together.

The providers are listed in the `[domain/`{.literal}*`<domain_name>`{.literal}*`]`{.literal} or `[domain/default]`{.literal} section of the file.

You can configure a single domain as one of the following providers:

-   An *identity provider*, which supplies user information such as UID and GID.

    -   Specify a domain as the *identity provider* by using the `id_provider`{.literal} option in the `[domain/`{.literal}*`<domain_name>`{.literal}*`]`{.literal} section of the `/etc/sssd/sssd.conf`{.literal} file.

-   An *authentication provider*, which handles authentication requests.

    -   Specify a domain as the *authentication provider* by using the `auth_provider`{.literal} option in the `[domain/`{.literal}*`<domain_name>`{.literal}*`]`{.literal} section of `/etc/sssd/sssd.conf`{.literal}.

-   An *access control provider*, which handles authorization requests.

    -   Specify a domain as the *access control provider* using the `access_provider`{.literal} option in the `[domain/`{.literal}*`<domain_name>`{.literal}*`]`{.literal} section of `/etc/sssd/sssd.conf`{.literal}. By default, the option is set to `permit`{.literal}, which always allows all access. See the **sssd.conf**(5) man page for details.

-   A combination of these providers, for example if all the corresponding operations are performed within a single server.

    -   In this case, the `id_provider`{.literal}, `auth_provider`{.literal}, and `access_provider`{.literal} options are all listed in the same `[domain/`{.literal}*`<domain_name>`{.literal}*`]`{.literal} or `[domain/default]`{.literal} section of `/etc/sssd/sssd.conf`{.literal}.

Note

You can configure multiple domains for SSSD. You must configure at least one domain, otherwise SSSD will not start.

#### [3.4.2. Proxy providers](#proxy_providers) {#proxy-providers .title}

Proxy providers serve as intermediaries for resources SSSD cannot directly access. SSSD connects to the proxy service to load external libraries, enabling integration with legacy systems like NIS and alternative authentication hardware.

You can configure SSSD to use a proxy provider to enable:

-   Alternative authentication methods, such as a fingerprint scanner
-   Legacy systems, such as NIS
-   A local system account defined in the `/etc/passwd`{.literal} file as an identity provider and a remote authentication provider, for example Kerberos
-   Authentication of local users using smart cards

#### [3.4.3. Available combinations of identity and authentication providers](#available_combinations_of_identity_and_authentication_providers) {#available-combinations-of-identity-and-authentication-providers .title}

With SSSD, you can mix specific providers for identity and authentication tasks. You can configure unified backends like Active Directory or hybrid setups, such as combining LDAP directories with Kerberos realms.

+------------------------------------------------------------------------+-----------------------------------+
| Identity provider                                                      | Authentication provider           |
+:=======================================================================+:==================================+
| Identity Management [^\[a\]^](#ftn.idm140250347090512)                 | Identity Management               |
+------------------------------------------------------------------------+-----------------------------------+
| Active Directory                                                       | Active Directory                  |
+------------------------------------------------------------------------+-----------------------------------+
| LDAP                                                                   | LDAP                              |
+------------------------------------------------------------------------+-----------------------------------+
| LDAP                                                                   | Kerberos                          |
+------------------------------------------------------------------------+-----------------------------------+
| Proxy                                                                  | Proxy                             |
+------------------------------------------------------------------------+-----------------------------------+
| Proxy                                                                  | LDAP                              |
+------------------------------------------------------------------------+-----------------------------------+
| Proxy                                                                  | Kerberos                          |
+------------------------------------------------------------------------+-----------------------------------+
| [^\[a\]^](#idm140250347090512) An extension of the LDAP provider type. |                                   |
+------------------------------------------------------------------------+-----------------------------------+

: Table 3.1. Available combinations of identity and authentication providers

Show more

**Additional resources**

-   [Configuring user authentication using authselect](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_authentication_and_authorization_in_rhel/configuring-user-authentication-using-authselect)
-   [Querying domain information using SSSD](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_authentication_and_authorization_in_rhel/querying-domain-information-using-sssd)
-   [Reporting on user access on hosts using SSSD](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_authentication_and_authorization_in_rhel/reporting-on-user-access-on-hosts-using-sssd)

## [Chapter 4. Configuring SSSD to use LDAP and require TLS authentication](#configuring-sssd-to-use-ldap-and-require-tls-authentication) {#chapter-4.-configuring-sssd-to-use-ldap-and-require-tls-authentication .title}

Configure the System Security Services Daemon (SSSD) to authenticate users against standalone LDAP servers. Enforcing TLS encryption ensures secure communication, protecting identity data from interception during retrieval.

Note

The default value of `ldap_id_use_start_tls`{.literal} is set to `true`{.literal} to enforce TLS, as it is not safe to use unencrypted communication.

Setting this value to `false`{.literal} disables TLS encryption, forcing identity lookups over unencrypted ldap://. This exposes the system to man-in-the-middle (MITM) attacks, where an attacker can intercept and modify LDAP search results, such as UID or GID values, to impersonate users and gain unauthorized access.

Verify that your environment is trusted before choosing unencrypted communication for `id_provider = ldap`{.literal}. Note that `id_provider = ad`{.literal} and `id_provider = ipa`{.literal} maintain encrypted connections through SASL and GSSAPI.

### [4.1. An OpenLDAP client using SSSD to retrieve data from LDAP in an encrypted way](#an-openldap-client-using-sssd-to-retrieve-data-from-ldap-in-an-encrypted-way) {#an-openldap-client-using-sssd-to-retrieve-data-from-ldap-in-an-encrypted-way .title}

SSSD operates as a client to retrieve identity data from OpenLDAP servers. This configuration utilizes encrypted connections and supports authentication through either Kerberos tickets or standard LDAP passwords.

Important

Configuring SSSD with LDAP is a complex procedure requiring a high level of expertise in SSSD and LDAP. Consider using an integrated and automated solution such as Active Directory or Identity Management (IdM) instead.

### [4.2. Configuring SSSD to use LDAP and require TLS authentication](#configuring-sssd-to-use-ldap-and-require-tls-authentication_configuring-sssd-to-use-ldap-and-require-tls-authentication) {#configuring-sssd-to-use-ldap-and-require-tls-authentication .title}

Establish a secure connection between Red Hat Enterprise Linux (RHEL) and an OpenLDAP server by configuring SSSD to enforce TLS. This process ensures that all identity data retrieval and authentication requests occur over an encrypted channel.

Use the following client configuration:

-   The RHEL system authenticates users stored in an OpenLDAP user account database.
-   The RHEL system uses the System Security Services Daemon (SSSD) service to retrieve user data.
-   The RHEL system communicates with the OpenLDAP server over a TLS-encrypted connection.

Note

You can alternatively use this procedure to configure your RHEL system as a client of a Red Hat Directory Server.

**Prerequisites**

-   The OpenLDAP server is installed and configured with user information.
-   You have root permissions on the host you are configuring as the LDAP client.
-   On the host you are configuring as the LDAP client, the `/etc/sssd/sssd.conf`{.literal} file has been created and configured to specify `ldap`{.literal} as the `autofs_provider`{.literal} and the `id_provider`{.literal}.
-   You have a PEM-formatted copy of the root CA signing certificate chain from the Certificate Authority that issued the OpenLDAP server certificate, stored in a local file named `core-dirsrv.ca.pem`{.literal}.

**Procedure**

1.  Install the requisite packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf -y install openldap-clients sssd sssd-ldap oddjob-mkhomedir
    ```

2.  Switch the authentication provider to `sssd`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # authselect select sssd with-mkhomedir
    ```

3.  Copy the `core-dirsrv.ca.pem`{.literal} file containing the root CA signing certificate chain from the Certificate Authority that issued the OpenLDAP server's SSL/TLS certificate into the `/etc/openldap/certs`{.literal} folder.

    ``` {.language-plaintext tabindex="-1"}
    # cp core-dirsrv.ca.pem /etc/openldap/certs
    ```

4.  Add the URL and suffix of your LDAP server to the `/etc/openldap/ldap.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    URI ldap://ldap-server.example.com/
    BASE dc=example,dc=com
    ```

5.  In the `/etc/openldap/ldap.conf`{.literal} file, add a line pointing the **TLS_CACERT** parameter to `/etc/openldap/certs/core-dirsrv.ca.pem`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # When no CA certificates are specified the Shared System Certificates
    # are in use. In order to have these available along with the ones specified
    # by TLS_CACERTDIR one has to include them explicitly:
    TLS_CACERT /etc/openldap/certs/core-dirsrv.ca.pem
    ```

6.  In the `/etc/sssd/sssd.conf`{.literal} file, add your environment values to the `ldap_uri`{.literal} and `ldap_search_base`{.literal} parameters:

    ``` {.language-plaintext tabindex="-1"}
    [domain/default]
    id_provider = ldap
    autofs_provider = ldap
    auth_provider = ldap
    chpass_provider = ldap
    ldap_uri = ldap://ldap-server.example.com/
    ldap_search_base = dc=example,dc=com
    cache_credentials = True
    ldap_tls_cacertdir = /etc/openldap/certs
    ldap_tls_reqcert = allow

    [sssd]
    services = nss, pam, autofs
    domains = default

    [nss]
    homedir_substring = /home
    …
    ```

7.  In `/etc/sssd/sssd.conf`{.literal}, specify the TLS authentication requirement by modifying the `ldap_tls_cacert`{.literal} and `ldap_tls_reqcert`{.literal} values in the `[domain]`{.literal} section:

    ``` {.language-plaintext tabindex="-1"}
    …
    cache_credentials = True
    ldap_tls_cacert = /etc/openldap/certs/core-dirsrv.ca.pem
    ldap_tls_reqcert = hard
    …
    ```

8.  Change the permissions on the `/etc/sssd/sssd.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # chmod 600 /etc/sssd/sssd.conf
    ```

9.  Restart and enable the SSSD service and the `oddjobd`{.literal} daemon:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd oddjobd
    # systemctl enable sssd oddjobd
    ```

10. Optional: If your LDAP server uses the deprecated TLS 1.0 or TLS 1.1 protocols, switch the system-wide cryptographic policy on the client system to the LEGACY level to allow RHEL to communicate using these protocols:

    ``` {.language-plaintext tabindex="-1"}
    # update-crypto-policies --set LEGACY
    ```

    For more details, see the [Strong crypto defaults in RHEL 8 and deprecation of weak crypto algorithms](https://access.redhat.com/articles/3642912) Knowledgebase article on the Red Hat Customer Portal and the `update-crypto-policies(8)`{.literal} man page on your system.

**Verification**

-   Verify you can retrieve user data from your LDAP server by using the `id`{.literal} command and specifying an LDAP user:

    ``` {.language-plaintext tabindex="-1"}
    # id <ldap_user>
    ```

    ``` {.language-plaintext tabindex="-1"}
    uid=17388( <ldap_user>) gid=45367(sysadmins) groups=45367(sysadmins),25395(engineers),10(wheel),1202200000(admins)
    ```

The system administrator can now query users from LDAP using the `id`{.literal} command. The command returns a correct user ID and group membership.

## [Chapter 5. Configuring SSSD to use a generic identity provider](#configuring-sssd-to-use-a-generic-identity-provider) {#chapter-5.-configuring-sssd-to-use-a-generic-identity-provider .title}

In Red Hat Enterprise Linux (RHEL), the System Security Services Daemon (SSSD) supports a direct integration with modern identity providers (IdP) that use the OAuth 2.0 and OpenID Connect (OIDC) protocols. This currently allows you to authenticate users against Red Hat build of Keycloak or Microsoft Entra ID without requiring a traditional LDAP or Active Directory infrastructure.

Important

The generic identity provider is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

### [5.1. Prerequisites](#prerequisites) {#prerequisites .title}

-   The `sssd-idp`{.literal} package is installed on the RHEL system. For more details, see the `sssd-idp`{.literal} man page.
-   You have administrator access to your identity provider (Keycloak or Entra ID).
-   The RHEL system can reach the IdP's discovery and token endpoints over HTTPS.

### [5.2. How SSSD authenticates with a generic IdP](#how-sssd-authenticates-with-a-generic-idp) {#how-sssd-authenticates-with-a-generic-idp .title}

SSSD (System Security Services Daemon) uses the OAuth 2.0 Device Authorization Grant flow to handle authentication with a generic IdP where a web browser cannot be directory rendered, such as RHEL terminal sessions.

1.  SSSD generates a user-friendly URL and a unique device code.
2.  The user opens the URL on a separate device (such as a smartphone or laptop).
3.  The user enters the code to authorize the RHEL login session, and, if the user is not already logged in, authenticates with the IdP.
4.  SSSD automatically detects the authorization and grants access to the RHEL session.

Note

If the URL is provided by the server-side, SSSD might show a single URL where the code is already included in the URL, for example, [`https://master.keycloak.test:8443/auth/realms/device?user_code=NVCT-RUFA`{.literal}](https://master.keycloak.test:8443/auth/realms/device?user_code=NVCT-RUFA) instead of URL [`https://master.keycloak.test:8443/auth/realms/device`{.literal}](https://master.keycloak.test:8443/auth/realms/device) and the `NVCT-RUFA`{.literal} code provided separately.

### [5.3. Registering an SSSD client in Red Hat build of Keycloak](#registering-an-sssd-client-in-red-hat-build-of-keycloak) {#registering-an-sssd-client-in-red-hat-build-of-keycloak .title}

Before configuring SSSD, you must register the SSSD client in Keycloak. This client manages the user authentication via the Device Authorization Grant and performs user and group lookups on behalf of SSSD.

**Prerequisites**

-   Red Hat build of Keycloak is installed and configured.
-   You have administrator access to the Red Hat build of Keycloak Admin Console.
-   The system has a valid SSL/TLS certificate if using HTTPS for the IdP.

**Procedure**

1.  Log in to the Keycloak Admin Console and select your `Realm`{.literal}.

2.  Navigate to **Clients \> Create client** and select **OpenID Connect** as the **Client type**.

3.  Specify a Client ID, for example, **RHELSSSDClient** and click **Next**.

4.  Specify a name for the client, for example **RHELSSSDClient**.

5.  Click **Next** and ensure the following settings are enabled for the SSSD client:

    -   **Client authentication** is on.
    -   Under **Authentication flow**, ensure the **OAuth 2.0 Device Authorization Grant** and **Service accounts roles** are both enabled.

6.  Click **Next** and click **Save**.

7.  On your SSSD client page, click **Service account roles** to add the required roles to your client.

8.  Click **Assign Roles** and select the following roles from the list:

    -   **View-groups**
    -   **Query-groups**
    -   **Query-users**
    -   **View-users**

9.  Click **Assign**.

10. Click **Clients \> RHELSSSDClient**.

11. Select the **Credentials** tab.

12. Click the copy icon beside the **Client Secret** to save it to your clipboard.

    Use this **Client Secret** to configure SSSD for generic IdP authentication.

### [5.4. Registering an SSSD client in Microsoft Entra ID](#registering-an-sssd-client-in-microsoft-entra-id) {#registering-an-sssd-client-in-microsoft-entra-id .title}

Before configuring SSSD, you must register the SSSD client in your IdP. This client in Microsoft Entra ID handles the user authentication via the Device Authorization Grant and also performs the necessary user and group lookups on behalf of SSSD. Registering your application in Microsoft Entra establishes a trust relationship between your app and the Microsoft identity platform.

**Prerequisites**

-   Your Microsoft Entra ID tenant is configured and you have administrator access.
-   The system has a valid SSL/TLS certificate if using HTTPS for the IdP.

**Procedure**

1.  Sign in to the Microsoft Entra admin center.

2.  Go to **Identity \> Applications \> App registrations \> New registration**.

3.  Enter a meaningful name for your application, for example **RHELSSSDClient**, and select the supported account types.

4.  Under **Authentication**, choose one of the following:

    a.  If you are using the device code flow without a secret, ensure **Allow public client flows** is set to **Yes**.
    b.  If you are configuring a confidential client, navigate to **Certificates & secrets** and create a **Client secret**.

5.  Copy the **Application (client) ID** and **Directory (tenant) ID**.

6.  Grant the registered application specific Application Permissions (not Delegated) to allow SSSD to retrieve user and group metadata via Client Credentials. Configure these under **Manage \> API permissions** in the Microsoft Entra admin center:

    -   `Group.Read.All`{.literal}

    -   `GroupMember.Read.All`{.literal}

    -   `User.Read.All`{.literal} (enables SSSD to look up other users during the identity phase)

    -   `User.Read`{.literal}

    -   **Admin Consent**: All `Application`{.literal} level permissions require a status of `Granted for [Organization]`{.literal} to take effect.

        Note

        You must grant **Admin Consent** for `User.Read`{.literal}. Without it, user authentication might fail if the SSSD option `idp_auth_scope`{.literal} excludes the `user.read`{.literal} scope.

### [5.5. Configuring SSSD for generic IdP authentication](#configuring-sssd-for-generic-idp-authentication) {#configuring-sssd-for-generic-idp-authentication .title}

Configure the System Security Services Daemon (SSSD) to authenticate users directly against modern identity providers. By modifying `/etc/sssd/sssd.conf`{.literal}, you enable secure communication between RHEL and your chosen OIDC-compliant provider, currently either Red Hat build by Keycloak or Microsoft Entra ID.

**Prerequisites**

-   The `sssd-idp`{.literal} package is installed.

**Procedure**

1.  To enable the generic IdP provider, open `/etc/sssd/sssd.conf`{.literal} in a text editor.

2.  Define the domain configuration for either Red Hat Build of Keycloak or Microsoft Entra ID using the `id_provider=idp`{.literal} option.

    a.  To define the configuration for Red Hat Build of Keycloak, add the following to the `sssd.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        [sssd]
        services = nss, pam
        domains = keycloak

        [domain/keycloak]
        idp_type = keycloak:https://master.keycloak.test:8443/auth/admin/realms/master/
        id_provider = idp
        auto_private_groups = true
        use_fully_qualified_names = true
        idp_client_id = <RHELSSSDClient>
        idp_client_secret = <RHELSSSDClientPassword>
        idp_token_endpoint = https://master.keycloak.test:8443/auth/realms/master/protocol/openid-connect/token
        idp_userinfo_endpoint = https://master.keycloak.test:8443/auth/realms/master/protocol/openid-connect/userinfo
        idp_device_auth_endpoint = https://master.keycloak.test:8443/auth/realms/master/protocol/openid-connect/auth/device
        idp_id_scope = profile
        idp_auth_scope = openid profile email

        [nss]
        default_shell = /bin/bash
        fallback_homedir = /home/%f
        ```

    b.  To define the configuration for Microsoft Entra ID, add the following to the `sssd.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        [sssd]
        services = nss, pam
        domains = entra_id

        [domain/entra_id]
        id_provider = idp
        auto_private_groups = true
        use_fully_qualified_names = true
        idp_client_id = <UUID_of_your_Entra_ID_client>
        idp_client_id = <Password_of_your_Entra_ID_client>
        idp_token_endpoint = https://login.microsoftonline.com/<your_Entra_ID_tennant_UUID>/oauth2/v2.0/token
        idp_device_auth_endpoint = https://login.microsoftonline.com/<your_Entra_ID_tennant_UUID>/oauth2/v2.0/devicecode
        idp_userinfo_endpoint = https://graph.microsoft.com/v1.0/me
        idp_id_scope = https%3A%2F%2Fgraph.microsoft.com%2F.default
        idp_auth_scope = openid profile email

        [nss]
        default_shell = /bin/bash
        fallback_homedir = /home/%f
        ```

3.  Remove any remaining logs and clear the cache:

    ``` {.language-plaintext tabindex="-1"}
    # sssctl logs-remove
    ```

    ``` {.language-plaintext tabindex="-1"}
    # sssctl cache-remove -ops
    ```

4.  Restart SSSD:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

**Verification**

1.  Attempt to look up a user defined in your IdP:

    ``` {.language-plaintext tabindex="-1"}
    # getent password <user_name>@keycloak
    ```

    ``` {.language-plaintext tabindex="-1"}
    <user_name>@keycloak:*:955808455:955808455::/home/<user_name>@keycloak:/bin/bash
    ```

2.  Attempt to log in as a user defined in your IdP:

    ``` {.language-plaintext tabindex="-1"}
    # ssh -l <user_name>@keycloak localhost
    ```

    ``` {.language-plaintext tabindex="-1"}
    (<user_name>@keycloak@localhost) Authenticate at https://master.keycloak.test:8443/auth/realms/device?user_code=NVCT-RUFA
    ```

3.  Copy the URL to your web browser.

    Note

    Ensure that you are not logged into the Keycloak Admin Console as another user or this attempt to log in fails.

4.  Enter your username and password to sign in. Note that the first time you log in, you have to change to a new password.

5.  On the **Grant Access to YourKeycloakSSSDClient** window, select **Yes**.

6.  Return to the SSSD configuration window and press **ENTER**.

7.  You should be logged in. Verify you are logged in as *\<user_name\>*:

    ``` {.language-plaintext tabindex="-1"}
    [<user_name>@keycloak@client ~] $ id
    ```

    ``` {.language-plaintext tabindex="-1"}
    uid=955808455(<user_name>@keycloak) gid=955808455(<user_name>@keycloak) groups=955808455(<user_name>@keycloak),955844066(group2@keycloak),955943585(group1@keycloak)
    ```

## [Chapter 6. Additional configuration for identity and authentication providers](#additional-configuration-for-identity-and-authentication-providers) {#chapter-6.-additional-configuration-for-identity-and-authentication-providers .title}

Extend the System Security Services Daemon (SSSD) functionality beyond basic connectivity by modifying the `/etc/sssd/sssd.conf`{.literal} file. Advanced configurations include customizing user name formats, enabling offline access, dynamically discovering servers via DNS, and enforcing granular access control rules.

-   Adjust how SSSD interprets and prints full user names to enable offline authentication.
-   Configure DNS Service Discovery, simple Access Provider Rules, and SSSD to apply an LDAP Access Filter.

### [6.1. Adjusting how SSSD interprets full user names](#adjusting-how-sssd-interprets-full-user-names) {#adjusting-how-sssd-interprets-full-user-names .title}

The System Security Services Daemon (SSSD) parses user inputs into name and domain components using Python-compatible regular expressions. You can override the default parsing logic by defining custom patterns with the `re_expression`{.literal} parameter to match specific organizational naming conventions.

By default, SSSD interprets full user names in the format *`<user_name>`{.literal}*`@`{.literal}*`<domain_name>`{.literal}* based on the following regular expression in Python syntax:

``` {.language-plaintext tabindex="-1"}
(?P_<name>_[^@]+)@?(?P_<domain>_[^@]*$)
```

Note

For Identity Management and Active Directory providers, the default user name format is *`<user_name>`{.literal}*`@`{.literal}*`<domain_name>`{.literal}* or *`<NetBIOS_name>\<user_name>`{.literal}*.

You can adjust how SSSD interprets full user names by adding the `re_expression`{.literal} option to the `/etc/sssd/sssd.conf`{.literal} file and defining a custom regular expression.

**Prerequisites**

-   `root`{.literal} access

**Procedure**

1.  Open the `/etc/sssd/sssd.conf`{.literal} file.

2.  Use the `re_expression`{.literal} option to define a custom regular expression.

    a.  To define regular expressions globally for all domains, add `re_expression`{.literal} to the `[sssd]`{.literal} section of the `sssd.conf`{.literal} file.

        You can use the following global expression to define the username in the format of *`<domain>`{.literal}*`\_<username>_`{.literal} or *`<domain>@<user_name>`{.literal}*:

        ``` {.language-plaintext tabindex="-1"}
        [sssd]
        [... file truncated ...]
        re_expression = (?P_<domain>_[\\]*?)\\?(?P_<name>_[\\]+$)
        ```

    b.  To define the regular expressions individually for a particular domain, add `re_expression`{.literal} to the corresponding domain section of the `sssd.conf`{.literal} file.

        You can use the following global expression to define the username in the format of *`<domain>`{.literal}*`\_<username>_`{.literal} or *`<domain>@<user_name>`{.literal}* for the LDAP domain:

        ``` {.language-plaintext tabindex="-1"}
        [domain/LDAP]
        [... file truncated ...]
        re_expression = (?P_<domain>_[\\]*?)\\?(?P_<name>_[\\]+$)
        ```

### [6.2. Adjusting how SSSD prints full user names](#adjusting-how-sssd-prints-full-user-names) {#adjusting-how-sssd-prints-full-user-names .title}

The System Security Services Daemon (SSSD) displays fully qualified user names, for example, `user@domain`{.literal}, by default when `use_fully_qualified_names`{.literal} is active. You can customize this output format using the `full_name_format`{.literal} option to match legacy requirements, such as displaying `domain\user`{.literal}.

If the `use_fully_qualified_names`{.literal} option is enabled in the `/etc/sssd/sssd.conf`{.literal} file, SSSD prints full user names in the format *`<name>`{.literal}*`@`{.literal}*`<domain>`{.literal}* based on the following expansion by default:

``` {.language-plaintext tabindex="-1"}
%1$s@%2$s
```

Note

If `use_fully_qualified_names`{.literal} is not set or is explicitly set to `false`{.literal} for trusted domains, it only prints the user name without the domain component.

You can adjust the format in which SSSD prints full user names by adding the `full_name_format`{.literal} option to the `/etc/sssd/sssd.conf`{.literal} file and defining a custom expansion.

**Prerequisites**

-   `root`{.literal} access

**Procedure**

1.  As `root`{.literal}, open the `/etc/sssd/sssd.conf`{.literal} file.

2.  To define the expansion globally for all domains, add `full_name_format`{.literal} to the `[sssd]`{.literal} section of `sssd.conf`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [sssd]
    [... file truncated ...]
    full_name_format = %1$s@%2$s
    ```

    In this case the user name is displayed as `user@domain.test`{.literal}.

3.  To define the user name printing format for a particular domain, add `full_name_format`{.literal} to the corresponding domain section of `sssd.conf`{.literal}.

    -   To configure the expansion for the Active Directory (AD) domain using `%2$s\%1$s`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        [domain/ad.domain]
        [... file truncated ...]
        full_name_format = %2$s\%1$s
        ```

        In this case the user name is displayed as `ad.domain\user`{.literal}.

    -   To configure the expansion for the Active Directory (AD) domain using `%3$s\%1$s`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        [domain/ad.domain]
        [... file truncated ...]
        full_name_format = %3$s\%1$s
        ```

        In this case the user name is displayed as `AD\user`{.literal} if the flat domain name of the Active Directory domain is set to `AD`{.literal}.

    Note

    SSSD can strip the domain component of the name in some name configurations, which can cause authentication errors. If you set `full_name_format`{.literal} to a non-standard value, you will get a warning prompting you to change it to a standard format.

### [6.3. Enabling offline authentication](#enabling-offline-authentication) {#enabling-offline-authentication .title}

The System Security Services Daemon (SSSD) requires credential caching to enable authentication when the identity provider is unreachable. Enabling `cache_credentials`{.literal} allows users to log in using locally stored hashes of their passwords during network outages, ensuring business continuity.

You can enable credential caching by setting `cache_credentials`{.literal} to `true`{.literal} in the `/etc/sssd/sssd.conf`{.literal} file. Cached credentials refer to passwords and the first authentication factor if two-factor authentication is used. Note that for passkey and smart card authentication, you do not need to set `cache_credentials`{.literal} to true or set any additional configuration; they are expected to work offline as long as a successful online authentication is recorded in the cache.

Important

SSSD never caches passwords in plain text. It stores only a hash of the password.

While credentials are stored as a salted SHA-512 hash, this potentially poses a security risk in case an attacker manages to access the cache file and break a password using a brute force attack. Accessing a cache file requires privileged access, which is the default on RHEL.

**Prerequisites**

-   `root`{.literal} access

**Procedure**

1.  Open the `/etc/sssd/sssd.conf`{.literal} file.

2.  In a domain section, add the `cache_credentials = true`{.literal} setting:

    ``` {.language-plaintext tabindex="-1"}
    [domain/<domain_name>]
    cache_credentials = true
    ```

3.  Optional, but recommended: Configure a time limit for how long SSSD allows offline authentication if the identity provider is unavailable:

    a.  Configure the PAM service to work with SSSD.

    b.  Use the `offline_credentials_expiration`{.literal} option to specify the time limit.

        Note that the limit is set in days.

        For example, to specify that users are able to authenticate offline for 3 days since the last successful login, use:

        ``` {.language-plaintext tabindex="-1"}
        [pam]
        offline_credentials_expiration = 3
        ```

**Additional resources**

-   [Configuring user authentication using authselect](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_authentication_and_authorization_in_rhel/configuring-user-authentication-using-authselect)

### [6.4. Configuring DNS Service Discovery](#configuring-dns-service-discovery) {#configuring-dns-service-discovery .title}

DNS service discovery allows the System Security Services Daemon (SSSD) to automatically locate identity servers by using SRV records. This configuration removes the need to hardcode server IP addresses, enabling dynamic failover and load balancing by querying the DNS infrastructure.

If the identity or authentication server is not explicitly defined in the `/etc/sssd/sssd.conf`{.literal} file, SSSD can discover the server dynamically using DNS service discovery.

For example, if `sssd.conf`{.literal} includes the `id_provider = ldap`{.literal} setting, but the `ldap_uri`{.literal} option does not specify any host name or IP address, SSSD uses DNS service discovery to discover the server dynamically.

Note

SSSD cannot dynamically discover backup servers, only the primary server.

**Prerequisites**

-   `root`{.literal} access

**Procedure**

1.  Open the `/etc/sssd/sssd.conf`{.literal} file.

2.  Set the primary server value to `_srv_`{.literal}.

    For an LDAP provider, the primary server is set using the `ldap_uri`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    [domain/<ldap_domain_name>]
    id_provider = ldap
    ldap_uri = _srv_
    ```

3.  Enable service discovery in the password change provider by setting a service type:

    ``` {.language-plaintext tabindex="-1"}
    [domain/<ldap_domain_name>]
    id_provider = ldap
    ldap_uri = _srv_

    chpass_provider = ldap
    ldap_chpass_dns_service_name = ldap
    ```

4.  Optional: By default, the service discovery uses the domain portion of the system host name as the domain name. To use a different DNS domain, specify the domain name by using the `dns_discovery_domain`{.literal} option.

5.  Optional: By default, the service discovery scans for the LDAP service type. To use a different service type, specify the type by using the `ldap_dns_service_name`{.literal} option.

6.  Optional: By default, SSSD attempts to look up an IPv4 address. If the attempt fails, SSSD attempts to look up an IPv6 address. To customize this behavior, use the `lookup_family_order`{.literal} option.

7.  For every service with which you want to use service discovery, add a DNS record to the DNS server:

    ``` {.language-plaintext tabindex="-1"}
    _<service_name>.<protocol>.<domain_name> <TTL> <priority> <weight> <port_number> <hostname>_
    ```

**Additional resources**

-   [RFC 2782 on DNS service discovery](http://www.ietf.org/rfc/rfc2782.txt)

### [6.5. Configuring simple Access Provider Rules](#configuring-simple-access-provider-rules) {#configuring-simple-access-provider-rules .title}

The `simple`{.literal} access provider restricts system login access based on explicit lists of users or groups. Configure allow or deny rules directly in `sssd.conf`{.literal} to enforce security policies locally without modifying the remote backend directory.

For example, you can use the `simple`{.literal} access provider to restrict access to a specific user or group. Other users or groups will not be allowed to log in even if they authenticate successfully against the configured authentication provider.

**Prerequisites**

-   `root`{.literal} access

**Procedure**

1.  Open the `/etc/sssd/sssd.conf`{.literal} file.

2.  Set the `access_provider`{.literal} option to `simple`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [domain/<domain_name>]
    access_provider = simple
    ```

3.  Define the access control rules for users.

    a.  To allow access to users, use the `simple_allow_users`{.literal} option.
    b.  To deny access to users, use the `simple_deny_users`{.literal} option.

    Important

    If you deny access to specific users, you automatically allow access to everyone else. Allowing access to specific users is considered safer than denying.

4.  Define the access control rules for groups. Choose one of the following:

    a.  To allow access to groups, use the `simple_allow_groups`{.literal} option.

    b.  To deny access to groups, use the `simple_deny_groups`{.literal} option.

        Important

        If you deny access to specific groups, you automatically allow access to everyone else. Allowing access to specific groups is considered safer than denying.

        For example, you can grant access to `alice`{.literal}, `bob`{.literal}, and members of the `engineers`{.literal} group, while denying access to all other users:

        ``` {.language-plaintext tabindex="-1"}
        [domain/<domain_name>]
        access_provider = simple
        simple_allow_users = alice, bob
        simple_allow_groups = engineers
        ```

        Important

        Keeping the deny list empty can lead to allowing access to everyone.

    Note

    If you are adding a trusted AD user to the `simple_allow_users`{.literal} list, ensure that you use the fully qualified domain name (FQDN) format, for example, aduser@ad.example.com. As short names in different domains can be the same, this prevents issues with the access control configuration.

### [6.6. Configuring SSSD to apply an LDAP access filter](#configuring-sssd-to-apply-an-ldap-access-filter) {#configuring-sssd-to-apply-an-ldap-access-filter .title}

LDAP access filters refine authorization by requiring specific attribute matches in the directory entry. SSSD evaluates these filters during login, granting access only if the user object satisfies the defined criteria, such as membership in a specific group.

When the `access_provider`{.literal} option is set in `/etc/sssd/sssd.conf`{.literal}, SSSD uses the specified access provider to evaluate which users are granted access to the system. If the access provider you are using is an extension of the LDAP provider type, you can also specify an LDAP access control filter that a user must match to be allowed access to the system.

For example, when using the Active Directory (AD) server as the access provider, you can restrict access to the Linux system only to specified AD users. All other users that do not match the specified filter have access denied.

Note

The access filter is applied on the LDAP user entry only. Therefore, using this type of access control on nested groups might not work. To apply access control on nested groups, see [Configuring `simple`{.literal} access provider rules](#configuring-simple-access-provider-rules "6.5. Configuring simple Access Provider Rules").

Important

When using offline caching, SSSD checks if the user's most recent online login attempt was successful. Users who logged in successfully during the most recent online login will still be able to log in offline, even if they do not match the access filter.

**Prerequisites**

-   `root`{.literal} access

**Procedure**

1.  Open the `/etc/sssd/sssd.conf`{.literal} file.

2.  In the `[domain]`{.literal} section, specify the access control filter.

    -   For an LDAP, use the `ldap_access_filter`{.literal} option.

    -   For an AD, use the `ad_access_filter`{.literal} option. Additionally, you must disable the GPO-based access control by setting the `ad_gpo_access_control`{.literal} option to `disabled`{.literal}.

        For example, to allow access only to AD users who belong to the `admins`{.literal} user group and have a `unixHomeDirectory`{.literal} attribute set, use:

        ``` {.language-plaintext tabindex="-1"}
        [domain/<ad_domain_name>]
        access provider = ad
        [... file truncated ...]
        ad_access_filter = (&(memberOf=cn=admins,ou=groups,dc=example,dc=com)(unixHomeDirectory=*))
        ad_gpo_access_control = disabled
        ```

        SSSD can also check results by the `authorizedService`{.literal} or `host`{.literal} attribute in an entry. In fact, all options MDASH LDAP filter, `authorizedService`{.literal}, and `host`{.literal} MDASH can be evaluated, depending on the user entry and the configuration. The `ldap_access_order`{.literal} parameter lists all access control methods to use, ordered as how they should be evaluated.

        ``` {.language-plaintext tabindex="-1"}
        [domain/example.com]
        access_provider = ldap
        ldap_access_filter = memberOf=cn=allowedusers,ou=Groups,dc=example,dc=com
        ldap_access_order = filter, host, authorized_service
        ```

## [Chapter 7. SSSD client-side view](#sssd-client-side-view) {#chapter-7.-sssd-client-side-view .title}

The `sss_override`{.literal} utility helps you to create a local view of user data. This tool modifies POSIX attributes on a specific machine without altering the central identity provider, handling conflicts or local requirements effectively.

You can configure overrides for all `id_provider`{.literal} values, except `ipa`{.literal}.

If you are using the `ipa`{.literal} provider, define ID views centrally in IPA.

**Additional resources**

-   [Using an ID view to override a user attribute value on an IdM client](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/using-an-id-view-to-override-a-user-attribute-value-on-an-idm-client)
-   [Potential negative impact of ID views on SSSD performance](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/using-an-id-view-to-override-a-user-attribute-value-on-an-idm-client#potential-negative-impact-of-id-views-on-sssd-performance)

### [7.1. Overriding the LDAP username attribute](#overriding-the-ldap-username-attribute) {#overriding-the-ldap-username-attribute .title}

LDAP user names may conflict with local system policies or naming conventions. Use the `sss_override`{.literal} command to map a remote LDAP user name to a distinct local alias, ensuring compatibility with the specific host.

**Prerequisites**

-   `root`{.literal} access
-   Have `sssd-tools`{.literal} package installed

**Procedure**

1.  Display the current information for the user:

    ``` {.language-plaintext tabindex="-1"}
    # id <ldap_username>
    ```

    Replace *`<ldap_username>`{.literal}* with the LDAP `username`{.literal} of the user. For example:

    ``` {.language-plaintext tabindex="-1"}
    # id sjones
    ```

    ``` {.language-plaintext tabindex="-1"}
    uid=1001(sjones) gid=6003 groups=6003,10(wheel)
    ```

2.  Add the local username:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-add <ldap_username> -n <local_username>
    ```

    Replace *`<ldap_username>`{.literal}* with the LDAP `username`{.literal} and replace *`<local_username>`{.literal}* with the desired local username. For example:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-add sjones -n sarah
    ```

3.  After creating the first override using the `sss_override user-add`{.literal} command, restart SSSD for the changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

**Verification**

-   Verify that the local username is added:

    ``` {.language-plaintext tabindex="-1"}
    # id <local_username>
    ```

    For example:

    ``` {.language-plaintext tabindex="-1"}
    # id sarah
    ```

    ``` {.language-plaintext tabindex="-1"}
    uid=1001(sjones) gid=6003(sjones) groups=6003(sjones),10(wheel)
    ```

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-show sjones
    user@ldap.example.com:sarah::::::
    ```

-   Optional: Display the overrides for the user:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-show <ldap_username>
    ```

    ``` {.language-plaintext tabindex="-1"}
    user@ldap.example.com:_<local_username>_::::::
    ```

### [7.2. Overriding the LDAP UID attribute](#overriding-the-ldap-uid-attribute) {#overriding-the-ldap-uid-attribute .title}

Conflicting numeric identifiers can cause file permission errors. You can override the unique identifier (UID) provided by LDAP with a specific local value using `sss_override`{.literal}, ensuring the user matches local file ownership requirements.

**Prerequisites**

-   `root`{.literal} access
-   Have `sssd-tools`{.literal} package installed

**Procedure**

1.  Display the current UID of the user:

    ``` {.language-plaintext tabindex="-1"}
    # id -u <ldap_username>
    ```

    Replace *`<ldap_username>`{.literal}* with the LDAP `username`{.literal} of the user. For example:

    ``` {.language-plaintext tabindex="-1"}
    # id -u sarah
    ```

    ``` {.language-plaintext tabindex="-1"}
    1001
    ```

2.  Override the UID of the user's account:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-add <ldap_username> -u <local_uid>
    ```

    Replace *`<ldap_username>`{.literal}* with the LDAP `username`{.literal} of the user and replace *`<local_uid>`{.literal}* with the new UID number. For example:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-add sarah -u 6666
    ```

3.  Expire the in-memory cache:

    ``` {.language-plaintext tabindex="-1"}
    # sss_cache --users
    ```

4.  After creating the first override using the `sss_override user-add`{.literal} command, restart SSSD for the changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

**Verification**

-   Verify that the local UID has been applied:

    ``` {.language-plaintext tabindex="-1"}
    # id -u <ldap_username>
    ```

-   Optional: Display the overrides for the user:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-show <ldap_username>
    ```

    ``` {.language-plaintext tabindex="-1"}
    user@ldap.example.com::_<local_uid>_:::::
    ```

### [7.3. Overriding the LDAP GID attribute](#overriding-the-ldap-gid-attribute) {#overriding-the-ldap-gid-attribute .title}

You can change the group identifier (GID) for an LDAP user on the local system. This action ensures the user's primary group matches specific local requirements, facilitating correct file access and group membership.

**Prerequisites**

-   `root`{.literal} access
-   Installed `sssd-tools`{.literal}

**Procedure**

1.  Display the current GID of the user:

    ``` {.language-plaintext tabindex="-1"}
    # id -g <ldap_username>
    ```

    Replace *`<ldap_username>`{.literal}* with the name of the user. For example:

    ``` {.language-plaintext tabindex="-1"}
    # id -g sarah
    ```

    ``` {.language-plaintext tabindex="-1"}
    6003
    ```

2.  Override the GID of the user's account:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-add <ldap_username> -g <local_gid>
    ```

    Replace *`<ldap_username>`{.literal}* with the name of the user and replace *`<local_gid>`{.literal}* with the local GID number. For example:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-add sarah -g 6666
    ```

3.  Expire the in-memory cache:

    ``` {.language-plaintext tabindex="-1"}
    # sss_cache --users
    ```

4.  After creating the first override using the `sss_override user-add`{.literal} command, restart SSSD for the changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

**Verification**

-   Verify that the local GID is applied:

    ``` {.language-plaintext tabindex="-1"}
    # id -g <ldap_username>
    ```

-   Optional: Display the overrides for the user:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-show <ldap_username>
    ```

    ``` {.language-plaintext tabindex="-1"}
    user@ldap.example.com::: 6666::::
    ```

### [7.4. Overriding the LDAP home directory attribute](#overriding-the-ldap-home-directory-attribute) {#overriding-the-ldap-home-directory-attribute .title}

Remote home directory paths often do not exist on every client machine. Overriding this attribute helps you to map users to a valid local path, ensuring they land in an existing directory upon login.

**Prerequisites**

-   `root`{.literal} access
-   Installed `sssd-tools`{.literal}

**Procedure**

1.  Display the current home directory of the user as stored locally:

    ``` {.language-plaintext tabindex="-1"}
    # getent passwd <ldap_username>
    ```

    ``` {.language-plaintext tabindex="-1"}
    <ldap_username>:x:XXXX:XXXX::/home/<home_directory>:/bin/bash
    ```

    Replace *`<ldap_username>`{.literal}* with the name of the user. The output shows the home directory value as seen locally, which might be different from the LDAP record. For example:

    ``` {.language-plaintext tabindex="-1"}
    # getent passwd sarah
    ```

    ``` {.language-plaintext tabindex="-1"}
    sarah:x:1001:6003::sarah:/bin/bash
    ```

2.  Override the home directory of the user:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-add <ldap_username> -h <new_home_directory>
    ```

    Replace *`<ldap_username>`{.literal}* with the name of the user and replace `<new_home_directory>`{.literal} with the new home directory. For example:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-add sarah -h admin
    ```

3.  Restart SSSD for the changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

**Verification**

-   Verify that the new home directory is defined:

    ``` {.language-plaintext tabindex="-1"}
    # getent passwd <ldap_username>
    ```

    ``` {.language-plaintext tabindex="-1"}
    <ldap_username>:x:XXXX:XXXX::/home/<new_home_directory>:/bin/bash
    ```

-   Optional: Display the overrides for the user:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-show <ldap_username>
    ```

    ``` {.language-plaintext tabindex="-1"}
    user@ldap.example.com:::::::<new_home_directory>::
    ```

### [7.5. Overriding the LDAP shell attribute](#overriding-the-ldap-shell-attribute) {#overriding-the-ldap-shell-attribute .title}

The default shell assigned in LDAP may be restricted or unavailable on specific clients. You can override this attribute to assign a valid local shell, such as `/bin/bash`{.literal} or `/sbin/nologin`{.literal}, appropriate for the host's specific purpose.

**Prerequisites**

-   `root`{.literal} access
-   Installed `sssd-tools`{.literal}

**Procedure**

1.  Display the current shell of the user as stored locally:

    ``` {.language-plaintext tabindex="-1"}
    # getent passwd <ldap_username>
    ```

    ``` {.language-plaintext tabindex="-1"}
    <ldap_username>:x:XXXX:XXXX::/home/<home_directory>:_<currentshell>_
    ```

    Replace *`<ldap_username>`{.literal}* with the name of the user.

2.  Override the shell of the user:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-add <ldap_username> -s <new_shell>
    ```

    Replace *`<ldap_username>`{.literal}* with the name of the user and replace *`<new_shell>`{.literal}* with the new shell.

3.  Restart SSSD for the changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

**Verification**

-   Verify that the new shell is defined:

    ``` {.language-plaintext tabindex="-1"}
    # getent passwd <ldap_username>
    ```

    ``` {.language-plaintext tabindex="-1"}
    <ldap_username>:x:XXXX:XXXX::/home/<home_directory>:_<new_shell>_
    ```

-   Optional: Display the overrides for the user:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-show <ldap_username>
    ```

    ``` {.language-plaintext tabindex="-1"}
    user@ldap.example.com::::::_<new_shell>_:
    ```

    For example, to change the shell of the user `sarah`{.literal} from `/bin/bash`{.literal} to `sbin/nologin`{.literal}:

    1.  Display the current shell of the user `sarah`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # getent passwd sarah
        ```

        ``` {.language-plaintext tabindex="-1"}
        sarah:x:1001:6003::sarah:/bin/bash
        ```

    2.  Override the shell of the user sarah with new `/sbin/nologin`{.literal} shell:

        ``` {.language-plaintext tabindex="-1"}
        # sss_override user-add sarah -s /sbin/nologin
        ```

    3.  Restart SSSD for the changes to take effect:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart sssd
        ```

    4.  Verify that the new shell is defined and overrides for the user display correctly:

        ``` {.language-plaintext tabindex="-1"}
        # getent passwd sarah
        ```

        ``` {.language-plaintext tabindex="-1"}
        sarah:x:1001:6003::sarah:/sbin/nologin
        ```

        ``` {.language-plaintext tabindex="-1"}
        # sss_override user-show sarah
        ```

        ``` {.language-plaintext tabindex="-1"}
        user@ldap.example.com::::::/sbin/nologin:
        ```

### [7.6. Listing overrides on a host](#listing-overrides-on-a-host) {#listing-overrides-on-a-host .title}

You must audit local modifications to ensure configuration consistency. The `sss_override`{.literal} tool provides search functions to list all currently active user and group overrides stored in the local cache.

**Prerequisites**

-   `root`{.literal} access
-   Installed `sssd-tools`{.literal}

**Procedure**

-   List all user overrides:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-find
    ```

    ``` {.language-plaintext tabindex="-1"}
    user1@ldap.example.com::8000::::/bin/zsh:
    user2@ldap.example.com::8001::::/bin/bash:
    ...
    ```

-   List all group overrides:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override group-find
    ```

    ``` {.language-plaintext tabindex="-1"}
    group1@ldap.example.com::7000
    group2@ldap.example.com::7001
    ...
    ```

### [7.7. Removing a local override](#removing-a-local-override) {#removing-a-local-override .title}

Removing an override reverts the user or group attributes to the values provided by the central directory. Use deletion commands to clean up obsolete configurations or restore default identity data immediately.

**Prerequisites**

-   `root`{.literal} access
-   Installed `sssd-tools`{.literal}

**Procedure**

-   To remove the override for a user account, use:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-del <local_username>
    ```

    Replace *\<local_username\>* with the name of the user. The changes take effect immediately.

-   To remove an override for a group, use:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override group-del <group_name>
    ```

-   After removing the first override using the `sss_override user-del`{.literal} or `sss_override group-del`{.literal} command, restart SSSD for the changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

    When you remove overrides for a user or group, all overrides for this object are removed.

### [7.8. Exporting and importing local view](#exporting-and-importing-local-view) {#exporting-and-importing-local-view .title}

Local overrides reside in the SSSD cache and risk deletion during cache clearing. Exporting these configurations to a backup file helps you to restore custom views quickly after system maintenance or migrations.

**Prerequisites**

-   `root`{.literal} access
-   Installed `sssd-tools`{.literal}

**Procedure**

-   To back up user and group view, use:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-export /var/lib/sss/backup/sssd_user_overrides.bak
    # sss_override group-export /var/lib/sss/backup/sssd_group_overrides.bak
    ```

-   To restore user and group view, use:

    ``` {.language-plaintext tabindex="-1"}
    # sss_override user-import /var/lib/sss/backup/sssd_user_overrides.bak
    # sss_override group-import /var/lib/sss/backup/sssd_group_overrides.bak
    ```

## [Chapter 8. Configuring a RHEL host to use AD as an authentication provider](#configuring-a-rhel-host-to-use-ad-as-an-authentication-provider) {#chapter-8.-configuring-a-rhel-host-to-use-ad-as-an-authentication-provider .title}

Configure Red Hat Enterprise Linux (RHEL) to authenticate against Active Directory (AD) without a domain join. This method utilizes SSSD proxies and Kerberos to verify credentials, allowing centralized authentication while preserving local administrative control.

Use this approach if:

-   You do not want AD administrators to have control over enabling and disabling the host.
-   The host, which can be a corporate PC, is only meant to be used by one user in your company.

Important

Use this approach only if you have a specific reason to avoid joining your host to AD.

Consider fully joining the system to AD or Identity Management (IdM) instead. Joining the RHEL host to a domain makes the setup easier to manage. If you are concerned about client access licences related to joining clients into AD directly, consider leveraging an IdM server that is in a trust agreement with AD. For more information about an IdM-AD trust, see [Planning a cross-forest trust between IdM and AD](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/planning-a-cross-forest-trust-between-idm-and-ad) and

[Installing a trust between IdM and AD](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_trust_between_idm_and_ad/index).

After you complete this procedure, **AD_user** can log in to **rhel_host** system using their the password set in the AD user database in the **example.com** domain. The **EXAMPLE.COM** Kerberos realm corresponds to the **example.com** domain.

**Prerequisites**

-   You have root access to **rhel_host**.

-   The **AD_user** user account exists in the **example.com** domain.

-   The Kerberos realm is **EXAMPLE.COM**.

-   **rhel_host** has not been joined to AD using the `realm join`{.literal} command.

-   You have installed the `sssd-proxy`{.literal} package.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install sssd-proxy
    ```

**Procedure**

1.  Create the **AD_user** user account locally without assigning a password to it:

    ``` {.language-plaintext tabindex="-1"}
    # useradd AD_user
    ```

2.  Open the `/etc/nsswitch.conf`{.literal} file for editing, and make sure that it contains the following lines:

    ``` {.language-plaintext tabindex="-1"}
    passwd:     sss files systemd
    group:      sss files systemd
    shadow:     files sss
    ```

3.  Open the `/etc/krb5.conf`{.literal} file for editing, and make sure that it contains the following sections and items:

    ``` {.language-plaintext tabindex="-1"}
    # To opt out of the system crypto-policies configuration of krb5, remove the
    # symlink at /etc/krb5.conf.d/crypto-policies which will not be recreated.
    includedir /etc/krb5.conf.d/

    [logging]
        default = FILE:/var/log/krb5libs.log
        kdc = FILE:/var/log/krb5kdc.log
        admin_server = FILE:/var/log/kadmind.log

    [libdefaults]
        dns_lookup_realm = false
        ticket_lifetime = 24h
        renew_lifetime = 7d
        forwardable = true
        rdns = false
        pkinit_anchors = /etc/pki/tls/certs/ca-bundle.crt
        spake_preauth_groups = edwards25519
        default_realm = EXAMPLE.COM
        default_ccache_name = KEYRING:persistent:%{uid}

    [realms]
     EXAMPLE.COM = {
         kdc = ad.example.com
         admin_server = ad.example.com
     }

    [domain_realm]
     .example.com = EXAMPLE.COM
     example.com = EXAMPLE.COM
    ```

4.  Create the `/etc/sssd/sssd.conf`{.literal} file and insert the following sections and lines into it:

    ``` {.language-plaintext tabindex="-1"}
    [sssd]
        services = nss, pam
        domains = EXAMPLE.COM

    [domain/EXAMPLE.COM]
        id_provider = proxy
        proxy_lib_name = files
        auth_provider = krb5
        krb5_realm = EXAMPLE.COM
        krb5_server = ad.example.com
    ```

5.  Change the permissions on the `/etc/sssd/sssd.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # chmod 600 /etc/sssd/sssd.conf
    ```

6.  Start the Security System Services Daemon (SSSD):

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start sssd
    ```

7.  Enable SSSD:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable sssd
    ```

8.  Open the `/etc/pam.d/system-auth`{.literal} file, and modify it so that it contains the following sections and lines:

    ``` {.language-plaintext tabindex="-1"}
    # Generated by authselect on Wed May  8 08:55:04 2019
    # Do not modify this file manually.

    auth        required                                     pam_env.so
    auth        required                                     pam_faildelay.so delay=2000000
    auth        [default=1 ignore=ignore success=ok]         pam_succeed_if.so uid >= 1000 quiet
    auth        [default=1 ignore=ignore success=ok]         pam_localuser.so
    auth        sufficient                                   pam_unix.so nullok try_first_pass
    auth        requisite                                    pam_succeed_if.so uid >= 1000 quiet_success
    auth        sufficient                                   pam_sss.so forward_pass
    auth        required                                     pam_deny.so

    account     required                                     pam_unix.so
    account     sufficient                                   pam_localuser.so
    account     sufficient                                   pam_succeed_if.so uid < 1000 quiet
    account     [default=bad success=ok user_unknown=ignore] pam_sss.so
    account     required                                     pam_permit.so

    password    requisite                                    pam_pwquality.so try_first_pass local_users_only
    password    sufficient                                   pam_unix.so sha512 shadow nullok try_first_pass use_authtok
    password    sufficient                                   pam_sss.so use_authtok
    password    required                                     pam_deny.so

    session     optional                                     pam_keyinit.so revoke
    session     required                                     pam_limits.so
    -session    optional                                     pam_systemd.so
    session     [success=1 default=ignore]                   pam_succeed_if.so service in crond quiet use_uid
    session     required                                     pam_unix.so
    session     optional                                     pam_sss.so
    ```

9.  Copy the contents of the `/etc/pam.d/system-auth`{.literal} file into the `/etc/pam.d/password-auth`{.literal} file. Enter **yes** to confirm the overwriting of the current contents of the file:

    ``` {.language-plaintext tabindex="-1"}
    # cp /etc/pam.d/system-auth /etc/pam.d/password-auth
    ```

    ``` {.language-plaintext tabindex="-1"}
    cp: overwrite '/etc/pam.d/password-auth'? yes
    ```

**Verification**

1.  Request a Kerberos ticket-granting ticket (TGT) for **AD_user**. Enter the password of **AD_user** as requested:

    ``` {.language-plaintext tabindex="-1"}
    # kinit AD_user
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password for AD_user@EXAMPLE.COM:
    ```

2.  Display the obtained TGT:

    ``` {.language-plaintext tabindex="-1"}
    # klist
    ```

    ``` {.language-plaintext tabindex="-1"}
    Ticket cache: KEYRING:persistent:0:0
    Default principal: AD_user@EXAMPLE.COM

    Valid starting     Expires            Service principal
    11/02/20 04:16:38  11/02/20 14:16:38  krbtgt/EXAMPLE.COM@EXAMPLE.COM
        renew until 18/02/20 04:16:34
    ```

**AD_user** has successfully logged in to **rhel_host** using the credentials from the **EXAMPLE.COM** Kerberos domain.

## [Chapter 9. Reporting on user access on hosts using SSSD](#reporting-on-user-access-on-hosts-using-sssd) {#chapter-9.-reporting-on-user-access-on-hosts-using-sssd .title}

The Security System Services Daemon (SSSD) tracks user access rights across network clients. Use the `sssctl`{.literal} command-line tool to generate detailed access control reports and audit user data for security compliance.

### [9.1. Prerequisites](#prerequisites_2) {#prerequisites-1 .title}

-   SSSD packages are installed in your network environment

### [9.2. The sssctl command](#the-sssctl-command) {#the-sssctl-command .title}

The `sssctl`{.literal} utility provides a unified interface for monitoring the Security System Services Daemon (SSSD) status. Use this tool to manage caches, review logs, and audit domain states or user authentication access.

You can use the `sssctl`{.literal} utility to gather information about:

-   Domain state
-   Client user authentication
-   User access on clients of a particular domain
-   Information about cached content

With the `sssctl`{.literal} tool, you can:

-   Manage the SSSD cache
-   Manage logs
-   Check configuration files

Note

The `sssctl`{.literal} tool replaces `sss_cache`{.literal} and `sss_debuglevel`{.literal} tools.

### [9.3. Generating access control reports using sssctl](#generating-access-control-reports-using-sssctl) {#generating-access-control-reports-using-sssctl .title}

The Security System Services Daemon (SSSD) enforces login permissions on the local machine. Generating an access control report lists the specific rules currently applied to the host, helping you to verify active security policies.

Note

The access report is not accurate because the tool does not track users locked out by the Key Distribution Center (KDC).

**Prerequisites**

-   You must be logged in with administrator privileges.

**Procedure**

-   To generate an access control report, run the following command, replacing *`<domain_name>`{.literal}*:

    ``` {.language-plaintext tabindex="-1"}
    [root@client1 ~]# sssctl access-report <domain_name>
    ```

    ``` {.language-plaintext tabindex="-1"}
    1 rule cached

    Rule name: example.user
        Member users: example.user
        Member services: sshd
    ```

### [9.4. Displaying user authorization details using sssctl](#displaying-user-authorization-details-using-sssctl) {#displaying-user-authorization-details-using-sssctl .title}

The `sssctl user-checks`{.literal} command validates specific user permissions against PAM services. Run this diagnostic tool to troubleshoot login failures and view data from the Name Service Switch (NSS) or InfoPipe responder.

Run `sssctl user-checks `{.literal}*`<user_name>`{.literal}* to display user data available from Name Service Switch (NSS) and the InfoPipe responder for the D-Bus interface. The output shows whether the user is authorized to log in using the `system-auth`{.literal} Pluggable Authentication Module (PAM) service.

The command has two options:

-   `-a`{.literal} for a PAM action
-   `-s`{.literal} for a PAM service

If you do not specify `-a`{.literal} and `-s`{.literal} options, the `sssctl`{.literal} tool uses default options: `-a acct -s system-auth`{.literal}.

**Prerequisites**

-   You must be logged in with administrator privileges.

**Procedure**

-   To display user data for a particular user, enter:

    ``` {.language-plaintext tabindex="-1"}
    [root@client1 ~]# sssctl user-checks -a acct -s sshd <user_name>
    ```

    ``` {.language-plaintext tabindex="-1"}
    user: example.user
    action: acct
    service: sshd
    ...
    ```

## [Chapter 10. Querying domain information using SSSD](#querying-domain-information-using-sssd) {#chapter-10.-querying-domain-information-using-sssd .title}

The `sssctl`{.literal} utility retrieves domain data from the System Security Services Daemon (SSSD), covering Identity Management and trusted Active Directory realms. Use this tool to audit available domains and verify connection status for troubleshooting.

### [10.1. Listing domains using sssctl](#listing-domains-using-sssctl) {#listing-domains-using-sssctl .title}

The `sssctl domain-list`{.literal} command outputs all detected identity domains, including local files and trusted external directories. This list helps you to verify the domain topology and ensure complete visibility of identity sources.

Note

The status might not be available immediately. If the domain is not visible, repeat the command.

**Prerequisites**

-   You must be logged in with administrator privileges.

**Procedure**

1.  Optional: To display help for the `sssctl`{.literal} command, enter:

    ``` {.language-plaintext tabindex="-1"}
    [user@client1 ~]$ sssctl --help
    ...
    ```

2.  To display a list of available domains, enter:

    ``` {.language-plaintext tabindex="-1"}
    [root@client1 ~]# sssctl domain-list
    ```

    ``` {.language-plaintext tabindex="-1"}
    implicit_files
    idm.example.com
    ad.example.com
    sub1.ad.example.com
    ```

    The list includes domains in the cross-forest trust between Active Directory and Identity Management.

### [10.2. Verifying the domain status using sssctl](#verifying-the-domain-status-using-sssctl) {#verifying-the-domain-status-using-sssctl .title}

The `sssctl domain-status`{.literal} command checks the real-time connectivity of a specific domain. This utility confirms server reachability and online status, assisting you in diagnosing network or configuration failures.

Note

The status might not be available immediately. If the domain is not visible, repeat the command.

**Prerequisites**

-   You must be logged in with administrator privileges.

**Procedure**

1.  Optional: To display help for the `sssctl`{.literal} command, enter:

    ``` {.language-plaintext tabindex="-1"}
    [user@client1 ~]$ sssctl --help
    ```

2.  To display user data for a particular domain, replace *`<domain_name>`{.literal}* with the actual domain name and enter:

    ``` {.language-plaintext tabindex="-1"}
    [root@client1 ~]# sssctl domain-status <domain_name>
    ```

    Example output for the domain idm.example.com

    ``` {.language-plaintext tabindex="-1"}
    Online status: Online

    Active servers:
    IPA: server.idm.example.com

    Discovered IPA servers:
    - server.idm.example.com
    ```

    The domain `idm.example.com`{.literal} is online and visible from the client where you applied the command.

    If the domain is not available, the result is:

    ``` {.language-plaintext tabindex="-1"}
    [root@client1 ~]# sssctl domain-status <domain_name>
    ```

    ``` {.language-plaintext tabindex="-1"}
    Unable to get online status
    ```

## [Chapter 11. Restricting domains for PAM services using SSSD](#restricting-domains-for-pam-services-using-sssd) {#chapter-11.-restricting-domains-for-pam-services-using-sssd .title}

The System Security Services Daemon (SSSD) restricts Pluggable Authentication Modules (PAMs) service access to specific identity domains based on the user running the service. With this evaluation mechanism, you can enforce granular control, ensuring services only interact with authorized identity providers.

### [11.1. Introduction to PAM](#introduction-to-pam) {#introduction-to-pam .title}

Pluggable Authentication Modules (PAM) provide a modular framework for system authentication. Applications offload identity verification to centrally configured PAM stacks, helping you to implement flexible policies involving Kerberos, SSSD, or local files.

PAM is pluggable because a PAM module exists for different types of authentication sources, such as Kerberos, SSSD, NIS, or the local file system. You can prioritize different authentication sources.

This modular architecture offers administrators a great deal of flexibility in setting authentication policies for the system. PAM is a useful system for developers and administrators for several reasons:

-   PAM provides a common authentication scheme, which can be used with a wide variety of applications.
-   PAM provides significant flexibility and control over authentication for system administrators.
-   PAM provides a single, fully-documented library, which allows developers to write programs without having to create their own authentication schemes.

#### [11.1.1. PAM configuration file format](#pam-configuration-file-format) {#pam-configuration-file-format .title}

Pluggable Authentication Module (PAM) configuration files consist of directives that control module behavior. Each line specifies the interface type, a control flag, the module library name, and optional arguments, instructing the system on how to process specific authentication tasks.

``` {.language-plaintext tabindex="-1"}
module_type  control_flag    <module_name> <module_arguments>
```

For example:

``` {.language-plaintext tabindex="-1"}
auth required    pam_unix.so
```

##### [11.1.1.1. PAM module types](#pam_module_types) {#pam-module-types .title}

PAM defines four interface types: account, authentication, password, and session. These categories determine the specific task a module performs, such as verifying credentials, setting up the user environment, or enforcing password complexity policies.

An individual module can provide any or all types of authentication tasks. For example, `pam_unix.so`{.literal} provides all four authentication tasks.

The module name, such as `pam_unix.so`{.literal}, provides PAM with the name of the library containing the specified module type. The directory name is omitted because the application is linked to the appropriate version of `libpam`{.literal}, which can locate the correct version of the module.

Module type directives can be stacked, or placed upon one another, so that multiple modules are used together for one purpose. The order of the modules is important, along with the control flags, it determines how significant the success or failure of a particular module is to the overall goal of authenticating the user to the service.

You can stack PAM modules to enforce specific conditions that must be met before a user is allowed to authenticate.

##### [11.1.1.2. PAM control flags](#pam_control_flags) {#pam-control-flags .title}

Control flags dictate how PAM handles module results. Keywords like required, requisite, and sufficient determine whether the authentication stack continues processing or immediately returns a success or failure status to the application.

Simple flags use a keyword, more complex syntax follows `[`{.literal}*`<value1>`{.literal}*`=`{.literal}*`<action1>`{.literal}*` `{.literal}*`<value2>`{.literal}*`=`{.literal}*`<action2>`{.literal}*` …​]`{.literal} format.

Note

When a module's control flag uses the `sufficient`{.literal} or `requisite`{.literal} value, the order in which the modules are listed is important to the authentication process.

For a detailed description of PAM control flags, including a list of options, see the `pam.conf(5)`{.literal} man page.

### [11.2. Domain-access restriction options](#domain-access-restriction-options) {#domain-access-restriction-options .title}

Manage control domain access by using `pam_trusted_users`{.literal} and `pam_public_domains`{.literal} in `sssd.conf`{.literal}. Additionally, the domains option in PAM configuration files limits specific services to a defined list of authentication providers.

To restrict access to selected domains, you can use the following options:

pam_trusted_users in /etc/sssd/sssd.conf
:   Lists numerical UIDs or user names for PAM services that SSSD trusts. The default setting is `all`{.literal}, which means all service users are trusted and can access any domain.

pam_public_domains in /etc/sssd/sssd.conf
:   Specifies public SSSD domains that are accessible by untrusted PAM service users. The option accepts the `all`{.literal} and `none`{.literal} values. The default value is `none`{.literal}, which means no domains are public and untrusted service users cannot access any domain.

domains for PAM configuration files

:   Specifies a list of domains against which a PAM service can authenticate. If you use `domains`{.literal} without specifying any domain, the PAM service cannot authenticate against any domain, for example:

    ``` {.language-plaintext tabindex="-1"}
    auth     required   pam_sss.so domains=
    ```

    If the PAM configuration file uses `domains`{.literal}, the PAM service is able to authenticate against all domains when that service is running under a trusted user.

    The `domains`{.literal} option in the `/etc/sssd/sssd.conf`{.literal} SSSD configuration file also specifies a list of domains to which SSSD attempts to authenticate. Note that the `domains`{.literal} option in a PAM configuration file cannot extend the list of domains in `sssd.conf`{.literal}, it can only restrict the `sssd.conf`{.literal} list of domains by specifying a shorter list. Therefore, if a domain is specified in the PAM file but not in `sssd.conf`{.literal}, the PAM service cannot authenticate against the domain.

The default settings `pam_trusted_users = all`{.literal} and `pam_public_domains = none`{.literal} specify that all PAM service users are trusted and can access any domain. Use the `domains`{.literal} option in PAM configuration files to restrict domain access.

Specifying a domain using `domains`{.literal} in the PAM configuration file while `sssd.conf`{.literal} contains `pam_public_domains`{.literal} also requires to specify the domain in `pam_public_domains`{.literal}. The `pam_public_domains`{.literal} option without including the required domain leads the PAM service to unsuccessful authentication against the domain in case this service is running under an untrusted user.

Note

Domain restrictions defined in a PAM configuration file apply to authentication actions only, not to user lookups.

### [11.3. Restricting domains for a PAM service](#restricting-domains-for-a-pam-service) {#restricting-domains-for-a-pam-service .title}

You can lock specific PAM services to a subset of available SSSD domains. This configuration forces the service to authenticate only against the specified providers, isolating critical applications from other identity sources.

**Prerequisites**

-   SSSD installed and running.

**Procedure**

1.  Configure SSSD to access the required domain or domains. Define the domains against which SSSD can authenticate in the `domains`{.literal} option in the `/etc/sssd/sssd.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    [sssd]
    domains = <idm.example.com>, <ad.example.com>, <ldap.example.com>
    ```

2.  Specify the domain or domains to which a PAM service can authenticate by setting the\`domains\` option in the PAM configuration file. For example:

    ``` {.language-plaintext tabindex="-1"}
    auth        sufficient    pam_sss.so forward_pass domains=<idm.example.com>
    account     [default=bad success=ok user_unknown=ignore] pam_sss.so
    password    sufficient    pam_sss.so use_authtok
    ```

    This configuration restricts the PAM service to authenticate against *`<idm.example.com>`{.literal}* only.

**Verification**

-   Authenticate against *`<idm.example.com>`{.literal}*. It must be successful.

### [11.4. About PAM configuration files](#about-pam-configuration-files) {#about-pam-configuration-files .title}

PAM configuration files in `/etc/pam.d/`{.literal} define policies for individual applications. Each file stacks specific modules to enforce security requirements, such as password quality checks or root access limits, for the service it controls.

For example, the `login`{.literal} program has a corresponding PAM configuration file named `/etc/pam.d/login`{.literal}.

Warning

Manual editing of PAM configuration files might lead to authentication and access issues. Configure PAMs using the `authselect`{.literal} tool.

See an example of PAM configuration file with the detailed description.

**Annotated PAM configuration example**

``` {.language-plaintext tabindex="-1"}
#%PAM-1.0
auth        required    pam_securetty.so
auth        required    pam_unix.so nullok
auth        required    pam_nologin.so
account     required    pam_unix.so
password    required    pam_pwquality.so retry=3
password    required    pam_unix.so shadow nullok use_authtok
session     required    pam_unix.so
```

where:

`auth required pam_securetty.so`{.literal}
:   Ensures that the root login is allowed only from a terminal which is listed in the `/etc/securetty`{.literal} file, if this file exists. If the terminal is not listed in the file, the login as root fails with a `Login incorrect`{.literal} message.

`auth required pam_unix.so nullok`{.literal}
:   Prompts the user for a password and checks it against the information stored in `/etc/passwd`{.literal} and, if it exists, `/etc/shadow`{.literal}. The `nullok`{.literal} argument allows a blank password.

`auth required pam_nologin.so`{.literal}

:   Checks if `/etc/nologin`{.literal} file exists. If it exists, and the user is not root, authentication fails.

    Note

    In this example, all three `auth`{.literal} modules are checked, even if the first `auth`{.literal} module fails. This is a good security approach that prevents potential attacker from knowing at what stage their authentication failed.

`account required pam_unix.so`{.literal}
:   Verifies the user's account. For example, if shadow passwords have been enabled, the account type of the `pam_unix.so`{.literal} module checks for expired accounts or if the user needs to change the password.

`password required pam_pwquality.so retry=3`{.literal}
:   Prompts for a new password if the current one has expired or when the user manually requests a password change. Then it checks the strength of the newly created password to ensure it meets quality requirements and is not easily determined by a dictionary-based password cracking program. The argument `retry=3`{.literal} specifies that user has three attempts to create a strong password.

`password required pam_unix.so shadow nullok use_authtok`{.literal}
:   The `pam_unix.so`{.literal} module manages password changes. The `shadow`{.literal} argument instructs the module to create shadow passwords when updating a user's password. The `nullok`{.literal} argument allows the user to change their password from a blank password, otherwise a null password is treated as an account lock. The `use_authtok`{.literal} argument accepts any password that was entered previously without prompting the user again. In this way, all new passwords must pass the `pam_pwquality.so`{.literal} check for secure passwords before being accepted.

`session required pam_unix.so`{.literal}
:   The `pam_unix.so`{.literal} module manages the session and logs the user name and service type at the beginning and end of each session. Logs are collected by the `systemd-journald`{.literal} service and can be viewed by using the `journalctl`{.literal} command. Logs are also stored in `/var/log/secure`{.literal}. This module can be supplemented by stacking it with other session modules for additional functionality.

## [Chapter 12. Centralizing SSH authentication with IdM](#centralizing-ssh-authentication-with-idm) {#chapter-12.-centralizing-ssh-authentication-with-idm .title}

Manually managing `authorized_keys`{.literal} and `known_hosts`{.literal} files across a large infrastructure introduces security risks and administrative overhead. By integrating the System Security Services Daemon (SSSD) with OpenSSH, you can centralize public key storage within Identity Management (IdM).

In this configuration:

-   The IdM LDAP directory serves as the single source of truth for user and host public keys.
-   SSSD fetches these keys and caches them locally for performance and offline availability.
-   OpenSSH queries SSSD instead of looking for local flat files on the file system.

### [12.1. Configuring OpenSSH to use SSSD for host keys](#configuring-openssh-to-use-sssd-for-host-keys) {#configuring-openssh-to-use-sssd-for-host-keys .title}

By configuring OpenSSH to use SSSD for host keys, you centralize the known hosts list within Identity Management (IdM). This allows every machine in your infrastructure to automatically recognize and trust every other machine in the domain.

**Prerequisites**

-   The system is enrolled in an IdM domain.
-   You have `sudo`{.literal} privileges.

**Procedure**

1.  Open the SSH configuration file. You can change the configuration on a per-user basis or for the whole system. Open the required configuration file.

    -   To change user-specific configuration, open the `~/.ssh/config`{.literal} file.
    -   To change system-wide configuration, open the `/etc/ssh/ssh_config`{.literal} file.

2.  Configure the SSH client to fetch keys from SSSD by adding the following lines to the file:

    ``` {.language-plaintext tabindex="-1"}
    KnownHostsCommand /usr/bin/sss_ssh_knownhosts %H
    ```

    The `%H`{.literal} token automatically passes the destination hostname to SSSD.

3.  Ensure that the SSSD SSH responder is active. Open the `/etc/sssd/sssd.conf`{.literal} file and verify that `ssh`{.literal} is included in the services list:

    ``` {.language-plaintext tabindex="-1"}
    [sssd]
    services = nss, pam, ssh
    ```

4.  Save and close the file.

5.  Restart SSSD for the changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

**Verification**

-   To confirm SSSD is serving the host key, run the following command:

    ``` {.language-plaintext tabindex="-1"}
    sss_ssh_knownhosts <hostname>
    ```

    ``` {.language-plaintext tabindex="-1"}
    Success: The command returns the host's public key string.
    ```

-   Attempt to connect to another host within the IdM domain:

    ``` {.language-plaintext tabindex="-1"}
    ssh user@remote-idm-host.example.com
    ```

    The client validates the host key via SSSD, allowing you to connect without a manual fingerprint prompt.

    Note

    The host you are connecting to must not be in the local `known_hosts`{.literal} file to ensure the test is executed correctly and is valid.

    For more information, see the `sss_ssh_knownhosts(1)`{.literal} and `ssh_config(5)`{.literal} man pages.

### [12.2. Configuring OpenSSH to use SSSD for user keys](#configuring-openssh-to-use-sssd-for-user-keys) {#configuring-openssh-to-use-sssd-for-user-keys .title}

By configuring OpenSSH to use SSSD for user keys, you move public key management into the IdM directory. This allows users to log in to any enrolled system in the infrastructure using their centralized credentials. The aim is to treat SSH keys as identity attributes rather than local files, ensuring that when you update a key in IdM, the change propagates instantly across the entire environment.

**Prerequisites**

-   User public keys are uploaded to the IdM server by using either the IdM Web UI or the `ipa user-mod --sshpubkey`{.literal} command.
-   The `sssd-dbus`{.literal} package is installed.

**Procedure**

1.  Open the SSH daemon configuration file:

    ``` {.language-plaintext tabindex="-1"}
    vi /etc/ssh/sshd_config
    ```

2.  Add the following lines to instruct the daemon to fetch keys from SSSD:

    ``` {.language-plaintext tabindex="-1"}
    AuthorizedKeysCommand /usr/bin/sss_ssh_authorizedkeys
    AuthorizedKeysCommandUser nobody
    ```

3.  Ensure that the SSSD SSH responder is active. Open the `/etc/sssd/sssd.conf`{.literal} file and verify that `ssh`{.literal} is included in the services list:

    ``` {.language-plaintext tabindex="-1"}
    [sssd]
    services = nss, pam, ssh
    ```

4.  Optional: If you changed the SSSD configuration, restart SSSD for the changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

5.  Restart the SSH service to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    systemctl restart sshd
    ```

**Verification**

-   To confirm SSSD is serving the key, run the following command on the configured system:

    ``` {.language-plaintext tabindex="-1"}
    sss_ssh_authorizedkeys <username>
    ```

    The command returns the user's public key string.

    For more information, see the `sss_ssh_authorizedkeys(1)`{.literal} man page.

-   From a remote machine, attempt to log in to the configured system using an SSH key:

    ``` {.language-plaintext tabindex="-1"}
    ssh <username>@remote-idm-host.example.com
    ```

    The client authenticates using the key served by SSSD, allowing you to connect without being prompted for a password.

    For more information on configuring SSH and on the configuration files, see the `ssh_config(5)`{.literal} man page.

### [12.3. Troubleshooting SSSD SSH key retrieval](#troubleshooting-the-sssd-key-cache) {#troubleshooting-sssd-ssh-key-retrieval .title}

If you update a key in Identity Management (IdM) but the change is not reflected in SSH login attempts, the issue can occur at two levels. First, SSSD might fail to retrieve the key from IdM or OpenSSH might fail to invoke the SSSD helper commands due to a misconfigured `AuthorizedKeysCommand`{.literal} or `KnownHostsCommand`{.literal} directive.

For details on debugging how SSSD fetches, caches, and verifies remote SSH keys or how it integrates into system authentication, see the `sssd-ssh`{.literal}, `sss_ssh_authorizedkeys`{.literal}, `sss_ssh_knownhosts`{.literal}, and `authselect`{.literal} man pages.

**Procedure**

-   Verify that SSSD can retrieve keys by manually running the commands that OpenSSH is configured to invoke:

    -   To check user keys:

        ``` {.language-plaintext tabindex="-1"}
        sss_ssh_authorizedkeys <username>
        ```

    -   To check host keys:

        ``` {.language-plaintext tabindex="-1"}
        sss_ssh_knownhosts <hostname>
        ```

        If either command returns an empty output or an error, the problem is in key retrieval between SSSD and IdM. Review the SSSD logs in `/var/log/sssd/sssd_ssh.log`{.literal} for errors.

        If the commands return the expected keys, the problem is likely in how SSH invokes these tools. Verify the `AuthorizedKeysCommand`{.literal} and `KnownHostsCommand`{.literal} directives in your SSH configuration files.

-   Reproduce the failing SSH connection with verbose output to identify where the failure occurs:

    ``` {.language-plaintext tabindex="-1"}
    ssh -v <username>@<hostname>
    ```

    You can increase the verbosity level up to three times (`-vvv`{.literal}) for more detailed debug messages.

-   If the keys are retrieved correctly but are stale, clear the SSSD cache for a specific user:

    ``` {.language-plaintext tabindex="-1"}
    sss_cache -u <username>
    ```

## [Chapter 13. Eliminating typographical errors in local SSSD configuration](#eliminating-typographical-errors-in-local-sssd-configuration) {#chapter-13.-eliminating-typographical-errors-in-local-sssd-configuration .title}

Use the `sssctl config-check`{.literal} command to validate the syntax of SSSD configuration files. This utility detects typos and invalid parameters in `/etc/sssd/sssd.conf`{.literal}, ensuring clean configuration before restarting the service.

**Prerequisites**

-   You are logged in as root.
-   The `sssd-tools`{.literal} package is installed.

**Procedure**

1.  Enter the `sssctl config-check`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # sssctl config-check
    ```

    ``` {.language-plaintext tabindex="-1"}
    Issues identified by validators: 1
    [rule/allowed_domain_options]: Attribute 'ldap_search' is not allowed in section 'domain/<domain_name>'. Check for typos.

    Messages generated during configuration merging: 0

    Used configuration snippet files: 0
    ```

2.  Open the `/etc/sssd/sssd.conf`{.literal} file and correct the typo. If you, for example, received the error message in the previous step, replace `ldap_search`{.literal} with `ldap_search_base`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [...]
    [domain/<domain_name>]
    ldap_search_base = dc=<domain_component>,dc=<tld>
    [...]
    ```

3.  Save the file.

4.  Restart SSSD:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

**Verification**

-   Enter the `sssctl config-check`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # sssctl config-check
    ```

    The output should indicate that no issues were found:

``` {.language-plaintext tabindex="-1"}
Issues identified by validators: 0

Messages generated during configuration merging: 0

Used configuration snippet files: 0
```

The `/etc/sssd/sssd.conf`{.literal} file now has no typographical errors.

## [Chapter 14. Troubleshooting authentication with SSSD in IdM](#troubleshooting-authentication-with-sssd-in-idm) {#chapter-14.-troubleshooting-authentication-with-sssd-in-idm .title}

Troubleshoot SSSD by analyzing interactions between clients, back-end servers, and authentication protocols. Tracing data flows helps isolate failures to specific components within the Identity Management infrastructure.

Authentication in an Identity Management (IdM) environment involves many components:

On the IdM client

:   -   The SSSD service.
    -   The Name Services Switch (NSS).
    -   Pluggable Authentication Modules (PAM).

On the IdM server

:   -   The SSSD service.
    -   The IdM Directory Server.
    -   The IdM Kerberos Key Distribution Center (KDC).

If you are authenticating as an Active Directory (AD) user

:   -   The Directory Server on an AD Domain Controller.
    -   The Kerberos server on an AD Domain Controller.

To authenticate users, you must be able to perform the following functions with the SSSD service:

-   Retrieve user information from the authentication server.
-   Prompt the user for their credentials, pass those credentials to the authentication server, and process the outcome.

Troubleshooting involves understanding how information flows between the SSSD service and the servers that store user information. This helps you to identify where the issue occurs and narrow down potential causes.

### [14.1. Data flow when retrieving IdM user information with SSSD](#data-flow-when-retrieving-idm-user-information-with-sssd) {#data-flow-when-retrieving-idm-user-information-with-sssd .title}

SSSD retrieves user data by routing `libc`{.literal} requests through the NSS responder to the backend process. The service checks local caches first, querying the remote IdM server only when necessary to fetch current identity information.

The following diagram is a simplification of the information flow between an IdM client and an IdM server during a request for IdM user information with the command `getent passwd `{.literal}*`<idm_user_name>`{.literal}*.

**Information flow between an IdM client and server for user information retrieval using `getent passwd`{.literal}**

1.  The `getent`{.literal} command triggers the `getpwnam`{.literal} call from the `libc`{.literal} library.
2.  The `libc`{.literal} library references the `/etc/nsswitch.conf`{.literal} configuration file to check which service is responsible for providing user information, and discovers the entry `sss`{.literal} for the SSSD service.
3.  The `libc`{.literal} library opens the `nss_sss`{.literal} module.
4.  The nss_sss module checks the memory-mapped cache for the user information. If the data is present in the cache, the `nss_sss`{.literal} module returns it.
5.  If the user information is not in the memory-mapped cache, the request is passed to the SSSD `sssd_nss`{.literal} responder process.
6.  The SSSD service checks its cache. If the data is present in the cache and valid, the `sssd_nss`{.literal} responder reads the data from the cache and returns it to the application.
7.  If the data is not present in the cache or it is expired, the `sssd_nss`{.literal} responder queries the appropriate back-end process and waits for a reply. The SSSD service uses the IPA backend in an IdM environment, enabled by the setting `id_provider=ipa`{.literal} in the `sssd.conf`{.literal} configuration file.
8.  The `sssd_be`{.literal} back-end process connects to the IdM server and requests the information from the IdM LDAP Directory Server.
9.  The SSSD back-end on the IdM server responds to the SSSD back-end process on the IdM client.
10. The SSSD back-end on the client stores the resulting data in the SSSD cache and alerts the responder process that the cache has been updated.
11. The `sssd_nss`{.literal} front-end responder process retrieves the information from the SSSD cache.
12. The `sssd_nss`{.literal} responder sends the user information to the `nss_sss`{.literal} responder, completing the request.
13. The `libc`{.literal} library returns the user information to the application that requested it.

### [14.2. Data flow when retrieving AD user information with SSSD](#data-flow-when-retrieving-ad-user-information-with-sssd) {#data-flow-when-retrieving-ad-user-information-with-sssd .title}

Retrieving Active Directory (AD) data involves the IdM server acting as a bridge. The client SSSD service queries the IdM server, which triggers the `extdom_extop`{.literal} plugin to fetch identity records from the AD Domain Controller.

If you have established a cross-forest trust between your IdM environment and an AD domain, the information flow when retrieving AD user information about an IdM client is very similar to the information flow when retrieving IdM user information, with the additional step of contacting the AD user database.

The following diagram is a simplification of the information flow when a user requests information about an AD user with the command `getent passwd `{.literal}*`<user_name@ad.example.com>`{.literal}*. It focuses on the communication between the SSSD service on an IdM client, the SSSD service on an IdM server, and the LDAP database on an AD Domain Controller.

**Information flow for retrieval of AD user information between an IdM client, IdM server, and AD Domain controller** image::169_RHEL_IdM_with_SSSD_0621-ad_user_info.png\[\"A diagram with numbered arrows representing the flow of information between an IdM client, an IdM server, and an AD Domain Controller. The following numbered list describes each step in the process.\"\]

1.  The IdM client looks to its local SSSD cache for AD user information.
2.  If the IdM client does not have the user information, or the information is stale, the SSSD service on the client contacts the `extdom_extop`{.literal} plugin on the IdM server to perform an LDAP extended operation and requests the information.
3.  The SSSD service on the IdM server looks for the AD user information in its local cache.
4.  If the IdM server does not have the user information in its SSSD cache, or its information is stale, it performs an LDAP search to request the user information from an AD Domain Controller.
5.  The SSSD service on the IdM server receives the AD user information from the AD domain controller and stores it in its cache.
6.  The `extdom_extop`{.literal} plugin receives the information from the SSSD service on the IdM server, which completes the LDAP extended operation.
7.  The SSSD service on the IdM client receives the AD user information from the LDAP extended operation.
8.  The IdM client stores the AD user information in its SSSD cache and returns the information to the application that requested it.

### [14.3. Data flow when authenticating as a user with SSSD in IdM](#data-flow-when-authenticating-as-a-user-with-sssd-in-idm) {#data-flow-when-authenticating-as-a-user-with-sssd-in-idm .title}

Services invoke the Pluggable Authentication Module (PAM) stack to initiate authentication. SSSD processes these requests by spawning child processes to validate credentials against the IdM Kerberos Key Distribution Center (KDC), supporting both standard password and smart card verification methods.

Authenticating as a user on an IdM server or client involves the following components:

-   The service that initiates the authentication request, such as the `sshd`{.literal} service.

-   The PAM library and its modules.

-   The SSSD service, its responders, and back-ends.

-   A smart card reader, if smart card authentication is configured.

-   The authentication server:

    -   IdM users are authenticated against an IdM KDC.
    -   Active Directory (AD) users are authenticated against an AD Domain Controller (DC).

The following diagram is a simplification of the information flow when a user needs to authenticate during an attempt to log in locally to a host via the SSH service on the command line.

**Information flow between an IdM client and an IdM server or AD Domain Controller during an authentication attempt**

1.  The authentication attempt with the `ssh`{.literal} command triggers the `libpam`{.literal} library.

2.  The `libpam`{.literal} library references the PAM file in the `/etc/pam.d/`{.literal} directory that corresponds to the service requesting the authentication attempt. In this example involving authenticating via the SSH service on the local host, the `libpam`{.literal} library checks the `/etc/pam.d/system-auth`{.literal} configuration file and discovers the `pam_sss.so`{.literal} entry for the SSSD PAM:

    ``` {.language-plaintext tabindex="-1"}
    auth    sufficient    pam_sss.so
    ```

3.  To determine which authentication methods are available, the `libpam`{.literal} library opens the `pam_sss`{.literal} module and sends an `SSS_PAM_PREAUTH`{.literal} request to the `sssd_pam`{.literal} PAM responder of the SSSD service.

4.  If smart card authentication is configured, the SSSD service spawns a temporary `p11_child`{.literal} process to check for a smart card and retrieve certificates from it.

5.  If smart card authentication is configured for the user, the `sssd_pam`{.literal} responder attempts to match the certificate from the smart card with the user. The `sssd_pam`{.literal} responder also performs a search for the groups that the user belongs to, since group membership might affect access control.

6.  The `sssd_pam`{.literal} responder sends an `SSS_PAM_PREAUTH`{.literal} request to the `sssd_be`{.literal} back-end responder to see which authentication methods the server supports, such as passwords or 2-factor authentication. In an IdM environment, where the SSSD service uses the IPA responder, the default authentication method is Kerberos. For this example, the user authenticates with a simple Kerberos password.

7.  The `sssd_be`{.literal} responder spawns a temporary `krb5_child`{.literal} process.

8.  The `krb5_child`{.literal} process contacts the KDC on the IdM server and checks for available authentication methods.

9.  The KDC responds to the request:

    a.  The `krb5_child`{.literal} process evaluates the reply and sends the results back to the `sssd_be`{.literal} backend process.
    b.  The `sssd_be`{.literal} backend process receives the result.
    c.  The `sssd_pam`{.literal} responder receives the result.
    d.  The `pam_sss`{.literal} module receives the result.

10. If password authentication is configured for the user, the `pam_sss`{.literal} module prompts the user for their password. If smart card authentication is configured, the `pam_sss`{.literal} module prompts the user for their smart card PIN.

11. The module sends an `SSS_PAM_AUTHENTICATE`{.literal} request with the user name and password, which travels to:

    a.  The `sssd_pam`{.literal} responder.
    b.  The `sssd_be`{.literal} back-end process.

12. The `sssd_be`{.literal} process spawns a temporary `krb5_child`{.literal} process to contact the KDC.

13. The `krb5_child`{.literal} process attempts to retrieve a Kerberos Ticket Granting Ticket (TGT) from the KDC with the user name and password the user provided.

14. The `krb5_child`{.literal} process receives the result of the authentication attempt.

15. The `krb5_child`{.literal} process:

    a.  Stores the TGT in a credential cache.
    b.  Returns the authentication result to the `sssd_be`{.literal} back-end process.

16. The authentication result travels from the `sssd_be`{.literal} process to:

    a.  The `sssd_pam`{.literal} responder.
    b.  The `pam_sss`{.literal} module.

17. The `pam_sss`{.literal} module sets an environment variable with the location of the user's TGT so other applications can reference it.

### [14.4. Narrowing the scope of authentication issues](#narrowing-the-scope-of-authentication-issues) {#narrowing-the-scope-of-authentication-issues .title}

Diagnosing login failures requires validating the authentication chain step-by-step. Verify network connectivity, service status, and KDC reachability before analyzing specific authorization rules.

To successfully authenticate a user, you must be able to retrieve user information with the SSSD service from the database that stores user information. Follow the steps to test different components of the authentication process so you can narrow the scope of authentication issues when a user is unable to log in.

**Procedure**

1.  Verify that the SSSD service and its processes are running.

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# pstree -a | grep sssd
    ```

    ``` {.language-plaintext tabindex="-1"}
      |-sssd -i --logger=files
      |   |-sssd_be --domain implicit_files --uid 0 --gid 0 --logger=files
      |   |-sssd_be --domain <domain_name> --uid 0 --gid 0 --logger=files
      |   |-sssd_ifp --uid 0 --gid 0 --logger=files
      |   |-sssd_nss --uid 0 --gid 0 --logger=files
      |   |-sssd_pac --uid 0 --gid 0 --logger=files
      |   |-sssd_pam --uid 0 --gid 0 --logger=files
      |   |-sssd_ssh --uid 0 --gid 0 --logger=files
      |   `-sssd_sudo --uid 0 --gid 0 --logger=files
      |-sssd_kcm --uid 0 --gid 0 --logger=files
    ```

2.  Verify that the client can contact the user database server using its IP address.

    ``` {.language-plaintext tabindex="-1"}
    [user@client ~]$ ping <IP_address_of_the_database_server>
    ```

    If this step fails, check that your network and firewall settings allow direct communication between IdM clients and servers. See [Using and configuring firewalld](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_firewalls_and_packet_filters/using-and-configuring-firewalld).

3.  Verify that the client can discover and contact the IdM LDAP server (for IdM users) or AD domain controller (for AD users) using its fully qualified host name.

    ``` {.language-plaintext tabindex="-1"}
    [user@client ~]$ dig -t SRV ldap._tcp.<domain>@<server_name>
    [user@client ~]$ ping <fully_qualified_host_name_of_the_server>
    ```

    If this step fails, check your Dynamic Name Service (DNS) settings, including the `/etc/resolv.conf`{.literal} file. See [Configuring the order of DNS servers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_networking/configuring-the-order-of-dns-servers).

    Note

    By default, the SSSD service attempts to automatically discover LDAP servers and AD DCs through DNS service (SRV) records. To restrict SSSD to specific servers, define them in the `sssd.conf`{.literal} configuration file using the following options:

    -   `ipa_server = `{.literal}*`<fully_qualified_host_name_of_the_server>`{.literal}*
    -   `ad_server = `{.literal}*`<fully_qualified_host_name_of_the_server>`{.literal}*
    -   `ldap_uri = `{.literal}*`<fully_qualified_host_name_of_the_server>`{.literal}*

    If you use these options, verify you can contact the servers listed in them.

4.  Verify that the client can authenticate to the LDAP server and retrieve user information with `ldapsearch`{.literal} commands.

    a.  If your LDAP server is an IdM server, like `server.example.com`{.literal}, retrieve a Kerberos ticket for the host and perform the database search authenticating with the host Kerberos principal:

        ``` {.language-plaintext tabindex="-1"}
        [user@client ~]$ kinit -k 'host/client.example.com@EXAMPLE.COM'
        [user@client ~]$ ldapsearch -LLL -Y GSSAPI -h server.example.com -b "dc=example,dc=com" uid=<idm_user>
        ```

    b.  If your LDAP server is an Active Directory (AD) Domain Controller (DC), like `server.ad.example.com`{.literal}, retrieve a Kerberos ticket for the host and perform the database search authenticating with the host Kerberos principal:

        ``` {.language-plaintext tabindex="-1"}
        [user@client ~]$ kinit -k 'CLIENT$@AD.EXAMPLE.COM'
        [user@client ~]$ ldapsearch -LLL -Y GSSAPI -h server.ad.example.com -b "dc=example,dc=com" sAMAccountname=<idm_user>
        ```

    c.  If your LDAP server is a plain LDAP server, and you have set the `ldap_default_bind_dn`{.literal} and `ldap_default_authtok`{.literal} options in the `sssd.conf`{.literal} file, authenticate as the same `ldap_default_bind_dn`{.literal} account:

        ``` {.language-plaintext tabindex="-1"}
        [user@client ~]$ ldapsearch -xLLL -D "cn=ldap_default_bind_dn_value" -W -h ldapserver.example.com -b "dc=example,dc=com" uid=<idm_user>
        ```

    If this step fails, verify that your database settings allow your host to search the LDAP server.

5.  Since the SSSD service uses Kerberos encryption, verify you can obtain a Kerberos ticket as the user that is unable to log in.

    a.  If your LDAP server is an IdM server:

        ``` {.language-plaintext tabindex="-1"}
        [user@client ~]$ kinit <idm_user>
        ```

    b.  If LDAP server database is an AD server:

        ``` {.language-plaintext tabindex="-1"}
        [user@client ~]$ kinit <ad_user@AD.EXAMPLE.COM>
        ```

    If this step fails, verify that your Kerberos server is operating properly, all servers have their times synchronized, and that the user account is not locked.

6.  Verify you can retrieve user information about the command line.

    ``` {.language-plaintext tabindex="-1"}
    [user@client ~]$ getent passwd <idm_user>
    [user@client ~]$ id <idm_user>
    ```

    If this step fails, verify that the SSSD service on the client can receive information from the user database:

    a.  Review errors in the `/var/log/messages`{.literal} log file.
    b.  Enable detailed logging in the SSSD service, collect debugging logs, and review the logs for indications to the source of the issue.
    c.  Optional: Open a Red Hat Technical Support case and provide the troubleshooting information you have gathered.

7.  If you have `sudo`{.literal} privileges on the host, use the `sssctl`{.literal} utility to verify the user is allowed to log in.

    ``` {.language-plaintext tabindex="-1"}
    [user@client ~]$ sudo sssctl user-checks -a auth -s ssh <idm_user>
    ```

    If this step fails, verify your authorization settings, such as your PAM configuration, IdM HBAC rules, and IdM RBAC rules:

    a.  Ensure that the user's UID is equal to or higher than `UID_MIN`{.literal}, which is defined in the `/etc/login.defs`{.literal} file.
    b.  Review authorization errors in the `/var/log/secure`{.literal} and `/var/log/messages`{.literal} log files.
    c.  Enable detailed logging in the SSSD service, collect debugging logs, and review the logs for indications to the source of the issue.
    d.  Optional: Open a Red Hat Technical Support case and provide the troubleshooting information you have gathered.

**Additional resources**

-   [Enabling detailed logging for SSSD in the sssd.conf file](#enabling-detailed-logging-for-sssd-in-the-sssd-conf-file "14.6. Enabling detailed logging for SSSD in the sssd.conf file")
-   [Enabling detailed logging for SSSD with the sssctl command](#enabling-detailed-logging-for-sssd-with-the-sssctl-command "14.7. Enabling detailed logging for SSSD with the sssctl command")
-   [Gathering debugging logs from the SSSD service to troubleshoot authentication issues with an IdM server](#gathering-debugging-logs-from-the-sssd-service-to-troubleshoot-authentication-issues-with-an-idm-server "14.8. Gathering debugging logs from the SSSD service to troubleshoot authentication issues with an IdM server")
-   [Gathering debugging logs from the SSSD service to troubleshoot authentication issues with an IdM client](#gathering-debugging-logs-from-the-sssd-service-to-troubleshoot-authentication-issues-with-an-idm-client "14.9. Gathering debugging logs from the SSSD service to troubleshoot authentication issues with an IdM client")

### [14.5. SSSD log files and logging levels](#sssd-log-files-and-logging-levels) {#sssd-log-files-and-logging-levels .title}

SSSD segregates logs by domain and component in the `/var/log/sssd/`{.literal} directory. Configure debug levels ranging from 0 to 9 to control verbosity, balancing disk usage with diagnostic detail.

For an IdM server in the `example.com`{.literal} IdM domain, its log files might look like this:

``` {.language-plaintext tabindex="-1"}
[root@server ~]# ls -l /var/log/sssd/
```

``` {.language-plaintext tabindex="-1"}
total 620
-rw-------.  1 root root      0 Mar 29 09:21 krb5_child.log
-rw-------.  1 root root  14324 Mar 29 09:50 ldap_child.log
-rw-------.  1 root root 212870 Mar 29 09:50 sssd_example.com.log
-rw-------.  1 root root      0 Mar 29 09:21 sssd_ifp.log
-rw-------.  1 root root      0 Mar 29 09:21 sssd_implicit_files.log
-rw-------.  1 root root      0 Mar 29 09:21 sssd.log
-rw-------.  1 root root 219873 Mar 29 10:03 sssd_nss.log
-rw-------.  1 root root      0 Mar 29 09:21 sssd_pac.log
-rw-------.  1 root root  13105 Mar 29 09:21 sssd_pam.log
-rw-------.  1 root root   9390 Mar 29 09:21 sssd_ssh.log
-rw-------.  1 root root      0 Mar 29 09:21 sssd_sudo.log
```

#### [14.5.1. SSSD log file purposes](#sssd_log_file_purposes) {#sssd-log-file-purposes .title}

Each SSSD component maintains a dedicated log file to isolate specific operations. These files capture data from helper processes, responders, and domain backends, simplifying the search for relevant error messages.

`krb5_child.log`{.literal}
:   Log file for the short-lived helper process involved in Kerberos authentication.

`ldap_child.log`{.literal}
:   Log file for the short-lived helper process involved in getting a Kerberos ticket for the communication with the LDAP server.

`sssd_<domain_name>.log`{.literal}

:   For each domain section in the `sssd.conf`{.literal} file, the SSSD service logs information about communication with the LDAP server to a separate log file. For example, in an environment with an IdM domain named `example.com`{.literal}, the SSSD service logs its information in a file named `sssd_example.com.log`{.literal}. If a host is directly integrated with an AD domain named `ad.example.com`{.literal}, information is logged to a file named `sssd_ad.example.com.log`{.literal}.

    Note

    If you have an IdM environment and a cross-forest trust with an AD domain, information about the AD domain is still logged to the log file for the IdM domain.

    Similarly, if a host is directly integrated to an AD domain, information about any child domains is written in the log file for the primary domain.

`selinux_child.log`{.literal}
:   Log file for the short-lived helper process that retrieves and sets SELinux information.

`sssd.log`{.literal}
:   Log file for SSSD monitoring and communicating with its responder and backend processes.

`sssd_ifp.log`{.literal}
:   Log file for the InfoPipe responder, which provides a public D-Bus interface accessible over the system bus.

`sssd_nss.log`{.literal}
:   Log file for the Name Services Switch (NSS) responder that retrieves user and group information.

`sssd_pac.log`{.literal}
:   Log file for the Microsoft Privilege Attribute Certificate (PAC) responder, which collects the PAC from AD Kerberos tickets and derives information about AD users from the PAC, which avoids requesting it directly from AD.

`sssd_pam.log`{.literal}
:   Log file for the Pluggable Authentication Module (PAM) responder.

`sssd_ssh.log`{.literal}
:   Log file for the SSH responder process.

#### [14.5.2. SSSD logging levels](#sssd_logging_levels) {#sssd-logging-levels .title}

Debug levels define the granularity of recorded events. Higher integer values capture increasingly detailed trace messages and internal function data, while lower levels record only critical or fatal service failures.

Setting a debug level also enables all debug levels below it. For example, setting the debug level at 6 also enables debug levels 0 through 5.

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Level                             | Description                                                                                                                         |
+:==================================+:====================================================================================================================================+
| 0                                 | **Fatal failures**. Errors that prevent the SSSD service from starting up or cause it to terminate.                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| 1                                 | **Critical failures**. Errors that do not terminate the SSSD service, but at least one major feature is not working properly.       |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| 2                                 | **Serious failures**. Errors announcing that a particular request or operation has failed. **This is the default debug log level.** |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| 3                                 | **Minor failures**. Errors that cause the operation failures captured at level 2.                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| 4                                 | **Configuration** settings.                                                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| 5                                 | **Function** data.                                                                                                                  |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| 6                                 | Trace messages for **operation** functions.                                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| 7                                 | Trace messages for **internal control** functions.                                                                                  |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| 8                                 | Contents of **function-internal** variables.                                                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| 9                                 | Extremely **low-level tracing** information.                                                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+

: Table 14.1. SSSD logging levels

Show more

### [14.6. Enabling detailed logging for SSSD in the sssd.conf file](#enabling-detailed-logging-for-sssd-in-the-sssd-conf-file) {#enabling-detailed-logging-for-sssd-in-the-sssd.conf-file .title}

Enable persistent verbose logging by modifying the `sssd.conf`{.literal} file. Setting the `debug_level`{.literal} parameter in specific configuration sections captures detailed data across service restarts.

By default, the SSSD service only logs serious failures (debug level 2), but it does not log at the level of detail necessary to troubleshoot authentication issues.

To enable detailed logging persistently across SSSD service restarts, add the option `debug_level=`{.literal}*`<integer>`{.literal}* in each section of the `/etc/sssd/sssd.conf`{.literal} configuration file, where the *`<integer>`{.literal}* value is a number between 0 and 9. Debug levels up to 3 log larger failures, and levels 8 and higher provide a large number of detailed log messages. **Level 6** is a good starting point for debugging authentication issues.

**Prerequisites**

-   You need the root password to edit the `sssd.conf`{.literal} configuration file and restart the SSSD service.

**Procedure**

1.  Open the `/etc/sssd/sssd.conf`{.literal} file in a text editor.

2.  Add the `debug_level`{.literal} option to every section of the file, and set the debug level to the verbosity of your choice.

    ``` {.language-plaintext tabindex="-1"}
    [domain/<domain_name>]
    debug_level = 6
    id_provider = ipa
    ...

    [sssd]
    debug_level = 6
    services = nss, pam, ifp, ssh, sudo
    domains = <domain_name>

    [nss]
    debug_level = 6

    [pam]
    debug_level = 6

    [sudo]
    debug_level = 6

    [ssh]
    debug_level = 6

    [pac]
    debug_level = 6

    [ifp]
    debug_level = 6
    ```

3.  Save and close the `sssd.conf`{.literal} file.

4.  Restart the SSSD service to load the new configuration settings.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# systemctl restart sssd
    ```

**Additional resources**

-   [SSSD log files and logging levels](#sssd-log-files-and-logging-levels "14.5. SSSD log files and logging levels")

### [14.7. Enabling detailed logging for SSSD with the sssctl command](#enabling-detailed-logging-for-sssd-with-the-sssctl-command) {#enabling-detailed-logging-for-sssd-with-the-sssctl-command .title}

The `sssctl`{.literal} utility adjusts logging verbosity immediately without editing configuration files. With this command, you can increase debug levels to capture specific events during active troubleshooting sessions.

By default, the SSSD service only logs serious failures (debug level 2), but it does not log at the level of detail necessary to troubleshoot authentication issues.

You can change the debug level of the SSSD service on the command line with the `sssctl debug-level `{.literal}*`<integer>`{.literal}* command, where the *`<integer>`{.literal}* value is a number between 0 and 9. Debug levels up to 3 log larger failures, and levels 8 and higher provide a large number of detailed log messages. Level 6 is a good starting point for debugging authentication issues.

**Prerequisites**

-   You need the root password to run the `sssctl`{.literal} command.

**Procedure**

-   Use the `sssctl debug-level`{.literal} command to set the debug level to your desired verbosity. For example:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# sssctl debug-level 6
    ```

**Additional resources**

-   [SSSD log files and logging levels](#sssd-log-files-and-logging-levels "14.5. SSSD log files and logging levels")

### [14.8. Gathering debugging logs from the SSSD service to troubleshoot authentication issues with an IdM server](#gathering-debugging-logs-from-the-sssd-service-to-troubleshoot-authentication-issues-with-an-idm-server) {#gathering-debugging-logs-from-the-sssd-service-to-troubleshoot-authentication-issues-with-an-idm-server .title}

Resolving server-side authentication errors involves capturing a clean set of logs during a reproduction attempt. Clear old logs and caches before triggering the failure to generate a focused dataset.

If you experience issues when attempting to authenticate as an IdM user to an IdM server, enable detailed debug logging in the SSSD service on the server and gather logs of an attempt to retrieve information about the user.

**Prerequisites**

-   You have `root`{.literal} permissions.

**Procedure**

1.  Enable detailed SSSD debug logging on the IdM server.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# sssctl debug-level 6
    ```

2.  Invalidate objects in the SSSD cache for the user that is experiencing authentication issues, so you do not bypass the LDAP server and retrieve information SSSD has already cached.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# sssctl cache-expire -u <idm_user>
    ```

3.  Minimize the troubleshooting dataset by removing older SSSD logs.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# sssctl logs-remove
    ```

4.  Attempt to switch to the user experiencing authentication problems, while gathering timestamps before and after the attempt. These timestamps further narrow the scope of the dataset.

    ``` {.language-plaintext tabindex="-1"}
    [root@server sssd]# date; su <idm_user>; date
    ```

    ``` {.language-plaintext tabindex="-1"}
    Mon Mar 29 15:33:48 EDT 2021
    su: user idm_user does not exist
    Mon Mar 29 15:33:49 EDT 2021
    ```

5.  Optional: Lower the debug level if you do not wish to continue gathering detailed SSSD logs.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# sssctl debug-level 2
    ```

6.  Review SSSD logs for information about the failed request. For example, reviewing the `/var/log/sssd/sssd_example.com.log`{.literal} file shows that the SSSD service did not find the user in the `cn=accounts,dc=example,dc=com`{.literal} LDAP subtree. This might indicate that the user does not exist, or exists in another location.

    ``` {.language-plaintext tabindex="-1"}
    (Mon Mar 29 15:33:48 2021) [sssd[be[example.com]]] [dp_get_account_info_send] (0x0200): Got request for [0x1][BE_REQ_USER][name=idm_user@example.com]
    ...
    (Mon Mar 29 15:33:48 2021) [sssd[be[example.com]]] [sdap_get_generic_ext_step] (0x0400): calling ldap_search_ext with [(&(uid=idm_user)(objectclass=posixAccount)(uid=)(&(uidNumber=)(!(uidNumber=0))))][cn=accounts,dc=example,dc=com].
    (Mon Mar 29 15:33:48 2021) [sssd[be[example.com]]] [sdap_get_generic_op_finished] (0x0400): Search result: Success(0), no errmsg set
    (Mon Mar 29 15:33:48 2021) [sssd[be[example.com]]] [sdap_search_user_process] (0x0400): Search for users, returned 0 results.
    (Mon Mar 29 15:33:48 2021) [sssd[be[example.com]]] [sysdb_search_by_name] (0x0400): No such entry
    (Mon Mar 29 15:33:48 2021) [sssd[be[example.com]]] [sysdb_delete_user] (0x0400): Error: 2 (No such file or directory)
    (Mon Mar 29 15:33:48 2021) [sssd[be[example.com]]] [sysdb_search_by_name] (0x0400): No such entry
    (Mon Mar 29 15:33:49 2021) [sssd[be[example.com]]] [ipa_id_get_account_info_orig_done] (0x0080): Object not found, ending request
    ```

7.  If you are unable to determine the cause of the authentication issue:

    a.  Collect the SSSD logs you recently generated.

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# sssctl logs-fetch sssd-logs-Mar29.tar
        ```

    b.  Open a Red Hat Technical Support case and provide:

        i.  The SSSD logs: `sssd-logs-Mar29.tar`{.literal}

        ii. The console output, including the time stamps and user name, of the request that corresponds to the logs:

            ``` {.language-plaintext tabindex="-1"}
            [root@server sssd]# date; id <idm_user>; date
            ```

            ``` {.language-plaintext tabindex="-1"}
            Mon Mar 29 15:33:48 EDT 2021
            id: 'idm_user': no such user
            Mon Mar 29 15:33:49 EDT 2021
            ```

### [14.9. Gathering debugging logs from the SSSD service to troubleshoot authentication issues with an IdM client](#gathering-debugging-logs-from-the-sssd-service-to-troubleshoot-authentication-issues-with-an-idm-client) {#gathering-debugging-logs-from-the-sssd-service-to-troubleshoot-authentication-issues-with-an-idm-client .title}

Client-side issues require simultaneous analysis of both client and server logs. Configure the client to contact a specific server, synchronizing log capture to trace the request across the network.

If you experience issues when attempting to authenticate as an IdM user to an IdM client, verify that you can retrieve user information about the IdM server. If you cannot retrieve the user information about an IdM server, you will not be able to retrieve it on an IdM client (which retrieves information from the IdM server).

After you have confirmed that authentication issues do not originate from the IdM server, gather SSSD debugging logs from both the IdM server and IdM client.

**Prerequisites**

-   The user only has authentication issues on IdM clients, not IdM servers.
-   You need the root password to run the `sssctl`{.literal} command and restart the SSSD service.

**Procedure**

1.  **On the client:** Open the `/etc/sssd/sssd.conf`{.literal} file in a text editor.

2.  **On the client:** Add the `ipa_server`{.literal} option to the `[domain]`{.literal} section of the file and set it to an IdM server using its fully qualified domain name (FQDN). This avoids the IdM client autodiscovering other IdM servers, thus limiting this test to just one client and one server.

    ``` {.language-plaintext tabindex="-1"}
    [domain/<idm_domain_name>]
    ipa_server = <idm_server_fqdn>
    ...
    ```

3.  **On the client:** Save and close the `sssd.conf`{.literal} file.

4.  **On the client:** Restart the SSSD service to load the configuration changes.

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# systemctl restart sssd
    ```

5.  **On the server and client:** Enable detailed SSSD debug logging.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# sssctl debug-level 6
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# sssctl debug-level 6
    ```

6.  **On the server and client:** Invalidate objects in the SSSD cache for the user experiencing authentication issues, so you do not bypass the LDAP database and retrieve information SSSD has already cached.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# sssctl cache-expire -u <idm_user>
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# sssctl cache-expire -u <idm_user>
    ```

7.  **On the server and client:** Minimize the troubleshooting dataset by removing older SSSD logs.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# sssctl logs-remove
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# sssctl logs-remove
    ```

8.  **On the client:** Attempt to switch to the user experiencing authentication problems while gathering timestamps before and after the attempt. These timestamps further narrow the scope of the dataset.

    ``` {.language-plaintext tabindex="-1"}
    [root@client sssd]# date; su <idm_user>; date
    ```

    ``` {.language-plaintext tabindex="-1"}
    Mon Mar 29 16:20:13 EDT 2021
    su: user idm_user does not exist
    Mon Mar 29 16:20:14 EDT 2021
    ```

9.  Optional: **On the server and client:** Lower the debug level if you do not wish to continue gathering detailed SSSD logs.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# sssctl debug-level 0
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# sssctl debug-level 0
    ```

10. **On the server and client:** Review SSSD logs for information about the failed request.

    a.  Review the request from the client in the client logs.
    b.  Review the request from the client in the server logs.
    c.  Review the result of the request in the server logs.
    d.  Review the outcome of the client receiving the results of the request from the server.

11. If you are unable to determine the cause of the authentication issue:

    a.  Collect the SSSD logs you recently generated on the IdM server and IdM client. Label them according to their hostname or role.

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# sssctl logs-fetch sssd-logs-server-Mar29.tar
        ```

        ``` {.language-plaintext tabindex="-1"}
        [root@client ~]# sssctl logs-fetch sssd-logs-client-Mar29.tar
        ```

    b.  Open a Red Hat Technical Support case and provide:

        i.  The SSSD debug logs:

            A.  `sssd-logs-server-Mar29.tar`{.literal} from the server
            B.  `sssd-logs-client-Mar29.tar`{.literal} from the client

        ii. The console output, including the time stamps and user name, of the request that corresponds to the logs:

            ``` {.language-plaintext tabindex="-1"}
            [root@client sssd]# date; su <idm_user>; date
            ```

            ``` {.language-plaintext tabindex="-1"}
            Mon Mar 29 16:20:13 EDT 2021
            su: user idm_user does not exist
            Mon Mar 29 16:20:14 EDT 2021
            ```

### [14.10. Tracking client requests in the SSSD backend](#tracking-client-requests-in-the-sssd-backend) {#tracking-client-requests-in-the-sssd-backend .title}

SSSD assigns unique Request IDs (RID) and Client IDs (CID) to track operations asynchronously. Trace these identifiers through the backend logs to correlate complex sequences of internal events.

To track client request in the back-end logs, you can use the unique request identifier `RID#`{.literal}*`<integer>`{.literal}*``  and client ID `[CID # ``{.literal}*`<integer>`{.literal}*`]`{.literal}. These identifiers help isolate logs to follow an individual request from start to finish across log files from multiple SSSD components.

**Prerequisites**

-   You have enabled debug logging and a request has been submitted from an IdM client.
-   You have `root`{.literal} privileges.

**Procedure**

1.  To review your SSSD log file, open the log file `/var/log/sssd/sssd_<domain_name>.log`{.literal} using the `less`{.literal} utility. For example:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# less /var/log/sssd/sssd_example.com.log
    ```

2.  Review the SSSD logs for information about the client request.

    ``` {.language-plaintext tabindex="-1"}
    (2021-07-26 18:26:37): [be[testidm.com]] [dp_req_destructor] (0x0400): [RID#3] Number of active DP request: 0
    (2021-07-26 18:26:37): [be[testidm.com]] [dp_req_reply_std] (0x1000): [RID#3] DP Request AccountDomain #3: Returning [Internal Error]: 3,1432158301,GetAccountDomain() not supported
    (2021-07-26 18:26:37): [be[testidm.com]] [dp_attach_req] (0x0400): [RID#4] DP Request Account #4: REQ_TRACE: New request. [sssd.nss CID #1] Flags [0x0001].
    (2021-07-26 18:26:37): [be[testidm.com]] [dp_attach_req] (0x0400): [RID#4] Number of active DP request: 1
    ```

    This sample output from an SSSD log file shows the unique identifiers `RID#3`{.literal} and `RID#4`{.literal} for two different requests.

    However, a single client request to the SSSD client interface often triggers multiple requests in the backend and as a result it is not a 1-to-1 correlation between client request and requests in the backend. Though the multiple requests in the backend have different RID numbers, each initial backend request includes the unique client ID so an administrator can track the multiple RID numbers to the single client request.

    The following example shows one client request `[sssd.nss CID #1]`{.literal} and the multiple requests generated in the backend, `[RID#5]`{.literal} to `[RID#13]`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    (2021-10-29 13:24:16): [be[ad.vm]] [dp_attach_req] (0x0400): [RID#5] DP Request [Account #5]: REQ_TRACE: New request. [sssd.nss CID #1] Flags [0x0001].
    (2021-10-29 13:24:16): [be[ad.vm]] [dp_attach_req] (0x0400): [RID#6] DP Request [AccountDomain #6]: REQ_TRACE: New request. [sssd.nss CID #1] Flags [0x0001].
    (2021-10-29 13:24:16): [be[ad.vm]] [dp_attach_req] (0x0400): [RID#7] DP Request [Account #7]: REQ_TRACE: New request. [sssd.nss CID #1] Flags [0x0001].
    (2021-10-29 13:24:17): [be[ad.vm]] [dp_attach_req] (0x0400): [RID#8] DP Request [Initgroups #8]: REQ_TRACE: New request. [sssd.nss CID #1] Flags [0x0001].
    (2021-10-29 13:24:17): [be[ad.vm]] [dp_attach_req] (0x0400): [RID#9] DP Request [Account #9]: REQ_TRACE: New request. [sssd.nss CID #1] Flags [0x0001].
    (2021-10-29 13:24:17): [be[ad.vm]] [dp_attach_req] (0x0400): [RID#10] DP Request [Account #10]: REQ_TRACE: New request. [sssd.nss CID #1] Flags [0x0001].
    (2021-10-29 13:24:17): [be[ad.vm]] [dp_attach_req] (0x0400): [RID#11] DP Request [Account #11]: REQ_TRACE: New request. [sssd.nss CID #1] Flags [0x0001].
    (2021-10-29 13:24:17): [be[ad.vm]] [dp_attach_req] (0x0400): [RID#12] DP Request [Account #12]: REQ_TRACE: New request. [sssd.nss CID #1] Flags [0x0001].
    (2021-10-29 13:24:17): [be[ad.vm]] [dp_attach_req] (0x0400): [RID#13] DP Request [Account #13]: REQ_TRACE: New request. [sssd.nss CID #1] Flags [0x0001].
    ```

### [14.11. Tracking client requests using the log analyzer tool](#tracking-client-requests-using-the-log-analyzer-tool) {#tracking-client-requests-using-the-log-analyzer-tool .title}

The System Security Services Daemon (SSSD) log analyzer tool parses verbose logs to reconstruct request chains. This utility filters the output to show only relevant entries for a specific client request, simplifying the analysis of dense log files.

You can use the tool to track requests from start to finish across log files from multiple SSSD components.

#### [14.11.1. How the log analyzer tool works](#how-the-log-analyzer-tool-works) {#how-the-log-analyzer-tool-works .title}

The analyzer links NSS and PAM requests across multiple SSSD processes. It tracks the lifecycle of a request using Client IDs, helping you to isolate specific authentication or lookup attempts.

Using the log parsing tool, you can track SSSD requests from start to finish across log files from multiple SSSD components. You run the analyzer tool using the `sssctl analyze`{.literal} command.

The log analyzer tool helps you to troubleshoot NSS and PAM issues in SSSD and more easily review SSSD debug logs. You can extract and print SSSD logs related only to certain client requests across SSSD processes.

SSSD tracks user and group identity information (`id`{.literal}, `getent`{.literal}) separately from user authentication (`su`{.literal}, `ssh`{.literal}) information. The client ID (CID) in the NSS responder is independent of the CID in the PAM responder and you see overlapping numbers when analyzing NSS and PAM requests. Use the `--pam`{.literal} option with the `sssctl analyze`{.literal} command to review PAM requests.

Note

Requests returned from the SSSD memory cache are not logged and cannot be tracked by the log analyzer tool.

#### [14.11.2. Running the log analyzer tool](#running-the-log-analyzer-tool) {#running-the-log-analyzer-tool .title}

Use `sssctl analyze`{.literal} to list recent requests and display their associated logs. This workflow identifies the unique Client ID and extracts the specific log entries required for troubleshooting.

**Prerequisites**

-   You must set `debug_level`{.literal} to at least 7 in the `[$responder]`{.literal} section, and `[domain/$domain]`{.literal} section of the `/etc/sssd/sssd.conf`{.literal} file to enable log parsing functionality.
-   Logs to analyze must be from a compatible version of SSSD built with `libtevent`{.literal} chain ID support, that is SSSD in RHEL 8.5 and later.

**Procedure**

1.  Run the log analyzer tool in `list`{.literal} mode to determine the client ID of the request you are tracking, adding the `-v`{.literal} option to display verbose output:

    ``` {.language-plaintext tabindex="-1"}
    # sssctl analyze request list -v
    ```

    A verbose list of recent client requests made to SSSD is displayed.

    Note

    If analyzing PAM requests, run the `sssctl analyze request list`{.literal} command with the `--pam`{.literal} option.

2.  Run the log analyzer tool with the `show [unique client ID]`{.literal} option to display logs pertaining to the specified client ID number:

    ``` {.language-plaintext tabindex="-1"}
    # sssctl analyze request show 20
    ```

3.  If required, you can run the log analyzer tool against log files, for example:

    ``` {.language-plaintext tabindex="-1"}
    # sssctl analyze --logdir=/tmp/var/log/sssd request list
    ```

### [14.12. Additional resources](#troubleshooting-authentication-with-sssd-in-idm_1412-additional-resources) {#additional-resources .title}

-   [General SSSD Debugging Procedures (Red Hat Knowledgebase)](https://access.redhat.com/solutions/217963)

## [Chapter 15. Configuring applications for a single sign-on](#Configuring_Applications_for_SSO) {#chapter-15.-configuring-applications-for-a-single-sign-on .title}

Single sign-on (SSO) simplifies authentication by allowing users to access multiple systems with a single login procedure. Configure applications like browsers and email clients to accept Kerberos tickets, SSL certificates, or tokens as valid credentials.

The configuration of different applications may vary. This chapter shows how to configure SSO authentication schema for the Mozilla Thunderbird email client and Mozilla Firefox web browser as the examples.

### [15.1. Prerequisites](#prerequisites_3) {#prerequisites-2 .title}

Verify that the target system hosts the required versions of Mozilla Firefox and Mozilla Thunderbird before attempting configuration. Ensure these applications are installed and accessible to the user. **Mozilla Firefox *version 88*** Mozilla Thunderbird *version 78*

### [15.2. Configuring Firefox to use Kerberos for single sign-on](#Configuring_Firefox_to_use_Kerberos_for_SSO) {#configuring-firefox-to-use-kerberos-for-single-sign-on .title}

Configure Firefox to negotiate Kerberos authentication with intranet sites. Adding specific domains to the trusted URI list in the configuration settings permits the browser to pass existing Kerberos credentials to the Key Distribution Center (KDC) automatically.

Note

Even after configuring Firefox to pass Kerberos credentials, you still need a valid Kerberos ticket. To generate a Kerberos ticket, use the `kinit`{.literal} command and supply the user password for the user on the KDC.

``` {.language-plaintext tabindex="-1"}
[jsmith@host ~] $ kinit
```

``` {.language-plaintext tabindex="-1"}
Password for jsmith@EXAMPLE.COM:
```

**Procedure**

1.  In the address bar of Firefox, type `about:config`{.literal} to display the list of current configuration options.

2.  In the **Filter** field, type `negotiate`{.literal} to restrict the list of options.

3.  Double-click the **network.negotiate-auth.trusted-uris** entry.

4.  Enter the name of the domain against which to authenticate, including the preceding period (.). If you want to add multiple domains, enter them in a comma separated list.

    **Manual Firefox Configuration**

**Additional resources**

-   [Logging in to IdM in the Web UI: Using a Kerberos ticket](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-idm-in-the-web-ui-using-a-kerberos-ticket)

### [15.3. Viewing certificates in Firefox](#viewing-certificates-in-firefox) {#viewing-certificates-in-firefox .title}

By inspecting the Certificate Manager, users can verify currently installed authorities and personal credentials. This audit ensures the browser possesses the necessary trust anchors for secure connections.

You can view stored certificates in Mozilla Firefox to verify authentication settings.

**Procedure**

1.  In Mozilla Firefox, open the Firefox menu and select **Preferences**.

2.  In the left panel, select the **Privacy & Security** section.

3.  Scroll down to the **Certificates** section.

4.  Click **View Certificates** to open the **Certificate Manager**.

### [15.4. Importing CA certificates in Firefox](#importing-ca-certificates-in-firefox) {#importing-ca-certificates-in-firefox .title}

Importing a Certificate Authority (CA) certificate establishes trust with external servers. Adding the CA file to the browser's store enables secure, encrypted connections to websites and applications issued by that authority.

**Prerequisites**

-   You have a CA certificate on your device.

**Procedure**

1.  Open **Certificate Manager**.

2.  Select the **Authorities** tab and click **Import**.

    **Figure 15.1. Importing the CA Certificate in Firefox**

3.  Select the downloaded CA certificate from your device.

### [15.5. Editing certificate trust settings in Firefox](#editing-certificate-trust-settings-in-firefox) {#editing-certificate-trust-settings-in-firefox .title}

Modify trust settings to define how the browser interacts with specific certificates. Adjusting these permissions determines if the browser validates the certificate for identifying websites or email users.

**Prerequisites**

1.  You have successfully imported a certificate.

**Procedure**

1.  Open **Certificate Manager**.

2.  Under the **Authorities** tab, select the appropriate certificate and click **Edit Trust**.

3.  Edit the certificate trust settings.

    **Figure 15.2. Editing the Certificate Trust Settings in Firefox**

### [15.6. Importing personal certificate for authentication in Firefox](#importing-personal-certificate-for-authentication-in-firefox) {#importing-personal-certificate-for-authentication-in-firefox .title}

Personal certificates identify the user to remote web services. Importing these files into the browser enables client-side authentication, allowing access to secure sites that require identity verification beyond simple passwords.

**Prerequisites**

1.  You have a personal certificate stored on your device.

**Procedure**

1.  Open **Certificate Manager**.

2.  Select the **Your Certificates** tab and click **Import**.

    **Figure 15.3. Importing a Personal Certificate for Authentication in Firefox**

3.  Import the appropriate certificate from your computer.

### [15.7. Viewing certificates in Thunderbird](#viewing-certificates-in-thunderbird) {#viewing-certificates-in-thunderbird .title}

By accessing the Certificate Manager in Thunderbird, users can audit stored security credentials. Reviewing these files ensures the email client contains the correct authorities and personal keys for encrypted communication.

**Procedure**

1.  In Thunderbird, open the main menu and select **Preferences**.

    **Figure 15.4. Selecting Preferences from menu**

2.  In the left panel, select the **Privacy & Security** section.

    **Figure 15.5. Selecting security section**

3.  Scroll down to the **Certificates** section.

4.  Click **Manage Certificates** to open the **Certificate Manager**.

    **Figure 15.6. Opening Certificate Manager**

### [15.8. Importing certificates in Thunderbird](#importing-certificates-in-thunderbird) {#importing-certificates-in-thunderbird .title}

Importing Certificate Authority (CA) files enables the email client to validate secure connections. Adding these authorities ensures Thunderbird trusts the SSL/TLS certificates presented by mail servers during data exchange.

**Prerequisites**

-   You have a CA certificate stored on your device.

**Procedure**

1.  Open **Certificate Manager**.

2.  Select the **Authorities** tab and click **Import**.

    **Figure 15.7. Importing the CA certificate in Thunderbird**

3.  Select the downloaded CA certificate.

### [15.9. Editing certificate trust settings in Thunderbird](#editing-certificate-trust-settings-in-thunderbird) {#editing-certificate-trust-settings-in-thunderbird .title}

Modifying trust attributes controls how Thunderbird validates certificates for specific operations. Adjust these settings to explicitly authorize authorities for identifying mail servers or signing email messages.

**Prerequisites**

-   You have successfully imported a certificate.

**Procedure**

1.  Open **Certificate Manager**.

2.  Under the **Authorities** tab, select the appropriate certificate and click **Edit Trust**.

3.  Edit the certificate trust settings.

    **Figure 15.8. Editing the certificate trust settings in Thunderbird**

### [15.10. Importing personal certificate in Thunderbird](#importing-personal-certificate-in-thunderbird) {#importing-personal-certificate-in-thunderbird .title}

Personal certificates enable S/MIME functionality for signing and encrypting emails. Importing these keys into the personal store allows the client to prove the sender's identity and decrypt incoming secure messages.

**Prerequisites**

1.  You have a personal certificate stored on your device.

**Procedure**

1.  Open **Certificate Manager**.

2.  Under the **Your Certificates** tab, click **Import**.

    **Figure 15.9. Importing a personal certificate for authentication in Thunderbird**

3.  Import the required certificate from your computer.

4.  Close the **Certificate Manager**.

5.  Open the main menu and select **Account Settings**.

    **Figure 15.10. Selecting Account Settings from menu**

6.  Select **End-To-End Encryption** in the left panel under your account email address.

    Selecting End-To-End Encryption section.

7.  Under **S/MIME** section, click the first **Select** button to choose your personal certificate to use for signing messages.

8.  Under **S/MIME** section, click the second **Select** button to choose your personal certificate for encrypting and decrypting messages.

    Choosing certificate for signing and encryption/decryption.

    Note

    If you forgot to import valid certificate, you can open **Certificate Manager** directly using the **Manage S/MIME certificate** option.

## [Legal Notice](#idm140250342294304) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
