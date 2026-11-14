---
{"title": "Restore a virtual domain controller", "url": "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/virtual-dc/restore-virtualized-domain-controller", "retrieved": "2026-11-14", "license": "CC-BY-4.0"}
---

# Restore a virtual domain controller

-   Applies to: ✅ [Windows Server 2025](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2022](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2019](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info), ✅ [Windows Server 2016](https://learn.microsoft.com/windows-server/get-started/windows-server-release-info)

You must regularly back up your system state in order to restore a physical or virtual domain controller (DC) during a disaster recovery scenario. The system state includes Active Directory data and log files, the registry, the system volume, and various elements of the operating system. Active Directory-compatible backup applications ensure consistent local and replicated Active Directory databases after a restore process, including notifying replication partners of invocation ID resets. Virtual hosting environments and disk or OS imaging applications let administrators bypass standard checks and validations that occur during DC system state restore.

If your DC virtual machine (VM) fails, and you don\'t see signs of an [update sequence number (USN) rollback](../../get-started/virtual-dc/virtualized-domain-controllers-hyper-v#usn-and-usn-rollback), there are two ways you can restore the VM:

-   If your system has a valid system state data backup from before the failure, you can restore it using the Active Directory-compatible backup utility you used to create the backup within the tombstone lifetime. The default tombstone lifetime is 180 days. You should back up your DCs regularly and at least every 90 days. For more information about determining tombstone lifetimes, see [Determine the tombstone lifetime for the forest](/en-us/previous-versions/windows/it-pro/windows-server-2003/cc784932(v=ws.10)).

-   If you have a working copy of the virtual hard disk (VHD) file but no system state backup, you can remove the existing VM and restore it using a previous copy of the VHD. Make sure to start the VM in DSRM, then configure the registry property as described in [Restore a system state backup](#restore-a-system-state-backup). After that, restart the DC in normal mode.

[](#determine-the-best-way-to-back-up-your-dc)

## Determine the best way to back up your DC {#determine-the-best-way-to-back-up-your-dc .heading-anchor}

There are several ways to back up your DC, but which way works best for your deployment depends on multiple factors.

-   If you don\'t have critical data on the DC or don\'t have a backup made before the DC went down:

    -   Forcibly remove the AD DS role from the DC.

    -   Remove the failed domain controller\'s computer account.

    -   If necessary, install the AD DS role on the replacement server that becomes the next DC.

-   If you have a system state backup, restore the DC by following the instructions in [Restore a system state backup](#restore-a-system-state-backup).

-   If you have a previous version of the DC on a VHD file, follow the directions in [Restore the virtual DC with a VHD file](#restore-the-virtual-dc-with-a-vhd-file).

    -   If the previous version runs Windows Server 2012 on a Hyper-V that supports the VM-GenerationID parameter, then deploy the VHD against a new VM, then restart the VM in normal mode.

    -   If the previous version runs a different version of Windows Server, have you already started it in normal mode?

        -   If no, then restore the DC by starting it in DSRM, setting the database restored from backup registry value to 1, then restarting it in normal mode.

        -   If yes, disconnect the virtual DC from the network, recover, and save any required unique data on a different copy of the VM, then don\'t use the original DC on the network again. Also, remove its AD DS role from original DC or reinstall the OS, then install the role to the new version of the DC.

If you\'re trying to restore an RODC:

-   If there\'s a system state data backup from before the original DC failed, use it to restore the DC.

-   If you don\'t have a system state backup but you do have a VHD file of a previous version of the DC, remove the failed DC, then create and start a new VM using the backup from the VHD file.

-   If you don\'t have either of those backups, remove the AD DS role from the domain controller by running this command:

    Windows Command Prompt

    ``` {.inner-focus data-language="cmd"}
    dcpromo /forceremoval
    ```

    After running the command, install the AD DS role on the replacement server to make it an RODC.

[](#restore-a-system-state-backup)

## Restore a system state backup {#restore-a-system-state-backup .heading-anchor}

If a valid system state backup exists for the DC VM, you can safely restore the backup by following the restore procedure for the backup tool that you used to back up the VHD file.

Important

To properly restore the DC, you must start the DC in DSRM, not normal mode. If you miss the opportunity to enter DSRM during system startup, turn off the DC\'s VM before it can fully start in normal mode. It\'s important to start the DC in DSRM because starting a DC in normal mode increments the USNs, even if the DC is disconnected from the network. For more information about USN rollback, see [USN and USN rollback](../../get-started/virtual-dc/virtualized-domain-controllers-hyper-v#usn-and-usn-rollback).

[](#restore-the-system-state-backup-of-the-virtual-dc)

### Restore the system state backup of the virtual DC {#restore-the-system-state-backup-of-the-virtual-dc .heading-anchor}

To restore the system state data backup of the virtual DC:

1.  Start the DC\'s VM, then press the F5 key to access **Windows Boot Manager**.

2.  If you\'re prompted to enter connection credentials, follow these steps:

    -   Immediately select the **Pause** button on the VM to pause the process.

    -   Enter your connection credentials.

    -   Select the **Play** button on the VM.

    -   Select inside the VM window, and press the F5 key.

    If **Windows Boot Manager** doesn\'t open and the DC begins to start in normal mode, turn the VM off to pause the process. Repeat this step as many times as necessary until you\'re able to access Windows Boot Manager. You can\'t access DSRM from the Windows Error Recovery menu. Therefore, turn off the VM and try again if the Windows Error Recovery menu appears.

3.  In **Windows Boot Manager**, press the F8 key to access advanced boot options.

4.  Under **Advanced Boot Options**, select **Directory Services Restore Mode**, and then press the Enter key to start the DC in DSRM.

5.  Use the appropriate restore method for the tool that you used to create the system state backup. If you used Windows Server Backup, follow the directions in [Performing a nonauthoritative restore of AD DS](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc730683(v=ws.10)).

[](#restore-the-virtual-dc-with-a-vhd-file)

### Restore the virtual DC with a VHD file {#restore-the-virtual-dc-with-a-vhd-file .heading-anchor}

If you don\'t have a system state data backup that predates the VM failure, you can use the VHD file to restore a DC that\'s running on a VM. Make sure you create a copy of the VHD file before you start. That way, if you encounter an issue during the procedure or miss a step, you can try again with the copied VHD.

Warning

You shouldn\'t use this procedure as a substitute for regularly planned and scheduled backups. Restores performed with this procedure aren\'t supported by Microsoft. Use this procedure only when there\'s no alternative.

Don\'t use this procedure if any VM has already started the copy of the VHD you plan to use for the restoration in normal mode.

To restore a virtual DC with a VHD file:

1.  Using the previous VHD, start the virtual DC in DSRM.

    -   Don\'t start the DC in normal mode. If you miss the **Windows Boot Manager** screen and the DC begins to start in normal mode, turn the VM off to prevent it from starting up.

2.  Open the Registry Editor by selecting **Start**, then entering `regedit.exe` and selecting **Registry Editor**.

    -   If the **User Account Control** dialog displays, confirm the displayed action is as expected, then select **Yes**.

    -   In Registry Editor, expand the path `HKLM\SYSTEM\CurrentControlSet\Services\NTDS\Parameters`.

    -   Look for a value named **DSA Previous Restore Count**. If the value is present, make a note of the setting. Otherwise, the setting value is the default (0). If no value is shown, don\'t manually set the value.

3.  Right-click the **Parameters** key, select **New**, and then select **DWORD (32-bit) Value**.

4.  Enter the new name **Database restored from backup**, then press the Enter key.

5.  Double-click the value you just created to open the **Edit DWORD (32-bit) Value** dialog, then find the **Value data** field and enter **1**.

6.  Restart the DC in normal mode.

7.  When the DC restarts, open Event Viewer by right-clicking **Start**, then selecting **Event Viewer**.

8.  Expand **Application and Services Logs**, then select the **Directory Services** log. Ensure the events appear in the details pane.

9.  Right-click the **Directory Services** log, then select **Find**.

10. In the **Find what** field, enter **1109**, then select **Find Next**.

11. You should see at least one entry for Event ID 1109. If you don\'t see this entry, proceed to the next step. Otherwise, double-click the entry and review the text. Confirm the text shows that the update was made to the InvocationID, as shown in the following example output:

    Output

    ``` {.inner-focus role="group" aria-label="Horizontally scrollable code" tabindex="0" data-language="output"}
    Active Directory has been restored from backup media, or has been configured to host an application partition.
    The invocationID attribute for this directory server has been changed.
    The highest update sequence number at the time the backup was created is <time>

    InvocationID attribute (old value):<Previous InvocationID value>
    InvocationID attribute (new value):<New InvocationID value>
    Update sequence number:<USN>

    The InvocationID is changed when a directory server is restored from backup media or is configured to host a writeable application directory partition.
    ```

12. Close **Event Viewer**.

13. Use **Registry Editor** to verify the value for the **DSA Previous Restore Count** setting is equal to the previous value plus one. If the correct value isn\'t there and you can\'t find an entry for Event ID 1109 in **Event Viewer**, verify that the DC\'s service packs are current.

    Note

    You can\'t try this procedure again on the same VHD. You can try again on a copy of the VHD or a different VHD that hasn\'t been started in normal mode by starting again from step 1.

14. Close the **Registry Editor**.

[](#additional-content)

## Additional content {#additional-content .heading-anchor}

For more information about virtualized DCs, see [Virtualizing domain controllers with Hyper-V](../../get-started/virtual-dc/virtualized-domain-controllers-hyper-v).

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

-   [Virtualized Domain Controller Troubleshooting](/en-us/windows-server/identity/ad-ds/manage/virtual-dc/virtualized-domain-controller-troubleshooting?source=recommendations)

    Learn more about: Virtualized Domain Controller Troubleshooting

-   [Can\'t promote a domain controller to a global catalog server - Windows Server](/en-us/troubleshoot/windows-server/active-directory/cannot-promote-dc-to-global-catalog-server?source=recommendations)

    Describes a problem where you can\'t promote a Windows Server-based domain controller to be a global catalog server.

-   [Verify DNS Functionality to Support Directory Replication](/en-us/windows-server/identity/ad-ds/manage/troubleshoot/verify-dns-functionality-to-support-directory-replication?source=recommendations)

    Learn more about: Verify DNS Functionality to Support Directory Replication

-   [How to reset the Directory Services Restore Mode administrator account password - Windows Server](/en-us/troubleshoot/windows-server/active-directory/reset-directory-services-restore-mode-admin-pwd?source=recommendations)

    Describes how to reset the DSRM administrator password for any server in your domain without restarting the server.

-   [Active Directory installation fails - Windows Server](/en-us/troubleshoot/windows-server/active-directory/creating-ntds-settings-object-for-ad-dc?source=recommendations)

    Fixes an error that occurs when you start Active Directory installation.

-   [Troubleshoot domain controller deployment - Windows Server](/en-us/troubleshoot/windows-server/active-directory/troubleshoot-domain-controller-deployment?source=recommendations)

    Provides information about troubleshooting domain controller deployment.

-   [Safely virtualizing Active Directory Domain Services (AD DS)](/en-us/windows-server/identity/ad-ds/introduction-to-active-directory-domain-services-ad-ds-virtualization-level-100?source=recommendations)

    USN Rollback and safe virtualization of Active Directory

-   [Virtualizing domain controllers with Hyper-V](/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controllers-hyper-v?source=recommendations)

    Learn about considerations for virtualizing Windows Server Active Directory domain controllers (DCs) in Hyper-V.

Training

Module

[Troubleshoot Active Directory - Training](/en-us/training/modules/troubleshoot-active-directory/?source=recommendations)

Learn how to troubleshoot Active Directory including recovering deleted objects with AD Recycle Bin, managing the AD DS database with NtdsUtil, restoring SYSVOL, troubleshooting replication, and diagnosing hybrid authentication with Microsoft Entra Connect.

Certification

[Microsoft Certified: Azure Virtual Desktop Specialty - Certifications](/en-us/credentials/certifications/azure-virtual-desktop-specialty/?source=recommendations)

Plan, deliver, manage, and monitor virtual desktop experiences and remote apps on Microsoft Azure for any device.

------------------------------------------------------------------------

-    Last updated on 01/24/2025
