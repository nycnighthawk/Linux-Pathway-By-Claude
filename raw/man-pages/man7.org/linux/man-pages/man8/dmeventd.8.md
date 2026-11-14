---
{"title": "dmeventd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/dmeventd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dmeventd(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [LVM PLUGINS](#LVM_PLUGINS) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                  |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DMEVENTD(8)              System Manager's Manual              DMEVENTD(8)

## [](#NAME)NAME

           dmeventd — Device-mapper event daemon

## [](#SYNOPSIS)SYNOPSIS

           dmeventd [-d [-d [-d]]] [-f] [-h] [-l] [-R] [-V] [-?]

## [](#DESCRIPTION)DESCRIPTION

           dmeventd is the event monitoring daemon for device-mapper devices.
           Library plugins can register and carry out actions triggered when
           particular events occur.

## [](#OPTIONS)OPTIONS

           -d     Repeat from 1 to 3 times (-d, -dd, -ddd) to increase the
                  detail of debug messages sent to syslog.  Each extra d adds
                  more debugging information.

           -f     Don't fork, run in the foreground.

           -h     Show help information.

           -l     Log through stdout and stderr instead of syslog.  This
                  option works only with option -f, otherwise it is ignored.

           -?     Show help information on stderr.

           -R     Replace a running dmeventd instance. The running dmeventd
                  must be version 2.02.77 or newer. The new dmeventd instance
                  will obtain a list of devices and events to monitor from
                  the currently running daemon.

           -V     Show version of dmeventd.

## [](#LVM_PLUGINS)LVM PLUGINS

           Mirror Attempts to handle device failure automatically.
                  See lvm.conf(5).

           Raid   Attempts to handle device failure automatically.
                  See lvm.conf(5).

           Snapshot
                  Monitors how full a snapshot is becoming and emits a
                  warning to syslog when it exceeds 80% full.  The warning is
                  repeated when 85%, 90% and 95% of the snapshot is filled.
                  See lvm.conf(5).  Snapshot which runs out of space gets
                  invalid and when it is mounted, it gets umounted if
                  possible.

           Thin   Monitors how full a thin pool data and metadata is becoming
                  and emits a warning to syslog when it exceeds 80% full.
                  The warning is repeated when more then 85%, 90% and 95% of
                  the thin pool is filled. See lvm.conf(5).  When a thin pool
                  fills over 50% (data or metadata) thin plugin calls
                  configured dmeventd/thin_command with every 5% increase.
                  With default setting it calls internal lvm lvextend
                  --use-policies to resize thin pool when it's been filled
                  above configured threshold
                  activation/thin_pool_autoextend_threshold.  If the command
                  fails, dmeventd thin plugin will keep retrying execution
                  with increasing time delay between retries upto 42 minutes.
                  User may also configure external command to support more
                  advanced maintenance operations of a thin pool.  Such
                  external command can e.g. remove some unneeded snapshots,
                  use fstrim(8) to free recover space in a thin pool, but
                  also can use lvextend --use-policies if other actions have
                  not released enough space.  Command is executed with
                  environmental variable LVM_RUN_BY_DMEVENTD=1 so any lvm2
                  command executed in this environment will not try to
                  interact with dmeventd.  To see the fullness of a thin pool
                  command may check these two environmental variables
                  DMEVENTD_THIN_POOL_DATA and DMEVENTD_THIN_POOL_METADATA.
                  Command can also read status with tools like lvs(8).

           Vdo    Monitors how full a VDO pool data is becoming and emits a
                  warning to syslog when it exceeds 80% full.  The warning is
                  repeated when more then 85%, 90% and 95% of the VDO pool is
                  filled. See lvm.conf(5).  When a VDO pool fills over 50%
                  vdo plugin calls configured dmeventd/vdo_command with every
                  5% increase.  With default setting it calls internal lvm
                  lvextend --use-policies to resize VDO pool when it's been
                  filled above the configured threshold
                  activation/vdo_pool_autoextend_threshold.  If the command
                  fails, dmeventd vdo plugin will keep retrying execution
                  with increasing time delay between retries upto 42 minutes.
                  User may also configure external command to support more
                  advanced maintenance operations of a VDO pool.  Such
                  external command can e.g. remove some unneeded space with
                  fstrim(8), but also can use lvextend --use-policies if
                  other actions have not released enough space.  Command is
                  executed with environmental variable LVM_RUN_BY_DMEVENTD=1
                  so any lvm2 command executed in this environment will not
                  try to interact with dmeventd.  To see the fullness of a
                  VDO pool command may check this environmental variable
                  DMEVENTD_VDO_POOL.  Command can also read status with tools
                  like lvs(8).

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           DMEVENTD_THIN_POOL_DATA
                  Variable is set by thin plugin and is available to executed
                  program. Value present actual usage of thin pool data
                  volume. Variable is not set when error event is processed.

           DMEVENTD_THIN_POOL_METADATA
                  Variable is set by thin plugin and is available to executed
                  program. Value present actual usage of thin pool metadata
                  volume. Variable is not set when error event is processed.

           DMEVENTD_VDO_POOL
                  Variable is set by vdo plugin and is available to executed
                  program. Value present actual usage of VDO pool data
                  volume. Variable is not set when error event is processed.

           LVM_RUN_BY_DMEVENTD
                  Variable is set by thin and vdo plugin to prohibit
                  recursive interation with dmeventd by any executed lvm2
                  command from a thin_command, vdo_command environment.

## [](#SEE_ALSO)SEE ALSO

           lvm(8), lvm.conf(5), lvextend(8),
           fstrim(8)

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

    Red Hat Inc        DM TOOLS 2.03.15(2)-git (2021-10-20)       DMEVENTD(8)

------------------------------------------------------------------------

Pages that refer to this page: [lvmraid(7)](../man7/lvmraid.7.html),  [lvmthin(7)](../man7/lvmthin.7.html),  [lvchange(8)](../man8/lvchange.8.html),  [lvconvert(8)](../man8/lvconvert.8.html),  [lvcreate(8)](../man8/lvcreate.8.html),  [lvdisplay(8)](../man8/lvdisplay.8.html),  [lvextend(8)](../man8/lvextend.8.html),  [lvm(8)](../man8/lvm.8.html),  [lvmconfig(8)](../man8/lvmconfig.8.html),  [lvmdevices(8)](../man8/lvmdevices.8.html),  [lvmdiskscan(8)](../man8/lvmdiskscan.8.html),  [lvm-fullreport(8)](../man8/lvm-fullreport.8.html),  [lvm-lvpoll(8)](../man8/lvm-lvpoll.8.html),  [lvreduce(8)](../man8/lvreduce.8.html),  [lvremove(8)](../man8/lvremove.8.html),  [lvrename(8)](../man8/lvrename.8.html),  [lvresize(8)](../man8/lvresize.8.html),  [lvs(8)](../man8/lvs.8.html),  [lvscan(8)](../man8/lvscan.8.html),  [pvchange(8)](../man8/pvchange.8.html),  [pvck(8)](../man8/pvck.8.html),  [pvcreate(8)](../man8/pvcreate.8.html),  [pvdisplay(8)](../man8/pvdisplay.8.html),  [pvmove(8)](../man8/pvmove.8.html),  [pvremove(8)](../man8/pvremove.8.html),  [pvresize(8)](../man8/pvresize.8.html),  [pvs(8)](../man8/pvs.8.html),  [pvscan(8)](../man8/pvscan.8.html),  [vgcfgbackup(8)](../man8/vgcfgbackup.8.html),  [vgcfgrestore(8)](../man8/vgcfgrestore.8.html),  [vgchange(8)](../man8/vgchange.8.html),  [vgck(8)](../man8/vgck.8.html),  [vgconvert(8)](../man8/vgconvert.8.html),  [vgcreate(8)](../man8/vgcreate.8.html),  [vgdisplay(8)](../man8/vgdisplay.8.html),  [vgexport(8)](../man8/vgexport.8.html),  [vgextend(8)](../man8/vgextend.8.html),  [vgimport(8)](../man8/vgimport.8.html),  [vgimportclone(8)](../man8/vgimportclone.8.html),  [vgimportdevices(8)](../man8/vgimportdevices.8.html),  [vgmerge(8)](../man8/vgmerge.8.html),  [vgmknodes(8)](../man8/vgmknodes.8.html),  [vgreduce(8)](../man8/vgreduce.8.html),  [vgremove(8)](../man8/vgremove.8.html),  [vgrename(8)](../man8/vgrename.8.html),  [vgs(8)](../man8/vgs.8.html),  [vgscan(8)](../man8/vgscan.8.html),  [vgsplit(8)](../man8/vgsplit.8.html)

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
