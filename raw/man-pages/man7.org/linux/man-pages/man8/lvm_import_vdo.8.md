---
{"title": "lvm_import_vdo(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lvm_import_vdo.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lvm_import_vdo(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [EXAMPLES](#EXAMPLES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LVM_IMPORT_VDO(8)        System Manager's Manual        LVM_IMPORT_VDO(8)

## [](#NAME)NAME

           lvm_import_vdo — Utility to import VDO volumes into a new volume
           group

## [](#SYNOPSIS)SYNOPSIS

           lvm_import_vdo [options] device

## [](#DESCRIPTION)DESCRIPTION

           lvm_import_vdo utility imports VDO volumes created and managed by
           vdo(8) manager into lvm2(8) managed VDO LV. This is realized by
           moving VDO superblock by 2MiB and creating lvm2 metadata at the
           front of this device.  The operation is not reversible, thus after
           conversion to lvm2 the access to VDO data is only possible with
           lvm2(8) commands, vdo(8) manager no longer control such volume.

## [](#OPTIONS)OPTIONS

           -f|--force
                  Bypass some sanity checks.

           -h|--help
                  Display the help text.

           -n|--name
                  Specifies the name of converted VDO LV. When the name is
                  not specified, some automatic name is selected. In case the
                  converted VDO volume is already using an LV as a backend
                  device, the name of this LV is used for VDO LV.  In this
                  case also the name of the volume group must stay the same.
                  Automatic name may change between releases and currently
                  selects "vdolv" as LV name and VG name is selected from
                  sequence "vdovg", "vdovg1", ...

           -v|--verbose
                  Be more verbose.

           -y|--yes
                  Answer "yes" at any prompts.

           --dry-run
                  Print verbosely commands without running them.

           --no-snapshot
                  With this option conversion tool will not use snapshot (COW
                  storage) for conversion in your $TMPDIR filesystem and it
                  will directly manipulate with VDO device in-place.
                  Warning: the snapshot usage makes the whole conversion
                  transactional and the snapshot can be just simply merged
                  once the whole conversion has successfully proceeded. In
                  the case of error the snapshot is just removed.  Without
                  the use of snapshot there is higher risk of problems with
                  recoverability in case some unexpected error occurs.

           --vdo-config
                  Configuration file for VDO manager.  Can be used to specify
                  configuration for vdo manager.

## [](#DIAGNOSTICS)DIAGNOSTICS

           On successful completion, the status code is 0.  A status code of
           1 is used for failure.

## [](#EXAMPLES)EXAMPLES

           Convert VDO volume created by vdo manager into logical volume LV1
           within volume group VG1.

           # lvm_import_vdo --name VG1/LV1 /dev/mapper/vdo-volume

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           TMPDIR The temporary directory name for mount points. Defaults to
                  "/tmp".

           DM_DEV_DIR
                  The device directory name.  Defaults to "/dev" and must be
                  an absolute path.

           DM_UUID_PREFIX
                  Specify uuid prefix for snapshot volume used during vdo
                  conversion.

           LVM_BINARY
                  Allow to override command called from lvm. Defaults to
                  "lvm".

           VDO_BINARY
                  Allow to override command called from vdo. Defaults to
                  "vdo".

## [](#SEE_ALSO)SEE ALSO

           lvm(8), lvm.conf(5),

           vdo(8)

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

    Red Hat, Inc.     LVM TOOLS 2.03.42(2)-git (2026-05-15) LVM_IMPORT_VDO(8)

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
