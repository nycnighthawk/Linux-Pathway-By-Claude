---
{"title": "ovs-tcpdump(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ovs-tcpdump.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ovs-tcpdump(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [Author](#Author) \| [Copyright](#Copyright) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    OVS-TCPDUMP(8)                 Open vSwitch                OVS-TCPDUMP(8)

## [](#NAME)NAME

           ovs-tcpdump - Dump traffic from an Open vSwitch port using tcpdump

## [](#SYNOPSIS)SYNOPSIS

           ovs-tcpdump -i <port> <tcpdump options>...

## [](#DESCRIPTION)DESCRIPTION

           ovs-tcpdump creates switch mirror ports in the ovs-vswitchd daemon
           and executes tcpdump to listen against those ports. When the
           tcpdump instance exits, it then cleans up the mirror port it
           created.

           ovs-tcpdump will not allow multiple mirrors for the same port. It
           has some logic to parse the current configuration and prevent
           duplicate mirrors.

           The -i option may not appear multiple times.

           It is important to note that under Linux-based kernels, tap
           devices do not receive packets unless the specific tuntap device
           has been opened by an application.  This requires CAP_NET_ADMIN
           privileges, so the ovs-tcpdump command must be run as a user with
           such permissions (this is usually a super-user).

## [](#OPTIONS)OPTIONS

           • -h or --help

             Prints a brief help message to the console.

           • -V or --version

             Prints version information to the console.

           • --db-sock <socket>

             The Open vSwitch database socket connection string. The default
             is unix:<rundir>/db.sock.

           • --dump-cmd <command>

             The command to run instead of tcpdump.

           • -i or --interface

             The interface for which a mirror port should be created, and
             packets should be dumped.

           • --mirror-to

             The name of the interface which should be the destination of the
             mirrored packets. If the specified interface does not exist, it
             will be created as part of the setup process. If the interface
             already exists, it must be a port type that can be used with the
             tcpdump utility.  Mirror ports cannot be used for normal
             traffic. The default value is mi<port>.

           • --span

             If specified, mirror all ports (optional).

           • --filter <flow>

             If specified, only mirror packets that match the provided
             OpenFlow filter.  The available fields are documented in
             ovs-fields(7).

## [](#SEE_ALSO)SEE ALSO

           ovs-appctl(8), ovs-vswitchd(8), ovs-pcap(1), ovs-fields(7),
           ovs-tcpundump(1), tcpdump(8), wireshark(8).

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

    4.0.90                         Aug 03, 2026                OVS-TCPDUMP(8)

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
