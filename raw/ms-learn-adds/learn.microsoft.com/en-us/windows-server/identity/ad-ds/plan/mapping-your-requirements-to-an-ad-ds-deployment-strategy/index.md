---
{"title": "Mapping Your Requirements to an AD DS Deployment Strategy", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/mapping-your-requirements-to-an-ad-ds-deployment-strategy", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Mapping Your Requirements to an AD DS Deployment Strategy

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

After you finish reviewing and identifying the Active Directory Domain Services (AD DS) design and deployment requirements and you determine which of them are related to your specific deployment, you can map those requirements to a specific AD DS deployment strategy.

Use the following table to determine which AD DS deployment strategy maps to the appropriate combination of AD DS design and deployment requirements for your organization. (\"Yes\" means that a specific requirement is necessary for your deployment strategy; \"No\" means that a specific requirement is not necessary for your deployment strategy.)

This table refers only to the three primary AD DS deployment strategies as described in this guide:

-   [Deploying AD DS in a New Organization](deploying-ad-ds-in-a-new-organization)

-   [Deploying AD DS in a Windows Server 2003 Organization](deploying-ad-ds-in-a-windows-server-2003-organization)

-   [Deploying AD DS in a Windows 2000 Organization](deploying-ad-ds-in-a-windows-2000-organization)

However, you can create a hybrid or custom AD DS deployment strategy by using any combination of the AD DS design and deployment requirements to meet the needs of your organization.

  AD DS design and deployment requirements                                                                                                                                                          Deploying AD DS in a New Organization                                                                                                                                                                                                                                                                             Deploying AD DS in a Windows Server 2003 Organization                                                                                                                                                                          Deploying AD DS in a Windows 2000 Organization
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Designing the Logical Structure for Windows Server 2008 AD DS](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc770806(v=ws.10))                                        Yes                                                                                                                                                                                                                                                                                                               Yes                                                                                                                                                                                                                            Yes
  [Designing the Site Topology for Windows Server 2008 AD DS](designing-the-site-topology)                                                                                                          Yes                                                                                                                                                                                                                                                                                                               Yes                                                                                                                                                                                                                            Yes
  Planning Domain Controller Capacity                                                                                                                                                               Yes                                                                                                                                                                                                                                                                                                               Yes                                                                                                                                                                                                                            Yes
  [Deploying a Windows Server 2008 Forest Root Domain](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc731174(v=ws.10))                                                   Yes                                                                                                                                                                                                                                                                                                               No                                                                                                                                                                                                                             No
  [Deploying Windows Server 2008 Regional Domains](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc755118(v=ws.10))                                                       Yes                                                                                                                                                                                                                                                                                                               Yes                                                                                                                                                                                                                            Yes
  [Enabling Advanced Features for AD DS](enabling-advanced-features-for-ad-ds)                                                                                                                      Yes                                                                                                                                                                                                                                                                                                               Yes, but all domain controllers in the environment must run Windows Server 2008 before you set the domain or forest functional level to Windows Server 2008.                                                                   Yes, but all domain controllers in the environment must run Windows Server 2008 before you set the domain or forest functional level to Windows Server 2008.
  [Upgrading Active Directory Domains to Windows Server 2008 and Windows Server 2008 R2 AD DS Domains](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc731188(v=ws.10))   No                                                                                                                                                                                                                                                                                                                Yes                                                                                                                                                                                                                            Yes
  [ADMT Guide: Migrating and Restructuring Active Directory Domains](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc974332(v=ws.10))                                     Yes, if you want to migrate a pilot domain into your production environment, merge with another organization and consolidate the two information technology (IT) infrastructures, or consolidate resource and account domains that you upgraded in place from Windows 2000 or Windows Server 2003 environments.   Yes, if you want to merge with another organization and consolidate the two IT infrastructures or consolidate resource and account domains that you upgraded in place from Windows 2000 or Windows Server 2003 environments.   Yes, if you want to merge with another organization and consolidate the two IT infrastructures or consolidate resource and account domains that you upgraded in place from Windows 2000 or Windows Server 2003 environments.
  [ADMT Guide: Migrating and Restructuring Active Directory Domains](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc974332(v=ws.10))                                     No                                                                                                                                                                                                                                                                                                                Yes, if you need to reduce the number of domains, reduce replication traffic and the amount of required user and group administration, or simplify the administration of Group Policy.                                         Yes, if you need to reduce the number of domains, reduce replication traffic and the amount of required user and group administration, or simplify the administration of Group Policy.

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

-   [Identifying Your AD DS Design and Deployment Requirements](/en-us/windows-server/identity/ad-ds/plan/identifying-your-ad-ds-design-and-deployment-requirements?source=recommendations)

    Learn more about: Identifying Your AD DS Design and Deployment Requirements

-   [AD DS Design Requirements](/en-us/windows-server/identity/ad-ds/plan/ad-ds-design-requirements?source=recommendations)

    Learn more about: AD DS Design Requirements

-   [Understanding AD DS Design](/en-us/windows-server/identity/ad-ds/plan/understanding-ad-ds-design?source=recommendations)

    Learn more about: Understanding AD DS Design

-   [AD DS Design and Planning](/en-us/windows-server/identity/ad-ds/plan/ad-ds-design-and-planning?source=recommendations)

    Learn more about: AD DS Design and Planning

-   [AD DS Deployment Requirements](/en-us/windows-server/identity/ad-ds/plan/ad-ds-deployment-requirements?source=recommendations)

    Learn more about: AD DS Deployment Requirements

-   [Designing the Logical Structure](/en-us/windows-server/identity/ad-ds/plan/designing-the-logical-structure?source=recommendations)

    Learn more about: Designing the Logical Structure

-   [Deploying AD DS in a New Organization](/en-us/windows-server/identity/ad-ds/plan/deploying-ad-ds-in-a-new-organization?source=recommendations)

    Learn more about: Deploying AD DS in a New Organization

Training

Module

[Active Directory Domain Services migration - Training](/en-us/training/modules/active-directory-domain-services-migration/?source=recommendations)

Determine the best approach to moving domain controllers to Windows Server 2025.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
