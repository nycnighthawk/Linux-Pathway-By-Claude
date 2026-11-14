---
{"title": "ovs-tcpundump(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ovs-tcpundump.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ovs-tcpundump(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [Author](#Author) \| [Copyright](#Copyright) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    OVS-TCPUNDUMP(1)               Open vSwitch              OVS-TCPUNDUMP(1)

## [](#NAME)NAME

           ovs-tcpundump - convert "tcpdump -xx" output to hex strings

## [](#SYNOPSIS)SYNOPSIS

           ovs-tcpundump < <file>

           ovs-tcpundump -h | --help

           ovs-tcpundump -V | --version

           The ovs-tcpundump program reads tcpdump -xx output from stdin,
           looking for hexadecimal packet data, and dumps each Ethernet as a
           single hexadecimal string on stdout.  This format is suitable for
           use with the ofproto/trace command supported by ovs-vswitchd(8)
           via ovs-appctl(8).

           At least two -x or -X options must be given, otherwise the output
           will omit the Ethernet header, which prevents the output from
           being used with ofproto/trace.

## [](#OPTIONS)OPTIONS

           • -h or --help

             Prints a brief help message to the console.

           • -V or --version

             Prints version information to the console.

## [](#SEE_ALSO)SEE ALSO

           ovs-appctl(8), ovs-vswitchd(8), ovs-pcap(1), tcpdump(8),
           wireshark(8).

## [](#Author)Author

           The Open vSwitch Development Community

## [](#Copyright)Copyright

           2016-2024, The Open vSwitch Development Community

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

    4.0.90                         Aug 03, 2026              OVS-TCPUNDUMP(1)

------------------------------------------------------------------------

Pages that refer to this page: [ovs-pcap(1)](../man1/ovs-pcap.1.html),  [ovs-tcpdump(8)](../man8/ovs-tcpdump.8.html),  [ovs-vswitchd(8)](../man8/ovs-vswitchd.8.html)

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
