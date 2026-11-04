---
{"title": "Install Active Directory Domain Services", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Install Active Directory Domain Services

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

This topic explains how to install Active Directory Domain Services (AD DS) in Windows Server by using any of the following methods:

-   Windows PowerShell

-   Server Manager

-   RODC installation using the GUI

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

The following credentials are required to run Adprep.exe and install AD DS.

-   To install a new forest, you must be logged on as the local Administrator for the computer.

-   To install a new child domain or new domain tree, you must be logged on as a member of the Enterprise Admins group.

-   To install an additional domain controller in an existing domain, you must be a member of the Domain Admins group.

    Note

    If you don\'t run adprep.exe command separately and you\'re installing the first domain controller that runs Windows Server in an existing domain or forest, you\'re prompted to supply credentials to run Adprep commands. The credential requirements are as follows:

    To introduce the first Windows Server domain controller in the forest, you need to supply credentials for a member of Enterprise Admins group, the Schema Admins group, and the Domain Admins group in the domain that hosts the schema master. To introduce the first Windows Server domain controller in a domain, you need to supply credentials for a member of the Domain Admins group. To introduce the first read-only domain controller (RODC) in the forest, you need to supply credentials for a member of the Enterprise Admins group.

[](#install-ad-ds-by-using-windows-powershell)

## Install AD DS by Using Windows PowerShell {#install-ad-ds-by-using-windows-powershell .heading-anchor}

Start with adding the role using Windows PowerShell. This command installs the AD DS server role and installs the AD DS and Active Directory Lightweight Directory Services (AD LDS) server administration tools, including GUI-based tools such as Active Directory Users and Computers and command-line tools such as dcdia.exe. Server administration tools aren\'t installed by default when you use Windows PowerShell. You need to specify **\"IncludeManagementTools** to manage the local server or install [Remote Server Administration Tools](https://www.microsoft.com/download/details.aspx?id=28972) to manage a remote server.

PowerShell

``` {.inner-focus data-language="powershell"}
Install-WindowsFeature -name AD-Domain-Services -IncludeManagementTools
```

No reboot is required until after the AD DS installation is complete.

You can then run this command to see the available cmdlets in the ADDSDeployment module.

PowerShell

``` {.inner-focus data-language="powershell"}
Get-Command -Module ADDSDeployment
```

To see the list of arguments that can be specified for a cmdlets and syntax:

PowerShell

``` {.inner-focus data-language="powershell"}
Get-Help <cmdlet name>
```

For example, to see the arguments for creating an unoccupied read-only domain controller (RODC) account, type

PowerShell

``` {.inner-focus data-language="powershell"}
Get-Help Add-ADDSReadOnlyDomainControllerAccount
```

You can also download the latest Help examples and concepts for Windows PowerShell cmdlets. For more information, see [about_Updatable_Help](/en-us/powershell/module/microsoft.powershell.core/about/about_updatable_help?view=powershell-5.1&preserve-view=true).

You can run Windows PowerShell cmdlets against remote servers:

-   In Windows PowerShell, use Invoke-Command with the ADDSDeployment cmdlet. For example, to install AD DS on a remote server named ConDC3 in the contoso.com domain, type:

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    Invoke-Command { Install-ADDSDomainController -DomainName contoso.com -Credential (Get-Credential) } -ComputerName ConDC3
    ```

-or-

-   In Server Manager, create a server group that includes the remote server. Right-select the name of the remote server and select **Windows PowerShell**.

To see the full list of ADDSDeployment cmdlets in Windows PowerShell, see [the ADDSDeployment reference](/en-us/powershell/module/addsdeployment).

[](#specify-windows-powershell-credentials)

### Specify Windows PowerShell Credentials {#specify-windows-powershell-credentials .heading-anchor}

You can specify credentials without revealing them in plain text on screen by using [Get-credential](/en-us/previous-versions/dd315327(v=technet.10)).

The operation for the -SafeModeAdministratorPassword and LocalAdministratorPassword arguments is special:

-   If not specified as an argument, the cmdlet prompts you to enter and confirm a masked password. This is the preferred usage when running the cmdlet interactively.

-   If specified with a value, the value must be a secure string. This isn\'t the preferred usage when running the cmdlet interactively.

For example, you can manually prompt for a password by using the **Read-Host** cmdlet to prompt the user for a secure string

PowerShell

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
-SafeModeAdministratorPassword (Read-Host -Prompt "DSRM Password:" -AsSecureString)
```

Warning

The previous option doesn\'t confirm the password, use extreme caution. The password isn\'t visible.

You can also provide a secure string as a converted clear-text variable, although this is highly discouraged:

PowerShell

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
-SafeModeAdministratorPassword (ConvertTo-SecureString "Password1" -AsPlainText -Force)
```

Warning

Providing or storing a clear text password isn\'t recommended. Anyone running this command in a script or looking over your shoulder knows the Directory Services Restore Mode (DSRM) password of that domain controller. With that knowledge, they can impersonate the domain controller itself and elevate their privilege to the highest level in an Active Directory forest.

[](#use-test-cmdlets)

### Use test cmdlets {#use-test-cmdlets .heading-anchor}

Each ADDSDeployment cmdlet has a corresponding test cmdlet. The test cmdlets runs only the prerequisite checks for the installation operation; no installation settings are configured. The arguments for each test cmdlet are the same as for the corresponding installation cmdlet, but **\"SkipPreChecks** isn\'t available for test cmdlets.

  Test cmdlet                                                                                                                                    Description
  ---------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------
  [Test-ADDSForestInstallation](/en-us/powershell/module/addsdeployment/test-addsforestinstallation)                                             Runs the prerequisites for installing a new Active Directory forest.
  [Test-ADDSDomainInstallation](/en-us/powershell/module/addsdeployment/test-addsdomaininstallation)                                             Runs the prerequisites for installing a new domain in Active Directory.
  [Test-ADDSDomainControllerInstallation](/en-us/powershell/module/addsdeployment/test-addsdomaincontrollerinstallation)                         Runs the prerequisites for installing a domain controller in Active Directory.
  [Test-ADDSReadOnlyDomainControllerAccountCreation](/en-us/powershell/module/addsdeployment/test-addsreadonlydomaincontrolleraccountcreation)   Runs the prerequisites for adding a read-only domain controller (RODC) account.

[](#install-a-new-forest-root-domain-using-windows-powershell)

### Install a new forest root domain using Windows PowerShell {#install-a-new-forest-root-domain-using-windows-powershell .heading-anchor}

The cmdlet [Install-ADDSForest](/en-us/powershell/module/addsdeployment/install-addsforest) installs a new forest.

For example, to install a new forest named corp.contoso.com and be securely prompted to provide the DSRM password, type:

PowerShell

``` {.inner-focus data-language="powershell"}
Install-ADDSForest -DomainName "corp.contoso.com"
```

Note

The DNS server is installed by default when you run Install-ADDSForest.

To install a new forest named **corp.contoso.com**, create a DNS delegation in the contoso.com domain, set domain functional level to Windows Server, and set forest functional level to Windows Server 2025, install the Active Directory database and SYSVOL on the D:\\ drive, install the log files on the E:\\ drive, and be prompted to provide the Directory Services Restore Mode password and type:

PowerShell

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
Install-ADDSForest -DomainName corp.contoso.com -CreateDNSDelegation -DomainMode Win2008 -ForestMode Win2025 -DatabasePath "d:\NTDS" -SYSVOLPath "d:\SYSVOL" -LogPath "e:\Logs"
```

[](#install-a-new-child-or-tree-domain-using-windows-powershell)

### Install a new child or tree domain using Windows PowerShell {#install-a-new-child-or-tree-domain-using-windows-powershell .heading-anchor}

Use the cmdlet [Install-ADDSDomain](/en-us/powershell/module/addsdeployment/install-addsdomain) to install a new domain.

Note

The **-credential** argument is only required when you\'re not currently logged on as a member of the Enterprise Admins group.

The **-NewDomainNetBIOSName** argument is required if you want to change the automatically generated 15-character name based on the DNS domain name prefix or if the name exceeds 15 characters.

For example, to use credentials of **corp\\EnterpriseAdmin1** to create a new child domain named **child**, with parent domain named **corp.contoso.com**, install DNS server, create a DNS delegation in the **corp.contoso.com** domain, set domain functional level to **Windows Server 2025**, make the domain controller a global catalog server in a site named **Houston**, use **DC1.corp.contoso.com** as the replication source domain controller, install the Active Directory database and SYSVOL on the D:\\ drive, install the log files on the E:\\ drive, and be prompted to provide the Directory Services Restore Mode password, but not prompted to confirm the command, type:

PowerShell

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
Install-ADDSDomain -SafeModeAdministratorPassword -Credential (get-credential corp\EnterpriseAdmin1) -NewDomainName child -ParentDomainName corp.contoso.com -InstallDNS -CreateDNSDelegation -DomainMode Win2025 -ReplicationSourceDC DC1.corp.contoso.com -SiteName Houston -DatabasePath "d:\NTDS" -SYSVOLPath "d:\SYSVOL" -LogPath "e:\Logs" -Confirm:$False
```

[](#install-an-additional-replica-domain-controller-using-windows-powershell)

### Install an additional (replica) domain controller using Windows PowerShell {#install-an-additional-replica-domain-controller-using-windows-powershell .heading-anchor}

Use [Install-ADDSDomainController](/en-us/powershell/module/addsdeployment/install-addsdomaincontroller) to install an additional domain controller.

To install a domain controller and DNS server in the corp.contoso.com domain and be prompted to supply the domain Administrator credentials and the DSRM password, type:

PowerShell

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
Install-ADDSDomainController -Credential (Get-Credential CORP\Administrator) -DomainName "corp.contoso.com"
```

If the computer is already domain joined and you\'re a member of the Domain Admins group, you can use:

PowerShell

``` {.inner-focus data-language="powershell"}
Install-ADDSDomainController -DomainName "corp.contoso.com"
```

To be prompted for the domain name, type:

PowerShell

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
Install-ADDSDomainController -Credential (Get-Credential) -DomainName (Read-Host "Domain to promote into")
```

The following command will use credentials of Contoso\\EnterpriseAdmin1 to install a writable domain controller and a global catalog server in a site named Boston, install DNS server, create a DNS delegation in the contoso.com domain, install from media that is stored in the c:\\ADDS IFM folder, install the Active Directory database and SYSVOL on the D:\\ drive, install the log files on the E:\\ drive, have the server automatically restart after AD DS installation is complete, and be prompted to provide the Directory Services Restore Mode password:

PowerShell

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
Install-ADDSDomainController -Credential (Get-Credential CONTOSO\EnterpriseAdmin1) -CreateDNSDelegation -DomainName corp.contoso.com -SiteName Boston -InstallationMediaPath "c:\ADDS IFM" -DatabasePath "d:\NTDS" -SYSVOLPath "d:\SYSVOL" -LogPath "e:\Logs"
```

[](#perform-a-staged-rodc-installation-using-windows-powershell)

### Perform a staged RODC installation using Windows PowerShell {#perform-a-staged-rodc-installation-using-windows-powershell .heading-anchor}

Use the cmdlet [Add-ADDSReadOnlyDomainControllerAccount](/en-us/powershell/module/addsdeployment/add-addsreadonlydomaincontrolleraccount) to create an RODC account.

For example, to create an RODC account named RODC1:

PowerShell

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
Add-ADDSReadOnlyDomainControllerAccount -DomainControllerAccountName RODC1 -DomainName corp.contoso.com -SiteName Boston -DelegatedAdministratorAccountName AdminUser
```

Then run the following commands on the server that you want to attach to the RODC1 account. The server can\'t be joined to the domain. First, install the AD DS server role and management tools:

PowerShell

``` {.inner-focus data-language="powershell"}
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
```

Then run the following command to create the RODC:

PowerShell

``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
Install-ADDSDomainController -DomainName corp.contoso.com -SafeModeAdministratorPassword (Read-Host -Prompt "DSRM Password:" -AsSecureString) -Credential (Get-Credential Corp\AdminUser) -UseExistingAccount
```

Press **Y** to confirm or include the **\"-Confirm:\$false\"** argument to prevent the confirmation prompt.

[](#install-ad-ds-using-server-manager)

## Install AD DS using Server Manager {#install-ad-ds-using-server-manager .heading-anchor}

AD DS can be installed in Windows Server using the Add Roles Wizard in Server Manager, followed by the Active Directory Domain Services Configuration Wizard, which is new beginning in Windows Server 2012. The Active Directory Domain Services Installation Wizard (dcpromo.exe) is deprecated beginning in Windows Server 2012.

The following sections explain how to create server pools in order to install and manage AD DS on multiple servers, and how to use the wizards to install AD DS.

[](#create-server-pools)

### Create server pools {#create-server-pools .heading-anchor}

Server Manager can pool other servers on the network as long as they\'re accessible from the computer running Server Manager. Once pooled, you choose those servers for remote installation of AD DS or any other configuration options possible within Server Manager. The computer running Server Manager automatically pools itself. For more information about server pools, see [Add Servers to Server Manager](/en-us/windows-server/administration/server-manager/add-servers-to-server-manager).

Note

In order to manage a domain-joined computer using Server Manager on a workgroup server, or vice-versa, additional configuration steps are needed. For more information, see \"Add and manage servers in workgroups\" in [Add Servers to Server Manager](/en-us/windows-server/administration/server-manager/add-servers-to-server-manager).

[](#install-ad-ds)

### Install AD DS {#install-ad-ds .heading-anchor}

Use the following procedures to install AD DS using the GUI method. The steps can be performed locally or remotely.

[](#install-ad-ds-by-using-server-manager)

#### Install AD DS by using Server Manager {#install-ad-ds-by-using-server-manager .heading-anchor}

1.  In Server Manager, select **Manage** and select **Add Roles and Features** to start the Add Roles Wizard.

2.  On the **Before you begin** page, select **Next**.

3.  On the **Select installation type** page, select **Role-based or feature-based installation** and then select **Next**.

4.  On the **Select destination server** page, select **Select a server from the server pool**, select the name of the server where you want to install AD DS and then select **Next**.

    To select remote servers, first create a server pool and add the remote servers to it. For more information about creating server pools, see [Add Servers to Server Manager](/en-us/windows-server/administration/server-manager/add-servers-to-server-manager).

5.  On the **Select server roles** page, select **Active Directory Domain Services**, then on the **Add Roles and Features Wizard** dialog box, select **Add Features**, and then select **Next**.

6.  On the **Select features** page, select any additional features you want to install and select **Next**.

7.  On the **Active Directory Domain Services** page, review the information and then select **Next**.

8.  On the **Confirm installation selections** page, select **Install**.

9.  On the **Results** page, verify that the installation succeeded, and select **Promote this server to a domain controller** to start the Active Directory Domain Services Configuration Wizard.

    Important

    If you close Add Roles Wizard at this point without starting the Active Directory Domain Services Configuration Wizard, you can restart it by selecting Tasks in Server Manager.

10. On the **Deployment Configuration** page, choose one of the following options:

    -   If you\'re installing an additional domain controller in an existing domain, select **Add a domain controller to an existing domain**, and type the name of the domain (for example, emea.corp.contoso.com) or select **Select\...** to choose a domain, and credentials (for example, specify an account that is a member of the Domain Admins group) and then select **Next**.

        Note

        The name of the domain and current user credentials are supplied by default only if the machine is domain-joined and you\'re performing a local installation. If you\'re installing AD DS on a remote server, you need to specify the credentials, by design. If current user credentials aren\'t sufficient to perform the installation, select **Change\...** in order to specify different credentials.

    -   If you\'re installing a new child domain, select **Add a new domain to an existing forest**, for **Select domain type**, select **Child Domain**, type or browse to the name of the parent domain DNS name (for example, corp.contoso.com), type the relative name of the new child domain (for example emea), type credentials to use to create the new domain, and then select **Next**.

    -   If you\'re installing a new domain tree, select **Add new domain to an existing forest**, for **Select domain type**, choose **Tree Domain**, type the name of the root domain (for example, corp.contoso.com), type the DNS name of the new domain (for example, fabrikam.com), type credentials to use to create the new domain, and then select **Next**.

    -   If you\'re installing a new forest, select **Add a new forest** and then type the name of the root domain (for example, corp.contoso.com).

11. On the **Domain Controller Options** page, choose one of the following options:

    -   If you\'re creating a new forest or domain, select the domain and forest functional levels, select **Domain Name System (DNS) server**, specify the DSRM password, and then select **Next**.

    -   If you\'re adding a domain controller to an existing domain, select **Domain Name System (DNS) server**, **Global Catalog (GC)**, or **Read Only Domain Controller (RODC)** as needed, choose the site name, and type the DSRM password and then select **Next**.

    For more information about which options on this page are available or not available under different conditions, see [Domain Controller Options](ad-ds-installation-and-removal-wizard-page-descriptions#domain-controller-options).

12. On the **DNS Options** page (which appears only if you install a DNS server), select **Update DNS delegation** as needed. If you do, provide credentials that have permission to create DNS delegation records in the parent DNS zone.

    If a DNS server that hosts the parent zone can\'t be contacted, the **Update DNS Delegation** option isn\'t available.

    For more information about whether you need to update the DNS delegation, see [Understanding Zone Delegation](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc771640(v=ws.11)). If you attempt to update the DNS delegation and encounter an error, see [DNS Options](ad-ds-installation-and-removal-wizard-page-descriptions#dns-options).

13. On the **RODC Options** page (which appears only if you install an RODC), specify the name of a group or user who will manage the RODC, add accounts to or remove accounts from the Allowed or Denied password replication groups, and then select **Next**.

    For more information, see [Password Replication Policy](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc730883(v=ws.10)).

14. On the **Additional Options** page, choose one of the following options:

    -   If you\'re creating a new domain, type a new NetBIOS name or verify the default NetBIOS name of the domain, and then select **Next**.

    -   If you\'re adding a domain controller to an existing domain, select the domain controller that you want to replicate the AD DS installation data from (or allow the wizard to select any domain controller). If you\'re installing from media, select **Install from media path** type and verify the path to the installation source files, and then select **Next**.

        You can\'t use install from media (IFM) to install the first domain controller in a domain. IFM doesn\'t work across different operating system versions. In other words, in order to install an additional domain controller that runs Windows Server by using IFM, you must create the backup media on a Windows Server domain controller. For more information about IFM, see [Installing an Additional Domain Controller by Using IFM](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc816722(v=ws.10)).

15. On the **Paths** page, type the locations for the Active Directory database, log files, and SYSVOL folder (or accept default locations), and select **Next**.

    Important

    Don\'t store the Active Directory database, log files, or SYSVOL folder on a data volume formatted with Resilient File System (ReFS).

16. On the **Preparation Options** page, enter credentials that are sufficient to run adprep.

17. On the **Review Options** page, confirm your selections, select **View script** if you want to export the settings to a Windows PowerShell script, and then select **Next**.

18. On the **Prerequisites Check** page, confirm that prerequisite validation completed and then select **Install**.

19. On the **Results** page, verify that the server was successfully configured as a domain controller. The server will be restarted automatically to complete the AD DS installation.

[](#perform-a-staged-rodc-installation-using-the-graphical-user-interface)

## Perform a Staged RODC Installation using the Graphical User Interface {#perform-a-staged-rodc-installation-using-the-graphical-user-interface .heading-anchor}

A staged RODC installation allows you to create an RODC in two stages. In the first stage, a member of the Domain Admins group creates an RODC account. In the second stage, a server is attached to the RODC account. The second stage can be completed by a member of the Domain Admins group or a delegated domain user or group.

[](#create-an-rodc-account-by-using-the-active-directory-management-tools)

### Create an RODC account by using the Active Directory management tools {#create-an-rodc-account-by-using-the-active-directory-management-tools .heading-anchor}

1.  You can create the RODC account using Active Directory Administrative Center or Active Directory Users and Computers.

    1.  select **Start**, select **Administrative Tools**, and then select **Active Directory Administrative Center**.

    2.  In the navigation pane (left pane), select the name of the domain.

    3.  In the Management list (center pane), select the **Domain Controllers** OU.

    4.  In the Tasks Pane (right pane), select **Pre-create a read-only domain controller account**.

    -Or-

    1.  select **Start**, select **Administrative Tools**, and then select **Active Directory Users and Computers**.

    2.  Either right-select the **Domain Controllers** organizational unit (OU) or select the **Domain Controllers** OU, and then select **Action**.

    3.  select **Pre-create Read-only Domain Controller account**.

2.  On the **Welcome to the Active Directory Domain Services Installation Wizard** page, if you want to modify the default the Password Replication Policy (PRP), select **Use advanced mode installation**, and then select **Next**.

3.  On the **Network Credentials** page, under **Specify the account credentials to use to perform the installation**, select **My current logged on credentials** or select **Alternate credentials**, and then select **Set**. In the **Windows Security** dialog box, provide the user name and password for an account that can install the additional domain controller. To install an additional domain controller, you must be a member of the Enterprise Admins group or the Domain Admins group. When you\'re finished providing credentials, select **Next**.

4.  On the **Specify the Computer Name** page, type the computer name of the server that will be the RODC.

5.  On the **Select a Site** page, select a site from the list or select the option to install the domain controller in the site that corresponds to the IP address of the computer on which you\'re running the wizard, and then select **Next**.

6.  On the **Additional Domain Controller Options** page, make the following selections, and then select **Next**:

    -   **DNS server**: This option is selected by default so that your domain controller can function as a Domain Name System (DNS) server. If you don\'t want the domain controller to be a DNS server, clear this option. However, if you don\'t install the DNS server role on the RODC and the RODC is the only domain controller in the branch office, users in the branch office won\'t be able to perform name resolution when the wide area network (WAN) to the hub site is offline.

    -   **Global catalog**: This option is selected by default. It adds the global catalog, read-only directory partitions to the domain controller, and it enables global catalog search functionality. If you don\'t want the domain controller to be a global catalog server, clear this option. However, if you don\'t install a global catalog server in the branch office or enable universal group membership caching for the site that includes the RODC, users in the branch office won\'t be able to log on to the domain when the WAN to the hub site is offline.

    -   **Read-only domain controller**. When you create an RODC account, this option is selected by default and you can\'t clear it.

7.  If you selected the **Use advanced mode installation** check box on the **Welcome** page, the **Specify the Password Replication Policy** page appears. By default, no account passwords are replicated to the RODC, and security-sensitive accounts (such as members of the Domain Admins group) are explicitly denied from ever having their passwords replicated to the RODC.

    To add other accounts to policy, select **Add**, then select **Allow passwords for the account to replicate to this RODC** or select **Deny passwords for the account from replicating to this RODC** and then select the accounts.

    When complete (or to accept the default setting), select **Next**.

8.  On the **Delegation of RODC Installation and Administration** page, type the name of the user or the group who will attach the server to the RODC account that you\'re creating. You can type the name of only one security principal.

    To search the directory for a specific user or group, select **Set**. In **Select User or Group**, type the name of the user or group. We recommend that you delegate RODC installation and administration to a group.

    This user or group will also have local administrative rights on the RODC after the installation. If you don\'t specify a user or group, only members of the Domain Admins group or the Enterprise Admins group will be able to attach the server to the account.

    When you\'re finished, select **Next**.

9.  On the **Summary** page, review your selections. select **Back** to change any selections, if necessary.

    To save the settings that you selected to an answer file that you can use to automate subsequent AD DS operations, select **Export settings**. Type a name for your answer file, and then select **Save**.

    When you\'re sure that your selections are accurate, select **Next** to create the RODC account.

10. On the **Completing the Active Directory Domain Services Installation Wizard** page, select **Finish**.

After an RODC account is created, you can attach a server to account to complete the RODC installation. This second stage can be completed in the branch office where the RODC will be located. The server where you perform this procedure must not be joined to the domain. You use the Add Roles Wizard in Server Manager to attach a server to an RODC account.

[](#attach-a-server-to-an-rodc-account-using-server-manager)

#### Attach a server to an RODC account using Server Manager {#attach-a-server-to-an-rodc-account-using-server-manager .heading-anchor}

1.  Log on as local Administrator.

2.  In Server Manager, select **Add roles and features**.

3.  On the **Before you begin** page, select **Next**.

4.  On the **Select installation type** page, select **Role-based or feature-based installation** and then select **Next**.

5.  On the **Select destination server** page, select **Select a server from the server pool**, select the name of the server where you want to install AD DS and then select **Next**.

6.  On the **Select server roles** page, select **Active Directory Domain Services**, select **Add Features** and then select **Next**.

7.  On the **Select features** page, select any additional features that you want to install and select **Next**.

8.  On the **Active Directory Domain Services** page, review the information and then select **Next**.

9.  On the **Confirm installation selections** page, select **Install**.

10. On the **Results** page, verify **Installation succeeded**, and select **Promote this server to a domain controller** to start the Active Directory Domain Services Configuration Wizard.

    Important

    If you close Add Roles Wizard at this point without starting the Active Directory Domain Services Configuration Wizard, you can restart it by selecting Tasks in Server Manager.

11. On the **Deployment Configuration** page, select **Add a domain controller to an existing domain**, type the name of the domain (for example, emea.contoso.com) and credentials (for example, specify an account that is delegated to manage and install the RODC), and then select **Next**.

12. On the **Domain Controller Options** page, select **Use existing RODC account**, type and confirm the Directory Services Restore Mode password, and then select **Next**.

13. On the **Additional Options** page, if you\'re installing from media, select **Install from media path** type and verify the path to the installation source files, select the domain controller that you want to replicate the AD DS installation data from (or allow the wizard to select any domain controller) and then select **Next**.

14. On the **Paths** page, type the locations for the Active Directory database, log files, and SYSVOL folder, or accept default locations, and then select **Next**.

15. On the **Review Options** page, confirm your selections, select **View Script** to export the settings to a Windows PowerShell script, and then select **Next**.

16. On the **Prerequisites Check** page, confirm that prerequisite validation completed and then select **Install**.

    To complete the AD DS installation, the server will restart automatically.

[](#related-content)

## Related content {#related-content .heading-anchor}

-   [Deploy a Forest with Server Manager](/en-us/windows-server/identity/ad-ds/deploy/install-a-new-windows-server-2012-active-directory-forest--level-200-)

-   [Install a Replica Windows Server Domain Controller in an Existing Domain](/en-us/windows-server/identity/ad-ds/deploy/install-a-replica-windows-server-2012-domain-controller-in-an-existing-domain--level-200-)

-   [Install an Active Directory Child or Tree Domain](/en-us/windows-server/identity/ad-ds/deploy/install-a-new-windows-server-2012-active-directory-child-or-tree-domain--level-200-)

-   [Install a Windows Server Active Directory Read-Only Domain Controller](/en-us/windows-server/identity/ad-ds/deploy/rodc/install-a-windows-server-2012-active-directory-read-only-domain-controller--rodc---level-200-)

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Install a New Windows Server 2012 Active Directory Forest (Level 200)](/en-us/windows-server/identity/ad-ds/deploy/install-a-new-windows-server-2012-active-directory-forest--level-200-?source=recommendations)

    Learn more about: Install a New Windows Server 2012 Active Directory Forest (Level 200)

-   [Install a New Windows Server 2012 Active Directory Child or Tree Domain (Level 200)](/en-us/windows-server/identity/ad-ds/deploy/install-a-new-windows-server-2012-active-directory-child-or-tree-domain--level-200-?source=recommendations)

    Learn more about: Install a New Windows Server 2012 Active Directory Child or Tree Domain (Level 200)

-   [AD DS Simplified Administration](/en-us/windows-server/identity/ad-ds/manage/ad-ds-simplified-administration?source=recommendations)

    Learn more about: AD DS Simplified Administration

-   [Install a Replica Windows Server 2012 Domain Controller in an Existing Domain (Level 200)](/en-us/windows-server/identity/ad-ds/deploy/install-a-replica-windows-server-2012-domain-controller-in-an-existing-domain--level-200-?source=recommendations)

    Learn more about: Install a Replica Windows Server 2012 Domain Controller in an Existing Domain (Level 200)

-   [Manage User Accounts with Active Directory Users and Computers in Windows Server](/en-us/windows-server/identity/ad-ds/manage-user-accounts-in-windows-server?source=recommendations)

    Create, delete, and manage user accounts in Active Directory Users and Computers. Learn how to manage user account properties, group memberships, and passwords.

-   [AD DS Deployment](/en-us/windows-server/identity/ad-ds/deploy/ad-ds-deployment?source=recommendations)

    Learn more about: AD DS Deployment

-   [What\'s New in Active Directory Domain Services Installation and Removal](/en-us/windows-server/identity/ad-ds/deploy/what-s-new-in-active-directory-domain-services-installation-and-removal?source=recommendations)

    Learn more about: What\'s New in Active Directory Domain Services Installation and Removal

-   [Advanced AD DS Management Using Active Directory Administrative Center (Level 200)](/en-us/windows-server/identity/ad-ds/get-started/adac/advanced-ad-ds-management-using-active-directory-administrative-center--level-200-?source=recommendations)

    Learn more about Advanced AD DS Management using Active Directory Administrative Center (Level 200).

Training

Module

[Manage AD DS domain controllers and FSMO roles - Training](/en-us/training/modules/manage-active-directory-domain-services-flexible-single-master-operation-roles/?source=recommendations)

Learn how to deploy and manage AD DS domain controllers, maintain availability with backup and recovery, manage the global catalog role, and transfer or seize FSMO roles including schema master, domain-naming master, RID master, infrastructure master, and PDC emulator.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 04/21/2025
