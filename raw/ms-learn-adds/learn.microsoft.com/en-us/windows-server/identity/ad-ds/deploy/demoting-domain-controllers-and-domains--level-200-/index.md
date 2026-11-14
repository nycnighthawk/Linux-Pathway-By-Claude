---
{"title": "Demote domain controllers and domains", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/demoting-domain-controllers-and-domains--level-200-", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Demote domain controllers and domains

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

This article explains how to remove Active Directory Domain Services (AD DS) by using Server Manager or Windows PowerShell.

[](#ad-ds-removal-workflow)

## AD DS removal workflow {#ad-ds-removal-workflow .heading-anchor}

The following workflow diagram shows the steps to remove AD DS.

Caution

Removing the AD DS roles with Dism.exe or the Windows PowerShell DISM module after promotion to a domain controller (DC) isn\'t supported and prevents the server from booting normally.

Unlike Server Manager and the ADDSDeployment module for Windows PowerShell, DISM is a native servicing system that has no inherent knowledge of AD DS or its configuration. We don\'t recommend using Dism.exe or the Windows PowerShell DISM module to uninstall the AD DS role unless the server is no longer a domain controller.

[](#demotion-and-role-removal-by-using-powershell)

## Demotion and role removal by using PowerShell {#demotion-and-role-removal-by-using-powershell .heading-anchor}

+------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| ADDSDeployment and ServerManager cmdlets       | Arguments (Bold arguments are required. *Italicized* arguments can be specified via Windows PowerShell or the AD DS Configuration Wizard.) |
+================================================+============================================================================================================================================+
| Uninstall-ADDSDomainController                 | -SkipPreChecks                                                                                                                             |
|                                                |                                                                                                                                            |
|                                                | *-LocalAdministratorPassword*                                                                                                              |
|                                                |                                                                                                                                            |
|                                                | -Confirm                                                                                                                                   |
|                                                |                                                                                                                                            |
|                                                | ***-Credential***                                                                                                                          |
|                                                |                                                                                                                                            |
|                                                | -DemoteOperationMasterRole                                                                                                                 |
|                                                |                                                                                                                                            |
|                                                | *-DNSDelegationRemovalCredential*                                                                                                          |
|                                                |                                                                                                                                            |
|                                                | -Force                                                                                                                                     |
|                                                |                                                                                                                                            |
|                                                | *-ForceRemoval*                                                                                                                            |
|                                                |                                                                                                                                            |
|                                                | *-IgnoreLastDCInDomainMismatch*                                                                                                            |
|                                                |                                                                                                                                            |
|                                                | *-IgnoreLastDNSServerForZone*                                                                                                              |
|                                                |                                                                                                                                            |
|                                                | *-LastDomainControllerInDomain*                                                                                                            |
|                                                |                                                                                                                                            |
|                                                | -Norebootoncompletion                                                                                                                      |
|                                                |                                                                                                                                            |
|                                                | *-RemoveApplicationPartitions*                                                                                                             |
|                                                |                                                                                                                                            |
|                                                | *-RemoveDNSDelegation*                                                                                                                     |
|                                                |                                                                                                                                            |
|                                                | -RetainDCMetadata                                                                                                                          |
+------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Uninstall-WindowsFeature/Remove-WindowsFeature | ***-Name***                                                                                                                                |
|                                                |                                                                                                                                            |
|                                                | ***-IncludeManagementTools***                                                                                                              |
|                                                |                                                                                                                                            |
|                                                | *-Restart*                                                                                                                                 |
|                                                |                                                                                                                                            |
|                                                | -Remove                                                                                                                                    |
|                                                |                                                                                                                                            |
|                                                | -Force                                                                                                                                     |
|                                                |                                                                                                                                            |
|                                                | -ComputerName                                                                                                                              |
|                                                |                                                                                                                                            |
|                                                | -Credential                                                                                                                                |
|                                                |                                                                                                                                            |
|                                                | -LogPath                                                                                                                                   |
|                                                |                                                                                                                                            |
|                                                | -Vhd                                                                                                                                       |
+------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+

To learn more about how to demote your DC by using PowerShell, see [Uninstall-ADDSDomainController](/en-us/powershell/module/addsdeployment/uninstall-addsdomaincontroller) and [Uninstall-WindowsFeature](/en-us/powershell/module/servermanager/uninstall-windowsfeature).

`Uninstall-ADDSDomainController` and `Uninstall-WindowsFeature` only require the minimum arguments because they each perform a single action. Selecting the **Enter** key during the confirmation phase initiates the irrevocable demotion process and restarts your device.

The **Credential** argument is only required if you aren\'t already signed in as a member of the Enterprise Admins group or the Domain Admins group. The **IncludeManagementTools** argument is only required if you want to remove all of the AD DS management utilities.

[](#demote)

## Demote {#demote .heading-anchor}

[](#remove-roles-and-features)

### Remove roles and features {#remove-roles-and-features .heading-anchor}

There are two methods you can use to remove the AD DS role:

-   On the **Manage** menu on the main dashboard, select **Remove Roles and Features**:

-   Select **AD DS** or **All Servers** on the navigation pane. Scroll down to the **Roles and Features** section. Right-click **Active Directory Domain Services** in the **Roles and Features** list and select **Remove Roles or Features**. This interface skips the **Server Selection** page.

The ServerManager cmdlets **Uninstall-WindowsFeature** and **Remove-WindowsFeature** prevent you from removing the AD DS role until you demote the domain controller.

[](#server-selection)

### Server Selection {#server-selection .heading-anchor}

The **Server Selection** section enables you to choose from one of the servers previously added to the pool, as long as it\'s accessible. The local server running Server Manager is always automatically available.

[](#server-roles-and-features)

### Server roles and features {#server-roles-and-features .heading-anchor}

Clear the **Active Directory Domain Services** checkbox to demote a domain controller. If the server is currently a domain controller, this action doesn\'t remove the AD DS role. Instead, it presents a **Validation Results** dialog that lets you demote the server. If the server is a domain controller, this action removes the binaries like any other role feature.

-   Don\'t remove any other AD DS-related roles or features - such as DNS, GPMC, or the RSAT tools - if you intend to promote the domain controller again immediately. Removing other roles and features increases the time to repromote because Server Manager reinstalls these features when you reinstall the role.
-   Remove unneeded AD DS roles and features at your own discretion if you intend to demote the domain controller permanently. To remove roles and features, clear the appropriate checkboxes.

Here\'s the full list of AD DS-related roles and features:

-   Active Directory Module for Windows PowerShell feature
-   AD DS and AD LDS Tools feature
-   Active Directory Administrative Center feature
-   AD DS Snap-ins and Command-line Tools feature
-   DNS Server
-   Group Policy Management Console

The equivalent ADDSDeployment and ServerManager Windows PowerShell cmdlets are:

PowerShell

``` {.inner-focus data-language="powershell"}
Uninstall-ADDSDomainController
Uninstall-WindowsFeature
```

[](#credentials)

### Credentials {#credentials .heading-anchor}

You configure demotion options on the **Credentials** page. Provide the credentials necessary to perform the demotion from the following list:

-   Demoting an extra domain controller requires Domain Admin credentials. Selecting **Force the removal of this domain controller** demotes the domain controller without removing the domain controller object\'s metadata from Active Directory.

    Warning

    Don\'t select this option unless the domain controller can\'t contact other domain controllers and there\'s no reasonable way to resolve that network issue. Forced demotion leaves orphaned metadata in Active Directory on the remaining domain controllers in the forest. In addition, all unreplicated changes on that domain controller, such as passwords or new user accounts, are lost forever. Orphaned metadata is the root cause in a significant percentage of Microsoft customer support cases for AD DS, Exchange, SQL Server, and other software.

    If you forcibly demote a domain controller, you must manually perform metadata cleanup immediately. For more information, see [Clean Up Server Metadata](ad-ds-metadata-cleanup).

-   Demoting the last domain controller in a domain requires Enterprise Admins group membership because doing so removes the domain itself. (If the domain is the last one in the forest, this action removes the forest.) Server Manager informs you if the current domain controller is the last domain controller in the domain. Select the **Last domain controller in the domain** checkbox to confirm that the domain controller is the last domain controller in the domain.

The equivalent ADDSDeployment Windows PowerShell arguments are:

PowerShell

``` {.inner-focus data-language="powershell"}
-Credential <PSCredential>
-ForceRemoval <{ $true | $false }>
-LastDomainControllerInDomain <{ $true | $false }>
```

[](#warnings)

### Warnings {#warnings .heading-anchor}

The **Warnings** page alerts you to the possible consequences of removing the domain controller. To continue, you must select **Proceed with removal**.

If you previously selected **Force the removal of this domain controller** on the **Credentials** page, the **Warnings** page shows all Flexible Single Master Operations roles hosted by the domain controller. You must seize the roles from another domain controller immediately after demoting the server. For more information on seizing FSMO roles, see [Seize the Operations Master Role](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc816779(v=ws.10)).

This page doesn\'t have an equivalent ADDSDeployment Windows PowerShell argument.

[](#removal-options)

### Removal Options {#removal-options .heading-anchor}

The **Removal Options** page appears if you select **Last domain controller in the domain** on the **Credentials** page. This page enables you to configure extra removal options. Select **Ignore last DNS server for zone**, **Remove application partitions**, and **Remove DNS Delegation** to enable the **Next** button.

The options only appear if applicable to the domain controller. For instance, if there\'s no DNS delegation for the server, that checkbox doesn\'t appear.

Select **Change** to specify alternative DNS administrative credentials. Select **View Partitions** to view extra partitions that the wizard removes during the demotion. By default, the only other partitions are Domain DNS and Forest DNS Zones. All other partitions are non-Windows partitions.

The equivalent ADDSDeployment cmdlet arguments are:

PowerShell

``` {.inner-focus data-language="PowerShell"}
-IgnoreLastDnsServerForZone <{ $true | false }>
-RemoveApplicationPartitions <{ $true | false }>
-RemoveDNSDelegation <{ $true | false }>
-DNSDelegationRemovalCredential <PsCredential>
```

[](#new-administrator-password)

### New Administrator Password {#new-administrator-password .heading-anchor}

The **New Administrator Password** page requires you to provide a password for the built-in local computer\'s Administrator account after the demotion completes and the computer becomes a domain member server or workgroup computer.

The **Uninstall-ADDSDomainController** cmdlet and arguments use the same defaults as Server Manager, if the values aren\'t specified.

The **LocalAdministratorPassword** argument is special:

-   If this argument isn\'t specified, the cmdlet prompts you to enter and confirm a masked password. This is the preferred usage when running the cmdlet interactively.
-   If the argument is specified with a value, the value must be a secure string. This isn\'t the preferred usage when running the cmdlet interactively.

For example, you can manually prompt for a password by using the **Read-Host** cmdlet to prompt the user for a secure string:

PowerShell

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
Uninstall-ADDSDomainController -LocalAdministratorPassword (Read-Host -Prompt "Password:" -AsSecureString)
```

Because the previous two options don\'t confirm the password, use extreme caution. The password isn\'t visible.

You can also provide a secure string as a converted clear-text variable, although this is highly discouraged. For example:

PowerShell

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
Uninstall-ADDSDomainController -LocalAdministratorPassword (ConvertTo-SecureString "Password1" -AsPlainText -Force)
```

Providing or storing a clear text password isn\'t recommended. Anyone running this command in a script or looking over your shoulder will know the local administrator password of the computer. With that knowledge, they have access to all of its data and can impersonate the server itself.

[](#confirmation)

### Confirmation {#confirmation .heading-anchor}

The **Confirmation** page shows the planned demotion. The page doesn\'t list demotion configuration options. This is the last page the wizard shows before the demotion begins. The **View script** button creates a Windows PowerShell demotion script.

Select **Demote** to run the following AD DS Deployment cmdlet:

PowerShell

``` {.inner-focus data-language="powershell"}
Uninstall-ADDSDomainController
```

Use the optional **Whatif** argument with the **Uninstall-ADDSDomainController** cmdlet to review configuration information. This enables you to see the explicit and implicit values of a cmdlet\'s arguments.

For example:

The prompt to restart is your last opportunity to cancel the operation when using ADDSDeployment Windows PowerShell. To override that prompt, use the **-force** or **confirm:\$false** arguments.

[](#demotion)

### Demotion {#demotion .heading-anchor}

When the **Demotion** page appears, the domain controller configuration begins and can\'t be halted or canceled. Detailed operations appear on this page and write to logs:

-   %systemroot%\\debug\\dcpromo.log
-   %systemroot%\\debug\\dcpromoui.log

To accept the reboot prompt automatically, use the **-force** or **-confirm:\$false** arguments with any ADDSDeployment Windows PowerShell cmdlet. To prevent the server from automatically rebooting at the end of promotion, use the **-norebootoncompletion:\$false** argument.

Warning

We don\'t recommend overriding the reboot. The member server must reboot to function correctly.

Here\'s an example of forced demotion with the minimum required arguments of **-forceremoval** and **-demoteoperationmasterrole**. The **-credential** argument isn\'t required because the user signed on as a member of the Enterprise Admins group:

Here\'s an example of removing the last domain controller in the domain, with the minimum required arguments of **-lastdomaincontrollerindomain** and **-removeapplicationpartitions**:

If you attempt to remove the AD DS role before demoting the server, Windows PowerShell blocks you with an error:

Important

You must restart the computer after demoting the server before you can remove the AD-Domain-Services role binaries.

[](#results)

### Results {#results .heading-anchor}

The **Results** page shows the success or failure of the promotion and any important administrative information. The domain controller automatically reboots after 10 seconds.

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

-   [Clean up AD DS server metadata](/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup?source=recommendations)

    Use built-in tools to clean up metadata from removed domain controllers

-   [Troubleshoot domain controller deployment - Windows Server](/en-us/troubleshoot/windows-server/active-directory/troubleshoot-domain-controller-deployment?source=recommendations)

    Provides information about troubleshooting domain controller deployment.

-   [Domain controllers don\'t demote - Windows Server](/en-us/troubleshoot/windows-server/active-directory/domain-controllers-not-demote?source=recommendations)

    Fixes the problem where domain controllers may not demote gracefully when you use the Active Directory Installation Wizard (Dcpromo.exe) to force demotion if a required dependency or operation fails in Windows Server 2003 or in Windows 2000 Server.

-   [View and transfer FSMO roles - Windows Server](/en-us/troubleshoot/windows-server/active-directory/view-transfer-fsmo-roles?source=recommendations)

    Describes how to view and transfer FSMO roles.

-   [Diagnose AD replication failures - Windows Server](/en-us/troubleshoot/windows-server/active-directory/diagnose-replication-failures?source=recommendations)

    Describes how to diagnose Active Directory replication failures.

-   [Transfer or seize Operation Master roles - Windows Server](/en-us/troubleshoot/windows-server/active-directory/transfer-or-seize-operation-master-roles-in-ad-ds?source=recommendations)

    Describes how you can use the Ntdsutil.exe utility to move or to seize Operation Master roles, formerly known as Flexible Single Master Operations (FSMO) roles.

Training

Module

[Manage AD DS domain controllers and FSMO roles - Training](/en-us/training/modules/manage-active-directory-domain-services-flexible-single-master-operation-roles/?source=recommendations)

Learn how to deploy and manage AD DS domain controllers, maintain availability with backup and recovery, manage the global catalog role, and transfer or seize FSMO roles including schema master, domain-naming master, RID master, infrastructure master, and PDC emulator.

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 07/11/2025
