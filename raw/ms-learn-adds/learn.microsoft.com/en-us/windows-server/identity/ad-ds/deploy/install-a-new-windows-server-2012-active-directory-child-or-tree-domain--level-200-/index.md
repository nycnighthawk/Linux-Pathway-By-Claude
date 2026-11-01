---
{"title": "Install a New Windows Server 2012 Active Directory Child or Tree Domain (Level 200)", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-a-new-windows-server-2012-active-directory-child-or-tree-domain--level-200-", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Install a New Windows Server 2012 Active Directory Child or Tree Domain (Level 200)

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

This topic explains how to add child and tree domains to an existing Windows Server 2012 forest, using Server Manager or Windows PowerShell.

-   [Child and Tree Domain Workflow](install-a-new-windows-server-2012-active-directory-child-or-tree-domain--level-200-#BKMK_Workflow)

-   [Child and Tree Domain Windows PowerShell](install-a-new-windows-server-2012-active-directory-child-or-tree-domain--level-200-#BKMK_PS)

-   [Deployment](install-a-new-windows-server-2012-active-directory-child-or-tree-domain--level-200-#BKMK_Deployment)

[](#BKMK_Workflow)

## Child and Tree Domain Workflow {#BKMK_Workflow .heading-anchor}

The following diagram illustrates the Active Directory Domain Services configuration process when you previously installed the AD DS role and you have started the Active Directory Domain Services Configuration Wizard using Server Manager to create a new domain in an existing forest.

[](#BKMK_PS)

## Child and Tree Domain Windows PowerShell {#BKMK_PS .heading-anchor}

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ADDSDeployment Cmdlet             | Arguments (**Bold** arguments are required. *Italicized* arguments can be specified by using Windows PowerShell or the AD DS Configuration Wizard.) |
+===================================+=====================================================================================================================================================+
| **Install-AddsDomain**            | -SkipPreChecks                                                                                                                                      |
|                                   |                                                                                                                                                     |
|                                   | ***-NewDomainName***                                                                                                                                |
|                                   |                                                                                                                                                     |
|                                   | ***-ParentDomainName***                                                                                                                             |
|                                   |                                                                                                                                                     |
|                                   | ***-SafeModeAdministratorPassword***                                                                                                                |
|                                   |                                                                                                                                                     |
|                                   | *-ADPrepCredential*                                                                                                                                 |
|                                   |                                                                                                                                                     |
|                                   | -AllowDomainReinstall                                                                                                                               |
|                                   |                                                                                                                                                     |
|                                   | -Confirm                                                                                                                                            |
|                                   |                                                                                                                                                     |
|                                   | *-CreateDNSDelegation*                                                                                                                              |
|                                   |                                                                                                                                                     |
|                                   | ***-Credential***                                                                                                                                   |
|                                   |                                                                                                                                                     |
|                                   | *-DatabasePath*                                                                                                                                     |
|                                   |                                                                                                                                                     |
|                                   | *-DNSDelegationCredential*                                                                                                                          |
|                                   |                                                                                                                                                     |
|                                   | -NoDNSOnNetwork                                                                                                                                     |
|                                   |                                                                                                                                                     |
|                                   | *-DomainMode*                                                                                                                                       |
|                                   |                                                                                                                                                     |
|                                   | ***-DomainType***                                                                                                                                   |
|                                   |                                                                                                                                                     |
|                                   | -Force                                                                                                                                              |
|                                   |                                                                                                                                                     |
|                                   | *-InstallDNS*                                                                                                                                       |
|                                   |                                                                                                                                                     |
|                                   | *-LogPath*                                                                                                                                          |
|                                   |                                                                                                                                                     |
|                                   | *-NewDomainNetBIOSName*                                                                                                                             |
|                                   |                                                                                                                                                     |
|                                   | *-NoGlobalCatalog*                                                                                                                                  |
|                                   |                                                                                                                                                     |
|                                   | -NoNorebootoncompletion                                                                                                                             |
|                                   |                                                                                                                                                     |
|                                   | *-ReplicationSourceDC*                                                                                                                              |
|                                   |                                                                                                                                                     |
|                                   | *-SiteName*                                                                                                                                         |
|                                   |                                                                                                                                                     |
|                                   | -SkipAutoConfigureDNS                                                                                                                               |
|                                   |                                                                                                                                                     |
|                                   | *-SYSVOLPath*                                                                                                                                       |
|                                   |                                                                                                                                                     |
|                                   | *-Whatif*                                                                                                                                           |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

Note

The **-credential** argument is only required when you are not currently logged on as a member of the Enterprise Admins group.The **-NewDomainNetBIOSName** argument is required if you want to change the automatically generated 15-character name based on the DNS domain name prefix or if the name exceeds 15 characters.

[](#BKMK_Deployment)

## Deployment {#BKMK_Deployment .heading-anchor}

[](#deployment-configuration)

### Deployment Configuration {#deployment-configuration .heading-anchor}

The following screenshot shows the options for adding a child domain:

The following screenshot shows the options for adding a tree domain:

Server Manager begins every domain controller promotion with the **Deployment Configuration** page. The remaining options and required fields change on this page and subsequent pages, depending on which deployment operation you select.

This topic combines two discrete operations: child domain promotion and tree domain promotion. The only difference between the two operations is the domain type that you choose to create. All of the other steps are identical between the two operations.

-   To create a new child domain, click **Add a domain to an existing Forest** and choose **Child Domain**. For **Parent domain name**, type or select the name of the parent domain. Then type the name of the new domain in the **New domain name** box. Provide a valid, single-label child domain name; the name must use DNS domain name requirements.

-   To create a tree domain within an existing forest, click **Add a domain to an existing Forest** and choose **Tree Domain**. Type the name of the forest root domain, and then type the name of the new domain. Provide a valid, fully qualified root domain name; the name cannot be single-labeled and must use DNS domain name requirements.

For more information about DNS names, see [Naming conventions in Active Directory for computers, domains, sites, and OUs](https://support.microsoft.com/kb/909264).

The Server Manager Active Directory Domain Services Configuration Wizard prompts you for domain credentials if your current credentials are not from the domain. Click **Change** to provide domain credentials for the promotion operation.

The Deployment Configuration ADDSDeployment cmdlet and arguments are:

``` {.inner-focus data-language=""}
Install-AddsDomain
-domaintype <{childdomain | treedomain}>
-parentdomainname <string>
-newdomainname <string>
-credential <pscredential>
```

[](#domain-controller-options)

### Domain Controller Options {#domain-controller-options .heading-anchor}

The **Domain Controller Options** page specifies the domain controller options for the new domain controller. The configurable domain controller options include **DNS server** and **Global Catalog**; you cannot configure read-only domain controller as the first domain controller in a new domain.

Microsoft recommends that all domain controllers provide DNS and GC services for high availability in distributed environments. GC is always selected by default and DNS is selected by default if the current domain hosts DNS already on its DCs, based on a Start-of-Authority query. You must also specify a **Domain functional level**. The default functional level is Windows Server 2012, and you can choose any other value that is equal to or greater than the current forest functional level.

The **Domain Controller Options** page also enables you to choose the appropriate Active Directory logical **site name** from the forest configuration. By default, the site with the most correct subnet is selected. If there is only one site, it is selected automatically.

Important

If the server does not belong to an Active Directory subnet and there is more than one Active Directory site, nothing is selected and the **Next** button is unavailable until you choose a site from the list.

The specified **Directory Services Restore Mode Password** must adhere to the password policy applied to the server. Always choose a strong, complex password or preferably, a passphrase.

The **Domain Controller Options** ADDSDeployment cmdlet arguments are:

``` {.inner-focus data-language=""}
-InstallDNS <{$false | $true}>
-NoGlobalCatalog <{$false | $true}>
-DomainMode <{Win2003 | Win2008 | Win2008R2 | Win2012 | Default}>
-Sitename <string>
-SafeModeAdministratorPassword <secure string>
-Credential <pscredential>
```

Important

The site name must already exist when provided as a value to the **sitename** argument. The **install-AddsDomainController** cmdlet does not create site names. You can use the **new-adreplicationsite** cmdlet to create new sites.

The **Install-ADDSDomainController** cmdlet arguments follow the same defaults as Server Manager if not specified.

The **SafeModeAdministratorPassword** argument\'s operation is special:

-   If *not specified* as an argument, the cmdlet prompts you to enter and confirm a masked password. This is the preferred usage when running the cmdlet interactively.

    For example, to create a new child domain named NorthAmerica in the Contoso.com forest and be prompted to enter and confirm a masked password:

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language=""}
    Install-ADDSDomain "NewDomainName NorthAmerica "ParentDomainName Contoso.com "DomainType Child
    ```

-   If specified *with a value*, the value must be a secure string. This is not the preferred usage when running the cmdlet interactively.

For example, you can manually prompt for a password by using the **Read-Host** cmdlet to prompt the user for a secure string:

``` {.inner-focus data-language=""}
-safemodeadministratorpassword (read-host -prompt "Password:" -assecurestring)
```

Warning

As the previous option does not confirm the password, use extreme caution: the password is not visible.

You can also provide a secure string as a converted clear-text variable, although this is highly discouraged.

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language=""}
-safemodeadministratorpassword (convertto-securestring "Password1" -asplaintext -force)
```

Finally, you could store the obfuscated password in a file, and then reuse it later, without the clear text password ever appearing. For example:

``` {.inner-focus data-language=""}
$file = "c:\pw.txt"
$pw = read-host -prompt "Password:" -assecurestring
$pw | ConvertFrom-SecureString | Set-Content $file

-safemodeadministratorpassword (Get-Content $File | ConvertTo-SecureString)
```

Warning

Providing or storing a clear or obfuscated text password is not recommended. Anyone running this command in a script or looking over your shoulder knows the DSRM password of that domain controller. Anyone with access to the file could reverse that obfuscated password. With that knowledge, they can logon to a DC started in DSRM and eventually impersonate the domain controller itself, elevating their privileges to the highest level in an AD forest. An additional set of steps using **System.Security.Cryptography** to encrypt the text file data is advisable but out of scope. The best practice is to totally avoid password storage.

The ADDSDeployment module offers an additional option to skip automatic configuration of DNS client settings, forwarders, and root hints. This is not configurable when using Server Manager. This argument matters only if you already installed the DNS Server service prior to configuring the domain controller:

``` {.inner-focus data-language=""}
-SkipAutoConfigureDNS
```

[](#dns-options-and-dns-delegation-credentials)

### DNS Options and DNS Delegation Credentials {#dns-options-and-dns-delegation-credentials .heading-anchor}

The **DNS Options** page enables you to provide alternate DNS Admin credentials for delegation.

When installing a new domain in an existing forest - where you selected DNS installation on the **Domain Controller Options** page - you cannot configure any options; the delegation happens automatically and irrevocably. You have the option to provide alternate DNS administrative credentials with rights to update that structure.

The **DNS Options** ADDSDeployment Windows PowerShell arguments are:

``` {.inner-focus data-language=""}
-creatednsdelegation
-dnsdelegationcredential <pscredential>
```

For more information about DNS delegation, see [Understanding Zone Delegation](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc771640(v=ws.11)).

[](#additional-options)

### Additional Options {#additional-options .heading-anchor}

The **Additional Options** page shows the NetBIOS name of the domain and enables you to override it. By default, the NetBIOS domain name matches the left-most label of the fully qualified domain name provided on the **Deployment Configuration** page. For example, if you provided the fully qualified domain name of corp.contoso.com, the default NetBIOS domain name is CORP.

If the name is 15 characters or less and does not conflict with another NetBIOS name, it is unaltered. If it does conflict with another NetBIOS name, a number is appended to the name. If the name is more than 15 characters, the wizard provides a unique, truncated suggestion. In either case, the wizard first validates the name is not already in use via a WINS lookup and NetBIOS broadcast.

For more information about DNS names, see [Naming conventions in Active Directory for computers, domains, sites, and OUs](https://support.microsoft.com/kb/909264).

The **Install-AddsDomain** arguments follow the same defaults as Server Manager if not specified. The **DomainNetBIOSName** operation is special:

1.  If the **NewDomainNetBIOSName** argument is not specified with a NetBIOS domain name and the single-label prefix domain name in the **DomainName** argument is 15 characters or fewer, then promotion continues with an automatically generated name.

2.  If the **NewDomainNetBIOSName** argument is not specified with a NetBIOS domain name and the single-label prefix domain name in the **DomainName** argument is 16 characters or more, then promotion fails.

3.  If the **NewDomainNetBIOSName** argument is specified with a NetBIOS domain name of 15 characters or fewer, then promotion continues with that specified name.

4.  If the **NewDomainNetBIOSName** argument is specified with a NetBIOS domain name of 16 characters or more, then promotion fails.

The **Additional Options** ADDSDeployment cmdlet argument is:

``` {.inner-focus data-language=""}
-newdomainnetbiosname <string>
```

[](#paths)

### Paths {#paths .heading-anchor}

The **Paths** page enables you to override the default folder locations of the AD DS database, the data base transaction logs, and the SYSVOL share. The default locations are always in subdirectories of %systemroot%.

The **Paths** ADDSDeployment cmdlet arguments are:

``` {.inner-focus data-language=""}
-databasepath <string>
-logpath <string>
-sysvolpath <string>
```

[](#review-options-and-view-script)

### Review Options and View Script {#review-options-and-view-script .heading-anchor}

The **Review Options** page enables you to validate your settings and ensure they meet your requirements before you start the installation. This is not the last opportunity to stop the installation when using Server Manager. This is simply an option to confirm your settings before continuing the configuration

The **Review Options** page in Server Manager also offers an optional **View Script** button to create a Unicode text file that contains the current ADDSDeployment configuration as a single Windows PowerShell script. This enables you to use the Server Manager graphical interface as a Windows PowerShell deployment studio. Use the Active Directory Domain Services Configuration Wizard to configure options, export the configuration, and then cancel the wizard. This process creates a valid and syntactically correct sample for further modification or direct use. For example:

``` {.inner-focus data-language=""}
#
# Windows PowerShell Script for AD DS Deployment
#

Import-Module ADDSDeployment
Install-ADDSDomain `
-NoGlobalCatalog:$false `
-CreateDNSDelegation `
-Credential (Get-Credential) `
-DatabasePath "C:\Windows\NTDS" `
-DomainMode "Win2012" `
-DomainType "ChildDomain" `
-InstallDNS:$true `
-LogPath "C:\Windows\NTDS" `
-NewDomainName "research" `
-NewDomainNetBIOSName "RESEARCH" `
-ParentDomainName "corp.contoso.com" `
-Norebootoncompletion:$false `
-SiteName "Default-First-Site-Name" `
-SYSVOLPath "C:\Windows\SYSVOL"
-Force:$true
```

Note

Server Manager generally fills in all arguments with values when promoting and does not rely on defaults (as they may change between future versions of Windows or service packs). The one exception to this is the **-safemodeadministratorpassword** argument (which is deliberately omitted from the script). To force a confirmation prompt, omit the value when running cmdlet interactively.

Use the optional **Whatif** argument with the **Install-ADDSForest** cmdlet to review configuration information. This enables you to see the explicit and implicit values of the arguments for a cmdlet.

[](#prerequisites-check)

### Prerequisites Check {#prerequisites-check .heading-anchor}

The **Prerequisites Check** is a new feature in AD DS domain configuration. This new phase validates that the server configuration is capable of supporting a new AD DS domain.

When installing a new forest root domain, the Server Manager Active Directory Domain Services Configuration Wizard invokes a series of serialized modular tests. These tests alert you with suggested repair options. You can run the tests as many times as required. The domain controller process cannot continue until all prerequisite tests pass.

The **Prerequisites Check** also surfaces relevant information such as security changes that affect older operating systems.

For more information on the specific prerequisite checks, see [Prerequisite Checking](../manage/ad-ds-simplified-administration#BKMK_PrerequisiteChecking).

You cannot bypass the **Prerequisite Check** when using Server Manager, but you can skip the process when using the AD DS Deployment cmdlet using the following argument:

``` {.inner-focus data-language=""}
-skipprechecks
```

Warning

Microsoft discourages skipping the prerequisite check as it can lead to a partial domain controller promotion or damaged AD DS forest.

Click **Install** to begin the domain controller promotion process. This is last opportunity to cancel the installation. You cannot cancel the promotion process once it begins. The computer will reboot automatically at the end of promotion, regardless of the promotion results.

[](#installation)

### Installation {#installation .heading-anchor}

When the **Installation** page displays, the domain controller configuration begins and cannot be halted or canceled. Detailed operations display on this page and are written to logs:

-   %systemroot%\\debug\\dcpromo.log

-   %systemroot%\\debug\\dcpromoui.log

To install a new Active Directory domain using the ADDSDeployment module, use the following cmdlet:

``` {.inner-focus data-language=""}
Install-addsdomain
```

See [Child and Tree Domain Windows PowerShell](install-a-new-windows-server-2012-active-directory-child-or-tree-domain--level-200-#BKMK_PS) for required and optional arguments.The **Install-addsdomain** cmdlet only has two phases (prerequisite checking and installation). The two figures below show the installation phase with the minimum required arguments of **-domaintype**, **-newdomainname**, **-parentdomainname**, and **-credential**. Note how, just like Server Manager, **Install-ADDSDomain** reminds you that promotion will reboot the server automatically.

To accept the reboot prompt automatically, use the **-force** or **-confirm:\$false** arguments with any ADDSDeployment Windows PowerShell cmdlet. To prevent the server from automatically rebooting at the end of promotion, use the **-norebootoncompletion** argument.

Warning

Overriding the reboot is not recommended. The domain controller must reboot to function correctly

[](#results)

### Results {#results .heading-anchor}

The **Results** page shows the success or failure of the promotion and any important administrative information. The domain controller will automatically reboot after 10 seconds.

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Install Active Directory Domain Services on Windows Server](/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-?source=recommendations)

    Learn more about how to install Active Directory Domain Services in Windows Server using PowerShell, or Server Manager.

-   [Install a New Windows Server 2012 Active Directory Forest (Level 200)](/en-us/windows-server/identity/ad-ds/deploy/install-a-new-windows-server-2012-active-directory-forest--level-200-?source=recommendations)

    Learn more about: Install a New Windows Server 2012 Active Directory Forest (Level 200)

-   [Install a Replica Windows Server 2012 Domain Controller in an Existing Domain (Level 200)](/en-us/windows-server/identity/ad-ds/deploy/install-a-replica-windows-server-2012-domain-controller-in-an-existing-domain--level-200-?source=recommendations)

    Learn more about: Install a Replica Windows Server 2012 Domain Controller in an Existing Domain (Level 200)

-   [AD DS Configuration Wizard Page Descriptions](/en-us/windows-server/identity/ad-ds/deploy/ad-ds-installation-and-removal-wizard-page-descriptions?source=recommendations)

    Find out about the Active Directory Domain Services Configuration Wizard pages that you use to promote a server to a domain controller and to demote a server.

-   [Selecting the Forest Root Domain](/en-us/windows-server/identity/ad-ds/plan/selecting-the-forest-root-domain?source=recommendations)

    Learn more about: Selecting the Forest Root Domain

-   [What\'s New in Active Directory Domain Services Installation and Removal](/en-us/windows-server/identity/ad-ds/deploy/what-s-new-in-active-directory-domain-services-installation-and-removal?source=recommendations)

    Learn more about: What\'s New in Active Directory Domain Services Installation and Removal

-   [Safely virtualizing Active Directory Domain Services (AD DS)](/en-us/windows-server/identity/ad-ds/introduction-to-active-directory-domain-services-ad-ds-virtualization-level-100?source=recommendations)

    USN Rollback and safe virtualization of Active Directory

-   [Virtualized Domain Controller Deployment and Configuration](/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controller-deployment-and-configuration?source=recommendations)

    Learn more about: Virtualized Domain Controller Deployment and Configuration

Training

Module

[Deploy and manage Active Directory Domain Services domain controllers - Training](/en-us/training/modules/deploy-manage-active-directory-domain-services-domain-controllers/?source=recommendations)

This module introduces you to the topology of domain controllers within an Active Directory environment. It also starts you down the path of deploying, managing, and migrating a domain controller between servers.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
