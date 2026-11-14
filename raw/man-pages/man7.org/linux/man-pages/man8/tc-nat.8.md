---
{"title": "tc-nat(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-nat.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-nat(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NAT action in tc(8)               Linux               NAT action in tc(8)

## [](#NAME)NAME

           nat - stateless native address translation action

## [](#SYNOPSIS)SYNOPSIS

           tc ... action nat DIRECTION OLD NEW

           DIRECTION := { ingress | egress }

           OLD := IPV4_ADDR_SPEC

           NEW := IPV4_ADDR_SPEC

           IPV4_ADDR_SPEC := { default | any | all |
                   in_addr[/{prefix|netmask}]

## [](#DESCRIPTION)DESCRIPTION

           The nat action allows one to perform NAT without the overhead of
           conntrack, which is desirable if the number of flows or addresses
           to perform NAT on is large. This action is best used in
           combination with the u32 filter to allow for efficient lookups of
           a large number of stateless NAT rules in constant time.

## [](#OPTIONS)OPTIONS

           ingress
                  Translate destination addresses, i.e. perform DNAT.

           egress Translate source addresses, i.e. perform SNAT.

           OLD    Specifies addresses which should be translated.

           NEW    Specifies addresses which OLD should be translated into.

## [](#NOTES)NOTES

           The accepted address format in OLD and NEW is quite flexible. It
           may either consist of one of the keywords default, any or all,
           representing the all-zero IP address or a combination of IP
           address and netmask or prefix length separated by a slash (/)
           sign. In any case, the mask (or prefix length) value of OLD is
           used for NEW as well so that a one-to-one mapping of addresses is
           assured.

           Address translation is done using a combination of binary
           operations. First, the original (source or destination) address is
           matched against the value of OLD.  If the original address fits,
           the new address is created by taking the leading bits from NEW
           (defined by the netmask of OLD) and taking the remaining bits from
           the original address.

           There is rudimental support for upper layer protocols, namely TCP,
           UDP and ICMP.  While for the first two only checksum recalculation
           is performed, the action also takes care of embedded IP headers in
           ICMP packets by translating the respective address therein, too.

## [](#SEE_ALSO)SEE ALSO

           tc(8)

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

    iproute2                       12 Jan 2015            NAT action in tc(8)

------------------------------------------------------------------------

Pages that refer to this page: [tc-actions(8)](../man8/tc-actions.8.html)

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
