---
{"title": "Raise domain and forest functional levels in Active Directory Domain Services", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/raise-domain-forest-functional-levels", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Raise domain and forest functional levels in Active Directory Domain Services

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Functional levels determine the available Active Directory Domain Services (AD DS) domain or forest capabilities. Functional levels also determine which Windows Server operating systems you can run on domain controllers in the domain or forest. Level changes happen when you use later versions of your domain controller operating system, the domain, or your forest functional level. This article describes how to raise Active Directory domain and forest functional levels. We recommend that you upgrade Active Directory Domain Service servers to the latest release.

To enable the latest domain features, all domain controllers in the domain must run the version of Windows Server that matches or is newer than the desired functional level. If they don\'t meet this requirement, the administrator can\'t raise the domain functional level.

To enable the latest forest-wide features, all domain controllers in the forest must run the Windows Server operating system version that matches or is newer than the desired functional level. The current domain functional level must already be at the latest level. If the forest meets these requirements, the administrator can raise the forest functional level.

The domain and forest functional levels only affect how the domain controllers operate together as a group. The clients that interact with the domain or with the forest are unaffected by the changes. Applications are also unaffected by these changes. However, applications can use new features found in later versions of Windows Server after the administrator raises the domain level. For more information about the functional levels, see [Active Directory Domain Services functional levels](/en-us/windows-server/identity/ad-ds/active-directory-functional-levels).

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

You need to meet the following prerequisites to raise the domain functional level:

-   All domain controllers in the domain are running at least the version of Windows Server that you want to raise the domain functional level to. For example, to raise the domain functional level to Windows Server 2025, all domain controllers in the domain must be running Windows Server 2025. If you have domain controllers running earlier versions of Windows Server, you must upgrade them to Windows Server 2025 before you can raise the domain functional level.

-   Before you can promote a machine running Windows Server 2025 to a domain controller in an existing domain, that domain must also be at least at the Windows Server 2016 functional level. Earlier versions of Windows Server don\'t support Windows Server 2025 domain controllers.

-   Your Active Directory forest and domain is operational and free from replication errors. To learn more about replication errors, see [Diagnose Active Directory replication failures](/en-us/troubleshoot/windows-server/active-directory/diagnose-replication-failures).

-   Identify all your DCs hosting the Global Catalog and FSMO roles. Create and verify backups of these domain controllers before making changes.

-   You must be a member of the Enterprise Admins group or equivalent to raise the forest functional level.

-   You must have a computer with one of the following Remote Server Administration Tools (RSAT) installed:

    -   AD DS Tools.
    -   Active Directory module for Windows PowerShell.

[](#view-the-current-functional-level)

## View the current functional level {#view-the-current-functional-level .heading-anchor}

To view the current domain and forest functional levels, you can use the Active Directory Domains and Trusts console or Windows PowerShell. The following sections describe how to view the functional levels by using these methods.

Note

Windows Server 2019 and Windows Server 2022 use Windows Server 2016 as the most recent functional levels.

-   [Desktop](#tabpanel_1_desktop)
-   [PowerShell](#tabpanel_1_PowerShell)

To view the domain or forest functional level by using the Active Directory Domains and Trusts console, complete these steps.

1.  Sign in to a computer with the AD DS Remote Server Administration Tools (RSAT) installed.

2.  Select the Start menu and enter *Active Directory Domains and Trusts* in the search box.

3.  Open **Active Directory Domains and Trusts**.

4.  In the console tree, right-click the domain node, and then select **Properties**.

5.  The **Properties** dialog shows the current domain and forest functional level.

[](#raise-the-functional-level)

## Raise the functional level {#raise-the-functional-level .heading-anchor}

To raise the domain and forest functional levels, you can use the Active Directory Domains and Trusts console or Windows PowerShell. The following sections describe how to raise the functional levels by using these methods.

Important

If all domain controllers in all domains in the forest are running Windows Server 2025, it isn\'t necessary to raise individual domain functional levels manually because raising the forest functional level to Windows Server 2025 automatically raises the domain functional level of all domains in the forest to Windows Server 2025.

-   [Desktop](#tabpanel_2_desktop)
-   [PowerShell](#tabpanel_2_PowerShell)

To raise the domain or forest functional level by using the Active Directory Domains and Trusts console, complete these steps.

1.  Sign in to a computer with the AD DS Remote Server Administration Tools (RSAT) installed.

2.  Select the Start menu and enter *Active Directory Domains and Trusts* in the search box.

3.  Open **Active Directory Domains and Trusts**.

4.  In the console tree, right-click the domain node, and then select **Raise Domain Functional Level**.

5.  In **Select an available domain functional level**, select the value and then select **Raise**.

6.  When prompted, select **OK** to confirm the change.

7.  After the domain functional level is raised, raise the forest functional level. In the console tree, right-click **Active Directory Domains and Trusts**, and then select **Raise Forest Functional Level**.

8.  In **Select an available forest functional level**, select the value and then select **Raise**.

You\'ve now raised the domain and forest functional level.

[](#related-content)

## Related content {#related-content .heading-anchor}

-   [Lower domain and forest functional levels in Active Directory Domain Services](lower-domain-forest-functional-levels)

-   [Forest and Domain Functional Levels](../active-directory-functional-levels)

-   [Identifying Your Functional Level Upgrade](identifying-your-functional-level-upgrade)

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

-   [How to raise Active Directory domain and forest functional levels - Windows Server](/en-us/troubleshoot/windows-server/active-directory/raise-active-directory-domain-forest-functional-levels?source=recommendations)

    Describes how to raise Active Directory domain and forest functional levels.

-   [Active Directory Domain Services Functional Levels](/en-us/windows-server/identity/ad-ds/active-directory-functional-levels?source=recommendations)

    Discover the capabilities of Active Directory Domain Services functional levels and learn how they impact domain controllers and Windows Server compatibility.

-   [Learn about upgrading your domain and forest functional levels in Active Directory Domain Services.](/en-us/windows-server/identity/ad-ds/plan/identifying-your-functional-level-upgrade?source=recommendations)

    Upgrade your domain and forest functional level in Active Director Domain Services for Windows Server

-   [Diagnose AD replication failures - Windows Server](/en-us/troubleshoot/windows-server/active-directory/diagnose-replication-failures?source=recommendations)

    Describes how to diagnose Active Directory replication failures.

-   [Upgrade domain controllers to a newer version of Windows Server](/en-us/windows-server/identity/ad-ds/deploy/upgrade-domain-controllers?source=recommendations)

    This article describes how to upgrade from an earlier version of Windows Server to a later version.

Training

Module

[Active Directory Domain Services migration - Training](/en-us/training/modules/active-directory-domain-services-migration/?source=recommendations)

Determine the best approach to moving domain controllers to Windows Server 2025.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 07/03/2026
