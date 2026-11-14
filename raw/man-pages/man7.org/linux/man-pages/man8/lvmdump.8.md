---
{"title": "lvmdump(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lvmdump.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lvmdump(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                   |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LVMDUMP(8)               System Manager's Manual               LVMDUMP(8)

## [](#NAME)NAME

           lvmdump — Create lvm2 information dumps for diagnostic purposes

## [](#SYNOPSIS)SYNOPSIS

           lvmdump [-a] [-c] [-d directory] [-h] [-l] [-m] [-p] [-s] [-u]

## [](#DESCRIPTION)DESCRIPTION

           lvmdump is a tool to dump various information concerning LVM2.  By
           default, it creates a tarball suitable for submission along with a
           problem report.

           The content of the tarball is as follows:
           • dmsetup info
           • table of currently running processes
           • recent entries from /var/log/messages (containing system mes‐
             sages)
           • complete lvm configuration and cache (content of /etc/lvm)
           • list of device nodes present under /dev
           • list of files present /sys/block
           • list of files present /sys/devices/virtual/block
           • if enabled with -m, metadata dump will be also included
           • if enabled with -a, debug output of vgscan, pvscan and list of
             all available volume groups, physical volumes and logical vol‐
             umes will be included
           • if enabled with -l, lvmetad state if running
           • if enabled with -p, lvmpolld state if running
           • if enabled with -s, system info and context
           • if enabled with -u, udev info and context

## [](#OPTIONS)OPTIONS

           -a     Advanced collection.
                  WARNING: if lvm is already hung, then this script may hang
                  as well if -a is used.

           -d directory
                  Dump into a directory instead of tarball By default, lvm‐
                  dump will produce a single compressed tarball containing
                  all the information. Using this option, it can be instruct‐
                  ed to only produce the raw dump tree, rooted in directory.

           -h     Print help message

           -l     Include lvmetad(8) daemon dump if it is running. The dump
                  contains cached information that is currently stored in
                  lvmetad: VG metadata, PV metadata and various mappings in
                  between these metadata for quick access.

           -m     Gather LVM metadata from the PVs This option generates a
                  1:1 dump of the metadata area from all PVs visible to the
                  system, which can cause the dump to increase in size con‐
                  siderably.  However, the metadata dump may represent a
                  valuable diagnostic resource.

           -p     Include lvmpolld(8) daemon dump if it is running.  The dump
                  contains all in-progress operation currently monitored by
                  the daemon and partial history for all yet uncollected re‐
                  sults of polling operations already finished including rea‐
                  son.

           -s     Gather system info and context. Currently, this encompasses
                  info gathered by calling lsblk command and various systemd
                  info and context: overall state of systemd units present in
                  the system, more detailed status of units controlling LVM
                  functionality and the content of systemd journal for cur‐
                  rent boot.

           -u     Gather udev info and context: /etc/udev/udev.conf file,
                  udev daemon version (output of 'udevadm info --version'
                  command), udev rules currently used in the system (content
                  of /lib/udev/rules.d and /etc/udev/rules.d directory), list
                  of files in /lib/udev directory and dump of current udev
                  database content (the output of 'udevadm info --export-db'
                  command).

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           LVM_BINARY
                  The LVM2 binary to use.  Defaults to "lvm".  Sometimes you
                  might need to set this to "/bin/lvm.static", for example.

           DMSETUP_BINARY
                  The dmsetup binary to use.  Defaults to "dmsetup".

## [](#SEE_ALSO)SEE ALSO

           lvm(8), lvmpolld(8), dmsetup(8),

           udev(8), udevadm(8)

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

    Red Hat, Inc.     LVM TOOLS 2.03.42(2)-git (2026-05-15)        LVMDUMP(8)

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
