---
{"title": "Installing trust between IdM and AD", "guide": "installing_trust_between_idm_and_ad", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/installing_trust_between_idm_and_ad/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Installing trust between IdM and AD {#installing-trust-between-idm-and-ad .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Managing a cross-forest trust between an IdM and AD domain {#managing-a-cross-forest-trust-between-an-idm-and-ad-domain .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm139635748235584)

**Abstract**

Both Identity Management (IdM) and Active Directory (AD) manage a variety of core services, such as Kerberos, LDAP, DNS, and certificate services. A trust relationship transparently integrates these two environments by enabling all core services to interact seamlessly. For example, a trust enables AD users to authenticate to services in the IdM topology. Preparing the trust requires the use of common encryption types in IdM and AD, opening ports in the firewall, and to configure DNS and Kerberos realm settings. If the trust is no longer required, you can remove it.

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

## [Chapter 1. Prerequisites for establishing a trust](#prerequisites-for-establishing-a-trust) {#chapter-1.-prerequisites-for-establishing-a-trust .title}

To establish a cross-forest trust between your Identity Management (IdM) domain and an Active Directory (AD) domain, you must correctly configure all required prerequisites on both the IdM server and the AD domain controller.

-   First, read the Planning a cross-forest trust between Identity Management and Active Directory document.

-   AD is installed with a domain controller on it.

-   The IdM server is installed and running.

-   Both the AD server and the IdM server must have their clocks in sync because Kerberos requires a maximum delay of five minutes in communication.

-   Unique NetBIOS names for each of the servers placed in the trust because the NetBIOS names are critical for identifying the AD domain.

    The NetBIOS name of an AD or IdM domain is usually the first part of the corresponding DNS domain. If the DNS domain is `ad.example.com`{.literal}, the NetBIOS name is typically `AD`{.literal}. However, it is not required. Important is that the NetBIOS name is just one word without periods. The maximum length of a NetBIOS name is 15 characters.

-   The IdM system must have the IPv6 protocol enabled in the kernel.

    If IPv6 is disabled, then the CLDAP plug-in used by the IdM services fails to initialize.

Note

In RHEL 7, *synchronization* and *trust* were two possible approaches to indirect integration of RHEL systems to Active Directory (AD). In RHEL 8, synchronization is deprecated and in RHEL 9, it is not available any more. To integrate IdM and AD, use the trust approach instead.

**Additional resources**

-   [Planning a cross-forest trust between Identity Management and Active Directory](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/planning-a-cross-forest-trust-between-idm-and-ad)
-   [Installing Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management)
-   [Migrating from synchronization to trust in RHEL 8](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html-single/migrating_to_identity_management_on_rhel_8/index#migrating-an-existing-environment-from-synchronization-to-trust-in-the-context-of-integrating-a-linux-domain-with-an-active-directory-domain)

## [Chapter 2. Supported versions of Windows Server](#supported-versions-of-windows-server) {#chapter-2.-supported-versions-of-windows-server .title}

Ensure that your Active Directory (AD) environment meets the requirements for compatibility with Identity Management (IdM).

You can establish a trust relationship with AD forests that use the following forest and domain functional levels:

-   Forest functional level range: Windows Server 2012 --- Windows Server 2025
-   Domain functional level range: Windows Server 2012 --- Windows Server 2025

IdM supports establishing a trust with AD domain controllers running the following operating systems:

-   Windows Server 2025
-   Windows Server 2022
-   Windows Server 2019
-   Windows Server 2016
-   Windows Server 2012 R2
-   Windows Server 2012

Important

IdM does not support establishing trust to AD with AD domain controllers running Windows Server 2008 R2 or earlier versions. IdM requires SMB encryption when establishing the trust relationship, which is only supported in Windows Server 2012 or later.

## [Chapter 3. How the trust between IdM and AD works](#how-the-trust-between-idm-and-ad-works) {#chapter-3.-how-the-trust-between-idm-and-ad-works .title}

Identity Management (IdM) and Active Directory (AD) establish a forest-level trust between two Active Directory forests, with IdM representing a separate AD forest. This enables all AD users to:

-   Log in to access Linux systems and resources.
-   Use single sign-on (SSO).

In the trust relationship, all IdM objects are managed in IdM, while all AD objects are managed in AD.

In complex environments, a single IdM forest can be connected to multiple AD forests. This configuration enables better separation of duties for different functions in the organization. AD administrators can focus on users and policies related to users while Linux administrators have full control over the Linux infrastructure. In such a case, the Linux realm controlled by IdM is analogous to an AD resource domain or realm but with Linux systems in it.

From the perspective of AD, Identity Management represents a separate AD forest with a single AD domain. When cross-forest trust is established between an AD forest root domain and an IdM domain, users from the AD forest domains can interact with Linux machines and services from the IdM domain.

Note

In trust environments, IdM enables you to use ID views to configure POSIX attributes for AD users on the IdM server.

## [Chapter 4. AD administration rights](#ad-administration-rights) {#chapter-4.-ad-administration-rights .title}

To establish a trust between Active Directory (AD) and Identity Management (IdM), you must use an AD administrator account that possesses the necessary privileges.

The AD administrator account used to establish a trust between AD and IdM must belong to one of the following groups:

-   Enterprise Admin group in the AD forest
-   Domain Admins group in the forest root domain for your AD forest

**Additional resources**

-   [Enterprise Admins](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#enterprise-admins)
-   [Domain Admins](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#domain-admins)
-   [How Domain and Forest Trusts Work](https://learn.microsoft.com/en-us/entra/identity/domain-services/concepts-forest-trust)

## [Chapter 5. Ensuring support for common encryption types in AD and RHEL](#ensuring-support-for-common-encryption-types-in-ad-and-rhel) {#chapter-5.-ensuring-support-for-common-encryption-types-in-ad-and-rhel .title}

By default, Identity Management establishes a cross-realm trust with support for AES-128, and AES-256 Kerberos encryption types, having deprecated the less secure RC4 type. However, Active Directory (AD) user credentials and trusts between AD domains might still rely solely on RC4 encryption.

RC4 encryption has been deprecated and disabled by default, as it is considered less secure than the newer AES-128 and AES-256 encryption types. In contrast, Active Directory (AD) user credentials and trusts between AD domains support RC4 encryption and they might not support AES encryption types.

Without any common encryption types, communication between IdM and AD child domains might not work, or some AD accounts might not be able to authenticate.

**Procedure**

1.  To enable AES encryption support in Active Directory (recommended), see the following Microsoft article: [AD DS: Security: Kerberos \"Unsupported etype\" error when accessing a resource in a trusted domain](https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/unsupported-etype-error-accessing-trusted-domain).

2.  To enable RC4 support in RHEL, if your Active Directory environment does not support AES encryption, set the cryptographic subpolicy to support legacy algorithms on every IdM trust controller, trust agent, and client that authenticates against AD Domain Controllers:

    ``` {.language-plaintext tabindex="-1"}
    [root@host ~]# update-crypto-policies --set LEGACY:AD-SUPPORT-LEGACY
    ```

    ``` {.language-plaintext tabindex="-1"}
    Setting system policy to LEGACY:AD-SUPPORT-LEGACY
    Note: System-wide crypto policies are applied on application start-up.
    It is recommended to restart the system for the change of policies
    to fully take place.
    ```

3.  Restart the host.

**Additional resources**

-   [Using system-wide cryptographic policies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/using-system-wide-cryptographic-policies)
-   [Trust controllers and trust agents](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/planning-a-cross-forest-trust-between-idm-and-ad#trust-controllers-and-trust-agents)

## [Chapter 6. Ports required for communication between IdM and AD](#ports-required-for-communication-between-idm-and-ad) {#chapter-6.-ports-required-for-communication-between-idm-and-ad .title}

Open the following ports on the firewalls of your AD Domain Controllers and IdM servers to enable necessary communication between your Active Directory (AD) and Identity Management (IdM) environments.

+--------------------------------+----------------------+----------------------+
| Service                        | Port                 | Protocol             |
+:===============================+:=====================+:=====================+
| Endpoint resolution portmapper | 135                  | TCP                  |
+--------------------------------+----------------------+----------------------+
| Microsoft-DS                   | 445                  | TCP and UDP          |
+--------------------------------+----------------------+----------------------+
| Dynamic RPC                    | 49152-65535          | TCP                  |
+--------------------------------+----------------------+----------------------+
| AD Global Catalog              | 3268                 | TCP                  |
+--------------------------------+----------------------+----------------------+
| LDAP                           | 389                  | TCP and UDP          |
+--------------------------------+----------------------+----------------------+

: Table 6.1. Ports required for an AD trust

Show more

Note

The TCP port 389 is not required to be open on IdM servers for trust, but it is necessary for clients communicating with the IdM server.

The TCP port 135 is required for the DCE RPC end-point mapper to work and is used during the IdM-AD trust creation.

Note

The `ipa-adtrust-install`{.literal} command currently lists ports 138 (NetBIOS-DGM) and 139 (NetBIOS-SSN) in its post-installation summary. These ports are not required and can remain blocked.

To open ports, you can use the following methods:

-   `firewalld`{.literal} service --- you can enable the particular ports or enable the following services which includes the ports:

    -   FreeIPA trust configuration
    -   FreeIPA with LDAP
    -   Kerberos
    -   DNS

    For details, see the `firewall-cmd`{.literal} man page on your system.

-   The [RHEL web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console), which is a UI with firewall settings based on the `firewalld`{.literal} service. In the **Networking** section, click Add services next to the firewall zone you use, and add the required services and ports.

+----------------------+----------------------+----------------------+
| Service              | Port                 | Protocol             |
+:=====================+:=====================+:=====================+
| Kerberos             | 88, 464              | TCP and UDP          |
+----------------------+----------------------+----------------------+
| LDAP                 | 389                  | TCP                  |
+----------------------+----------------------+----------------------+
| DNS                  | 53                   | TCP and UDP          |
+----------------------+----------------------+----------------------+

: Table 6.2. Ports required by IdM servers in a trust

Show more

+----------------------+----------------------+----------------------+
| Service              | Port                 | Protocol             |
+:=====================+:=====================+:=====================+
| Kerberos             | 88                   | UDP and TCP          |
+----------------------+----------------------+----------------------+

: Table 6.3. Ports required by IdM clients in an AD trust

Show more

Note

The `libkrb5`{.literal} library uses UDP and falls back to the TCP protocol if the data sent from the Key Distribution Center (KDC) is too large. Active Directory attaches a Privilege Attribute Certificate (PAC) to the Kerberos ticket, which increases the size and requires to use the TCP protocol. To avoid the fall-back and resending the request, SSSD uses TCP for user authentication by default. If you want to configure the size before `libkrb5`{.literal} uses TCP, set the `udp_preference_limit`{.literal} in the `/etc/krb5.conf`{.literal} file. For details, see the `krb5.conf(5)`{.literal} man page on your system.

The following diagram shows communication sent by IdM clients, and received and responded to by IdM servers and AD Domain Controllers. To set the incoming and outgoing ports and protocols on your firewall, use the `firewalld`{.literal} service, which already has definitions for FreeIPA services.

Note

The default and recommended configuration for establishing a trust uses port `389`{.literal} (LDAP). This connection is secured by SASL/GSSAPI, which provides strong, built-in encryption. For compatibility with specific Active Directory (AD) environments that are configured to reject this default method and mandate LDAPS, communication over port `636`{.literal} is also possible. This is a non-standard configuration and should only be used if your AD policy makes it strictly necessary. Consult your AD administrator to confirm your environment's requirements before configuring your firewall. If you are in this scenario, open a support case.

**Additional resources**

-   [The default dynamic port range for TCP/IP has changed since Windows Vista and in Windows Server 2008](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/default-dynamic-port-range-tcpip-chang)

## [Chapter 7. Configuring DNS and realm settings for a trust](#configuring-dns-and-realm-settings-for-a-trust) {#chapter-7.-configuring-dns-and-realm-settings-for-a-trust .title}

Before establishing a trust between Identity Management (IdM) and Active Directory (AD), you must ensure that both environments can mutually resolve domain names correctly.

To configure DNS resolution between an IdM server, using an integrated DNS server and a Certification Authority (CA), and an AD Domain Controller, perform the following tasks:

-   Prepare the IdM environment: configure the necessary DNS zones and resource records.
-   Enable cross-domain resolution: configure conditional DNS forwarding on the AD server to point to IdM.
-   Validate connectivity: verify the DNS configuration to ensure seamless communication between realms.

### [7.1. Unique primary DNS domains](#unique-primary-dns-domains) {#unique-primary-dns-domains .title}

For a successful Identity Management (IdM) to Active Directory (AD) trust, each environment must occupy a unique, dedicated DNS domain and Kerberos realm. This separation allows Active Directory to route authentication requests correctly via name suffix routing.

Each system must have its own unique primary DNS domain configured. For example:

-   *`ad.example.com`{.literal}* for AD and *`idm.example.com`{.literal}* for IdM
-   *`example.com`{.literal}* for AD and *`idm.example.com`{.literal}* for IdM
-   *`ad.example.com`{.literal}* for AD and *`example.com`{.literal}* for IdM

The most convenient management solution is an environment where each DNS domain is managed by integrated DNS servers, but it is possible to use any other standard-compliant DNS server as well.

Kerberos realm names as upper-case versions of primary DNS domain names
:   Kerberos realm names must match the primary DNS domain names, with all letters uppercase. For example, if the domain names are *`ad.example.com`{.literal}* for AD and *`idm.example.com`{.literal}* for IdM, the Kerberos realm names are required to be *`AD.EXAMPLE.COM`{.literal}* and *`IDM.EXAMPLE.COM`{.literal}*.

DNS records resolvable from all DNS domains in the trust
:   All machines must resolve DNS records from all DNS domains involved in the trust relationship.

IdM and AD DNS Domains
:   Systems joined to IdM can be distributed over multiple DNS domains. Deploy IdM clients in a DNS zone separate from those managed by Active Directory. The primary IdM DNS domain must have proper SRV records to support AD trusts.

Note

In some environments with trusts between IdM and AD, you can install an IdM client on a host that is part of the Active Directory DNS domain. The host can then benefit from the Linux-focused features of IdM. This is not a recommended configuration and has some limitations.

You can acquire a list of the required SRV records specific to your system configuration by running the following command:

``` {.language-plaintext tabindex="-1"}
$ ipa dns-update-system-records --dry-run
```

The generated list can look for example like this:

``` {.language-plaintext tabindex="-1"}
IPA DNS records:
  _kerberos-master._tcp.idm.example.com. 86400 IN SRV 0 100 88 server.idm.example.com.
  _kerberos-master._udp.idm.example.com. 86400 IN SRV 0 100 88 server.idm.example.com.
  _kerberos._tcp.idm.example.com. 86400 IN SRV 0 100 88 server.idm.example.com.
  _kerberos._tcp.idm.example.com. 86400 IN SRV 0 100 88 server.idm.example.com.
  _kerberos.idm.example.com. 86400 IN TXT "IDM.EXAMPLE.COM"
  _kpasswd._tcp.idm.example.com. 86400 IN SRV 0 100 464 server.idm.example.com.
  _kpasswd._udp.idm.example.com. 86400 IN SRV 0 100 464 server.idm.example.com.
  _ldap._tcp.idm.example.com. 86400 IN SRV 0 100 389 server.idm.example.com.
  _ipa-ca.idm.example.com. 86400 IN A 192.168.122.2
```

For other DNS domains that are part of the same IdM realm, it is not required for the SRV records to be configured when the trust to AD is configured. The reason is that AD domain controllers do not use SRV records to discover KDCs but rather base the KDC discovery on name suffix routing information for the trust.

**Additional resources**

-   [Configuring IdM clients in an Active Directory DNS domain](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_trust_between_idm_and_ad/configuring-idm-clients-in-an-active-directory-dns-domain)

### [7.2. Configuring a DNS forward zone in the IdM Web UI](#configuring-a-dns-forward-zone-in-the-idm-web-ui) {#configuring-a-dns-forward-zone-in-the-idm-web-ui .title}

Use the Identity Management (IdM) Web UI to configure DNS forward zones. This allows the IdM server to route queries for external domains, such as an Active Directory environment, to their respective DNS servers.

**Prerequisites**

-   Access to the IdM Web UI with a user account that has administrator rights.
-   Correctly configured DNS server.

**Procedure**

1.  Log in to the IdM Web UI with administrator privileges.

2.  Click the **Network Services** tab.

3.  Click the **DNS** tab.

4.  In the drop down menu, click **DNS Forward Zones**.

5.  Click the **Add** button.

6.  In the **Add DNS forward zone** dialog box, add a zone name.

7.  In the **Zone forwarders** item, click the **Add** button.

8.  In the **Zone forwarders** field, add the IP address of the server for which you want to create the forward zone.

9.  Click the **Add** button.

    The forwarded zone has been added to the DNS settings and you can verify it in the DNS Forward Zones settings. The Web UI informs you about success with the following pop-up message: **DNS Forward Zone successfully added.**

    Note

    After adding a forward zone to the configuration, the Web UI might display a warning about a DNSSEC validation failure.

    DNSSEC (Domain Name System Security Extensions) secures DNS data with a digital signature to protect DNS from attacks. This service is enabled by default in the IdM server. The warning appears because the remote DNS server does not use DNSSEC. Enable DNSSEC on the remote DNS server.

    If you cannot enable DNSSEC validation on the remote server, you can disable DNSSEC in the IdM server:

    1.  Open the `/etc/named/ipa-options-ext.conf`{.literal} file on your IdM server.

    2.  Add the following DNSSEC parameters:

        ``` {.language-plaintext tabindex="-1"}
        dnssec-validation no;
        ```

    3.  Save and close the configuration file.

    4.  Restart the DNS service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart named
        ```

    Note that DNSSEC is only available as Technology Preview in IdM.

**Verification**

-   Use the `nslookup`{.literal} command with the name of the remote DNS server:

    ``` {.language-plaintext tabindex="-1"}
    $ nslookup ad.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    Server:        192.168.122.2
    Address:       192.168.122.2#53

    No-authoritative answer:
    Name:          ad.example.com
    Address:       192.168.122.3
    ```

    If you configured the domain forwarding correctly, the IP address of the remote DNS server is displayed.

**Additional resources**

-   [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser)

### [7.3. Configuring a DNS forward zone in the CLI](#configuring-a-dns-forward-zone-in-the-cli) {#configuring-a-dns-forward-zone-in-the-cli .title}

Use the Identity Management (IdM) CLI to configure DNS forward zones. This allows the IdM server to route queries for external domains, such as an Active Directory environment, to their respective DNS servers.

**Prerequisites**

-   Access to the CLI with a user account that has administrator rights.
-   Correctly configured DNS server.

**Procedure**

-   Create a DNS forward zone for the AD domain, and specify the IP address of the remote DNS server with the `--forwarder`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    # ipa dnsforwardzone-add ad.example.com --forwarder=192.168.122.3 --forward-policy=first
    ```

    Note

    You might see a warning about a DNSSEC validation failure in the `/var/log/messages`{.literal} system logs after adding a new forward zone to the configuration:

    ``` {.language-plaintext tabindex="-1"}
    named[2572]: no valid DS resolving 'host.ad.example.com/A/IN':  192.168.100.25#53
    ```

    DNSSEC (Domain Name System Security Extensions) secures DNS data with a digital signature to protect DNS from attacks. This service is enabled by default in the IdM server. The warning appears because the remote DNS server does not use DNSSEC. Enable DNSSEC on the remote DNS server.

    If you cannot enable DNSSEC validation on the remote server, you can disable DNSSEC in the IdM server:

    1.  Open the `/etc/named/ipa-options-ext.conf`{.literal} file on your IdM server.

    2.  Add the following DNSSEC parameters:

        ``` {.language-plaintext tabindex="-1"}
        dnssec-validation no;
        ```

    3.  Save and close the configuration file.

    4.  Restart the DNS service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart named
        ```

    Note that DNSSEC is only available as Technology Preview in IdM.

**Verification**

-   Use the `nslookup`{.literal} command with the name of the remote DNS server:

    ``` {.language-plaintext tabindex="-1"}
    $ nslookup ad.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    Server:        192.168.122.2
    Address:       192.168.122.2#53

    No-authoritative answer:
    Name:          ad.example.com
    Address:       192.168.122.3
    ```

    If the domain forwarding is configured correctly, the `nslookup`{.literal} request displays an IP address of the remote DNS server.

### [7.4. Configuring DNS forwarding in AD](#configuring-dns-forwarding-in-ad) {#configuring-dns-forwarding-in-ad .title}

Configure a conditional forwarder in Active Directory (AD) to enable the Windows environment to resolve the Identity Management (IdM) domain. This is essential for AD to locate IdM Kerberos and LDAP services.

**Prerequisites**

-   Windows Server with AD installed.
-   DNS port open on both servers.

**Procedure**

1.  Log in to the Windows Server.

2.  Open **Server Manager**.

3.  Open **DNS Manager**.

4.  In **Conditional Forwarders**, add a new forwarder and enter:

    -   DNS Domain: The fully qualified domain name, for example, *`server.idm.example.com`{.literal}*
    -   IP Address: The IP address of the IdM DNS server.

5.  Save the settings.

### [7.5. Verifying the DNS configuration](#verifying-the-dns-configuration) {#verifying-the-dns-configuration .title}

Verify that both Identity Management (IdM) and Active Directory (AD) can resolve their own service records and those of the peer domain. Ensure successful bidirectional resolution before establishing the trust relationship.

**Prerequisites**

-   You are logged in with an account that has `sudo`{.literal} permissions.

**Procedure**

1.  Run a DNS query for the Kerberos over UDP and LDAP over TCP service records.

    ``` {.language-plaintext tabindex="-1"}
    [admin@server ~]# dig +short -t SRV _kerberos._udp.idm.example.com.
    ```

    ``` {.language-plaintext tabindex="-1"}
    0 100 88 server.idm.example.com.
    ```

    ``` {.language-plaintext tabindex="-1"}
    [admin@server ~]# dig +short -t SRV _ldap._tcp.idm.example.com.
    ```

    ``` {.language-plaintext tabindex="-1"}
    0 100 389 server.idm.example.com.
    ```

    The commands return the SRV records for the IdM servers.

2.  Run a DNS query for the TXT record with the IdM Kerberos realm name. The returned value should match the Kerberos realm you specified when installing IdM.

    ``` {.language-plaintext tabindex="-1"}
    [admin@server ~]# dig +short -t TXT _kerberos.idm.example.com.
    ```

    ``` {.language-plaintext tabindex="-1"}
    "IDM.EXAMPLE.COM"
    ```

    If the previous steps did not return all the expected records, update the DNS configuration with the missing records:

    -   If your IdM environment uses an integrated DNS server, enter the `ipa dns-update-system-records`{.literal} command without any options to update your system records:

        ``` {.language-plaintext tabindex="-1"}
        [admin@server ~]$ ipa dns-update-system-records
        ```

    -   If your IdM environment does not use an integrated DNS server:

        1.  On the IdM server, export the IdM DNS records into a file:

            ``` {.language-plaintext tabindex="-1"}
            [admin@server ~]$ ipa dns-update-system-records --dry-run --out dns_records_file.nsupdate
            ```

            The command creates a file named **dns_records_file.nsupdate** with the relevant IdM DNS records.

        2.  Submit a DNS update request to your DNS server using the `nsupdate`{.literal} utility and the `dns_records_file.nsupdate`{.literal} file. For more information, see [Updating External DNS Records Using nsupdate](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/linux_domain_identity_authentication_and_policy_guide/dns-updates-external#dns-update-external-nsupdate) in RHEL 7 documentation. Alternatively, refer to your DNS server documentation for adding DNS records.

3.  Verify that IdM is able to resolve service records for AD with a command that runs a DNS query for Kerberos and LDAP over TCP service records:

    ``` {.language-plaintext tabindex="-1"}
    [admin@server ~]# dig +short -t SRV _kerberos._tcp.dc._msdcs.ad.example.com.
    ```

    ``` {.language-plaintext tabindex="-1"}
    0 100 88 addc1.ad.example.com.
    ```

    ``` {.language-plaintext tabindex="-1"}
    [admin@server ~]# dig +short -t SRV _ldap._tcp.dc._msdcs.ad.example.com.
    ```

    ``` {.language-plaintext tabindex="-1"}
    0 100 389 addc1.ad.example.com.
    ```

## [Chapter 8. Configuring IdM clients in an Active Directory DNS domain](#configuring-idm-clients-in-an-active-directory-dns-domain) {#chapter-8.-configuring-idm-clients-in-an-active-directory-dns-domain .title}

While IdM clients should ideally reside in a separate DNS zone, you can join clients located in an Active Directory (AD) DNS domain to IdM. This enables RHEL-specific features for hosts within the AD namespace.

Important

This configuration is not recommended and has limitations. Always deploy IdM clients in a DNS zone separate from the ones owned by AD and access IdM clients using their IdM host names.

Your IdM client configuration depends on whether you require single sign-on with Kerberos.

### [8.1. Configuring an IdM client without Kerberos single sign-on](#configuring-an-idm-client-without-kerberos-single-sign-on) {#configuring-an-idm-client-without-kerberos-single-sign-on .title}

When an IdM client resides in an Active Directory (AD) DNS domain, password-based authentication is the only supported authentication method. Join the client to the IdM realm manually without Kerberos single sign-on.

**Procedure**

1.  Install the IdM client with the `--domain=IPA_DNS_Domain`{.literal} option to ensure the System Security Services Daemon (SSSD) can communicate with the IdM servers:

    ``` {.language-plaintext tabindex="-1"}
    [root@idm-client.ad.example.com ~]# ipa-client-install --domain=idm.example.com
    ```

    This option disables the SRV record auto-detection for the Active Directory DNS domain.

2.  Open the `/etc/krb5.conf`{.literal} configuration file and locate the existing mapping for the Active Directory domain in the `[domain_realm]`{.literal} section.

    ``` {.language-plaintext tabindex="-1"}
    .ad.example.com = IDM.EXAMPLE.COM
    ad.example.com = IDM.EXAMPLE.COM
    ```

3.  Replace both lines with an entry mapping the fully qualified domain name (FQDN) of the Linux clients in the Active Directory DNS zone to the IdM realm:

    ``` {.language-plaintext tabindex="-1"}
    idm-client.ad.example.com = IDM.EXAMPLE.COM
    ```

    By replacing the default mapping, you prevent Kerberos from sending its requests for the Active Directory domain to the IdM Kerberos Distribution Center (KDC). Instead Kerberos uses auto-discovery through SRV DNS records to locate the KDC.

### [8.2. Requesting SSL certificates without single sign-on](#requesting-ssl-certificates-without-single-sign-on) {#requesting-ssl-certificates-without-single-sign-on .title}

Request SSL certificates using `certmonger`{.literal} for Identity Management (IdM) clients without Kerberos SSO to enable secure SSL-based services.

After you configure an IdM client without Kerberos single sign-on, you can configure SSL-based services.

SSL-based services require a certificate with `dNSName`{.literal} extension records that cover all system host names, because both original (A/AAAA) and CNAME records must be in the certificate. Currently, IdM only issues certificates to host objects in the IdM database.

In this configuration, where single sign-on is not enabled, IdM already contains a host object for the FQDN in its database. You can use `certmonger`{.literal} to request a certificate using the FQDN.

**Prerequisites**

-   An IdM client configured without Kerberos single-sign on.

**Procedure**

-   Use `certmonger`{.literal} to request a certificate using the FQDN:

    ``` {.language-plaintext tabindex="-1"}
    [root@idm-client.ad.example.com ~]# ipa-getcert request -r \
          -f /etc/httpd/alias/server.crt \
          -k /etc/httpd/alias/server.key \
          -N CN=ipa-client.ad.example.com \
          -D ipa-client.ad.example.com \
          -K host/idm-client.ad.example.com@IDM.EXAMPLE.COM \
          -U id-kp-serverAuth
    ```

    The `certmonger`{.literal} service uses the default host key stored in the `/etc/krb5.keytab`{.literal} file to authenticate to the IdM Certificate Authority (CA).

### [8.3. Configuring an IdM client with Kerberos single sign-on](#configuring-an-idm-client-with-kerberos-single-sign-on) {#configuring-an-idm-client-with-kerberos-single-sign-on .title}

To enable Kerberos single sign-on (SSO) for IdM clients across DNS domains, you must map a CNAME record from the Active Directory (AD) domain to the IdM client's A/AAAA record and configure the client to allow flexible principal acceptance.

For Kerberos-based application servers, MIT Kerberos supports a method to allow the acceptance of any host-based principal available in the application's keytab.

**Procedure**

1.  Configure Kerberos by editing the `/etc/krb5.conf`{.literal} file on the IdM client. In the `[libdefaults]`{.literal} section, set `ignore_acceptor_hostname`{.literal} to `true`{.literal}. This allows the application to accept any host-based principal in its keytab:

    ``` {.language-plaintext tabindex="-1"}
    ignore_acceptor_hostname = true
    ```

2.  Ensure a CNAME record exists in the Active Directory DNS, for example `idm-client.ad.example.com`{.literal}, pointing to the IdM client's A/AAAA record in the IdM DNS domain.

### [8.4. Requesting SSL certificates with single sign-on](#requesting-ssl-certificates-with-single-sign-on) {#requesting-ssl-certificates-with-single-sign-on .title}

To secure services using Kerberos SSO, your SSL certificate must include both the host's A/AAAA and CNAME records. Since IdM only issues certificates to database host objects, you must manually create and link a host entry for the CNAME alias.

Create a host object for `ipa-client.example.com`{.literal} in IdM and make sure the real IdM machine's host object is able to manage this host.

**Prerequisites**

-   You have disabled the strict checks on what Kerberos principal is used to target the Kerberos server.

**Procedure**

1.  On the IdM server, create a host entry for the AD-side alias. Use `--force`{.literal} because the name resolves to a CNAME rather than an A/AAAA record.

    ``` {.language-plaintext tabindex="-1"}
    [root@idm-server.idm.example.com ~]# ipa host-add idm-client.ad.example.com --force
    ```

2.  To allow the physical IdM host to manage the new alias entry in the IdM database, grant management permissions to the host.

    ``` {.language-plaintext tabindex="-1"}
    [root@idm-server.idm.example.com ~]# ipa host-add-managedby idm-client.ad.example.com \
          --hosts=idm-client.idm.example.com
    ```

3.  On the IdM client, use `ipa-getcert`{.literal} to request the certificate. Ensure that you include both the FQDN and the CNAME using the `-D`{.literal} flags.

    ``` {.language-plaintext tabindex="-1"}
    [root@idm-client.idm.example.com ~]# ipa-getcert request -r \
          -f /etc/httpd/alias/server.crt \
          -k /etc/httpd/alias/server.key \
          -N CN=`hostname --fqdn` \
          -D `hostname --fqdn` \
          -D idm-client.ad.example.com \
          -K host/idm-client.idm.example.com@IDM.EXAMPLE.COM \
          -U id-kp-serverAuth
    ```

    In SSL/TLS, the client checks the Subject Alternative Name (SAN) field. By using -D twice, you are populating that SAN field with both names so that no matter which URL the user hits, the certificate remains valid.

## [Chapter 9. Setting up a trust](#setting-up-a-trust) {#chapter-9.-setting-up-a-trust .title}

Establishing a trust between Identity Management (IdM) and Active Directory (AD) enables seamless cross-platform resource access. Learn how to prepare the IdM domain, configure trust agreements using the CLI, Web UI, or Ansible, and verify cross-realm Kerberos authentication.

### [9.1. Prerequisites](#prerequisites) {#prerequisites .title}

-   DNS is correctly configured. Both IdM and AD servers must be able to resolve each other names.
-   Supported versions of AD and IdM are deployed.
-   You have obtained a Kerberos ticket.

**Additional resources**

-   [Configuring DNS and realm settings for a trust](#unique-primary-dns-domains "7.1. Unique primary DNS domains")
-   [Supported versions of Windows Server](#supported-versions-of-windows-server "Chapter 2. Supported versions of Windows Server")
-   [Using kinit to log in to IdM manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-idm-in-the-web-ui-using-a-kerberos-ticket#using-kinit-to-log-in-to-idm-manually_login-web-ui-krb)

### [9.2. Preparing the IdM server for the trust](#preparing-the-idm-server-for-the-trust) {#preparing-the-idm-server-for-the-trust .title}

Before you can establish a trust with AD, you must prepare the IdM domain using the `ipa-adtrust-install`{.literal} utility on an IdM server.

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

8.  Make sure that DNS is properly configured, as described in [Verifying the DNS configuration for a trust](#verifying-the-dns-configuration "7.5. Verifying the DNS configuration").

    Important

    Red Hat strongly recommends you verify the DNS configuration as described in [Verifying the DNS configuration for a trust](#verifying-the-dns-configuration "7.5. Verifying the DNS configuration") every time after running `ipa-adtrust-install`{.literal}, especially if IdM or AD do not use integrated DNS servers.

9.  Restart the `ipa`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# ipactl restart
    ```

10. Use the `smbclient`{.literal} utility to verify that Samba responds to Kerberos authentication from the IdM side:

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

### [9.3. Setting up a trust agreement using the command line](#setting-up-a-trust-agreement-using-the-command-line) {#setting-up-a-trust-agreement-using-the-command-line .title}

Use the command line to establish a trust between Identity Management (IdM) and Active Directory (AD). IdM supports one-way, two-way, and external forest trusts, allowing you to control how users access resources across domains using the `ipa trust-add`{.literal} utility.

-   **One-way trust** --- default option. One-way trust enables Active Directory (AD) users and groups to access resources in IdM, but not the other way around. The IdM domain trusts the AD forest, but the AD forest does not trust the IdM domain.

-   **Two-way trust** --- Two-way trust enables AD users and groups to access resources in IdM.

    You must configure a two-way trust for solutions such as Microsoft SQL Server that expect the `S4U2Self`{.literal} and `S4U2Proxy`{.literal} Microsoft extensions to the Kerberos protocol to work over a trust boundary. An application on a RHEL IdM host might request `S4U2Self`{.literal} or `S4U2Proxy`{.literal} information from an Active Directory domain controller about an AD user, and a two-way trust provides this feature.

    Note that this two-way trust functionality does not allow IdM users to login to Windows systems, and the two-way trust in IdM does not give the users any additional rights compared to the one-way trust solution in AD.

    -   To create the two-way trust, add the following option to the command: `--two-way=true`{.literal}

-   **External trust** - a trust relationship between IdM and an AD domain in different forests. While a forest trust always requires establishing a trust between IdM and the root domain of an Active Directory forest, an external trust can be established from IdM to a domain within a forest. This is only recommended if it is not possible to establish a forest trust between forest root domains due to administrative or organizational reasons.

    -   To create the external trust, add the following option to the command: `--external=true`{.literal}

The steps below show you how to create a one-way trust agreement.

**Prerequisites**

-   User name and password of a Windows administrator.
-   You have [prepared the IdM server for the trust](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/installing_trust_between_idm_and_ad/index#preparing-the-idm-server-for-the-trust_setting-up-a-trust).

**Procedure**

-   Create a trust agreement for the AD domain and the IdM domain by using the `ipa trust-add`{.literal} command:

    -   To have SSSD automatically generate UIDs and GIDs for AD users based on their SID, create a trust agreement with the `Active Directory domain`{.literal} ID range type. This is the most common configuration.

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa trust-add --type=ad ad.example.com --admin <ad_admin_username> --password --range-type=ipa-ad-trust
        ```

    -   If you have configured POSIX attributes for your users in Active Directory (such as `uidNumber`{.literal} and `gidNumber`{.literal}) and you want SSSD to process this information, create a trust agreement with the `Active Directory domain with POSIX attributes`{.literal} ID range type:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa trust-add --type=ad ad.example.com --admin <ad_admin_username> --password --range-type=ipa-ad-trust-posix
        ```

        Warning

        If you do not specify an ID Range type when creating a trust, IdM attempts to automatically select the appropriate range type by requesting details from AD domain controllers in the forest root domain. If IdM does not detect any POSIX attributes, the trust installation script selects the `Active Directory domain`{.literal} ID range.

        If IdM detects any POSIX attributes in the forest root domain, the trust installation script selects the `Active Directory domain with POSIX attributes`{.literal} ID range and assumes that UIDs and GIDs are correctly defined in AD. If POSIX attributes are not correctly set in AD, you will not be able to resolve AD users.

        For example, if the users and groups that need access to IdM systems are not part of the forest root domain, but instead are located in a child domain of the forest domain, the installation script might not detect the POSIX attributes defined in the child AD domain. In this case, explicitly choose the POSIX ID range type when establishing the trust.

### [9.4. Setting up a trust agreement in the IdM Web UI](#setting-up-a-trust-agreement-in-the-idm-web-ui) {#setting-up-a-trust-agreement-in-the-idm-web-ui .title}

To enable Active Directory (AD) users to authenticate and access resources, you can establish a cross-forest trust by using the Identity Management (IdM) Web UI. This configuration ensures that both domains correctly resolve identities and share resources.

**Prerequisites**

-   DNS is correctly configured. Both IdM and AD servers must be able to resolve each other names.
-   Supported versions of AD and IdM are deployed.
-   You have obtained a Kerberos ticket.
-   Before creating a trust in the Web UI, prepare the IdM server for the trust as described in: [Setting up a trust](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_trust_between_idm_and_ad/setting-up-a-trust).
-   You are logged in as an IdM administrator. For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

**Procedure**

1.  In the IdM Web UI, click the **IPA Server** tab.

2.  In the **IPA Server** tab, click the **Trusts** tab.

3.  In the drop down menu, select the **Trusts** option.

4.  Click the **Add** button.

5.  In the **Add Trust** dialog box, enter the name of the Active Directory domain.

6.  In the **Account** and **Password** fields, add the administrator credentials of the Active Directory administrator.

7.  Optional: Select **Two-way trust**, if you want to enable AD users and groups to access resources in IdM. However, the two-way trust in IdM does not give the users any additional rights compared to the one-way trust solution in AD. Both solutions are considered equally secure because of default cross-forest trust SID filtering settings.

8.  Optional: Select **External trust** if you are configuring a trust with an AD domain that is not the root domain of an AD forest. While a forest trust always requires establishing a trust between IdM and the root domain of an Active Directory forest, you can establish an external trust from IdM to any domain within an AD forest.

9.  Optional: By default, the trust installation script tries to detect the appropriate ID range type. You can also explicitly set the ID range type by choosing one of the following options:

    a.  To have SSSD automatically generate UIDs and GIDs for AD users based on their SID, select the `Active Directory domain`{.literal} ID range type. This is the most common configuration.

    b.  If you have configured POSIX attributes for your users in Active Directory (such as `uidNumber`{.literal} and `gidNumber`{.literal}) and you want SSSD to process this information, select the `Active Directory domain with POSIX attributes`{.literal} ID range type.

        Warning

        If you leave the **Range type** setting on the default `Detect`{.literal} option, IdM attempts to automatically select the appropriate range type by requesting details from AD domain controllers in the forest root domain. If IdM does not detect any POSIX attributes, the trust installation script selects the `Active Directory domain`{.literal} ID range.

        If IdM detects any POSIX attributes in the forest root domain, the trust installation script selects the `Active Directory domain with POSIX attributes`{.literal} ID range and assumes that UIDs and GIDs are correctly defined in AD. If POSIX attributes are not correctly set in AD, you will not be able to resolve AD users.

        For example, if the users and groups that need access to IdM systems are not part of the forest root domain, but instead are located in a child domain of the forest domain, the installation script might not detect the POSIX attributes defined in the child AD domain. In this case, explicitly choose the POSIX ID range type when establishing the trust.

10. Click **Add**.

**Verification**

-   If the trust has been successfully added to the IdM server, you can see the green pop-up window in the IdM Web UI. It means that the:

    -   Domain name exists

    -   User name and password of the Windows Server has been added correctly.

Now you can continue to test the trust connection and Kerberos authentication.

### [9.5. Setting up a trust agreement using Ansible](#setting-up-a-trust-agreement-using-ansible) {#setting-up-a-trust-agreement-using-ansible .title}

To automate the creation of trust agreements between Identity Management (IdM) and Active Directory (AD), use the `ansible-freeipa`{.literal} package in Ansible playbooks.

You can configure three types of trust agreements:

-   **One-way trust** --- default option. One-way trust enables Active Directory (AD) users and groups to access resources in IdM, but not the other way around. The IdM domain trusts the AD forest, but the AD forest does not trust the IdM domain.

-   **Two-way trust** --- Two-way trust enables AD users and groups to access resources in IdM.

    You must configure a two-way trust for solutions such as Microsoft SQL Server that expect the `S4U2Self`{.literal} and `S4U2Proxy`{.literal} Microsoft extensions to the Kerberos protocol to work over a trust boundary. An application on a RHEL IdM host might request `S4U2Self`{.literal} or `S4U2Proxy`{.literal} information from an Active Directory domain controller about an AD user, and a two-way trust provides this feature.

    Note that this two-way trust functionality does not allow IdM users to login to Windows systems, and the two-way trust in IdM does not give the users any additional rights compared to the one-way trust solution in AD.

    -   To create the two-way trust, add the following variable to the playbook task below: `two_way: true`{.literal}

-   **External trust** - a trust relationship between IdM and an AD domain in different forests. While a forest trust always requires establishing a trust between IdM and the root domain of an Active Directory forest, an external trust can be established from IdM to a domain within a forest. This is only recommended if it is not possible to establish a forest trust between forest root domains due to administrative or organizational reasons.

    -   To create the external trust, add the following variable to the playbook task below: `external: true`{.literal}

**Prerequisites**

-   User name and password of a Windows administrator.

-   The IdM `admin`{.literal} password.

-   You have [prepared the IdM server for the trust](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_trust_between_idm_and_ad/setting-up-a-trust).

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to your **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Select one of the following scenarios based on your use case:

    -   To create an ID mapping trust agreement, in which SSSD automatically generates UIDs and GIDs for AD users and groups based on their SIDs, create an `add-trust.yml`{.literal} playbook with the following content:

        ``` {.language-plaintext tabindex="-1"}
        ---
        - name: Playbook to create a trust
          hosts: ipaserver

          vars_files:
          - /home/user_name/MyPlaybooks/secret.yml
          tasks:
            - name: ensure the trust is present
              ipatrust:
                ipaadmin_password: "{{ ipaadmin_password }}"
                realm: ad.example.com
                admin: Administrator
                password: secret_password
                state: present
        ```

        In the example:

        -   `realm`{.literal} defines the AD realm name string.
        -   `admin`{.literal} defines the AD domain administrator string.
        -   `password`{.literal} defines the AD domain administrator's password string.

    -   To create a POSIX trust agreement, in which SSSD processes POSIX attributes stored in AD, such as `uidNumber`{.literal} and `gidNumber`{.literal}, create an `add-trust.yml`{.literal} playbook with the following content:

        ``` {.language-plaintext tabindex="-1"}
        ---
        - name: Playbook to create a trust
          hosts: ipaserver

          vars_files:
          - /home/user_name/MyPlaybooks/secret.yml
          tasks:
            - name: ensure the trust is present
              ipatrust:
                ipaadmin_password: "{{ ipaadmin_password }}"
                realm: ad.example.com
                admin: Administrator
                password: secret_password
                range_type: ipa-ad-trust-posix
                state: present
        ```

    -   To create a trust agreement in which IdM attempts to automatically select the appropriate range type, `ipa-ad-trust`{.literal} or `ipa-ad-trust-posix`{.literal}, by requesting details from AD domain controllers in the forest root domain, create an `add-trust.yml`{.literal} playbook with the following content:

        ``` {.language-plaintext tabindex="-1"}
        ---
        - name: Playbook to create a trust
          hosts: ipaserver

          vars_files:
          - /home/user_name/MyPlaybooks/secret.yml
          tasks:
            - name: ensure the trust is present
              ipatrust:
                ipaadmin_password: "{{ ipaadmin_password }}"
                realm: ad.example.com
                admin: Administrator
                password: secret_password
                state: present
        ```

    Warning

    If you do not specify an ID range type when creating a trust, and if IdM does not detect any POSIX attributes in the AD forest root domain, the trust installation script selects the `Active Directory domain`{.literal} ID range.

    If IdM detects any POSIX attributes in the forest root domain, the trust installation script selects the `Active Directory domain with POSIX attributes`{.literal} ID range and assumes that UIDs and GIDs are correctly defined in AD.

    However, if POSIX attributes are not correctly set in AD, you will not be able to resolve AD users. For example, if the users and groups that need access to IdM systems are not part of the forest root domain, but instead are located in a child domain of the forest domain, the installation script might not detect the POSIX attributes defined in the child AD domain. In this case, explicitly choose the POSIX ID range type when establishing the trust.

3.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-trust.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/trust`{.literal} directory on the control node.

4.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory add-trust.yml
    ```

### [9.6. Verifying the Kerberos configuration](#verifying-the-kerberos-configuration) {#verifying-the-kerberos-configuration .title}

Verify the cross-realm trust by confirming that an Active Directory (AD) user can successfully obtain a Kerberos ticket-granting ticket (TGT) and access services within the IdM domain.

**Procedure**

1.  Request a ticket for an Active Directory (AD) user:

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# kinit user@AD.EXAMPLE.COM
    ```

2.  Request service tickets for a service within the IdM domain:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# kvno -S host server.idm.example.com
    ```

    If the AD service ticket is successfully granted, there is a cross-realm ticket-granting ticket (TGT) listed with all of the other requested tickets. The TGT is named krbtgt/IPA.DOMAIN@AD.DOMAIN.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ]# klist
    ```

    ``` {.language-plaintext tabindex="-1"}
    Ticket cache: KEYRING:persistent:0:krb_ccache_hRtox00
    Default principal: user@AD.EXAMPLE.COM

    Valid starting       Expires              Service principal
    03.05.2016 18:31:06  04.05.2016 04:31:01  host/server.idm.example.com@IDM.EXAMPLE.COM
        renew until 04.05.2016 18:31:00
    03.05.2016 18:31:06 04.05.2016 04:31:01 krbtgt/IDM.EXAMPLE.COM@AD.EXAMPLE.COM
        renew until 04.05.2016 18:31:00
    03.05.2016 18:31:01  04.05.2016 04:31:01  krbtgt/AD.EXAMPLE.COM@AD.EXAMPLE.COM
        renew until 04.05.2016 18:31:00
    ```

    The `localauth`{.literal} plug-in maps Kerberos principals to local SSSD user names. This allows AD users to use Kerberos authentication and access Linux services, which support GSSAPI authentication directly.

### [9.7. Verifying the trust configuration on IdM](#verifying-the-trust-configuration-on-idm) {#verifying-the-trust-configuration-on-idm .title}

Ensure the Identity Management (IdM) and Active Directory (AD) environments are correctly integrated by verifying that both systems can resolve the necessary SRV service records for Kerberos and LDAP.

**Prerequisites**

-   You need to be logged in with administrator privileges.

**Procedure**

1.  Run a DNS query for the MS DC Kerberos over UDP and LDAP over TCP service records.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dig +short -t SRV _kerberos._udp.dc._msdcs.idm.example.com.
    ```

    ``` {.language-plaintext tabindex="-1"}
    0 100 88 server.idm.example.com.
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dig +short -t SRV _ldap._tcp.dc._msdcs.idm.example.com.
    ```

    ``` {.language-plaintext tabindex="-1"}
    0 100 389 server.idm.example.com.
    ```

    These commands list all IdM servers on which `ipa-adtrust-install`{.literal} has been executed. The output is empty if `ipa-adtrust-install`{.literal} has not been executed on any IdM server, which is typically before establishing the first trust relationship.

2.  Run a DNS query for the Kerberos and LDAP over TCP service records to verify that IdM is able to resolve service records for AD:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# dig +short -t SRV _kerberos._tcp.dc._msdcs.ad.example.com.
    ```

    ``` {.language-plaintext tabindex="-1"}
    0 100 88 addc1.ad.example.com.
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# dig +short -t SRV _ldap._tcp.dc._msdcs.ad.example.com.
    ```

    ``` {.language-plaintext tabindex="-1"}
    0 100 389 addc1.ad.example.com.
    ```

### [9.8. Verifying the trust configuration on AD](#verifying-the-trust-configuration-on-ad) {#verifying-the-trust-configuration-on-ad .title}

Use the `nslookup.exe`{.literal} utility on the Active Directory (AD) server to verify that IdM service records, including SRV and TXT types, are correctly resolvable to ensure proper communication between the two realms.

**Prerequisites**

-   You need to be logged in with administrator privileges.

**Procedure**

1.  On the AD server, set the `nslookup.exe`{.literal} utility to look up service records.

    ``` {.language-plaintext tabindex="-1"}
    C:\>nslookup.exe
    > set type=SRV
    ```

2.  Enter the domain name for the Kerberos over UDP and LDAP over TCP service records.

    ``` {.language-plaintext tabindex="-1"}
    > _kerberos._udp.idm.example.com.
    _kerberos._udp.idm.example.com.       SRV service location:
        priority                = 0
        weight                  = 100
        port                    = 88
        svr hostname   = server.idm.example.com
    > _ldap._tcp.idm.example.com
    _ldap._tcp.idm.example.com       SRV service location:
        priority                = 0
        weight                  = 100
        port                    = 389
        svr hostname   = server.idm.example.com
    ```

3.  Change the service type to TXT and run a DNS query for the TXT record with the IdM Kerberos realm name.

    ``` {.language-plaintext tabindex="-1"}
    C:\>nslookup.exe
    > set type=TXT
    > _kerberos.idm.example.com.
    _kerberos.idm.example.com.        text =

        "IDM.EXAMPLE.COM"
    ```

4.  Run a DNS query for the MS DC Kerberos over UDP and LDAP over TCP service records.

    ``` {.language-plaintext tabindex="-1"}
    C:\>nslookup.exe
    > set type=SRV
    > _kerberos._udp.dc._msdcs.idm.example.com.
    _kerberos._udp.dc._msdcs.idm.example.com.        SRV service location:
        priority = 0
        weight = 100
        port = 88
        svr hostname = server.idm.example.com
    > _ldap._tcp.dc._msdcs.idm.example.com.
    _ldap._tcp.dc._msdcs.idm.example.com.        SRV service location:
        priority = 0
        weight = 100
        port = 389
        svr hostname = server.idm.example.com
    ```

    Active Directory only expects to discover domain controllers that can respond to AD-specific protocol requests, such as other AD domain controllers and IdM trust controllers. Use the `ipa-adtrust-install`{.literal} tool to promote an IdM server to a trust controller, and you can verify which servers are trust controllers with the `ipa server-role-find --role 'AD trust controller'`{.literal} command.

5.  Verify that AD services are resolvable from the AD server.

    ``` {.language-plaintext tabindex="-1"}
    C:\>nslookup.exe
    > set type=SRV
    ```

6.  Enter the domain name for the Kerberos over UDP and LDAP over TCP service records.

    ``` {.language-plaintext tabindex="-1"}
    > _kerberos._udp.dc._msdcs.ad.example.com.
    _kerberos._udp.dc._msdcs.ad.example.com.    SRV service location:
        priority = 0
        weight = 100
        port = 88
        svr hostname = addc1.ad.example.com
    > _ldap._tcp.dc._msdcs.ad.example.com.
    _ldap._tcp.dc._msdcs.ad.example.com.    SRV service location:
        priority = 0
        weight = 100
        port = 389
        svr hostname = addc1.ad.example.com
    ```

### [9.9. Creating a trust agent](#creating-a-trust-agent) {#creating-a-trust-agent .title}

A trust agent is an Identity Management (IdM) server that performs identity lookups against Active Directory (AD) domain controllers without being a full AD trust controller.

**Prerequisites**

-   IdM is installed with an Active Directory trust.
-   The `sssd-tools`{.literal} package is installed.

**Procedure**

1.  On an existing trust controller, run the `ipa-adtrust-install --add-agents`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    [root@existing_trust_controller]# ipa-adtrust-install --add-agents
    ```

    The command starts an interactive configuration session and prompts you for the information required to configure the agent.

2.  Restart the IdM service on the trust agent.

    ``` {.language-plaintext tabindex="-1"}
    [root@new_trust_agent]# ipactl restart
    ```

3.  Remove all entries from the SSSD cache on the trust agent:

    ``` {.language-plaintext tabindex="-1"}
    [root@new_trust_agent]# sssctl cache-remove
    ```

4.  Verify that the replica has the AD trust agent role installed:.

    ``` {.language-plaintext tabindex="-1"}
    [root@existing_trust_controller]# ipa server-show new_replica.idm.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    Enabled server roles: CA server, NTP server, AD trust agent
    ```

**Additional resources**

-   [Trust controllers and trust agents](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/planning-a-cross-forest-trust-between-idm-and-ad#trust-controllers-and-trust-agents)

### [9.10. Enabling automatic private group mapping for a POSIX ID range on the CLI](#enabling-automatic-private-group-mapping-for-a-posix-id-range-on-the-cli) {#enabling-automatic-private-group-mapping-for-a-posix-id-range-on-the-cli .title}

Enable automatic private group mapping for POSIX ID ranges to resolve Active Directory users who lack primary group configurations. Setting the `hybrid`{.literal} option for the `auto_private_groups`{.literal} SSSD parameter ensures SSSD can correctly map these users within IdM.

**Prerequisites**

-   You have successfully established a POSIX cross-forest trust between your IdM and AD environments.

**Procedure**

1.  Display all ID ranges and make note of the AD ID range you want to modify.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa idrange-find
    ```

    ``` {.language-plaintext tabindex="-1"}
    ----------------
    2 ranges matched
    ----------------
      Range name: IDM.EXAMPLE.COM_id_range
      First Posix ID of the range: 882200000
      Number of IDs in the range: 200000
      Range type: local domain range

      Range name: AD.EXAMPLE.COM_id_range
      First Posix ID of the range: 1337000000
      Number of IDs in the range: 200000
      Domain SID of the trusted domain: S-1-5-21-4123312420-990666102-3578675309
      Range type: Active Directory trust range with POSIX attributes
    ----------------------------
    Number of entries returned 2
    ----------------------------
    ```

2.  Adjust the automatic private group behavior for the AD ID range with the `ipa idrange-mod`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa idrange-mod --auto-private-groups=hybrid AD.EXAMPLE.COM_id_range
    ```

3.  Reset the SSSD cache to enable the new setting.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# sss_cache -E
    ```

**Additional resources**

-   [Options for automatically mapping private groups for AD users](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/index#options-for-automatically-mapping-private-groups-for-ad-users-posix-trusts)

### [9.11. Enabling automatic private group mapping for a POSIX ID range in the IdM WebUI](#enabling-automatic-private-group-mapping-for-a-posix-id-range-in-the-idm-webui) {#enabling-automatic-private-group-mapping-for-a-posix-id-range-in-the-idm-webui .title}

Enable automatic private group mapping for POSIX ID ranges to resolve Active Directory users who lack primary group configurations. Setting the `hybrid`{.literal} option for the `auto_private_groups`{.literal} SSSD parameter ensures SSSD can correctly map these users within IdM.

**Prerequisites**

-   You have successfully established a POSIX cross-forest trust between your IdM and AD environments.

**Procedure**

1.  Log into the IdM Web UI with your user name and password.

2.  Open the **IPA Server** → **ID Ranges** tab.

3.  Select the ID range you want to modify, such as `AD.EXAMPLE.COM_id_range`{.literal}.

4.  From the **Auto private groups** drop down menu, select the `hybrid`{.literal} option.

5.  Click the **Save** button to save your changes.

**Additional resources**

-   [Options for automatically mapping private groups for AD users: ID mapping trusts](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/planning-a-cross-forest-trust-between-idm-and-ad#options-for-automatically-mapping-private-groups-for-ad-users-id-mapping-trusts)

## [Chapter 10. Troubleshooting setting up a cross-forest trust](#troubleshooting-setting-up-a-cross-forest-trust) {#chapter-10.-troubleshooting-setting-up-a-cross-forest-trust .title}

Resolve cross-forest trust issues by analyzing the command execution sequence, verifying environment prerequisites, and capturing detailed debug logs for analysis.

### [10.1. Sequence of events when establishing a cross-forest trust with AD](#sequence-of-events-when-establishing-a-cross-forest-trust-with-ad) {#sequence-of-events-when-establishing-a-cross-forest-trust-with-ad .title}

Establishing a cross-forest trust involves a specific sequence of validation and configuration steps. Understanding these internal actions helps isolate whether a failure occurs during input verification or domain-level communication.

Part 1: The command verifies settings and inputs

:   1.  Verify that the IdM server has the **Trust Controller** role.
    2.  Validate the options passed to the `ipa trust-add`{.literal} command.
    3.  Validate the ID range associated with a trusted forest root domain. If you did not specify the ID range type and properties as options to the `ipa trust-add`{.literal} command, they are discovered from Active Directory.

Part 2: The command attempts to establish a trust to an Active Directory domain

:   

4.  Create a separate trust object for each trust direction. Each of the objects get created on both sides (IdM and AD). If you are establishing a one-way trust, only one object is created on each side.

5.  The IdM server uses the Samba suite to handle domain controller capabilities for Active Directory and creates a trust object on the target AD PDC:

    a.  The IdM server establishes a secure connection to the `IPC$`{.literal} share on the target DC. Since RHEL 8.4, the connection requires at least the SMB3 protocol with Windows Server 2012 and above to ensure the connection is sufficiently secure with AES-based encryption used for the session.

    b.  The IdM server queries for the presence of the trusted domain object (TDO) using an `LSA QueryTrustedDomainInfoByName`{.literal} call.

    c.  If the TDO is already present, remove it with an `LSA DeleteTrustedDomain`{.literal} call.

        Note

        This call fails if the AD user account used to establish the trust does not have full **Enterprise Admin (EA)** or **Domain Admin (DA)** privileges for the forest root, such as members of the **Incoming Forest Trust Builders** group. If the old TDO is not automatically removed, an AD Administrator must manually remove it from AD.

    d.  The IdM server creates a new TDO with an `LSA CreateTrustedDomainEx2`{.literal} call. The TDO credentials are randomly generated using a Samba-provided password generator with 128 random characters.

    e.  The new TDO is then modified with an `LSA SetInformationTrustedDomain`{.literal} call to make sure encryption types supported by the trust are set properly:

        i.  The `RC4_HMAC_MD5`{.literal} encryption type is enabled, even if there are no RC4 keys in use, due to how Active Directory is designed.
        ii. `AES128_CTS_HMAC_SHA1_96`{.literal} and `AES256_CTS_HMAC_SHA1_96`{.literal} encryption types are enabled.

6.  For a forest trust, verify that in-forest domains can be reached transitively with an `LSA SetInformationTrustedDomain`{.literal} call.

7.  Add trust topology information about the other forest (IdM in the case of communicating with AD, AD in the case of communicating with IdM) using an `LSA RSetForestTrustInformation`{.literal} call.

    Note

    This step might cause a conflict for one of three reasons:

    -   A SID namespace conflict, reported as an `LSA_SID_DISABLED_CONFLICT`{.literal} error. This conflict cannot be resolved.
    -   A NetBIOS namespace conflict, reported as an `LSA_NB_DISABLED_CONFLICT`{.literal} error. This conflict cannot be resolved.
    -   A DNS namespace conflict with a top level name (TLN), reported as an `LSA_TLN_DISABLED_CONFLICT`{.literal} error. The IdM server can automatically resolve a TLN conflict if it is caused by another forest.

    To resolve a TLN conflict, the IdM server performs the following steps:

    1.  Retrieve forest trust information for the conflicting forest.
    2.  Add an exclusion entry for the IdM DNS namespace to the AD forest.
    3.  Set forest trust information for the forest we conflict on.
    4.  Re-try establishing the trust to the original forest.

    The IdM server can only resolve these conflicts if you authenticated the `ipa trust-add`{.literal} command with the privileges of an AD administrator that can change forest trusts. If you do not have access to those privileges, the administrator of the original forest must manually perform the steps above in the **Active Directory Domains and Trusts** section of the Windows UI.

8.  If it does not exist, create the ID range for the trusted domain.

9.  For a forest trust, query Active Directory domain controllers from the forest root for details about the forest topology. The IdM server uses this information to create additional ID ranges for any additional domains from the trusted forest.

**Additional resources**

-   [Trust controllers and trust agents](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/planning-a-cross-forest-trust-between-idm-and-ad#trust-controllers-and-trust-agents)
-   [Microsoft Documentation: Overview Documents](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-winprotlp/4a1806f9-2979-491d-af3c-f82ed0a4c1ba)
-   [Microsoft Documentation: Technical Documents](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-winprotlp/e36c976a-6263-42a8-b119-7a3cc41ddd2a)
-   [Microsoft Documentation: Privileged Accounts and Groups in Active Directory](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory)

### [10.2. Checklist of prerequisites for establishing an AD trust](#checklist-of-prerequisites-for-establishing-an-ad-trust) {#checklist-of-prerequisites-for-establishing-an-ad-trust .title}

Successful trust establishment depends on specific environmental configurations. Review the requirements for product versions, administrative privileges, networking, and DNS settings.

+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Component                   | Configuration                                                                                                                                                                                | Additional details                                                                                                                                                                                                                                                                                                 |
+:============================+:=============================================================================================================================================================================================+:===================================================================================================================================================================================================================================================================================================================+
| Product versions            | Your Active Directory domain is using a supported version of Windows Server.                                                                                                                 | [Supported versions of Windows Server](#supported-versions-of-windows-server "Chapter 2. Supported versions of Windows Server")                                                                                                                                                                                    |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AD Administrator privileges | The Active Directory administration account must be a member of one of the following groups:                                                                                                 |                                                                                                                                                                                                                                                                                                                    |
|                             |                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                    |
|                             | -   **Enterprise Admin (EA)** group in the AD forest                                                                                                                                         |                                                                                                                                                                                                                                                                                                                    |
|                             | -   **Domain Admins (DA)** group in the forest root domain for your AD forest                                                                                                                |                                                                                                                                                                                                                                                                                                                    |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Networking                  | IPv6 support is enabled in the Linux kernel for all IdM servers.                                                                                                                             | [IPv6 requirements in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/preparing-the-system-for-idm-server-installation#ipv6_requirements_in_idm)                                                                                                     |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Date and time               | Verify the date and time settings on both servers match.                                                                                                                                     | [Time service requirements for IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/preparing-the-system-for-idm-server-installation#time-service-requirements-for-idm)                                                                                   |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Encryption types            | The following AD accounts have AES encryption keys:                                                                                                                                          | -   [Support for encryption types in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/preparing-the-system-for-idm-server-installation#ipv6_requirements_in_idm)                                                                                      |
|                             |                                                                                                                                                                                              | -   [Enabling the AES encryption type in Active Directory using a GPO](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_trust_between_idm_and_ad/ensuring-support-for-common-encryption-types-in-ad-and-rhel#enabling-the-aes-encryption-type-in-active-directory-using-a-gpo) |
|                             | -   AD Administrator                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                    |
|                             | -   AD user accounts                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                    |
|                             | -   AD services                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                    |
|                             |                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                    |
|                             | If you have recently enabled AES encryption in AD, generate new AES keys with the following steps:                                                                                           |                                                                                                                                                                                                                                                                                                                    |
|                             |                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                    |
|                             | 1.  Re-establish trust relationships between any AD domains in your forest.                                                                                                                  |                                                                                                                                                                                                                                                                                                                    |
|                             | 2.  Change the passwords for the AD Administrator, user accounts, and services.                                                                                                              |                                                                                                                                                                                                                                                                                                                    |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Firewall                    | You have opened all necessary ports on IdM servers and AD Domain Controllers for bidirectional communication.                                                                                | [Ports required for communication between IdM and AD](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_trust_between_idm_and_ad/ports-required-for-communication-between-idm-and-ad)                                                                                           |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DNS                         | -   IdM and AD each have unique primary DNS domains.                                                                                                                                         | [Configuring DNS and realm settings for a trust](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_trust_between_idm_and_ad/configuring-dns-and-realm-settings-for-a-trust)                                                                                                     |
|                             | -   IdM and AD DNS domains do not overlap.                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                    |
|                             | -   Proper DNS service (SRV) records for LDAP and Kerberos services.                                                                                                                         |                                                                                                                                                                                                                                                                                                                    |
|                             | -   You can resolve DNS records from all DNS domains in the trust.                                                                                                                           |                                                                                                                                                                                                                                                                                                                    |
|                             | -   Kerberos realm names are the upper-case versions of primary DNS domain names. For example, DNS domain `example.com`{.literal} has a corresponding Kerberos realm `EXAMPLE.COM`{.literal} |                                                                                                                                                                                                                                                                                                                    |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Topology                    | Ensure you are attempting to establish a trust with an IdM server you have configured as a trust controller.                                                                                 | [Trust controllers and trust agents](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/planning-a-cross-forest-trust-between-idm-and-ad#trust-controllers-and-trust-agents)                                                                                   |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 10.1. Table

Show more

### [10.3. Gathering debug logs of an attempt to establish an AD trust](#gathering-debug-logs-of-an-attempt-to-establish-an-ad-trust) {#gathering-debug-logs-of-an-attempt-to-establish-an-ad-trust .title}

Enable debug mode for Identity Management (IdM), Apache, and Samba to gather detailed logs of failed Active Directory (AD) trust attempts for troubleshooting or Red Hat Technical Support.

**Prerequisites**

-   You need root permissions to restart IdM services.

**Procedure**

1.  To enable debugging for the IdM server, create the file `/etc/ipa/server.conf`{.literal} with the following contents.

    ``` {.language-plaintext tabindex="-1"}
    [global]
    debug=True
    ```

2.  Restart the `httpd`{.literal} service to load the debugging configuration.

    ``` {.language-plaintext tabindex="-1"}
    [root@trust_controller ~]# systemctl restart httpd
    ```

3.  Stop the `smb`{.literal} and `winbind`{.literal} services.

    ``` {.language-plaintext tabindex="-1"}
    [root@trust_controller ~]# systemctl stop smb winbind
    ```

4.  Set the debugging log level for the `smb`{.literal} and `winbind`{.literal} services.

    ``` {.language-plaintext tabindex="-1"}
    [root@trust_controller ~]# net conf setparm global 'log level' 100
    ```

5.  To enable debug logging for Samba client code used by the IdM framework, edit the `/usr/share/ipa/smb.conf.empty`{.literal} configuration file to have the following contents.

    ``` {.language-plaintext tabindex="-1"}
        [global]
        log level = 100
    ```

6.  Remove previous Samba logs.

    ``` {.language-plaintext tabindex="-1"}
    [root@trust_controller ~]# rm /var/log/samba/log.*
    ```

7.  Start the `smb`{.literal} and `winbind`{.literal} services.

    ``` {.language-plaintext tabindex="-1"}
    [root@trust_controller ~]# systemctl start smb winbind
    ```

8.  Print a timestamp as you attempt to establish a trust with verbose mode enabled.

    ``` {.language-plaintext tabindex="-1"}
    [root@trust_controller ~]# date; ipa -vvv trust-add --type=ad ad.example.com
    ```

9.  Review the following error log files for information about the failed request:

    a.  `/var/log/httpd/error_log`{.literal}
    b.  `/var/log/samba/log.*`{.literal}

10. Disable debugging.

    ``` {.language-plaintext tabindex="-1"}
    [root@trust_controller ~]# mv /etc/ipa/server.conf /etc/ipa/server.conf.backup
    [root@trust_controller ~]# systemctl restart httpd
    [root@trust_controller ~]# systemctl stop smb winbind
    [root@trust_controller ~]# net conf setparm global 'log level' 0
    [root@trust_controller ~]# mv /usr/share/ipa/smb.conf.empty /usr/share/ipa/smb.conf.empty.backup
    [root@trust_controller ~]# systemctl start smb winbind
    ```

11. Optional: If you are unable to determine the cause of the authentication issue:

    a.  Collect and archive the log files you recently generated.

        ``` {.language-plaintext tabindex="-1"}
        [root@trust_controller ~]# tar -cvf debugging-trust.tar /var/log/httpd/error_log /var/log/samba/log.*
        ```

    b.  Open a Red Hat Technical Support case and provide the timestamp and debug logs from the attempt.

**Additional resources**

-   [IPA - AD Trust Troubleshooting](https://access.redhat.com/articles/2772181)

## [Chapter 11. Troubleshooting client access to services in the other forest](#troubleshooting-client-access-to-services-in-the-other-forest) {#chapter-11.-troubleshooting-client-access-to-services-in-the-other-forest .title}

Troubleshoot cross-forest authentication by tracing the Kerberos ticket requests and referrals between environments. These logic flows help isolate failures in the service request chain.

### [11.1. Flow of information when a host in the AD forest root domain requests services from an IdM server](#flow-of-information-when-a-host-in-the-ad-forest-root-domain-requests-services-from-an-idm-server) {#flow-of-information-when-a-host-in-the-ad-forest-root-domain-requests-services-from-an-idm-server .title}

Analyze the Kerberos communication path for Active Directory (AD) clients requesting services in the Identity Management (IdM) domain. This sequence identifies how KDCs handle cross-realm referrals and PAC validation.

If you have trouble accessing IdM services from AD clients, you can use this information to narrow your troubleshooting efforts and identify the source of the issue.

1.  The AD client contacts the AD Kerberos Distribution Center (KDC) to perform a TGS Request for the service in the IdM domain.
2.  The AD KDC recognizes that the service belongs to the trusted IdM domain.
3.  The AD KDC sends the client a cross-realm ticket-granting ticket (TGT), along with a referral to the trusted IdM KDC.
4.  The AD client uses the cross-realm TGT to request a ticket to the IdM KDC.
5.  The IdM KDC validates the Privileged Attribute Certificate (MS-PAC) that is transmitted with the cross-realm TGT.
6.  The IPA-KDB plugin might check the LDAP directory to see if foreign principals are allowed to get tickets for the requested service.
7.  The IPA-KDB plugin decodes the MS-PAC, verifies, and filters the data. It performs lookups in the LDAP server to check if it needs to augment the MS-PAC with additional information, such as local groups.
8.  The IPA-KDB plugin then encodes the PAC, signs it, attaches it to the service ticket, and sends it to the AD client.
9.  The AD client can now contact the IdM service using the service ticket issued by IdM KDC.

### [11.2. Flow of information when a host in an AD child domain requests services from an IdM server](#flow-of-information-when-a-host-in-an-ad-child-domain-requests-services-from-an-idm-server) {#flow-of-information-when-a-host-in-an-ad-child-domain-requests-services-from-an-idm-server .title}

Authenticating a client from an Active Directory (AD) child domain involves a multi-step Kerberos referral chain through the AD forest root KDC before reaching the Identity Management (IdM) KDC for final validation.

If you have trouble accessing IdM services from AD clients, and your AD client belongs to a domain that is a child domain of an AD forest root, you can use this information to narrow your troubleshooting efforts and identify the source of the issue.

1.  The AD client contacts the AD Kerberos Distribution Center (KDC) in its own domain to perform a TGS Request for the service in the IdM domain.
2.  The AD KDC in `child.ad.example.com`{.literal}, the child domain, recognizes that the service belongs to the trusted IdM domain.
3.  The AD KDC in the child domain sends the client a referral ticket for the AD forest root domain `ad.example.com`{.literal}.
4.  The AD client contacts the KDC in the AD forest root domain for the service in the IdM domain.
5.  The KDC in the forest root domain recognizes that the service belongs to the trusted IdM domain.
6.  The AD KDC sends the client a cross-realm ticket-granting ticket (TGT), along with a referral to the trusted IdM KDC.
7.  The AD client uses the cross-realm TGT to request a ticket to the IdM KDC.
8.  The IdM KDC validates the Privileged Attribute Certificate (MS-PAC) that is transmitted with the cross-realm TGT.
9.  The IPA-KDB plugin might check the LDAP directory to see if foreign principals are allowed to get tickets for the requested service.
10. The IPA-KDB plugin decodes the MS-PAC, verifies, and filters the data. It performs lookups in the LDAP server to check if it needs to augment the MS-PAC with additional information, such as local groups.
11. The IPA-KDB plugin then encodes the PAC, signs it, attaches it to the service ticket, and sends it to the AD client.
12. The AD client can now contact the IdM service using the service ticket issued by IdM KDC.

### [11.3. Flow of information when an IdM client requests services from an AD server](#flow-of-information-when-an-idm-client-requests-services-from-an-ad-server) {#flow-of-information-when-an-idm-client-requests-services-from-an-ad-server .title}

Accessing Active Directory (AD) services from an Identity Management (IdM) client requires a two-way trust to facilitate cross-realm ticket-granting tickets (TGT) and the generation of a Privileged Attribute Certificate.

If you have trouble accessing AD services from IdM clients, you can use this information to narrow your troubleshooting efforts and identify the source of the issue.

Note

By default, IdM establishes a one-way trust to AD, which means it is not possible to issue cross-realm ticket-granting ticket (TGT) for resources in an AD forest. To be able to request tickets to services from trusted AD domains, configure a two-way trust.

1.  The IdM client requests a ticket-granting ticket (TGT) from the IdM Kerberos Distribution Center (KDC) for the AD service it wants to contact.
2.  The IdM KDC recognizes that the service belongs to the AD realm, verifies that the realm is known and trusted, and that the client is allowed to request services from that realm.
3.  Using information from the IdM Directory Server about the user principal, the IdM KDC creates a cross-realm TGT with a Privileged Attribute Certificate (MS-PAC) record about the user principal.
4.  The IdM KDC sends back a cross-realm TGT to the IdM client.
5.  The IdM client contacts the AD KDC to request a ticket for the AD service, presenting the cross-realm TGT that contains the MS-PAC provided by the IdM KDC.
6.  The AD server validates and filters the PAC, and returns a ticket for the AD service.
7.  The IPA client can now contact the AD service.

**Additional resources**

-   [One-way trusts and two-way trusts](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management/planning-a-cross-forest-trust-between-idm-and-ad#one-way-trusts-and-two-way-trusts)

## [Chapter 12. Removing the trust using the command line](#removing-the-trust-using-the-command-line) {#chapter-12.-removing-the-trust-using-the-command-line .title}

Delete an Identity Management (IdM) trust agreement using the command line. This process removes the trust relationship from the IdM framework but preserves existing ID ranges by default.

**Prerequisites**

-   You have obtained a Kerberos ticket as an IdM administrator. For details, see [Logging in to IdM in the Web UI: Using a Kerberos ticket](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-idm-in-the-web-ui-using-a-kerberos-ticket).

**Procedure**

1.  Use the `ipa trust-del`{.literal} command to remove the trust configuration from IdM.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa trust-del ad_domain_name
    ```

    ``` {.language-plaintext tabindex="-1"}
    ------------------------------
    Deleted trust "ad_domain_name"
    ------------------------------
    ```

2.  Remove the trust object from your Active Directory configuration.

    Note

    Removing the trust configuration does not automatically remove the ID range IdM has created for AD users. This way, if you add the trust again, the existing ID range is re-used. Also, if AD users have created files on an IdM client, their POSIX IDs are preserved in the file metadata.

    To remove all information related to an AD trust, remove the AD user ID range after removing the trust configuration and trust object:

    ``` {.language-plaintext tabindex="-1"}
    # ipa idrange-del AD.EXAMPLE.COM_id_range
    # systemctl restart sssd
    ```

**Verification**

-   Use the `ipa trust-show`{.literal} command to confirm that the trust has been removed.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa trust-show ad.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    ipa: ERROR: ad.example.com: trust not found
    ```

## [Chapter 13. Removing the trust using the IdM Web UI](#removing-the-trust-using-the-idm-web-ui) {#chapter-13.-removing-the-trust-using-the-idm-web-ui .title}

Remove an Active Directory (AD) trust relationship through the Identity Management (IdM) Web UI. This action deletes the trust configuration in IdM while retaining associated ID ranges.

**Prerequisites**

-   You have obtained a Kerberos ticket. For details, see [Logging in to IdM in the Web UI: Using a Kerberos ticket](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-idm-in-the-web-ui-using-a-kerberos-ticket).

**Procedure**

1.  Log in to the IdM Web UI with administrator privileges. For details, see [Accessing the IdM Web UI in a web browser](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/accessing-the-idm-web-ui-in-a-web-browser).

2.  In the IdM Web UI, click the **IPA Server** tab.

3.  In the **IPA Server** tab, click the **Trusts** tab.

4.  Select the trust you want to remove.

5.  Click the **Delete** button.

6.  In the **Remove trusts** dialog box, click **Delete**.

7.  Remove the trust object from your Active Directory configuration.

    Note

    Removing the trust configuration does not automatically remove the ID range IdM has created for AD users. This way, if you add the trust again, the existing ID range is re-used. Also, if AD users have created files on an IdM client, their POSIX IDs are preserved in the file metadata.

    To remove all information related to an AD trust, remove the AD user ID range in the `ID Ranges`{.literal} tab after removing the trust configuration and trust object.

**Verification**

-   If the trust has been successfully deleted, the Web UI displays a green pop-up with the text:

## [Chapter 14. Removing the trust using Ansible](#removing-the-trust-using-ansible) {#chapter-14.-removing-the-trust-using-ansible .title}

To ensure consistent cleanup across your Identity Management (IdM) environment, run an Ansible playbook using the `ipatrust`{.literal} module to automate the removal of an Active Directory (AD) trust.

**Prerequisites**

-   You have obtained a Kerberos ticket as an IdM administrator. For details, see [Logging in to IdM in the Web UI: Using a Kerberos ticket](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/accessing_identity_management_services/logging-in-to-idm-in-the-web-ui-using-a-kerberos-ticket).

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  Navigate to your **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Create an `del-trust.yml`{.literal} playbook with the following content:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Playbook to delete trust
      hosts: ipaserver

      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
        - name: ensure the trust is absent
          ipatrust:
            ipaadmin_password: "{{ ipaadmin_password }}"
            realm: ad.example.com
            state: absent
    ```

    In the example, `realm`{.literal} defines the AD realm name string.

3.  Save the file.

    For details about variables and example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/README-trust.md`{.literal} file and the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/trust`{.literal} directory on the control node.

4.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory del-trust.yml
    ```

    Note

    Removing the trust configuration does not automatically remove the ID range IdM has created for AD users. This way, if you add the trust again, the existing ID range is re-used. Also, if AD users have created files on an IdM client, their POSIX IDs are preserved in the file metadata.

    To remove all information related to an AD trust, remove the AD user ID range after removing the trust configuration and trust object:

    ``` {.language-plaintext tabindex="-1"}
    # ipa idrange-del AD.EXAMPLE.COM_id_range
    # systemctl restart sssd
    ```

**Verification**

-   Use the `ipa trust-show`{.literal} command to confirm that the trust has been removed.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa trust-show ad.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    ipa: ERROR: ad.example.com: trust not found
    ```

## [Chapter 15. Removing an ID range after removing a trust to AD](#removing-an-id-range-after-removing-a-trust-to-ad) {#chapter-15.-removing-an-id-range-after-removing-a-trust-to-ad .title}

Manually delete the ID range associated with a removed Active Directory (AD) trust to clean up the Identity Management (IdM) configuration. This action purges unused ID allocations from the system.

Warning

IDs allocated to ID ranges associated with trusted domains might still be used for ownership of files and directories on systems enrolled into IdM.

If you remove the ID range that corresponds to an AD trust that you have removed, you will not be able to resolve the ownership of any files and directories owned by AD users.

**Prerequisites**

-   You have removed a trust to an AD environment.

**Procedure**

1.  Display all the ID ranges that are currently in use:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa idrange-find
    ```

2.  Identify the name of the ID range associated with the trust you have removed. The first part of the name of the ID range is the name of the trust, for example `AD.EXAMPLE.COM_id_range`{.literal}.

3.  Remove the range:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa idrange-del AD.EXAMPLE.COM_id_range
    ```

4.  Restart the SSSD service to remove references to the ID range you have removed.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# systemctl restart sssd
    ```

## [Legal Notice](#idm139635748235584) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
