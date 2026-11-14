---
{"title": "Active Directory Forest Recovery - Back up the System State data", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-backing-up-system-state", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Back up the System State data

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

Use the following procedure to perform a system state backup on a Domain Controller (DC) by using Windows Server Backup or wbadmin.exe.

[](#perform-a-system-state-backup-using-windows-server-backup)

## Perform a system state backup using Windows Server Backup {#perform-a-system-state-backup-using-windows-server-backup .heading-anchor}

1.  Open **Server Manager**, select **Tools**, and then select **Windows Server Backup**.
    -   In Windows Server 2008 R2 and Windows Server 2008, select **Start**, point to **Administrative Tools**, and then select **Windows Server Backup**.
2.  If you\'re prompted, in the **User Account Control** dialog box, provide Backup Operator credentials, and then select **OK**.
3.  Select **Local Backup**.
4.  On the **Action** menu, select **Backup once**.
5.  In the Backup Once Wizard, on the **Backup options** page, select **Different options**, and then select **Next**.
6.  On the **Select backup configuration** page, select **Custom**, and then select **Next**.
7.  On the **Select Items for Backup** screen, select **Add Items** and select **System State** and select **Ok**.
    -   In Windows Server 2008 R2 and Windows Server 2008, select the volumes to include in the backup. If you select the **Enable system recovery** check box, all critical volumes are selected.
8.  On the **Specify destination type** page, select **Local drives** or **Remote shared folder**, and then select **Next**. If you\'re backing up to a remote shared folder, do the following:
    -   Type the path to the shared folder.
    -   Under **Access Control**, select **Do not inherit** or **Inherit** to determine access to the backup, and then select **Next**.
    -   In the **Provide user credentials for Backup** dialog box, provide the user name and password for a user who has write access to the shared folder, and then select **OK**.
9.  For Windows Server 2008 R2 and Windows Server 2008, on the **Specify advanced option** page, select **VSS copy backup** and then select **Next**.
10. On the **Select Backup Destination** page, choose the backup location. If you selected local drive choose a local drive or if you selected remote share choose a network share.
11. On the confirmation screen, select **Backup**.
12. Once this has completed select **Close**.
13. Close Windows Server Backup.

[](#perform-a-system-state-backup-using-wbadminexe)

## Perform a system state backup using Wbadmin.exe {#perform-a-system-state-backup-using-wbadminexe .heading-anchor}

Open an elevated command prompt, type the following command and press ENTER:

cli

``` {.inner-focus data-language="cli"}
wbadmin start systemstatebackup -backuptarget:<targetDrive>:
```

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

-   [AD Forest Recovery - Backing up a full server](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-backing-up-a-full-server?source=recommendations)

    A Bare Metal Recovery (BMR) backup is recommended to prepare for a forest recovery because it can be restored to different hardware or a different operating system instance. Using Windows Server Backup you can perform a Bare-Metal Recovery (BMR) backup of your server.

-   [Active Directory Forest Recovery - Prerequisites](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-prerequisites?source=recommendations)

    The following document discusses prerequisites that you should be familiar with before devising a forest recovery plan or attempting a recovery.

-   [Active Directory Forest Recovery - Perform initial recovery](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-initial-recovery?source=recommendations)

    Beginning with a writeable DC in the forest root domain, complete the steps in this section in order to restore the first DC.

-   [AD Forest Recovery - Devising an AD Forest Recovery Plan](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-devise-a-plan?source=recommendations)

    Learn more about: AD Forest Recovery - Devising an AD Forest Recovery Plan

-   [AD Forest Recovery - Configure DNS Server service](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-configure-dns?source=recommendations)

    Learn more about: AD Forest Recovery - Configuring the DNS Server service

-   [Active Directory Forest Recovery - Determine how to recover the forest](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-determine-how-to-recover?source=recommendations)

    Recovering an entire Active Directory forest involves restoring at least one Domain Controller (DC) in every domain from available backup. Recovering the forest restores each domain in the forest to its state at the time of the last trusted backup. Consequently, the restore operation will result in the loss of at least the following Active Directory data\...

-   [Active Directory Forest Recovery - Recovering a single domain in a multidomain forest](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-recover-single-domain-multidomain-forest?source=recommendations)

    In certain scenarios, it may be necessary to recover only a single domain within a forest that has multiple domains, rather than a full forest recovery. This topic covers considerations for recovering a single domain and possible strategies for recovery.

-   [Active Directory Forest Recovery - Procedures](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-procedures?source=recommendations)

    View a list of procedures that are used in backing up and restoring domain controllers and Active Directory.

Training

Module

[Troubleshoot Active Directory - Training](/en-us/training/modules/troubleshoot-active-directory/?source=recommendations)

Learn how to troubleshoot Active Directory including recovering deleted objects with AD Recycle Bin, managing the AD DS database with NtdsUtil, restoring SYSVOL, troubleshooting replication, and diagnosing hybrid authentication with Microsoft Entra Connect.

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 05/12/2025
