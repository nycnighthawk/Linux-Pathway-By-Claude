---
{"title": "ovs-pcap(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ovs-pcap.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ovs-pcap(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ovs-pcap(1)                Open vSwitch Manual                ovs-pcap(1)

## [](#NAME)NAME

           ovs-pcap - print packets from a pcap file as hex

## [](#SYNOPSIS)SYNOPSIS

           ovs-pcap file

           Common options:
                  [-h | --help] [-V | --version]

## [](#DESCRIPTION)DESCRIPTION

           The ovs-pcap program reads the pcap file named on the command line
           and prints each packet's contents as a sequence of hex digits on a
           line of its own.  This format is suitable for use with the
           ofproto/trace command supported by ovs-vswitchd(8).

## [](#OPTIONS)OPTIONS

           -h
           --help Prints a brief help message to the console.

           -V
           --version
                  Prints version information to the console.

## [](#SEE_ALSO)SEE ALSO

           ovs-vswitchd(8), ovs-tcpundump(1), tcpdump(8), wireshark(8).

## [](#COLOPHON)COLOPHON

           This page is part of the Open vSwitch (a distributed virtual
           multilayer switch) project.  Information about the project can be
           found at ⟨http://openvswitch.org/⟩.  If you have a bug report for
           this manual page, send it to bugs@openvswitch.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/openvswitch/ovs.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-23.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Open vSwitch                      3.2.90                      ovs-pcap(1)

------------------------------------------------------------------------

Pages that refer to this page: [ovs-tcpundump(1)](../man1/ovs-tcpundump.1.html),  [ovs-tcpdump(8)](../man8/ovs-tcpdump.8.html),  [ovs-vswitchd(8)](../man8/ovs-vswitchd.8.html)

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
