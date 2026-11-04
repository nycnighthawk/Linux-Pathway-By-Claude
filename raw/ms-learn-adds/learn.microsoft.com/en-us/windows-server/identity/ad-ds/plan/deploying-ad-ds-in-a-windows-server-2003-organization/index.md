---
{"title": "Deploying AD DS in a Windows Server 2003 Organization", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/deploying-ad-ds-in-a-windows-server-2003-organization", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Deploying AD DS in a Windows Server 2003 Organization

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

If your organization is currently running Windows Server 2003 Active Directory, you can deploy Windows Server 2008 Active Directory Domain Services (AD DS) by either performing an in-place upgrade of some or all of your domain controllers\' operating systems to Windows Server 2008 or by introducing domain controllers running Windows Server 2008 into your environment.

Before you can add a domain controller running Windows Server 2008 to an existing Windows Server 2003 Active Directory domain, you must run **adprep**, a command-line tool. Adprep extends the AD DS schema, updates default security descriptors of selected objects, and adds new directory objects as required by some applications. Adprep is available on the Windows Server 2008 installation disk (\\sources\\adprep\\adprep.exe). For more information, see [Adprep](/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc731728(v=ws.11)).

The following illustration shows the steps for deploying Windows Server 2008 AD DS in a network environment that is currently running Windows Server 2003 Active Directory.

Note

If you want to set the domain or forest functional level to Windows Server 2008 , all domain controllers in your environment must run the Windows Server 2008 operating system.

Consolidating resource domains and account domains that are upgraded in place from a Windows Server 2003 environment as part of your Windows Server 2008 AD DS deployment may require interforest or intraforest domain restructuring. Restructuring AD DS domains between forests helps you reduce the complexity of the representation of your organization in AD DS, and it helps reduce the associated administrative costs. Restructuring AD DS domains within a forest helps you decrease the administrative overhead for your organization by reducing replication traffic, reducing the amount of user and group administration that is required, and simplifying the administration of Group Policy. For more information, see [ADMT Guide: Migrating and Restructuring Active Directory Domains](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc974332(v=ws.10)).

For a list of detailed tasks that you can use to plan and deploy AD DS in an organization that is running Windows Server 2003 Active Directory, see [Checklist: Deploying AD DS in a Windows Server 2003 Organization](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc771407(v=ws.10)).

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Deploying AD DS in a Windows 2000 Organization](/en-us/windows-server/identity/ad-ds/plan/deploying-ad-ds-in-a-windows-2000-organization?source=recommendations)

    Learn more about: Deploying AD DS in a Windows 2000 Organization

-   [Deploying AD DS in a New Organization](/en-us/windows-server/identity/ad-ds/plan/deploying-ad-ds-in-a-new-organization?source=recommendations)

    Learn more about: Deploying AD DS in a New Organization

-   [Evaluating AD DS Deployment Strategy Examples](/en-us/windows-server/identity/ad-ds/plan/evaluating-ad-ds-deployment-strategy-examples?source=recommendations)

    Learn more about: Evaluating AD DS Deployment Strategy Examples

-   [Mapping Your Requirements to an AD DS Deployment Strategy](/en-us/windows-server/identity/ad-ds/plan/mapping-your-requirements-to-an-ad-ds-deployment-strategy?source=recommendations)

    Learn more about: Mapping Your Requirements to an AD DS Deployment Strategy

-   [Appendix A - Reviewing Key AD DS Terms](/en-us/windows-server/identity/ad-ds/plan/appendix-a--reviewing-key-ad-ds-terms?source=recommendations)

    Learn more about: Appendix A: Reviewing Key AD DS Terms

-   [Identifying the Deployment Project Participants](/en-us/windows-server/identity/ad-ds/plan/identifying-the-deployment-project-participants?source=recommendations)

    Learn more about: Identifying the Deployment Project Participants

Training

Module

[Active Directory Domain Services migration - Training](/en-us/training/modules/active-directory-domain-services-migration/?source=recommendations)

Determine the best approach to moving domain controllers to Windows Server 2025.

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
