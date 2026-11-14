---
{"title": "btrfs-replace(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/btrfs-replace.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# btrfs-replace(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SUBCOMMAND](#SUBCOMMAND) \| [EXAMPLES](#EXAMPLES) \| [EXIT STATUS](#EXIT_STATUS) \| [AVAILABILITY](#AVAILABILITY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                               |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BTRFS-REPLACE(8)               Btrfs Manual              BTRFS-REPLACE(8)

## [](#NAME)NAME

           btrfs-replace - replace devices managed by btrfs with other
           device.

## [](#SYNOPSIS)SYNOPSIS

           btrfs replace <subcommand> <args>

## [](#DESCRIPTION)DESCRIPTION

           btrfs replace is used to replace btrfs managed devices with other
           device.

## [](#SUBCOMMAND)SUBCOMMAND

           cancel <mount_point>
               Cancel a running device replace operation.

           start [options] <srcdev>|<devid> <targetdev> <path>
               Replace device of a btrfs filesystem.

               On a live filesystem, duplicate the data to the target device
               which is currently stored on the source device. If the source
               device is not available anymore, or if the -r option is set,
               the data is built only using the RAID redundancy mechanisms.
               After completion of the operation, the source device is
               removed from the filesystem. If the <srcdev> is a numerical
               value, it is assumed to be the device id of the filesystem
               which is mounted at <path>, otherwise it is the path to the
               source device. If the source device is disconnected, from the
               system, you have to use the devid parameter format. The
               <targetdev> needs to be same size or larger than the <srcdev>.

                   Note
                   the filesystem has to be resized to fully take advantage
                   of a larger target device; this can be achieved with btrfs
                   filesystem resize <devid>:max /path
               Options

               -r
                   only read from <srcdev> if no other zero-defect mirror
                   exists. (enable this if your drive has lots of read
                   errors, the access would be very slow)

               -f
                   force using and overwriting <targetdev> even if it looks
                   like it contains a valid btrfs filesystem.

                   A valid filesystem is assumed if a btrfs superblock is
                   found which contains a correct checksum. Devices that are
                   currently mounted are never allowed to be used as the
                   <targetdev>.

               -B
                   no background replace.

               --enqueue
                   wait if there’s another exclusive operation running,
                   otherwise continue

               -K|--nodiscard
                   Do not perform whole device TRIM operation on devices that
                   are capable of that. This does not affect discard/trim
                   operation when the filesystem is mounted. Please see the
                   mount option discard for that in btrfs(5).

           status [-1] <mount_point>
               Print status and progress information of a running device
               replace operation.

               Options

               -1
                   print once instead of print continuously until the replace
                   operation finishes (or is cancelled)

## [](#EXAMPLES)EXAMPLES

           Example 1. Replacing an online drive with a bigger one

           Given the following filesystem mounted at /mnt/my-vault

               Label: 'MyVault'  uuid: ae20903e-b72d-49ba-b944-901fc6d888a1
                       Total devices 2 FS bytes used 1TiB
                       devid    1 size 1TiB used 500.00GiB path /dev/sda
                       devid    2 size 1TiB used 500.00GiB path /dev/sdb

           In order to replace /dev/sda (devid 1) with a bigger drive located
           at /dev/sdc you would run the following:

               btrfs replace start 1 /dev/sdc /mnt/my-vault/

           You can monitor progress via:

               btrfs replace status /mnt/my-vault/

           After the replacement is complete, as per the docs at
           btrfs-filesystem(8) in order to use the entire storage space of
           the new drive you need to run:

               btrfs filesystem resize 1:max /mnt/my-vault/

## [](#EXIT_STATUS)EXIT STATUS

           btrfs replace returns a zero exit status if it succeeds. Non zero
           is returned in case of failure.

## [](#AVAILABILITY)AVAILABILITY

           btrfs is part of btrfs-progs. Please refer to the btrfs wiki
           http://btrfs.wiki.kernel.org for further details.

## [](#SEE_ALSO)SEE ALSO

           mkfs.btrfs(8), btrfs-device(8), btrfs-filesystem(8),

## [](#COLOPHON)COLOPHON

           This page is part of the btrfs-progs (btrfs filesystem tools)
           project.  Information about the project can be found at 
           ⟨https://btrfs.wiki.kernel.org/index.php/Btrfs_source_repositories⟩.
           If you have a bug report for this manual page, see
           ⟨https://btrfs.wiki.kernel.org/index.php/Problem_FAQ#How_do_I_report_bugs_and_issues.3F⟩.
           This page was obtained from the project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/linux/kernel/git/kdave/btrfs-progs.git⟩
           on 2026-08-03.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-05-10.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    Btrfs v5.16.1                   02/06/2022               BTRFS-REPLACE(8)

------------------------------------------------------------------------

Pages that refer to this page: [btrfs(8)](../man8/btrfs.8.html),  [btrfs-device(8)](../man8/btrfs-device.8.html)

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
