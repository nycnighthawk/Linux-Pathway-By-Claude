---
{"title": "ifpps(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ifpps.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ifpps(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [USAGE EXAMPLE](#USAGE_EXAMPLE) \| [NOTE](#NOTE) \| [LEGAL](#LEGAL) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IFPPS(8)                   netsniff-ng toolkit                   IFPPS(8)

## [](#NAME)NAME

           ifpps - top-like networking and system statistics

## [](#SYNOPSIS)SYNOPSIS

           ifpps { [options] | [device] }

## [](#DESCRIPTION)DESCRIPTION

           ifpps is a small utility which periodically provides top-like
           networking and system statistics from the kernel. ifpps gathers
           its data directly from procfs files and does not make use of any
           user space monitoring libraries which would falsify statistics
           under high load.

           For instance, consider the following scenario: two directly
           connected Linux machines with Intel Core 2 Quad Q6600 2.40GHz
           CPUs, 4 GB RAM, and an Intel 82566DC-2 Gigabit Ethernet NIC are
           used for performance evaluation.  One machine generates 64 byte
           network packets by using the kernel space packet generator pktgen
           with a maximum possible packet rate. The other machine displays
           statistics about incoming network packets by using i) iptraf(8)
           and ii) ifpps.

           iptraf which incorporates pcap(3) shows an average packet rate of
           246,000 pps while on the other hand ifpps shows an average packet
           rate of 1,378,000 pps. Hence, due to packet copies and deferring
           statistics creation into user space, a measurement error of
           approximately 460 percent occurs. Tools like iptraf might display
           much more information such as TCP per flow statistics (hence the
           use of the pcap library).  This is not possible with ifpps,
           because overall networking statistics are its focus; statistics,
           which are also fairly reliable under high packet load.

           ifpps also periodically displays CPU load, interrupt, software
           interrupt data per sample interval as well as total interrupts,
           all per CPU. In case the number of CPUs exceeds 5 or the number
           specified by the user with the -n command line option, ifpps will
           only display this number top heavy hitters. The topmost heavy
           hitter CPU will be marked with “+”.  The least heavy hitter will
           always be displayed and is marked with “-”. In addition, the
           average for all the above per-CPU data is shown. Optionally the
           median values can be displayed using the -m command line option.

           ifpps also supports directly the gnuplot(1) data sample format.
           This facilitates creation of gnuplot figures from ifpps time
           series.

## [](#OPTIONS)OPTIONS

           -d <netdev>, --dev <netdev>
                  Networking device to fetch statistics from, for example
                  eth0, wlan0.

           -n, --num-cpus
                  Set maximum number of top hitter CPUs (in terms of time
                  spent in system/user mode) to display in ncurses mode,
                  default is 10.

           -t <time>, --interval <time>
                  Statistics refresh interval in milliseconds, default is
                  1000ms.

           -c, --csv
                  Output (once) the ncurses data to the terminal as
                  gnuplot(1)-ready data.

           -l, --loop
                  Continuously output the terminal data after a refresh
                  interval. This option is only available if option -c is
                  given. For -l it is usually recommended to redirect the
                  output into a file that is to be processed later with
                  gnuplot(1).

           -m, --median
                  Show median values across all CPUs for CPU load, interrupts
                  (per interval and absolute) and software interrupts.

           -o, --omit-header
                  Omit printing the CSV header. This option is only available
                  if -c is given.

           -p, --promisc
                  Turn on promiscuous mode for the given networking device.

           -P, --percentage
                  Show percentage of current throughput in relation to
                  theoretical line rate.

           -W, --no-warn
                  Suppress possible warnings in the ncurses output, e.g.
                  about a too low sampling interval that could cause
                  performance regression.

           -v, --version
                  Show version information.

           -h, --help
                  Show user help.

## [](#USAGE_EXAMPLE)USAGE EXAMPLE

           ifpps eth0
                  Default ncurses output for the eth0 device.

           ifpps -pd eth0
                  Ncurses output for the eth0 device in promiscuous mode.

           ifpps -lpcd wlan0 > plot.dat
                  Continuous terminal output for the wlan0 device in
                  promiscuous mode.

## [](#NOTE)NOTE

           On 10Gbit/s cards or higher, receive and transmit statistics are
           usually accumulated at a higher duration interval than 1 second.
           Thus, it might be advisable to alter the timing to a higher
           accumulation interval for such cards.

## [](#LEGAL)LEGAL

           ifpps is licensed under the GNU GPL version 2.0.

## [](#HISTORY)HISTORY

           ifpps was originally written for the netsniff-ng toolkit by Daniel
           Borkmann. It is currently maintained by Tobias Klauser
           <tklauser@distanz.ch> and Daniel Borkmann
           <dborkma@tik.ee.ethz.ch>.

## [](#SEE_ALSO)SEE ALSO

           netsniff-ng(8), trafgen(8), mausezahn(8), bpfc(8), flowtop(8),
           astraceroute(8), curvetun(8)

## [](#AUTHOR)AUTHOR

           Manpage was written by Daniel Borkmann.

## [](#COLOPHON)COLOPHON

           This page is part of the Linux netsniff-ng toolkit project. A
           description of the project, and information about reporting bugs,
           can be found at http://netsniff-ng.org/.

## [](#COLOPHON)COLOPHON

           This page is part of the netsniff-ng (a free Linux networking
           toolkit) project.  Information about the project can be found at
           ⟨http://netsniff-ng.org/⟩.  If you have a bug report for this
           manual page, send it to netsniff-ng@googlegroups.com.  This page
           was obtained from the project's upstream Git repository
           ⟨https://github.com/netsniff-ng/netsniff-ng⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2025-06-11.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Linux                         03 March 2013                      IFPPS(8)

------------------------------------------------------------------------

Pages that refer to this page: [astraceroute(8)](../man8/astraceroute.8.html),  [bpfc(8)](../man8/bpfc.8.html),  [curvetun(8)](../man8/curvetun.8.html),  [flowtop(8)](../man8/flowtop.8.html),  [mausezahn(8)](../man8/mausezahn.8.html),  [netsniff-ng(8)](../man8/netsniff-ng.8.html),  [trafgen(8)](../man8/trafgen.8.html)

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
