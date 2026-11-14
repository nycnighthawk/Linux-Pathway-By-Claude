---
{"title": "Delegation of control in Active Directory Domain Services", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/delegation-control-wizard", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Delegation of control in Active Directory Domain Services

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Delegation of control means you can assign a range of administrative tasks to different users and groups. You can assign basic administrative tasks to regular users or groups, and leave domain-wide and forest-wide administration to members of the Domain Admins and Enterprise Admins groups. By delegating administration, you can allow groups within your organization to take more control of their local resources. You also help secure your Active Directory environment against accidental or malicious damage by limiting the membership of administrator groups.

You can delegate administrative control to any level of a domain tree by creating organizational units within a domain and delegating administrative control for specific organizational units to particular users or groups. To decide what organizational units you want to create, and which organizational units should contain accounts or shared resources, consider the structure of your organization.

Active Directory defines specific permissions and user rights that can be used for delegating or restricting administrative control. By using a combination of organizational units, groups, and permissions, you can define the most appropriate administrative scope for a particular person. This scope could be an entire domain, all organizational units within a domain, or a single organizational unit.

You can assign administrative control to a user or group by using the *Delegation of Control Wizard*. You can use the Delegation of Control Wizard to delegate the following tasks:

-   Create, delete, and manage user accounts
-   Reset user passwords and force password change at next logon
-   Read all user information
-   Modify the membership of a group
-   Join a computer to a domain
-   Manage Group Policy links
-   Generate Resultant Set of Policy (Planning)
-   Generate Resultant Set of Policy (Logging)
-   Create, delete, and manage inetOrgPerson accounts
-   Reset inetOrgPerson passwords and force password change at next sign-in
-   Read all inetOrgPerson information

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

Before you can delegate control, you need to meet the following prerequisites.

-   You must be a member of the Domain Admins group or have been delegated the necessary permissions to perform the tasks you want to delegate.

-   On the computer where you\'ll delegate control, you must have the AD DS Remote Server Administration Tools (RSAT) installed.

[](#delegate-control)

## Delegate control {#delegate-control .heading-anchor}

When you use the Delegation of Control Wizard, you delegate not only at the domain or organizational unit level, but to all objects under the parent container.

To use the Delegation of Control Wizard, perform the following steps:

1.  In Active Directory Users and Computers, select the parent container. For example, select the domain or organizational unit over which you want to delegate control.

2.  On the **Action** menu, select **Delegate control**. This action starts the Delegation of Control Wizard.

3.  On the Users or Groups page, select the users or groups to which you\'re delegating privileges.

4.  On the Tasks to Delegate page, select the task that you want to delegate from a list of common tasks, as described earlier in this article.

5.  Select **Finish** to complete the delegation process.

You can also choose the create a custom task to delegate option if you want to create a custom task. Creating a custom task involves specifying the type of object that the task relates to and the permissions you want to delegate. The common tasks apply to all objects within the scope of the container on which you perform delegation.

[](#related-content)

## Related content {#related-content .heading-anchor}

-   [Delegating Administration by Using OU Objects](../plan/delegating-administration-by-using-ou-objects)
-   [Tier Model for Active Directory Domain Services](../tier-model)
-   [Setting up delegated Managed Service Accounts](../../../security/delegated-managed-service-accounts/delegated-managed-service-accounts-set-up-dmsa)

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

-   [Delegating Administration by Using OU Objects](/en-us/windows-server/identity/ad-ds/plan/delegating-administration-by-using-ou-objects?source=recommendations)

    Learn more about: Delegating Administration by Using OU Objects

-   [Delegating Administration of Default Containers and OUs](/en-us/windows-server/identity/ad-ds/plan/delegating-administration-of-default-containers-and-ous?source=recommendations)

    Learn more about: Delegating Administration of Default Containers and OUs

-   [Active Directory Security Groups](/en-us/windows-server/identity/ad-ds/manage/understand-security-groups?source=recommendations)

    Become familiar with Windows Server Active Directory security groups, group scope, and group functions. See information on groups, such as members and rights.

-   [Active Directory domain join permissions in Windows Server](/en-us/windows-server/identity/ad-ds/manage/active-directory-domain-join-permissions?source=recommendations)

    This article describes the permissions required in Active Directory to successfully join computers to a Windows Server domain using a new computer account or an existing account.

-   [Back Up and Restore Group Policy in Windows](/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-backup-restore?source=recommendations)

    Learn how to back up, restore, migrate, and copy Group Policy Objects by using the Group Policy Management Console in Windows.

-   [Delegating Administration of Account OUs and Resource OUs](/en-us/windows-server/identity/ad-ds/plan/delegating-administration-of-account-ous-and-resource-ous?source=recommendations)

    Learn more about: Delegating Administration of Account OUs and Resource OUs

-   [Active Directory Accounts](/en-us/windows-server/identity/ad-ds/manage/understand-default-user-accounts?source=recommendations)

    This article discusses how to create default local Windows Server Active Directory accounts on a domain controller.

-   [Active Directory Privileged Accounts and Groups Guide](/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory?source=recommendations)

    Discover Active Directory privileged accounts and groups including Enterprise Admins, Domain Admins, and built-in security groups. Learn rights, permissions, and security best practices for AD administration.

Training

Module

[Guided project - Administer Active Directory Domain Services - Training](/en-us/training/modules/guided-project-administer-active-directory-domain-services/?source=recommendations)

This guided project helps prepare you to manage Active Directory Domain services, including creating and deploying domains, configuring group policy objects, establishing and enforcing passwords, and maintaining security of Active Directory.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 07/01/2026
