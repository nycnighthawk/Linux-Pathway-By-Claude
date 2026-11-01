---
{"title": "Lower domain and forest functional levels in Active Directory Domain Services", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/lower-domain-forest-functional-levels", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Lower domain and forest functional levels in Active Directory Domain Services

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Functional levels determine the capabilities available in an Active Directory Domain Services (AD DS) domain or forest, and which Windows Server operating systems you can run on domain controllers. You raise a functional level to enable newer capabilities. Raising a level is no longer permanent, so you can lower a domain or forest back to a supported earlier level. You might need to lower the level if you raise it before your environment is ready, or if you need to add domain controllers that run an earlier version of Windows Server.

This article shows how to lower domain and forest functional levels by using PowerShell. After you complete the steps, the domain or forest operates at the level you specify, provided it meets the prerequisites described in this article.

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

Before you lower a functional level, make sure your environment meets the prerequisites in this section.

[](#permissions-and-tools)

### Permissions and tools {#permissions-and-tools .heading-anchor}

-   To lower the domain functional level, you\'re a member of the Domain Admins group or have equivalent permissions. To lower the forest functional level, you\'re a member of the Enterprise Admins group or have equivalent permissions.

-   You have a computer with the AD DS Remote Server Administration Tools (RSAT) installed, including the Active Directory module for Windows PowerShell.

[](#supported-rollback-levels)

### Supported rollback levels {#supported-rollback-levels .heading-anchor}

-   If your forest or domain contains Windows Server 2022 or earlier domain controllers, the lowest level you can roll back to is Windows Server 2008.

-   If your forest or domain contains Windows Server 2025 domain controllers, the lowest level you can roll back to is Windows Server 2016.

[](#forest-functional-level-prerequisites)

### Forest functional level prerequisites {#forest-functional-level-prerequisites .heading-anchor}

-   Your forest doesn\'t use any forest-level features exclusive to the current functional level. After you enable a feature tied to a specific forest functional level, you can\'t roll back to a lower level.

-   You have access to the domain controller that holds the Schema Operations Master flexible single master operations (FSMO) role.

[](#domain-functional-level-prerequisites)

### Domain functional level prerequisites {#domain-functional-level-prerequisites .heading-anchor}

-   Your domain doesn\'t use any features exclusive to the current domain functional level. For details about the features each level supports, see [Active Directory Domain Services functional levels](../active-directory-functional-levels).

-   The target domain functional level isn\'t lower than the current forest functional level.

-   You have network connectivity to the domain controller that holds the Primary Domain Controller (PDC) emulator FSMO role.

[](#lower-the-forest-functional-level)

## Lower the forest functional level {#lower-the-forest-functional-level .heading-anchor}

To lower the forest functional level by using PowerShell:

1.  Sign in to a computer with RSAT installed.

2.  Open PowerShell as an administrator.

3.  Run the following command to lower the forest functional level. Replace *`<forest>`* with the forest name and *`<level>`* with the forest functional level you want. For example, use `Windows2016Forest` to roll back to the Windows Server 2016 level.

    PowerShell

    ``` {.inner-focus data-language="powershell"}
    Set-ADForestMode -Identity <forest> -ForestMode <level>
    ```

4.  When PowerShell prompts you to confirm, enter **Y**.

5.  Run the following command to verify the change.

    PowerShell

    ``` {.inner-focus data-language="powershell"}
    Get-ADForest | Select-Object ForestMode
    ```

6.  Confirm that `ForestMode` shows the level you set.

[](#lower-the-domain-functional-level)

## Lower the domain functional level {#lower-the-domain-functional-level .heading-anchor}

To lower the domain functional level by using PowerShell:

1.  Sign in to a computer with RSAT installed.

2.  Open PowerShell as an administrator.

3.  Run the following command to lower the domain functional level. Replace *`<domain>`* with the domain name and *`<level>`* with the domain functional level you want. For example, use `Windows2016Domain` to roll back to the Windows Server 2016 level.

    PowerShell

    ``` {.inner-focus data-language="powershell"}
    Set-ADDomainMode -Identity <domain> -DomainMode <level>
    ```

4.  When PowerShell prompts you to confirm, enter **Y**.

5.  Run the following command to verify the change.

    PowerShell

    ``` {.inner-focus data-language="powershell"}
    Get-ADDomain | Select-Object DomainMode
    ```

6.  Confirm that `DomainMode` shows the level you set.

[](#related-content)

## Related content {#related-content .heading-anchor}

-   [Raise domain and forest functional levels in Active Directory Domain Services](raise-domain-forest-functional-levels)

-   [Active Directory Domain Services functional levels](../active-directory-functional-levels)

-   [Set-ADDomainMode](/en-us/powershell/module/activedirectory/set-addomainmode)

-   [Set-ADForestMode](/en-us/powershell/module/activedirectory/set-adforestmode)

**Note:** The author created this article with assistance from AI. [Learn more](/principles-for-ai-generated-content)

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

-   [Raise Domain and Forest Functional Levels in AD DS on Windows Server](/en-us/windows-server/identity/ad-ds/plan/raise-domain-forest-functional-levels?source=recommendations)

    Learn how to raise domain and forest functional levels in Active Directory Domain Services on Windows Server.

-   [Diagnose AD replication failures - Windows Server](/en-us/troubleshoot/windows-server/active-directory/diagnose-replication-failures?source=recommendations)

    Describes how to diagnose Active Directory replication failures.

-   [How to raise Active Directory domain and forest functional levels - Windows Server](/en-us/troubleshoot/windows-server/active-directory/raise-active-directory-domain-forest-functional-levels?source=recommendations)

    Describes how to raise Active Directory domain and forest functional levels.

-   [Orphaned child domain controller isn\'t replicated - Windows Server](/en-us/troubleshoot/windows-server/active-directory/orphaned-child-domain-isnt-replicated?source=recommendations)

    Describes an issue in which an orphaned child domain controller can\'t replicate information to other domain controllers in a domain, and provides a resolution.

-   [Active Directory Domain Services Functional Levels](/en-us/windows-server/identity/ad-ds/active-directory-functional-levels?source=recommendations)

    Discover the capabilities of Active Directory Domain Services functional levels and learn how they impact domain controllers and Windows Server compatibility.

-   [Learn about upgrading your domain and forest functional levels in Active Directory Domain Services.](/en-us/windows-server/identity/ad-ds/plan/identifying-your-functional-level-upgrade?source=recommendations)

    Upgrade your domain and forest functional level in Active Director Domain Services for Windows Server

-   [Troubleshooting Active Directory Replication Problems](/en-us/windows-server/identity/ad-ds/manage/troubleshoot/troubleshooting-active-directory-replication-problems?source=recommendations)

    Learn more about: Troubleshooting Active Directory Replication Problems

-   [Verify that SRV Domain Name System (DNS) records have been created - Windows Server](/en-us/troubleshoot/windows-server/networking/verify-srv-dns-records-have-been-created?source=recommendations)

    Describes how to verify Service Location (SRV) locator resource records for a domain controller after you install the Active Directory directory service.

------------------------------------------------------------------------

-    Last updated on 07/03/2026
