---
{"title": "lvmlockctl(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lvmlockctl.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lvmlockctl(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [USAGE](#USAGE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LVMLOCKCTL(8)            System Manager's Manual            LVMLOCKCTL(8)

## [](#NAME)NAME

           lvmlockctl — Control for lvmlockd

## [](#SYNOPSIS)SYNOPSIS

           lvmlockctl [options]

## [](#DESCRIPTION)DESCRIPTION

           This command interacts with lvmlockd(8).

## [](#OPTIONS)OPTIONS

           -h|--help
                  Show this help information.

           -q|--quit
                  Tell lvmlockd to quit.

           -i|--info
                  Print lock state information from lvmlockd.

           -d|--dump
                  Print log buffer from lvmlockd.

           -w|--wait 0|1
                  Wait option for other commands.

           -f|--force 0|1
                  Force option for other commands.

           -k|--kill vgname
                  Kill access to the VG when sanlock cannot renew lease.

           -r|--drop vgname
                  Clear locks for the VG when it is unused after kill (-k).

           -E|--gl-enable vgname
                  Tell lvmlockd to enable the global lock in a sanlock VG.

           -D|--gl-disable vgname
                  Tell lvmlockd to disable the global lock in a sanlock VG.

           -S|--stop-lockspaces
                  Stop all lockspaces.

## [](#USAGE)USAGE

           --info This collects and displays lock state from lvmlockd.  The
                  display is primitive, incomplete and may change in future
                  versions.  To print the raw info lines from lvmlockd,
                  combine this option with --dump|-d.  Each VG lockspace may
                  include lines with prefixes: "VG" for volume group info,
                  "LS" for lockspace info, "PR" for persistent reservation
                  fencing info, "LK" for lock info, "LW" for waiting lock
                  info.

           --dump This collects the circular log buffer of debug statements
                  from lvmlockd and prints it.

           --kill This is run by sanlock when it loses access to the storage
                  holding leases for a VG.  It runs the command specified in
                  lvm.conf lvmlockctl_kill_command to deactivate LVs in the
                  VG.  If the specified command is successful, locks will be
                  dropped for the VG in lvmlockd (the equivalent of
                  lvmlockctl --drop will be run.)  If no command is
                  specified, or the command fails, then the user must
                  intervene to forcefully deactivate LVs in the VG, and if
                  successful, run lvmlockctl --drop.  For more, see
                  lvmlockd(8).

           --drop This should only be run after a VG has been successfully
                  deactivated following an lvmlockctl --kill command.  It
                  clears the stale lockspace from lvmlockd.  When
                  lvmlockctl_kill_command is used, the --kill command may run
                  drop automatically.  For more, see lvmlockd(8).

           --gl-enable
                  This enables the global lock in a sanlock VG.  This is
                  necessary if the VG that previously held the global lock is
                  removed.  For more, see lvmlockd(8).

           --gl-disable
                  This disables the global lock in a sanlock VG.  This is
                  necessary if the global lock has mistakenly been enabled in
                  more than one VG.  The global lock should be disabled in
                  all but one sanlock VG.  For more, see lvmlockd(8).

           --stop-lockspaces
                  This tells lvmlockd to stop all lockspaces.  It can be
                  useful to stop lockspaces for VGs that the vgchange
                  --lock-stop command can no longer see, or to stop the dlm
                  global lockspace which is not directly stopped by the
                  vgchange command.  The wait and force options can be used
                  with this command.

## [](#SEE_ALSO)SEE ALSO

           lvm(8), lvmlockd(8)

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

    Red Hat, Inc.     LVM TOOLS 2.03.42(2)-git (2026-05-15)     LVMLOCKCTL(8)

------------------------------------------------------------------------

Pages that refer to this page: [lvchange(8)](../man8/lvchange.8.html),  [lvconvert(8)](../man8/lvconvert.8.html),  [lvcreate(8)](../man8/lvcreate.8.html),  [lvdisplay(8)](../man8/lvdisplay.8.html),  [lvextend(8)](../man8/lvextend.8.html),  [lvm(8)](../man8/lvm.8.html),  [lvmconfig(8)](../man8/lvmconfig.8.html),  [lvmdevices(8)](../man8/lvmdevices.8.html),  [lvmdiskscan(8)](../man8/lvmdiskscan.8.html),  [lvm-fullreport(8)](../man8/lvm-fullreport.8.html),  [lvmlockd(8)](../man8/lvmlockd.8.html),  [lvm-lvpoll(8)](../man8/lvm-lvpoll.8.html),  [lvreduce(8)](../man8/lvreduce.8.html),  [lvremove(8)](../man8/lvremove.8.html),  [lvrename(8)](../man8/lvrename.8.html),  [lvresize(8)](../man8/lvresize.8.html),  [lvs(8)](../man8/lvs.8.html),  [lvscan(8)](../man8/lvscan.8.html),  [pvchange(8)](../man8/pvchange.8.html),  [pvck(8)](../man8/pvck.8.html),  [pvcreate(8)](../man8/pvcreate.8.html),  [pvdisplay(8)](../man8/pvdisplay.8.html),  [pvmove(8)](../man8/pvmove.8.html),  [pvremove(8)](../man8/pvremove.8.html),  [pvresize(8)](../man8/pvresize.8.html),  [pvs(8)](../man8/pvs.8.html),  [pvscan(8)](../man8/pvscan.8.html),  [vgcfgbackup(8)](../man8/vgcfgbackup.8.html),  [vgcfgrestore(8)](../man8/vgcfgrestore.8.html),  [vgchange(8)](../man8/vgchange.8.html),  [vgck(8)](../man8/vgck.8.html),  [vgconvert(8)](../man8/vgconvert.8.html),  [vgcreate(8)](../man8/vgcreate.8.html),  [vgdisplay(8)](../man8/vgdisplay.8.html),  [vgexport(8)](../man8/vgexport.8.html),  [vgextend(8)](../man8/vgextend.8.html),  [vgimport(8)](../man8/vgimport.8.html),  [vgimportclone(8)](../man8/vgimportclone.8.html),  [vgimportdevices(8)](../man8/vgimportdevices.8.html),  [vgmerge(8)](../man8/vgmerge.8.html),  [vgmknodes(8)](../man8/vgmknodes.8.html),  [vgreduce(8)](../man8/vgreduce.8.html),  [vgremove(8)](../man8/vgremove.8.html),  [vgrename(8)](../man8/vgrename.8.html),  [vgs(8)](../man8/vgs.8.html),  [vgscan(8)](../man8/vgscan.8.html),  [vgsplit(8)](../man8/vgsplit.8.html)

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
