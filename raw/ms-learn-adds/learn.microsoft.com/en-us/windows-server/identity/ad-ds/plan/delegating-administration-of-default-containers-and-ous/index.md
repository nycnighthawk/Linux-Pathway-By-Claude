---
{"title": "Delegating Administration of Default Containers and OUs", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/delegating-administration-of-default-containers-and-ous", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Delegating Administration of Default Containers and OUs

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Every Active Directory domain contains a standard set of containers and organizational units (OUs) that are created during the installation of Active Directory Domain Services (AD DS). These include the following:

-   Domain container, which serves as the root container to the hierarchy

-   Built-in container, which holds the default service administrator accounts

-   Users container, which is the default location for new user accounts and groups created in the domain

-   Computers container, which is the default location for new computer accounts created in the domain

-   Domain Controllers OU, which is the default location for the computer accounts for domain controllers computer accounts

The forest owner controls these default containers and OUs.

[](#domain-container)

## Domain container {#domain-container .heading-anchor}

The domain container is the root container of the hierarchy of a domain. Changes to the policies or the access control list (ACL) on this container can potentially have domain-wide impact. Do not delegate control of this container; it must be controlled by the service administrators.

[](#users-and-computers-containers)

## Users and computers containers {#users-and-computers-containers .heading-anchor}

When you perform an in-place domain upgrade from Windows Server 2003 to Windows Server 2008 , existing users and computers are automatically placed into the users and the computers containers. If you are creating a new Active Directory domain, the users and computers containers are the default locations for all new user accounts and non-domain-controller computer accounts in the domain.

Important

If you need to delegate control over users or computers, do not modify the default settings on the users and computers containers. Instead, create new OUs (as needed) and move the user and computer objects from their default containers and into the new OUs. Delegate control over the new OUs, as needed. We recommend that you not modify who controls the default containers.

Also, you cannot apply Group Policy settings to the default users and computers containers. To apply Group Policy to users and computers, create new OUs and move the user and computer objects into those OUs. Apply the Group Policy settings to the new OUs.

Optionally, you can redirect the creation of objects that are placed in the default containers to be placed in containers of your choice.

[](#well-known-users-and-groups-and-built-in-accounts)

## Well-known users and groups and built-in accounts {#well-known-users-and-groups-and-built-in-accounts .heading-anchor}

By default, several well-known users and groups and built-in accounts are created in a new domain. We recommend that management of these accounts remains under the control of the service administrators. Do not delegate management of these accounts to an individual who is not a service administrator. The following table lists the well-known users and groups and built-in accounts that need to remain under the control of the service administrators.

+---------------------------------------------+------------------------------------+
| Well-known users and groups                 | Built-in accounts                  |
+=============================================+====================================+
| Cert Publishers                             | Administrator                      |
|                                             |                                    |
| Domain Controllers                          | Guest                              |
|                                             |                                    |
| Group Policy Creator Owners                 | Guests                             |
|                                             |                                    |
| KRBTGT                                      | Account Operators                  |
|                                             |                                    |
| Domain Guests                               | Administrators                     |
|                                             |                                    |
| Administrator                               | Backup Operators                   |
|                                             |                                    |
| Domain Admins                               | Incoming Forest Trust Builders     |
|                                             |                                    |
| Schema Admins (forest root domain only)     | Print Operators                    |
|                                             |                                    |
| Enterprise Admins (forest root domain only) | Pre-Windows 2000 Compatible Access |
|                                             |                                    |
| Domain Users                                | Server Operators                   |
|                                             |                                    |
|                                             | Users                              |
+---------------------------------------------+------------------------------------+

[](#domain-controller-ou)

## Domain Controller OU {#domain-controller-ou .heading-anchor}

When domain controllers are added to the domain, their computer objects are automatically added to the Domain Controller OU. This OU has a default set of policies applied to it. To ensure that these policies are applied uniformly to all domain controllers, we recommend that you not move the computer objects of the domain controllers out of this OU. Failure to apply the default policies can cause a domain controller to fail to function properly.

By default, the service administrators control this OU. Do not delegate control of this OU to individuals other than the service administrators.

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Delegating Administration of Account OUs and Resource OUs](/en-us/windows-server/identity/ad-ds/plan/delegating-administration-of-account-ous-and-resource-ous?source=recommendations)

    Learn more about: Delegating Administration of Account OUs and Resource OUs

-   [Delegating Administration by Using OU Objects](/en-us/windows-server/identity/ad-ds/plan/delegating-administration-by-using-ou-objects?source=recommendations)

    Learn more about: Delegating Administration by Using OU Objects

-   [Delegation of Control in AD DS on Windows Server](/en-us/windows-server/identity/ad-ds/manage/delegation-control-wizard?source=recommendations)

    Learn how to delegate administrative control in Active Directory Domain Services on Windows Server.

-   [Active Directory domain join permissions in Windows Server](/en-us/windows-server/identity/ad-ds/manage/active-directory-domain-join-permissions?source=recommendations)

    This article describes the permissions required in Active Directory to successfully join computers to a Windows Server domain using a new computer account or an existing account.

-   [Back Up and Restore Group Policy in Windows](/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-backup-restore?source=recommendations)

    Learn how to back up, restore, migrate, and copy Group Policy Objects by using the Group Policy Management Console in Windows.

-   [Reviewing OU Design Concepts](/en-us/windows-server/identity/ad-ds/plan/reviewing-ou-design-concepts?source=recommendations)

    Learn more about: Reviewing OU Design Concepts

-   [Redirect users and computers containers - Windows Server](/en-us/troubleshoot/windows-server/active-directory/redirect-users-computers-containers?source=recommendations)

    Describes how to use redirusr and redircmp to redirect user, computer, and group accounts in Active Directory domains.

Training

Module

[Introduction to AD DS - Training](/en-us/training/modules/introduction-to-ad-ds/?source=recommendations)

Introduction to AD DS

------------------------------------------------------------------------

-    Last updated on 05/12/2025
