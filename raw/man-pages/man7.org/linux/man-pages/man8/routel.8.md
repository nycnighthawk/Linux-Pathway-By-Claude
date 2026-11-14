---
{"title": "routel(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/routel.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# routel(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ROUTEL(8)                         Linux                         ROUTEL(8)

## [](#NAME)NAME

           routel - list routes with pretty output format

## [](#SYNOPSIS)SYNOPSIS

           routel [ OPTIONS ] [ tablenr [ ip route options... ] ]

            OPTIONS := { -h | --help | [{-f | --family } {inet | inet6 } | -4
           | -6 }

## [](#DESCRIPTION)DESCRIPTION

           The routel script will list routes in a format that some might
           consider easier to interpret then the ip route list equivalent.

## [](#AUTHORS)AUTHORS

           Rewritten by Stephen Hemminger <stephen@networkplumber.org>.
           Original script by Stephen R. van den Berg <srb@cuci.nl>.
           This manual page was written by Andreas Henriksson
           <andreas@fatal.se>, for the Debian GNU/Linux system.

## [](#SEE_ALSO)SEE ALSO

           ip(8)

## [](#COLOPHON)COLOPHON

           This page is part of the iproute2 (utilities for controlling
           TCP/IP networking and traffic) project.  Information about the
           project can be found at 
           ⟨http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2⟩.
           If you have a bug report for this manual page, send it to
           netdev@vger.kernel.org, shemminger@osdl.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/network/iproute2/iproute2.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-28.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    iproute2                       1 Sept, 2021                     ROUTEL(8)

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
