---
{"title": "fsadm(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/fsadm.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fsadm(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [EXAMPLES](#EXAMPLES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FSADM(8)                 System Manager's Manual                 FSADM(8)

## [](#NAME)NAME

           fsadm — Utility to resize or check filesystem on a device

## [](#SYNOPSIS)SYNOPSIS

           fsadm [options] check device
           fsadm [options] resize device [new_size]

## [](#DESCRIPTION)DESCRIPTION

           The  fsadm  utility  checks  or resizes the filesystem on a device
           (which can also be a dm-crypt encrypted device).  It tries to  use
           the same API for ext2, ext3, ext4, ReiserFS and XFS filesystems.

## [](#OPTIONS)OPTIONS

           -e|--ext-offline
                  Unmount ext2/ext3/ext4 filesystem before doing resize.

           -f|--force
                  Bypass some sanity checks.

           -h|--help
                  Display the help text.

           -l|--lvresize
                  Also resize the given lvm2 logical volume. More volume man‐
                  agement functionality is provided with complementary
                  lvresize(8) and the option -r|--resizefs.

           -n|--dry-run
                  Print commands without running them.

           -v|--verbose
                  Be more verbose.

           -y|--yes
                  Answer "yes" at any prompts.

           -c|--cryptresize
                  Resize dm-crypt mapping together with filesystem detected
                  on the device.  The dm-crypt device must be recognizable by
                  cryptsetup(8).

           new_size[B|K|M|G|T|P|E]
                  Absolute number of filesystem blocks to be in the filesys‐
                  tem, or an absolute size using a suffix (in powers of
                  1024).  If new_size is not supplied, the whole device is
                  used.

## [](#DIAGNOSTICS)DIAGNOSTICS

           On successful completion, the status code is 0.  A status code of
           2 indicates the operation was interrupted by the user.  A status
           code of 3 indicates the requested check operation could not be
           performed because the filesystem is mounted and does not support
           an online fsck(8).  A status code of 1 is used for other failures.

## [](#EXAMPLES)EXAMPLES

           Resize the filesystem on logical volume /dev/vg/test to 1000 MiB.
           If /dev/vg/test contains ext2/ext3/ext4 filesystem it will be un‐
           mounted prior to the resize.  All [y/n] questions will be answered
           'y'.

           fsadm -e -y resize /dev/vg/test 1000M

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           TMPDIR The temporary directory name for mount points. Defaults to
                  "/tmp".

           DM_DEV_DIR
                  The device directory name.  Defaults to "/dev" and must be
                  an absolute path.

## [](#SEE_ALSO)SEE ALSO

           lvm(8), lvresize(8), lvm.conf(5),

           fsck(8), tune2fs(8), resize2fs(8),

           reiserfstune(8), resize_reiserfs(8),

           xfs_info(8), xfs_growfs(8), xfs_check(8),

           cryptsetup(8)

## [](#COLOPHON)COLOPHON

           This page is part of the lvm2 (Logical Volume Manager 2) project.
           Information about the project can be found at 
           ⟨http://www.sourceware.org/lvm2/⟩.  If you have a bug report for
           this manual page, see ⟨https://github.com/lvmteam/lvm2/issues⟩.
           This page was obtained from the project's upstream Git repository
           ⟨git://sourceware.org/git/lvm2.git⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Red Hat, Inc.     LVM TOOLS 2.03.42(2)-git (2026-05-15)          FSADM(8)

------------------------------------------------------------------------

Pages that refer to this page: [lvchange(8)](../man8/lvchange.8.html),  [lvconvert(8)](../man8/lvconvert.8.html),  [lvcreate(8)](../man8/lvcreate.8.html),  [lvdisplay(8)](../man8/lvdisplay.8.html),  [lvextend(8)](../man8/lvextend.8.html),  [lvm(8)](../man8/lvm.8.html),  [lvmconfig(8)](../man8/lvmconfig.8.html),  [lvmdevices(8)](../man8/lvmdevices.8.html),  [lvmdiskscan(8)](../man8/lvmdiskscan.8.html),  [lvm-fullreport(8)](../man8/lvm-fullreport.8.html),  [lvm-lvpoll(8)](../man8/lvm-lvpoll.8.html),  [lvreduce(8)](../man8/lvreduce.8.html),  [lvremove(8)](../man8/lvremove.8.html),  [lvrename(8)](../man8/lvrename.8.html),  [lvresize(8)](../man8/lvresize.8.html),  [lvs(8)](../man8/lvs.8.html),  [lvscan(8)](../man8/lvscan.8.html),  [pvchange(8)](../man8/pvchange.8.html),  [pvck(8)](../man8/pvck.8.html),  [pvcreate(8)](../man8/pvcreate.8.html),  [pvdisplay(8)](../man8/pvdisplay.8.html),  [pvmove(8)](../man8/pvmove.8.html),  [pvremove(8)](../man8/pvremove.8.html),  [pvresize(8)](../man8/pvresize.8.html),  [pvs(8)](../man8/pvs.8.html),  [pvscan(8)](../man8/pvscan.8.html),  [vgcfgbackup(8)](../man8/vgcfgbackup.8.html),  [vgcfgrestore(8)](../man8/vgcfgrestore.8.html),  [vgchange(8)](../man8/vgchange.8.html),  [vgck(8)](../man8/vgck.8.html),  [vgconvert(8)](../man8/vgconvert.8.html),  [vgcreate(8)](../man8/vgcreate.8.html),  [vgdisplay(8)](../man8/vgdisplay.8.html),  [vgexport(8)](../man8/vgexport.8.html),  [vgextend(8)](../man8/vgextend.8.html),  [vgimport(8)](../man8/vgimport.8.html),  [vgimportclone(8)](../man8/vgimportclone.8.html),  [vgimportdevices(8)](../man8/vgimportdevices.8.html),  [vgmerge(8)](../man8/vgmerge.8.html),  [vgmknodes(8)](../man8/vgmknodes.8.html),  [vgreduce(8)](../man8/vgreduce.8.html),  [vgremove(8)](../man8/vgremove.8.html),  [vgrename(8)](../man8/vgrename.8.html),  [vgs(8)](../man8/vgs.8.html),  [vgscan(8)](../man8/vgscan.8.html),  [vgsplit(8)](../man8/vgsplit.8.html)

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
