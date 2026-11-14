---
{"title": "blkdeactivate(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/blkdeactivate.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# blkdeactivate(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BLKDEACTIVATE(8)                                         BLKDEACTIVATE(8)

## [](#NAME)NAME

           blkdeactivate — utility to deactivate block devices

## [](#SYNOPSIS)SYNOPSIS

           blkdeactivate [-d dm_options] [-e] [-h] [-l lvm_options] [-m
           mpath_options] [-r mdraid_options] [-o vdo_options] [-u] [-v]
           [device]

## [](#DESCRIPTION)DESCRIPTION

           The  blkdeactivate  utility deactivates block devices. For mounted
           block devices, it attempts to unmount it automatically before try‐
           ing to deactivate. The utility  currently  supports  device-mapper
           devices  (DM), including LVM volumes and software RAID MD devices.
           LVM volumes are handled directly using  the  lvm(8)  command,  the
           rest   of  device-mapper  based  devices  are  handled  using  the
           dmsetup(8) command.  MD devices are  handled  using  the  mdadm(8)
           command.

## [](#OPTIONS)OPTIONS

           -d|--dmoptions dm_options
                  Comma separated list of device-mapper specific options.
                  Accepted dmsetup(8) options are:

                  retry  Retry removal several times in case of failure.

                  force  Force device removal.

           -e|--errors
                  Show errors reported from tools called by blkdeactivate.
                  Without this option, any error messages from these external
                  tools are suppressed and the blkdeactivate itself provides
                  only a summary message to indicate the device was skipped.

           -h|--help
                  Display the help text.

           -l|--lvmoptions lvm_options
                  Comma-separated list of LVM specific options:

                  retry  Retry removal several times in case of failure.

                  wholevg
                         Deactivate the whole LVM Volume Group when process‐
                         ing a Logical Volume.  Deactivating the Volume Group
                         as a whole is quicker than deactivating each Logical
                         Volume separately.

           -r|--mdraidoptions mdraid_options
                  Comma-separated list of MD RAID specific options:

                  wait   Wait MD device's resync, recovery or reshape action
                         to complete before deactivation.

           -m|--mpathoptions mpath_options
                  Comma-separated list of device-mapper multipath specific
                  options:

                  disablequeueing
                         Disable queueing on all multipath devices before de‐
                         activation.  This avoids a situation where blkdeac‐
                         tivate may end up waiting if all the paths are un‐
                         available for any underlying device-mapper multipath
                         device.

           -o|--vdooptions vdo_options
                  Comma-separated list of VDO specific options:

                  configfile=file
                         Use specified VDO configuration file.

           -u|--umount
                  Unmount a mounted device before trying to deactivate it.
                  Without this option used, a device that is mounted is not
                  deactivated.

           -v, --verbose
                  Run in verbose mode. Use -vv for even more verbose mode.

## [](#EXAMPLES)EXAMPLES

           Deactivate all supported block devices found in the system, skip‐
           ping mounted devices.
           # blkdeactivate

           Deactivate all supported block devices found in the system, un‐
           mounting any mounted devices first, if possible.
           # blkdeactivate -u

           Deactivate the device /dev/vg/lvol0 together with all its holders,
           unmounting any mounted devices first, if possible.
           # blkdeactivate -u /dev/vg/lvol0

           Deactivate all supported block devices found in the system. If the
           deactivation of a device-mapper device fails, retry it. Deactivate
           the whole Volume Group at once when processing an LVM Logical Vol‐
           ume.
           # blkdeactivate -u -d retry -l wholevg

           Deactivate all supported block devices found in the system. If the
           deactivation of a device-mapper device fails, retry it and force
           removal.
           # blkdeactivate -d force,retry

## [](#SEE_ALSO)SEE ALSO

           dmsetup(8), lsblk(8), lvm(8), mdadm(8), multipathd(8), vdo(8),
           umount(8)

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

    Red Hat, Inc      LVM TOOLS 2.03.15(2)-git (2021-10-20)  BLKDEACTIVATE(8)

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
