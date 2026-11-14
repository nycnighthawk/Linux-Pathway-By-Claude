---
{"title": "Computer Naming", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/computer-naming", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Computer Naming

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

When a computer running the Windows 2000, Windows XP, Windows Server 2003, Windows Server 2008 , or Windows Vista operating system joins a domain, by default the computer assigns itself a name. The name it assigns itself comprises the host name of the computer (that is, Computer Name in System Properties) and the Domain Name System (DNS) name of the Active Directory domain that the computer joined (that is, Primary DNS Suffix in System Properties). The concatenation of the host name and the DNS name of the domain is known as the fully qualified domain name (FQDN). For example, if a computer with host name Server1 joins the domain corp.contoso.com, the FQDN of the computer is server1.corp.contoso.com.

If a computer already has a different DNS domain name that was statically entered into a DNS zone or registered by an integrated DNS/Dynamic Host Configuration Protocol (DHCP) Server service, the FQDN of the computer is distinct from the name that was registered previously. The computer can be referenced by either name.

For more information about naming conventions in Active Directory Domain Services (AD DS), see [Naming conventions in Active Directory for computers, domains, sites, and OUs](https://support.microsoft.com/help/909264/).

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Domain Controller Location](/en-us/windows-server/identity/ad-ds/plan/domain-controller-location?source=recommendations)

    Learn more about: Domain Controller Location

-   [Active Directory-Integrated DNS Zones](/en-us/windows-server/identity/ad-ds/plan/active-directory-integrated-dns-zones?source=recommendations)

    Learn more about: Active Directory-Integrated DNS Zones

-   [Integrating AD DS into an Existing DNS Infrastructure](/en-us/windows-server/identity/ad-ds/plan/integrating-ad-ds-into-an-existing-dns-infrastructure?source=recommendations)

    Learn more about: Integrating AD DS into an Existing DNS Infrastructure

-   [DNS for AD DS Owner Role](/en-us/windows-server/identity/ad-ds/deploy/assigning-the-dns-for-ad-ds-owner-role?source=recommendations)

    Information about the DNS for AD DS Owner role.

-   [DNS and AD DS](/en-us/windows-server/identity/ad-ds/plan/dns-and-ad-ds?source=recommendations)

    Learn more about: DNS and AD DS

-   [Appendix A - DNS Inventory](/en-us/windows-server/identity/ad-ds/plan/appendix-a--dns-inventory?source=recommendations)

    Learn more about: Appendix A: DNS Inventory

------------------------------------------------------------------------

-    Last updated on 05/12/2025
