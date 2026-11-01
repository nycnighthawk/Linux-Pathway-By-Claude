---
{"title": "Delegated Managed Service Accounts overview", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/delegated-managed-service-accounts-overview", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Delegated Managed Service Accounts overview

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

A new account type known as delegated Managed Service Account (dMSA) is introduced in Windows Server 2025 that allows migration from a traditional service account to a machine account with managed and fully randomized keys, while disabling original service account passwords. Authentication for dMSA is linked to the device identity, which means that only specified machine identities mapped in Active Directory (AD) can access the account. Using dMSA helps to prevent harvesting credentials using a compromised account (kerberoasting), which is a common issue with traditional service accounts.

[](#dmsa-and-gmsa-comparison)

## dMSA and gMSA comparison {#dmsa-and-gmsa-comparison .heading-anchor}

dMSAs and gMSAs are two types of managed service accounts that are used to run services and applications in Windows Server. A dMSA is managed by an administrator and is used to run a service or application on a specific server. A gMSA is managed by AD and is used to run a service or application on multiple servers. Both offer improved security and simplified password management. dMSA differs by:

-   Utilizing gMSA concepts to limit scope of usage using [Credential Guard](/en-us/windows/security/identity-protection/credential-guard) (CG) to bind machine authentication.
-   CG can be used to enhance security in dMSA by automatically rotating passwords and binding all service account tickets. Legacy accounts are then disabled to further improve security.
-   Although gMSAs are secured with machine generated and autorotated passwords, the passwords are still not machine bound and can be stolen.

[](#functionality-of-dmsa)

## Functionality of dMSA {#functionality-of-dmsa .heading-anchor}

dMSA allows users to create them as a standalone account, or to replace an existing standard service account. When a dMSA supersedes an existing account, authentication to that existing account using its password is blocked. The request is redirected to the [Local Security Authority](/en-us/windows/win32/secauthn/lsa-authentication) (LSA) to authenticate using dMSA, which has access to everything the previous account could access in AD.

During migration, dMSA automatically learns the devices on which the service account to be used which is then used to move from all existing service accounts.

dMSA uses a randomized secret (derived from the machine account credential) that is held by the Domain Controller (DC) to encrypt tickets. The secret can be further protected by enabling CG. While the secrets used by dMSA are updated periodically on an epoch like a gMSA, the key difference is that dMSA\'s secret can\'t be retrieved or found anywhere other than on the DC.

[](#migration-flow-for-dmsa)

## Migration flow for dMSA {#migration-flow-for-dmsa .heading-anchor}

A quick concept of the migration flow process for a dMSA involves the following steps:

1.  The CG policy can be configured to protect the machines identity.
2.  An administrator starts and completes migration of the service account.
3.  The service account refreshes the Ticket Granting Server (TGT).
4.  The service account adds the machine identity to allow principles.
5.  The original service account becomes disabled.

Take note of the following when migrating dMSAs:

-   You can\'t migrate from a managed service account or a gMSA to a dMSA.
-   Wait at least two ticket lifetimes (equivalent to 14 days) after modifying the Security Descriptor (SD) before completing the dMSA migration. Keeping a service in the **start** state for four ticket lifetimes (28 days) is recommended. Delay the migration if your DCs are partitioned or replication is broken during onboarding.
-   Pay attention to sites where replication delays are longer than the default ticket renewal time of **10 hours**. The **groupMSAMembership** attribute is checked and updated at every ticket renewal, and every time the original service account logs on during the \"start migration\" state, which adds the machine account to the **groupMSAMembership** of the dMSA.
    -   Example, two sites utilize the same service account and each replication cycle takes more than 10 hours per ticket lifetime. In this scenario, a group membership is lost during the initial replication cycles.
-   Migration requires access to a Read-Write Domain Controller (RWDC) to query and modify the SD.
-   Unconstrained delegation stops working once the migration is complete if the old service account was using it. If you\'re using a dMSA protected by CG, unconstrained delegation stops working. To learn more, see [Considerations and known issues when using Credential Guard](/en-us/windows/security/identity-protection/credential-guard/considerations-known-issues).

Warning

If you\'re going to migrate to a dMSA, all machines using the service account need to be updated to support dMSA. If this isn\'t true, machines that don\'t support dMSA fails authentication with the existing service account once the account becomes disabled during migration.

[](#account-attributes-for-dmsa)

## Account attributes for dMSA {#account-attributes-for-dmsa .heading-anchor}

This section describes how the attributes for dMSA changes in the AD schema. These attributes can be viewed using the **Active Directory Users and Computers** snap-in or running **ADSI Edit** on the DC.

Note

The numerical attributes set for the account indicate:

-   **1** - Account migration has begun.
-   **2** - Account migration has completed.

Running `Start-ADServiceAccountMigration` performs the following changes:

-   The service account is granted *Generic Read* to all properties on the dMSA
-   The service account is granted *Write* property to **msDS-groupMSAMembership**
-   **msDS-DelegatedMSAState** is changed to 1
-   **msDS-ManagedAccountPrecededByLink** is set to the service account
-   **msDS-SupersededAccountState** is changed to 1
-   **msDS-SupersededManagedServiceAccountLink** is set to the dMSA

Running `Complete-ADServiceAccountMigration` performs the following changes:

-   The service account is removed from *Generic Read* to all properties on the dMSA
-   The service account is removed from *Write* property on the **msDS-GroupMSAMembership** attribute
-   **msDS-DelegatedMSAState** is set to 2
-   The Service Principal Names (SPNs) are copied over from the service account to the dMSA account
-   **msDS-AllowedToDelegateTo** is copied over if applicable
-   **msDS-AllowedToActOnBehalfOfOtherIdentity** the security descriptor is copied over if applicable
-   The assigned AuthN policy, **msDS-AssignedAuthnPolicy**, of the service account are copied over
-   dMSA is added to any AuthN policy silos that the service account was a member of
-   The trusted \"Auth for Delegation\" User Account Control (UAC) bit is copied over if it was set on the service account
-   **msDS-SupersededServiceAccountState** is set to 2
-   The service account is disabled via the UAC disable bit
-   The SPNs are removed from the account

[](#dmsa-realms)

## dMSA realms {#dmsa-realms .heading-anchor}

Realms serve as logical groupings that define authentication boundaries, commonly used when integrating different versions of AD across domains or forests. They\'re especially important in mixed domain environments where some domains may not fully support all features of dMSA. By specifying realms, dMSA can ensure proper communication and authentication flow between domains.

Administrators can use realms to specify which domains or directory components can authenticate and access the dMSA account. This ensures that even older child domains, which may not natively support dMSA features, can interact with the accounts while maintaining security boundaries. Realms facilitate seamless transitions and feature coexistence in mixed environments, ensuring compatibility between domains while maintaining strong security when enabled.

For example, if you have a primary domain called `corp.contoso.com` running on Windows Server 2025 and an older child domain called `legacy.corp.contoso.com` running Windows Server 2022, you can specify the realm as `legacy.corp.contoso.com`.

To edit this group policy setting for your environment, navigate to the following path:

**Computer Configuration\\Administrative Templates\\System\\Kerberos\\Enable Delegated Managed Service Account logons**

[](#see-also)

## See also {#see-also .heading-anchor}

[Setting up Delegated Managed Service Accounts](delegated-managed-service-accounts-set-up-dmsa)

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

-   [Setting up delegated Managed Service Accounts (dMSA) in Windows Server 2025](/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/delegated-managed-service-accounts-set-up-dmsa?source=recommendations)

    Learn how to set up delegated Managed Service Accounts (dMSA) in Windows Server 2025 to ensure device credentials isolation in Active Directory.

-   [Group Managed Service Accounts overview](/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/group-managed-service-accounts-overview?source=recommendations)

    Learn about the group Managed Service Account; practical applications, changes in Microsoft\'s implementation, both hardware and software requirements.

-   [Manage Group Managed Service Accounts](/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/manage-group-managed-service-accounts?source=recommendations)

    Learn how to manage and use Group Managed Service Accounts (gMSA) in Windows Server.

-   [Service Accounts in Windows Server](/en-us/windows-server/identity/ad-ds/manage/understand-service-accounts?source=recommendations)

    Learn how service accounts work in Windows Server, including sMSA, gMSA, dMSA, and virtual accounts, and the password policy and minimum length for each type.

-   [Active Directory Privileged Accounts and Groups Guide](/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory?source=recommendations)

    Discover Active Directory privileged accounts and groups including Enterprise Admins, Domain Admins, and built-in security groups. Learn rights, permissions, and security best practices for AD administration.

-   [Introduction to Active Directory service accounts - Microsoft Entra](/en-us/entra/architecture/service-accounts-on-premises?source=recommendations)

    An introduction to the types of service accounts in Active Directory, and how to secure them.

-   [Security Principals](/en-us/windows-server/identity/ad-ds/manage/understand-security-principals?source=recommendations)

    This article discusses security principals for Windows Server accounts and security groups and how they work in Active Directory.

Training

Module

[Active Directory Domain Services migration - Training](/en-us/training/modules/active-directory-domain-services-migration/?source=recommendations)

Determine the best approach to moving domain controllers to Windows Server 2025.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 05/30/2025
