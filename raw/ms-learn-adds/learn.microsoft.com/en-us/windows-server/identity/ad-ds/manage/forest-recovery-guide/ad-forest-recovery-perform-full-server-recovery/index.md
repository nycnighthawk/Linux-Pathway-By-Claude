---
{"title": "Active Directory Forest Recovery - Perform a full server recovery", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-full-server-recovery", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Active Directory Forest Recovery - Perform a full server recovery {#active-directory-forest-recovery----perform-a-full-server-recovery}

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

[](#active-directory-full-server-recovery)

## Active Directory Full Server Recovery {#active-directory-full-server-recovery .heading-anchor}

A full server recovery is necessary if you\'re restoring to different hardware or a different operating system instance. Bare-Metal recovery is a supported method of backup.

Keep in mind the following:

-   The number drives on the target server needs to be equal to the number in the backup and they need to be the same size or greater.
-   The target server needs to be started from the operating system DVD in order to access Windows PE Environment, and using the **Repair your computer** option.
-   If you\'re using disk volume encryption solutions like BitLocker, make sure you test and apply the steps necessary to the server recovery plan for getting the server OS restored and started properly.
-   If the target DC is running in a VM on Hyper-V and the backup is stored on a network location, you must install a legacy network adapter, with all isolation precautions needed depending on your recovery scenario.
-   After you perform a full server recovery, you need to separately perform an authoritative restore of SYSVOL, as described in [AD Forest Recovery - Performing an authoritative synchronization of DFSR-replicated SYSVOL](ad-forest-recovery-authoritative-recovery-sysvol).

Depending on your scenario, use one of the following procedures to perform a full restore.

**Perform a full server restore with a healthy local backup using the latest image**

1.  Start Windows Setup, specify the Language, Time and currency format, and keyboard options and select **Next**.
2.  Select **Repair your computer**.
3.  Select **Troubleshoot**.\
4.  Select **System Image Recovery**.\
5.  Select **Windows Server 2016**.
6.  If you\'re restoring the most recent local backup, select **Use the latest available system image (recommended)** and select **Next**.
    Note

    If you need to select a backup from another time as the problem was introduced was introduced some time ago, select \"Select a system image\" and chose the known good backup.
7.  You\'ll now be given an option to:
    -   Format and repartition disks.
    -   Install drivers.
    -   Deselecting the **Advanced** features of automatically restarting and checking for disk errors. These are enabled by default.
8.  Select **Next**.
9.  Select **Finish**. You\'ll be prompted if you\'re sure you want to continue. Select **Yes**.
10. Once this completes, perform an authoritative restore of SYSVOL, as described in [AD Forest Recovery - Performing an authoritative synchronization of DFSR-replicated SYSVOL](ad-forest-recovery-authoritative-recovery-sysvol).

[](#perform-a-full-server-restore-with-any-image-local-or-remote)

## Perform a full server restore with any image local or remote {#perform-a-full-server-restore-with-any-image-local-or-remote .heading-anchor}

1.  Start Windows Setup, specify the Language, Time and currency format, and keyboard options and select **Next**.
2.  Select **Repair your computer**.
3.  Select **Troubleshoot**, select **System Image Recovery**, and select **Windows Server 2016**.
4.  If you\'re restoring the most recent local backup, select **Select a system image** and select **Next**.
5.  Now you can select the location of the backup that you want to restore. If the image is local, you can select it from the list.
6.  If the image is on a network share, select **Advanced**. You can also select **Advanced** if you need to install a driver.
7.  If you\'re restoring from the network after clicking **Advanced** select **Search for a system image on the network**. You may be prompted to restore network connectivity. Select Ok.\
8.  Type the UNC path to the backup share location (for example, `\\\\server1\\backups`) and select **OK**. You can also type the IP address of the target server, such as `\\\\192.168.1.3\\backups`.
9.  Type credentials necessary to access the share and select OK.
10. Now **Select the date and time of system image to restore** and select **Next**.
11. You\'ll now be given an option to:
    -   Format and repartition disks.
    -   Install drivers.
    -   Deselecting the **Advanced** features of automatically restarting and checking for disk errors. These are enabled by default.
12. Select **Next**.
13. Select **Finish**. You\'ll be prompted asking if you\'re sure you want to continue. Select **Yes**.
14. Once this completes, perform an authoritative restore of SYSVOL, as described in [AD Forest Recovery - Performing an authoritative synchronization of DFSR-replicated SYSVOL](ad-forest-recovery-authoritative-recovery-sysvol).

[](#enable-the-network-adapter-for-a-network-backup)

## Enable the network adapter for a network backup {#enable-the-network-adapter-for-a-network-backup .heading-anchor}

If you need to enable a network adapter from the command prompt to restore from a network share, use the following steps.

1.  Start Windows Setup, specify the Language, Time and currency format, and keyboard options and select **Next**.

2.  Select **Repair your computer**. I

3.  Select **Troubleshoot**, select **Command Prompt**.

4.  Type the following command and press ENTER: `wpeinit`

5.  To confirm the name of the network adapter, type: `show interfaces`

6.  Type the following commands and press ENTER after each command: `netsh` `interface` `tcp` `ipv4` `set address "Name of Network Adapter" static IPv4 Address SubnetMask IPv4 Gateway Address 1`

    For example:

    `set address "Local Area Connection" static 192.168.1.2 255.0.0.0 192.168.1.1 1`

7.  Type `quit` to return to a command prompt.

8.  Type `ipconfig /all` to verify the network adapter has an IP address and try to ping the IP address of the server that hosts the backup share to confirm connectivity.

9.  Close the command prompt when you\'re done.

10. Now that the network adapter is working, repeat the steps above to complete the restore.

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

-   [Active Directory Forest Recovery - Procedures](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-procedures?source=recommendations)

    View a list of procedures that are used in backing up and restoring domain controllers and Active Directory.

-   [AD Forest Recovery - Backing up a full server](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-backing-up-a-full-server?source=recommendations)

    A Bare Metal Recovery (BMR) backup is recommended to prepare for a forest recovery because it can be restored to different hardware or a different operating system instance. Using Windows Server Backup you can perform a Bare-Metal Recovery (BMR) backup of your server.

-   [Active Directory Forest Recovery - Perform initial recovery](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-initial-recovery?source=recommendations)

    Beginning with a writeable DC in the forest root domain, complete the steps in this section in order to restore the first DC.

-   [AD Forest Recovery - Backing up the System State data](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-backing-up-system-state?source=recommendations)

    Learn more about: AD Forest Recovery - Backing up the System State data

-   [Active Directory Forest Recovery - Performing a nonauthoritative restore of Active Directory Domain Services](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-nonauthoritative-restore?source=recommendations)

    The following procedures use the wbadmin.exe to perform a nonauthoritative restore of Active Directory or Active Directory Domain Services (AD DS). If you\'re using a different backup solution or if you intend to complete the authoritative restore of SYSVOL later in the forest recovery process\...

-   [Active Directory Forest Recovery - Determine how to recover the forest](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-determine-how-to-recover?source=recommendations)

    Recovering an entire Active Directory forest involves restoring at least one Domain Controller (DC) in every domain from available backup. Recovering the forest restores each domain in the forest to its state at the time of the last trusted backup. Consequently, the restore operation will result in the loss of at least the following Active Directory data\...

-   [AD Forest Recovery - Steps for Restoring the forest](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-steps-for-restoring-the-forest?source=recommendations)

    This section provides an overview of the recommended path for recovering a forest. The forest recovery steps are described in detail later.

-   [Active Directory Forest Recovery - Prerequisites](/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-prerequisites?source=recommendations)

    The following document discusses prerequisites that you should be familiar with before devising a forest recovery plan or attempting a recovery.

Training

Module

[Troubleshoot Active Directory - Training](/en-us/training/modules/troubleshoot-active-directory/?source=recommendations)

Learn how to troubleshoot Active Directory including recovering deleted objects with AD Recycle Bin, managing the AD DS database with NtdsUtil, restoring SYSVOL, troubleshooting replication, and diagnosing hybrid authentication with Microsoft Entra Connect.

Certification

[Microsoft Certified: Windows Server Administrator Associate - Certifications](/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.

------------------------------------------------------------------------

-    Last updated on 11/01/2024
