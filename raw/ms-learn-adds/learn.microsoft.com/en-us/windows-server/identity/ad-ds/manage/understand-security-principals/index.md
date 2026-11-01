---
{"title": "Security principals", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-principals", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Security principals

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

This reference article describes security principals for Windows accounts and security groups, in addition to security technologies that are related to security principals.

[](#what-are-security-principals)

## What are security principals? {#what-are-security-principals .heading-anchor}

A security principal is any entity that can be authenticated by the operating system, such as a user account, a computer account, or the security groups for these accounts. Security principals have long been a foundation for controlling access to securable resources on Windows computers. Each security principal is represented in the operating system by a unique security identifier (SID).

Note

This content pertains only to the Windows versions in the \"Applies to\" list at the beginning of the article.

[](#how-security-principals-work)

## How security principals work {#how-security-principals-work .heading-anchor}

Security principals that are created in an Active Directory domain are Active Directory objects, which can be used to manage access to domain resources. Each security principal is assigned a unique identifier, which it retains for its entire lifetime. Local user accounts and security groups are created on a local computer, and they can be used to manage access to resources on that computer. Local user accounts and security groups are managed by the Security Account Manager (SAM) on the local computer.

[](#authorization-and-access-control-components)

### Authorization and access control components {#authorization-and-access-control-components .heading-anchor}

The following diagram illustrates the Windows authorization and access control process. In the diagram, the subject (a process that\'s initiated by a user) attempts to access an object, such as a shared folder. The information in the user's access token is compared to the access control entries (ACEs) in the object\'s security descriptor, and the access decision is made. The SIDs of security principals are used in the user\'s access token and in the ACEs in the object's security descriptor.

[](#authorization-and-access-control-process)

### Authorization and access control process {#authorization-and-access-control-process .heading-anchor}

Security principals are closely related to the following components and technologies:

-   [Security identifiers](#security-identifiers)
-   [Access tokens](#access-tokens)
-   [Security descriptors and access control lists](#security-descriptors-and-access-control-lists)
-   [Permissions](#permissions)

[](#security-identifiers)

### Security identifiers {#security-identifiers .heading-anchor}

Security identifiers (SIDs) provide a fundamental building block of the Windows security model. They work with specific components of the authorization and access control technologies in the security infrastructure of Windows Server operating systems. This helps protect access to network resources and provides a more secure computing environment.

A SID is a value of variable length that\'s used to uniquely identify a security principal that represents any entity that can be authenticated by the system. These entities include a user account, a computer account, or a security group. Each security principal is automatically assigned a SID when it\'s created. The SID is stored in a security database. When a SID is used as the unique identifier for a user or group, it can never be used to identify another user or group.

Each time a user signs in, the system creates an access token for that user. The access token contains the user\'s SID, user rights, and the SIDs for groups that the user belongs to. This token provides the security context for whatever actions the user performs on the computer.

In addition to the uniquely created, domain-specific SIDs that are assigned to specific users and groups, there are well-known SIDs that identify generic groups and generic users. For example, the *Everyone* and *World* SIDs identify groups that include all users. Well-known SIDs have values that remain constant across all operating systems.

[](#access-tokens)

### Access tokens {#access-tokens .heading-anchor}

An access token is a protected object that contains information about the identity and user rights that are associated with a user account.

When a user signs in interactively or tries to make a network connection to a computer running Windows, the sign-in process authenticates the user\'s credentials. If authentication is successful, the process returns a SID for the user and a list of SIDs for the user\'s security groups. The Local Security Authority (LSA) on the computer uses this information to create an access token (in this case, the primary access token). This includes the SIDs that are returned by the sign-in process and a list of user rights that are assigned by the local security policy to the user and to the user\'s security groups.

After the LSA creates the primary access token, a copy of the access token is attached to every thread and process that runs on the user\'s behalf. Whenever a thread or process interacts with a securable object or tries to perform a system task that requires user rights, the operating system checks the access token that\'s associated with the thread to determine the level of authorization.

There are two kinds of access tokens: primary and impersonation. Every process has a primary token that describes the security context of the user account that\'s associated with the process. A primary access token is typically assigned to a process to represent the default security information for that process. Impersonation tokens, on the other hand, are used for client and server scenarios. Impersonation tokens enable a thread to run in a security context that differs from the security context of the process that owns the thread.

[](#security-descriptors-and-access-control-lists)

### Security descriptors and access control lists {#security-descriptors-and-access-control-lists .heading-anchor}

A security descriptor is a data structure that\'s associated with each securable object. All objects in Active Directory and all securable objects on a local computer or on the network have security descriptors to help control access to the objects. Security descriptors include information about who owns an object, who can access it and in what way, and what types of access are audited. Security descriptors contain the access control list (ACL) of an object, which includes all the security permissions that apply to that object. An object\'s security descriptor can contain two types of ACLs:

-   A *discretionary* access control list (DACL), which identifies the users and groups that are allowed or denied access.

-   A *system* access control list (SACL), which controls how access is audited.

You can use this access control model to individually secure objects and attributes such as files and folders, Active Directory objects, registry keys, printers, devices, ports, services, processes, and threads. Because of this individual control, you can adjust the security of objects to meet the needs of your organization, delegate authority over objects or attributes, and create custom objects or attributes that require the definition of unique security protections.

[](#permissions)

### Permissions {#permissions .heading-anchor}

Permissions enable the owner of each securable object, such as a file, Active Directory object, or registry key, to control who can perform an operation or a set of operations on the object or object property. Permissions are expressed in the security architecture as ACEs. Because access to an object is at the discretion of the object\'s owner, the type of access control that\'s used in Windows is called discretionary access control.

Permissions are different from user rights in that permissions are attached to objects, and user rights apply to user accounts. Administrators can assign user rights to groups or users. These rights authorize users to perform specific actions, such as signing in to a system interactively or backing up files and directories.

On computers, user rights enable administrators to control who has the authority to perform operations that affect an entire computer, rather than a particular object. Administrators assign user rights to individual users or groups as part of the security settings for the computer. Although user rights can be managed centrally through Group Policy, they\'re applied locally. Users can (and usually do) have different user rights on different computers.

For information about which user rights are available and how they can be implemented, see [User Rights Assignment](/en-us/windows/device-security/security-policy-settings/user-rights-assignment).

[](#security-context-in-authentication)

### Security context in authentication {#security-context-in-authentication .heading-anchor}

A user account enables a user to sign in to computers, networks, and domains with an identity that can be authenticated by the computer, network, or domain.

In Windows, any user, service, group, or computer that can initiate action is a security principal. Security principals have accounts, which can be local to a computer or domain-based. For example, domain-joined Windows client computers can participate in a network domain by communicating with a domain controller, even when no user is signed in.

To initiate communications, the computer must have an active account in the domain. Before accepting communications from the computer, the Local Security Authority on the domain controller authenticates the computer\'s identity and then defines the computer\'s security context just as it would for a user\'s security principal.

This security context defines the identity and capabilities of a user or service on a particular computer, or of a user, service, group, or computer on a network. For example, it defines the resources (such as a file share or printer) that can be accessed and the actions (such as Read, Write, or Modify) that can be performed by a user, service, or computer on that resource.

The security context of a user or computer can vary from one computer to another, such as when a user authenticates to a server or a workstation other than the user\'s primary workstation. It can also vary from one session to another, such as when an administrator modifies the user\'s rights and permissions. In addition, the security context is different when a user or computer is operating on a standalone basis, in a mixed network domain, or as part of an Active Directory domain.

[](#accounts-and-security-groups)

## Accounts and security groups {#accounts-and-security-groups .heading-anchor}

Accounts and security groups that are created in an Active Directory domain are stored in the Active Directory database and managed by using Active Directory tools. These security principals are directory objects, and they can be used to manage access to domain resources.

Local user accounts and security groups are created on a local computer, and they can be used to manage access to resources on that computer. Local user accounts and security groups are stored in and managed by the Security Accounts Manager (SAM) on the local computer.

[](#user-accounts)

### User accounts {#user-accounts .heading-anchor}

A user account uniquely identifies a person who is using a computer system. The account signals the system to enforce the appropriate authorization to allow or deny that user access to resources. User accounts can be created in Active Directory and on local computers, and administrators use them to:

-   Represent, identify, and authenticate the identity of a user. A user account enables a user to sign in to computers, networks, and domains with a unique identifier that can be authenticated by the computer, network, or domain.

-   Authorize (grant or deny) access to resources. After a user has been authenticated, the user is authorized access to resources based on the permissions that are assigned to that user for the resource.

-   Audit the actions that are carried out on a user account.

Windows and the Windows Server operating systems have built-in user accounts, or you can create user accounts to meet the requirements of your organization.

[](#security-groups)

### Security groups {#security-groups .heading-anchor}

A security group is a collection of user accounts, computer accounts, and other groups of accounts that can be managed as a single unit from a security perspective. In Windows operating systems, there are several built-in security groups that are preconfigured with the appropriate rights and permissions for performing specific tasks. Additionally, you can (and usually will) create a security group for each unique combination of security requirements that applies to multiple users in your organization.

Groups can be Active Directory-based or local to a particular computer:

-   Active Directory security groups are used to manage rights and permissions to domain resources.

-   Local groups exist in the SAM database on local computers (on all Windows-based computers) except domain controllers. You use local groups to manage rights and permissions only to resources on the local computer.

By using security groups to manage access control, you can:

-   Simplify administration. You can assign a common set of rights, a common set of permissions, or both to many accounts at one time, rather than assigning them to each account individually. Also, when users transfer jobs or leave the organization, permissions aren\'t tied to their user accounts, making permission reassignment or removal easier.

-   Implement a role-based access control model. You can use this model to grant permissions by using groups with different scopes for appropriate purposes. Scopes that are available in Windows include local, global, domain local, and universal.

-   Minimize the size of ACLs and speed up security checking. A security group has its own SID, so the group SID can be used to specify permissions for a resource. In an environment with more than a few thousand users, if the SIDs of individual user accounts are used to specify access to a resource, the ACL of that resource can become unmanageably large, and the time that\'s needed for the system to check permissions to the resource can become unacceptable.

For descriptions and settings information about the domain security groups that are defined in Active Directory, see [Active Directory security groups](understand-security-groups).

For descriptions and settings information about special identities, see [Special identity groups](understand-special-identities-groups).

[](#related-content)

## Related content {#related-content .heading-anchor}

-   [Access control overview](/en-us/windows/security/identity-protection/access-control/access-control)

------------------------------------------------------------------------

## Feedback {#ms--feedback .title .is-3}

Was this page helpful?

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

------------------------------------------------------------------------

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3}

Documentation

-   [Active Directory Security Groups](/en-us/windows-server/identity/ad-ds/manage/understand-security-groups?source=recommendations)

    Become familiar with Windows Server Active Directory security groups, group scope, and group functions. See information on groups, such as members and rights.

-   [Active Directory Accounts](/en-us/windows-server/identity/ad-ds/manage/understand-default-user-accounts?source=recommendations)

    This article discusses how to create default local Windows Server Active Directory accounts on a domain controller.

-   [Special Identity Groups](/en-us/windows-server/identity/ad-ds/manage/understand-special-identities-groups?source=recommendations)

    Learn about Windows Server special identity groups that are used for Windows access control.

-   [Group Policy overview for Windows Server](/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview?source=recommendations)

    Learn about what Group Policy does and how it works with Active Directory Domain Services in Windows.

-   [Active Directory Privileged Accounts and Groups Guide](/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory?source=recommendations)

    Discover Active Directory privileged accounts and groups including Enterprise Admins, Domain Admins, and built-in security groups. Learn rights, permissions, and security best practices for AD administration.

-   [Active Directory Replication and Topology Management Using Windows PowerShell](/en-us/windows-server/identity/ad-ds/manage/powershell/active-directory-replication-and-topology-management-using-windows-powershell?source=recommendations)

    Learn more about: Active Directory Replication and Topology Management Using Windows PowerShell

Training

Module

[Secure Windows Server user accounts - Training](/en-us/training/modules/secure-windows-server-user-accounts/?source=recommendations)

Learn how to secure Active Directory user accounts using least privilege, Protected Users group, authentication policy silos, Windows Defender Credential Guard, NTLM blocking, and account remediation techniques.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 07/11/2025
