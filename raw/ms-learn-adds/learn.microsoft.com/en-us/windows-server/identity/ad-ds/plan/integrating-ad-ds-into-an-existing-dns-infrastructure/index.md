---
{"title": "Integrating AD DS into an Existing DNS Infrastructure", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/integrating-ad-ds-into-an-existing-dns-infrastructure", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Integrating AD DS into an Existing DNS Infrastructure

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

If your organization already has an existing Domain Name System (DNS) Server service, the DNS for Active Directory Domain Services (AD DS) owner must work with the DNS owner for your organization to integrate AD DS into the existing infrastructure. This involves creating a DNS server and DNS client configuration.

[](#creating-a-dns-server-configuration)

## Creating a DNS server configuration {#creating-a-dns-server-configuration .heading-anchor}

When integrating AD DS with an existing DNS namespace, we recommend that you do the following:

-   Install the DNS Server service on every domain controller in the forest. This provides fault tolerance if one of the DNS servers is unavailable. In this way, domain controllers don\'t need to rely on other DNS servers for name resolution. This also simplifies the management environment because all domain controllers have a uniform configuration.

-   Configure the Active Directory forest root domain controller to host the DNS zone for the Active Directory forest.

-   Configure the domain controllers for each regional domain to host the DNS zones that correspond to their Active Directory domains.

-   Configure the zone containing the Active Directory forest-wide locator records (that is, the \_msdcs.*forestname* zone) to replicate to every DNS server in the forest by using the forest-wide DNS application directory partition.

    Note

    When the DNS Server service is installed with the Active Directory Domain Services Installation Wizard (we recommend this option), all the previous tasks are performed automatically. For more information, see [Deploying a Windows Server 2008 Forest Root Domain](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc731174(v=ws.10)).

    Note

    AD DS uses forest-wide locator records to enable replication partners to find each other and to enable clients to find global catalog servers. AD DS stores the forest-wide locator records in the \_msdcs.*forestname* zone. Because the information in the zone must be widely available, this zone is replicated to all DNS servers in the forest by means of the forest-wide DNS application directory partition.

The existing DNS structure remains intact. You don\'t need to move any servers or zones. You simply need to create a delegation to your Active Directory-integrated DNS zones from your existing DNS hierarchy.

[](#creating-the-dns-client-configuration)

## Creating the DNS client configuration {#creating-the-dns-client-configuration .heading-anchor}

To configure DNS on client computers, the DNS for AD DS owner must specify the computer naming scheme and how the clients locate DNS servers. The following table lists our recommended configurations for these design elements.

  Design element                  Configuration
  ------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Computer naming                 Use default naming. When a computer using a Windows operating system joins a domain, the computer assigns itself a fully qualified domain name (FQDN) that comprises the host name of the computer and the name of the Active Directory domain.
  Client resolver configuration   Configure client computers to point to any DNS server on the network.

Note

Active Directory clients and domain controllers can dynamically register their DNS names even if they are not pointing to the DNS server that is authoritative for their names.

A computer might have a different existing DNS name if the organization previously, statically registered the computer in DNS or if the organization previously deployed an integrated Dynamic Host Configuration Protocol (DHCP) solution. If your client computers already have a registered DNS name, when the domain to which they\'re joined is upgraded to Windows Server 2008 AD DS, they\'ll have two different names:

-   The existing DNS name

-   The new fully qualified domain name (FQDN)

Clients can still be located by either name. Any existing DNS, DHCP, or integrated DNS/DHCP solution is left intact. The new primary names are created automatically and updated with dynamic update. They\'re cleaned up automatically with scavenging.

If you want to take advantage of Kerberos authentication when connecting to a server running Windows 2000, Windows Server 2003, or Windows Server 2008, you must make sure that the client connects to the server by using the primary name.

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

-   [Active Directory-Integrated DNS Zones](/en-us/windows-server/identity/ad-ds/plan/active-directory-integrated-dns-zones?source=recommendations)

    Learn more about: Active Directory-Integrated DNS Zones

-   [DNS and AD DS](/en-us/windows-server/identity/ad-ds/plan/dns-and-ad-ds?source=recommendations)

    Learn more about: DNS and AD DS

-   [Recommendations for Domain Name System (DNS) client settings - Windows Server](/en-us/troubleshoot/windows-server/networking/best-practices-for-dns-client-settings?source=recommendations)

    Describes recommendations for configuring DNS client settings.

-   [Domain Controller Location](/en-us/windows-server/identity/ad-ds/plan/domain-controller-location?source=recommendations)

    Learn more about: Domain Controller Location

-   [Reviewing DNS Concepts](/en-us/windows-server/identity/ad-ds/plan/reviewing-dns-concepts?source=recommendations)

    Learn more about: Reviewing DNS Concepts

-   [dcpromo in Windows Server](/en-us/windows-server/administration/windows-commands/dcpromo?source=recommendations)

    Learn about using the dcpromo command to install, promote, demote, and remove Active Directory Domain Services (AD DS) from a Windows Server.

Training

Module

[Implement Windows Server DNS - Training](/en-us/training/modules/implement-windows-server-dns/?source=recommendations)

Learn how to deploy and configure DNS in Windows Server, including DNS architecture, forward and reverse lookup zones, AD-integrated zones, zone transfers, forwarders, conditional forwarding, and stub zones.

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
