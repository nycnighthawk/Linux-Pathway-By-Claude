---
{"title": "ip-maddress(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ip-maddress.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ip-maddress(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP-MADDRESS(8)                    Linux                    IP-MADDRESS(8)

## [](#NAME)NAME

           ip-maddress - multicast addresses management

## [](#SYNOPSIS)SYNOPSIS

           ip [ OPTIONS ] maddress  { COMMAND | help }

           ip maddress [ add | del ] MULTIADDR dev NAME

           ip maddress show [ dev NAME ]

## [](#DESCRIPTION)DESCRIPTION

           maddress objects are multicast addresses.

       ip maddress show - list multicast addresses
           dev NAME (default)
                  the device name.

           ip maddress add - add a multicast address

           ip maddress delete - delete a multicast address

                  These commands attach/detach a static link-layer multicast
                  address to listen on the interface.  Note that it is
                  impossible to join protocol multicast groups statically.
                  This command only manages link-layer addresses.

                  address LLADDRESS (default)
                         the link-layer multicast address.

                  dev NAME
                         the device to join/leave this multicast address.

## [](#SEE_ALSO)SEE ALSO

           ip(8)

## [](#AUTHOR)AUTHOR

           Original Manpage by Michail Litvak <mci@owl.openwall.com>

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

    iproute2                       20 Dec 2011                 IP-MADDRESS(8)

------------------------------------------------------------------------

Pages that refer to this page: [ip(8)](../man8/ip.8.html),  [ipmaddr(8)](../man8/ipmaddr.8.html)

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
