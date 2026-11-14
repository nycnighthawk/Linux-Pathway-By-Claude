---
{"title": "Appendix C: Protected Accounts and Groups in Active Directory", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-c--protected-accounts-and-groups-in-active-directory", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Appendix C: Protected Accounts and Groups in Active Directory

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

[](#appendix-c-protected-accounts-and-groups-in-active-directory-1)

## Appendix C: Protected Accounts and Groups in Active Directory {#appendix-c-protected-accounts-and-groups-in-active-directory-1 .heading-anchor}

Within Active Directory, a default set of highly privileged accounts and groups are considered protected accounts and groups. With most objects in Active Directory, users delegated permissions to manage Active Directory objects can change permissions on the objects, including altering permissions to allow themselves to modify membership of special groups.

Protected accounts and groups are special objects where permissions are set and enforced via an automatic process that ensures the permissions on the objects remain consistent. These permissions remain even if you move the objects to different locations in Active Directory. If a protected object\'s permissions are modified, existing processes ensure that permissions are returned to their defaults quickly.

[](#protected-groups)

### Protected Groups {#protected-groups .heading-anchor}

The following security accounts and groups are protected in Active Directory Domain Services:

-   Account Operators
-   Administrator
-   Administrators
-   Backup Operators
-   Domain Admins
-   Domain Controllers
-   Enterprise Admins
-   Enterprise Key Admins
-   Key Admins
-   Krbtgt
-   Print Operators
-   Read-only Domain Controllers
-   Replicator
-   Schema Admins
-   Server Operators

[](#adminsdholder)

#### AdminSDHolder {#adminsdholder .heading-anchor}

The purpose of the AdminSDHolder object is to provide \"template\" permissions for the protected accounts and groups in the domain. AdminSDHolder is automatically created as an object in the System container of every Active Directory domain. Its path is: **CN=AdminSDHolder,CN=System,DC=\<domain_component\>,DC=\<domain_component\>?.**

While the Administrators group owns most objects in an Active Directory domain, the Domain Admins group owns the AdminSDHolder object. By default, Enterprise Admins can make changes to any domain\'s AdminSDHolder object, as can the domain\'s Domain Admins and Administrators groups. Additionally, although the default owner of AdminSDHolder is the domain\'s Domain Admins group, members of Administrators or Enterprise Admins can take ownership of the object.

[](#sdprop)

#### SDProp {#sdprop .heading-anchor}

SDProp is a process that runs every 60 minutes (by default) on the domain controller that holds the domain\'s PDC Emulator (PDCE). SDProp compares the permissions on the domain\'s AdminSDHolder object with the permissions on the protected accounts and groups in the domain. If the permissions on any of the protected accounts and groups do not match the permissions on the AdminSDHolder object, SDProp resets the permissions on the protected accounts and groups to match those configured for the domain\'s AdminSDHolder object.

Permissions inheritance is disabled on protected groups and accounts. Even if the accounts and groups are moved to different locations in the directory, they will not inherit permissions from their new parent objects. Inheritance is disabled on the AdminSDHolder object so that permission changes to the parent objects do not change the permissions of AdminSDHolder.

[](#changing-sdprop-interval)

##### Changing SDProp Interval {#changing-sdprop-interval .heading-anchor}

Normally, you should not need to change the interval at which SDProp runs, except for testing purposes. If you need to change the SDProp interval, on the PDCE for the domain, use regedit to add or modify the AdminSDProtectFrequency DWORD value in HKLM\\SYSTEM\\CurrentControlSet\\Services\\NTDS\\Parameters.

The range of values is in seconds from 60 to 7200 (one minute to two hours). To remove changes, delete AdminSDProtectFrequency key. Deleting the key causes SDProp to revert back to the 60 minute interval. You generally should not reduce this interval in production domains as it can increase LSASS processing overhead on the domain controller. The impact of this increase is dependent on the number of protected objects in the domain.

[](#running-sdprop-manually)

##### Running SDProp Manually {#running-sdprop-manually .heading-anchor}

A better approach to testing AdminSDHolder changes is to run SDProp manually, which causes the task to run immediately but does not affect scheduled execution. You can force SDProp to run by using Ldp.exe or by running an LDAP modification script. To run SDProp manually, perform the following steps:

1.  Launch **Ldp.exe**.

2.  In the **Ldp** dialog box, click **Connection**, and click **Connect**.

3.  In the **Connect** dialog box, type the name of the domain controller for the domain that holds the PDC Emulator (PDCE) role and click **OK**.

4.  To verify the connection, check that **Dn: (RootDSE)** is present similar to the following screenshot. Next click **Connection** and click **Bind**.

5.  In the **Bind** dialog box, type the credentials of a user account that has permission to modify the rootDSE object. (If you are logged on as that user, you can select **Bind as currently logged on user**.) Click **OK**.

6.  Once the bind operation completes, click **Browse**, and click **Modify**.

7.  In the **Modify** dialog box, leave the **DN** field blank. In the **Edit Entry Attribute** field, type **RunProtectAdminGroupsTask**, and in the **Values** field, type **1**. Click **Enter** to populate the entry list as shown here.

8.  In the populated **Modify** dialog box, click **Run**, and verify that the changes you made to the AdminSDHolder object have appeared on that object.

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

-   [Active Directory Privileged Accounts and Groups Guide](/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory?source=recommendations)

    Discover Active Directory privileged accounts and groups including Enterprise Admins, Domain Admins, and built-in security groups. Learn rights, permissions, and security best practices for AD administration.

-   [Appendix E - Securing Enterprise Admins Groups in Active Directory](/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-e--securing-enterprise-admins-groups-in-active-directory?source=recommendations)

    Learn more about: Appendix E: Securing Enterprise Admins Groups in Active Directory

-   [\[MS-ADTS\]: AdminSDHolder](/en-us/openspecs/windows_protocols/ms-adts/dd3d29f3-8e1e-4e8c-a210-9eaef3abd628?source=recommendations)

    References Special Objects in section 6.1: Windows NT operating system Glossary terms: Active Directory, security

-   [Appendix D - Securing Built-In Administrator Accounts in Active Directory](/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-d--securing-built-in-administrator-accounts-in-active-directory?source=recommendations)

    Learn more about: Appendix D: Securing Built-In Administrator Accounts in Active Directory

-   [Appendix F - Securing Domain Admins Groups in Active Directory](/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-f--securing-domain-admins-groups-in-active-directory?source=recommendations)

    Learn more about: Appendix F: Securing Domain Admins Groups in Active Directory

-   [How to Configure Protected Accounts](/en-us/windows-server/security/windows-authentication/how-to-configure-protected-accounts?source=recommendations)

    Learn more about: How to Configure Protected Accounts

-   [Protected Users Security Group in Windows Server](/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group?source=recommendations)

    Learn about the Active Directory security group Protected Users feature and how it works in Windows Server.

-   [Reducing the Active Directory Attack Surface](/en-us/windows-server/identity/ad-ds/plan/security-best-practices/reducing-the-active-directory-attack-surface?source=recommendations)

    Learn more about: Reducing the Active Directory Attack Surface

Training

Module

[Secure Windows Server user accounts - Training](/en-us/training/modules/secure-windows-server-user-accounts/?source=recommendations)

Learn how to secure Active Directory user accounts using least privilege, Protected Users group, authentication policy silos, Windows Defender Credential Guard, NTLM blocking, and account remediation techniques.

Certification

[Microsoft Certified: Information Security Administrator Associate - Certifications](/en-us/credentials/certifications/information-security-administrator/?source=recommendations)

As an Information Security Administrator, you plan and implement information security of sensitive data by using Microsoft Purview and related services.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
