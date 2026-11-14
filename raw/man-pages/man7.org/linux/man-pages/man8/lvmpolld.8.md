---
{"title": "lvmpolld(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lvmpolld.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lvmpolld(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                   |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LVMPOLLD(8)              System Manager's Manual              LVMPOLLD(8)

## [](#NAME)NAME

           lvmpolld — LVM poll daemon

## [](#SYNOPSIS)SYNOPSIS

           lvmpolld [-B|--binary lvm_binary_path] [-f|--foreground]
                    [-h|--help] [-l|--log all|wire|debug]
                    [-p|--pidfile pidfile_path] [-s|--socket socket_path]
                    [-t|--timeout timeout_value] [-V|--version]

           lvmpolld [--dump]

## [](#DESCRIPTION)DESCRIPTION

           lvmpolld  is  polling daemon for LVM. The daemon receives requests
           for polling of already initialised operations originating in  LVM2
           command  line tool.  The requests for polling originate in the lv‐
           convert, pvmove, lvchange or vgchange LVM2 commands.

           The purpose of lvmpolld is to reduce the number of  spawned  back‐
           ground  processes  per  otherwise  unique polling operation. There
           should be only one. It also eliminates the  possibility  of  unso‐
           licited termination of background process by external factors.

           lvmpolld  is  used  by LVM only if it is enabled in lvm.conf(5) by
           specifying the global/use_lvmpolld setting. If this is not defined
           in the LVM configuration explicitly then default setting  is  used
           instead   (see  the  output  of  lvmconfig  --type  default  glob‐
           al/use_lvmpolld command).

## [](#OPTIONS)OPTIONS

           To run the daemon in a test environment both the pidfile_path  and
           the socket_path should be changed from the defaults.

           -B|--binary lvm_binary_path
                  Optional path to alternative LVM binary (default:
                  /bin/lvm).  Use for testing purposes only.

           --dump Contact the running lvmpolld daemon to obtain the complete
                  state and print it out in a raw format.

           -f|--foreground
                  Don't fork, but run in the foreground.

           -h|--help
                  Show help information.

           -l|--log all|wire|debug
                  Select the type of log messages to generate.  Messages are
                  logged by syslog.  Additionally, when -f is given they are
                  also sent to standard error.  There are two classes of mes‐
                  sages: wire and debug.  Selecting 'all' supplies both and
                  is equivalent to a comma-separated list -l wire,debug.

           -p|--pidfile pidfile_path
                  Path to the pidfile. This overrides both the built-in de‐
                  fault (/run/lvmpolld.pid) and the environment variable
                  LVM_LVMPOLLD_PIDFILE.  This file is used to prevent more
                  than one instance of the daemon running simultaneously.

           -s|--socket socket_path
                  Path to the socket file. This overrides both the built-in
                  default (/run/lvm/lvmpolld.socket) and the environment
                  variable LVM_LVMPOLLD_SOCKET.

           -t|--timeout timeout_value
                  The daemon may shutdown after being idle for the given time
                  (in seconds).  When the option is omitted or the value giv‐
                  en is zero the daemon never shutdowns on idle.

           -V|--version
                  Display the version of lvmpolld daemon.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           LVM_LVMPOLLD_PIDFILE
                  Path for the pid file.

           LVM_LVMPOLLD_SOCKET
                  Path for the socket file.

## [](#SEE_ALSO)SEE ALSO

           lvm(8), lvm.conf(5), lvchange(8), lvconvert(8), pvmove(8),
           vgchange(8)

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

    Red Hat, Inc.     LVM TOOLS 2.03.42(2)-git (2026-05-15)       LVMPOLLD(8)

------------------------------------------------------------------------

Pages that refer to this page: [lvchange(8)](../man8/lvchange.8.html),  [lvconvert(8)](../man8/lvconvert.8.html),  [lvcreate(8)](../man8/lvcreate.8.html),  [lvdisplay(8)](../man8/lvdisplay.8.html),  [lvextend(8)](../man8/lvextend.8.html),  [lvm(8)](../man8/lvm.8.html),  [lvmconfig(8)](../man8/lvmconfig.8.html),  [lvmdevices(8)](../man8/lvmdevices.8.html),  [lvmdiskscan(8)](../man8/lvmdiskscan.8.html),  [lvmdump(8)](../man8/lvmdump.8.html),  [lvm-fullreport(8)](../man8/lvm-fullreport.8.html),  [lvm-lvpoll(8)](../man8/lvm-lvpoll.8.html),  [lvreduce(8)](../man8/lvreduce.8.html),  [lvremove(8)](../man8/lvremove.8.html),  [lvrename(8)](../man8/lvrename.8.html),  [lvresize(8)](../man8/lvresize.8.html),  [lvs(8)](../man8/lvs.8.html),  [lvscan(8)](../man8/lvscan.8.html),  [pvchange(8)](../man8/pvchange.8.html),  [pvck(8)](../man8/pvck.8.html),  [pvcreate(8)](../man8/pvcreate.8.html),  [pvdisplay(8)](../man8/pvdisplay.8.html),  [pvmove(8)](../man8/pvmove.8.html),  [pvremove(8)](../man8/pvremove.8.html),  [pvresize(8)](../man8/pvresize.8.html),  [pvs(8)](../man8/pvs.8.html),  [pvscan(8)](../man8/pvscan.8.html),  [vgcfgbackup(8)](../man8/vgcfgbackup.8.html),  [vgcfgrestore(8)](../man8/vgcfgrestore.8.html),  [vgchange(8)](../man8/vgchange.8.html),  [vgck(8)](../man8/vgck.8.html),  [vgconvert(8)](../man8/vgconvert.8.html),  [vgcreate(8)](../man8/vgcreate.8.html),  [vgdisplay(8)](../man8/vgdisplay.8.html),  [vgexport(8)](../man8/vgexport.8.html),  [vgextend(8)](../man8/vgextend.8.html),  [vgimport(8)](../man8/vgimport.8.html),  [vgimportclone(8)](../man8/vgimportclone.8.html),  [vgimportdevices(8)](../man8/vgimportdevices.8.html),  [vgmerge(8)](../man8/vgmerge.8.html),  [vgmknodes(8)](../man8/vgmknodes.8.html),  [vgreduce(8)](../man8/vgreduce.8.html),  [vgremove(8)](../man8/vgremove.8.html),  [vgrename(8)](../man8/vgrename.8.html),  [vgs(8)](../man8/vgs.8.html),  [vgscan(8)](../man8/vgscan.8.html),  [vgsplit(8)](../man8/vgsplit.8.html)

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
