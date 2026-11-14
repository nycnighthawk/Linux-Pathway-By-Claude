---
{"title": "Delegating Administration of Account OUs and Resource OUs", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/delegating-administration-of-account-ous-and-resource-ous", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Delegating Administration of Account OUs and Resource OUs

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Account organizational units (OUs) contain user, group, and computer objects. Resource OUs contain resources and the accounts that are responsible for managing those resources. The forest owner is responsible for creating an OU structure to manage these objects and resources and for delegating control of that structure to the OU owner.

[](#delegating-administration-of-account-ous)

## Delegating administration of account OUs {#delegating-administration-of-account-ous .heading-anchor}

Delegate an account OU structure to data administrators if they need to create and modify user, group, and computer objects. The account OU structure is a subtree of OUs for each account type that must be independently controlled. For example, the OU owner can delegate specific control to various data administrators over child OUs in an account OU for users, computers, groups, and service accounts.

The following illustration shows one example of an account OU structure.

The following table lists and describes the possible child OUs that you can create in an account OU structure.

  OU                 Purpose
  ------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Users              Contains user accounts for nonadministrative personnel.
  Service Accounts   Some services that require access to network resources run as user accounts. This OU is created to separate service user accounts from the user accounts contained in the users OU. Also, placing the different types of user accounts in separate OUs enables you to manage them according to their specific administrative requirements.
  Computers          Contains accounts for computers other than domain controllers.
  Groups             Contains groups of all types except for administrative groups, which are managed separately.
  Admins             Contains user and group accounts for data administrators in the account OU structure to allow them to be managed separately from regular users. Enable auditing for this OU so that you can track changes to administrative users and groups.

The following illustration shows one example of an administrative group design for an account OU structure.

Groups that manage the child OUs are granted full control only over the specific class of objects that they are responsible for managing.

The types of groups that you use to delegate control within an OU structure are based on where the accounts are located relative to the OU structure that is to be managed. If the admin user accounts and the OU structure all exist within a single domain, the groups that you create to use for delegation must be global groups. If your organization has a department that manages its own user accounts and exists in more than one geographical region, you might have a group of data administrators who are responsible for managing account OUs in more than one domain. If the accounts of the data administrators all exist in a single domain and you have OU structures in multiple domains to which you need to delegate control, make those administrative accounts members of global groups and delegate control of the OU structures in each domain to those global groups. If the data administrators accounts to which you delegate control of an OU structure come from multiple domains, you must use a universal group. Universal groups can contain users from different domains, and therefore, they can be used to delegate control in multiple domains.

[](#delegating-administration-of-resource-ous)

## Delegating administration of resource OUs {#delegating-administration-of-resource-ous .heading-anchor}

Resource OUs are used to manage access to resources. The resource OU owner creates computer accounts for servers that are joined to the domain that include resources such as file shares, databases, and printers. The resource OU owner also creates groups to control access to those resources.

The following illustration shows the two possible locations for the resource OU.

The resource OU can be located under the domain root or as a child OU of the corresponding account OU in the OU administrative hierarchy. Resource OUs do not have any standard child OUs. Computers and groups are placed directly in the resource OU.

The resource OU owner owns the objects within the OU but does not own the OU container itself. Resource OU owners manage only computer and group objects; they cannot create other classes of objects within the OU, and they cannot create child OUs.

Note

The creator or owner of an object has the ability to set the access control list (ACL) on the object regardless of the permissions that are inherited from the parent container. If a resource OU owner can reset the ACL on an OU, that owner can create any class of object in the OU, including users. For this reason, resource OU owners are not permitted to create OUs.

For each resource OU in the domain, create a global group to represent the data administrators who are responsible for managing the content of the OU. This group has full control over the group and computer objects in the OU but not over the OU container itself.

The following illustration shows the administrative group design for a resource OU.

Placing the computer accounts into a resource OU gives the OU owner control over the account objects but does not make the OU owner an administrator of the computers. In an Active Directory domain, the Domain Admins group is, by default, placed in the local Administrators group on all computers. That is, service administrators have control over those computers. If resource OU owners require administrative control over the computers in their OUs, the forest owner can apply a Restricted Groups Group Policy to make the resource OU owner a member of the Administrators group on the computers in that OU.

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

-    Last updated on 05/12/2025
