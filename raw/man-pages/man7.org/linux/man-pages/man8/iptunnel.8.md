---
{"title": "iptunnel(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/iptunnel.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# iptunnel(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [NOTE](#NOTE) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IPTUNNEL(8)        Linux System Administrator's Manual        IPTUNNEL(8)

## [](#NAME)NAME

           iptunnel - creates, changes, deletes, and displays configured
           tunnels

## [](#SYNOPSIS)SYNOPSIS

           iptunnel [<operation>] [<args>]

## [](#NOTE)NOTE

           This program is obsolete. Please use ip tunnel instead, and see
           ip-tunnel(8) for more information.

## [](#DESCRIPTION)DESCRIPTION

           The iptunnel command creates configured tunnels for sending and
           receiving IPv6 or IPv4 packets that are encapsulated as the
           payload of an IPv4 datagram.

           The iptunnel command can perform one of the following operations:

           create - create a tunnel interface, which you must subsequently
           configure.

           change - change an existing tunnel interface.

           delete - delete a tunnel interface. You must disable the tunnel
           before you can delete it.

           show - show the tunnel attributes (name, tunnel end points, next
           hop for tunneled packets).

## [](#SEE_ALSO)SEE ALSO

           Homepage of the net-tools project: 
           ⟨https://net-tools.sourceforge.io⟩

           ip-tunnel(8), ip(8)

## [](#COLOPHON)COLOPHON

           This page is part of the net-tools (networking utilities) project.
           Information about the project can be found at 
           ⟨http://net-tools.sourceforge.net/⟩.  If you have a bug report for
           this manual page, see ⟨http://net-tools.sourceforge.net/⟩.  This
           page was obtained from the project's upstream Git repository
           ⟨git://git.code.sf.net/p/net-tools/code⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-06-12.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    net-tools                       2025-09-10                    IPTUNNEL(8)

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
