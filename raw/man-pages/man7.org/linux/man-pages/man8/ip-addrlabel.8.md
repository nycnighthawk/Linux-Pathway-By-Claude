---
{"title": "ip-addrlabel(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ip-addrlabel.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ip-addrlabel(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IP-ADDRLABEL(8)                   Linux                   IP-ADDRLABEL(8)

## [](#NAME)NAME

           ip-addrlabel - protocol address label management

## [](#SYNOPSIS)SYNOPSIS

           ip addrlabel  { COMMAND | help }

           ip addrlabel { add | del } prefix PREFIX [ dev DEV ] [ label
                   NUMBER ]

           ip addrlabel { list | flush }

## [](#DESCRIPTION)DESCRIPTION

           IPv6 address labels are used for address selection; they are
           described in RFC 3484. Precedence is managed by userspace, and
           only the label itself is stored in the kernel.

       ip addrlabel add - add an address label
           add an address label entry to the kernel.

           prefix PREFIX

           dev DEV
                  the outgoing interface.

           label NUMBER
                  the label for the prefix.  0xffffffff is reserved.

       ip addrlabel del - delete an address label
           delete an address label entry from the kernel.  Arguments:
           coincide with the arguments of ip addrlabel add but the label is
           not required.

       ip addrlabel list - list address labels
           list the current address label entries in the kernel.

       ip addrlabel flush - flush address labels
           flush all address labels in the kernel. This does not restore any
           default settings.

## [](#SEE_ALSO)SEE ALSO

           ip(8)

## [](#AUTHOR)AUTHOR

           Manpage by Yoshifuji Hideaki / 吉藤英明

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

    iproute2                       20 Dec 2011                IP-ADDRLABEL(8)

------------------------------------------------------------------------

Pages that refer to this page: [networkctl(1)](../man1/networkctl.1.html),  [ip(8)](../man8/ip.8.html)

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
