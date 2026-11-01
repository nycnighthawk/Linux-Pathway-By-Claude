---
{"title": "Setting up delegated Managed Service Accounts", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/delegated-managed-service-accounts-set-up-dmsa", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Setting up delegated Managed Service Accounts

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

A delegated Managed Service Account (dMSA) is an Active Directory (AD) account that provides secure and efficient management of credentials. Unlike traditional service accounts, dMSAs don\'t require manual password management since AD automatically takes care of it. With dMSAs, specific permissions can be delegated to access resources in the domain, which reduces security risks and provides better visibility and logs of service account activity.

Setting up a dMSA is currently only available on devices running Windows Server 2025. DMSA is a more secure and manageable approach to service account management compared to traditional service accounts. By migrating critical services to dMSA, organizations can ensure that these services are managed in a secure and compliant manner. DMSA provides a higher level of security by offering unique and frequently rotated passwords, which reduces the likelihood of unauthorized access and improves overall security.

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

-   The **Active Directory Domain Services** role must be installed on your device or on any device if using remote management tools. To learn more, see [Install or Uninstall Roles, Role Services, or Features](/en-us/windows-server/administration/server-manager/install-or-uninstall-roles-role-services-or-features).

-   Once the role is installed, your device must be promoted to a Domain Controller (DC). In **Server Manager**, the flag icon displays a new notification. Select **Promote this server to a domain controller**, then complete the necessary steps.

-   You must be a member of the **Domain Admins** or **Enterprise Admins** group, or have equivalent AD permissions, to create or migrate to a dMSA.

-   Ensure that a two-way forest trust is established between the relevant AD forests to support authentication for cross-domain and cross-forest scenarios with dMSA.

-   The **KDS root key** must be generated on the DC before a dMSA is created or migrated. Run `Get-KdsRootKey` in PowerShell to verify if the key is available. If the key is unavailable, it can be added by running `Add-KdsRootKey –EffectiveTime ((get-date).addhours(-10))`.

    Note

    In order to use the dMSA as a standalone Managed Service Account (MSA) or to supersede a legacy service account, the following command needs to be ran on the client device:

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    $params = @{
     Path = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Kerberos\Parameters"
     Name = "DelegatedMSAEnabled"
     Value = 1
     Type = "DWORD"
    }
    Set-ItemProperty @params
    ```

[](#create-a-standalone-dmsa)

## Create a standalone dMSA {#create-a-standalone-dmsa .heading-anchor}

The following instructions allow users to create a new dMSA without migrating from a traditional service account.

1.  Open a PowerShell session with admin rights and run:

    PowerShell

    ``` {.inner-focus data-language="powershell"}
    $params = @{
     Name = "ServiceAccountName"
     DNSHostName = "DNSHostName"
     CreateDelegatedServiceAccount = $true
     KerberosEncryptionType = "AES256"
    }
    New-ADServiceAccount @params
    ```

2.  Grant permission to the specific device to retrieve the password for the service account in AD:

    PowerShell

    ``` {.inner-focus data-language="powershell"}
    $params = @{
     Identity = "DMSA Name"
     PrincipalsAllowedToRetrieveManagedPassword = "Machine$"
    }
    Set-ADServiceAccount @params
    ```

3.  The **msDS-DelegatedMSAState** property value for the dMSA must be set to **3**. To view the current property value, run:

    PowerShell

    ``` {.inner-focus data-language="powershell"}
    $params = @{
     Identity = "dMSAsnmp"
     Properties = "msDS-DelegatedMSAState"
    }
    Get-ADServiceAccount @params
    ```

    To set this value to **3**, run:

    PowerShell

    ``` {.inner-focus data-language="powershell"}
    $params = @{
     Identity = "dMSAsnmp"
     Properties = @{
      "msDS-DelegatedMSAState" = 3
     }
    }
    Set-ADServiceAccount @params
    ```

[](#migrate-to-a-dmsa)

## Migrate to a dMSA {#migrate-to-a-dmsa .heading-anchor}

To migrate a service account to a dMSA, follow these steps:

1.  Create a dMSA a described in [Create a standalone dMSA](#create-a-standalone-dmsa).

2.  Initiate account migration to a dMSA:

    PowerShell

    ``` {.inner-focus data-language="powershell"}
    $params = @{
     Identity = "<DMSAName>"
     SupersededAccount = "<DN of service account>"
    }
    Start-ADServiceAccountMigration @params
    ```

3.  If the service account being migrated to a dMSA has access to multiple servers, a registry policy must first be applied to ensure it defaults to the DC. Once you sign in using the dMSA, run:

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    $params = @{
     Path = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Kerberos\Parameters"
     Name = "DelegatedMSAEnabled"
     Value = "1"
     PropertyType = "DWORD"
     Force = $true
    }
    New-ItemProperty @params
    ```

4.  Once changes to the registry are applied and the account is linked, restart the running services for the account by running:

    PowerShell

    ``` {.inner-focus data-language="powershell"}
    Get-Service | Where-Object {$_.Status -eq "Running"} | Restart-Service
    ```

Note

In the case that the service account is connected to multiple devices and migration has ended, the [PrincipalsAllowedToRetrieveManagedPassword](/en-us/powershell/module/activedirectory/set-adserviceaccount?view=windowsserver2022-ps#example-3-set-the-principals-allowed-to-retrieve-the-password-for-an-msa&preserve-view=true) needs to be updated manually.

[](#complete-account-migration)

### Complete account migration {#complete-account-migration .heading-anchor}

Warning

When finalizing the migration, **never** delete the original service account in case you need to revert back to it post migration as this causes several issues.

To complete the account migration, traditional service accounts must be disabled to ensure that all services use the dMSA.

To disable the traditional service account, run the following command:

PowerShell

``` {.inner-focus data-language="powershell"}
$params = @{
 Identity = "<DMSAName>"
 SupersededAccount = "<DN of service account>"
}
Complete-ADServiceAccountMigration @params
```

If the wrong account is being migrated, run the following to undo all steps during migration:

PowerShell

``` {.inner-focus data-language="powershell"}
$params = @{
 Identity = "<DMSAName>"
 SupersededAccount = "<DN of service account>"
}
Undo-ADServiceAccountMigration @params
```

To revert a service account back to an inactive or unlinked state, run:

PowerShell

``` {.inner-focus data-language="powershell"}
$params = @{
 Identity = "<DMSAName>"
 SupersededAccount = "<DN of service account>"
}
Reset-ADServiceAccountMigration @params
```

[](#view-dmsa-event-logs)

## View dMSA event logs {#view-dmsa-event-logs .heading-anchor}

Events can be viewed using the Event Viewer (eventvwr.exe) by performing the following actions:

1.  Right-click on **Start** and select **Event Viewer**.
2.  In the left pane, expand **Applications and Services** and navigate to **Microsoft\\Windows\\Security-Kerberos\\Operational**.
3.  Logging for this provider is disabled by default, to enable logging, right-click on **Operational** and select **Enable Log**.

The following table describes these captured events.

  Event ID   Description
  ---------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  307        **dMSA Migration** - This event is written for both dMSAs under migration and for ones that migrated. It contains information about the old service account and the new dMSA.
  308        **dMSA Permission Add** - This event is logged when a machine attempts to add itself to the principals allowed to retrieve managed password field of a dMSA during migration.
  309        **dMSA Key Fetch** - This event is logged when the Kerberos client attempts to fetch keys for a dMSA from the domain controller.

[](#see-also)

## See also {#see-also .heading-anchor}

-   [New-ADServiceAccount](/en-us/powershell/module/activedirectory/new-adserviceaccount?view=windowsserver2025-ps&preserve-view=true)
-   [Complete-ADServiceAccountMigration](/en-us/powershell/module/activedirectory/complete-adserviceaccountmigration?view=windowsserver2025-ps&preserve-view=true)
-   [Reset-ADServiceAccountMigration](/en-us/powershell/module/activedirectory/reset-adserviceaccountmigration?view=windowsserver2025-ps&preserve-view=true)
-   [Start-ADServiceAccountMigration](/en-us/powershell/module/activedirectory/start-adserviceaccountmigration?view=windowsserver2025-ps&preserve-view=true)
-   [Undo-ADServiceAccountMigration](/en-us/powershell/module/activedirectory/undo-adserviceaccountmigration?view=windowsserver2025-ps&preserve-view=true)

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

-   [Delegated Managed Service Accounts overview in Windows Server 2025](/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/delegated-managed-service-accounts-overview?source=recommendations)

    Learn about delegated Managed Service Accounts (DMSA) that authenticate specific machine identities mapped in Active Directory along with Credential Guard to ensure device credentials isolation in Windows Server 2025.

-   [Delegation of Control in AD DS on Windows Server](/en-us/windows-server/identity/ad-ds/manage/delegation-control-wizard?source=recommendations)

    Learn how to delegate administrative control in Active Directory Domain Services on Windows Server.

-   [Active Directory Privileged Accounts and Groups Guide](/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory?source=recommendations)

    Discover Active Directory privileged accounts and groups including Enterprise Admins, Domain Admins, and built-in security groups. Learn rights, permissions, and security best practices for AD administration.

-   [Redirect users and computers containers - Windows Server](/en-us/troubleshoot/windows-server/active-directory/redirect-users-computers-containers?source=recommendations)

    Describes how to use redirusr and redircmp to redirect user, computer, and group accounts in Active Directory domains.

-   [Default workstation number a user can join to the domain - Windows Server](/en-us/troubleshoot/windows-server/active-directory/default-workstation-numbers-join-domain?source=recommendations)

    Describes the default number of workstations a user can join to the domain and how to the change the AD to allow more or fewer machine accounts in the domain.

-   [Service Accounts in Windows Server](/en-us/windows-server/identity/ad-ds/manage/understand-service-accounts?source=recommendations)

    Learn how service accounts work in Windows Server, including sMSA, gMSA, dMSA, and virtual accounts, and the password policy and minimum length for each type.

-   [Active Directory domain join permissions in Windows Server](/en-us/windows-server/identity/ad-ds/manage/active-directory-domain-join-permissions?source=recommendations)

    This article describes the permissions required in Active Directory to successfully join computers to a Windows Server domain using a new computer account or an existing account.

Training

Module

[Active Directory Domain Services migration - Training](/en-us/training/modules/active-directory-domain-services-migration/?source=recommendations)

Determine the best approach to moving domain controllers to Windows Server 2025.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 05/30/2025
