---
{"title": "ethers(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/ethers.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ethers(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ETHERS(5)          Linux System Administrator's Manual          ETHERS(5)

## [](#NAME)NAME

           ethers - Ethernet address to IP number database

## [](#DESCRIPTION)DESCRIPTION

           /etc/ethers contains 48 bit Ethernet addresses and their
           corresponding IP numbers, one line for each IP number:

                  Ethernet-address  IP-number

           The two items are separated by any number of SPACE and/or TAB
           characters.  A # at the beginning of a line starts a comment which
           extends to the end of the line.  The Ethernet-address is written
           as x:x:x:x:x:x, where x is a hexadecimal number between 0 and ff
           which represents one byte of the address, which is in network byte
           order (big-endian).  The IP-number may be a hostname which can be
           resolved by DNS or a dot separated number.

## [](#EXAMPLES)EXAMPLES

           08:00:20:00:61:CA  pal

## [](#FILES)FILES

           /etc/ethers

## [](#SEE_ALSO)SEE ALSO

           Homepage of the net-tools project: 
           ⟨https://net-tools.sourceforge.io⟩

           arp(8), ip-link(8), rarp(8), rarpd(8), dnsmasq(8)

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

    net-tools                       2025-09-10                      ETHERS(5)

------------------------------------------------------------------------

Pages that refer to this page: [ether_aton(3)](../man3/ether_aton.3.html),  [pcap-filter(7)](../man7/pcap-filter.7.html),  [arp(8)](../man8/arp.8.html),  [rarp(8)](../man8/rarp.8.html),  [route(8)](../man8/route.8.html)

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
