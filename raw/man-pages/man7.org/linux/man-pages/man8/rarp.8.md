---
{"title": "rarp(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rarp.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rarp(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [NOTE](#NOTE) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [WARNING](#WARNING) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                  |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RARP(8)            Linux System Administrator's Manual            RARP(8)

## [](#NAME)NAME

           rarp - manipulate the system RARP table

## [](#SYNOPSIS)SYNOPSIS

           rarp -a

           rarp [-v]-d hostname ...
           rarp[-v] [-t type] -s hostname hw_addr

           rarp [-V] [--version] [-h] [--help]

## [](#NOTE)NOTE

           This program is obsolete.  From version 2.3, the Linux kernel no
           longer contains RARP support.  Use the rarpd(8) as a usermode
           replacement.

## [](#DESCRIPTION)DESCRIPTION

           Rarp manipulates the kernel's (before version 2.3) RARP (reverse
           ARP) table in various ways.  The primary options are clearing an
           address mapping entry and manually setting up one.  For debugging
           purposes, the rarp program also allows a complete dump of the RARP
           table.

           The RARP table was used to announce additional MAC addresses when
           ARP neighbor discoveries are received.

## [](#OPTIONS)OPTIONS

           -V     Display the version of RARP in use.

           -v     Tell the user what is going on by being verbose.

           -t type
                  When setting or reading the RARP table, this optional
                  parameter tells rarp which class of entries it should check
                  for.  The default value of this parameter is ether (i.e.
                  hardware code 0x01 for IEEE 802.3 10Mbps Ethernet .  Other
                  values might include network technologies such as AX.25
                  (ax25) and NET/ROM (netrom).

           -a, --list
                  Lists the entries in the RARP table.

           -d  hostname, --delete hostname
                  Remove all RARP entries for the specified host.

           -s hostname hw_addr, --set hostname hw_addr
                  Create a RARP address mapping entry for host hostname with
                  hardware address set to hw_addr.  The format of the
                  hardware address is dependent on the hardware class, but
                  for most classes one can assume that the usual presentation
                  can be used.  For the Ethernet class, this is 6 bytes in
                  hexadecimal, separated by colons.

## [](#WARNING)WARNING

           Some systems (notably older Suns) assume that the host replying to
           a RARP query can also provide other remote boot services.
           Therefore never gratuitously add rarp entries unless you wish to
           meet the wrath of the network administrator.

## [](#FILES)FILES

           /proc/net/rarp (obsolete)

## [](#SEE_ALSO)SEE ALSO

           Homepage of the net-tools project: 
           ⟨https://net-tools.sourceforge.io⟩

           rarpd(8), arp(8), route(8), ifconfig(8), netstat(8)
           ethers(5), hosts(5)

## [](#AUTHORS)AUTHORS

           Ross D. Martin <martin@trcsun3.eas.asu.edu>,
           Fred N. van Kempen <waltje@uwalt.nl.mugnet.org>,
           Phil Blundell <Philip.Blundell@pobox.com>.

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

    net-tools                       2025-09-10                        RARP(8)

------------------------------------------------------------------------

Pages that refer to this page: [ethers(5)](../man5/ethers.5.html),  [proc_pid_net(5)](../man5/proc_pid_net.5.html)

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
