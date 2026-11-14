---
{"title": "quota_nld(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/quota_nld.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# quota_nld(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RQUOTAD(8)               System Manager's Manual               RQUOTAD(8)

## [](#NAME)NAME

           quota_nld - quota netlink message daemon

## [](#SYNOPSIS)SYNOPSIS

           quota_nld [[ -D | -C ][ -F ][ -b ]]

## [](#DESCRIPTION)DESCRIPTION

           quota_nld listens on netlink socket and processes received quota
           warnings. By default quota_nld forwards warning messages to both
           the system's DBUS (so that the desktop manager can display a
           dialog) and the last-accessed terminal of the user to whom each
           warning is directed. Either of these destinations can be disabled
           with the -D and -C options, respectively.

           In the case of the user's terminal, quota messages about falling
           below the hard and soft limits are not sent unless the -b option
           is specified. In the case of the DBUS, all quota messages are
           sent.

           Note, that you have to enable the kernel support for sending quota
           messages over netlink (in Filesystems->Quota menu).

## [](#OPTIONS)OPTIONS

           -V, --version
                  Show version of quota tools and exit.

           -h, --help
                  Show a usage message and exit.

           -D, --no-dbus
                  Do not forward quota warnings to DBUS.

           -C, --no-console
                  Do not print quota warnings to the user's last-accessed
                  terminal.

           -b, --print-below
                  If quota warnings are printed to users' terminals, include
                  messages about falling below their hard and soft limits.

           -F, --foreground
                  Run daemon in foreground (may be useful for debugging
                  purposes).

## [](#SEE_ALSO)SEE ALSO

           quota(1), netlink(7), dbus.freedesktop.org

## [](#COLOPHON)COLOPHON

           This page is part of the quota (Linux Diskquota Tools) project.
           Information about the project can be found at [unknown -- if you
           know, please contact man-pages@man7.org] It is not known how to
           report bugs for this man page; if you know, please send a mail to
           man-pages@man7.org.  This page was obtained from the project's
           upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/quota/quota-tools.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2025-12-11.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                                                   RQUOTAD(8)

------------------------------------------------------------------------

Pages that refer to this page: [quota(1)](../man1/quota.1.html),  [quotaon(8)](../man8/quotaon.8.html),  [repquota(8)](../man8/repquota.8.html)

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
