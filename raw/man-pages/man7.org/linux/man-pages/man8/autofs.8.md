---
{"title": "autofs(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/autofs.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# autofs(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPERATION](#OPERATION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    AUTOFS(8)                System Manager's Manual                AUTOFS(8)

## [](#NAME)NAME

           autofs - Service control for the automounter

## [](#SYNOPSIS)SYNOPSIS

           If a SysV init script system is being used:
           @initdir@/autofs start|stop|restart|reload|status

           or if the systemd init system is being used:
           systemctl start|stop|restart|reload|status autofs.service

## [](#DESCRIPTION)DESCRIPTION

           autofs controls the operation of the automount(8) daemon(s)
           running on the Linux system. Usually autofs is invoked at system
           boot time with the start parameter and at shutdown time with the
           stop parameter. Service control actions can also be manually
           invoked by the system administrator to shut down, restart, reload
           or obtain service status.

## [](#OPERATION)OPERATION

           autofs will consult a configuration file @mapdir@/auto.master (see
           auto.master(5)) by default to find mount points on the system. For
           each of those mount points automount(8) will mount and start a
           thread, with the appropriate parameters, to manage the mount
           point.

           @initdir@/autofs reload or systemctl autofs.service reload will
           check the current auto.master map against the current automount
           managed mounts. It will terminate those daemons or threads
           (depending on autofs version) whose entries have been removed, re-
           read the automount maps for entries that have changed and start
           new daemons or threads for entries that have been added.

           If an indirect map is modified then the change will become
           effective immediately.  If an indirect map uses the browse option,
           the master map contains direct mount maps or the auto.master map
           is modified then the autofs service control reload action must be
           rerun to activate the changes.

           However, if a map entry has offsets and is currently in use the
           offset mounts cannot be updated due to potential mount
           dependencies. In this case the map entry offsets will not be
           updated until after the map entry has expired.

           @initdir@/autofs status or systemctl status autofs.service will
           display the status of, automount(8), running or not. When using
           the systemd init system the status output includes somewhat more
           information related to the service status.

           systemctl(1) has more functions than the actions mentioned here,
           see systemctl(1) for more information.

## [](#SEE_ALSO)SEE ALSO

           automount(8), autofs(5), autofs.conf(5), auto.master(5),
           autofs_ldap_auth.conf(5), systemctl(1).

## [](#AUTHOR)AUTHOR

           This manual page was written by Christoph Lameter
           <chris@waterf.org>, for the Debian GNU/Linux system.  Edited by H.
           Peter Anvin <hpa@transmeta.com> and Ian Kent <raven@themaw.net>.

## [](#COLOPHON)COLOPHON

           This page is part of the autofs (automount) project.  Information
           about the project can be found at ⟨UNKNOWN⟩.  If you have a bug
           report for this manual page, send it to autofs@vger.kernel.org.
           This page was obtained from the project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/linux/storage/autofs/autofs.git⟩ on
           2026-08-03.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-05-16.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                    9 Sep 1997                      AUTOFS(8)

------------------------------------------------------------------------

Pages that refer to this page: [autofs(5)](../man5/autofs.5.html),  [auto.master(5)](../man5/auto.master.5.html),  [automount(8)](../man8/automount.8.html)

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
