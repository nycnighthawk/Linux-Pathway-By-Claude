---
{"title": "Locating domain controllers in Windows and Windows Server", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/dc-locator", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Locating domain controllers in Windows and Windows Server

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Domain controller location refers to the algorithm the client machine uses to find a suitable domain controller. Domain controller location is a critical function in all enterprise environments to allow client authentication with Active Directory.

In this article, learn about the domain controller locator process, including discovery, closest site detection, and configuration of NetBIOS domain name mappings.

[](#domain-controller-locator-process)

## Domain controller locator process {#domain-controller-locator-process .heading-anchor}

The domain controller locator (DC locator) algorithm consists of two parts:

-   Locator finds which domain controllers are registered.

-   Locator submits a query to locate a domain controller in the specified domain.

An LDAP User Datagram Protocol (UDP) lookup is then sent to one or more of the domain controllers listed in the response to ensure their availability. Finally, the *Netlogon service* caches the discovered domain controller to aid in resolving future requests.

[](#discovery-process)

### Discovery process {#discovery-process .heading-anchor}

Active Directory domains always have two distinct names: the DNS fully qualified domain name (FQDN) and the NetBIOS domain name. NetBIOS domain names have legacy length and other constraints. For example, NetBIOS domains are limited to 15 characters.

The NetBIOS domain name of an Active Directory domain doesn\'t need to be the same as the Active Directory domain\'s FQDN. For example, an Active Directory domain\'s FQDN might be `contoso.com`, but the domain might have a NetBIOS domain name of `fabrikam`.

DC location in Windows can operate in two basic modes:

-   **DNS-based discovery** is based on domain controller advertisement using DNS.

    Domain controllers register various SRV records in DNS, such as records that represent key capabilities like Key Distribution Center or Global Catalog, and records that describe locality, like Active Directory site records. Clients query DNS for the appropriate SRV records and then ping those servers by using UDP-based LDAP pings.

    This mode is supported only when you use DNS domain names and your domain controllers are running Windows 2000 and later. Supported domain controllers run more optimally in this mode but can change to the other mode in certain scenarios.

-   **NetBIOS-based discovery** involves domain controllers registering records in [Windows Internet Name Service (WINS)](/en-us/windows-server/networking/technologies/wins/wins-top). Clients query WINS for the appropriate records, followed by pinging the possible target candidate DCs. A variant of this mode uses a broadcast mechanism supported by [mailslot messages](/en-us/windows/win32/ipc/about-mailslots) where the client broadcasts packets on its local network to look for DCs.

Important

When an application requests a DC but specifies a short NetBIOS-style domain name, DC location always tries to map that short domain name to a DNS domain name. If DC location can map the domain names successfully, it uses DNS-based discovery with the mapped DNS domain name.

NetBIOS-style domain names are mapped to DNS domain names from multiple sources, in the following order:

1.  Cached information from a previous lookup

2.  All domains in the current forest

3.  Top-level names (TLNs) for all trusting forest trusts and external trusts

4.  For Windows Server 2025 and later:

    1.  Administrator-configured domain name mappings

    2.  Domain name mappings for all forests and child domains in trusting forest trusts

5.  Sign-in sessions on the client machine

When none of these sources can find a DNS domain name, DC location can proceed with NetBIOS-based discovery by using the original NetBIOS-style short domain name

Beginning with Windows Server 2025, Netlogon downloads and caches naming information about domains and child domains in all trusting forests. This information is used when you\'re mapping NetBIOS-style domain names to DNS domain names.

We recommend using DNS-based discovery instead of NetBIOS-based discovery. DNS-based discovery is more reliable and secure. [DsGetDcName](/en-us/windows/win32/api/dsgetdc/nf-dsgetdc-dsgetdcnamew) is the primary DC location API.

Important

Beginning with Windows Server 2025, DC locator doesn\'t allow the use of NetBIOS-style location. To learn how to configure this behavior, see the [NetBIOS discovery policy setting](#netbios-discovery-policy-setting) section in this article.

To learn about the discovery process, select the tab that corresponds to the method you want to learn about.

-   [DNS-based discovery](#tabpanel_1_dns-based-discovery)
-   [NetBIOS-based discovery](#tabpanel_1_netbios-based-discovery)

The process that the locator follows can be summarized as follows:

1.  On the client (the computer that\'s locating the domain controller), the locator is initiated as a remote procedure call (RPC) to the local Netlogon service. The Netlogon service implements the Locator API (`DsGetDcName`).

2.  The client collects the information that\'s needed to select a domain controller and passes the information to the Netlogon service by using the `DsGetDcName` API.

3.  The Netlogon service on the client uses the collected information to look up a domain controller for the specified domain. The lookup process uses one of the following two methods:

4.  Netlogon queries DNS by using the IP/DNS-compatible locator. `DsGetDcName` calls the DnsQuery call to read the Service Resource (SRV) records and A records from DNS after it appends the domain name to the appropriate string that specifies the SRV records.

    -   When a workstation signs in to a Windows-based domain, it queries DNS for SRV records in the format `_<service>._<protocol>.<DnsDomainName>`. Clients querying DNS for an LDAP server for the domain using the following format, where `DnsDomainName` is the domain name.

        `_ldap._tcp.DnsDomainName`

5.  The Netlogon service sends a datagram as an LDAP UDP search to the discovered domain controllers that register the name.

6.  Each available domain controller responds to the datagram to indicate that it\'s currently operational and then returns the information to `DsGetDcName`.

7.  The Netlogon service returns the information to the client from the domain controller that responds first.

8.  The Netlogon service caches the domain controller information so that it isn\'t necessary to repeat the discovery process for subsequent requests. Caching this information encourages the consistent use of the same domain controller and, thus, a consistent view of Active Directory.

[](#netbios-discovery-policy-setting)

### NetBIOS discovery policy setting {#netbios-discovery-policy-setting .heading-anchor}

Beginning with Windows Server 2025, DC locator doesn\'t allow the use of the NetBIOS-based discovery. `BlockNetBIOSDiscovery` is a new Group Policy setting for the Netlogon service that allows administrators to control this behavior. To access the policy in Group Policy Management Editor, go to **Computer Configuration** \> **Administrative Templates** \> **System** \> **Net Logon** \> **DC Locator DNS Records** \> **Block NetBIOS-based discovery for domain controller location**.

The following settings apply to `BlockNetBIOSDiscovery`:

-   `TRUE` (default): DC locator doesn\'t allow the use of NetBIOS-style DC location.
-   `FALSE`: DC locator allows the use of WINS or mailslot-based discovery if all legacy constraints also allow it.

You use the `BlockNetBIOSDiscovery` setting to enforce a secure-by-default posture for DC location. We recommend that you keep it set to `TRUE`. Disable it only for temporary periods while you\'re pursuing other mitigations.

The new policy setting looks like this:

Tip

You can separately enable or disable the ability to use mailslots on a machine-wide basis by using the SMB `EnableMailslots` policy setting. For DC locator to be able to use mailslots for DC discovery, you must enable mailslots at the SMB level and disable `BlockNetBIOSDiscovery`. You can query and set the `EnableMailslots` setting by running the `Get-SmbClientConfiguration` and `Set-SmbClientConfiguration` PowerShell cmdlets.

[](#closest-active-directory-site)

## Closest Active Directory site {#closest-active-directory-site .heading-anchor}

After the client locates a domain controller, it establishes communication by using LDAP to gain access to Active Directory. As part of that negotiation, the domain controller identifies which site the client is in based on the client\'s IP subnet.

If the client is communicating with a domain controller that isn\'t in the closest, most optimal site, the domain controller returns the name of the client\'s site. If the client has already tried to find domain controllers in that site, the client uses a domain controller in a less optimal site instead. For example, the client sends a DNS Lookup query to DNS to find domain controllers in the client\'s subnet. Otherwise, the client does a site-specific DNS lookup again with the new optimal site name. The domain controller uses some of the directory service information for identifying sites and subnets.

The client caches the domain controller entry. If the domain controller isn\'t in the optimal site, the client flushes the cache after 15 minutes and discards the cache entry. It then attempts to find an optimal domain controller in the same site as the client.

After the client establishes a communications path to the domain controller, it can establish the sign-in and authentication credentials. If necessary, the client can also set up a secure channel for Windows-based computers. The client is now ready to perform normal queries and search for information against the directory.

The client establishes an LDAP connection to a domain controller to sign in. The sign-in process uses *Security Accounts Manager*. The communications path uses the LDAP interface, and a domain controller authenticates the client. After that, the client account is verified and passed through Security Accounts Manager to the directory service agent, then to the database layer, and finally to the database in the Extensible Storage Engine (ESE).

[](#configuring-netbios-domain-name-mappings)

## Configuring NetBIOS domain name mappings {#configuring-netbios-domain-name-mappings .heading-anchor}

Beginning with Windows Server 2025, forest administrators can configure custom mappings from DNS domain name to NetBIOS domain name. Administrator-configured mappings at the forest level are an optional mechanism that you should use only when all other options are insufficient. For example, if an application or environment requires other domain name mappings that other sources can\'t automatically provide.

The custom domain name mappings are stored in a `serviceConnectionPoint` object located in the naming context for the Active Directory configuration. For example:

`CN=DCLocatorDomainNameMappings,CN=Windows NT,CN=Services,CN=Configuration,DC=contoso,DC=com`

The `msDS-Setting`s attribute of this `serviceConnectionPoint` object can contain one or more values. Each value contains the DNS domain name and the NetBIOS domain name, separated by a semicolon, as in dnsdomainname.com:NetBIOSdomainname.

For example:

-   `contoso.com:fabrikam`
-   `tatertots.contoso.com:tots`
-   `tailspintoys.com:tailspintoys`

You can configure these mappings in the Active Directory Domains and Trusts management settings by following these steps:

1.  Right-click the domain.
2.  Select **Properties**.
3.  Select the **DC locator mappings** tab.

The Netlogon service on clients then downloads and caches the custom mappings in the `DCLocatorDomainNameMappings` object every 12 hours. The service automatically uses this information when you\'re mapping NetBIOS-style domain names to DNS domain names.

The new Active Directory Domains and Trusts management page looks like this:

Important

Configure administrator-configured forest-level domain name mappings only when you\'re sure that all other name mapping sources are insufficient. As a general rule, such arbitrary mappings are necessary only when no trust relationship exists between clients and the target domains, and client applications can\'t be migrated to specifying DNS-style domain names.

[](#related-content)

## Related content {#related-content .heading-anchor}

-   [DsGetDcName](/en-us/windows/win32/api/dsgetdc/nf-dsgetdc-dsgetdcnamew)
-   [How domain controllers are located in Windows](/en-us/troubleshoot/windows-server/identity/how-domain-controllers-are-located)
-   [How to verify that SRV DNS records have been created for a domain controller](/en-us/troubleshoot/windows-server/networking/verify-srv-dns-records-have-been-created)
-   [The Beginning of the end of Remote Mailslots](https://techcommunity.microsoft.com/t5/storage-at-microsoft/the-beginning-of-the-end-of-remote-mailslots/ba-p/3762048)
-   [Windows Internet Name Service (WINS)](/en-us/windows-server/networking/technologies/wins/wins-top)
-   [About mailslots](/en-us/windows/win32/ipc/about-mailslots)

Reading mode disabled

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Troubleshoot domain controller location issues in Windows - Windows Server](/en-us/troubleshoot/windows-server/windows-security/troubleshoot-domain-controller-location-issues?source=recommendations)

    Helps troubleshoot domain controller location issues in Windows.

-   [Verify that SRV Domain Name System (DNS) records have been created - Windows Server](/en-us/troubleshoot/windows-server/networking/verify-srv-dns-records-have-been-created?source=recommendations)

    Describes how to verify Service Location (SRV) locator resource records for a domain controller after you install the Active Directory directory service.

-   [Troubleshoot domain controller deployment - Windows Server](/en-us/troubleshoot/windows-server/active-directory/troubleshoot-domain-controller-deployment?source=recommendations)

    Provides information about troubleshooting domain controller deployment.

-   [Troubleshooting Active Directory Replication Problems](/en-us/windows-server/identity/ad-ds/manage/troubleshoot/troubleshooting-active-directory-replication-problems?source=recommendations)

    Learn more about: Troubleshooting Active Directory Replication Problems

-   [Domain controller is not functioning correctly - Windows Server](/en-us/troubleshoot/windows-server/active-directory/domain-controller-not-functioning-correctly?source=recommendations)

    Provides common resolutions to issues where you cannot open Active Directory snap-ins or connect to a domain controller from another computer. Additionally, discusses resolutions to errors in the DCDIAG tool.

-   [Active Directory domain join troubleshooting guidance - Windows Server](/en-us/troubleshoot/windows-server/active-directory/active-directory-domain-join-troubleshooting-guidance?source=recommendations)

    Provides guidance to troubleshoot domain join issues.

-   [Errors when you run DCDIAG commands - Windows Server](/en-us/troubleshoot/windows-server/active-directory/dcdiag-commands-running-errors?source=recommendations)

    Fixes errors that occur when you run DCDIAG.EXE /E or /A or /C commands.

Training

Module

[Active Directory Domain Services migration - Training](/en-us/training/modules/active-directory-domain-services-migration/?source=recommendations)

Determine the best approach to moving domain controllers to Windows Server 2025.

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 07/10/2025
