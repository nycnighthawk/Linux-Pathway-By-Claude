---
{"title": "Manage group Managed Service Accounts", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/manage-group-managed-service-accounts", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Manage group Managed Service Accounts

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

In this article, learn how to enable and use group Managed Service Accounts (gMSA) in Windows Server.

Authentication protocols supporting mutual authentication such as Kerberos can\'t be used unless all the instances of the services use the same principal. For example, when a client computer connects to a service that uses load balancing or another method where all the servers appear to be the same service to the client. Meaning each service has to use the same passwords or keys to prove their identity. Group Managed Service Accounts are a type of account that can be used with multiple servers. A gMSA is a domain account that can be used to run services on multiple servers without having to manage the password. The gMSA provides automatic password management and simplified service principal name (SPN) management, including delegation of management to other administrators.

Note

Failover clusters don\'t support gMSAs. However, services that run on top of the Cluster service can use a gMSA or a sMSA if they\'re a Windows service, an App pool, a scheduled task, or natively support gMSA or sMSA.

Services can choose the principal to use. Each principal type supports different services and has different limitations.

  Principals                                   Services supported                        Password management
  -------------------------------------------- ----------------------------------------- -------------------------------------------------------
  Computer Account of Windows system           Limited to one domain joined server       Computer manages
  Computer Account without Windows system      Any domain joined server                  None
  Virtual Account                              Limited to one server                     Computer manages
  Windows standalone Managed Service Account   Limited to one domain joined server       Computer manages
  User Account                                 Any domain joined server                  None
  Group Managed Service Account                Any Windows Server domain-joined server   The domain controller manages, and the host retrieves

A Windows computer account, a Windows standalone Managed Service Account (sMSA), or virtual accounts can\'t be shared across multiple systems. When you use virtual accounts, the identity is also local to the machine and not recognized by the domain. If you configure one account for services on server farms to share, you would have to choose a user account or a computer account apart from a Windows system. Either way, these accounts don\'t have the capability of single-point-of-control password management. Without password management, each organization needs to update keys for the service in Active Directory (AD) and distribute these keys to all instances of those services.

With Windows Server, services and service administrators don\'t need to manage password synchronization between service instances when using gMSA. You create the gMSA in AD and then configure the service that supports Managed Service Accounts. Use of the gMSA is scoped to any machine that is able to use the Lightweight Directory Access Protocol (LDAP) to retrieve the gMSA\'s credentials. You can create a gMSA using the `New-ADServiceAccount` cmdlets that are part of the AD module. The following services support the service identity configuration on the host.

-   Same APIs as sMSA, so products that support sMSA support gMSA

-   Services that use [Service Control Manager](/en-us/windows/win32/services/services) to configure logon identity

-   Services that use the Internet Information Services (IIS) manager for [application pools](/en-us/iis/manage/configuring-security/application-pool-identities) to configure identity

-   Tasks using [Task Scheduler](/en-us/windows/win32/taskschd/task-scheduler-start-page).

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

To manage gMSAs, your device must meet the following requirements:

-   Your device must have the **Active Directory Domain Services** (AD DS) role installed. To learn more, see [Add or remove roles and features in Windows Server](/en-us/windows-server/administration/server-manager/add-remove-roles-features).

-   You must be a member of the **Domain Admins** or **Enterprise Admins** group.

-   Both the domain and forest functional levels should be set to Windows Server 2012 or later to support gMSA features for all devices. To learn more about updating the schema, see [Raise domain and forest functional levels in Active Directory Domain Services](/en-us/windows-server/identity/ad-ds/plan/raise-domain-forest-functional-levels).

-   A Key Distribution Services (KDS) root key must be created in the domain for secure password management. Verify its creation using the KdsSvc Operational log (Event ID 4004). To learn more about creating the KDS (kdssvc.dll) root key, see [Create the Key Distribution Services KDS Root Key](create-the-key-distribution-services-kds-root-key).

Tip

To control which hosts or services can use a gMSA, add their computer accounts to a designated security group (either new or existing) and assign the necessary permissions to this group. Likewise, use a security group to manage access for services running under gMSAs, ensuring the group has all required permissions for service operation and resource access.

For Kerberos authentication to work with services using gMSAs, the following are required:

-   Ensure that the SPNs are correctly registered for each service using a gMSA. This allows Kerberos to identify and authenticate the service.

-   Ensure DNS records are set up correctly for name resolution, which Kerberos relies on for locating domain services.

-   Ensure that firewalls and network policies allow Kerberos traffic and necessary service communications.

-   For the Kerberos ticket lifetime settings, configure the ticket expiration and renewal policies in line with your security and operational requirements.

-   All systems involved in the authentication process must have synchronized clocks. Kerberos is sensitive to time configuration, and discrepancies can cause authentication failures.

-   All systems that log on as, or install using a gMSA must support the Kerberos encryption types required by gMSA. Systems that don\'t meet this requirement can\'t log on or install gMSA.

If you\'re managing AD from a computer that isn\'t a domain controller, install the Remote Server Administration Tools (RSAT) to access the necessary management features. RSAT provides the AD module for PowerShell. After installing RSAT, open PowerShell as an administrator and run `Import-Module ActiveDirectory` to enable AD management cmdlets. This allows administrators to manage AD remotely and securely, minimizing the load on domain controllers.

[](#create-a-gmsa)

### Create a gMSA {#create-a-gmsa .heading-anchor}

To create a gMSA using PowerShell, follow these steps in an elevated PowerShell window:

Important

gMSA account names must be unique within a forest level and not just a domain. Attempting to create a gMSA account with a duplicate name fails, even in different domains.

1.  Create the KDS Root Key, if one doesn\'t exist, by following the guidance in [Create the Key Distribution Services KDS Root Key](/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/create-the-key-distribution-services-kds-root-key). If a key already exists, skip this step.

2.  To create a gMSA, run the following command. Replace `<gMSAName>` with your desired gMSA name and `<domain>` with your domain\'s name. Replace `<SecurityGroup>` with the name of the security group or computer accounts that should have access to retrieve the gMSA\'s password.

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    New-ADServiceAccount -Name <gMSAName> -DNSHostName <gMSAName>.<domain> -PrincipalsAllowedToRetrieveManagedPassword <SecurityGroup>
    ```

    To create a gMSA for outbound authentication only, run the following command. Replace `<Days>` with a numerical value. If a value isn\'t provided, it defaults to `30` days.

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    New-ADServiceAccount -Name <gMSAName> -DNSHostName <gMSAName>.<domain> -RestrictToOutboundAuthenticationOnly -ManagedPasswordIntervalInDays <Days> -PrincipalsAllowedToRetrieveManagedPassword <SecurityGroup>
    ```

    Important

    The password change interval can only be set during creation. If you need to change the interval, you must create a new gMSA and set it at creation time.

3.  Run the following command to verify see if the target device has access to retrieve the gMSA password.

    PowerShell

    ``` {.inner-focus data-language="powershell"}
    Test-ADServiceAccount -Identity <gMSAName>
    ```

Membership in the appropriate security group or having the necessary delegated permissions to create `msDS-GroupManagedServiceAccount` objects is required to complete this procedure. While members of **Account Operators** can manage certain user and group objects in AD, they don\'t have default rights to create gMSAs unless those permissions are delegated to them. For detailed information about using the appropriate accounts and group memberships, see [Active Directory security groups](../../understand-security-groups).

You can also update the gMSA properties using the `Set-ADServiceAccount` cmdlet. For example, to update the computers display name, run the following command replacing `<gMSAName>` and `<NewDisplayName>` with your values:

PowerShell

``` {.inner-focus data-language="powershell"}
Set-ADServiceAccount -Identity "<gMSAName>" -DisplayName "<NewDisplayName>"
```

For detailed information on how to set other properties for the gMSA, see [Set-ADServiceAccount](/en-us/powershell/module/activedirectory/set-adserviceaccount#examples).

[](#verify-changes-to-a-gmsa)

## Verify changes to a gMSA {#verify-changes-to-a-gmsa .heading-anchor}

After making changes to a gMSA, you can verify if the gMSA is updated correctly. These changes include adding, removing, and uninstalling a gMSA. You can also perform this step at any time when updates are made to the gMSA properties.

Run the following command replacing `<gMSAName>` with the name of the gMSA you created:

PowerShell

``` {.inner-focus data-language="powershell"}
Get-ADServiceAccount -Identity "<gMSAName>" | Select-Object *
```

[](#add-member-hosts-to-a-security-group)

## Add member hosts to a security group {#add-member-hosts-to-a-security-group .heading-anchor}

Note

-   **Group-centric management** (`Add-ADGroupMember` / `Remove-ADGroupMember`): Use these cmdlets when you want to manage the membership of a specific group. They\'re best suited for adding or removing multiple users, computers, or other objects to or from a single group efficiently.

-   **Principal-centric management** (`Add-ADPrincipalGroupMembership` / `Remove-ADPrincipalGroupMembership`): Choose these cmdlets when your goal is to manage a specific user or computer\'s membership across multiple groups. They allow you to add or remove a principal from several groups in a single operation, making it easier to update group affiliations for individual accounts.

If you use security groups to manage member hosts, add the computer account for the new member host to the security group that contains the gMSA\'s member hosts. You can do this using one of the following methods:

-   [ADUC](#tabpanel_1_aduc)
-   [CMD](#tabpanel_1_cmd)
-   [PowerShell](#tabpanel_1_powershell)

To use the Active Directory Users and Computers (ADUC) snap-in, see [Add a computer account to a group](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc733097(v=ws.11)) and [Manage User Accounts in Active Directory Users and Computers](/en-us/windows-server/identity/ad-ds/manage-user-accounts-in-windows-server).

If using computer accounts, find the existing accounts and then add the new computer account.

[](#remove-member-hosts-from-a-security-group)

## Remove member hosts from a security group {#remove-member-hosts-from-a-security-group .heading-anchor}

-   [ADUC](#tabpanel_2_aduc)
-   [CMD](#tabpanel_2_cmd)
-   [PowerShell](#tabpanel_2_powershell)

To use the ADUC snap-in, see [Delete a Computer Account](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754624(v=ws.11)) and [Remove a user account](/en-us/windows-server/identity/ad-ds/manage-user-accounts-in-windows-server#remove-a-user-account).

[](#install-a-gmsa-on-your-system)

## Install a gMSA on your system {#install-a-gmsa-on-your-system .heading-anchor}

After creating a gMSA and adding the member hosts to the security group, you must install the gMSA on each host computer where the service runs. To install a gMSA, open an elevated PowerShell window and run the following command replacing `<gMSAName>` with your value:

PowerShell

``` {.inner-focus data-language="powershell"}
Install-ADServiceAccount -Identity <gMSAName>
```

For more information about the `Install-ADServiceAccount` cmdlet, see [Install-ADServiceAccount](/en-us/powershell/module/activedirectory/install-adserviceaccount).

[](#uninstall-a-gmsa-from-your-system)

## Uninstall a gMSA from your system {#uninstall-a-gmsa-from-your-system .heading-anchor}

While you can\'t uninstall gMSAs in ADUC, you can manually delete a gMSA by finding it in the **Managed Service Accounts** container and deleting it like any other AD object. However, keep in mind that this doesn\'t perform the same clean-up operations that `Uninstall-ADServiceAccount` would in PowerShell.

To uninstall a gMSA, open an elevated PowerShell window and follow these steps.

1.  To remove a single gMSA from your environment, run the following command replacing `<gMSAName>` with your value:

    PowerShell

    ``` {.inner-focus data-language="powershell"}
    Uninstall-ADServiceAccount -Identity <gMSAName>
    ```

2.  To remove multiple gMSAs from your environment, run the following command replacing `<gMSA#$>` with your values:

    PowerShell

    ``` {.inner-focus data-language="powershell"}
    $gMSANames = @("gMSA1$", "gMSA2$", "gMSA3$")

    foreach ($gMSAs in $gMSANames) {
      Uninstall-ADServiceAccount -Identity $gMSAs
    }
    ```

For more information about the `Uninstall-ADServiceAccount` cmdlet, see [Uninstall-ADServiceAccount](/en-us/powershell/module/activedirectory/uninstall-adserviceaccount).

[](#see-also)

## See also {#see-also .heading-anchor}

-   [Group Managed Service Accounts overview](group-managed-service-accounts-overview)

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

-   [Create a Key Distribution Service (KDS) Root Key](/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/create-the-key-distribution-services-kds-root-key?source=recommendations)

    Learn how to create a Key Distribution Service root key on a domain controller by using Windows PowerShell to generate group Managed Service Account passwords in Windows Server 2012 or later.

-   [Group Managed Service Accounts overview](/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/group-managed-service-accounts-overview?source=recommendations)

    Learn about the group Managed Service Account; practical applications, changes in Microsoft\'s implementation, both hardware and software requirements.

-   [Troubleshoot gMSAs for Windows containers](/en-us/virtualization/windowscontainers/manage-containers/gmsa-troubleshooting?source=recommendations)

    How to troubleshoot group Managed Service Accounts (gMSAs) for Windows containers.

Training

Module

[Manage Active Directory Domain Services using PowerShell cmdlets - Training](/en-us/training/modules/manage-active-directory-domain-services-use-powershell-cmdlets/?source=recommendations)

This module covers the cmdlets that are used to administer Active Directory Domain Services.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 04/16/2026
