---
{"title": "iptraf-ng(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/iptraf.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# iptraf-ng(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SIGNALS](#SIGNALS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [MANUAL AUTHOR](#MANUAL_AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IPTRAF-NG(8)             System Manager's Manual             IPTRAF-NG(8)

## [](#NAME)NAME

           iptraf - Interactive Colorful IP LAN Monitor

## [](#SYNOPSIS)SYNOPSIS

           iptraf-ng { [ -f ] [ { -i iface | -g | -d iface | -s iface | -z
           iface | -l iface } [ -t timeout ] [ -B [ -L logfile ] ] ] | [ -h ]
           }

## [](#DESCRIPTION)DESCRIPTION

           iptraf-ng is an ncurses-based IP LAN monitor that generates
           various network statistics including TCP info, UDP counts, ICMP
           and OSPF information, Ethernet load info, node stats, IP checksum
           errors, and others.

           If the iptraf-ng command is issued without any command-line
           options, the program comes up in interactive mode, with the
           various facilities accessed through the main menu.

## [](#OPTIONS)OPTIONS

           These options can also be supplied to the command:

           -i iface
                  immediately start the IP traffic monitor on the specified
                  interface, or all interfaces if "-i all" is specified

           -g     immediately start the general interface statistics

           -d iface
                  allows you to immediately start the detailed on the
                  indicated interface (iface)

           -s iface
                  allows you to immediately monitor TCP and UDP traffic on
                  the specified interface (iface)

           -z iface
                  shows packet counts by size on the specified interface

           -l iface
                  start the LAN station monitor on the specified interface,
                  or all LAN interfaces if "-l all" is specified

           -t timeout
                  tells IPTraf-ng to run the specified facility for only
                  timeout minutes.  This option is used only with one of the
                  above parameters.

           -B     redirect standard output to /dev/null, closes standard
                  input, and forks the program into the background.  Can be
                  used only with one of the facility invocation parameters
                  above.  Send the backgrounded process a USR2 signal to
                  terminate.

           -L logfile
                  allows you to specify an alternate log file name.  The
                  default log file name is based on either the interface
                  selected (detailed interface statistics, TCP/UDP service
                  statistics, packet size breakdown), or the instance of the
                  facility (IP traffic monitor, LAN station monitor).  If a
                  path is not specified, the log file is placed in
                  /var/log/iptraf-ng

           -f     clears all locks and counters, causing this instance of
                  IPTraf-ng to think it's the first one running.  This should
                  only be used to recover from an abnormal termination or
                  system crash.

           -h     shows a command summary

## [](#SIGNALS)SIGNALS

            SIGUSR1 - rotates log files while program is running
            SIGUSR2 - terminates an IPTraf-ng process running in the
           background.

## [](#FILES)FILES

            /var/log/iptraf-ng/*.log - log file
            /var/lib/iptraf-ng/* - important IPTraf-ng data files

## [](#SEE_ALSO)SEE ALSO

            Documentation/* - complete documentation written by the author

## [](#AUTHOR)AUTHOR

           Gerard Paul Java (riker@mozcom.com)

## [](#MANUAL_AUTHOR)MANUAL AUTHOR

           Frederic Peters (fpeters@debian.org), using iptraf-ng -h General
           manual page modifications by Gerard Paul Java (riker@mozcom.com),
           Phil Cameron (pcameron@redhat.com)

## [](#COLOPHON)COLOPHON

           This page is part of the iptraf-ng (Interactive Colorful IP LAN
           Monitor) project.  Information about the project can be found at
           ⟨https://github.com/iptraf-ng/iptraf-ng⟩.  If you have a bug
           report for this manual page, see ⟨[unknown]⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/iptraf-ng/iptraf-ng.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2025-01-10.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                               IPTraf-ng Help Page               IPTRAF-NG(8)

------------------------------------------------------------------------

Pages that refer to this page: [ifpps(8)](../man8/ifpps.8.html)

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
