---
{"title": "Create root filesystem snapshots with LVM", "url": "https://wiki.archlinux.org/title/Create_root_filesystem_snapshots_with_LVM", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Create root filesystem snapshots with LVM

Related articles

-   [LVM](../en/LVM.html "LVM")
-   [Full system backup with tar](../en/Full_system_backup_with_tar.html "Full system backup with tar")

This article describes how to set up root filesystem LVM snapshot creation during system start. Such snapshots can be used for [full system backups](../en/Full_system_backup_with_tar.html "Full system backup with tar") with minimal downtime or testing system updates with the option to revert them.

**Note** You need a system with [LVM](../en/LVM.html "LVM") root filesystem and [systemd](../en/Systemd.html "Systemd"). Ensure that [LVM snapshots](../en/LVM.html#Snapshots "LVM") prerequisites are correctly setup.

## Configuration {#Configuration}

An AUR package is available, [make-lvm-snapshot](https://aur.archlinux.org/packages/make-lvm-snapshot/)^AUR^, which can help automate the following process. It implements similar service and target files to those included in this article. The projects [README](https://gitlab.com/Marcool04/make-lvm-snapshot) contains important setup information.

If you prefer a fully \"manual\" setup, you will need to write a systemd service to create a clean snapshot of the root volume during system startup.

Create:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/mk-lvm-snapshots.service
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Unit]
Description=make LVM snapshots
Requires=local-fs-pre.target
Wants=local-fs.target
DefaultDependencies=no
Conflicts=shutdown.target
After=local-fs-pre.target
Before=local-fs.target

[Install]
WantedBy=make-snapshots.target

[Service]
Type=oneshot
ExecStart=/usr/bin/lvcreate -L10G -n snap-root -s lvmvolume/root
```

Adapt the `lvcreate` command to match your root volume group and volume name. Adjust the snapshot size if necessary. If additional filesystems should be snapshotted during startup you may extend the `ExecStart` property with addtional lvcreate commands, separated with ` ; ` (consider there is a space before and after the semicolon, see [systemd.service(5) § COMMAND LINES](https://man.archlinux.org/man/systemd.service.5#COMMAND_LINES) for details).

**Note** You should test the `lvcreate` command in the running system until it works as desired. Remove the test snapshots with `lvremove`. The snapshots taken from a running system are not as consistent as snapshots taken in single user mode or during startup.

Create a new systemd target:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/make-snapshots.target
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Unit]
Description=Make Snapshots
Requires=multi-user.target
```

Adapt the base target, if `multi-user.target` is not your default target. If you want to get into your desktop, you need to change it to `graphical.target`.

[Enable](../en/Help:Reading.html#Control_of_systemd_units "Enable") `mk-lvm-snapshots.service`.

If the system is started with the new target, LVM snapshot(s) are created just after mounting the local filesystems. To get a [GRUB](../en/GRUB.html "GRUB") menu entry starting this target create `/boot/grub/custom.cfg` based on the `grub.cfg` entry for your normal startup. The kernel command line is extended to start the new `make-snapshots.target`:

    ### make snapshots ###
    menuentry 'Arch GNU/Linux, make snapshots' --class arch --class gnu-linux --class gnu --class os {
    ...
            echo    'Loading Linux core repo kernel ...'
            linux   /boot/vmlinuz-linux root=/dev/lvmvolume/root ro systemd.unit=make-snapshots.target
            echo    'Loading initial ramdisk ...'
            initrd  /boot/initramfs-linux.img
    }

Remember to adjust `custom.cfg` if `grub.cfg` changes.

After restarting the system with this grub entry `lvs` should show up the newly created snapshot.

**Tip** To get the messages of the new service, run `journalctl -u mk-lvm-snapshots.service` as root.

## Usage {#Usage}

### Backup {#Backup}

To use this functionality for a full system backup, restart your system with the snapshot creation target. Mount the snapshot volume (and further volumes, if required), preferably using the read-only (`-o`) option. Then backup your system, for example with tar as described in [Full system backup with tar](../en/Full_system_backup_with_tar.html "Full system backup with tar").

During backup you can continue to use your system normally, since all changes to your regular volumes are invisible in the snapshots. Do not forget to delete the snapshot volume after the backup---changes to your regular volume will use up space in the snapshot due to the copy-on-write operations. If the snapshot space becomes fully used, and LVM is not able to automatically grow the snapshot, LVM will deny further writes to your regular volumes or drop the snapshot, which should be avoided.

### Revert updates {#Revert_updates}

Another use for LVM snapshots is testing and reverting of updates. In this case create a snapshot for the system in a known good state and perform updates or changes afterwards.

If you want to permantly stick to the updates just drop the snapshot with *lvremove*. If you want to revert to the snapshotted state issue a `lvconvert --merge` for the snapshot. During the next restart of the system (use the default target) the snapshot is merged back into your regular volume. All changes to the volume happened after the snapshot are undone.

**Note** After merging the snapshot no longer exists. Recreate a new snapshot if further testing with rollback option is desired.
