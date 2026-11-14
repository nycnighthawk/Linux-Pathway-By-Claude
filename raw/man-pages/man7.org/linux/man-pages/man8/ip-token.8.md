---
{"title": "ip-token(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ip-token.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ip-token(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP-TOKEN(8)                       Linux                       IP-TOKEN(8)

## [](#NAME)NAME

           ip-token - tokenized interface identifier support

## [](#SYNOPSIS)SYNOPSIS

           ip token { COMMAND | help }

           ip token set TOKEN dev DEV

           ip token del dev DEV

           ip token get [ dev DEV ]

           ip token [ list ]

## [](#DESCRIPTION)DESCRIPTION

           IPv6 tokenized interface identifier support is used for assigning
           well-known host-part addresses to nodes whilst still obtaining a
           global network prefix from Router advertisements. The primary
           target for tokenized identifiers are server platforms where
           addresses are usually manually configured, rather than using
           DHCPv6 or SLAAC. By using tokenized identifiers, hosts can still
           determine their network prefix by use of SLAAC, but more readily
           be automatically renumbered should their network prefix change
           [1]. Tokenized IPv6 Identifiers are described in the draft [1]:
           <draft-chown-6man-tokenised-ipv6-identifiers-02>.

       ip token set - set an interface token
           set the interface token to the kernel.

           TOKEN  the interface identifier token address.

           dev DEV
                  the networking interface.

       ip token del - delete an interface token
           delete the interface token from the kernel.

           dev DEV
                  the networking interface.

       ip token get - get the interface token from the kernel
           show a tokenized interface identifier of a particular networking
           device.  Arguments: coincide with the arguments of ip token set
           but the TOKEN must be left out.

       ip token list - list all interface tokens
           list all tokenized interface identifiers for the networking
           interfaces from the kernel.

## [](#SEE_ALSO)SEE ALSO

           ip(8)

## [](#AUTHOR)AUTHOR

           Manpage by Daniel Borkmann

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

    iproute2                       28 Mar 2013                    IP-TOKEN(8)

------------------------------------------------------------------------

Pages that refer to this page: [ip(8)](../man8/ip.8.html)

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
