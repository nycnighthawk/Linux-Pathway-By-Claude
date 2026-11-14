---
{"title": "eject(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/eject.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# eject(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                      |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    EJECT(1)                      User Commands                      EJECT(1)

## [](#NAME)NAME

           eject - eject removable media

## [](#SYNOPSIS)SYNOPSIS

           eject [options] device|mountpoint

## [](#DESCRIPTION)DESCRIPTION

           eject allows removable media (typically a CD-ROM, floppy disk,
           tape, JAZ, ZIP or USB disk) to be ejected under software control.
           The command can also control some multi-disc CD-ROM changers, the
           auto-eject feature supported by some devices, and close the disc
           tray of some CD-ROM drives.

           The device corresponding to device or mountpoint is ejected. If no
           name is specified, the default name /dev/cdrom is used. The device
           may be addressed by device name (e.g., 'sda'), device path (e.g.,
           '/dev/sda'), UUID=uuid or LABEL=label tags.

           There are four different methods of ejecting, depending on whether
           the device is a CD-ROM, SCSI device, removable floppy, or tape. By
           default eject tries all four methods in order until it succeeds.

           If a device partition is specified, the whole-disk device is used.

           If the device or a device partition is currently mounted, it is
           unmounted before ejecting. The eject is processed on exclusive
           open block device file descriptor if --no-unmount or --force are
           not specified.

## [](#OPTIONS)OPTIONS

           -a, --auto on|off
               This option controls the auto-eject mode, supported by some
               devices. When enabled, the drive automatically ejects when the
               device is closed.

           -c, --changerslot slot
               With this option a CD slot can be selected from an ATAPI/IDE
               CD-ROM changer. The CD-ROM drive cannot be in use (mounted
               data CD or playing a music CD) for a change request to work.
               Please also note that the first slot of the changer is
               referred to as 0, not 1.

           -d, --default
               List the default device name.

           -F, --force
               Force eject, don’t check device type, don’t open device with
               exclusive lock. The successful result may be false positive on
               non hot-pluggable devices.

           -f, --floppy
               This option specifies that the drive should be ejected using a
               removable floppy disk eject command.

           -i, --manualeject on|off
               This option controls locking of the hardware eject button.
               When enabled, the drive will not be ejected when the button is
               pressed. This is useful when you are carrying a laptop in a
               bag or case and don’t want it to eject if the button is
               inadvertently pressed.

           -M, --no-partitions-unmount
               The option tells eject to not try to unmount other partitions
               on partitioned devices. If another partition is still mounted,
               the program will not attempt to eject the media. It will
               attempt to unmount only the device or mountpoint given on the
               command line.

           -m, --no-unmount
               The option tells eject to not try to unmount at all. If this
               option is not specified then eject opens the device with
               O_EXCL flag to be sure that the device is not used (since
               v2.35).

           -n, --noop
               With this option the selected device is displayed but no
               action is performed.

           -p, --proc
               This option allows you to use /proc/mounts instead /etc/mtab.
               It also passes the -n option to umount(8).

           -q, --tape
               This option specifies that the drive should be ejected using a
               tape drive offline command.

           -r, --cdrom
               This option specifies that the drive should be ejected using a
               CDROM eject command.

           -s, --scsi
               This option specifies that the drive should be ejected using
               SCSI commands.

           -T, --traytoggle
               With this option the drive is given a CD-ROM tray close
               command if it’s opened, and a CD-ROM tray eject command if
               it’s closed. Not all devices support this command, because it
               uses the above CD-ROM tray close command.

           -t, --trayclose
               With this option the drive is given a CD-ROM tray close
               command. Not all devices support this command.

           -v, --verbose
               Run in verbose mode; more information is displayed about what
               the command is doing.

           -X, --listspeed
               With this option the CD-ROM drive will be probed to detect the
               available speeds. The output is a list of speeds which can be
               used as an argument of the -x option. This only works with
               Linux 2.6.13 or higher, on previous versions solely the
               maximum speed will be reported. Also note that some drives may
               not correctly report the speed and therefore this option does
               not work with them.

           -x, --cdspeed speed
               With this option the drive is given a CD-ROM select speed
               command. The speed argument is a number indicating the desired
               speed (e.g., 8 for 8X speed), or 0 for maximum data rate. Not
               all devices support this command and you can only specify
               speeds that the drive is capable of. Every time the media is
               changed this option is cleared. This option can be used alone,
               or with the -t and -c options.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXIT_STATUS)EXIT STATUS

           Returns 0 if operation was successful, 1 if operation failed or
           command syntax was not valid.

## [](#NOTES)NOTES

           eject only works with devices that support one or more of the four
           methods of ejecting. This includes most CD-ROM drives (IDE, SCSI,
           and proprietary), some SCSI tape drives, JAZ drives, ZIP drives
           (parallel port, SCSI, and IDE versions), and LS120 removable
           floppies. Users have also reported success with floppy drives on
           Sun SPARC and Apple Macintosh systems. If eject does not work, it
           is most likely a limitation of the kernel driver for the device
           and not the eject program itself.

           The -r, -s, -f, and -q options allow controlling which methods are
           used to eject. More than one method can be specified. If none of
           these options are specified, it tries all four (this works fine in
           most cases).

           eject may not always be able to determine if the device is mounted
           (e.g., if it has several names). If the device name is a symbolic
           link, eject will follow the link and use the device that it points
           to.

           If eject determines that the device can have multiple partitions,
           it will attempt to unmount all mounted partitions of the device
           before ejecting (see also --no-partitions-unmount). If an unmount
           fails, the program will not attempt to eject the media.

           You can eject an audio CD. Some CD-ROM drives will refuse to open
           the tray if the drive is empty. Some devices do not support the
           tray close command.

           If the auto-eject feature is enabled, then the drive will always
           be ejected after running this command. Not all Linux kernel CD-ROM
           drivers support the auto-eject mode. There is no way to find out
           the state of the auto-eject mode.

           You need appropriate privileges to access the device files.
           Running as root is required to eject some devices (e.g., SCSI
           devices).

## [](#AUTHORS)AUTHORS

           Jeff Tranter <tranter@pobox.com> - original author, Karel Zak
           <kzak@redhat.com> and Michal Luscon <mluscon@redhat.com> -
           util-linux version.

## [](#SEE_ALSO)SEE ALSO

           findmnt(8), lsblk(8), mount(8), umount(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The eject command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                       EJECT(1)

------------------------------------------------------------------------

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
