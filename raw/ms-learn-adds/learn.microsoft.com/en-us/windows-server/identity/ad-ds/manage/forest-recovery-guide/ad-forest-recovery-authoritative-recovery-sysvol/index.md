---
{"title": "Active Directory Forest Recovery - Perform an authoritative synchronization of DFSR-replicated SYSVOL", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-authoritative-recovery-sysvol", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Perform an authoritative synchronization of DFSR-replicated SYSVOL

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

There are different ways to perform an authoritative restore of SYSVOL. You can either edit the **msDFSR-Options** attribute or perform a system state restore using wbadmin --authsysvol. If you have the option to restore a system state backup (that is, you\'re restoring AD DS to the same hardware and operating system instance) then using wbadmin --authsysvol is simpler. But if you need to perform a bare metal restore, then you need to edit the **msDFSR-Options** attribute.

Use the following steps to perform an authoritative synchronization of SYSVOL (if it\'s replicated using DFSR) by editing the **msDFSR-Options** attribute. Note it can also be done using PowerShell.

**To perform an authoritative synchronization of DFSR-replicated SYSVOL using Active Directory Users and Computers**

1.  Open Active Directory Users and Computers.

2.  Select **View**, and then select **Users, Contacts, Groups, and Computers as containers** and **Advanced Features**.

3.  In the tree-view, select **Domain Controllers**, the name of the DC you restored, **DFSR-LocalSettings**, and then **Domain System Volume**.

4.  In the Details pane, right-click **SYSVOL Subscription**, select **Properties**, and select **Attribute Editor**.

5.  Select **msDFSR-Options**, select **Edit**, type **1**, and select **OK**.

6.  Select **OK** to close the Attribute Editor.

[](#verify-if-the-authoritative-restore-is-successful-using-powershell)

## Verify if the authoritative restore is successful using PowerShell {#verify-if-the-authoritative-restore-is-successful-using-powershell .heading-anchor}

1.  After the previous operation, restart the DFSR service:

    **Restart-Service DFSR -PassThru**

2.  Verify the presence if Event ID 4602

    **Get-WinEvent -LogName \'DFS Replication\' \| Where-Object ID -EQ 4602 \| Format-Table -AutoSize -Wrap**

[](#next-steps)

## Next steps {#next-steps .heading-anchor}

-   [AD Forest Recovery - Prerequisites](ad-forest-recovery-prerequisites)
-   [AD Forest Recovery - Devise a custom forest recovery plan](ad-forest-recovery-devise-a-plan)
-   [AD Forest Recovery - Steps to restore the forest](ad-forest-recovery-steps-for-restoring-the-forest)
-   [AD Forest Recovery - Identify the problem](ad-forest-recovery-identify-the-problem)
-   [AD Forest Recovery - Determine how to recover](ad-forest-recovery-determine-how-to-recover)
-   [AD Forest Recovery - Perform initial recovery](ad-forest-recovery-perform-initial-recovery)
-   [AD Forest Recovery - Procedures](ad-forest-recovery-procedures)
-   [AD Forest Recovery - Frequently Asked Questions (FAQ)](ad-forest-recovery-faq)
-   [AD Forest Recovery - Recover a single domain within a multidomain forest](ad-forest-recovery-recover-single-domain-multidomain-forest)
-   [AD Forest Recovery - Redeploy remaining DCs](ad-forest-recovery-restore-additional-dcs)
-   [AD Forest Recovery - Virtualization](ad-forest-recovery-virtualization)
-   [AD Forest Recovery - Cleanup](ad-forest-recovery-cleanup)

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

-   [Active Directory Forest Recovery - Performing a nonauthoritative restore of Active Directory Domain Services](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-nonauthoritative-restore?source=recommendations)

    The following procedures use the wbadmin.exe to perform a nonauthoritative restore of Active Directory or Active Directory Domain Services (AD DS). If you\'re using a different backup solution or if you intend to complete the authoritative restore of SYSVOL later in the forest recovery process\...

-   [Force synchronization for Distributed File System Replication (DFSR) replicated sysvol replication - Windows Server](/en-us/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization?source=recommendations)

    Describes how to restart DFSR on a server, either authoritatively or non-authoritative.

-   [How to rebuild the SYSVOL tree and its content in a domain - Windows Server](/en-us/troubleshoot/windows-server/group-policy/rebuild-sysvol-tree-and-content-in-a-domain?source=recommendations)

    Describes how to use the Burflags registry value to rebuild each domain controller\'s copy of the system volume tree (SYSVOL) on all domain controllers in a common Active Directory domain.

-   [AD Forest Recovery - Configure DNS Server service](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-configure-dns?source=recommendations)

    Learn more about: AD Forest Recovery - Configuring the DNS Server service

-   [Distributed File System Replication (DFSR) SYSVOL fails to migrate or replicate - Windows Server](/en-us/troubleshoot/windows-server/group-policy/dfsr-sysvol-fails-migrate-replicate?source=recommendations)

    Provides a solution to issues where DFSR SYSVOL fails to migrate or replicate, or SYSVOL isn\'t shared.

-   [Backing Up and Restoring an FRS-Replicated SYSVOL Folder - Win32 apps](/en-us/windows/win32/vss/backing-up-and-restoring-an-frs-replicated-sysvol-folder?source=recommendations)

    This topic explains how to determine whether a SYSVOL folder is replicated by DFSR or FSR and explains how to backup and restore an FRS-replicated SYSVOL folder.

-   [Troubleshoot missing SYSVOL and Netlogon shares for Distributed File System (DFS) Replication - Windows Server](/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares?source=recommendations)

    Describes how to troubleshoot SYSVOL and Netlogon shares that are missing.

-   [The NETLOGON share is not present after you install Active Directory Domain Services on a new full or read-only Windows Server 2008-based domain controller - Windows Server](/en-us/troubleshoot/windows-server/active-directory/netlogon-share-not-present-after-install-ad-ds-on-full-read-only-domain-controller?source=recommendations)

    This article contains a workaround for a problem that occurs after you install AD DS on a new full or read-only Windows Server 2008-based domain controller.

Training

Module

[Troubleshoot Active Directory - Training](/en-us/training/modules/troubleshoot-active-directory/?source=recommendations)

Learn how to troubleshoot Active Directory including recovering deleted objects with AD Recycle Bin, managing the AD DS database with NtdsUtil, restoring SYSVOL, troubleshooting replication, and diagnosing hybrid authentication with Microsoft Entra Connect.

------------------------------------------------------------------------

-    Last updated on 11/01/2024
