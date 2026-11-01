---
{"title": "Active Directory Forest Recovery - Back up a full server", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-backing-up-a-full-server", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Back up a full server

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

A Bare Metal Recovery (BMR) backup is recommended to prepare for a forest recovery because it can be restored to different hardware or a different operating system instance. Using Windows Server Backup you can perform a Bare-Metal Recovery (BMR) backup of your server.

[](#windows-server-backup)

## Windows Server Backup {#windows-server-backup .heading-anchor}

Windows Server Backup isn\'t installed by default. In Windows Server 2012 R2, Windows Server 2016 and newer, install it by following the steps below.

Note

Please be aware that the steps may vary slightly between Windows Server 2012 R2 and Windows Server 2016+.

[](#install-windows-server-backup)

## Install Windows Server Backup {#install-windows-server-backup .heading-anchor}

1.  Open **Server Manager** and select **Add roles and features**.
2.  On the **Add Roles and Features Wizard** select **Next**.
3.  On the **Installation Type** screen, leave the default **Role-based or feature-based installation** and select **Next**.
4.  On the **Server Selection** screen, select **Next**.
5.  On the Server Roles screen, select **Next**.
6.  On the **Features** screen, select **Windows Server Backup** and select **Next**
7.  Select **Install**.
8.  Once the installation is complete, select **Close**.

[](#perform-a-backup-with-windows-server-backup)

## Perform a backup with Windows Server Backup {#perform-a-backup-with-windows-server-backup .heading-anchor}

1.  Open **Server Manager**, select **Tools**, and then select **Windows Server Backup**.
2.  If you\'re prompted, in the **User Account Control** dialog box, provide Backup Operator credentials, and then select **OK**.
3.  Select **Local Backup**.
4.  On the **Action** menu, select **Backup once**.
5.  In the Backup Once Wizard, on the **Backup options** page, select **Different options**, and then select **Next**.
6.  On the **Select backup configuration** page, select **Full server (recommended)**, and then select **Next**. Or when you select "Custom", make sure to select "Bare metal recovery" and the items is selected automatically:\
7.  On the **Specify destination type** page, select **Local drives** or **Remote shared folder**, and then select **Next**.
8.  On the **Select Backup Destination** page, choose the backup location. If you selected local drive choose a local drive or if you selected remote share choose a network share.
9.  On the confirmation screen, select **Backup**.
10. Once this has completed select **Close**.
11. Close Windows Server Backup.

Note

If you get an error stating that no backup storage location is available, you will need to either exclude one of the volumes that has been selected or add a new volume or remote share. If you get a warning stating that the selected volume is also included in the list of items to backup, determine whether or not to remove and click **OK**.

[](#use-wbadminexe-to-back-up-a-windows-server)

## Use `wbadmin.exe` to back up a Windows Server {#use-wbadminexe-to-back-up-a-windows-server .heading-anchor}

`Wbadmin.exe` is a command-line utility that enables you to back up and restore your operating system, volumes, files, folders, and applications from a command prompt.

[](#perform-a-full-server-backup-using-wbadminexe)

## Perform a full server backup using `wbadmin.exe` {#perform-a-full-server-backup-using-wbadminexe .heading-anchor}

-   Open an elevated command prompt, type the following command and press ENTER:

    For bare-metal backup:

    `wbadmin start backup -allCritical -backuptarget:\<Drive_letter_to_store_backup\>:`

    For full server backup:

    `wbadmin start backup -backuptarget:\<Drive_letter_to_store_backup\>: -include:\<Drive_letter_to_include\>:`

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

-   [AD Forest Recovery - Backing up the System State data](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-backing-up-system-state?source=recommendations)

    Learn more about: AD Forest Recovery - Backing up the System State data

-   [AD Forest Recovery - Performing a full server recovery](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-full-server-recovery?source=recommendations)

    A full server recovery is necessary if you\'re restoring to different hardware or a different operating system instance. Bare-Metal recovery is a supported method of backup.

-   [Active Directory Forest Recovery - Procedures](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-procedures?source=recommendations)

    View a list of procedures that are used in backing up and restoring domain controllers and Active Directory.

-   [Active Directory Forest Recovery - Prerequisites](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-prerequisites?source=recommendations)

    The following document discusses prerequisites that you should be familiar with before devising a forest recovery plan or attempting a recovery.

-   [Active Directory Forest Recovery - Perform initial recovery](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-initial-recovery?source=recommendations)

    Beginning with a writeable DC in the forest root domain, complete the steps in this section in order to restore the first DC.

-   [Back up system state and bare metal](/en-us/system-center/dpm/back-up-system-state-and-bare-metal?source=recommendations)

    You can use DPM to back up your system state and provide bare metal recovery (BMR) protection.

-   [AD Forest Recovery - Devising an AD Forest Recovery Plan](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-devise-a-plan?source=recommendations)

    Learn more about: AD Forest Recovery - Devising an AD Forest Recovery Plan

-   [AD Forest Recovery - Configure DNS Server service](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-configure-dns?source=recommendations)

    Learn more about: AD Forest Recovery - Configuring the DNS Server service

Training

Module

[Implement hybrid backup and recovery with Windows Server IaaS - Training](/en-us/training/modules/implement-hybrid-backup-recovery-windows-server-iaas/?source=recommendations)

Learn about Azure Backup before learning to implement Recovery Vaults and Azure Backup Policies. Learn to implement Windows IaaS VM recovery, perform backup and restore of on-premises workloads, and manage Azure VM backups.

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 11/01/2024
