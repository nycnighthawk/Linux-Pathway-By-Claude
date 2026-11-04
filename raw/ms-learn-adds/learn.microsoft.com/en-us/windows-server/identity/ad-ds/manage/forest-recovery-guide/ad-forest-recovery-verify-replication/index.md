---
{"title": "Active Directory Forest Recovery - Verify Replication", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-verify-replication", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Verify Replication

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

After you\'ve restored or reinstalled all domain controllers (DCs), you can verify that AD DS, and the sysvol folder has recovered and is replicating correctly by using `repadmin /replsum`. `repadmin /replsum` runs on any version of Windows Server.

Check the DFS Replication event logs for Event ID 4602 (or File Replication Service event ID 13516). This log event indicates sysvol replication has been initialized.

If the first recovered DC has Event ID 4614 in the DFS Replication log ("the domain controller is waiting to perform initial replication\"), the replicated folder remains in the initial synchronization state until it has replicated with its partner. If Event ID 4602 doesn\'t appear, you need to perform the following manual steps to recover the sysvol folder if it\'s replicated using DFSR.

1.  If DFSR Event 4612 appears on the first restored DC, perform a manual authoritative restore as described in [2218556: How to force authoritative and nonauthoritative synchronization for DFSR-replicated sysvol replication)](https://support.microsoft.com/kb/2218556).
2.  Set **SysvolReady Flag** to 1 manually, as described in [947022 The NETLOGON share isn\'t present after you install Active Directory Domain Services on a new full or read-only Windows Server 2008-based domain controller](https://support.microsoft.com/kb/947022).

You can also create a diagnostic report DFS Replication. For more information, see [Create a Diagnostic Report for DFS Replication](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754227(v=ws.11)) and [DFS Step-by-Step Guide for Windows Server 2008](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754227(v=ws.11)). If the server is running Windows Server 2008 R2, you can use [dfsrdiag.exe ReplicationState command line switch](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754227(v=ws.11)).

You can also run the Replications test using dcdiag.exe to check for replication errors. For more information, see Knowledge Base [Active Directory replication error 8452 - Windows Server](/en-us/troubleshoot/windows-server/identity/replication-error-8452).

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

-   [Force synchronization for Distributed File System Replication (DFSR) replicated sysvol replication - Windows Server](/en-us/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization?source=recommendations)

    Describes how to restart DFSR on a server, either authoritatively or non-authoritative.

-   [Troubleshoot missing SYSVOL and Netlogon shares for Distributed File System (DFS) Replication - Windows Server](/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares?source=recommendations)

    Describes how to troubleshoot SYSVOL and Netlogon shares that are missing.

-   [AD Replication error 1908 - Windows Server](/en-us/troubleshoot/windows-server/active-directory/ad-replication-error-1908-not-find-domain-controller?source=recommendations)

    Provides a resolution for troubleshooting AD Replication error 1908, which is Could not find the domain controller for this domain.

-   [Distributed File System Replication (DFSR) SYSVOL fails to migrate or replicate - Windows Server](/en-us/troubleshoot/windows-server/group-policy/dfsr-sysvol-fails-migrate-replicate?source=recommendations)

    Provides a solution to issues where DFSR SYSVOL fails to migrate or replicate, or SYSVOL isn\'t shared.

-   [SYSVOL DFSR migration fails after you in-place upgrade DC - Windows Server](/en-us/troubleshoot/windows-server/networking/sysvol-dfsr-migration-fails-after-in-place-upgrade?source=recommendations)

    Address an issue in which SYSVOL DFSR migration fails after you in-place upgrade a domain controller to Windows Server 2019.

-   [Errors when you run DCDIAG commands - Windows Server](/en-us/troubleshoot/windows-server/active-directory/dcdiag-commands-running-errors?source=recommendations)

    Fixes errors that occur when you run DCDIAG.EXE /E or /A or /C commands.

-   [AD Forest Recovery - Performing an authoritative synchronization of DFSR-replicated SYSVOL](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-authoritative-recovery-sysvol?source=recommendations)

    There are different ways to perform an authoritative restore of SYSVOL. You can either edit the \*\*msDFSR-Options\*\* attribute or perform a system state restore using wbadmin --authsysvol. If you have the option to restore a system state backup (that is, you\'re restoring AD DS to the same hardware and operating system instance) then using wbadmin --authsysvol is simpler. But if you need to perform a bare metal restore, then you need to edit the \*\*msDFSR-Options\*\* attribute.

-   [The NETLOGON share is not present after you install Active Directory Domain Services on a new full or read-only Windows Server 2008-based domain controller - Windows Server](/en-us/troubleshoot/windows-server/active-directory/netlogon-share-not-present-after-install-ad-ds-on-full-read-only-domain-controller?source=recommendations)

    This article contains a workaround for a problem that occurs after you install AD DS on a new full or read-only Windows Server 2008-based domain controller.

Training

Module

[Troubleshoot Active Directory - Training](/en-us/training/modules/troubleshoot-active-directory/?source=recommendations)

Learn how to troubleshoot Active Directory including recovering deleted objects with AD Recycle Bin, managing the AD DS database with NtdsUtil, restoring SYSVOL, troubleshooting replication, and diagnosing hybrid authentication with Microsoft Entra Connect.

------------------------------------------------------------------------

-    Last updated on 09/25/2025
