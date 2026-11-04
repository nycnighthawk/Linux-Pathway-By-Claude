---
{"title": "Enable and use Active Directory Recycle Bin", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/active-directory-recycle-bin", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Enable and use Active Directory Recycle Bin

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Active Directory Recycle Bin allows you to preserve and recover accidentally deleted Active Directory objects. When you enable Active Directory Recycle Bin, all link-valued and non-link-valued attributes of the deleted Active Directory objects are preserved. Meaning objects can be restored in their entirety to the same consistent logical state that they were in immediately before deletion. For example, restored user accounts automatically regain all group memberships and corresponding access rights that they had immediately before deletion, within and across domains.

Important

Active Directory Recycle Bin isn\'t enabled by default. The process of enabling Active Directory Recycle Bin is irreversible. After you enable Active Directory Recycle Bin in your environment, you can\'t disable it.

[](#prerequisites)

## Prerequisites {#prerequisites .heading-anchor}

Before you can enable Active Directory Recycle Bin, you need to complete the following prerequisites.

-   The forest and domain functional level must be Windows Server 2008 R2 or higher.

-   You must be a member of the Domain Admins group in the domain you want to enable Active Directory Recycle Bin.

-   You must have either of the following Remote Server Administration Tools (RSAT) installed:

    -   Active Directory Administrative Center (ADAC)
    -   Active Directory module for Windows PowerShell.

[](#enable-active-directory-recycle-bin)

## Enable Active Directory Recycle Bin {#enable-active-directory-recycle-bin .heading-anchor}

To enable Active Directory Recycle Bin, perform the following steps:

-   [Active Directory Administrative Center](#tabpanel_1_adac)
-   [PowerShell](#tabpanel_1_powershell)

Here\'s how to enable Active Directory Recycle Bin using Active Directory Administrative Center (ADAC):

1.  Sign into a computer that has the Active Directory module for Windows PowerShell installed.

2.  Open Active Directory Administrative Center, either from the Tools menu of the Server Manager console or by running an elevated PowerShell session and typing **dsac.exe**.

3.  If the appropriate target domain isn\'t selected, choose **Manage**, choose **Add Navigation Nodes**, and select the appropriate target domain in the **Add Navigation Nodes** dialog box and then choose **OK**.

4.  In the **Tasks** pane, choose **Enable Recycle Bin** in the **Tasks** pane, choose **OK** on the warning message box, and then choose **OK** to the refresh ADAC message.

5.  To refresh ADAC, press F5 or select the refresh icon.

If you encounter an error, you can try moving both the schema master and the domain naming master roles to the same domain controller in the root domain. Then run the cmdlet from that domain controller.

[](#restore-deleted-objects)

## Restore deleted objects {#restore-deleted-objects .heading-anchor}

Perform perform the following steps to restore deleted objects using Active Directory Administrative Center.

Tip

You can only restore AD DS items that were deleted after Active Directory Recycle Bin is enabled. You can\'t use Active Directory Recycle Bin to recover items that were deleted before enabling this functionality.

-   [Active Directory Administrative Center](#tabpanel_2_adac)
-   [PowerShell](#tabpanel_2_powershell)

Here\'s how to restore deleted objects using Active Directory Administrative Center:

1.  Open Active Directory Administrative Center, either from the Tools menu of the Server Manager console or by running an elevated PowerShell session and typing **dsac.exe**.

2.  choose **Manage**, choose **Add Navigation Nodes**, and select the appropriate target domain in the **Add Navigation Nodes** dialog box and then choose **OK**.

3.  Navigate to the **Deleted Objects** container.

4.  Select the users you wish to restore and then choose either **Restore** in the **Tasks** pane, or **Restore To** in the **Tasks** pane and specify the location to which you wish to restore the deleted objects.

5.  To confirm the objects were restored to their original location, navigate to the target domain and verify the user accounts are listed.

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

-   [Restore user accounts and groups in AD - Windows Server](/en-us/troubleshoot/windows-server/active-directory/retore-deleted-accounts-and-groups-in-ad?source=recommendations)

    Discusses how to recover from the accidental deletion of users and their group memberships in Active Directory.

-   [Diagnose AD replication failures - Windows Server](/en-us/troubleshoot/windows-server/active-directory/diagnose-replication-failures?source=recommendations)

    Describes how to diagnose Active Directory replication failures.

-   [Demote Domain Controllers and Domains](/en-us/windows-server/identity/ad-ds/deploy/demoting-domain-controllers-and-domains--level-200-?source=recommendations)

    Learn how to demote domain controllers and domains using Server Manager or PowerShell in Windows Server.

Training

Module

[Troubleshoot Active Directory - Training](/en-us/training/modules/troubleshoot-active-directory/?source=recommendations)

Learn how to troubleshoot Active Directory including recovering deleted objects with AD Recycle Bin, managing the AD DS database with NtdsUtil, restoring SYSVOL, troubleshooting replication, and diagnosing hybrid authentication with Microsoft Entra Connect.

Certification

[Microsoft Certified: Identity and Access Administrator Associate - Certifications](/en-us/credentials/certifications/identity-and-access-administrator/?source=recommendations)

Demonstrate the features of Microsoft Entra ID to modernize identity solutions, implement hybrid solutions, and implement identity governance.

------------------------------------------------------------------------

-    Last updated on 06/06/2025
