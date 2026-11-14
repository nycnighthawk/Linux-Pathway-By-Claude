---
{"title": "Upgrade domain controllers to a newer version of Windows Server", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/upgrade-domain-controllers", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Upgrade domain controllers to a newer version of Windows Server

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

This article provides background information about Active Directory Domain Services in Windows Server and explains the process for upgrading domain controllers (DCs) from an earlier version of Windows Server.

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

The recommended way to upgrade a domain is to use a clean OS install to promote new servers to DCs that run a newer version of Windows Server and demote the older DCs as needed. This method is preferable to performing an in-place upgrade of the operating system on an existing DC. A clean OS install ensures you get the full Active Directory performance improvements included in new versions of Windows Server.

Follow these general steps before you promote a server to a DC that runs a newer version of Windows Server:

1.  Verify the target server meets the [system requirements](../../../get-started/hardware-requirements).

2.  Verify application compatibility.

3.  Review recommendations for moving to a newer version of Windows Server.

4.  Verify security settings.

5.  Check connectivity to the target server from the computer where you plan to run the installation.

6.  Check for availability of the necessary Flexible Single Master Operation (FSMO) roles in Active Directory. This step is required for the following scenarios:

    -   To install the first DC that runs the latest Windows Server version in an existing domain and forest, the machine where you run the installation needs connectivity to:
        -   The **schema master** to run `adprep /forestprep`.
        -   The **infrastructure master** to run `adprep /domainprep`.
    -   To install the first DC in a domain where the forest schema is already extended, you only need connectivity to the **infrastructure master**.
    -   To install or remove a domain in an existing forest, you need connectivity to the **domain naming master**.
    -   Any DC installation also requires connectivity to the **RID master.**
    -   If you\'re installing the first read-only DC in an existing forest, you need connectivity to the **infrastructure master** for each application directory partition, which is also known as a non-domain naming context.

    To find out which server or servers hold which FSMO role, run the following commands in an elevated PowerShell session by using an account that\'s a member of the Domain Admins group:

    PowerShell

    ``` {.inner-focus data-language="PowerShell"}
    Get-ADDomain | FL InfrastructureMaster, RIDMaster, PDCEmulator
    Get-ADForest | FL DomainNamingMaster, SchemaMaster
    ```

[](#installation-actions-and-required-administrative-levels)

### Installation actions and required administrative levels {#installation-actions-and-required-administrative-levels .heading-anchor}

The following table provides a summary of the installation actions and the permissions requirements to accomplish these steps.

  Installation action                           Credential requirements
  --------------------------------------------- -----------------------------------------------------
  Install a new forest.                         Local admin on the target server
  Install a new domain in an existing forest.   Enterprise admins
  Install another DC in an existing domain.     Domain admins
  Run `adprep /forestprep`.                     Schema admins, enterprise admins, and domain admins
  Run `adprep /domainprep`.                     Domain admins
  Run `adprep /domainprep /gpprep.`             Domain admins
  Run `adprep /rodcprep`.                       Enterprise admins

[](#supported-in-place-upgrade-paths)

## Supported in-place upgrade paths {#supported-in-place-upgrade-paths .heading-anchor}

Only 64-bit version upgrades are supported. For more information about supported upgrade paths, see [Supported upgrade paths](../../../get-started/supported-upgrade-paths).

[](#adprep---forestprep-and-domainprep)

## Adprep - forestprep and domainprep {#adprep---forestprep-and-domainprep .heading-anchor}

For an in-place upgrade of an existing DC, you must run `adprep /forestprep` and `adprep /domainprep` manually. You need to run `Adprep /forestprep` only once in the forest for each newer version of Windows Server. Run `Adprep /domainprep` once in each domain in which you have DCs that you\'re upgrading for each newer version of Windows Server.

If you\'re promoting a new server to a DC, you don\'t need to run these command-line tools manually. They\'re integrated into the PowerShell and Server Manager experiences.

For more information on running adprep, see [Running Adprep](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd464018(v=ws.10)).

[](#functional-level-features-and-requirements)

## Functional-level features and requirements {#functional-level-features-and-requirements .heading-anchor}

Windows Server 2019 or later requires a Windows Server 2008 forest functional level as a minimum. Windows Server 2016 requires a Windows Server 2003 forest functional level as a minimum. If the forest contains DCs running an older forest functional level than the operating system supports, the installation is blocked. Those DCs must be removed and the forest functional level raised to a version that\'s supported before you add newer Windows Server DCs to your forest. For more information about supported functional levels, see [Forest and domain functional levels](../active-directory-functional-levels).

Note

No new forest or domain functional levels have been added since Windows Server 2016. Later operating system versions can and should be used for domain controllers. They use Windows Server 2016 as the most recent functional levels.

[](#roll-back-functional-levels)

### Roll back functional levels {#roll-back-functional-levels .heading-anchor}

After you set the forest functional level to a certain value, you can\'t roll back or lower the forest functional level, with the following exceptions:

-   If you\'re upgrading from Windows Server 2012 R2 forest functional level, you can roll back to Windows Server 2012 R2.
-   If you\'re upgrading from Windows Server 2008 R2 forest functional level, you can roll back to Windows Server 2008 R2.

After you set the domain functional level to a certain value, you can\'t roll back or lower the domain functional level, with the following exceptions:

-   When you raise the domain functional level to Windows Server 2016 and if the forest functional level is Windows Server 2012 or lower, you have the option of rolling the domain functional level back to Windows Server 2012 or Windows Server 2012 R2.

For more information about features available at each of the functional levels, see [Forest and domain functional levels](../active-directory-functional-levels).

[](#active-directory-domain-services-interoperability)

## Active Directory Domain Services interoperability {#active-directory-domain-services-interoperability .heading-anchor}

Active Directory Domain Services isn\'t supported on the following Windows operating systems:

-   Windows MultiPoint Server
-   Windows Server Essentials

Active Directory Domain Services can\'t be installed on a server that also runs the following server roles or role services:

-   Microsoft Hyper-V Server
-   Remote Desktop Connection Broker

[](#administration-of-windows-server)

## Administration of Windows Server {#administration-of-windows-server .heading-anchor}

Use the Remote Server Administration Tools for Windows 10 or later to manage domain controllers and other servers that run Windows Server. You can run the Windows Server Remote Server Administration Tools on a computer that runs Windows 10 or later.

[](#add-a-new-domain-controller-with-a-newer-version-of-windows-server)

## Add a new domain controller with a newer version of Windows Server {#add-a-new-domain-controller-with-a-newer-version-of-windows-server .heading-anchor}

The following example shows how to upgrade the Contoso forest from a previous version of Windows Server to a later version.

1.  Join the new Windows Server to your forest. Restart when you\'re prompted.

2.  Sign in to the new Windows Server with a domain admin account.

3.  In **Server Manager**, under **Add Roles and Features**, install **Active Directory Domain Services** on the new Windows Server. This action automatically runs adprep on the earlier version forest and domain.

4.  In **Server Manager**, select the yellow triangle. From the drop-down, select **Promote the server to a domain controller**.

5.  On the **Deployment Configuration** screen, select **Add a domain controller to an existing domain** and click next.

6.  On the **Domain Controller options** screen, enter the **Directory Services Restore Mode (DSRM)** password and select **Next**.

7.  For the rest of the screens, select **Next**.

8.  On the **Prerequisite Check** screen, select **Install**. After the restart has completed, sign in again.

9.  On the earlier version of Windows Server, in **Server Manager**, under **Tools**, select **Active Directory Module for Windows PowerShell**.

10. In the PowerShell window, use the `Move-ADDirectoryServerOperationMasterRole` cmdlet to move the FSMO roles. You can enter the name of each Operation Master Role or use numbers to specify the roles. For more information, see [Move-ADDirectoryServerOperationMasterRole](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd464018(v=ws.10)).

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    Move-ADDirectoryServerOperationMasterRole -Identity "DC-W2K16" -OperationMasterRole 0,1,2,3,4
    ```

11. To verify the roles were moved, go to the new Windows Server. In **Server Manager**, under **Tools**, select **Active Directory Module for Windows PowerShell**. Use the `Get-ADDomain` and `Get-ADForest` cmdlets to view the FSMO role holders.

12. Demote and remove the earlier Windows Server DC. For information on how to demote a DC, see [Demoting domain controllers and domains](demoting-domain-controllers-and-domains--level-200-).

13. After the server is demoted and removed, you can [raise the forest functional and domain functional levels](/en-us/troubleshoot/windows-server/identity/raise-active-directory-domain-forest-functional-levels) to the latest version of Windows Server.

[](#next-steps)

## Next steps {#next-steps .heading-anchor}

-   [What\'s new in Active Directory Domain Services installation and removal](what-s-new-in-active-directory-domain-services-installation-and-removal)
-   [Install Active Directory Domain Services (Level 100)](install-active-directory-domain-services--level-100-)
-   [Windows Server functional levels](../active-directory-functional-levels)

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

-   [Active Directory Domain Services Functional Levels](/en-us/windows-server/identity/ad-ds/active-directory-functional-levels?source=recommendations)

    Discover the capabilities of Active Directory Domain Services functional levels and learn how they impact domain controllers and Windows Server compatibility.

-   [How to raise Active Directory domain and forest functional levels - Windows Server](/en-us/troubleshoot/windows-server/active-directory/raise-active-directory-domain-forest-functional-levels?source=recommendations)

    Describes how to raise Active Directory domain and forest functional levels.

-   [Raise Domain and Forest Functional Levels in AD DS on Windows Server](/en-us/windows-server/identity/ad-ds/plan/raise-domain-forest-functional-levels?source=recommendations)

    Learn how to raise domain and forest functional levels in Active Directory Domain Services on Windows Server.

-   [Learn about upgrading your domain and forest functional levels in Active Directory Domain Services.](/en-us/windows-server/identity/ad-ds/plan/identifying-your-functional-level-upgrade?source=recommendations)

    Upgrade your domain and forest functional level in Active Director Domain Services for Windows Server

-   [Upgrade and migrate roles and features in Windows Server](/en-us/windows-server/get-started/upgrade-migrate-roles-features?source=recommendations)

    Upgrade Windows Server with confidence. Learn about supported upgrade paths, and migration tools for a smooth transition.

-   [Upgrade Domain Controllers to Windows Server 2012 R2 and Windows Server 2012](/en-us/windows-server/identity/ad-ds/deploy/upgrade-domain-controllers-to-windows-server-2012-r2-and-windows-server-2012?source=recommendations)

    Learn more about upgrading domain controllers to Windows Server 2012 R2 and Windows Server 2012

Training

Module

[Active Directory Domain Services migration - Training](/en-us/training/modules/active-directory-domain-services-migration/?source=recommendations)

Determine the best approach to moving domain controllers to Windows Server 2025.

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 09/16/2026
