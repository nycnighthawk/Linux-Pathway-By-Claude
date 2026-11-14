---
{"title": "DNS and AD DS", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/dns-and-ad-ds", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# DNS and AD DS

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Active Directory Domain Services (AD DS) uses Domain Name System (DNS) name resolution services to make it possible for clients to locate domain controllers and for the domain controllers that host the directory service to communicate with each other.

AD DS enables easy integration of the Active Directory namespace into an existing DNS namespace. Features such as Active Directory-integrated DNS zones make it easier for you to deploy DNS by eliminating the need to set up secondary zones, and then configure zone transfers.

For information about how DNS supports AD DS, see the section [DNS Support for Active Directory Technical Reference](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc781627(v=ws.10)).

Note

If you implement a disjoint namespace in which the AD DS domain name differs from the primary DNS suffix that clients use, AD DS integration with DNS is more complex. For more information, see [Disjoint Namespace](disjoint-namespace).

[](#in-this-section)

## In this section {#in-this-section .heading-anchor}

-   [Domain Controller Location](domain-controller-location)
-   [Active Directory-Integrated DNS Zones](active-directory-integrated-dns-zones)
-   [Computer Naming](computer-naming)
-   [Disjoint Namespace](disjoint-namespace)

Reading mode disabled

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
