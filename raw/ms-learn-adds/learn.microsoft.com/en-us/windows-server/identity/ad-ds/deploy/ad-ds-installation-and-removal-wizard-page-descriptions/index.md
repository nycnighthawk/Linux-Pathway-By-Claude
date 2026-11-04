---
{"title": "Active Directory Domain Services (AD DS) configuration wizard page descriptions", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-installation-and-removal-wizard-page-descriptions", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Active Directory Domain Services (AD DS) configuration wizard page descriptions

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

The Active Directory Domain Services (AD DS) Configuration Wizard is a tool in Server Manager that enables administrators to promote servers to domain controllers or demote them as needed. This article provides a detailed overview of the wizard\'s pages, including their controls and options, to help you navigate the installation and removal processes effectively. Whether you\'re creating a new forest, adding a domain controller to an existing domain, or demoting a domain controller, this guide outlines the steps and considerations for each operation.

Watch the following video to get an overview of promoting and demoting domain controllers using the AD DS Configuration Wizard:\
\

[](#summary-of-each-page)

## Summary of each page {#summary-of-each-page .heading-anchor}

The tables in this section summarize the pages that you see when you use the Active Directory Domain Services Configuration Wizard to promote a server to a domain controller or to demote a domain controller. Select the link for each page to learn more about the options and controls that you see on that page.

When you promote a server to a domain controller, you navigate through the following pages:

  Active Directory configuration page                       Description
  --------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Deployment Configuration](#deployment-configuration)     Select the type of deployment operation you want to perform: create a new forest (first domain controller), create a new domain within an existing forest, or add an additional domain controller to an existing domain. This page also validates basic requirements and prompts for domain names.
  [Domain Controller Options](#domain-controller-options)   Configure forest and domain functional levels, select domain controller roles including DNS server, Global Catalog, and Read-Only Domain Controller options. Set the Directory Services Restore Mode (DSRM) password required for offline AD DS operations and maintenance.
  [DNS Options](#dns-options)                               Configure DNS delegation settings when installing the DNS server role. Create delegation records in the parent DNS zone to ensure proper name resolution and authority transfer for the new domain controller\'s DNS zone.
  [RODC Options](#rodc-options)                             Set up delegated administrator accounts that can manage the read-only domain controller locally, and configure the Password Replication Policy (PRP) to control which user and computer account passwords can be cached on the RODC for authentication.
  [Additional Options](#additional-options)                 Specify the NetBIOS domain name for new domains, select a specific domain controller as the replication source, and configure install from media options using backup media created with Windows Server Backup or ntdsutil.exe to reduce installation time.
  [Paths](#paths)                                           Set custom file system locations for the Active Directory database (`ntds.dit`), database transaction logs, and `SYSVOL` shared folder instead of using the default system drive locations for better performance or storage management.
  [Preparation Options](#preparation-options)               Provide Enterprise Admins, Schema Admins, or Domain Admins credentials to run required `adprep.exe` commands (`forestprep`, `domainprep`, or `rodcprep`) when the current user account lacks sufficient permissions for schema or domain preparation.
  [Review Options](#review-options)                         Review and validate all selected configuration settings before starting the installation process. Export the configuration as a Windows PowerShell script for automation or documentation purposes, and make final adjustments if needed.
  [Prerequisites Check](#prerequisites-check)               Display comprehensive results of prerequisite validation checks including network connectivity, DNS resolution, permissions verification, and system requirements. Shows any warnings or errors that must be addressed before proceeding.
  [Results](#results)                                       Show the final results and status of the domain controller installation or promotion process, including success confirmation, any post-installation warnings, and options to restart the server to complete the configuration.

When you demote a domain controller, you navigate through the following pages:

  Active Directory configuration page                         Description
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Credentials](#credentials)                                 Provide the required credentials for demotion operation, including Domain Admin credentials for additional domain controllers or Enterprise Admins credentials for the last domain controller in a domain. Configure forced removal options if the domain controller cannot contact other domain controllers.
  [Warnings](#warnings)                                       Review warnings about removing critical roles and services hosted by the domain controller, such as DNS server, global catalog, or operations master roles. Acknowledge the impact of removing these roles before proceeding with demotion.
  [Removal Options](#removal-options)                         Configure DNS zone delegation removal options when the domain controller being demoted hosts DNS zones. Remove the DNS server from zone delegations to prevent DNS resolution issues after demotion.
  [New Administrator Password](#new-administrator-password)   Set a new password for the built-in local Administrator account that will be used after demotion when the computer becomes a member server or workgroup computer instead of a domain controller.
  [Review Options](#review-options-1)                         Review and validate all demotion settings before starting the process. Export the configuration as a Windows PowerShell script for automation purposes and confirm final settings before beginning the domain controller demotion.

[](#pages-when-promoting-a-server-to-a-domain-controller)

## Pages when promoting a server to a domain controller {#pages-when-promoting-a-server-to-a-domain-controller .heading-anchor}

The following sections describe the pages that you see when you use the Active Directory Domain Services Configuration Wizard to promote a server to a domain controller.

[](#deployment-configuration)

### Deployment Configuration {#deployment-configuration .heading-anchor}

Server Manager begins every domain controller installation with the **Deployment Configuration** page. The options and required fields that you see on this page and subsequent pages depend on which deployment operation you select.

The wizard runs some validations and tests on the **Deployment Configuration** page and again later as part of prerequisite checks. For example, a check is performed when you try to install the first Windows Server domain controller in a forest. If the functional level of the forest doesn\'t support the Windows Server version of the domain controller, an error appears on this page.

The following sections describe the deployment operations that you can select on this page.

[](#create-a-forest)

#### Create a forest {#create-a-forest .heading-anchor}

The following screenshot shows the options that appear when you create a forest:

-   When you create a forest, you must specify a name for the forest root domain.

    -   The forest root domain name can\'t be single-labeled. For example, it must be `example-domain.com` instead of `example-domain`.
    -   It must use allowed Domain Name System (DNS) domain naming conventions. For more information about DNS domain naming conventions, see [Naming conventions in Active Directory for computers, domains, sites, and OUs](/en-us/troubleshoot/windows-server/active-directory/naming-conventions-for-computer-domain-site-ou).
    -   You can specify an internationalized domain name (IDN).

-   The name of any Active Directory forest that you create must be different from your external DNS name. For example, if your internet DNS URL is `https://example-domain.com`, you must choose a different name for your internal forest to avoid future compatibility issues. That name should be unique and unlikely for web traffic, for example, `corp.example-domain.com`.

-   You must be a member of Administrators group on the server that you want to create a forest on.

For more information about how to create a forest, see [Install a New Windows Server 2012 Active Directory Forest (Level 200)](install-a-new-windows-server-2012-active-directory-forest--level-200-).

[](#create-a-domain)

#### Create a domain {#create-a-domain .heading-anchor}

The following screenshot shows the options that appear when you create a domain:

Note

If you create a tree domain, you need to specify the name of the forest root domain instead of the parent domain. But the remaining wizard pages and options are the same whether you create a child domain or a tree domain.

-   For **Parent domain name**, select **Select** to go to the parent domain or Active Directory tree, or enter a valid parent domain or tree name.

-   For **New domain name**, enter the name of the new domain.

    -   For a tree domain, provide a valid, fully qualified root domain name. The name can\'t be single-labeled, and it must meet DNS domain name requirements.
    -   For a child domain, provide a valid, single-label child domain name. The name must meet DNS domain name requirements.

-   If your current credentials aren\'t from the domain, the Active Directory Domain Services Configuration Wizard prompts you for domain credentials. Select **Change** to provide domain credentials.

For more information about how to create a domain, see [Install a New Windows Server 2012 Active Directory Child or Tree Domain (Level 200)](install-a-new-windows-server-2012-active-directory-child-or-tree-domain--level-200-).

[](#add-a-domain-controller-to-an-existing-domain)

#### Add a domain controller to an existing domain {#add-a-domain-controller-to-an-existing-domain .heading-anchor}

The following screenshot shows you the options that appear when you add a new domain controller to an existing domain:

-   For **Domain**, select **Select** to go to the domain, or enter a valid domain name.

-   As needed, Server Manager prompts you for valid credentials. Installing an additional domain controller requires membership in the Domain Admins group.

    Also, installing the first domain controller that runs Windows Server in a forest requires credentials that include group memberships in both the Enterprise Admins and Schema Admins groups. The Active Directory Domain Services Configuration Wizard prompts you later if your current credentials don\'t have adequate permissions or group memberships.

For more information about how to add a domain controller to an existing domain, see [Install a Replica Windows Server 2012 Domain Controller in an Existing Domain (Level 200)](install-a-replica-windows-server-2012-domain-controller-in-an-existing-domain--level-200-).

[](#domain-controller-options)

### Domain Controller Options {#domain-controller-options .heading-anchor}

The options that you see on the **Domain Controller Options** page depend on your deployment operation. The following sections describe the options that you configure for each operation.

[](#new-forest-options)

#### New forest options {#new-forest-options .heading-anchor}

When you create a forest, the **Domain Controller Options** page displays the options shown in the following screenshot:

-   The default values of the forest and domain functional levels depend on your Windows Server version.

    Starting with Windows Server 2012, the domain functional level offers the following settings in the key distribution center (KDC) administrative template policy **KDC support for claims, compound authentication, and Kerberos armoring**:

    -   Always provide claims
    -   Fail unarmored authentication requests

    For more information, see [Support for claims, compound authentication, and Kerberos armoring](/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831747(v=ws.11)#support-for-claims-compound-authentication-and-kerberos-armoring).

    Any domains that you create in a forest automatically operate at the domain functional level that\'s equal to the selected forest functional level. Also, any domain controllers in the domain run the Windows Server version of the selected domain functional level.

    For more information about features that are available at various functional levels, see [Active Directory Domain Services functional levels](../active-directory-functional-levels).

    The features that are available on a domain controller depend on the version of Windows Server that the domain controller runs.

-   When you create a forest, the **Domain Name System (DNS) server** option is selected by default. The first domain controller in the forest must be a global catalog server, and it can\'t be a read-only domain controller (RODC).

-   To sign in to a domain controller that\'s not running AD DS, you need the Directory Services Restore Mode (DSRM) password. The password you specify must adhere to the password policy applied to the server. By default, that policy doesn\'t require a strong password. It only requires a nonblank password. Always choose a strong, complex password or, preferably, a passphrase. For information about how to synchronize the DSRM password with the password of a domain user account, see the [support article about synchronizing passwords](https://support.microsoft.com/topic/a-feature-is-available-for-windows-server-2008-that-lets-you-synchronize-the-dsrm-administrator-password-with-a-domain-user-account-a9a2ef06-2771-b0d4-6cd3-e1fe836f69e1).

For more information about how to create a forest, see [Install a New Windows Server 2012 Active Directory Forest (Level 200)](install-a-new-windows-server-2012-active-directory-forest--level-200-).

[](#new-child-domain-options)

#### New child domain options {#new-child-domain-options .heading-anchor}

When you create a child domain, the **Domain Controller Options** page displays the options shown in the following screenshot:

-   The default value of the domain functional level depends on your Windows Server version. You can specify any value that\'s greater than or equal to the forest functional level.

-   You can configure the following domain controller options:

    -   **Domain Name System (DNS) server**
    -   **Global Catalog (GC)**

    You can\'t configure the first domain controller in a new domain to be an RODC.

    We recommend that all domain controllers provide DNS and global catalog services for high availability in distributed environments. For this reason, the wizard enables these options by default when you create a domain.

-   You can also use this page to select an appropriate Active Directory logical site name from the forest configuration. By default, the site with the most correct subnet is selected. If there\'s only one site, that site is automatically selected.

    Important

    If the server doesn\'t belong to an Active Directory subnet and there\'s more than one site, nothing is selected. The **Next** button isn\'t available until you select a site from the list.

For more information about how to create a domain, see [Install a New Windows Server 2012 Active Directory Child or Tree Domain (Level 200)](install-a-new-windows-server-2012-active-directory-child-or-tree-domain--level-200-).

[](#options-for-adding-a-domain-controller-to-a-domain)

#### Options for adding a domain controller to a domain {#options-for-adding-a-domain-controller-to-a-domain .heading-anchor}

When you add a domain controller to a domain, the **Domain Controller Options** page displays the options shown in the following screenshot:

You can configure the following domain controller options:

-   **Domain Name System (DNS) server**
-   **Global Catalog (GC)**
-   **Read only domain controller (RODC)**

We recommend that all domain controllers provide DNS and global catalog services for high availability in distributed environments. For this reason, these options are enabled by default. For more information about deploying RODCs, see [Read-Only Domain Controller Planning and Deployment Guide](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc771744(v=ws.10)).

For more information about how to add a domain controller to an existing domain, see [Install a Replica Windows Server 2012 Domain Controller in an Existing Domain (Level 200)](install-a-replica-windows-server-2012-domain-controller-in-an-existing-domain--level-200-).

[](#dns-options)

### DNS Options {#dns-options .heading-anchor}

If you install the DNS server role, the following **DNS Options** page appears:

When you install the DNS server role, delegation records that point to the DNS server as authoritative for the zone should be created in the parent DNS zone. Delegation records transfer name resolution authority. They also provide correct referral to other DNS servers and clients of new servers that are authoritative for the new zone. These resource records include the following records:

-   A name server (NS) resource record to effect the delegation. This resource record advertises that the server named `ns1.na.example.microsoft.com` is an authoritative server for the delegated subdomain.
-   A host (A or AAAA) resource record, which is also known as a glue record. This record must be present to resolve the name of the server that\'s specified in the NS resource record to its IP address. The process of resolving the host name in this resource record to the delegated DNS server in the NS resource record is sometimes referred to as *glue chasing*.

You can have the Active Directory Domain Services Configuration Wizard create these records automatically. On the **Domain Controller Options** page, if you select **Next**, the wizard verifies that the appropriate records exist in the parent DNS zone. If the wizard can\'t verify that the records exist in the parent domain, the wizard provides you with the option to create a DNS delegation for a new domain (or update the existing delegation) automatically and continue with the new domain controller installation.

Alternatively, you can create these DNS delegation records before you install the DNS server role. To create a zone delegation, open **DNS Manager**, right-click the parent domain, and then select **New Delegation**. Follow the steps in the New Delegation Wizard to create the delegation.

The installation process tries to create the delegation to ensure that computers in other domains can resolve DNS queries for hosts, including domain controllers and member computers, in the DNS subdomain. The delegation records can be automatically created only on Microsoft DNS servers. If the parent DNS domain zone resides on non-Microsoft DNS servers such as Berkeley Internet Name Domain (BIND) servers, a warning about the failure to create DNS delegation records appears on the **Prerequisites Check** page. For more information about the warning, see [Known Issues for installing and removing AD DS](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754463(v=ws.10)).

Delegations between the parent domain and the subdomain being promoted can be created and validated before or after the installation. There\'s no reason to delay the installation of a new domain controller because you can\'t create or update the DNS delegation.

For more information about delegation, see [Understanding zone delegation](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc771640(v=ws.11)). If zone delegation isn\'t possible in your situation, you can consider other methods for providing name resolution from other domains to the hosts in your domain. For example, the DNS administrator of another domain can configure conditional forwarding, stub zones, or secondary zones in order to resolve names in your domain. For more information, see the following resources:

-   [Understanding zone types](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc771898(v=ws.11))
-   [Understanding stub zones](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc779197(v=ws.10))
-   [Understanding forwarders](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc782142(v=ws.10))

[](#rodc-options)

### RODC Options {#rodc-options .heading-anchor}

The following screenshot shows the options that appear when you install an RODC.

-   You can use the **Delegated administrator account** option to specify the accounts that are assigned local administrative permissions to the RODC. These users can operate with privileges equivalent to the local computer\'s Administrators group. They aren\'t members of the Domain Admins or the domain built-in Administrators groups. This option is useful for delegating branch office administration without granting domain administrative permissions. Configuring delegation of administration isn\'t required. For more information, see [Administrator role separation](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753170(v=ws.10)).

-   You can use the remaining options on the page to configure the password replication policy (PRP), which acts as an access control list (ACL). This policy determines whether an RODC can cache a password. After the RODC receives an authenticated user or computer sign-in request, it refers to the PRP to determine whether the password for the account should be cached. The same account can then perform subsequent sign-ins more efficiently. When an account is cached, the RODC can authenticate it even if the WAN link to the hub site is offline.

    The PRP lists two types of accounts:

    -   Accounts that have passwords that can be cached
    -   Accounts that have passwords that are explicitly denied from being cached

    If a user or computer account is on the list of accounts that can be cached, the RODC hasn\'t necessarily cached the password for that account. For example, an administrator can specify in advance the accounts that an RODC should cache.

    The passwords aren\'t cached for any user or computer accounts that aren\'t denied or allowed, explicitly or implicitly. If those users or computers don\'t have access to a writable domain controller, they can\'t access AD DS-provided resources or functionality. For more information about the PRP, see [Password replication policy](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc730883(v=ws.10)). For more information about managing the PRP, see [Administering the password replication policy](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754646(v=ws.10)).

For more information about installing RODCs, see [Install a Windows Server 2012 Active Directory Read-Only Domain Controller (RODC) (Level 200)](rodc/install-a-windows-server-2012-active-directory-read-only-domain-controller--rodc---level-200-).

[](#additional-options)

### Additional Options {#additional-options .heading-anchor}

The following screenshot shows the option that appears on the **Additional Options** page when you create a domain:

The following screenshot shows the options that appear on the **Additional Options** page when you add a domain controller to an existing domain:

-   You can use the **Replicate from** option to specify a domain controller as the replication source, or to allow the wizard to choose any domain controller as the replication source.

-   You can use the **Install from media** option to specify a backed-up media source to use to install the domain controller. If the installation media is stored locally, you can use the **Path** option to select the file location. This option isn\'t available for a remote installation. You can select **Verify** to ensure the provided path is valid media. You must create the media that you use for this option by using Windows Server Backup or `ntdsutil.exe` from another existing Windows Server computer. You can\'t use an operating system earlier than Windows Server 2012 to create media for the domain controller. If the media is protected with a SysKey password, Server Manager prompts for the image\'s password during verification.

For more information about how to create a domain, see [Install a New Windows Server 2012 Active Directory Child or Tree Domain (Level 200)](install-a-new-windows-server-2012-active-directory-child-or-tree-domain--level-200-). For more information about how to add a domain controller to an existing domain, see [Install a Replica Windows Server 2012 Domain Controller in an Existing Domain (Level 200)](install-a-replica-windows-server-2012-domain-controller-in-an-existing-domain--level-200-).

[](#paths)

### Paths {#paths .heading-anchor}

The following screenshot shows the options that appear on the **Paths** page:

You can use the **Paths** page to override the default folder locations of the AD DS database (NTDS.DIT), the database transaction logs, and the SYSVOL share. The default locations are always in the `%systemroot%` folder. For a local installation, you can select a location for storing the files.

[](#preparation-options)

### Preparation Options {#preparation-options .heading-anchor}

The following screenshot shows the **Preparation Options** page:

This page prompts you to supply credentials to run `adprep.exe`. The wizard displays this page when both of the following conditions are met:

-   You\'re not currently signed in with sufficient credentials to run `adprep.exe` commands.
-   In order to complete the AD DS installation, `adprep.exe` is required to run.

The `adprep.exe` tool is required to run in the following situations:

-   The `adprep /forestprep` command must be run to add the first domain controller that runs Windows Server 2012 to an existing forest. To run this command, you must be a member of the Enterprise Admins group, the Schema Admins group, and the Domain Admins group of the domain that hosts the schema master. For this command to run successfully, there must be connectivity between the computer where you run the command and the schema master for the forest.

-   The `adprep /domainprep` command must be run to add the first domain controller that runs Windows Server 2012 to an existing domain. This command must be run by a member of the Domain Admins group of the domain where you install the domain controller that runs Windows Server. For this command to run successfully, there must be connectivity between the computer where you run the command and the infrastructure master for the domain.

-   The `adprep /rodcprep` command must be run to add the first RODC to an existing forest. This command must be run by a member of the Enterprise Admins group. For this command to run successfully, there must be connectivity between the computer where you run the command and the infrastructure master for each application directory partition in the forest.

For more information about `adprep.exe`, see [Adprep.exe integration](what-s-new-in-active-directory-domain-services-installation-and-removal) and [Running Adprep.exe](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd464018(v=ws.10)).

[](#review-options)

### Review Options {#review-options .heading-anchor}

The following screenshot shows the **Review Options** page:

-   You can use the **Review Options** page to validate your settings and ensure that they meet your requirements before you start the installation. This page isn\'t the last opportunity in Server Manager to stop the installation. You can use this page to review and confirm your settings before continuing the configuration.

-   On this page, you also have the option of using the **View script** button to create a Unicode text file that contains the current `ADDSDeployment` module configuration as a single Windows PowerShell script. As a result, you can use the Server Manager graphical interface as a Windows PowerShell deployment studio:

    -   Use the Active Directory Domain Services Configuration Wizard to configure options.
    -   Export the configuration.
    -   Cancel the wizard.

    This process creates a valid and syntactically correct sample for further modification or direct use.

[](#prerequisites-check)

### Prerequisites Check {#prerequisites-check .heading-anchor}

The following screenshot shows the **Prerequisites Check** page:

This page displays potential problems that are detected during the prerequisites check. The results can list warnings, including the following ones:

-   Domain controllers that run Windows Server have a default setting, **Allow cryptography algorithms compatible with Windows NT 4**, that prevents clients that use weaker cryptography algorithms from establishing secure channel sessions. For more information about the potential impact and a workaround, see [Disable the AllowNT4Crypto setting on all affected domain controllers](/en-us/services-hub/unified/health/remediation-steps-ad/disable-the-allownt4crypto-setting-on-all-affected-domain-controllers).

-   A DNS delegation can\'t be created or updated. For more information, see [DNS Options](#dns-options).

-   Windows Management Instrumentation (WMI) calls fail. The prerequisite check requires WMI calls. If a WMI call is blocked by firewall rules, it can fail and return a remote procedure call (RPC) server unavailable error.

For more information about the specific prerequisite checks that are performed for AD DS installation, see [Prerequisite tests](../manage/ad-ds-simplified-administration#BKMK_ADDSInstallPrerequisiteTests).

[](#results)

### Results {#results .heading-anchor}

The following screenshot shows the **Results** page:

On this page, you can review the results of the installation.

You can also restart the target server from this page after the wizard finishes. But if the installation succeeds, the server restarts regardless of whether you select that option.

In some cases, the target server fails to restart. If the wizard finishes on a target server that isn\'t joined to the domain before the installation, the system state of the target server can make the server unreachable on the network. The system state can also prevent you from having permissions to manage the remote server.

If the target server fails to restart in these cases, you must manually restart it. You can\'t use tools like `shutdown.exe` or Windows PowerShell to restart it. You can use Remote Desktop Services to sign in and remotely shut down the target server.

[](#pages-when-demoting-a-domain-controller)

## Pages when demoting a domain controller {#pages-when-demoting-a-domain-controller .heading-anchor}

The following sections describe the pages that you see when you use the Active Directory Domain Services Configuration Wizard to demote a domain controller.

[](#credentials)

### Credentials {#credentials .heading-anchor}

The following screenshot shows the **Credentials** page that appears at the start of the demotion process.

On this page, you configure demotion options. The following credentials are needed to perform the demotion in various situations:

-   Demoting an additional domain controller requires Domain Admin credentials. Selecting **Force removal of the domain controller** demotes the domain controller without removing the domain controller object\'s metadata from Active Directory.

    Important

    Don\'t select the **Force the removal of this domain controller** option unless the domain controller can\'t contact other domain controllers and there\'s *no reasonable way* to resolve that network issue. Forced demotion leaves orphaned metadata in Active Directory on the remaining domain controllers in the forest. Also, all unreplicated changes on that domain controller, such as passwords or new user accounts, are lost forever. Orphaned metadata is the root cause in a significant percentage of Microsoft support cases for AD DS, Microsoft Exchange, SQL Server, and other software. If you forcibly demote a domain controller, you must manually perform metadata cleanup immediately. For instructions, see [Clean up server metadata](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc816907(v=ws.10)).

-   Demoting the last domain controller in a domain requires Enterprise Admins group membership, because this action removes the domain itself. If the domain is the last one in the forest, this action also removes the forest. Server Manager informs you if the current domain controller is the last domain controller in the domain. Select **Last domain controller in the domain** to confirm the domain controller is the last domain controller in the domain.

For more information about removing AD DS, see [Remove Active Directory Domain Services (Level 100)](/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh472163(v=ws.11)) and [Demoting domain controllers and domains](demoting-domain-controllers-and-domains--level-200-).

[](#warnings)

### Warnings {#warnings .heading-anchor}

When you use Server Manager to demote a domain controller, the wizard displays warnings in certain cases. If the domain controller also hosts other roles, such as the DNS server or global catalog server roles, the following **Warnings** page appears:

Before you can select **Next** to continue, you must select **Proceed with removal** to acknowledge that demoting the domain controller makes those roles unavailable.

If you force the removal of a domain controller:

-   Any Active Directory object changes that aren\'t replicated to other domain controllers in the domain are lost.

-   All application directory partitions on the domain controller are removed. If the domain controller holds the last replica of one or more application directory partitions, those partitions no longer exist when the removal operation is complete.

-   Critical operations in the domain and forest can be affected in the following ways if the domain controller hosts certain roles:

      Role                                       Result of removing the domain controller                                                                                                                                                                               Action to take before you continue
      ------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      Global catalog                             Users might have trouble signing in to domains in the forest.                                                                                                                                                          Ensure that enough global catalog servers are in the forest and site to service user sign-ins. If necessary, designate another global catalog server, and update clients and applications with the new information.
      DNS server                                 All the DNS data that\'s stored in Active Directory-integrated zones is lost. After you remove AD DS, the DNS server isn\'t able to perform name resolution for the DNS zones that were Active Directory-integrated.   Update the DNS configuration of all computers that currently refer to the IP address of the DNS server for name resolution. Configure them with the IP address of a new DNS server.
      Infrastructure master                      Clients in the domain might have difficulty locating objects in other domains.                                                                                                                                         Transfer the infrastructure master role to a domain controller that isn\'t a global catalog server.
      Relative ID (RID) master                   You might have problems creating user accounts, computer accounts, and security groups.                                                                                                                                Transfer the RID master role to a domain controller in the same domain as the domain controller that you\'re demoting.
      Primary domain controller (PDC) emulator   Operations that are performed by the PDC emulator, such as Group Policy updates and password resets for non-AD DS accounts, don\'t function properly.                                                                  Transfer the PDC emulator master role to a domain controller that\'s in the same domain as the domain controller that you\'re demoting.
      Schema master                              You can no longer modify the schema for the forest.                                                                                                                                                                    Transfer the schema master role to a domain controller in the root domain in the forest.
      Domain naming master                       You can no longer add domains to or remove domains from the forest.                                                                                                                                                    Transfer the domain naming master role to a domain controller in the root domain in the forest.

Before you remove a domain controller that hosts any operations master roles, try to transfer the role to another domain controller.

If it isn\'t possible to transfer the role, first remove AD DS from the computer. Then seize the role by using `ntdsutil.exe` on the domain controller that you plan to seize the role to. If possible, use a recent replication partner in the same site as the domain controller that you\'re demoting. For more information about transferring and seizing operations master roles, see [Transfer or seize Operation Master roles in Active Directory Domain Services](/en-us/troubleshoot/windows-server/active-directory/transfer-or-seize-operation-master-roles-in-ad-ds).

If the wizard can\'t determine whether the domain controller hosts an operations master role, run the `netdom.exe` command to determine whether the domain controller performs any operations master roles.

After you uninstall AD DS from the last domain controller in the domain, the domain no longer exists.

[](#removal-options)

### Removal Options {#removal-options .heading-anchor}

If the domain controller that you demote is a DNS server that\'s delegated to host the DNS zone, you see the following page. It provides the option to remove the DNS server from the DNS zone delegation.

For more information about removing AD DS, see [Remove Active Directory Domain Services (Level 100)](/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh472163(v=ws.11)) and [Demoting domain controllers and domains](demoting-domain-controllers-and-domains--level-200-).

[](#new-administrator-password)

### New Administrator Password {#new-administrator-password .heading-anchor}

The **New Administrator Password** page requires you to provide a password for the built-in local computer\'s Administrator account. This password is used when the demotion is complete and the computer becomes a domain member server or workgroup computer.

For more information about removing AD DS, see [Remove Active Directory Domain Services (Level 100)](/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh472163(v=ws.11)) and [Demoting domain controllers and domains](demoting-domain-controllers-and-domains--level-200-).

[](#review-options-1)

### Review Options {#review-options-1 .heading-anchor}

The following screenshot shows the **Review Options** page that you see when you demote a domain controller:

You can use this page to review your selections and start the demotion.

This page also provides you with the chance to export the configuration settings for demotion to a Windows PowerShell script so you can automate other demotions.

To demote the server, select **Demote**.

**Note:** The author created this article with assistance from AI. [Learn more](/principles-for-ai-generated-content)

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

-    Last updated on 07/17/2025
