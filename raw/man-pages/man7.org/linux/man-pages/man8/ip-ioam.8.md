---
{"title": "ip-ioam(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ip-ioam.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ip-ioam(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP-IOAM(8)                        Linux                        IP-IOAM(8)

## [](#NAME)NAME

           ip-ioam - IPv6 In-situ OAM (IOAM)

## [](#SYNOPSIS)SYNOPSIS

           ip ioam  { COMMAND | help }

           ip ioam namespace show

           ip ioam namespace add ID  [ data DATA32 ]  [ wide DATA64 ]

           ip ioam namespace del ID

           ip ioam schema show

           ip ioam schema add ID DATA

           ip ioam schema del ID

           ip ioam namespace set ID schema  { ID | none }

           ip ioam monitor

## [](#DESCRIPTION)DESCRIPTION

           The ip ioam command is used to configure IPv6 In-situ OAM (IOAM6)
           internal parameters, namely IOAM namespaces and schemas.

           Those parameters also include the mapping between an IOAM
           namespace and an IOAM schema.

           The ip ioam monitor command displays IOAM data received.

## [](#EXAMPLES)EXAMPLES

       Configure an IOAM namespace (ID = 1) with both data (32 bits) and wide
           data (64 bits)
           # ip ioam namespace add 1 data 0xdeadbeef wide 0xcafec0caf00dc0de

       Link an existing IOAM schema (ID = 7) to an existing IOAM namespace
           (ID = 1)
           # ip ioam namespace set 1 schema 7

## [](#SEE_ALSO)SEE ALSO

           ip-route(8)

## [](#AUTHOR)AUTHOR

           Justin Iurman <justin.iurman@uliege.be>

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

    iproute2                       05 Jul 2021                     IP-IOAM(8)

------------------------------------------------------------------------

Pages that refer to this page: [ip(8)](../man8/ip.8.html),  [ip-route(8)](../man8/ip-route.8.html)

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
