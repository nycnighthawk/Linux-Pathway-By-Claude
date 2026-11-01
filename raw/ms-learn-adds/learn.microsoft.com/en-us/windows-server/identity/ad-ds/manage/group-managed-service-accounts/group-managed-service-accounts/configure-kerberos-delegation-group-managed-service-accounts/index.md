---
{"title": "Configuring Kerberos delegation for group Managed Service Accounts", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/configure-kerberos-delegation-group-managed-service-accounts", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Configuring Kerberos delegation for group Managed Service Accounts

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Normally, when you work with Kerberos delegation, you set the service principal name (SPN) either with a setspn.exe command or manually by using the attribute editor in Active Directory Users and Computers. Additionally, enabling **View** \> **Advanced features** in Active Directory Users and Computers adds another way to configure Kerberos delegation from the **Delegation** tab of a user or a computer account.

But for standalone and group Managed Service Accounts, the **Delegation** tab doesn\'t appear, even after you add SPNs to these accounts or enable **View** \> **Advanced features**.

To configure delegation for these special accounts, you need to set the correct attributes manually. There are two attributes that you need to modify for these accounts:

-   userAccountControl defines the type of delegation.
-   msDS-AllowedToDelegateTo defines where the SPNs for delegation will be added.

You can set these attributes in two ways:

-   Use PowerShell.
-   Manually update the userAccountControl value.

[](#use-powershell-commands)

## Use PowerShell commands {#use-powershell-commands .heading-anchor}

The more secure and convenient way is to use PowerShell commands to update those attributes. You don\'t need to calculate final userAccountControl values when using PowerShell. Here are the commands to enable different types of delegation:

-   **Don\'t trust this computer for delegation**

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    Set-ADAccountControl -Identity TestgMSA$ -TrustedForDelegation $false -TrustedToAuthForDelegation $false
    Set-ADServiceAccount -Identity TestgMSA$ -Clear 'msDS-AllowedToDelegateTo'
    ```

-   **Unconstrained delegation / Trust this computer for delegation to any service**

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    Set-ADAccountControl -Identity TestgMSA$ -TrustedForDelegation $true -TrustedToAuthForDelegation $false
    Set-ADServiceAccount -Identity TestgMSA$ -Clear 'msDS-AllowedToDelegateTo'
    ```

-   **Kerberos-constrained delegation / Trust this computer for delegation to specified services only (Use Kerberos only)**

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    Set-ADAccountControl -Identity TestgMSA$ -TrustedForDelegation $false -TrustedToAuthForDelegation $false
    ```

    Update the Backend Service SPNs in msDS-AllowedToDelegateTo attribute.

-   **Kerberos-constrained delegation with protocol transition / Trust this computer for delegation to specified services only (Use any authentication protocol)**

    PowerShell

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="powershell"}
    Set-ADAccountControl -Identity TestgMSA$ -TrustedForDelegation $false -TrustedToAuthForDelegation $true
    ```

    Update the Backend Service SPNs in msDS-AllowedToDelegateTo attribute.

[](#manually-update-the-useraccountcontrol-value)

## Manually update the userAccountControl value {#manually-update-the-useraccountcontrol-value .heading-anchor}

Some of the easiest ways to modify attributes are by enabling **View** \> **Advanced features** in Active Directory Users and Computers or by using ADSIEdit.msc.

Here are the userAccountControl values that can be added for different types of delegation. Be careful when you edit this attribute value. Ensure that only the TRUSTED_FOR_DELEGATION or TRUSTED_TO_AUTH_FOR_DELEGATION flag is added, and that other properties aren\'t changed. Also, ensure that both the flags aren\'t added together in the userAccountControl value on a Managed Service Account.

  Delegation type                                                                                                                                              Property flag                    Value in hexadecimal   Value in decimal
  ------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------- ---------------------- ------------------
  Unconstrained delegation / Trust this computer for delegation to any service                                                                                 TRUSTED_FOR_DELEGATION           0x80000                524288
  Kerberos-constrained delegation / Trust this computer for delegation to specified services only (Use Kerberos only)                                          No change                        No change              No change
  Kerberos-constrained delegation with protocol transition / Trust this computer for delegation to specified services only (Use any authentication protocol)   TRUSTED_TO_AUTH_FOR_DELEGATION   0x1000000              16777216

When you manually update the userAccountControl value, make sure the new value is added with the existing value and doesn\'t replace the existing value. For example, say the current value of UAC is 4096 (hexadecimal 0x1000), which is WORKSTATION_TRUST_ACCOUNT:

To enable **Unconstrained delegation (Not secure)**, you must add the userAccountControl value for TRUSTED_FOR_DELEGATION together with the existing value. The UAC value should become 0x81000 (0x1000 + 0x80000), which means WORKSTATION_TRUST_ACCOUNT and TRUSTED_FOR_DELEGATION.

If you add SPNs by mistake or want to remove SPNs from the delegation list of the account, you can manually edit the **msDS-AllowedToDelegateTo** attribute of the account. This method is applicable for any user or computer account.

[](#related-content)

## Related content {#related-content .heading-anchor}

-   [Group Managed Service Accounts Overview](group-managed-service-accounts-overview)
-   [Manage Group Managed Service Accounts](manage-group-managed-service-accounts)

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Manage Group Managed Service Accounts](/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/manage-group-managed-service-accounts?source=recommendations)

    Learn how to manage and use Group Managed Service Accounts (gMSA) in Windows Server.

-   [ms-DS-Allowed-To-Delegate-To attribute - Win32 apps](/en-us/windows/win32/adschema/a-msds-allowedtodelegateto?source=recommendations)

    This is an attribute on service account (computer or user account) objects.

-   [How to configure Kerberos Constrained Delegation for Web Enrollment proxy pages - Windows Server](/en-us/troubleshoot/windows-server/active-directory/configure-kerberos-constrained-delegation?source=recommendations)

    Discusses how to implement S4U2Proxy and Constrained Delegation on a custom service account or the NetworkServices account for Web Enrollment proxy pages.

-   [Create a Key Distribution Service (KDS) Root Key](/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/create-the-key-distribution-services-kds-root-key?source=recommendations)

    Learn how to create a Key Distribution Service root key on a domain controller by using Windows PowerShell to generate group Managed Service Account passwords in Windows Server 2012 or later.

-   [Group Managed Service Accounts overview](/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/group-managed-service-accounts-overview?source=recommendations)

    Learn about the group Managed Service Account; practical applications, changes in Microsoft\'s implementation, both hardware and software requirements.

Training

Module

[Manage security in Active Directory - Training](/en-us/training/modules/manage-security-active-directory/?source=recommendations)

Learn how to manage security in Active Directory, including configuring user rights with least privilege, delegating permissions, using the Protected Users group and Credential Guard, blocking NTLM authentication, and finding problematic accounts.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 07/11/2025
