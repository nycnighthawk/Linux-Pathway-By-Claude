---
{"title": "Active Directory-Integrated DNS Zones", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/active-directory-integrated-dns-zones", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Active Directory-Integrated DNS Zones

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Domain Name System (DNS) servers running on domain controllers can store their zones in Active Directory Domain Services (AD DS). In this way, it is not necessary to configure a separate DNS replication topology that uses ordinary DNS zone transfers because all zone data is replicated automatically by means of Active Directory replication. This simplifies the process of deploying DNS and provides the following advantages:

-   Multiple masters are created for DNS replication. Therefore, any domain controller in the domain running the DNS Server service can write updates to the Active Directory-integrated DNS zones for the domain name for which they are authoritative. A separate DNS zone transfer topology is not needed.

-   Secure dynamic updates are supported. Secure dynamic updates allow an administrator to control what computers update what names and prevent unauthorized computers from overwriting existing names in DNS.

Active Directory-integrated DNS in Windows Server 2008 stores zone data in application directory partitions. (There are no behavioral changes from Windows Server 2003-based DNS integration with Active Directory.) The following DNS-specific application directory partitions are created during AD DS installation:

-   A forest-wide application directory partition, called ForestDnsZones

-   Domain-wide application directory partitions for each domain in the forest, named DomainDnsZones

For more information about how AD DS stores DNS information in application partitions, see the [DNS Technical Reference](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc779926(v=ws.10)).

Note

We recommend that you install DNS when you run the Active Directory Domain Services Installation Wizard (Dcpromo.exe). If you do this, the wizard creates the DNS zone delegation automatically. For more information, see [Deploying a Windows Server 2008 Forest Root Domain](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc731174(v=ws.10)).

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Integrating AD DS into an Existing DNS Infrastructure](/en-us/windows-server/identity/ad-ds/plan/integrating-ad-ds-into-an-existing-dns-infrastructure?source=recommendations)

    Learn more about: Integrating AD DS into an Existing DNS Infrastructure

-   [DNS and AD DS](/en-us/windows-server/identity/ad-ds/plan/dns-and-ad-ds?source=recommendations)

    Learn more about: DNS and AD DS

-   [Reviewing DNS Concepts](/en-us/windows-server/identity/ad-ds/plan/reviewing-dns-concepts?source=recommendations)

    Learn more about: Reviewing DNS Concepts

-   [Domain Controller Location](/en-us/windows-server/identity/ad-ds/plan/domain-controller-location?source=recommendations)

    Learn more about: Domain Controller Location

-   [Creating a DNS Infrastructure Design](/en-us/windows-server/identity/ad-ds/plan/creating-a-dns-infrastructure-design?source=recommendations)

    Learn more about: Creating a DNS Infrastructure Design

-   [DNS for AD DS Owner Role](/en-us/windows-server/identity/ad-ds/deploy/assigning-the-dns-for-ad-ds-owner-role?source=recommendations)

    Information about the DNS for AD DS Owner role.

-   [Recommendations for Domain Name System (DNS) client settings - Windows Server](/en-us/troubleshoot/windows-server/networking/best-practices-for-dns-client-settings?source=recommendations)

    Describes recommendations for configuring DNS client settings.

Training

Module

[Implement Windows Server DNS - Training](/en-us/training/modules/implement-windows-server-dns/?source=recommendations)

Learn how to deploy and configure DNS in Windows Server, including DNS architecture, forward and reverse lookup zones, AD-integrated zones, zone transfers, forwarders, conditional forwarding, and stub zones.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
