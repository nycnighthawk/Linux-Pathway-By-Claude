---
{"title": "org.freedesktop.oom1(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/org.freedesktop.oom1.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# org.freedesktop.oom1(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [INTRODUCTION](#INTRODUCTION) \| [THE MANAGER OBJECT](#THE_MANAGER_OBJECT) \| [VERSIONING](#VERSIONING) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                      |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ORG.FREEDESKTOP.OOM1(5)    org.freedesktop.oom1   ORG.FREEDESKTOP.OOM1(5)

## [](#NAME)NAME

           org.freedesktop.oom1 - The D-Bus interface of systemd-oomd

## [](#INTRODUCTION)INTRODUCTION

           systemd-oomd.service(8) is a system service which implements a
           userspace out-of-memory (OOM) killer. This page describes the
           D-Bus interface.

## [](#THE_MANAGER_OBJECT)THE MANAGER OBJECT

           The service exposes the following interfaces on the Manager object
           on the bus:

               node /org/freedesktop/oom1 {
                 interface org.freedesktop.oom1.Manager {
                   methods:
                     DumpByFileDescriptor(out h fd);
                   signals:
                     Killed(s cgroup,
                            s reason);
                 };
                 interface org.freedesktop.DBus.Peer { ... };
                 interface org.freedesktop.DBus.Introspectable { ... };
                 interface org.freedesktop.DBus.Properties { ... };
               };

       Methods
           Killed() signal is sent when any cgroup is killed by oomd.

           Note that more reasons will be added in the future, and the table
           below will be expanded accordingly.

           Table 1. Killing reasons
           ┌─────────────────┬──────────────────────────┐
           │ Reason          │ Description              │
           ├─────────────────┼──────────────────────────┤
           │ memory-used     │ Application took too     │
           │                 │ much memory and swap.    │
           ├─────────────────┼──────────────────────────┤
           │ memory-pressure │ Application took enough  │
           │                 │ memory and swap to cause │
           │                 │ sufficient slowdown of   │
           │                 │ other applications.      │
           └─────────────────┴──────────────────────────┘

## [](#VERSIONING)VERSIONING

           These D-Bus interfaces follow the usual interface versioning
           guidelines[1].

## [](#HISTORY)HISTORY

       The Manager Object
           Killed() was added in version 252.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-oomd.service(8), oomctl(1)

## [](#NOTES)NOTES

            1. the usual interface versioning guidelines
               https://0pointer.de/blog/projects/versioning-dbus.html

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                 ORG.FREEDESKTOP.OOM1(5)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-oomd.service(8)](../man8/systemd-oomd.service.8.html)

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
