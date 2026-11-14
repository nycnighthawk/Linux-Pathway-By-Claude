---
{"title": "Transfer Flexible Single Master Operations roles", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/manage-fsmo-roles", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Transfer Flexible Single Master Operations roles

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

When you create a new domain, the Active Directory Domain Services Installation Wizard automatically assigns all the domain-level Flexible Single Master Operations (FSMO) to the first domain controller that is created in that domain. When you create a new forest, the wizard also assigns the two forest-level operations master roles to the first domain controller. After the domain is created and functioning, you might want to transfer various operations master roles to different domain controllers to optimize performance and simplify administration.

Consider moving the operations master role or roles when any of the following conditions exist:

-   Inadequate service performance

-   Failure of a domain controller that hosts an operations master role

-   Decommissioning of a domain controller that hosts an operations master role

-   Administrative configuration changes that affect operations master role placement

If an operations master role holder has failed or been decommissioned before you can transfer the role, you must seize and transfer the role to a healthy domain controller. If you can\'t fix the previous role holder, or if you seized the roles, remove the previous role holder from the domain and clean up its metadata. To learn more about metadata cleanup, see [Clean up Active Directory Domain Controller server metadata](../deploy/ad-ds-metadata-cleanup). If you plan to reuse the repaired computer as a domain control, we recommend you format and rebuild the computer instead of restoring the domain controller from a backup. Restored domain controllers would as be role holders again and cause a conflict.

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

Before you transfer an operations master role, you need to complete the following prerequisites.

-   Review the article [Flexible Single Master Operations roles](understand-fsmo-roles) for other considerations before transferring an FSMO role.

-   To transfer the Schema Master role, your account must be a member of the Schema Admins group and should also be a member of the Enterprise Admins group.

-   To transfer the Domain Naming Master role, your account must be a member of the Enterprise Admins group.

-   To transfer the PDC Emulator role, your account must be a member of the Domain Admins group.

-   To transfer the RID Master role, your account must be a member of the Domain Admins group.

-   To transfer the Infrastructure Master role, your account must be a member of the Domain Admins group.

-   Your Active Directory domain is operational and free from replication errors. To learn more about replication errors, see [Diagnose Active Directory replication failures](/en-us/troubleshoot/windows-server/active-directory/diagnose-replication-failures).

[](#find-the-current-role-holders)

## Find the current role holders {#find-the-current-role-holders .heading-anchor}

To determine which domain controller holds a specific operations master role, you can use the Active Directory Users and Computers snap-in or the PowerShell cmdlet `Get-ADDomainController`. To find the current role holders, run the following steps.

1.  Sign on to a computer with the AD DS Remote Server Administration Tools (RSAT) installed.

2.  Open a PowerShell window.

3.  Run the following PowerShell commands to list the domain controllers and their operations master roles. The script lists the domain controllers in the domain and the operations master roles that they hold.

    PowerShell

    ``` {.inner-focus data-language="powershell"}
    $domainControllers = Get-ADDomainController -Filter *
    foreach ($dc in $domainControllers) {
        Write-Output "Name: $($dc.Name)"
        Write-Output "OperationMasterRoles:"
        foreach ($role in $dc.OperationMasterRoles) {
            Write-Output "- $role"
        }
    }
    ```

[](#transfer-schema-master-role)

## Transfer Schema master role {#transfer-schema-master-role .heading-anchor}

To transfer the Schema master role, follow these steps.

1.  Run the following PowerShell command to transfer the Schema Master role to another domain controller. Replace `<TargetServer>` with the name of the domain controller that you want to transfer the role to.

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    Move-ADDirectoryServerOperationMasterRole -Identity <TargetServer> -OperationMasterRole SchemaMaster
    ```

2.  When prompted, type **Yes** or Y to confirm the transfer.

3.  To confirm that the Schema Master role has been transferred, run the following PowerShell command:

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    Get-ADDomainController -Identity <TargetServer> | Select-Object OperationMasterRoles
    ```

If the domain controller that currently holds the Schema Master role has failed, you can use the `Move-ADDirectoryServerOperationMasterRole` with the **Force** parameter to seize the role and move it to a functional domain controller.

[](#transfer-domain-naming-master-role)

## Transfer Domain Naming Master role {#transfer-domain-naming-master-role .heading-anchor}

To transfer the Domain Naming Master role, run the following PowerShell command:

1.  Run the following PowerShell command to transfer the Domain Naming Master role to another domain controller. Replace `<TargetServer>` with the name of the domain controller that you want to transfer the role to.

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    Move-ADDirectoryServerOperationMasterRole -Identity <TargetServer> -OperationMasterRole DomainNamingMaster
    ```

2.  When prompted, type **Yes** or Y to confirm the transfer.

3.  To confirm that the Domain Naming Master role has been transferred, run the following PowerShell command:

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    Get-ADDomainController -Identity <TargetServer> | Select-Object OperationMasterRoles
    ```

If the domain controller that currently holds the Domain Naming Master role has failed, you can use the `Move-ADDirectoryServerOperationMasterRole` with the **Force** parameter to seize the role and move it to a functional domain controller.

[](#transfer-pdc-emulator-role)

## Transfer PDC Emulator role {#transfer-pdc-emulator-role .heading-anchor}

To transfer the PDC Emulator role, run the following PowerShell command:

1.  Run the following PowerShell command to transfer the PDC Emulator role to another domain controller. Replace `<TargetServer>` with the name of the domain controller that you want to transfer the role to.

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    Move-ADDirectoryServerOperationMasterRole -Identity <TargetServer> -OperationMasterRole PDCEmulator
    ```

2.  When prompted, type **Yes** or Y to confirm the transfer.

3.  To confirm that the PDC Emulator role has been transferred, run the following PowerShell command:

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    Get-ADDomainController -Identity <TargetServer> | Select-Object OperationMasterRoles
    ```

If the domain controller that currently holds the PDC Emulator role has failed, you can use the `Move-ADDirectoryServerOperationMasterRole` with the **Force** parameter to seize the role and move it to a functional domain controller.

[](#transfer-rid-master-role)

## Transfer RID Master role {#transfer-rid-master-role .heading-anchor}

To transfer the RID Master role, follow these steps.

1.  Run the following PowerShell command to transfer the RID Master role to another domain controller. Replace `<TargetServer>` with the name of the domain controller that you want to transfer the role to.

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    Move-ADDirectoryServerOperationMasterRole -Identity <TargetServer> -OperationMasterRole RIDMaster
    ```

2.  When prompted, type **Yes** or Y to confirm the transfer.

3.  To confirm that the RID Master role has been transferred, run the following PowerShell command:

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    Get-ADDomainController -Identity <TargetServer> | Select-Object OperationMasterRoles
    ```

If the domain controller that currently holds the RID Master role has failed, you can use the `Move-ADDirectoryServerOperationMasterRole` with the **Force** parameter to seize the role and move it to a functional domain controller.

[](#transfer-infrastructure-master-role)

## Transfer Infrastructure Master role {#transfer-infrastructure-master-role .heading-anchor}

To transfer the Infrastructure Master role, follow these steps.

1.  Run the following PowerShell command to transfer the Infrastructure Master role to another domain controller. Replace `<TargetServer>` with the name of the domain controller that you want to transfer the role to.

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    Move-ADDirectoryServerOperationMasterRole -Identity <TargetServer> -OperationMasterRole InfrastructureMaster
    ```

2.  When prompted, type **Yes** or Y to confirm the transfer.

3.  To confirm that the Infrastructure Master role has been transferred, run the following PowerShell command:

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    Get-ADDomainController -Identity <TargetServer> | Select-Object OperationMasterRoles
    ```

If the domain controller that currently holds the Infrastructure Master role has failed, you can use the `Move-ADDirectoryServerOperationMasterRole` with the **Force** parameter to seize the role and move it to a functional domain controller.

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

-    Last updated on 07/02/2024
