---
{"title": "Special identity groups", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-special-identities-groups", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Special identity groups

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Learn about Windows Server special identity groups (sometimes called *security groups*) that are used for Windows access control.

[](#what-is-a-special-identity-group)

## What is a special identity group? {#what-is-a-special-identity-group .heading-anchor}

Special identity groups are similar to the Active Directory security groups that are listed in the Active Directory Users and BuiltIn containers. Special identity groups can provide an efficient way to assign access to resources in your network. By using special identity groups, you can:

-   Assign user rights to security groups in Active Directory.

-   Assign permissions to security groups to access resources.

[](#how-special-identity-groups-work-in-windows-server)

## How special identity groups work in Windows Server {#how-special-identity-groups-work-in-windows-server .heading-anchor}

If a server is running one of the versions of the Windows Server operating system shown in **Applies to** at the beginning of this article, the server has several special identity groups. These special identity groups don\'t have specific memberships that you can modify, but they can represent different users at different times, depending on the circumstances.

Although you can assign rights and permissions for specific resources to a special identity group, you can\'t view or modify the membership of a special identity group. Group scopes don\'t apply to special identity groups. Users are automatically assigned to special identity groups when they sign in or access a specific resource.

For information about Active Directory security groups and group scopes, see [Active Directory security groups](understand-security-groups).

[](#default-special-identity-groups)

## Default special identity groups {#default-special-identity-groups .heading-anchor}

The following sections describe the default special identity groups in Windows Server.

-   [Anonymous Logon](#anonymous-logon)
-   [Attested key property](#attested-key-property)
-   [Authenticated Users](#authenticated-users)
-   [Authentication authority asserted identity](#authentication-authority-asserted-identity)
-   [Batch](#batch)
-   [Console logon](#console-logon)
-   [Creator Group](#creator-group)
-   [Creator Owner](#creator-owner)
-   [Dialup](#dialup)
-   [Digest Authentication](#digest-authentication)
-   [Enterprise Domain Controllers](#enterprise-domain-controllers)
-   [Enterprise Read-only Domain Controllers](#enterprise-read-only-domain-controllers)
-   [Everyone](#everyone)
-   [Fresh Public Key identity](#fresh-public-key-identity)
-   [Interactive](#interactive)
-   [IUSR](#iusr)
-   [Key trust](#key-trust)
-   [Local Service](#local-service)
-   [LocalSystem](#localsystem)
-   [MFA key property](#mfa-key-property)
-   [Network](#network)
-   [Network Service](#network-service)
-   [NTLM Authentication](#ntlm-authentication)
-   [Other Organization](#other-organization)
-   [Owner Rights](#owner-rights)
-   [Principal Self](#principal-self)
-   [Proxy](#proxy)
-   [Read-only Domain Controllers](#read-only-domain-controllers)
-   [Remote Interactive Logon](#remote-interactive-logon)
-   [Restricted](#restricted)
-   [SChannel Authentication](#schannel-authentication)
-   [Service](#service)
-   [Service asserted identity](#service-asserted-identity)
-   [Terminal Server User](#terminal-server-user)
-   [This Organization](#this-organization)
-   [Window Manager\\Window Manager Group](#window-managerwindow-manager-group)

[](#anonymous-logon)

### Anonymous Logon {#anonymous-logon .heading-anchor}

Any user who accesses the system through an anonymous logon has the Anonymous Logon identity. This identity allows anonymous access to resources, like to a webpage that\'s published on a corporate server. The Anonymous Logon group isn\'t a member of the Everyone group by default.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-5-7
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#attested-key-property)

### Attested key property {#attested-key-property .heading-anchor}

A security identifier (SID) that means the key trust object had the attestation property.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-18-6
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#authenticated-users)

### Authenticated Users {#authenticated-users .heading-anchor}

Any user who accesses the system through a sign-in process has the Authenticated Users identity. This identity allows access to shared resources within the domain, such as files in a shared folder that should be accessible to all the employees in the organization. Membership is controlled by the operating system.

+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attribute                            | Value                                                                                                                                                       |
+======================================+=============================================================================================================================================================+
| Well-known SID/RID                   | S-1-5-11                                                                                                                                                    |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Object class                         | Foreign Security Principal                                                                                                                                  |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default location in Active Directory | CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>                                                                                 |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default user rights                  | [Access this computer from the network](/en-us/windows/device-security/security-policy-settings/access-this-computer-from-the-network): SeNetworkLogonRight |
|                                      |                                                                                                                                                             |
|                                      | [Add workstations to domain](/en-us/windows/device-security/security-policy-settings/add-workstations-to-domain): SeMachineAccountPrivilege                 |
|                                      |                                                                                                                                                             |
|                                      | [Bypass traverse checking](/en-us/windows/device-security/security-policy-settings/bypass-traverse-checking): SeChangeNotifyPrivilege                       |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[](#authentication-authority-asserted-identity)

### Authentication authority asserted identity {#authentication-authority-asserted-identity .heading-anchor}

An SID that means the client\'s identity is asserted by an authentication authority based on proof of possession of client credentials.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-18-1
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#batch)

### Batch {#batch .heading-anchor}

Any user or process that accesses the system as a batch job or through the batch queue has the Batch identity. This identity allows batch jobs to run scheduled tasks, such as a nightly cleanup job that deletes temporary files. Membership is controlled by the operating system.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-5-3
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#console-logon)

### Console logon {#console-logon .heading-anchor}

A group that includes users who are logged on to the physical console. This SID can be used to implement security policies that grant different rights based on whether a user has been granted physical access to the console.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-2-1
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#creator-group)

### Creator Group {#creator-group .heading-anchor}

The person who created a file or directory is a member of this special identity group. The Windows Server operating system uses this identity to automatically grant access permissions to the creator of a file or directory.

A placeholder SID is created in an inheritable access control entry (ACE). When the ACE is inherited, the system replaces this SID with the SID for the primary group of the object's current owner. The primary group is used only by the POSIX subsystem.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-3-1
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#creator-owner)

### Creator Owner {#creator-owner .heading-anchor}

The person who created a file or directory is a member of this special identity group. The Windows Server operating system uses this identity to automatically grant access permissions to the creator of a file or directory. A placeholder SID is created in an inheritable ACE. When the ACE is inherited, the system replaces this SID with the SID for the object's current owner.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-3-0
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#dialup)

### Dialup {#dialup .heading-anchor}

Any user who accesses the system through a dial-up connection has the Dialup identity. This identity distinguishes dial-up users from other types of authenticated users.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-5-1
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#digest-authentication)

### Digest Authentication {#digest-authentication .heading-anchor}

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-5-64-21
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#enterprise-domain-controllers)

### Enterprise Domain Controllers {#enterprise-domain-controllers .heading-anchor}

This group includes all domain controllers in an Active Directory forest. Domain controllers with enterprise-wide roles and responsibilities have the Enterprise Domain Controllers identity. This identity allows domain controllers to perform certain tasks in the enterprise by using transitive trusts. Membership is controlled by the operating system.

+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attribute                            | Value                                                                                                                                                       |
+======================================+=============================================================================================================================================================+
| Well-known SID/RID                   | S-1-5-9                                                                                                                                                     |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Object class                         | Foreign Security Principal                                                                                                                                  |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default location in Active Directory | CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>                                                                                 |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default user rights                  | [Access this computer from the network](/en-us/windows/device-security/security-policy-settings/access-this-computer-from-the-network): SeNetworkLogonRight |
|                                      |                                                                                                                                                             |
|                                      | [Allow log on locally](/en-us/windows/device-security/security-policy-settings/allow-log-on-locally): SeInteractiveLogonRight                               |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[](#enterprise-read-only-domain-controllers)

### Enterprise Read-only Domain Controllers {#enterprise-read-only-domain-controllers .heading-anchor}

This group includes all Read-only Domain Controllers (RODC) in an Active Directory forest. An Enterprise RODC can replicate a larger subset of the Active Directory database, including the global catalog and read-only domain partitions for all domains in the forest. Membership is controlled by the operating system.

  Attribute                              Value
  -------------------------------------- -----------------------------------
  Well-known SID/RID                     S-1-5-21-\<RootDomain\>-498
  Object class                           Group
  Default location in Active Directory   CN=Users, DC=\<forestRootDomain\>
  Default user rights                    None

[](#everyone)

### Everyone {#everyone .heading-anchor}

All interactive, network, dial-up, and authenticated users are members of the Everyone group. This special identity group gives wide access to system resources. When a user logs on to the network, the user is automatically added to the Everyone group. Membership is controlled by the operating system.

On computers running Windows 2000 and earlier, the Everyone group includes the Anonymous Logon group as a default member. Beginning in Windows Server 2003, the Everyone group contains only Authenticated Users and Guest. The group no longer includes Anonymous Logon by default. To change the Everyone group setting to include the Anonymous Logon group, in the Registry Editor, go to the **Computer\\HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Lsa** key and set the value of the **everyoneincludesanonymous** DWORD to **1**.

+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attribute                            | Value                                                                                                                                                       |
+======================================+=============================================================================================================================================================+
| Well-known SID/RID                   | S-1-1-0                                                                                                                                                     |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Object class                         | Foreign Security Principal                                                                                                                                  |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default location in Active Directory | CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>                                                                                 |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default user rights                  | [Access this computer from the network](/en-us/windows/device-security/security-policy-settings/access-this-computer-from-the-network): SeNetworkLogonRight |
|                                      |                                                                                                                                                             |
|                                      | [Bypass traverse checking](/en-us/windows/device-security/security-policy-settings/bypass-traverse-checking): SeChangeNotifyPrivilege                       |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[](#fresh-public-key-identity)

### Fresh Public Key identity {#fresh-public-key-identity .heading-anchor}

An SID that means the client\'s identity is asserted by an authentication authority based on proof of current possession of client public key credentials.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-18-3
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#interactive)

### Interactive {#interactive .heading-anchor}

Any user who is logged on to the local system has the Interactive identity. This identity allows only local users to access a resource. When a user accesses a specific resource on the computer to which they\'re currently logged on, the user is automatically added to the Interactive group. Membership is controlled by the operating system.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-5-4
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#iusr)

### IUSR {#iusr .heading-anchor}

Internet Information Services (IIS) uses this account by default when anonymous authentication is enabled.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-5-17
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#key-trust)

### Key trust {#key-trust .heading-anchor}

An SID that means the client\'s identity is based on proof of possession of public key credentials by using the key trust object.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-18-4
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#local-service)

### Local Service {#local-service .heading-anchor}

The Local Service account is similar to the Authenticated User account. Members of the Local Service account have the same level of access to resources and objects as members of the Users group. This limited access helps safeguard your system if individual services or processes are compromised. Services that run as the Local Service account access network resources as a null session with anonymous credentials. The name of the account is NT AUTHORITY\\LocalService. This account doesn\'t have a password.

+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attribute                            | Value                                                                                                                                                                  |
+======================================+========================================================================================================================================================================+
| Well-known SID/RID                   | S-1-5-19                                                                                                                                                               |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Object class                         | Foreign Security Principal                                                                                                                                             |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default location in Active Directory | CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>                                                                                            |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default user rights                  | [Adjust memory quotas for a process](/en-us/windows/device-security/security-policy-settings/adjust-memory-quotas-for-a-process): SeIncreaseQuotaPrivilege             |
|                                      |                                                                                                                                                                        |
|                                      | [Bypass traverse checking](/en-us/windows/device-security/security-policy-settings/bypass-traverse-checking): SeChangeNotifyPrivilege                                  |
|                                      |                                                                                                                                                                        |
|                                      | [Change the system time](/en-us/windows/device-security/security-policy-settings/change-the-system-time): SeSystemtimePrivilege                                        |
|                                      |                                                                                                                                                                        |
|                                      | [Change the time zone](/en-us/windows/device-security/security-policy-settings/change-the-time-zone): SeTimeZonePrivilege                                              |
|                                      |                                                                                                                                                                        |
|                                      | [Create global objects](/en-us/windows/device-security/security-policy-settings/create-global-objects): SeCreateGlobalPrivilege                                        |
|                                      |                                                                                                                                                                        |
|                                      | [Generate security audits](/en-us/windows/device-security/security-policy-settings/generate-security-audits): SeAuditPrivilege                                         |
|                                      |                                                                                                                                                                        |
|                                      | [Impersonate a client after authentication](/en-us/windows/device-security/security-policy-settings/impersonate-a-client-after-authentication): SeImpersonatePrivilege |
|                                      |                                                                                                                                                                        |
|                                      | [Replace a process level token](/en-us/windows/device-security/security-policy-settings/replace-a-process-level-token): SeAssignPrimaryTokenPrivilege                  |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[](#localsystem)

### LocalSystem {#localsystem .heading-anchor}

The LocalSystem account is a service account that\'s used by the operating system. The LocalSystem account is a powerful account that has full access to the system and acts as the computer on the network. If a service logs on to the LocalSystem account on a domain controller, that service has access to the entire domain. Some services are configured by default to log on to the LocalSystem account. Don\'t change the default service setting. The name of the account is LocalSystem. This account doesn\'t have a password.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-5-18
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#mfa-key-property)

### MFA key property {#mfa-key-property .heading-anchor}

An SID that means the key trust object had the multifactor authentication (MFA) property.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-18-5
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#network)

### Network {#network .heading-anchor}

This group implicitly includes all users who are logged on through a network connection. Any user who accesses the system through a network has the Network identity. This identity allows only remote users to access a resource. When a user accesses a specific resource over the network, the user is automatically added to the Network group. Membership is controlled by the operating system.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-5-2
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#network-service)

### Network Service {#network-service .heading-anchor}

The Network Service account is similar to the Authenticated User account. Members of the Network Service account have the same level of access to resources and objects as members of the Users group. This limited access helps safeguard your system if individual services or processes are compromised. Services that run as the Network Service account access network resources by using the credentials of the computer account. The name of the account is NT AUTHORITY\\NetworkService. This account doesn\'t have a password.

+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attribute                            | Value                                                                                                                                                                  |
+======================================+========================================================================================================================================================================+
| Well-known SID/RID                   | S-1-5-20                                                                                                                                                               |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Object class                         | Foreign Security Principal                                                                                                                                             |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default location in Active Directory | CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>                                                                                            |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default user rights                  | [Adjust memory quotas for a process](/en-us/windows/device-security/security-policy-settings/adjust-memory-quotas-for-a-process): SeIncreaseQuotaPrivilege             |
|                                      |                                                                                                                                                                        |
|                                      | [Bypass traverse checking](/en-us/windows/device-security/security-policy-settings/bypass-traverse-checking): SeChangeNotifyPrivilege                                  |
|                                      |                                                                                                                                                                        |
|                                      | [Create global objects](/en-us/windows/device-security/security-policy-settings/create-global-objects): SeCreateGlobalPrivilege                                        |
|                                      |                                                                                                                                                                        |
|                                      | [Generate security audits](/en-us/windows/device-security/security-policy-settings/generate-security-audits): SeAuditPrivilege                                         |
|                                      |                                                                                                                                                                        |
|                                      | [Impersonate a client after authentication](/en-us/windows/device-security/security-policy-settings/impersonate-a-client-after-authentication): SeImpersonatePrivilege |
|                                      |                                                                                                                                                                        |
|                                      | [Replace a process level token](/en-us/windows/device-security/security-policy-settings/replace-a-process-level-token): SeAssignPrimaryTokenPrivilege                  |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[](#ntlm-authentication)

### NTLM Authentication {#ntlm-authentication .heading-anchor}

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-5-64-10
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#other-organization)

### Other Organization {#other-organization .heading-anchor}

This group implicitly includes all users who are logged on to the system through a dial-up connection. Membership is controlled by the operating system.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-5-1000
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#owner-rights)

### Owner Rights {#owner-rights .heading-anchor}

The Owner Rights group represents the current owner of the object. When an ACE that carries this SID is applied to an object, the system ignores the implicit READ_CONTROL and WRITE_DAC permissions for the object owner.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-3-4
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#principal-self)

### Principal Self {#principal-self .heading-anchor}

This identity is a placeholder in an ACE on a user, group, or computer object in Active Directory. When you grant permissions to Principal Self, you grant permissions to the security principal that\'s represented by the object. During an access check, the operating system replaces the SID for Principal Self with the SID for the security principal that\'s represented by the object.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-5-10
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#proxy)

### Proxy {#proxy .heading-anchor}

Identifies a SECURITY_NT_AUTHORITY proxy.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-5-8
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#read-only-domain-controllers)

### Read-only Domain Controllers {#read-only-domain-controllers .heading-anchor}

This group includes all RODCs in the domain with read-only rights to the Active Directory database. Except for account passwords, a RODC holds all the Active Directory objects and attributes that a writable domain controller holds. It allows domain controller deployment when physical security is scarce or not guaranteed. RODCs are explicit members of this group.

  Attribute                              Value
  -------------------------------------- -----------------------------
  Well-known SID/RID                     S-1-5-21-\<domain\>-521
  Object class                           Group
  Default location in Active Directory   CN=Users, DC=\<rootDomain\>
  Default user rights                    None

Note

The [Denied RODC Password Replication group](understand-security-groups#denied-rodc-password-replication) is created automatically when an RODC account is created in the forest. Passwords can\'t be replicated in the Denied RODC Password Replication group.

[](#remote-interactive-logon)

### Remote Interactive Logon {#remote-interactive-logon .heading-anchor}

This identity represents all users who are currently logged on to a computer by using a Remote Desktop Protocol connection. This group is a subset of the Interactive group. Access tokens that contain the Remote Interactive Logon SID also contain the Interactive SID.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-5-14
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#restricted)

### Restricted {#restricted .heading-anchor}

Users and computers with restricted capabilities have the Restricted identity. This identity group is used by a process that\'s running in a restricted security context, such as when you run an application with the RunAs service. When code runs at the Restricted security level, the Restricted SID is added to the user's access token.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-5-12
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#schannel-authentication)

### SChannel Authentication {#schannel-authentication .heading-anchor}

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-5-64-14
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#service)

### Service {#service .heading-anchor}

Any service that accesses the system has the Service identity. This identity group includes all security principals that are signed in as a service. This identity grants access to processes that Windows Server services are running. Membership is controlled by the operating system.

+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attribute                            | Value                                                                                                                                                                  |
+======================================+========================================================================================================================================================================+
| Well-known SID/RID                   | S-1-5-6                                                                                                                                                                |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Object class                         | Foreign Security Principal                                                                                                                                             |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default location in Active Directory | CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>                                                                                            |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default user rights                  | [Create global objects](/en-us/windows/device-security/security-policy-settings/create-global-objects): SeCreateGlobalPrivilege                                        |
|                                      |                                                                                                                                                                        |
|                                      | [Impersonate a client after authentication](/en-us/windows/device-security/security-policy-settings/impersonate-a-client-after-authentication): SeImpersonatePrivilege |
+--------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[](#service-asserted-identity)

### Service asserted identity {#service-asserted-identity .heading-anchor}

An SID that means the client\'s identity is asserted by a service.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-18-2
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#terminal-server-user)

### Terminal Server User {#terminal-server-user .heading-anchor}

Any user that\'s accessing the system through Terminal Services has the Terminal Server User identity. This identity allows users to access Terminal Server applications and to do other necessary tasks with Terminal Server services. Membership is controlled by the operating system.

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-5-13
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#this-organization)

### This Organization {#this-organization .heading-anchor}

  Attribute                              Value
  -------------------------------------- -----------------------------------------------------------------------------
  Well-known SID/RID                     S-1-5-15
  Object class                           Foreign Security Principal
  Default location in Active Directory   CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>
  Default user rights                    None

[](#window-managerwindow-manager-group)

### Window Manager\\Window Manager Group {#window-managerwindow-manager-group .heading-anchor}

+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attribute                            | Value                                                                                                                                                   |
+======================================+=========================================================================================================================================================+
| Well-known SID/RID                   | S-1-5-90                                                                                                                                                |
+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Object class                         | Foreign Security Principal                                                                                                                              |
+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default location in Active Directory | CN=WellKnown Security Principals, CN=Configuration, DC=\<forestRootDomain\>                                                                             |
+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default user rights                  | [Bypass traverse checking](/en-us/windows/device-security/security-policy-settings/bypass-traverse-checking): SeChangeNotifyPrivilege                   |
|                                      |                                                                                                                                                         |
|                                      | [Increase a process working set](/en-us/windows/device-security/security-policy-settings/increase-a-process-working-set): SeIncreaseWorkingSetPrivilege |
+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[](#related-content)

## Related content {#related-content .heading-anchor}

-   [Active Directory security groups](understand-security-groups)

-   [Security principals](understand-security-principals)

-   [Access control overview](/en-us/windows/security/identity-protection/access-control/access-control)

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

-   [Active Directory Security Groups](/en-us/windows-server/identity/ad-ds/manage/understand-security-groups?source=recommendations)

    Become familiar with Windows Server Active Directory security groups, group scope, and group functions. See information on groups, such as members and rights.

-   [Add special groups to built-in groups - Windows Server](/en-us/troubleshoot/windows-server/active-directory/add-special-groups-to-built-in-groups?source=recommendations)

    Describes how to add special groups to built-in groups.

-   [Security Identifiers](/en-us/windows-server/identity/ad-ds/manage/understand-security-identifiers?source=recommendations)

    Become familiar with unique identifiers for Windows Server accounts and groups, such as security identifiers (SIDs). See tables of well-known SIDs.

-   [Security Principals](/en-us/windows-server/identity/ad-ds/manage/understand-security-principals?source=recommendations)

    This article discusses security principals for Windows Server accounts and security groups and how they work in Active Directory.

-   [\[MS-ADTS\]: Enterprise Domain Controllers](/en-us/openspecs/windows_protocols/ms-adts/9ec0405f-bab3-4a35-899f-a08ac734f2b7?source=recommendations)

    name: Enterprise Domain Controllers parent: WellKnown Security Principals objectSid: S-1-5-9 By default all normal

-   [Back Up and Restore Group Policy in Windows](/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-backup-restore?source=recommendations)

    Learn how to back up, restore, migrate, and copy Group Policy Objects by using the Group Policy Management Console in Windows.

Training

Module

[Secure Windows Server user accounts - Training](/en-us/training/modules/secure-windows-server-user-accounts/?source=recommendations)

Learn how to secure Active Directory user accounts using least privilege, Protected Users group, authentication policy silos, Windows Defender Credential Guard, NTLM blocking, and account remediation techniques.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 07/08/2025
