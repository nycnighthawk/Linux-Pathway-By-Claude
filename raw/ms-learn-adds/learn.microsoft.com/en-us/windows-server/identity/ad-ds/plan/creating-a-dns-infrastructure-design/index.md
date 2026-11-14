---
{"title": "Creating a DNS Infrastructure Design", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/creating-a-dns-infrastructure-design", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Creating a DNS Infrastructure Design

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

After you create your Active Directory forest and domain designs, you must design a Domain Name System (DNS) infrastructure to support your Active Directory logical structure. DNS enables users to use friendly names that are easy to remember to connect to computers and other resources on IP networks. Active Directory Domain Services (AD DS) in Windows Server 2008 requires DNS.

The process for designing DNS to support AD DS varies according to whether your organization already has an existing DNS Server service or you are deploying a new DNS Server service:

-   If you already have an existing DNS infrastructure, you must integrate the Active Directory namespace into that environment. For more information, see [Integrating AD DS into an Existing DNS Infrastructure](integrating-ad-ds-into-an-existing-dns-infrastructure).
-   If you do not have a DNS infrastructure in place, you must design and deploy a new DNS infrastructure to support AD DS. For more information, see [Deploying Domain Name System (DNS)](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc780661(v=ws.10)).

If your organization has an existing DNS infrastructure, you must make sure that you understand how your DNS infrastructure will interact with the Active Directory namespace. For a worksheet to assist you in documenting your existing DNS infrastructure design, download Job_Aids_Designing_and_Deploying_Directory_and_Security_Services.zip from [Job Aids for Windows Server 2003 Deployment Kit](https://microsoft.com/download/details.aspx?id=9608) and open \"DNS Inventory\" (DSSLOGI_8.doc).

Note

In addition to IP version 4 (IPv4) addresses, Windows Server also supports IP version 6 (IPv6) addresses. For a worksheet to assist you in listing the IPv6 addresses while documenting the recursive name resolution method of your current DNS structure, see [Appendix A: DNS Inventory](appendix-a--dns-inventory).

Before you design your DNS infrastructure to support AD DS, it can be helpful to read about the DNS hierarchy, the DNS name resolution process, and how DNS supports AD DS. For more information about the DNS hierarchy and name resolution process, see the [DNS Technical Reference](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc779926(v=ws.10)). For more information about how DNS supports AD DS, see the [DNS Support for Active Directory Technical Reference](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc781627(v=ws.10)).

[](#in-this-section)

## In this section {#in-this-section .heading-anchor}

-   [Reviewing DNS Concepts](reviewing-dns-concepts)
-   [DNS and AD DS](dns-and-ad-ds)
-   [DNS for AD DS Owner Role](../deploy/assigning-the-dns-for-ad-ds-owner-role)
-   [Integrating AD DS into an Existing DNS Infrastructure](integrating-ad-ds-into-an-existing-dns-infrastructure)

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3 hidden=""}

------------------------------------------------------------------------

-    Last updated on 05/12/2025
