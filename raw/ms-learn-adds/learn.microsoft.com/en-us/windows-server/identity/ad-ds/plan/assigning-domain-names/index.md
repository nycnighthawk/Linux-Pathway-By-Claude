---
{"title": "Assigning Domain Names", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/assigning-domain-names", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Assigning Domain Names

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

You must assign a name to every domain in your plan. Active Directory Domain Services (AD DS) domains have two types of names: Domain Name System (DNS) names and NetBIOS names. In general, both names are visible to end users. The DNS names of Active Directory domains include two parts, a prefix and a suffix. When creating domain names, first determine the DNS prefix. This is the first label in the DNS name of the domain. The suffix is determined when you select the name of the forest root domain. The following table lists the prefix naming rules for DNS names.

  Rule                                                               Explanation
  ------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------
  Select a prefix that is not likely to become outdated.             Avoid names such as a product line or operating system that might change in the future. We recommend using geographical names.
  Select a prefix that includes Internet standard characters only.   A-Z, a-z, 0-9, and (-), but not entirely numerical.
  Include 15 characters or less in the prefix.                       If you choose a prefix length of 15 characters or less, the NetBIOS name is the same as the prefix.

For more information, see [Naming conventions in Active Directory for computers, domains, sites, and OUs](https://support.microsoft.com/help/909264/).

Note

Although Dcpromo.exe in Windows Server 2008 and Windows Server 2003 allows you to create a single-label DNS domain name, you should not use a single-label DNS name for a domain for several reasons. In Windows Server 2008 R2, Dcpromo.exe does not allow you to create a single-label DNS name for a domain. For more information, see [Deployment and operation of Active Directory domains that are configured by using single-label DNS names](https://support.microsoft.com/help/300684/).

If the current NetBIOS name of the domain is inappropriate to represent the region or fails to satisfy the prefix naming rules, select a new prefix. In this case, the NetBIOS name of the domain is different from the DNS prefix of the domain.

For each new domain that you deploy, select a prefix that is appropriate for the region and that satisfies prefix naming rules. We recommend that the NetBIOS name of the domain be the same as the DNS prefix.

Document the DNS prefix and NetBIOS names that you select for each domain in your forest. You can add the DNS and NetBIOS name information to the \"Domain Planning\" worksheet that you created to document your plan for new and upgraded domains. To open it, download Job_Aids_Designing_and_Deploying_Directory_and_Security_Services.zip from [Job Aids for Windows Server 2003 Deployment Kit](https://microsoft.com/download/details.aspx?id=9608) and open \"Domain Planning\" (DSSLOGI_5.doc).

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

-   [Selecting the Forest Root Domain](/en-us/windows-server/identity/ad-ds/plan/selecting-the-forest-root-domain?source=recommendations)

    Learn more about: Selecting the Forest Root Domain

-   [Name computers, domains, sites, and OUs - Windows Server](/en-us/troubleshoot/windows-server/active-directory/naming-conventions-for-computer-domain-site-ou?source=recommendations)

    Describes how to name computers, domains, sites, and organizational units in Active Directory.

-   [Install a New Windows Server 2012 Active Directory Child or Tree Domain (Level 200)](/en-us/windows-server/identity/ad-ds/deploy/install-a-new-windows-server-2012-active-directory-child-or-tree-domain--level-200-?source=recommendations)

    Learn more about: Install a New Windows Server 2012 Active Directory Child or Tree Domain (Level 200)

-   [Determining Whether to Upgrade Existing Domains or Deploy New Domains](/en-us/windows-server/identity/ad-ds/plan/determining-whether-to-upgrade-existing-domains-or-deploy-new-domains?source=recommendations)

    Learn more about: Determining Whether to Upgrade Existing Domains or Deploy New Domains

-   [Determining the Number of Domains Required](/en-us/windows-server/identity/ad-ds/plan/determining-the-number-of-domains-required?source=recommendations)

    Learn more about: Determining the Number of Domains Required

-   [Best Practices for Active Directory Domains that Use Single-label DNS Names - Windows Server](/en-us/troubleshoot/windows-server/active-directory/deployment-operation-ad-domains?source=recommendations)

    This article provides information about the deployment and operation of Windows member computers and domain controllers that are joined to Active Directory domains use single-label DNS names.

-   [How trusts work for Microsoft Entra Domain Services - Microsoft Entra ID](/en-us/entra/identity/domain-services/concepts-forest-trust?source=recommendations)

    Learn how domain and forest trust relationships work in Active Directory and how they apply to Microsoft Entra Domain Services for cross-forest authentication.

-   [Recommendations for Domain Name System (DNS) client settings - Windows Server](/en-us/troubleshoot/windows-server/networking/best-practices-for-dns-client-settings?source=recommendations)

    Describes recommendations for configuring DNS client settings.

Training

Module

[Introduction to AD DS - Training](/en-us/training/modules/introduction-to-ad-ds/?source=recommendations)

Introduction to AD DS

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
