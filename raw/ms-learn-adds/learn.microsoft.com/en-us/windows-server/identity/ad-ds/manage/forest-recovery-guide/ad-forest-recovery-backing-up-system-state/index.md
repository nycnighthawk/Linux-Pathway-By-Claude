---
{"title": "Active Directory Forest Recovery - Back up the System State data", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-backing-up-system-state", "retrieved": "2026-11-01", "license": "CC-BY-4.0"}
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

## Additional resources {#ms--additional-resources-mobile-heading .title .is-3 hidden=""}

------------------------------------------------------------------------

-    Last updated on 05/12/2025
