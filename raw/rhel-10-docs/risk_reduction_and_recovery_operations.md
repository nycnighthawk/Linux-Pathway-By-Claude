---
{"title": "Risk reduction and recovery operations", "guide": "risk_reduction_and_recovery_operations", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/risk_reduction_and_recovery_operations/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Risk reduction and recovery operations {#risk-reduction-and-recovery-operations .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Backing up data, log monitoring, and managing security updates {#backing-up-data-log-monitoring-and-managing-security-updates .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140494125956336)

**Abstract**

Use the Relax-and-Recover (ReaR) tool to back up and restore systems after failures. Monitor and troubleshoot system events through log files and the Audit framework. Manage and install security updates to maintain system stability and compliance.

------------------------------------------------------------------------

## [Providing feedback on Red Hat documentation](#providing-feedback-on-red-hat-documentation) {#providing-feedback-on-red-hat-documentation .title}

We are committed to providing high-quality documentation and value your feedback. To help us improve, you can submit suggestions or report errors through the Red Hat Jira tracking system.

**Procedure**

1.  Log in to the [Jira](https://redhat.atlassian.net/jira/software/c/projects/RHELDOCS/issues/) website.

    If you do not have an account, select the option to create one.

2.  Click **Create** in the top navigation bar.

3.  Enter a descriptive title in the **Summary** field.

4.  Enter your suggestion for improvement in the **Description** field. Include links to the relevant parts of the documentation.

5.  Click **Create** at the bottom of the window.

## [Chapter 1. Recovering and restoring a system](#recovering-and-restoring-a-system) {#chapter-1.-recovering-and-restoring-a-system .title}

To back up and restore your system, Red Hat Enterprise Linux provides the Relax-and-Recover (ReaR) utility.

You can use ReaR as a disaster recovery solution and also for system migration.

By using ReaR, you can perform the following tasks:

-   Produce a system backup and a bootable image, and use the image to restore the system from an existing backup.
-   Replicate the original storage layout.
-   Restore user and system files.
-   Restore the system to different hardware.

Additionally, for disaster recovery, you can also integrate certain backup software with ReaR.

### [1.1. Configuring ReaR and manually creating a backup](#setting-up-rear-and-manually-creating-a-backup) {#configuring-rear-and-manually-creating-a-backup .title}

To create a rescue system, first install the packages for the Relax-and-Recover (ReaR) utility, adjust ReaR settings, and manually generate a system backup. This prepares your system for potential disaster recovery operations.

**Prerequisites**

-   The necessary configurations based on your backup restore plan are ready.

    Note

    The following steps use the `NETFS`{.literal} backup method in example configurations. This method is fully-integrated and built-in with ReaR, and produces a backup in a location specified by the `BACKUP_URL`{.literal} configuration setting. By default it uses the system `tar`{.literal} utility to create a backup archive named `backup.tar.gz`{.literal}.

-   You are using the Intel 64 or AMD64 (x86-64) hardware architecture, or the IBM POWER little-endian (ppc64le) architecture.

    If you are using the IBM Z architecture, see [Using a ReaR rescue image on the 64-bit IBM Z architecture](#using-a-rear-rescue-image-on-the-64-bit-ibm-z-architecture "1.2. Using a ReaR rescue image on the 64-bit IBM Z architecture").

    On the 64-bit ARM architecture, ReaR is provided as a [Technology Preview](https://access.redhat.com/support/offerings/techpreview).

    Important

    Technology Preview features are not supported with Red Hat production Service Level Agreements (SLAs), might not be functionally complete, and Red Hat does not recommend using them for production. These previews provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

**Procedure**

1.  Install the ReaR utility:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install rear
    ```

2.  Modify the ReaR configuration file in an editor of your choice, for example:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/rear/local.conf
    ```

    -   Add the backup setting details to `/etc/rear/local.conf`{.literal}. For example, in the case of the `NETFS`{.literal} backup method, add the following lines:

        ``` {.language-plaintext tabindex="-1"}
        BACKUP=NETFS
        OUTPUT=ISO
        BACKUP_URL=<data-backup-location>
        OUTPUT_URL=<rescue-image-location>
        ```

        Replace *\<data-backup-location\>* with the location for the `tar`{.literal} data backup, and *\<rescue-image-location\>* with the location for the rescue system `ISO`{.literal} image. For example:

        ``` {.language-plaintext tabindex="-1"}
        BACKUP=NETFS
        OUTPUT=ISO

        # Backup is stored on an external drive
        BACKUP_URL=file:///run/media/user/external_drive/server_backups/

        # The ISO is stored on a dedicated NFS share
        OUTPUT_URL=nfs://backup-server.local/exports/rear/
        ```

        For further information on the syntax of the `/etc/rear/local.conf`{.literal} file and for supported formats of `BACKUP_URL`{.literal} and `OUTPUT_URL`{.literal}, see the `rear(8)`{.literal} man page.

        For a list of configuration variables that you can use in `/etc/rear/local.conf`{.literal}, as well as their default values, see the `/usr/share/rear/conf/default.conf`{.literal} file.

    -   To configure ReaR to keep the previous backup archive when the new one is created, also add the following line to the configuration file:

        ``` {.language-plaintext tabindex="-1"}
        NETFS_KEEP_OLD_BACKUP_COPY=y
        ```

    -   To make the backups incremental, meaning that only the changed files are backed up on each run, add the following line:

        ``` {.language-plaintext tabindex="-1"}
        BACKUP_TYPE=incremental
        ```

    -   If you are planning to boot the ReaR rescue system on UEFI firmware, add the following line to ensure the boot does not fail:

        ``` {.language-plaintext tabindex="-1"}
        SECURE_BOOT_BOOTLOADER=/boot/efi/EFI/redhat/shimx64.efi
        ```

        If your system uses the 64-bit ARM architecture (`aarch64`{.literal}), use the following path instead:

        ``` {.language-plaintext tabindex="-1"}
        SECURE_BOOT_BOOTLOADER=/boot/efi/EFI/redhat/shimaa64.efi
        ```

3.  Create a rescue system and data backup based on your restore plan. For example, when using the `NETFS`{.literal} backup method, run the following command:

    ``` {.language-plaintext tabindex="-1"}
    # rear mkbackup
    ```

    a.  If you need to create only the rescue system, use the `rear mkrescue`{.literal} command instead
    b.  If you need to create only the data backup, use the `rear mkbackuponly`{.literal} command instead.

4.  Optional: Schedule regular automatic ReaR backup. You can use a variety of backup methods, based on your use case. For example:

    -   Create a `/etc/cron.d/rear`{.literal} crontab file, and add the following line:

        ``` {.language-plaintext tabindex="-1"}
        30 1 * * * /usr/sbin/rear mkbackup
        ```

        This runs the `rear mkbackup`{.literal} command at 1:30 AM every day, which creates a rescue system and a data backup in the location set up in the `/etc/rear/local.conf`{.literal} file.

    -   If you use an external backup method, schedule an external backup. The details depend on the backup method that you are using in ReaR.

**Verification**

1.  Burn the ISO image of the rescue system to a DVD, and attempt to use the DVD to boot.

    If this displays a **Relax-and-Recover** interface after booting, the rescue DVD works correctly.

2.  Use the ReaR interface to restore the system, and test that the restored system works.

**Next steps**

-   [Recovering your system by using ReaR](#recovering-your-system-by-using-rear "1.3. Recovering your system by using ReaR")
-   [Modifying the content of the ReaR backup](#rear-exclusions "1.4. Modifying the content of the ReaR backup")

### [1.2. Using a ReaR rescue image on the 64-bit IBM Z architecture](#using-a-rear-rescue-image-on-the-64-bit-ibm-z-architecture) {#using-a-rear-rescue-image-on-the-64-bit-ibm-z-architecture .title}

To quickly recover and restore systems running on the IBM Z architecture, you can use the Relax-and-Recover (ReaR) rescue image.

ReaR provides basic functionality on the 64-bit IBM Z architecture and is fully supported in RHEL 10. You can create a ReaR rescue image on IBM Z only in the z/VM environment. Backing up and recovering logical partitions (LPARs) is not supported.

On IBM Z, ReaR currently supports only the Initial Program Load (IPL) output method. IPL produces a kernel and an initial RAM disk (`initrd`{.literal}) that can be used with the `zipl`{.literal} boot loader.

**Prerequisites**

-   You installed the `rear`{.literal} package.

**Procedure**

1.  Install ReaR:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install rear
    ```

2.  Add the following variables to the `/etc/rear/local.conf`{.literal} file to configure ReaR for producing a rescue image on the 64-bit IBM Z architecture:

    a.  To configure the `IPL`{.literal} output method, add the\`OUTPUT=IPL\` line to the configuration.

    b.  To configure the backup method and destination, add `BACKUP`{.literal} and `BACKUP_URL`{.literal} variables. For example:

        ``` {.language-plaintext tabindex="-1"}
        BACKUP=NETFS

        BACKUP_URL=nfs://<nfsserver_name>/<share_path>
        ```

        Important

        Local backup storage is currently not supported on the 64-bit IBM Z architecture.

    c.  Optional: You can also configure the `OUTPUT_URL`{.literal} variable to save the kernel and `initrd`{.literal} files. By default, the `OUTPUT_URL`{.literal} is aligned with `BACKUP_URL`{.literal}.

3.  To perform backup and rescue image creation:

    ``` {.language-plaintext tabindex="-1"}
    # rear mkbackup
    ```

    This creates the kernel and initrd files at the location specified by the `BACKUP_URL`{.literal} or `OUTPUT_URL`{.literal} (if set) variable, and a backup by using the specified backup method.

    Warning

    The rescue process reformats all the DASDs (Direct Attached Storage Devices) connected to the system. Do not attempt a system recovery if there is any valuable data present on the system storage devices. This also includes the device prepared with the `zipl`{.literal} boot loader, ReaR kernel, and `initrd`{.literal} that were used to boot into the rescue environment. Ensure to keep a copy.

4.  To recover the system, boot from a DASD or an FCP-attached SCSI device prepared with the `zipl`{.literal} boot loader. Use the previously created ReaR kernel and `initrd`{.literal} files.

5.  When the rescue kernel and `initrd`{.literal} are booted, the ReaR rescue environment starts. Proceed with system recovery.

**Next steps**

-   [Recovering your system by using ReaR](#recovering-your-system-by-using-rear "1.3. Recovering your system by using ReaR")

**Additional resources**

-   [Installing under z/VM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/booting-the-installation-media#booting-the-installation-on-ibm-z-to-install-rhel-in-zvm)
-   [Using a Prepared DASD](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/booting-the-installation-media#booting-the-rhel-installation-by-using-a-prepared-dasd)

### [1.3. Recovering your system by using ReaR](#recovering-your-system-by-using-rear) {#recovering-your-system-by-using-rear .title}

To recover your RHEL system on new hardware after a failure of the current hardware, use the Relax-and-Recover (ReaR) utility.

**Prerequisites**

-   You have configured ReaR and created a backup. For instructions, see [Configuring ReaR and manually creating a backup](#setting-up-rear-and-manually-creating-a-backup "1.1. Configuring ReaR and manually creating a backup").

-   You have a set of working hardware on which you want to run the system after you recover it.

-   The hard disk on which you plan to recover your system does not contain any critical data.

    Important

    Recovering a system on a hard disk by using ReaR erases all data currently stored on the disk.

**Procedure**

1.  Boot the rescue system on the new hardware. For example, you can burn the ISO image of the rescue system to a DVD, and boot from the DVD.

2.  In the **Relax-and-Recover** boot menu, select the option to boot to the recovery environment.

3.  In the `RESCUE`{.literal} prompt, run the `rear recover`{.literal} command.

    The rescue system recreates the partition layout and file systems.

4.  Restore user and system files from the data backup into the `/mnt/local/`{.literal} directory.

    For example, if you used the `NETFS`{.literal} method to create the backup, ReaR automatically performs the restoration process. However, based on your backup settings, ReaR might still require your confirmation in certain points of the restoration.

**Additional resources**

-   [Modifying the content of the ReaR backup](#rear-exclusions "1.4. Modifying the content of the ReaR backup")

### [1.4. Modifying the content of the ReaR backup](#rear-exclusions) {#modifying-the-content-of-the-rear-backup .title}

When creating a rescue system and data backup by using the Relax-and-Recover (ReaR) utility, certain files and storage components are not included in the backups. To adjust what data and devices are excluded from the backups, modify ReaR configuration.

When creating the rescue image, ReaR creates the `/var/lib/rear/layout/disklayout.conf`{.literal} layout file, and embeds the file in the rescue image.

During the recovery process, ReaR uses the layout file to recreate the storage layout of the original system on the disks of the recovered system. The storage layout includes partitions, volume groups, logical volumes, file systems, and other storage components.

**Prerequisites**

-   You have configured ReaR on your system. For instructions, see [Configuring ReaR and manually creating a backup](#setting-up-rear-and-manually-creating-a-backup "1.1. Configuring ReaR and manually creating a backup").

**Procedure**

1.  Generate the current layout file.

    ``` {.language-plaintext tabindex="-1"}
    # rear savelayout
    ```

2.  Open the layout file to examine its configuration. For example:

    ``` {.language-plaintext tabindex="-1"}
    # vi /var/lib/rear/layout/disklayout.conf
    ```

3.  To exclude specific files or storage devices from the backup, you can configure ReaR to ignore them when creating the rescue image.

    a.  Open the ReaR local configuration file for editing. For example:

        ``` {.language-plaintext tabindex="-1"}
        # vi /etc/rear/local.conf
        ```

    b.  Adjust which storage devices will be excluded from the layout file. You can use a variety of `exclude`{.literal} variables in the `/etc/rear/local.conf`{.literal} file, including the following:

        -   `AUTOEXCLUDE_DISKS`{.literal}
        -   `AUTOEXCLUDE_MULTIPATH`{.literal}
        -   `AUTOEXCLUDE_PATH`{.literal}
        -   `EXCLUDE_RECREATE`{.literal}

        For information on the functions and syntax of these variables and the layout file, see the `Layout configuration`{.literal} chapter in the ReaR user guide. This guide is installed with the `rear`{.literal} package, and is available at `/usr/share/doc/rear/user-guide/relax-and-recover-user-guide.html`{.literal}.

    c.  By default, when a local disk-based file system is included in the layout file, all its files are backed up when you run the `rear mkbackup`{.literal} or `rear mkbackuponly`{.literal} commands.

        To configure specific files or a directory tree to be excluded from the backup, use the `BACKUP_PROG_EXCLUDE`{.literal} variable.

        The value of `BACKUP_PROG_EXCLUDE`{.literal} must be an array of file matching patterns that `tar`{.literal} or `rsync`{.literal} uses. Note that you must quote the patterns to prevent their expansion by the shell when it reads the configuration file.

        The default value of this variable is set in the `/usr/share/rear/conf/default.conf`{.literal} file. The default value contains, for example, the `/tmp/*`{.literal} pattern that excludes all the files and directories under the `/tmp`{.literal} directory, but not the `/tmp`{.literal} directory itself.

        If you need to exclude other files and directories, append further patterns to the variable. To ensure that the default values are preserved, do not override the variable.

        For example, to exclude all files and directories under the directory `/data/temp`{.literal}, use:

        ``` {.language-plaintext tabindex="-1"}
        BACKUP_PROG_EXCLUDE+=( '/data/temp/*' )
        ```

        Note

        When you exclude all files and directories in a single mounted file system this way, ReaR recreates the file system during recovery, but it will be empty. You can use this for file systems that contain temporary data and do not require preserving, or for data that is backed up by using methods independent of ReaR.

**Verification**

1.  To ensure that the layout file includes only the required storage components, do the following:

    a.  Re-generate the layout file.

        ``` {.language-plaintext tabindex="-1"}
        # rear savelayout
        ```

    b.  Open the new layout file and make sure that your configuration changes had the intended effect.

        ``` {.language-plaintext tabindex="-1"}
        # vi /var/lib/rear/layout/disklayout.conf
        ```

2.  To ensure that the backup excludes specific files, use the `rear mkbackup`{.literal} command. This lists the backup exclude patterns in the log.

    You can find the log file in the `/var/log/rear`{.literal} directory. Use this to verify the exclude rules before performing a full system recovery. For example, the log can contain the following entries:

    ``` {.language-plaintext tabindex="-1"}
    2025-04-29 10:17:41.312431050 Making backup (using backup method NETFS)
    2025-04-29 10:17:41.314369109 Backup include list (backup-include.txt contents):
    2025-04-29 10:17:41.316197323   /
    2025-04-29 10:17:41.318052001 Backup exclude list (backup-exclude.txt contents):
    2025-04-29 10:17:41.319857125   /tmp/*
    2025-04-29 10:17:41.321644442   /dev/shm/*
    2025-04-29 10:17:41.323436363   /var/lib/rear/output/*
    ```

    In this example, the entire root file system is included in the backup, with the exception of all files and directories under the `/tmp`{.literal}, `/dev/shm`{.literal} and `/var/lib/rear/output`{.literal} directories.

## [Chapter 2. Troubleshooting problems by using log files](#troubleshooting-problems-by-using-log-files) {#chapter-2.-troubleshooting-problems-by-using-log-files .title}

Use log files to troubleshoot and monitor the system. Log files contain messages about the system, kernel, services, and applications, recorded efficiently using the built-in syslog protocol.

### [2.1. Basic troubleshooting by using log files](#basic-troubleshooting-by-using-log-files) {#basic-troubleshooting-by-using-log-files .title}

Investigate system problems by examining journal entries and traditional log files. Filtering logs by time, service, and priority helps you quickly narrow down the root cause.

**Prerequisites**

-   You are logged in to the system.

**Procedure**

1.  View log messages from the current boot:

    ``` {.language-plaintext tabindex="-1"}
    $ journalctl -b
    ```

2.  Filter log messages by a specific time range:

    ``` {.language-plaintext tabindex="-1"}
    $ journalctl --since "2025-07-01 08:00:00" --until "2025-07-01 12:00:00"
    ```

3.  Display only error and higher-priority messages:

    ``` {.language-plaintext tabindex="-1"}
    $ journalctl -p err -b
    ```

4.  Filter messages by a specific service:

    ``` {.language-plaintext tabindex="-1"}
    $ journalctl -u <service_name>.service -b
    ```

5.  Examine traditional log files for services that do not log through the journal:

    ``` {.language-plaintext tabindex="-1"}
    # cat /var/log/messages
    ```

    Some services store logs in subdirectories under `/var/log/`{.literal}. For example, the `httpd`{.literal} service uses `/var/log/httpd/`{.literal}.

6.  Follow new log entries in real time to observe ongoing issues:

    ``` {.language-plaintext tabindex="-1"}
    $ journalctl -f
    ```

**Verification**

-   Verify that the log output contains entries relevant to the issue you are investigating, such as error messages, failed service starts, or unexpected reboots.

### [2.2. Services that handle syslog messages](#services-handling-syslog-messages) {#services-that-handle-syslog-messages .title}

The `rsyslogd`{.literal} and `journald`{.literal} system services handle syslog messages. These services capture, process, and store security-relevant system events.

The following services handle syslog messages:

The `systemd-journald`{.literal} daemon

:   Collects messages from the following sources and forwards them to Rsyslog for further processing:

    -   Kernel
    -   Early stages of the boot process
    -   Standard and error output of daemons as they start and run
    -   Syslog

The `rsyslog`{.literal} service
:   Sorts syslog messages by type and priority and writes them to the files in the `/var/log`{.literal} directory. The `/var/log`{.literal} directory persistently stores the log messages.

### [2.3. Subdirectories that store syslog messages](#subdirectories-storing-syslog-messages) {#subdirectories-that-store-syslog-messages .title}

Locate where system logging services store recorded syslog messages. Most log files are kept in the /var/log/ directory, often organized logically into subdirectories based on the application.

The following subdirectories under the `/var/log`{.literal} directory store syslog messages:

/var/log/messages
:   all syslog messages except the following

/var/log/secure
:   security and authentication-related messages and errors

/var/log/maillog
:   mail server-related messages and errors

/var/log/cron
:   log files related to periodically executed tasks

/var/log/boot.log
:   log files related to system startup

### [2.4. Commands for viewing logs](#commands-for-viewing-logs) {#commands-for-viewing-logs .title}

You can view and manage log files by using the Journal, which is a component of `systemd`{.literal}. It addresses problems connected with traditional logging, is closely integrated with the rest of the system, and supports various logging technologies and access management for the log files.

You can use the `journalctl`{.literal} command to view messages in the system journal, for example:

``` {.language-plaintext tabindex="-1"}
$ journalctl -b | grep kvm
May 15 11:31:41 localhost.localdomain kernel: kvm-clock: Using msrs 4b564d01 and 4b564d00
May 15 11:31:41 localhost.localdomain kernel: kvm-clock: cpu 0, msr 76401001, primary cpu clock
```

#### [2.4.1. Viewing system information](#viewing_system_information) {#viewing-system-information .title}

`journalctl`{.literal}
:   Shows all collected journal entries.

`journalctl FILEPATH`{.literal}
:   Shows logs related to a specific file. For example, the `journalctl /dev/sda`{.literal} command displays logs related to the `/dev/sda`{.literal} file system.

`journalctl -b`{.literal}
:   Shows logs for the current boot.

`journalctl -k -b -1`{.literal}
:   Shows kernel logs for the current boot.

#### [2.4.2. Viewing information about specific services](#viewing_information_about_specific_services) {#viewing-information-about-specific-services .title}

`journalctl -b _SYSTEMD_UNIT=`{.literal}*`<name.service>`{.literal}*
:   Filters log to show entries matching the `systemd`{.literal} service.

`journalctl -b _SYSTEMD_UNIT=`{.literal}*`<name.service>`{.literal}*` _PID=`{.literal}*`<number>`{.literal}*
:   Combines matches. For example, this command shows logs for `systemd-units`{.literal} that match *`<name.service>`{.literal}* and the PID *`<number>`{.literal}*.

`journalctl -b _SYSTEMD_UNIT=`{.literal}*`<name.service>`{.literal}*` _PID=`{.literal}*`<number>`{.literal}*` + _SYSTEMD_UNIT=`{.literal}*`<name2.service>`{.literal}*
:   The plus sign (+) separator combines two expressions in a logical OR. For example, this command shows all messages from the *`<name.service>`{.literal}* service process with the `PID`{.literal} plus all messages from the *`<name2.service>`{.literal}* service (from any of its processes).

`journalctl -b _SYSTEMD_UNIT=`{.literal}*`<name.service>`{.literal}*` _SYSTEMD_UNIT=`{.literal}*`<name2.service>`{.literal}*
:   This command shows all entries matching either expression, referring to the same field. Here, this command shows logs matching a systemd-unit *`<name.service>`{.literal}* or a systemd-unit *`<name2.service>`{.literal}*.

#### [2.4.3. Viewing logs related to specific boots](#viewing_logs_related_to_specific_boots) {#viewing-logs-related-to-specific-boots .title}

`journalctl --list-boots`{.literal}
:   Shows a tabular list of boot numbers, their IDs, and the timestamps of the first and last message pertaining to the boot. You can use the ID in the next command to view detailed information.

`journalctl --boot=ID _SYSTEMD_UNIT=`{.literal}*`<name.service>`{.literal}*
:   Shows information about the specified boot ID.

### [2.5. Additional resources](#troubleshooting-problems-by-using-log-files_25-additional-resources) {#additional-resources .title}

-   [Configuring a remote logging solution](#configuring-a-remote-logging-solution "Chapter 5. Configuring a remote logging solution")

## [Chapter 3. Reviewing and filtering logs in the web console](#reviewing-and-filtering-logs-in-the-web-console) {#chapter-3.-reviewing-and-filtering-logs-in-the-web-console .title}

The Red Hat Enterprise Linux web console provides a graphical interface for accessing, reviewing, and filtering logs. You can use the most common functions without memorizing the corresponding commands and options.

### [3.1. Reviewing logs in the web console](#reviewing-logs-in-the-web-console) {#reviewing-logs-in-the-web-console .title}

You can quickly access and examine system logs by using the RHEL web console's dedicated **Logs** section. This graphical interface helps centralize log monitoring for various system functions across the host and provides a UI for the `journalctl`{.literal} utility.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

**Procedure**

1.  Log in to the RHEL 10 web console.
2.  Click **Logs**.
3.  Open log entry details by clicking on your selected log entry in the list.

**Next steps**

-   After clicking Toggle filters to expand the menu, you can use the Pause button to pause new log entries from appearing. Once you resume new log entries, the web console loads all log entries that are reported after you use the Pause button.
-   You can filter the logs by time, priority, or identifier. For more information, see [Reviewing and filtering logs in the web console](#reviewing-and-filtering-logs-in-the-web-console "Chapter 3. Reviewing and filtering logs in the web console").

### [3.2. Filtering logs in the web console](#filtering-logs-in-the-web-console) {#filtering-logs-in-the-web-console .title}

You can filter system logs directly in the RHEL web console based on time range, priority, or specific identifiers. This capability helps administrators focus only on critical messages for targeted troubleshooting.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  Click **Logs**.

3.  Click Toggle filters.

4.  To change the default log filtering, use the **Time**, **Priority**, and **Identifier** drop-down menus.

5.  Optional: By default, the web console shows the latest log entries. To filter by a specific time range, click the Expand button.

6.  Click the → button (right pointing arrow) to apply your filters.

7.  To open a log entry, click the selected log entry.

### [3.3. Text search options for filtering logs in the web console](#text-search-options-for-filtering-logs-in-the-web-console) {#text-search-options-for-filtering-logs-in-the-web-console .title}

With the text search syntax and options available in the RHEL web console, you can filter logs effectively. This enables high precision when searching for specific errors or keywords across extensive system logs.

The text search option functionality provides a wide variety of options for filtering logs. You can use the predefined options from the three drop-down menus or type the whole search yourself.

Drop-down menus

:   You can use three drop-down menus to specify the main parameters of your search:

    -   **Time**: This drop-down menu contains predefined searches for different time ranges of your search.
    -   **Priority**: This drop-down menu provides options for different priority levels. It corresponds to the `journalctl --priority`{.literal} option. The default priority value is **Error and above**. It is set every time you do not specify any other priority.
    -   **Identifier**: In this drop-down menu, you can select an identifier that you want to filter. Corresponds to the `journalctl --identifier`{.literal} option.

Quantifiers
:   You can use six quantifiers to specify your search. They are covered in the **Options for filtering logs** table.

Log fields
:   To search for a specific log field, you can specify the field together with its content.

Free-form text search in log messages
:   You can filter any text string of your choice in the log messages. The string can also be in the form of a regular expression.

**Example 3.1. Logs filtering based on time**

Filter all log messages identified by \'systemd\' that happened since October 22, 2020 midnight and journal field \'JOB_TYPE\' is either \'start\' or \'restart.

1.  Type `identifier:systemd since:2020-10-22 JOB_TYPE=start,restart`{.literal} to search field.

2.  Check the results.

**Example 3.2. Logs containing error and fail messages**

Filter all log messages that come from \'cockpit.service\' systemd unit that happened in the boot before last and the message body contains either \"error\" or \"fail\".

1.  Type `service:cockpit boot:-1 error|fail`{.literal} to the search field.

2.  Check the results.

### [3.4. Using a text search box to filter logs in the web console](#using-a-text-search-box-to-filter-logs-in-the-web-console) {#using-a-text-search-box-to-filter-logs-in-the-web-console .title}

You can filter logs according to different parameters by using the text search box in the web console. The search combines the usage of the filtering drop-down menus, quantifiers, log fields, and free-form string search.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  Click **Logs**.

3.  Use the drop-down menus to specify the three main quantifiers - time range, priority, and identifier(s) - you want to filter.

    The **Priority** quantifier must have a value. If you do not specify a value, it automatically filters the **Error and above** priority. The options you set reflect in the text search box.

4.  Specify the log field you want to filter.

    You can add several log fields.

5.  You can use a free-form string to search for anything else. The search box also accepts regular expressions.

### [3.5. Options for filtering logs](#options-for-logs-filtering) {#options-for-filtering-logs .title}

Review the various options available for filtering system logs in the RHEL web console. Options include time range, priority, identifier, and customized text search fields.

You can use `journalctl`{.literal} options for filtering logs in the web console. Some of these options are provided as parts of the drop-down menus in the web console interface.

+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Option name            | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Notes                                                                                                                          |
+:=======================+:================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+:===============================================================================================================================+
| `priority`{.literal}   | Filters output by message priorities. Takes a single numeric or textual log level. The log levels are the usual syslog log levels. If a single log level is specified, all messages with this log level or a lower and more important log level are shown.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Covered in the **Priority** drop-down menu.                                                                                    |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| `identifier`{.literal} | Shows messages for the specified syslog identifier SYSLOG_IDENTIFIER. Can be specified multiple times.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Covered in the **Identifier** drop-down menu.                                                                                  |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| `follow`{.literal}     | Shows only the most recent journal entries, and continuously prints new entries as they are appended to the journal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Not covered in a drop-down.                                                                                                    |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| `service`{.literal}    | Shows messages for the specified `systemd`{.literal} unit. Can be specified multiple times.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Is not covered in a drop-down. Corresponds to the `journalctl --unit`{.literal} parameter.                                     |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| `boot`{.literal}       | Shows messages from a specific boot.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Covered only as **Current boot** or **Previous boot** in the **Time** drop-down menu. You must specify other options manually. |
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                |
|                        | A positive integer looks up the boots starting from the beginning of the journal, and an equal-or-less-than-zero integer looks up boots starting from the end of the journal. Therefore, 1 means the first boot found in the journal in chronological order, 2 the second, and so on; while -0 is the last boot, -1 the boot before last, and so on.                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| `since`{.literal}      | Starts showing entries on or newer than the specified date, or on or older than the selected date. Date specifications should be of the format \"2012-10-30 18:17:16\". If the time part is omitted, \"00:00:00\" is considered. If only the seconds component is omitted, \":00\" is assumed. If the date component is omitted, the current day is assumed. Alternatively, the strings \"yesterday\", \"today\", \"tomorrow\" are understood, which refer to 00:00:00 of the day before the current day, the current day, or the day after the current day. \"now\" refers to the current time. Finally, relative times might be specified, prefixed with \"-\" or \"+\", referring to times before or after the current time. | Not covered in a drop-down.                                                                                                    |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+

: Table 3.1. Options for filtering logs in the RHEL web console

Show more

## [Chapter 4. Configuring the systemd journal by using RHEL system roles](#configuring-the-systemd-journal-by-using-rhel-system-roles) {#chapter-4.-configuring-the-systemd-journal-by-using-rhel-system-roles .title}

With the `journald`{.literal} RHEL system role you can automate the `systemd`{.literal} journal, and configure persistent logging by using the Red Hat Ansible Automation Platform.

### [4.1. Configuring persistent logging by using the journald RHEL system role](#configuring-persistent-logging-by-using-the-journald-rhel-system-role) {#configuring-persistent-logging-by-using-the-journald-rhel-system-role .title}

By default, the `systemd`{.literal} journal stores logs only in a small ring buffer in `/run/log/journal`{.literal}, which is not persistent. Rebooting the system also removes journal database logs. You can configure persistent logging consistently on multiple systems by using the `journald`{.literal} RHEL system role.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configure journald
      hosts: managed-node-01.example.com
      tasks:
        - name: Configure persistent logging
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.journald
          vars:
            journald_persistent: true
            journald_max_disk_size: <size>
            journald_per_user: true
            journald_sync_interval: <interval>
    ```

    The settings specified in the example playbook include the following:

    `journald_persistent: true`{.literal}
    :   Enables persistent logging.

    `journald_max_disk_size: `{.literal}*`<size>`{.literal}*
    :   Specifies the maximum size of disk space for journal files in MB, for example, `2048`{.literal}.

    `journald_per_user: true`{.literal}
    :   Configures `journald`{.literal} to keep log data separate for each user.

    `journald_sync_interval: `{.literal}*`<interval>`{.literal}*

    :   Sets the synchronization interval in minutes, for example, `1`{.literal}.

        For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.journald/README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

-   On the managed node, verify that the `/var/log/journal/`{.literal} directory exists and contains journal log files:

    ``` {.language-plaintext tabindex="-1"}
    # ls /var/log/journal//
    ```

    If the directory exists and contains files, persistent logging is configured correctly.

## [Chapter 5. Configuring a remote logging solution](#configuring-a-remote-logging-solution) {#chapter-5.-configuring-a-remote-logging-solution .title}

Ensure that logs from various machines in your environment are recorded centrally on a logging server. You can configure the Rsyslog application to forward logs that meet specific criteria from client systems to the server.

Choose a transport protocol based on your requirements:

TCP
:   Reliable delivery with message acknowledgment. Use when log integrity is important.

UDP
:   Faster but messages can be lost. Use when speed is critical and occasional log loss is acceptable.

TLS
:   Encrypted transport over TCP. Use when sending logs over untrusted networks.

RELP
:   Reliable delivery with reduced risk of message loss, even during network outages. Use in environments where no log messages must be lost.

### [5.1. The Rsyslog logging service](#the-rsyslog-logging-service) {#the-rsyslog-logging-service .title}

The Rsyslog logging service defines rules in the `/etc/rsyslog.conf`{.literal} file. Rules classify messages by urgency and topic, determining the action Rsyslog performs.

The Rsyslog application, in combination with the `systemd-journald`{.literal} service, provides local and remote logging support in Red Hat Enterprise Linux. The `rsyslogd`{.literal} daemon continuously reads `syslog`{.literal} messages received by the `systemd-journald`{.literal} service from the Journal. It then filters and processes these events, records them to log files, or forwards them to other services.

The `rsyslogd`{.literal} daemon also provides extended filtering, encryption-protected relaying of messages, input and output modules, and support for transport that uses the TCP and UDP protocols.

In `/etc/rsyslog.conf`{.literal}, which is the main configuration file for `rsyslog`{.literal}, you can specify the rules according to which `rsyslogd`{.literal} handles the messages. Generally, you can classify messages by their source and topic (facility) and urgency (priority), and then assign an action that should be performed when a message fits these criteria.

In `/etc/rsyslog.conf`{.literal}, you can also see a list of log files maintained by `rsyslogd`{.literal}. Most log files are located in the `/var/log/`{.literal} directory. Some applications, such as `httpd`{.literal} and `samba`{.literal}, store their log files in a subdirectory within `/var/log/`{.literal}.

For more information, see the `rsyslogd(8)`{.literal} and `rsyslog.conf(5)`{.literal} man pages on your system, or the comprehensive documentation installed with the `rsyslog-doc`{.literal} package in the `/usr/share/doc/rsyslog/html/index.html`{.literal} file.

### [5.2. Installing Rsyslog documentation](#installing-rsyslog-documentation) {#installing-rsyslog-documentation .title}

Install the `rsyslog-doc`{.literal} documentation package locally. This provides quick, offline access to the extensive documentation for the Rsyslog application, complementing the online resources.

The Rsyslog application has extensive online documentation that is available at [Rsyslog official documentation](https://www.rsyslog.com/doc/), but you can also install the `rsyslog-doc`{.literal} documentation package on your system.

**Prerequisites**

-   You have activated the `AppStream`{.literal} repository on your system.
-   You are authorized to install new packages using `sudo`{.literal}.

**Procedure**

-   Install the `rsyslog-doc`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install rsyslog-doc
    ```

**Verification**

-   Open the `/usr/share/doc/rsyslog/html/index.html`{.literal} file in a browser of your choice, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ firefox /usr/share/doc/rsyslog/html/index.html &
    ```

### [5.3. Configuring a server for remote logging over TCP](#configuring-a-server-for-remote-logging-over-tcp) {#configuring-a-server-for-remote-logging-over-tcp .title}

Configure your Rsyslog server to receive remote logs through the reliable TCP protocol. This setup helps ensure high integrity when transferring logs from client systems over the network.

With the Rsyslog application, you can maintain a centralized logging system where log messages are forwarded to a server over the network. To avoid message loss when the server is not available, you can configure an action queue for the forwarding action. This way, messages that failed to be sent are stored locally until the server is reachable again. Note that such queues cannot be configured for connections that use the UDP protocol.

The `omfwd`{.literal} plugin provides forwarding over UDP or TCP. The default protocol is UDP. Because the plugin is built-in, it does not have to be loaded.

By default, `rsyslog`{.literal} uses TCP on port `514`{.literal}.

**Prerequisites**

-   Rsyslog is installed on the server system.
-   You are logged in as `root`{.literal} on the server.
-   The `policycoreutils-python-utils`{.literal} package is installed for the optional step using the `semanage`{.literal} command.
-   The `firewalld`{.literal} service is running.

**Procedure**

1.  Optional: To use a different port for `rsyslog`{.literal} traffic, add the `syslogd_port_t`{.literal} SELinux type to port. For example, enable port `30514`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # semanage port -a -t syslogd_port_t -p tcp 30514
    ```

2.  Optional: To use a different port for `rsyslog`{.literal} traffic, configure `firewalld`{.literal} to allow incoming `rsyslog`{.literal} traffic on that port. For example, allow TCP traffic on port `30514`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --zone=<zone_name> --permanent --add-port=30514/tcp
    success
    # firewall-cmd --reload
    ```

3.  Create a new file in the `/etc/rsyslog.d/`{.literal} directory named, for example, `remotelog.conf`{.literal}, and insert the following content:

    ``` {.language-plaintext tabindex="-1"}
    # Define templates before the rules that use them
    # Per-Host templates for remote systems
    template(name="TmplAuthpriv" type="list") {
        constant(value="/var/log/remote/auth/")
        property(name="hostname")
        constant(value="/")
        property(name="programname" SecurePath="replace")
        constant(value=".log")
        }

    template(name="TmplMsg" type="list") {
        constant(value="/var/log/remote/msg/")
        property(name="hostname")
        constant(value="/")
        property(name="programname" SecurePath="replace")
        constant(value=".log")
        }

    # Provides TCP syslog reception
    module(load="imtcp")

    # Adding this ruleset to process remote messages
    ruleset(name="remote1"){
         authpriv.*   action(type="omfile" DynaFile="TmplAuthpriv")
          *.info;mail.none;authpriv.none;cron.none
    action(type="omfile" DynaFile="TmplMsg")
    }

    input(type="imtcp" port="30514" ruleset="remote1")
    ```

4.  Save the changes to the `/etc/rsyslog.d/remotelog.conf`{.literal} file.

5.  Test the syntax of the `/etc/rsyslog.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # rsyslogd -N 1
    rsyslogd: version 8.1911.0-2.el8, config validation run...
    rsyslogd: End of config validation run. Bye.
    ```

6.  Make sure the `rsyslog`{.literal} service is running and enabled on the logging server:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status rsyslog
    ```

7.  Restart the `rsyslog`{.literal} service.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart rsyslog
    ```

8.  Optional: If `rsyslog`{.literal} is not enabled, ensure the `rsyslog`{.literal} service starts automatically after reboot:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable rsyslog
    ```

**Verification**

-   To verify that the client system sends messages to the server:

    1.  On the client system, send a test message:

        ``` {.language-plaintext tabindex="-1"}
        # logger test
        ```

    2.  On the server system, view the `/var/log/messages`{.literal} log, for example:

        ``` {.language-plaintext tabindex="-1"}
        # cat /var/log/remote/msg/<hostname>/root.log
        Feb 25 03:53:17 <hostname> root[6064]: test
        ```

        Where *`<hostname>`{.literal}* is the hostname of the client system. Note that the log contains the user name of the user who entered the logger command, in this case, `root`{.literal}.

### [5.4. Configuring remote logging to a server over TCP](#configuring-remote-logging-to-a-server-over-tcp) {#configuring-remote-logging-to-a-server-over-tcp .title}

You can configure a system for forwarding log messages to a server over the TCP protocol. The `omfwd`{.literal} plugin provides forwarding over UDP or TCP. The default protocol is UDP. Because the plugin is built in, you do not have to load it.

**Prerequisites**

-   The `rsyslog`{.literal} package is installed on the client systems that should report to the server.
-   You have configured the server for remote logging.
-   The specified port is permitted in SELinux and open in firewall.
-   The system contains the `policycoreutils-python-utils`{.literal} package, which provides the `semanage`{.literal} command for adding a non-standard port to the SELinux configuration.

**Procedure**

1.  Create a new file in the `/etc/rsyslog.d/`{.literal} directory named, for example, `10-remotelog.conf`{.literal}, and insert the following content:

    ``` {.language-plaintext tabindex="-1"}
    *.* action(type="omfwd"
          queue.type="linkedlist"
          queue.filename="example_fwd"
          action.resumeRetryCount="-1"
          queue.saveOnShutdown="on"
          target="example.com" port="30514" protocol="tcp"
         )
    ```

    Where:

    -   The `queue.type="linkedlist"`{.literal} setting enables a LinkedList in-memory queue,

    -   The `queue.filename`{.literal} setting defines a disk storage. The backup files are created with the `example_fwd`{.literal} prefix in the working directory specified by the preceding global `workDirectory`{.literal} directive.

    -   The `action.resumeRetryCount -1`{.literal} setting prevents `rsyslog`{.literal} from dropping messages when retrying to connect if server is not responding,

    -   The `queue.saveOnShutdown="on"`{.literal} setting saves in-memory data if `rsyslog`{.literal} shuts down.

    -   The last line forwards all received messages to the logging server. Port specification is optional.

        With this configuration, `rsyslog`{.literal} sends messages to the server but keeps messages in memory if the remote server is not reachable. A file on disk is created only if `rsyslog`{.literal} runs out of the configured memory queue space or needs to shut down, which benefits the system performance.

        Note

        Rsyslog processes configuration files `/etc/rsyslog.d/`{.literal} in the lexical order.

2.  Restart the `rsyslog`{.literal} service.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart rsyslog
    ```

**Verification**

To verify that the client system sends messages to the server:

1.  On the client system, send a test message:

    ``` {.language-plaintext tabindex="-1"}
    # logger test
    ```

2.  On the server system, view the `/var/log/messages`{.literal} log, for example:

    ``` {.language-plaintext tabindex="-1"}
    # cat /var/log/remote/msg/hostname/root.log
    Feb 25 03:53:17 hostname root[6064]: test
    ```

    Where *hostname* is the hostname of the client system. Note that the log contains the user name of the user that entered the `logger`{.literal} command, in this case `root`{.literal}.

### [5.5. Configuring TLS-encrypted remote logging](#configuring-tls-encrypted-remote-logging) {#configuring-tls-encrypted-remote-logging .title}

Encrypt remote logging communication by using TLS to secure the data transfer. Configuring TLS on both the server and the client helps protect sensitive logs from network interception.

By default, Rsyslog sends remote logging messages in plain text. To use encrypted transport through TLS, configure both the server and the client. The server collects and analyzes the logs sent by one or more client systems.

You can use either the `ossl`{.literal} network stream driver (OpenSSL) or the `gtls`{.literal} stream driver (GnuTLS).

Note

If you have a separate system with higher security, for example a system that is not connected to any network, use it as the certification authority (CA).

You can customize your connection settings with stream drivers at multiple levels. On the server side, use the `global`{.literal}, `module`{.literal}, and `input`{.literal} levels. On the client side, use the `global`{.literal} and `action`{.literal} levels. A more specific configuration overrides a more general one. For example, you can use `ossl`{.literal} in global settings for most connections and `gtls`{.literal} only for specific connections.

**Prerequisites**

-   You have `root`{.literal} access to both the client and server systems.

-   The following packages are installed on the server and the client systems:

    -   The `rsyslog`{.literal} package.
    -   For the `ossl`{.literal} network stream driver, the `rsyslog-openssl`{.literal} package.
    -   For the `gtls`{.literal} network stream driver, the `rsyslog-gnutls`{.literal} package.
    -   For generating certificates by using the `certtool`{.literal} command, the `gnutls-utils`{.literal} package.

-   On your logging server, the following certificates are in the `/etc/pki/ca-trust/source/anchors/`{.literal} directory, and your system configuration is updated by using the `update-ca-trust`{.literal} command:

    -   `ca-cert.pem`{.literal} - a CA certificate that can verify keys and certificates on logging servers and clients.
    -   `server-cert.pem`{.literal} - a public key of the logging server.
    -   `server-key.pem`{.literal} - a private key of the logging server.

-   On your logging clients, the following certificates are in the `/etc/pki/ca-trust/source/anchors/`{.literal} directory, and your system configuration is updated by using `update-ca-trust`{.literal}:

    -   `ca-cert.pem`{.literal} - a CA certificate that can verify keys and certificates on logging servers and clients.
    -   `client-cert.pem`{.literal} - a public key of a client.
    -   `client-key.pem`{.literal} - a private key of a client.
    -   If the server runs RHEL 9.2 or later and FIPS mode is enabled, clients must either support the Extended Master Secret (EMS) extension or use TLS 1.3. TLS 1.2 connections without EMS fail. For more information, see the [TLS extension \"Extended Master Secret\" enforced](https://access.redhat.com/solutions/7018256) article (Red Hat Knowledgebase).

**Procedure**

1.  Configure the server for receiving encrypted logs from your client systems:

    a.  Create a new file in the `/etc/rsyslog.d/`{.literal} directory named, for example, `securelogser.conf`{.literal}.

    b.  To encrypt the communication, the configuration file must contain paths to certificate files on your server, a selected authentication method, and a stream driver that supports TLS encryption. Add the following lines to the `/etc/rsyslog.d/securelogser.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        # Set certificate files
        global(
          DefaultNetstreamDriverCAFile="/etc/pki/ca-trust/source/anchors/ca-cert.pem"
          DefaultNetstreamDriverCertFile="/etc/pki/ca-trust/source/anchors/server-cert.pem"
          DefaultNetstreamDriverKeyFile="/etc/pki/ca-trust/source/anchors/server-key.pem"
        )

        # TCP listener
        module(
          load="imtcp"
          PermittedPeer=["client1.example.com", "client2.example.com"]
          StreamDriver.AuthMode="x509/name"
          StreamDriver.Mode="1"
          StreamDriver.Name="ossl"
        )

        # Start up listener at port 514
        input(
          type="imtcp"
          port="514"
        )
        ```

        Note

        If you prefer the GnuTLS driver, use the `StreamDriver.Name="gtls"`{.literal} configuration option. See the documentation installed with the `rsyslog-doc`{.literal} package for more information about less strict authentication modes than `x509/name`{.literal}.

    c.  Optional: To customize the connection configuration, replace the `input`{.literal} section with the following:

        ``` {.language-plaintext tabindex="-1"}
        input(
          type="imtcp"
          Port="50515"
          StreamDriver.Name="<driver>"
          streamdriver.CAFile="/etc/rsyslog.d/<ca1>.pem"
          streamdriver.CertFile="/etc/rsyslog.d/<server1_cert>.pem"
          streamdriver.KeyFile="/etc/rsyslog.d/<server1_key>.pem"
        )
        ```

        -   Replace *`<driver>`{.literal}* with `ossl`{.literal} or `gtls`{.literal} depending on the driver you want to use.
        -   Replace *`<ca1>`{.literal}* with the CA certificate, *`<server1_cert>`{.literal}* with the certificate, and *`<server1_key>`{.literal}* with the key of the customized connection.

    d.  Save the changes to the `/etc/rsyslog.d/securelogser.conf`{.literal} file.

    e.  Verify the syntax of the `/etc/rsyslog.conf`{.literal} file and any files in the `/etc/rsyslog.d/`{.literal} directory:

        ``` {.language-plaintext tabindex="-1"}
        # rsyslogd -N 1
        rsyslogd: version 8.1911.0-2.el8, config validation run (level 1)...
        rsyslogd: End of config validation run. Bye.
        ```

    f.  Make sure the `rsyslog`{.literal} service is running and enabled on the logging server:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl status rsyslog
        ```

    g.  Restart the `rsyslog`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart rsyslog
        ```

    h.  Optional: If Rsyslog is not enabled, ensure the `rsyslog`{.literal} service starts automatically after reboot:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable rsyslog
        ```

2.  Configure clients for sending encrypted logs to the server:

    a.  On a client system, create a new file in the `/etc/rsyslog.d/`{.literal} directory named, for example, `securelogcli.conf`{.literal}.

    b.  Add the following lines to the `/etc/rsyslog.d/securelogcli.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        # Set certificate files
        global(
          DefaultNetstreamDriverCAFile="/etc/pki/ca-trust/source/anchors/ca-cert.pem"
          DefaultNetstreamDriverCertFile="/etc/pki/ca-trust/source/anchors/client-cert.pem"
          DefaultNetstreamDriverKeyFile="/etc/pki/ca-trust/source/anchors/client-key.pem"
        )

        # Set up the action for all messages
        *.* action(
          type="omfwd"
          StreamDriver="ossl"
          StreamDriverMode="1"
          StreamDriverPermittedPeers="server.example.com"
          StreamDriverAuthMode="x509/name"
          target="server.example.com" port="514" protocol="tcp"
        )
        ```

        Note

        If you prefer the GnuTLS driver, use the `StreamDriver.Name="gtls"`{.literal} configuration option.

    c.  Optional: To customize the connection configuration, replace the `action`{.literal} section with the following:

        ``` {.language-plaintext tabindex="-1"}
        local1.* action(
          type="omfwd"
          StreamDriver="<driver>"
          StreamDriverMode="1"
          StreamDriverAuthMode="x509/certvalid"
          streamDriver.CAFile="/etc/rsyslog.d/<ca1>.pem"
          streamDriver.CertFile="/etc/rsyslog.d/<client1_cert>.pem"
          streamDriver.KeyFile="/etc/rsyslog.d/<client1_key>.pem"
          target="server.example.com" port="514" protocol="tcp"
          )
        ```

        -   Replace *`<driver>`{.literal}* with `ossl`{.literal} or `gtls`{.literal} depending on the driver you want to use.
        -   Replace *`<ca1>`{.literal}* with the CA certificate, *`<client1_cert>`{.literal}* with the certificate, and `<client1_key>`{.literal} with the key of the customized connection.

    d.  Save the changes to the `/etc/rsyslog.d/securelogcli.conf`{.literal} file.

    e.  Verify the syntax of the `/etc/rsyslog.conf`{.literal} file and other files in the `/etc/rsyslog.d/`{.literal} directory:

        ``` {.language-plaintext tabindex="-1"}
        # rsyslogd -N 1
        rsyslogd: version 8.1911.0-2.el8, config validation run (level 1)...
        rsyslogd: End of config validation run. Bye.
        ```

    f.  Make sure the `rsyslog`{.literal} service is running and enabled on the logging server:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl status rsyslog
        ```

    g.  Restart the `rsyslog`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart rsyslog
        ```

    h.  Optional: If Rsyslog is not enabled, ensure the `rsyslog`{.literal} service starts automatically after reboot:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable rsyslog
        ```

**Verification**

To verify that the client system sends messages to the server:

1.  On the client system, send a test message:

    ``` {.language-plaintext tabindex="-1"}
    # logger test
    ```

2.  On the server system, view the `/var/log/messages`{.literal} log, for example:

    ``` {.language-plaintext tabindex="-1"}
    # cat /var/log/remote/msg/<hostname>/root.log
    Feb 25 03:53:17 <hostname> root[6064]: test
    ```

    Where *`<hostname>`{.literal}* is the hostname of the client system. Note that the log contains the user name of the user who entered the logger command, in this case, `root`{.literal}.

**Additional resources**

-   [Configuring logging by using RHEL system roles](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/risk_reduction_and_recovery_operations/configuring-logging-by-using-rhel-system-roles)

### [5.6. Configuring a server for receiving remote logging information over UDP](#configuring-a-server-for-receiving-remote-logging-information-over-udp) {#configuring-a-server-for-receiving-remote-logging-information-over-udp .title}

Configure the Rsyslog server to receive remote logs through the high-speed UDP protocol. UDP is suitable when log loss is acceptable, offering faster transmission than TCP.

To use remote logging through UDP, configure both the server and the client. The receiving server collects and analyzes the logs sent by one or more client systems. By default, `rsyslog`{.literal} uses UDP on port `514`{.literal} to receive log information from remote systems.

**Prerequisites**

-   Rsyslog is installed on the server system.
-   You are logged in as `root`{.literal} on the server.
-   The `policycoreutils-python-utils`{.literal} package is installed for the optional step that uses the `semanage`{.literal} command.
-   The `firewalld`{.literal} service is running.

**Procedure**

1.  Optional: To use a different port for `rsyslog`{.literal} traffic than the default port `514`{.literal}:

    a.  Add the `syslogd_port_t`{.literal} SELinux type to the SELinux policy configuration, replacing *`portno`{.literal}* with the port number you want `rsyslog`{.literal} to use:

        ``` {.language-plaintext tabindex="-1"}
        # semanage port -a -t syslogd_port_t -p udp portno
        ```

    b.  Configure `firewalld`{.literal} to allow incoming `rsyslog`{.literal} traffic, replacing *`portno`{.literal}* with the port number and `zone`{.literal} with the zone you want `rsyslog`{.literal} to use:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --zone=zone --permanent --add-port=portno/udp
        success
        # firewall-cmd --reload
        ```

    c.  Reload the firewall rules:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --reload
        ```

2.  Create a new `.conf`{.literal} file in the `/etc/rsyslog.d/`{.literal} directory, for example, `remotelogserv.conf`{.literal}, and insert the following content:

    ``` {.language-plaintext tabindex="-1"}
    # Define templates before the rules that use them
    # Per-Host templates for remote systems
    template(name="TmplAuthpriv" type="list") {
        constant(value="/var/log/remote/auth/")
        property(name="hostname")
        constant(value="/")
        property(name="programname" SecurePath="replace")
        constant(value=".log")
        }

    template(name="TmplMsg" type="list") {
        constant(value="/var/log/remote/msg/")
        property(name="hostname")
        constant(value="/")
        property(name="programname" SecurePath="replace")
        constant(value=".log")
        }

    # Provides UDP syslog reception
    module(load="imudp")

    # This ruleset processes remote messages
    ruleset(name="remote1"){
         authpriv.*   action(type="omfile" DynaFile="TmplAuthpriv")
          *.info;mail.none;authpriv.none;cron.none
    action(type="omfile" DynaFile="TmplMsg")
    }

    input(type="imudp" port="514" ruleset="remote1")
    ```

    Where `514`{.literal} is the port number `rsyslog`{.literal} uses by default. You can specify a different port instead.

3.  Verify the syntax of the `/etc/rsyslog.conf`{.literal} file and all `.conf`{.literal} files in the `/etc/rsyslog.d/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # rsyslogd -N 1
    rsyslogd: version 8.1911.0-2.el8, config validation run...
    ```

4.  Restart the `rsyslog`{.literal} service.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart rsyslog
    ```

5.  Optional: If `rsyslog`{.literal} is not enabled, ensure the `rsyslog`{.literal} service starts automatically after reboot:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable rsyslog
    ```

**Verification**

-   To verify that the client system sends messages to the server:

    1.  On the client system, send a test message:

        ``` {.language-plaintext tabindex="-1"}
        # logger test
        ```

    2.  On the server system, view the `/var/log/messages`{.literal} log, for example:

        ``` {.language-plaintext tabindex="-1"}
        # cat /var/log/remote/msg/<hostname>/root.log
        Feb 25 03:53:17 <hostname> root[6064]: test
        ```

        Where *`<hostname>`{.literal}* is the hostname of the client system. Note that the log contains the user name of the user who entered the logger command, in this case, `root`{.literal}.

### [5.7. Configuring remote logging to a server over UDP](#configuring-remote-logging-to-a-server-over-udp) {#configuring-remote-logging-to-a-server-over-udp .title}

Configure a client system to send its logs to a remote server by using the UDP protocol. UDP is preferred when speed is critical and the occasional loss of a log message is acceptable.

The `omfwd`{.literal} plugin provides forwarding over UDP or TCP. The default protocol is UDP. Because the plugin is built in, you do not have to load it.

**Prerequisites**

-   The `rsyslog`{.literal} package is installed on the client systems that should report to the server.
-   You have configured the server for remote logging as described in [Configuring a server for receiving remote logging information over UDP](#configuring-a-server-for-receiving-remote-logging-information-over-udp "5.6. Configuring a server for receiving remote logging information over UDP").

**Procedure**

1.  Create a new `.conf`{.literal} file in the `/etc/rsyslog.d/`{.literal} directory, for example, `10-remotelogcli.conf`{.literal}, and insert the following content:

    ``` {.language-plaintext tabindex="-1"}
    *.* action(type="omfwd"
          queue.type="linkedlist"
          queue.filename="example_fwd"
          action.resumeRetryCount="-1"
          queue.saveOnShutdown="on"
          target="example.com" port="portno" protocol="udp"
         )
    ```

    Where:

    -   The `queue.type="linkedlist"`{.literal} setting enables a LinkedList in-memory queue.

    -   The `queue.filename`{.literal} setting defines a disk storage. The backup files are created with the *`example_fwd`{.literal}* prefix in the working directory specified by the preceding global `workDirectory`{.literal} directive.

    -   The `action.resumeRetryCount -1`{.literal} setting prevents `rsyslog`{.literal} from dropping messages when retrying to connect if the server is not responding.

    -   The `enabled queue.saveOnShutdown="on"`{.literal} setting saves in-memory data if `rsyslog`{.literal} shuts down.

    -   The *`portno`{.literal}* value is the port number you want `rsyslog`{.literal} to use. The default value is `514`{.literal}.

    -   The last line forwards all received messages to the logging server, port specification is optional.

        With this configuration, `rsyslog`{.literal} sends messages to the server but keeps messages in memory if the remote server is not reachable. A file on disk is created only if `rsyslog`{.literal} runs out of the configured memory queue space or needs to shut down, which benefits the system performance.

    Note

    Rsyslog processes configuration files `/etc/rsyslog.d/`{.literal} in the lexical order.

2.  Restart the `rsyslog`{.literal} service.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart rsyslog
    ```

3.  Optional: If `rsyslog`{.literal} is not enabled, ensure the `rsyslog`{.literal} service starts automatically after reboot:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable rsyslog
    ```

**Verification**

To verify that the client system sends messages to the server, follow these steps:

1.  On the client system, send a test message:

    ``` {.language-plaintext tabindex="-1"}
    # logger test
    ```

2.  On the server system, view the `/var/log/remote/msg/`{.literal}*`hostname`{.literal}*`/root.log`{.literal} log, for example:

    ``` {.language-plaintext tabindex="-1"}
    # cat /var/log/remote/msg/hostname/root.log
    Feb 25 03:53:17 hostname root[6064]: test
    ```

    Where `hostname`{.literal} is the hostname of the client system. Note that the log contains the user name of the user that entered the logger command, in this case `root`{.literal}.

### [5.8. Load balancing helper in Rsyslog](#load-balancing-helper-in-rsyslog) {#load-balancing-helper-in-rsyslog .title}

Configure the load balancing helper in Rsyslog to distribute log traffic across multiple remote logging servers. This improves system resilience and prevents any single server from becoming overwhelmed.

When used in a cluster, you can improve Rsyslog load balancing by modifying the `RebindInterval`{.literal} setting. This option specifies an interval at which the current connection is broken and is re-established. This setting applies to TCP, UDP, and RELP traffic. The load balancers perceive it as a new connection and forward the messages to another physical target system.

You can use `RebindInterval`{.literal} in scenarios when a target system changes its IP address. The Rsyslog application caches the IP address when the connection is established. Therefore, the messages are sent to the same server. If the IP address changes, the UDP packets are lost until the Rsyslog service restarts. Re-establishing the connection ensures that the IP is resolved by DNS again.

**Example 5.1. Usage of RebindInterval for TCP, UDP, and RELP traffic**

``` {.language-plaintext tabindex="-1"}
action(type="omfwd" protocol="tcp" RebindInterval="250" target="example.com" port="514" …)

action(type="omfwd" protocol="udp" RebindInterval="250" target="example.com" port="514" …)

action(type="omrelp" RebindInterval="250" target="example.com" port="6514" …)
```

### [5.9. Configuring reliable remote logging](#configuring-reliable-remote-logging) {#configuring-reliable-remote-logging .title}

Configure reliable remote logging with the Reliable Event Logging Protocol (RELP). This helps guarantee that log messages reach the central server, preventing data loss even during network outages.

With RELP, you can send and receive syslog messages over TCP with a much reduced risk of message loss. RELP reliably delivers event messages, which is useful in environments where message loss is not acceptable. To use RELP, configure the `imrelp`{.literal} input module on the server to receive logs and the `omrelp`{.literal} output module on the client to send logs.

**Prerequisites**

-   You have installed the `rsyslog`{.literal}, `librelp`{.literal}, and `rsyslog-relp`{.literal} packages on the server and the client systems.
-   The specified port is permitted in SELinux and open in the firewall.

**Procedure**

1.  Configure the client system for reliable remote logging:

    a.  On the client system, create a new `.conf`{.literal} file in the `/etc/rsyslog.d/`{.literal} directory named, for example, `relpclient.conf`{.literal}, and insert the following content:

        ``` {.language-plaintext tabindex="-1"}
        module(load="omrelp")
        *.* action(type="omrelp" target="_target_IP_" port="_target_port_")
        ```

        Where:

        -   *`target_IP`{.literal}* is the IP address of the logging server.
        -   *`target_port`{.literal}* is the port of the logging server.

    b.  Save the changes to the `/etc/rsyslog.d/relpclient.conf`{.literal} file.

    c.  Restart the `rsyslog`{.literal} service.

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart rsyslog
        ```

    d.  Optional: If `rsyslog`{.literal} is not enabled, ensure the `rsyslog`{.literal} service starts automatically after reboot:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable rsyslog
        ```

2.  Configure the server system for reliable remote logging:

    a.  On the server system, create a new `.conf`{.literal} file in the `/etc/rsyslog.d/`{.literal} directory named, for example, `relpserv.conf`{.literal}, and insert the following content:

        ``` {.language-plaintext tabindex="-1"}
        ruleset(name="relp"){
        *.* action(type="omfile" file="_log_path_")
        }

        module(load="imrelp")
        input(type="imrelp" port="_target_port_" ruleset="relp")
        ```

        Where:

        -   *`log_path`{.literal}* specifies the path for storing messages.
        -   *`target_port`{.literal}* is the port of the logging server. Use the same value as in the client configuration file.

    b.  Save the changes to the `/etc/rsyslog.d/relpserv.conf`{.literal} file.

    c.  Restart the `rsyslog`{.literal} service.

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart rsyslog
        ```

    d.  Optional: If `rsyslog`{.literal} is not enabled, ensure the `rsyslog`{.literal} service starts automatically after reboot:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable rsyslog
        ```

**Verification**

To verify that the client system sends messages to the server:

1.  On the client system, send a test message:

    ``` {.language-plaintext tabindex="-1"}
    # logger test
    ```

2.  On the server system, view the log at the specified *`log_path`{.literal}*, for example:

    ``` {.language-plaintext tabindex="-1"}
    # cat /var/log/remote/msg/hostname/root.log
    Feb 25 03:53:17 hostname root[6064]: test
    ```

    Where `hostname`{.literal} is the hostname of the client system. Note that the log contains the user name of the user who entered the logger command, in this case, `root`{.literal}.

### [5.10. Supported Rsyslog modules](#supported-rsyslog-modules) {#supported-rsyslog-modules .title}

Extend Rsyslog functionality with specific modules. These modules provide additional input, output, or configuration directives. The directives become available after you load the module. Use these modules to customize how Rsyslog processes and handles log messages.

You can list the input and output modules installed on your system by entering the following command:

``` {.language-plaintext tabindex="-1"}
# ls /usr/lib64/rsyslog/{i,o}m*
```

Install the `rsyslog-doc`{.literal} package. Then view the list of all available `rsyslog`{.literal} modules in `/usr/share/doc/rsyslog/html/configuration/modules/idx_output.html`{.literal}.

### [5.11. Configuring Netconsole to log kernel messages to a remote host](#configuring-the-netconsole-service-to-log-kernel-messages-to-a-remote-host) {#configuring-netconsole-to-log-kernel-messages-to-a-remote-host .title}

Configure the `netconsole`{.literal} service to forward kernel messages to a remote host. This helps capture critical kernel events, especially when the local system logging functions have failed.

When logging to disk or using a serial console is not possible, you can use the `netconsole`{.literal} kernel module to log kernel messages over a network. The messages are sent to a remote `rsyslog`{.literal} service.

**Prerequisites**

-   A system log service, such as Rsyslog is installed on the remote host.
-   The remote system log service is configured to receive incoming log entries from this host.

**Procedure**

1.  Install the `netconsole-service`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install netconsole-service
    ```

2.  Edit the `/etc/sysconfig/netconsole`{.literal} file and set the `SYSLOGADDR`{.literal} parameter to the IP address of the remote host:

    ``` {.language-plaintext tabindex="-1"}
    # SYSLOGADDR=192.0.2.1
    ```

3.  Enable and start the `netconsole`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now netconsole
    ```

**Verification**

-   Display the `/var/log/messages`{.literal} file on the remote system log server.

### [5.12. Additional resources](#configuring-a-remote-logging-solution_512-additional-resources) {#additional-resources-1 .title}

-   [Configuring system logging without journald or with minimized journald usage (Red Hat Knowledgebase)](https://access.redhat.com/articles/4058681)
-   [Negative effects of the RHEL default logging setup on performance and their mitigations (Red Hat Knowledgebase)](https://access.redhat.com/articles/4095141)

## [Chapter 6. Configuring logging by using RHEL system roles](#configuring-logging-by-using-rhel-system-roles) {#chapter-6.-configuring-logging-by-using-rhel-system-roles .title}

You can use the `logging`{.literal} RHEL system role to configure your local and remote hosts as logging servers in an automated fashion to collect logs from many client systems.

Logging solutions provide multiple ways of reading logs and multiple logging outputs.

For example, a logging system can receive the following inputs:

-   Local files
-   `systemd/journal`{.literal}
-   Another logging system over the network

In addition, a logging system can have the following outputs:

-   Logs stored in the local files in the `/var/log/`{.literal} directory
-   Logs sent to Elasticsearch engine
-   Logs forwarded to another logging system

With the `logging`{.literal} RHEL system role, you can combine the inputs and outputs to fit your scenario. For example, you can store `journald`{.literal} inputs in a local file while forwarding file-based inputs to another logging system.

### [6.1. Filtering local log messages by using the logging RHEL system role](#filtering-local-log-messages-by-using-the-logging-rhel-system-role) {#filtering-local-log-messages-by-using-the-logging-rhel-system-role .title}

You can use the property-based filter of the `logging`{.literal} RHEL system role to filter your local log messages based on various conditions, such as message content, facility, or severity.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Deploy the logging solution
      hosts: managed-node-01.example.com
      tasks:
        - name: Filter logs based on a specific value they contain
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.logging
          vars:
            logging_inputs:
              - name: files_input
                type: basics
            logging_outputs:
              - name: files_output0
                type: files
                property: msg
                property_op: contains
                property_value: error
                path: /var/log/errors.log
              - name: files_output1
                type: files
                property: msg
                property_op: "!contains"
                property_value: error
                path: /var/log/others.log
            logging_flows:
              - name: flow0
                inputs: [files_input]
                outputs: [files_output0, files_output1]
    ```

    The settings specified in the example playbook include the following:

    `logging_inputs`{.literal}
    :   Defines a list of logging input dictionaries. The `type: basics`{.literal} option covers inputs from `systemd`{.literal} journal or Unix socket.

    `logging_outputs`{.literal}
    :   Defines a list of logging output dictionaries. The `type: files`{.literal} option supports storing logs in the local files, usually in the `/var/log/`{.literal} directory. The `property: msg`{.literal}; `property: contains`{.literal}; and `property_value: error`{.literal} options specify that all logs that contain the `error`{.literal} string are stored in the `/var/log/errors.log`{.literal} file. The `property: msg`{.literal}; `property: !contains`{.literal}; and `property_value: error`{.literal} options specify that all other logs are put in the `/var/log/others.log`{.literal} file. You can replace the `error`{.literal} value with the string by which you want to filter.

    `logging_flows`{.literal}
    :   Defines a list of logging flow dictionaries to specify relationships between `logging_inputs`{.literal} and `logging_outputs`{.literal}. The `inputs: [files_input]`{.literal} option specifies a list of inputs, from which processing of logs starts. The `outputs: [files_output0, files_output1]`{.literal} option specifies a list of outputs, to which the logs are sent.

    For details about all variables used in the playbook and more information about `rsyslog`{.literal}, see the `/usr/share/ansible/roles/rhel-system-roles.logging/README.md`{.literal} file and `rsyslog.conf(5)`{.literal} and `syslog(3)`{.literal} manual pages on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

1.  On the managed node, test the syntax of the `/etc/rsyslog.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # rsyslogd -N 1
    rsyslogd: version 8.1911.0-6.el8, config validation run...
    rsyslogd: End of config validation run. Bye.
    ```

2.  On the managed node, verify that the system sends messages that contain the `error`{.literal} string to the log:

    a.  Send a test message:

        ``` {.language-plaintext tabindex="-1"}
        # logger error
        ```

    b.  View the `/var/log/errors.log`{.literal} log, for example:

        ``` {.language-plaintext tabindex="-1"}
        # cat /var/log/errors.log
        Aug  5 13:48:31 hostname root[6778]: error
        ```

        Where *`hostname`{.literal}* is the host name of the client system. Note that the log contains the user name of the user that entered the logger command, in this case `root`{.literal}.

### [6.2. Applying a remote logging solution by using the logging RHEL system role](#applying-a-remote-logging-solution-by-using-the-logging-rhel-system-role) {#applying-a-remote-logging-solution-by-using-the-logging-rhel-system-role .title}

You can use the `logging`{.literal} RHEL system role to configure centralized log management across multiple systems. The server receives remote input from the `remote_rsyslog`{.literal} and `remote_files`{.literal} configurations, and outputs the logs to local files in directories named by remote host names.

As a result, you can cover use cases where you need for example:

-   Centralized log management: Collecting, accessing, and managing log messages of multiple machines from a single storage point simplifies day-to-day monitoring and troubleshooting tasks. Also, this use case reduces the need to log in to individual machines to check the log messages.
-   Enhanced security: Storing log messages in one central place increases chances they are in a secure and tamper-proof environment. Such an environment makes it easier to detect and respond to security incidents more effectively and to meet audit requirements.
-   Improved efficiency in log analysis: Correlating log messages from multiple systems is important for fast troubleshooting of complex problems that span multiple machines or services. That way you can quickly analyze and cross-reference events from different sources.
-   Define the ports in the SELinux policy of the server or client system and open the firewall for those ports. The default SELinux policy includes ports 601, 514, 6514, 10514, and 20514. To use a different port, see [modify the SELinux policy on the client and server systems](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/index#customizing-the-selinux-policy-for-the-apache-http-server-in-a-non-standard-configuration).

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Deploy the logging solution
      hosts: managed-node-01.example.com
      tasks:
        - name: Configure the server to receive remote input
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.logging
          vars:
            logging_inputs:
              - name: remote_udp_input
                type: remote
                udp_ports: [ 601 ]
              - name: remote_tcp_input
                type: remote
                tcp_ports: [ 601 ]
            logging_outputs:
              - name: remote_files_output
                type: remote_files
            logging_flows:
              - name: flow_0
                inputs: [remote_udp_input, remote_tcp_input]
                outputs: [remote_files_output]

    - name: Deploy the logging solution
      hosts: managed-node-02.example.com
      tasks:
        - name: Configure the server to output the logs to local files in directories named by remote host names
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.logging
          vars:
            logging_inputs:
              - name: basic_input
                type: basics
            logging_outputs:
              - name: forward_output0
                type: forwards
                severity: info
                target: <host1.example.com>
                udp_port: 601
              - name: forward_output1
                type: forwards
                facility: mail
                target: <host1.example.com>
                tcp_port: 601
            logging_flows:
              - name: flows0
                inputs: [basic_input]
                outputs: [forward_output0, forward_output1]
    ```

    The settings specified in the first play of the example playbook include the following:

    `logging_inputs`{.literal}
    :   Defines a list of logging input dictionaries. The `type: remote`{.literal} option covers remote inputs from the other logging system over the network. The `udp_ports: [ 601 ]`{.literal} option defines a list of UDP port numbers to monitor. The `tcp_ports: [ 601 ]`{.literal} option defines a list of TCP port numbers to monitor. If both `udp_ports`{.literal} and `tcp_ports`{.literal} are set, `udp_ports`{.literal} is used and `tcp_ports`{.literal} is dropped.

    `logging_outputs`{.literal}
    :   Defines a list of logging output dictionaries. The `type: remote_files`{.literal} option makes output store logs to the local files per remote host and program name originated the logs.

    `logging_flows`{.literal}
    :   Defines a list of logging flow dictionaries to specify relationships between `logging_inputs`{.literal} and `logging_outputs`{.literal}. The `inputs: [remote_udp_input, remote_tcp_input]`{.literal} option specifies a list of inputs, from which processing of logs starts. The `outputs: [remote_files_output]`{.literal} option specifies a list of outputs, to which the logs are sent.

    The settings specified in the second play of the example playbook include the following:

    `logging_inputs`{.literal}
    :   Defines a list of logging input dictionaries. The `type: basics`{.literal} option covers inputs from `systemd`{.literal} journal or Unix socket.

    `logging_outputs`{.literal}
    :   Defines a list of logging output dictionaries. The `type: forwards`{.literal} option supports sending logs to the remote logging server over the network. The `severity: info`{.literal} option refers to log messages of informative importance. The `facility: mail`{.literal} option refers to the type of system program that is generating the log message. The `target: `{.literal}*`<host1.example.com>`{.literal}* option specifies the hostname of the remote logging server. The `udp_port: 601`{.literal}/`tcp_port: 601`{.literal} options define the UDP/TCP ports on which the remote logging server listens.

    `logging_flows`{.literal}
    :   Defines a list of logging flow dictionaries to specify relationships between `logging_inputs`{.literal} and `logging_outputs`{.literal}. The `inputs: [basic_input]`{.literal} option specifies a list of inputs, from which processing of logs starts. The `outputs: [forward_output0, forward_output1]`{.literal} option specifies a list of outputs, to which the logs are sent.

    For details about the role variables and more information about `rsyslog`{.literal}, see the `/usr/share/ansible/roles/rhel-system-roles.logging/README.md`{.literal} file and the `rsyslog.conf(5)`{.literal} and `syslog(3)`{.literal} manual pages on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

1.  On both the client and the server system, test the syntax of the `/etc/rsyslog.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # rsyslogd -N 1
    rsyslogd: version 8.1911.0-6.el8, config validation run (level 1), master config /etc/rsyslog.conf
    rsyslogd: End of config validation run. Bye.
    ```

2.  Verify that the client system sends messages to the server:

    a.  On the client system, send a test message:

        ``` {.language-plaintext tabindex="-1"}
        # logger test
        ```

    b.  On the server system, view the `/var/log/`{.literal}*`<host2.example.com>`{.literal}*`/messages`{.literal} log, for example:

        ``` {.language-plaintext tabindex="-1"}
        # cat /var/log/<host2.example.com>/messages
        Aug  5 13:48:31 <host2.example.com> root[6778]: test
        ```

        Where *`<host2.example.com>`{.literal}* is the host name of the client system. Note that the log contains the user name of the user that entered the logger command, in this case `root`{.literal}.

### [6.3. Using the logging RHEL system role with TLS](#using-the-logging-rhel-system-role-with-tls) {#using-the-logging-rhel-system-role-with-tls .title}

You can use the `logging`{.literal} RHEL system role to configure a secure transfer of log messages. One or more clients take logs from the `systemd-journal`{.literal} service and transfer them to a remote server by using TLS.

Typically, TLS for transferring logs in a remote logging solution is used when sending sensitive data over less trusted or public networks, such as the Internet. Also, by using certificates in TLS you can ensure that the client is forwarding logs to the correct and trusted server. This prevents attacks like \"man-in-the-middle\".

#### [6.3.1. Configuring client logging with TLS](#configuring-client-logging-with-tls) {#configuring-client-logging-with-tls .title}

You can use the `logging`{.literal} RHEL system role to configure logging on RHEL clients and transfer logs to a remote logging system by using TLS encryption.

The role creates a private key and a certificate. Next, it configures TLS on all hosts in the clients group in the Ansible inventory. The TLS protocol encrypts the message transmission for secure transfer of logs over the network.

Note

You do not have to call the `certificate`{.literal} RHEL system role in the playbook to create the certificate. The `logging`{.literal} RHEL system role calls it automatically when the `logging_certificates`{.literal} variable is set.

In order for the CA to be able to sign the created certificate, the managed nodes must be enrolled in an IdM domain.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.
-   The managed nodes are enrolled in an IdM domain.
-   If the logging server runs RHEL 9.2 or later with FIPS mode enabled, clients must support the Extended Master Secret (EMS) extension or use TLS 1.3. TLS 1.2 connections without EMS fail. For more information, see the Red Hat Knowledgebase solution [TLS extension \"Extended Master Secret\" enforced](https://access.redhat.com/solutions/7018256).

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configure remote logging solution by using TLS for secure transfer of logs
      hosts: managed-node-01.example.com
      tasks:
        - name: Deploying files input and forwards output with certs
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.logging
          vars:
            logging_certificates:
              - name: logging_cert
                dns: ['www.example.com']
                ca: ipa
                principal: "logging/{{ inventory_hostname }}@IDM.EXAMPLE.COM"
            logging_pki_files:
              - ca_cert: /local/path/to/ca_cert.pem
                cert: /local/path/to/logging_cert.pem
                private_key: /local/path/to/logging_cert.pem
            logging_inputs:
              - name: input_name
                type: files
                input_log_path: /var/log/containers/*.log
            logging_outputs:
              - name: output_name
                type: forwards
                target: your_target_host
                tcp_port: 514
                tls: true
                pki_authmode: x509/name
                permitted_server: 'server.example.com'
            logging_flows:
              - name: flow_name
                inputs: [input_name]
                outputs: [output_name]
    ```

    The settings specified in the example playbook include the following:

    `logging_certificates`{.literal}
    :   The value of this parameter is passed on to `certificate_requests`{.literal} in the `certificate`{.literal} RHEL system role and used to create a private key and certificate.

    `logging_pki_files`{.literal}

    :   Using this parameter, you can configure the paths and other settings that logging uses to find the CA, certificate, and key files used for TLS, specified with one or more of the following sub-parameters: `ca_cert`{.literal}, `ca_cert_src`{.literal}, `cert`{.literal}, `cert_src`{.literal}, `private_key`{.literal}, `private_key_src`{.literal}, and `tls`{.literal}.

        Note

        If you are using `logging_certificates`{.literal} to create the files on the managed node, do not use `ca_cert_src`{.literal}, `cert_src`{.literal}, and `private_key_src`{.literal}, which are used to copy files not created by `logging_certificates`{.literal}.

    `ca_cert`{.literal}
    :   Represents the path to the CA certificate file on the managed node. The default path is `/etc/pki/tls/certs/ca.pem`{.literal} and the file name is set by the user.

    `cert`{.literal}
    :   Represents the path to the certificate file on the managed node. The default path is `/etc/pki/tls/certs/server-cert.pem`{.literal} and the file name is set by the user.

    `private_key`{.literal}
    :   Represents the path to the private key file on the managed node. The default path is `/etc/pki/tls/private/server-key.pem`{.literal} and the file name is set by the user.

    `ca_cert_src`{.literal}
    :   Represents the path to the CA certificate file on the control node which is copied to the target host to the location specified by `ca_cert`{.literal}. Do not use this if using `logging_certificates`{.literal}.

    `cert_src`{.literal}
    :   Represents the path to a certificate file on the control node which is copied to the target host to the location specified by `cert`{.literal}. Do not use this if using `logging_certificates`{.literal}.

    `private_key_src`{.literal}
    :   Represents the path to a private key file on the control node which is copied to the target host to the location specified by `private_key`{.literal}. Do not use this if using `logging_certificates`{.literal}.

    `tls`{.literal}
    :   Setting this parameter to `true`{.literal} ensures secure transfer of logs over the network. If you do not want a secure wrapper, you can set `tls: false`{.literal}.

    For details about the role variables and more information about `rsyslog`{.literal}, see the `/usr/share/ansible/roles/rhel-system-roles.logging/README.md`{.literal} file and the `rsyslog.conf(5)`{.literal} and `syslog(3)`{.literal} manual pages on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

1.  On the client system, send a test message:

    ``` {.language-plaintext tabindex="-1"}
    # logger test
    ```

2.  On the server system, view the `/var/log/remote/`{.literal}*`<hostname>`{.literal}*`/`{.literal} log to verify the test message arrived:

    ``` {.language-plaintext tabindex="-1"}
    # cat /var/log/remote/<hostname>/.log*
    ```

    Where *`<hostname>`{.literal}* is the host name of the client system. The log must contain the `test`{.literal} message.

**Additional resources**

-   [Requesting certificates from a CA and creating self-signed certificates by using RHEL system roles](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/requesting-certificates-from-a-ca-and-creating-self-signed-certificates-by-using-rhel-system-roles)

#### [6.3.2. Configuring server logging with TLS](#configuring-server-logging-with-tls) {#configuring-server-logging-with-tls .title}

You can use the `logging`{.literal} RHEL system role to configure logging on RHEL servers and set them to receive logs from a remote logging system by using TLS encryption.

The role creates a private key and a certificate. Next, it configures TLS on all hosts in the server group in the Ansible inventory.

Note

You do not have to call the `certificate`{.literal} RHEL system role in the playbook to create the certificate. The `logging`{.literal} RHEL system role calls it automatically.

In order for the CA to be able to sign the created certificate, the managed nodes must be enrolled in an IdM domain.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.
-   The managed nodes are enrolled in an IdM domain.
-   If the logging server runs RHEL 9.2 or later with FIPS mode enabled, clients must support the Extended Master Secret (EMS) extension or use TLS 1.3. TLS 1.2 connections without EMS fail. For more information, see the Red Hat Knowledgebase solution [TLS extension \"Extended Master Secret\" enforced](https://access.redhat.com/solutions/7018256).

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configure remote logging solution by using TLS for secure transfer of logs
      hosts: managed-node-01.example.com
      tasks:
        - name: Deploying remote input and remote_files output with certs
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.logging
          vars:
            logging_certificates:
              - name: logging_cert
                dns: ['www.example.com']
                ca: ipa
                principal: "logging/{{ inventory_hostname }}@IDM.EXAMPLE.COM"
            logging_pki_files:
              - ca_cert: /local/path/to/ca_cert.pem
                cert: /local/path/to/logging_cert.pem
                private_key: /local/path/to/logging_cert.pem
            logging_inputs:
              - name: input_name
                type: remote
                tcp_ports: [514]
                tls: true
                permitted_clients: ['clients.example.com']
            logging_outputs:
              - name: output_name
                type: remote_files
                remote_log_path: /var/log/remote/%FROMHOST%/%PROGRAMNAME:::secpath-replace%.log
                async_writing: true
                client_count: 20
                io_buffer_size: 8192
            logging_flows:
              - name: flow_name
                inputs: [input_name]
                outputs: [output_name]
    ```

    The settings specified in the example playbook include the following:

    `logging_certificates`{.literal}
    :   The value of this parameter is passed on to `certificate_requests`{.literal} in the `certificate`{.literal} RHEL system role and used to create a private key and certificate.

    `logging_pki_files`{.literal}

    :   Using this parameter, you can configure the paths and other settings that logging uses to find the CA, certificate, and key files used for TLS, specified with one or more of the following sub-parameters: `ca_cert`{.literal}, `ca_cert_src`{.literal}, `cert`{.literal}, `cert_src`{.literal}, `private_key`{.literal}, `private_key_src`{.literal}, and `tls`{.literal}.

        Note

        If you are using `logging_certificates`{.literal} to create the files on the managed node, do not use `ca_cert_src`{.literal}, `cert_src`{.literal}, and `private_key_src`{.literal}, which are used to copy files not created by `logging_certificates`{.literal}.

    `ca_cert`{.literal}
    :   Represents the path to the CA certificate file on the managed node. The default path is `/etc/pki/tls/certs/ca.pem`{.literal} and the file name is set by the user.

    `cert`{.literal}
    :   Represents the path to the certificate file on the managed node. The default path is `/etc/pki/tls/certs/server-cert.pem`{.literal} and the file name is set by the user.

    `private_key`{.literal}
    :   Represents the path to the private key file on the managed node. The default path is `/etc/pki/tls/private/server-key.pem`{.literal} and the file name is set by the user.

    `ca_cert_src`{.literal}
    :   Represents the path to the CA certificate file on the control node which is copied to the target host to the location specified by `ca_cert`{.literal}. Do not use this if using `logging_certificates`{.literal}.

    `cert_src`{.literal}
    :   Represents the path to a certificate file on the control node which is copied to the target host to the location specified by `cert`{.literal}. Do not use this if using `logging_certificates`{.literal}.

    `private_key_src`{.literal}
    :   Represents the path to a private key file on the control node which is copied to the target host to the location specified by `private_key`{.literal}. Do not use this if using `logging_certificates`{.literal}.

    `tls`{.literal}
    :   Setting this parameter to `true`{.literal} ensures secure transfer of logs over the network. If you do not want a secure wrapper, you can set `tls: false`{.literal}.

    For details about the role variables and more information about `rsyslog`{.literal}, see the `/usr/share/ansible/roles/rhel-system-roles.logging/README.md`{.literal} file and the `rsyslog.conf(5)`{.literal} and `syslog(3)`{.literal} manual pages on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

1.  On the client system, send a test message:

    ``` {.language-plaintext tabindex="-1"}
    # logger test
    ```

2.  On the server system, view the `/var/log/remote/`{.literal}*`<hostname>`{.literal}*`/`{.literal} log to verify the test message arrived:

    ``` {.language-plaintext tabindex="-1"}
    # cat /var/log/remote/<hostname>/.log*
    ```

    Where *`<hostname>`{.literal}* is the host name of the client system. The log must contain the `test`{.literal} message.

**Additional resources**

-   [Requesting certificates from a CA and creating self-signed certificates by using RHEL system roles](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/requesting-certificates-from-a-ca-and-creating-self-signed-certificates-by-using-rhel-system-roles)

### [6.4. Using the logging RHEL system roles with RELP](#using-the-logging-rhel-system-roles-with-relp) {#using-the-logging-rhel-system-roles-with-relp .title}

You can use the `logging`{.literal} RHEL system role to configure Reliable Event Logging Protocol (RELP) between a RELP client and RELP server.

RELP is a networking protocol for data and message logging over the TCP network. It ensures reliable delivery of event messages and you can use it in environments that do not tolerate any message loss.

The RELP sender transfers log entries in the form of commands and the receiver acknowledges them after they are processed. To ensure consistency, RELP stores the transaction number to each transferred command for any kind of message recovery.

#### [6.4.1. Configuring client logging with RELP](#configuring-client-logging-with-relp) {#configuring-client-logging-with-relp .title}

You can use the `logging`{.literal} RHEL system role to configure a transfer of log messages stored locally to the remote logging system with RELP.

The RELP configuration uses Transport Layer Security (TLS) to encrypt the message transmission for secure transfer of logs over the network.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configure client-side of the remote logging solution by using RELP
      hosts: managed-node-01.example.com
      tasks:
        - name: Deploy basic input and RELP output
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.logging
          vars:
            logging_inputs:
              - name: basic_input
                type: basics
            logging_outputs:
              - name: relp_client
                type: relp
                target: logging.server.com
                port: 20514
                tls: true
                ca_cert: /etc/pki/tls/certs/ca.pem
                cert: /etc/pki/tls/certs/client-cert.pem
                private_key: /etc/pki/tls/private/client-key.pem
                pki_authmode: name
                permitted_servers:
                  - '*.server.example.com'
            logging_flows:
              - name: example_flow
                inputs: [basic_input]
                outputs: [relp_client]
    ```

    The settings specified in the example playbook include the following:

    `target`{.literal}
    :   This is a required parameter that specifies the host name where the remote logging system is running.

    `port`{.literal}
    :   Port number the remote logging system is listening.

    `tls`{.literal}

    :   Ensures secure transfer of logs over the network. If you do not want a secure wrapper you can set the `tls`{.literal} variable to `false`{.literal}. By default `tls`{.literal} parameter is set to true while working with RELP and requires key/certificates and triplets {`ca_cert`{.literal}, `cert`{.literal}, `private_key`{.literal}} or {`ca_cert_src`{.literal}, `cert_src`{.literal}, `private_key_src`{.literal}}.

        -   If the {`ca_cert_src`{.literal}, `cert_src`{.literal}, `private_key_src`{.literal}} triplet is set, the default locations `/etc/pki/tls/certs`{.literal} and `/etc/pki/tls/private`{.literal} are used as the destination on the managed node to transfer files from control node. In this case, the file names are identical to the original ones in the triplet
        -   If the {`ca_cert`{.literal}, `cert`{.literal}, `private_key`{.literal}} triplet is set, files are expected to be on the default path before the logging configuration.
        -   If both triplets are set, files are transferred from the local path on the control node to the specific path of the managed node.

    `ca_cert`{.literal}
    :   Represents the path to CA certificate. The default path is `/etc/pki/tls/certs/ca.pem`{.literal} and the file name is set by the user.

    `cert`{.literal}
    :   Represents the path to certificate. The default path is `/etc/pki/tls/certs/server-cert.pem`{.literal} and the file name is set by the user.

    `private_key`{.literal}
    :   Represents the path to the private key. The default path is `/etc/pki/tls/private/server-key.pem`{.literal} and the file name is set by the user.

    `ca_cert_src`{.literal}
    :   Represents local CA certificate file path which is copied to the managed node. If `ca_cert`{.literal} is specified, it is copied to the location.

    `cert_src`{.literal}
    :   Represents the local certificate file path which is copied to the managed node. If `cert`{.literal} is specified, it is copied to the location.

    `private_key_src`{.literal}
    :   Represents the local key file path which is copied to the managed node. If `private_key`{.literal} is specified, it is copied to the location.

    `pki_authmode`{.literal}
    :   Accepts the authentication mode as `name`{.literal} or `fingerprint`{.literal}.

    `permitted_servers`{.literal}
    :   List of servers that are allowed by the logging client to connect and send logs over TLS.

    `inputs`{.literal}
    :   List of logging input dictionary.

    `outputs`{.literal}
    :   List of logging output dictionary.

    For details about the role variables and more information about `rsyslog`{.literal}, see the `/usr/share/ansible/roles/rhel-system-roles.logging/README.md`{.literal} file and the `rsyslog.conf(5)`{.literal} and `syslog(3)`{.literal} manual pages on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

1.  On the client system, send a test message:

    ``` {.language-plaintext tabindex="-1"}
    # logger test
    ```

2.  On the server system, view the `/var/log/remote/`{.literal}*`<hostname>`{.literal}*`/`{.literal} log to verify the test message arrived:

    ``` {.language-plaintext tabindex="-1"}
    # cat /var/log/remote/<hostname>/.log*
    ```

    Where *`<hostname>`{.literal}* is the host name of the client system. The log must contain the `test`{.literal} message.

#### [6.4.2. Configuring server logging with RELP](#configuring-server-logging-with-relp) {#configuring-server-logging-with-relp .title}

You can use the `logging`{.literal} RHEL system role to configure a server for receiving log messages from the remote logging system with RELP.

The RELP configuration uses TLS to encrypt the message transmission for secure transfer of logs over the network.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configure server-side of the remote logging solution by using RELP
      hosts: managed-node-01.example.com
      tasks:
        - name: Deploying remote input and remote_files output
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.logging
          vars:
            logging_inputs:
              - name: relp_server
                type: relp
                port: 20514
                tls: true
                ca_cert: /etc/pki/tls/certs/ca.pem
                cert: /etc/pki/tls/certs/server-cert.pem
                private_key: /etc/pki/tls/private/server-key.pem
                pki_authmode: name
                permitted_clients:
                  - '*client.example.com'
            logging_outputs:
              - name: remote_files_output
                type: remote_files
            logging_flows:
              - name: example_flow
                inputs: [relp_server]
                outputs: [remote_files_output]
    ```

    The settings specified in the example playbook include the following:

    `port`{.literal}
    :   Port number the remote logging system is listening.

    `tls`{.literal}

    :   Ensures secure transfer of logs over the network. If you do not want a secure wrapper you can set the `tls`{.literal} variable to `false`{.literal}. By default `tls`{.literal} parameter is set to true while working with RELP and requires key/certificates and triplets {`ca_cert`{.literal}, `cert`{.literal}, `private_key`{.literal}} or {`ca_cert_src`{.literal}, `cert_src`{.literal}, `private_key_src`{.literal}}.

        -   If the {`ca_cert_src`{.literal}, `cert_src`{.literal}, `private_key_src`{.literal}} triplet is set, the default locations `/etc/pki/tls/certs`{.literal} and `/etc/pki/tls/private`{.literal} are used as the destination on the managed node to transfer files from control node. In this case, the file names are identical to the original ones in the triplet
        -   If the {`ca_cert`{.literal}, `cert`{.literal}, `private_key`{.literal}} triplet is set, files are expected to be on the default path before the logging configuration.
        -   If both triplets are set, files are transferred from the local path on the control node to the specific path of the managed node.

    `ca_cert`{.literal}
    :   Represents the path to CA certificate. The default path is `/etc/pki/tls/certs/ca.pem`{.literal} and the file name is set by the user.

    `cert`{.literal}
    :   Represents the path to the certificate. The default path is `/etc/pki/tls/certs/server-cert.pem`{.literal} and the file name is set by the user.

    `private_key`{.literal}
    :   Represents the path to the private key. The default path is `/etc/pki/tls/private/server-key.pem`{.literal} and the file name is set by the user.

    `ca_cert_src`{.literal}
    :   Represents local CA certificate file path which is copied to the managed node. If `ca_cert`{.literal} is specified, it is copied to the location.

    `cert_src`{.literal}
    :   Represents the local certificate file path which is copied to the managed node. If `cert`{.literal} is specified, it is copied to the location.

    `private_key_src`{.literal}
    :   Represents the local key file path which is copied to the managed node. If `private_key`{.literal} is specified, it is copied to the location.

    `pki_authmode`{.literal}
    :   Accepts the authentication mode as `name`{.literal} or `fingerprint`{.literal}.

    `permitted_clients`{.literal}
    :   List of clients that are allowed by the logging server to connect and send logs over TLS.

    `inputs`{.literal}
    :   List of logging input dictionary.

    `outputs`{.literal}
    :   List of logging output dictionary.

    For details about the role variables and more information about `rsyslog`{.literal}, see the `/usr/share/ansible/roles/rhel-system-roles.logging/README.md`{.literal} file and the `rsyslog.conf(5)`{.literal} and `syslog(3)`{.literal} manual pages on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

1.  On the client system, send a test message:

    ``` {.language-plaintext tabindex="-1"}
    # logger test
    ```

2.  On the server system, view the `/var/log/remote/`{.literal}*`<hostname>`{.literal}*`/`{.literal} log to verify the test message arrived:

    ``` {.language-plaintext tabindex="-1"}
    # cat /var/log/remote/<hostname>/.log*
    ```

    Where *`<hostname>`{.literal}* is the host name of the client system. The log must contain the `test`{.literal} message.

## [Chapter 7. Auditing the system](#auditing-the-system) {#chapter-7.-auditing-the-system .title}

Audit your system to record security-relevant events, identify potential intrusions, and verify compliance with security policies. The Linux Audit system is central to this security process.

The Audit system does not provide additional security for your system. Instead, it can detect security policy violations on your system. You can further prevent these violations by additional security measures, such as SELinux.

### [7.1. Linux Audit](#linux-audit) {#linux-audit .title}

With Linux Audit, you can track security-relevant information about your system. By following preconfigured rules, Audit generates log entries to record as much information as possible about events on your system. This information is crucial to determine the violator of the security policy.

Audit can record, for example, the following information in its log files:

-   Date and time, type, and outcome of an event
-   Sensitivity labels of subjects and objects
-   Association of an event with the identity of the user who triggered the event
-   All modifications to Audit configuration and attempts to access Audit log files
-   All uses of authentication mechanisms, such as SSH, Kerberos, and others
-   Changes to any trusted database, such as `/etc/passwd`{.literal}
-   Attempts to import or export information into or from the system
-   Include or exclude events based on user identity, subject and object labels, and other attributes

The use of the Audit system is also a requirement for several security-related certifications. Audit is designed to meet or exceed the requirements of the following certifications or compliance guides:

-   Controlled Access Protection Profile (CAPP)
-   Labeled Security Protection Profile (LSPP)
-   Rule Set Base Access Control (RSBAC)
-   National Industrial Security Program Operating Manual (NISPOM)
-   Federal Information Security Management Act (FISMA)
-   Payment Card Industry - Data Security Standard (PCI-DSS)
-   Security Technical Implementation Guides (STIG)

Audit has also been evaluated by National Information Assurance Partnership (NIAP) and Best Security Industries (BSI). You can use Audit for:

Watching file access
:   Audit can track whether a file or a directory has been accessed, modified, executed, or the file's attributes have been changed. This is useful, for example, to detect access to important files and have an Audit trail available in case one of these files is corrupted.

Monitoring system calls
:   Audit can be configured to generate a log entry every time a particular system call is used. This can be used, for example, to track changes to the system time by monitoring the `settimeofday`{.literal}, `clock_adjtime`{.literal}, and other time-related system calls.

Recording commands run by a user
:   Audit can track whether a file has been executed, so rules can be defined to record every execution of a particular command. For example, a rule can be defined for every executable in the `/bin`{.literal} directory. The resulting log entries can then be searched by user ID to generate an audit trail of executed commands per user.

Recording execution of system path names
:   Aside from monitoring file access which translates a path to an inode at rule invocation, Audit can now monitor the execution of a path even if it does not exist at rule invocation, or if the file is replaced after rule invocation. This allows rules to continue to work after upgrading a program executable or before it is even installed.

Recording security events
:   The `pam_faillock`{.literal} authentication module is capable of recording failed login attempts. Audit can be configured to record failed login attempts as well and provides additional information about the user who attempted to log in.

Searching for events
:   Audit provides the `ausearch`{.literal} utility, which can be used to filter the log entries and provide a complete audit trail based on several conditions.

Running summary reports
:   The `aureport`{.literal} utility can be used to generate, among other things, daily reports of recorded events. A system administrator can then analyze these reports and investigate suspicious activity further.

Monitoring network access
:   The `nftables`{.literal}, `iptables`{.literal}, and `ebtables`{.literal} utilities can be configured to trigger Audit events, allowing system administrators to monitor network access.

Note

Audit affects system performance depending on the amount of information collected.

### [7.2. Audit system architecture](#audit-system-architecture) {#audit-system-architecture .title}

The Audit system records security-relevant events by using user-space applications and kernel-side system call processing.

The Audit system consists of the following main parts:

Kernel-side system call processing

:   The kernel component receives system calls from user-space applications. It filters them through one of these filters: `user`{.literal}, `task`{.literal}, `fstype`{.literal}, or `exit`{.literal}.

    After a system call passes the `exclude`{.literal} filter, it is sent through one of these filters. The filter sends it to the Audit daemon based on the Audit rule configuration. The kernel component receives system calls from user-space applications and processes them through a series of filters. First, any system call can be dropped by the `exclude`{.literal} filter. Then, the system call passes through one of the following filters based on the rule type: `user`{.literal}, `task`{.literal}, `fstype`{.literal}, or `exit`{.literal}. The matching filter evaluates the Audit rule configuration and sends relevant events to the Audit daemon.

User-space applications and utilities

:   The user-space Audit daemon collects information from the kernel. It writes entries to a log file. Other Audit utilities interact with:

    -   The Audit daemon
    -   The kernel Audit component
    -   The Audit log files
    -   The `auditctl`{.literal} utility interacts with the kernel Audit component. It manages rules. It also controls settings and parameters of the event generation process.
    -   The remaining Audit utilities use the Audit log files as input. They generate output based on your requirements. For example, the `aureport`{.literal} utility generates a report of all recorded events.

    In RHEL 10, the Audit dispatcher daemon (`audisp`{.literal}) functionality is integrated in the Audit daemon (`auditd`{.literal}). Configuration files for plugins are in the `/etc/audit/plugins.d/`{.literal} directory. These plugins enable real-time analytical programs to interact with Audit events.

### [7.3. Audit settings for a secure environment](#audit-settings-for-a-secure-environment) {#audit-settings-for-a-secure-environment .title}

Configure specific audit rules and settings, such as those provided by STIG, to create a secure audit environment. This helps ensure comprehensive logging of security-relevant events.

The default `auditd`{.literal} configuration should be suitable for most environments. However, if your environment must meet strict security policies, you can change the following settings for the Audit daemon configuration in the `/etc/audit/auditd.conf`{.literal} file:

Log file settings, `log_file`{.literal}
:   The directory that holds the Audit log files (usually `/var/log/audit/`{.literal}) should reside on a separate mount point. This prevents other processes from consuming space in this directory and provides accurate detection of the remaining space for the Audit daemon.

`max_log_file`{.literal}
:   Specifies the maximum size of a single Audit log file, must be set to make full use of the available space on the partition that holds the Audit log files. The `max_log_file`{.literal} parameter specifies the maximum file size in megabytes. The value given must be numeric.

`max_log_file_action`{.literal}
:   Decides what action is taken once the limit set in `max_log_file`{.literal} is reached, should be set to `keep_logs`{.literal} to prevent Audit log files from being overwritten.

Disk space management, `space_left`{.literal}
:   Specifies the amount of free space left on the disk for which an action that is set in the `space_left_action`{.literal} parameter is triggered. Must be set to a number that gives the administrator enough time to respond and free up disk space. The `space_left`{.literal} value depends on the rate at which the Audit log files are generated. If the value of `space_left`{.literal} is specified as a whole number, it is interpreted as an absolute size in megabytes (MiB). If the value is specified as a number between 1 and 99 followed by a percentage sign (for example, 5%), the Audit daemon calculates the absolute size in megabytes based on the size of the file system containing `log_file`{.literal}.

`space_left_action`{.literal}
:   It is recommended to set the `space_left_action`{.literal} parameter to `email`{.literal} or `exec`{.literal} with an appropriate notification method.

`admin_space_left`{.literal}
:   Specifies the absolute minimum amount of free space for which an action that is set in the `admin_space_left_action`{.literal} parameter is triggered, must be set to a value that leaves enough space to log actions performed by the administrator. The numeric value for this parameter should be lower than the number for `space_left`{.literal}. You can also append a percent sign (for example, 1%) to the number to have the audit daemon calculate the number based on the disk partition size.

`admin_space_left_action`{.literal}
:   Should be set to `single`{.literal} to put the system into single-user mode and allow the administrator to free up some disk space.

Error handling and synchronization, `disk_full_action`{.literal}
:   Specifies an action that is triggered when no free space is available on the partition that holds the Audit log files, must be set to `halt`{.literal} or `single`{.literal}. This ensures that the system is either shut down or operating in single-user mode when Audit can no longer log events.

`disk_error_action`{.literal}
:   Specifies an action that is triggered in case an error is detected on the partition that holds the Audit log files, must be set to `syslog`{.literal}, `single`{.literal}, or `halt`{.literal}, depending on your local security policies regarding the handling of hardware malfunctions.

`flush`{.literal}
:   Should be set to `incremental_async`{.literal}. It works in combination with the `freq`{.literal} parameter, which determines how many records can be sent to the disk before forcing a hard synchronization with the hard drive. The `freq`{.literal} parameter should be set to `100`{.literal}. These parameters assure that Audit event data is synchronized with the log files on the disk while keeping good performance for bursts of activity.

The remaining configuration options should be set according to your local security policy.

### [7.4. Commands to start and control auditd](#starting-and-controlling-auditd) {#commands-to-start-and-control-auditd .title}

Start, stop, and control the `auditd`{.literal} service, which manages the system audit records. Maintaining this service is crucial for continuous security monitoring and recording important events.

After `auditd`{.literal} is configured, start the service to collect Audit information and store it in the log files. Use the following command as the root user to start `auditd`{.literal}:

``` {.language-plaintext tabindex="-1"}
# service auditd start
```

To configure `auditd`{.literal} to start at boot time:

``` {.language-plaintext tabindex="-1"}
# systemctl enable auditd
```

You can temporarily disable `auditd`{.literal} with the `# auditctl -e 0`{.literal} command and re-enable it with `# auditctl -e 1`{.literal}.

You can perform other actions on `auditd`{.literal} by using the `service auditd `{.literal}*`<action>`{.literal}* command, where *\<action\>* can be one of the following:

`stop`{.literal}
:   Stops `auditd`{.literal}.

`restart`{.literal}
:   Restarts `auditd`{.literal}.

`reload`{.literal} or `force-reload`{.literal}
:   Reloads the configuration of `auditd`{.literal} from the `/etc/audit/auditd.conf`{.literal} file.

`rotate`{.literal}
:   Rotates the log files in the `/var/log/audit/`{.literal} directory.

`resume`{.literal}
:   Resumes logging of Audit events after it has been previously suspended, for example, when there is not enough free space on the disk partition that holds the Audit log files.

`condrestart`{.literal} or `try-restart`{.literal}
:   Restarts `auditd`{.literal} only if it is already running.

`status`{.literal}
:   Displays the running status of `auditd`{.literal}.

Note

The `service`{.literal} command is the only way to interact with the `auditd`{.literal} daemon correctly. You must use the `service`{.literal} command so that the `auid`{.literal} value is properly recorded. You can use the `systemctl`{.literal} command only for two actions: `enable`{.literal} and `status`{.literal}.

### [7.5. Audit log entries](#audit-log-entries) {#audit-log-entries .title}

Log entries created by the Audit system provide crucial data for forensic analysis and troubleshooting.

By default, the Audit system stores log entries in the `/var/log/audit/audit.log`{.literal} file; if log rotation is enabled, rotated `audit.log`{.literal} files are stored in the same directory.

Add the following Audit rule to log every attempt to read or modify the `/etc/ssh/sshd_config`{.literal} file:

``` {.language-plaintext tabindex="-1"}
# auditctl -w /etc/ssh/sshd_config -p warx -k sshd_config
```

If the `auditd`{.literal} daemon is running, for example, using the following command creates a new event in the Audit log file:

``` {.language-plaintext tabindex="-1"}
$ cat /etc/ssh/sshd_config
```

This event in the `audit.log`{.literal} file looks as follows:

``` {.language-plaintext tabindex="-1"}
type=SYSCALL msg=audit(1364481363.243:24287): arch=c000003e syscall=2 success=no exit=-13 a0=7fffd19c5592 a1=0 a2=7fffd19c4b50 a3=a items=1 ppid=2686 pid=3538 auid=1000 uid=1000 gid=1000 euid=1000 suid=1000 fsuid=1000 egid=1000 sgid=1000 fsgid=1000 tty=pts0 ses=1 comm="cat" exe="/bin/cat" subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 key="sshd_config"
type=CWD msg=audit(1364481363.243:24287):  cwd="/home/shadowman"
type=PATH msg=audit(1364481363.243:24287): item=0 name="/etc/ssh/sshd_config" inode=409248 dev=fd:00 mode=0100600 ouid=0 ogid=0 rdev=00:00 obj=system_u:object_r:etc_t:s0  nametype=NORMAL cap_fp=none cap_fi=none cap_fe=0 cap_fver=0
type=PROCTITLE msg=audit(1364481363.243:24287) : proctitle=636174002F6574632F7373682F737368645F636F6E666967
```

The previous event consists of four records, which share the same timestamp and serial number. Records always start with the `type=`{.literal} keyword. Each record consists of several *`name`{.literal}*`=`{.literal}*`value`{.literal}* pairs separated by a white space or a comma. A detailed analysis of the previous event follows:

**Example 7.1. First Record**

`type=SYSCALL`{.literal}
:   The `type`{.literal} field contains the type of the record. In this example, the `SYSCALL`{.literal} value specifies that this record was triggered by a system call to the kernel.

`msg=audit(1364481363.243:24287):`{.literal}

:   The `msg`{.literal} field records:

    -   A timestamp and a unique ID of the record in the form `audit(`{.literal}*`time_stamp`{.literal}*`:`{.literal}*`ID`{.literal}*`)`{.literal}. Multiple records can share the same timestamp and ID if they were generated as part of the same Audit event. The timestamp is using the Unix time format - seconds since 00:00:00 UTC on 1 January 1970.
    -   Various event-specific *`name`{.literal}*`=`{.literal}*`value`{.literal}* pairs provided by the kernel or user-space applications.

`arch=c000003e`{.literal}
:   The `arch`{.literal} field contains information about the CPU architecture of the system. The value, `c000003e`{.literal}, is encoded in hexadecimal notation. When searching Audit records with the `ausearch`{.literal} command, use the `-i`{.literal} or `--interpret`{.literal} option to automatically convert hexadecimal values into their human-readable equivalents. The `c000003e`{.literal} value is interpreted as `x86_64`{.literal}.

`syscall=2`{.literal}
:   The `syscall`{.literal} field records the type of the system call that was sent to the kernel. The value, `2`{.literal}, can be matched with its human-readable equivalent in the `/usr/include/asm/unistd_64.h`{.literal} file. In this case, `2`{.literal} is the `open`{.literal} system call. Note that the `ausyscall`{.literal} utility allows you to convert system call numbers to their human-readable equivalents. Use the `ausyscall --dump`{.literal} command to display a listing of all system calls along with their numbers. For more information, see the `ausyscall`{.literal}(8) man page.

`success=no`{.literal}
:   The `success`{.literal} field records whether the system call recorded in that particular event succeeded or failed. In this case, the call did not succeed.

`exit=-13`{.literal}

:   The `exit`{.literal} field contains a value that specifies the exit code returned by the system call. This value varies for a different system call. You can interpret the value to its human-readable equivalent with the following command:

    ``` {.language-plaintext tabindex="-1"}
    # ausearch --interpret --exit -13
    ```

    Note that the previous example assumes that your Audit log contains an event that failed with exit code `-13`{.literal}.

`a0=7fffd19c5592`{.literal}, `a1=0`{.literal}, `a2=7fffd19c5592`{.literal}, `a3=a`{.literal}
:   The `a0`{.literal} to `a3`{.literal} fields record the first four arguments, encoded in hexadecimal notation, of the system call in this event. These arguments depend on the system call that is used; they can be interpreted by the `ausearch`{.literal} utility.

`items=1`{.literal}
:   The `items`{.literal} field contains the number of PATH auxiliary records that follow the syscall record.

`ppid=2686`{.literal}
:   The `ppid`{.literal} field records the Parent Process ID (PPID). In this case, `2686`{.literal} was the PPID of the parent process such as `bash`{.literal}.

`pid=3538`{.literal}
:   The `pid`{.literal} field records the Process ID (PID). In this case, `3538`{.literal} was the PID of the `cat`{.literal} process.

`auid=1000`{.literal}
:   The `auid`{.literal} field records the Audit user ID, that is the `loginuid`{.literal}. This ID is assigned to a user upon login and is inherited by every process even when the user's identity changes, for example, by switching user accounts with the `su - john`{.literal} command.

`uid=1000`{.literal}
:   The `uid`{.literal} field records the user ID of the user who started the analyzed process. The user ID can be interpreted into user names with the following command: `ausearch -i --uid `{.literal}*`UID`{.literal}*.

`gid=1000`{.literal}
:   The `gid`{.literal} field records the group ID of the user who started the analyzed process.

`euid=1000`{.literal}
:   The `euid`{.literal} field records the effective user ID of the user who started the analyzed process.

`suid=1000`{.literal}
:   The `suid`{.literal} field records the set user ID of the user who started the analyzed process.

`fsuid=1000`{.literal}
:   The `fsuid`{.literal} field records the file system user ID of the user who started the analyzed process.

`egid=1000`{.literal}
:   The `egid`{.literal} field records the effective group ID of the user who started the analyzed process.

`sgid=1000`{.literal}
:   The `sgid`{.literal} field records the set group ID of the user who started the analyzed process.

`fsgid=1000`{.literal}
:   The `fsgid`{.literal} field records the file system group ID of the user who started the analyzed process.

`tty=pts0`{.literal}
:   The `tty`{.literal} field records the terminal from which the analyzed process was invoked.

`ses=1`{.literal}
:   The `ses`{.literal} field records the session ID of the session from which the analyzed process was invoked.

`comm="cat"`{.literal}
:   Records the command-line name of the command that was used to start the analyzed process. In this case, the `cat`{.literal} command was used to trigger this Audit event.

`exe="/bin/cat"`{.literal}
:   The `exe`{.literal} field records the path to the executable that was used to start the analyzed process.

`subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023`{.literal}
:   The `subj`{.literal} field records the SELinux context with which the analyzed process was labeled at the time of execution.

`key="sshd_config"`{.literal}
:   The `key`{.literal} field records the administrator-defined string associated with the rule that generated this event in the Audit log.

**Example 7.2. Second Record**

`type=CWD`{.literal}

:   In the second record, the `type`{.literal} field value is `CWD`{.literal} - current working directory. This type is used to record the working directory from which the process that invoked the system call specified in the first record was executed.

    The purpose of this record is to record the current process's location in case a relative path winds up being captured in the associated PATH record. This way the absolute path can be reconstructed.

`msg=audit(1364481363.243:24287)`{.literal}
:   The `msg`{.literal} field holds the same timestamp and ID value as the value in the first record. The timestamp uses the Unix time format - seconds since 00:00:00 UTC on 1 January 1970.

`cwd="/home/`{.literal}*`user_name`{.literal}*`"`{.literal}
:   The `cwd`{.literal} field contains the path to the directory in which the system call was invoked.

**Example 7.3. Third Record**

`type=PATH`{.literal}
:   In the third record, the `type`{.literal} field value is `PATH`{.literal}. An Audit event contains a `PATH`{.literal}-type record for every path that is passed to the system call as an argument. In this Audit event, only one path (`/etc/ssh/sshd_config`{.literal}) was used as an argument.

`msg=audit(1364481363.243:24287):`{.literal}
:   The `msg`{.literal} field holds the same timestamp and ID value as the value in the first and second record.

`item=0`{.literal}
:   The `item`{.literal} field indicates which item, of the total number of items referenced in the `SYSCALL`{.literal} type record, the current record is. This number is zero-based; a value of `0`{.literal} means it is the first item.

`name="/etc/ssh/sshd_config"`{.literal}
:   The `name`{.literal} field records the path of the file or directory that was passed to the system call as an argument. In this case, it was the `/etc/ssh/sshd_config`{.literal} file.

`inode=409248`{.literal}

:   The `inode`{.literal} field contains the inode number associated with the file or directory recorded in this event. The following command displays the file or directory that is associated with the `409248`{.literal} inode number:

    ``` {.language-plaintext tabindex="-1"}
    # find / -inum 409248 -print
    /etc/ssh/sshd_config
    ```

`dev=fd:00`{.literal}
:   The `dev`{.literal} field specifies the minor and major ID of the device that contains the file or directory recorded in this event. In this case, the value represents the `/dev/fd/0`{.literal} device.

`mode=0100600`{.literal}
:   The `mode`{.literal} field records the file or directory permissions, encoded in numerical notation as returned by the `stat`{.literal} command in the `st_mode`{.literal} field. See the `stat(2)`{.literal} man page for more information. In this case, `0100600`{.literal} can be interpreted as `-rw-------`{.literal}, meaning that only the root user has read and write permissions to the `/etc/ssh/sshd_config`{.literal} file.

`ouid=0`{.literal}
:   The `ouid`{.literal} field records the object owner's user ID.

`ogid=0`{.literal}
:   The `ogid`{.literal} field records the object owner's group ID.

`rdev=00:00`{.literal}
:   The `rdev`{.literal} field contains a recorded device identifier for special files only. In this case, it is not used as the recorded file is a regular file.

`obj=system_u:object_r:etc_t:s0`{.literal}
:   The `obj`{.literal} field records the SELinux context with which the recorded file or directory was labeled at the time of execution.

`nametype=NORMAL`{.literal}
:   The `nametype`{.literal} field records the intent of each path record's operation in the context of a given syscall.

`cap_fp=none`{.literal}
:   The `cap_fp`{.literal} field records data related to the setting of a permitted file system-based capability of the file or directory object.

`cap_fi=none`{.literal}
:   The `cap_fi`{.literal} field records data related to the setting of an inherited file system-based capability of the file or directory object.

`cap_fe=0`{.literal}
:   The `cap_fe`{.literal} field records the setting of the effective bit of the file system-based capability of the file or directory object.

`cap_fver=0`{.literal}
:   The `cap_fver`{.literal} field records the version of the file system-based capability of the file or directory object.

**Example 7.4. Fourth Record**

`type=PROCTITLE`{.literal}
:   The `type`{.literal} field contains the type of the record. In this example, the `PROCTITLE`{.literal} value specifies that this record gives the full command-line that triggered this Audit event, triggered by a system call to the kernel.

`proctitle=636174002F6574632F7373682F737368645F636F6E666967`{.literal}
:   The `proctitle`{.literal} field records the full command-line of the command that started the analyzed process. The field is encoded in hexadecimal notation to not allow the user to influence the Audit log parser. The text decodes to the command that triggered this Audit event. When searching Audit records with the `ausearch`{.literal} command, use the `-i`{.literal} or `--interpret`{.literal} option to automatically convert hexadecimal values into their human-readable equivalents. The `636174002F6574632F7373682F737368645F636F6E666967`{.literal} value is interpreted as `cat /etc/ssh/sshd_config`{.literal}.

### [7.6. Examples of Audit rules defined with auditctl](#examples-of-audit-rules-defined-with-auditctl) {#examples-of-audit-rules-defined-with-auditctl .title}

Define Audit rules by using the `auditctl`{.literal} utility to control which system events are captured in your logs. These examples demonstrate how to monitor file access, system calls, and executable files.

The Linux Audit system operates on a set of rules that define what is captured in the log files. Audit rules can be set either on the command line by using the `auditctl`{.literal} utility or in the `/etc/audit/rules.d/`{.literal} directory.

By using the `auditctl`{.literal} command, you can control the basic functionality of the Audit system and define rules that decide which Audit events are logged. See the `auditctl(8)`{.literal} man page on your system for more information.

**Example 7.5. File-system rules**

-   To define a rule that logs all write access to, and every attribute change of, the `/etc/passwd`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # auditctl -w /etc/passwd -p wa -k passwd_changes
    ```

-   To define a rule that logs all write access to, and every attribute change of, all the files in the `/etc/selinux/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # auditctl -w /etc/selinux/ -p wa -k selinux_changes
    ```

**Example 7.6. System-call rules**

-   To define a rule that creates a log entry every time the `adjtimex`{.literal} or `settimeofday`{.literal} system calls are used by a program, and the system uses the 64-bit architecture:

    ``` {.language-plaintext tabindex="-1"}
    # auditctl -a always,exit -F arch=b64 -S adjtimex -S settimeofday -k time_change
    ```

-   To define a rule that creates a log entry every time a file is deleted or renamed by a system user whose ID is 1000 or larger:

    ``` {.language-plaintext tabindex="-1"}
    # auditctl -a always,exit -S unlink -S unlinkat -S rename -S renameat -F auid>=1000 -F auid!=4294967295 -k delete
    ```

    Note that the `-F auid!=4294967295`{.literal} option is used to exclude users whose login UID is not set.

**Example 7.7. Executable-file rules**

-   To define a rule that logs all execution of the `/bin/id`{.literal} program, enter the following command:

    ``` {.language-plaintext tabindex="-1"}
    # auditctl -a always,exit -F exe=/bin/id -F arch=b64 -S execve -k execution_bin_id
    ```

### [7.7. Audit persistent rules](#audit-persistent-rules) {#audit-persistent-rules .title}

Create persistent Audit rules by adding them to the `/etc/audit/rules.d/`{.literal} directory. This helps ensure that your monitoring configuration remains active and effective even after a system reboot.

To define Audit rules that are persistent across reboots, either include them directly in the `/etc/audit/rules.d/audit.rules`{.literal} file or use the `augenrules`{.literal} program. The `augenrules`{.literal} program reads rules from the `/etc/audit/rules.d/`{.literal} directory.

Note that the `/etc/audit/audit.rules`{.literal} file is generated whenever the `auditd`{.literal} service starts. Files in `/etc/audit/rules.d/`{.literal} use the same `auditctl`{.literal} command-line syntax to specify the rules. Empty lines and text following a hash sign (#) are ignored.

Furthermore, you can use the `auditctl`{.literal} command to read rules from a specified file by using the `-R`{.literal} option, for example:

``` {.language-plaintext tabindex="-1"}
# auditctl -R /usr/share/audit/sample-rules/30-stig.rules
```

The `augenrules`{.literal} script reads rules located in the `/etc/audit/rules.d/`{.literal} directory and compiles them into an `audit.rules`{.literal} file. This script processes all files that end with `.rules`{.literal} in a specific order based on their natural sort order. The files in this directory are organized into groups with the following meanings:

10
:   Kernel and `auditctl`{.literal} configuration

20
:   Rules that could match general rules, but you want a different match

30
:   Main rules

40
:   Optional rules

50
:   Server-specific rules

70
:   System local rules

90
:   Finalize (immutable)

Do not use all the rules at once. Plan the policy and copy individual files to `/etc/audit/rules.d/`{.literal}. For example, to set a system up in the STIG configuration, copy rules `10-base-config`{.literal}, `30-stig`{.literal}, `31-privileged`{.literal}, and `99-finalize`{.literal}.

Once you have the rules in the `/etc/audit/rules.d/`{.literal} directory, load them by running the `augenrules`{.literal} script with the `--load`{.literal} directive:

``` {.language-plaintext tabindex="-1"}
# augenrules --load
/sbin/augenrules: No change
No rules
enabled 1
failure 1
pid 742
rate_limit 0
…
```

See the `audit.rules(8)`{.literal} and `augenrules(8)`{.literal} man pages on your system for more information.

### [7.8. Pre-configured Audit rules files for compliance with standards](#pre-configured-audit-rules-files-for-compliance-with-standards) {#pre-configured-audit-rules-files-for-compliance-with-standards .title}

Use pre-configured rule files as a baseline to align your Audit system with standards such as PCI-DSS or STIG. These samples demonstrate how to structure rules to meet specific compliance requirements.

To configure Audit for compliance with a specific certification standard, such as OSPP, PCI DSS, or STIG, you can use the pre-configured rules files installed with the `audit`{.literal} package. The sample rules are located in the `/usr/share/audit/sample-rules`{.literal} directory.

Important

The Audit sample rules in the `sample-rules`{.literal} directory are not exhaustive nor up to date because security standards are dynamic and subject to change. These rules are provided only to demonstrate how Audit rules can be structured and written. They do not ensure immediate compliance with the latest security standards. To bring your system into compliance with the latest security standards according to specific security guidelines, use the [SCAP-based security compliance tools](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/scanning-the-system-for-configuration-compliance#configuration-compliance-tools-in-rhel).

`30-nispom.rules`{.literal}
:   Audit rule configuration that meets the requirements specified in the Information System Security chapter of the National Industrial Security Program Operating Manual.

`30-ospp-v42*.rules`{.literal}
:   Audit rule configuration that meets the requirements defined in the OSPP (Protection Profile for General Purpose Operating Systems) profile version 4.2.

`30-pci-dss-v31.rules`{.literal}
:   Audit rule configuration that meets the requirements set by Payment Card Industry Data Security Standard (PCI DSS) v3.1.

`30-stig.rules`{.literal}
:   Audit rule configuration that meets the requirements set by Security Technical Implementation Guides (STIG).

To use these configuration files, copy them to the `/etc/audit/rules.d/`{.literal} directory and use the `augenrules --load`{.literal} command, for example:

``` {.language-plaintext tabindex="-1"}
# cd /usr/share/audit/sample-rules/
# cp 10-base-config.rules 30-stig.rules 31-privileged.rules 99-finalize.rules /etc/audit/rules.d/
# augenrules --load
```

You can order Audit rules by using a numbering scheme. See the `/usr/share/audit/sample-rules/README-rules`{.literal} file for more information.

See the `audit.rules(7)`{.literal} man page on your system for more information.

### [7.9. Disabling augenrules](#disabling-augenrules) {#disabling-augenrules .title}

You can turn off the `augenrules`{.literal} utility, which switches Audit to use rules defined in the `/etc/audit/audit.rules`{.literal} file. This allows for a more straightforward rule management process in specific environments.

**Prerequisites**

-   You have root access to the system.
-   The `auditd`{.literal} service is installed.

**Procedure**

1.  Copy the `/usr/lib/systemd/system/auditd.service`{.literal} file to the `/etc/systemd/system/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # cp -f /usr/lib/systemd/system/auditd.service /etc/systemd/system/
    ```

2.  Edit the `/etc/systemd/system/auditd.service`{.literal} file in a text editor of your choice, for example:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/systemd/system/auditd.service
    ```

3.  Comment out the line containing `augenrules`{.literal}, and uncomment the line containing the `auditctl -R`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    #ExecStartPost=-/sbin/augenrules --load
    ExecStartPost=-/sbin/auditctl -R /etc/audit/audit.rules
    ```

4.  Reload the `systemd`{.literal} daemon to fetch changes in the `auditd.service`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

5.  Restart the `auditd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # service auditd restart
    ```

**Verification**

-   Verify that `auditd`{.literal} uses the `auditctl`{.literal} command instead of `augenrules`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # grep ExecStartPost /etc/systemd/system/auditd.service
    ExecStartPost=-/sbin/auditctl -R /etc/audit/audit.rules
    ```

**Additional resources**

-   [Auditd service restart overrides changes made to /etc/audit/audit.rules (Red Hat Knowledgebase)](https://access.redhat.com/solutions/1505033)

### [7.10. Configuring Audit to monitor software updates](#setting-up-audit-to-monitor-software-updates) {#configuring-audit-to-monitor-software-updates .title}

Configure Audit to monitor software updates and package installations by using specialized rule files. This setup generates events whenever tools such as DNF or RPM modify the system.

You can use the pre-configured rule `44-installers.rules`{.literal} to configure Audit to monitor the following utilities that install software:

-   `dnf`{.literal} [^\[1\]^](#ftn.idm140494128391376)
-   `yum`{.literal}
-   `pip`{.literal}
-   `npm`{.literal}
-   `cpan`{.literal}
-   `gem`{.literal}
-   `luarocks`{.literal}

To monitor the RPM utility, install the `rpm-plugin-audit`{.literal} package. Audit will then generate `SOFTWARE_UPDATE`{.literal} events when it installs or updates a package. You can list these events by entering `ausearch -m SOFTWARE_UPDATE`{.literal} on the command line.

Note

Pre-configured rule files cannot be used on systems with the `ppc64le`{.literal} and `aarch64`{.literal} architectures.

**Prerequisites**

-   The `auditd`{.literal} service is configured in accordance with [Section 7.3, "Audit settings for a secure environment"](#audit-settings-for-a-secure-environment "7.3. Audit settings for a secure environment").

**Procedure**

1.  Copy the pre-configured rule file `44-installers.rules`{.literal} from the `/usr/share/audit/sample-rules/`{.literal} directory to the `/etc/audit/rules.d/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # cp /usr/share/audit/sample-rules/44-installers.rules /etc/audit/rules.d/
    ```

2.  Load the audit rules:

    ``` {.language-plaintext tabindex="-1"}
    # augenrules --load
    ```

**Verification**

1.  List the loaded rules:

    ``` {.language-plaintext tabindex="-1"}
    # auditctl -l
    -p x-w /usr/bin/dnf-3 -k software-installer
    -p x-w /usr/bin/yum -k software-installer
    -p x-w /usr/bin/pip -k software-installer
    -p x-w /usr/bin/npm -k software-installer
    -p x-w /usr/bin/cpan -k software-installer
    -p x-w /usr/bin/gem -k software-installer
    -p x-w /usr/bin/luarocks -k software-installer
    ```

2.  Perform an installation, for example:

    ``` {.language-plaintext tabindex="-1"}
    # dnf reinstall -y vim-enhanced
    ```

3.  Search the Audit log for recent installation events, for example:

    ``` {.language-plaintext tabindex="-1"}
    # ausearch -ts recent -k software-installer
    &#8211;&#8211;&#8211;&#8211;
    time->Thu Dec 16 10:33:46 2021
    type=PROCTITLE msg=audit(1639668826.074:298): proctitle=2F7573722F6C6962657865632F706C6174666F726D2D707974686F6E002F7573722F62696E2F646E66007265696E7374616C6C002D790076696D2D656E68616E636564
    type=PATH msg=audit(1639668826.074:298): item=2 name="/lib64/ld-linux-x86-64.so.2" inode=10092 dev=fd:01 mode=0100755 ouid=0 ogid=0 rdev=00:00 obj=system_u:object_r:ld_so_t:s0 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
    type=PATH msg=audit(1639668826.074:298): item=1 name="/usr/libexec/platform-python" inode=4618433 dev=fd:01 mode=0100755 ouid=0 ogid=0 rdev=00:00 obj=system_u:object_r:bin_t:s0 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
    type=PATH msg=audit(1639668826.074:298): item=0 name="/usr/bin/dnf" inode=6886099 dev=fd:01 mode=0100755 ouid=0 ogid=0 rdev=00:00 obj=system_u:object_r:rpm_exec_t:s0 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
    type=CWD msg=audit(1639668826.074:298): cwd="/root"
    type=EXECVE msg=audit(1639668826.074:298): argc=5 a0="/usr/libexec/platform-python" a1="/usr/bin/dnf" a2="reinstall" a3="-y" a4="vim-enhanced"
    type=SYSCALL msg=audit(1639668826.074:298): arch=c000003e syscall=59 success=yes exit=0 a0=55c437f22b20 a1=55c437f2c9d0 a2=55c437f2aeb0 a3=8 items=3 ppid=5256 pid=5375 auid=0 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=pts0 ses=3 comm="dnf" exe="/usr/libexec/platform-python3.6" subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 key="software-installer"
    ```

\

------------------------------------------------------------------------

[^\[1\]^](#idm140494128391376) Because `dnf`{.literal} is a symlink in RHEL, the path in the `dnf`{.literal} Audit rule must include the target of the symlink. To receive correct Audit events, modify the `44-installers.rules`{.literal} file by changing the `path=/usr/bin/dnf`{.literal} path to `/usr/bin/dnf-3`{.literal}.

### [7.11. Monitoring user login times with Audit](#monitoring-user-login-times-with-audit) {#monitoring-user-login-times-with-audit .title}

Use the `ausearch`{.literal} and `aureport`{.literal} tools to monitor and display user login times and session activities. This provides a clear overview of when users access the system without requiring custom configuration.

**Prerequisites**

-   The `auditd`{.literal} service is configured in accordance with [Section 7.3, "Audit settings for a secure environment"](#audit-settings-for-a-secure-environment "7.3. Audit settings for a secure environment").

**Procedure**

1.  Search the Audit log for the `USER_LOGIN`{.literal} message type:

    ``` {.language-plaintext tabindex="-1"}
    # ausearch -m USER_LOGIN -ts '12/02/2020' '18:00:00' -sv no
    time->Mon Nov 22 07:33:22 2021
    type=USER_LOGIN msg=audit(1637584402.416:92): pid=1939 uid=0 auid=4294967295 ses=4294967295 subj=system_u:system_r:sshd_t:s0-s0:c0.c1023 msg='op=login acct="(unknown)" exe="/usr/sbin/sshd" hostname=? addr=10.37.128.108 terminal=ssh res=failed'
    ```

    -   You can specify the date and time with the `-ts`{.literal} option. If you do not use this option, `ausearch`{.literal} provides results from today, and if you omit time, `ausearch`{.literal} provides results from midnight.
    -   You can use the `-sv yes`{.literal} option to filter out successful login attempts and `-sv no`{.literal} for unsuccessful login attempts.

2.  Pipe the raw output of the `ausearch`{.literal} command into the `aulast`{.literal} utility, which displays the output in a format similar to the output of the `last`{.literal} command. For example:

    ``` {.language-plaintext tabindex="-1"}
    # ausearch --raw | aulast --stdin
    root     ssh          10.37.128.108    Mon Nov 22 07:33 - 07:33  (00:00)
    root     ssh          10.37.128.108    Mon Nov 22 07:33 - 07:33  (00:00)
    root     ssh          10.22.16.106     Mon Nov 22 07:40 - 07:40  (00:00)
    reboot   system boot  4.18.0-348.6.el8 Mon Nov 22 07:33
    ```

3.  Display the list of login events by using the `aureport`{.literal} command with the `--login -i`{.literal} options.

    ``` {.language-plaintext tabindex="-1"}
    # aureport --login -i

    Login Report
    ============================================
    # date time auid host term exe success event
    ============================================
    1. 11/16/2021 13:11:30 root 10.40.192.190 ssh /usr/sbin/sshd yes 6920
    2. 11/16/2021 13:11:31 root 10.40.192.190 ssh /usr/sbin/sshd yes 6925
    3. 11/16/2021 13:11:31 root 10.40.192.190 ssh /usr/sbin/sshd yes 6930
    4. 11/16/2021 13:11:31 root 10.40.192.190 ssh /usr/sbin/sshd yes 6935
    5. 11/16/2021 13:11:33 root 10.40.192.190 ssh /usr/sbin/sshd yes 6940
    6. 11/16/2021 13:11:33 root 10.40.192.190 /dev/pts/0 /usr/sbin/sshd yes 6945
    ```

**Verification**

-   Verify that the Audit system captures login events by searching for recent `USER_LOGIN`{.literal} messages:

    ``` {.language-plaintext tabindex="-1"}
    # ausearch -m USER_LOGIN -ts recent
    ```

    If the output returns login events, the Audit system is correctly monitoring user login times.

### [7.12. Additional resources](#auditing-the-system_712-additional-resources) {#additional-resources-2 .title}

-   [Auditd execution options in a container (Red Hat Knowledgebase)](https://access.redhat.com/articles/4494341)
-   [Linux Audit Documentation Project page (Github.com)](https://github.com/linux-audit/audit-documentation/wiki)

## [Chapter 8. Managing and monitoring security updates](#managing-and-monitoring-security-updates) {#chapter-8.-managing-and-monitoring-security-updates .title}

Install security updates and display additional details about the updates to keep your Red Hat Enterprise Linux systems secured against newly discovered threats and vulnerabilities.

### [8.1. Identifying security updates](#identifying-security-updates) {#identifying-security-updates .title}

Keeping enterprise systems secure from current and future threats requires regular security updates. Red Hat Product Security provides the guidance you need to confidently deploy and maintain enterprise solutions.

#### [8.1.1. Red Hat Security Advisories](#what-are-security-advisories) {#red-hat-security-advisories .title}

Red Hat Security Advisories (RHSA) document the information about security flaws being fixed in Red Hat products and services.

Each RHSA includes the following information:

-   Severity
-   Type and status
-   Affected products
-   Summary of fixed issues
-   Links to the tickets about the problem. Note that not all tickets are public.
-   Common Vulnerabilities and Exposures (CVE) numbers and links with additional details, such as attack complexity.

Red Hat Customer Portal provides a list of Red Hat Security Advisories published by Red Hat. You can display details of a specific advisory by navigating to the advisory's ID from the list of Red Hat Security Advisories.

**Figure 8.1. List of security advisories**

Optionally, you can also filter the results by specific product, variant, version, and architecture. For example, to display only advisories for Red Hat Enterprise Linux 10, you can set the following filters:

-   Product: Red Hat Enterprise Linux
-   Variant: All Variants
-   Version: 10
-   Optionally, select a minor version.

**Additional resources**

-   [List of Red Hat Security Advisories](https://access.redhat.com/security/security-updates)
-   [Anatomy of a Red Hat Security Advisory](https://access.redhat.com/blogs/766093/posts/1975923)

#### [8.1.2. Displaying security updates that are not installed on a host](#displaying-security-updates-that-are-not-installed-on-a-host) {#displaying-security-updates-that-are-not-installed-on-a-host .title}

Display all security updates that are currently not installed on your host system to identify critical packages that require immediate action or installation.

You can list all available security updates for your system by using the DNF utility.

**Prerequisites**

-   A Red Hat subscription is attached to the host.

**Procedure**

-   List all available security updates which have not been installed on the host:

    ``` {.language-plaintext tabindex="-1"}
    # dnf updateinfo list updates security
    …
    RHSA-2019:0997 Important/Sec. platform-python-3.6.8-2.el8_0.x86_64
    RHSA-2019:0997 Important/Sec. python3-libs-3.6.8-2.el8_0.x86_64
    RHSA-2019:0990 Moderate/Sec.  systemd-239-13.el8_0.3.x86_64
    …
    ```

#### [8.1.3. Displaying security updates that are installed on a host](#displaying-security-updates-that-are-installed-on-a-host) {#displaying-security-updates-that-are-installed-on-a-host .title}

Display security updates that are already installed on your host. This helps you verify that required fixes are applied and track your system's current security posture.

You can list installed security updates for your system by using the DNF utility.

**Prerequisites**

-   A Red Hat subscription is attached to the host.

**Procedure**

-   List all security updates which are installed on the host:

    ``` {.language-plaintext tabindex="-1"}
    # dnf updateinfo list security --installed
    …
    RHSA-2019:1234 Important/Sec. libssh2-1.8.0-7.module+el8+2833+c7d6d092
    RHSA-2019:4567 Important/Sec. python3-libs-3.6.7.1.el8.x86_64
    RHSA-2019:8901 Important/Sec. python3-libs-3.6.8-1.el8.x86_64
    …
    ```

    If multiple updates of a single package are installed, `dnf`{.literal} lists all advisories for the package. In the previous example, two security updates for the `python3-libs`{.literal} package have been installed since the system installation.

#### [8.1.4. Displaying a specific advisory by using DNF](#displaying-a-specific-advisory-by-using-dnf) {#displaying-a-specific-advisory-by-using-dnf .title}

Use the DNF utility to display detailed information about a specific security advisory. This helps you understand the related bug, its severity, and which packages are included in the fix.

**Prerequisites**

-   A Red Hat subscription is attached to the host.
-   You know the ID of the security advisory.
-   The update provided by the advisory is not installed.

**Procedure**

-   Display a specific advisory, for example:

    ``` {.language-plaintext tabindex="-1"}
    # dnf updateinfo info RHSA-2019:0997
    ====================================================================
      Important: python3 security update
    ====================================================================
      Update ID: RHSA-2019:0997
           Type: security
        Updated: 2019-05-07 05:41:52
           Bugs: 1688543 - CVE-2019-9636 python: Information Disclosure due to urlsplit improper NFKC normalization
           CVEs: CVE-2019-9636
    Description: …
    ```

### [8.2. Installing security updates](#installing-security-updates) {#installing-security-updates .title}

In Red Hat Enterprise Linux, you can install a specific security advisory and all available security updates. You can also configure the system to download and install security updates automatically.

#### [8.2.1. Installing all available security updates](#installing-all-available-security-updates) {#installing-all-available-security-updates .title}

Install all available Red Hat security updates by using the DNF utility. This helps patch all known vulnerabilities and quickly brings the system into full compliance.

**Prerequisites**

-   A Red Hat subscription is attached to the host.

**Procedure**

1.  Install security updates by using the DNF utility:

    ``` {.language-plaintext tabindex="-1"}
    # dnf update --security
    ```

    Without the `--security`{.literal} parameter, `dnf update`{.literal} installs all updates, including bug fixes and enhancements.

2.  Confirm and start the installation by pressing y:

    ``` {.language-plaintext tabindex="-1"}
    …
    Transaction Summary
    ===========================================
    Upgrade  … Packages

    Total download size: … M
    Is this ok [y/d/N]: y
    ```

3.  Optional: List processes that require a manual restart of the system after installing the updated packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf needs-restarting
    1107 : /usr/sbin/rsyslogd -n
    1199 : -bash
    ```

    The previous command lists only processes that require a restart, and not services. That is, you cannot restart processes listed by using the `systemctl`{.literal} command. For example, the `bash`{.literal} process shown in the output terminates when the user who owns it logs out.

**Verification**

-   Verify that no remaining security updates are available:

    ``` {.language-plaintext tabindex="-1"}
    # dnf updateinfo list updates security
    ```

    If the command returns no output, all available security updates are installed.

#### [8.2.2. Installing a security update provided by a specific advisory](#installing-a-security-update-provided-by-a-specific-advisory) {#installing-a-security-update-provided-by-a-specific-advisory .title}

Install a security update associated with a specific advisory ID by using the DNF utility. This enables targeted patching of critical vulnerabilities without updating all packages.

In certain situations, you should install only specific updates. For example, if a specific service can be updated without scheduling downtime, you can install security updates for that service only and install the remaining updates later.

**Prerequisites**

-   A Red Hat subscription is attached to the host.

-   You know the ID of the security advisory that you want to update.

    For more information, see the [Identifying the security advisory updates](#identifying-security-updates "8.1. Identifying security updates") section.

**Procedure**

1.  Install a specific advisory, for example:

    ``` {.language-plaintext tabindex="-1"}
    # dnf update --advisory=RHSA-2019:0997
    ```

2.  Alternatively, update to apply a specific advisory with a minimal version change by using the `dnf upgrade-minimal`{.literal} command, for example:

    ``` {.language-plaintext tabindex="-1"}
    # dnf upgrade-minimal --advisory=RHSA-2019:0997
    ```

3.  Confirm and start the installation by pressing `y`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    …
    Transaction Summary
    ===========================================
    Upgrade  … Packages

    Total download size: … M
    Is this ok [y/d/N]: y
    ```

4.  Optional: List the processes that require a manual restart of the system after installing the updated packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf needs-restarting
    1107 : /usr/sbin/rsyslogd -n
    1199 : -bash
    ```

    The previous command lists only processes that require a restart, and not services. That is, you cannot restart processes listed by using the `systemctl`{.literal} command. For example, the `bash`{.literal} process shown in the output terminates when the user who owns it logs out.

**Verification**

-   Verify that the advisory is now listed as installed:

    ``` {.language-plaintext tabindex="-1"}
    # dnf updateinfo list security --installed
    ```

    The output includes the advisory ID that you installed.

#### [8.2.3. Installing security updates automatically](#installing-security-updates-automatically) {#installing-security-updates-automatically .title}

Configure the dnf-automatic tool to download and install security updates automatically. Automating this task helps ensure that your systems remain protected against newly discovered threats without manual intervention.

See the `dnf-automatic(8)`{.literal} man page on your system for more information.

**Prerequisites**

-   A Red Hat subscription is attached to the host.
-   The `dnf-automatic`{.literal} package is installed.

**Procedure**

1.  In the `/etc/dnf/automatic.conf`{.literal} file, in the `[commands]`{.literal} section, make sure the `upgrade_type`{.literal} option is set to either `default`{.literal} or `security`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [commands]
    #  What kind of upgrade to perform:
    # default                            = all available upgrades
    # security                           = only the security upgrades
    upgrade_type = security
    ```

2.  Enable and start the systemd timer unit:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now dnf-automatic-install.timer
    ```

**Verification**

1.  Verify that the timer is enabled:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status dnf-automatic-install.timer
    ```

## [Legal Notice](#idm140494125956336) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
