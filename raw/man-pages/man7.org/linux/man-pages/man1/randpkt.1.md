---
{"title": "randpkt(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/randpkt.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# randpkt(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DIAGNOSTIC OPTIONS](#DIAGNOSTIC_OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                             |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RANDPKT(1)                                                     RANDPKT(1)

## [](#NAME)NAME

           randpkt - Random packet generator

## [](#SYNOPSIS)SYNOPSIS

           randpkt [ -b <maxbytes> ] [ -c <count> ] [ -F <file format> ] [ -r
           ] [ -t <type> ] <filename>

           randpkt -h|--help

           randpkt -v|--version

## [](#DESCRIPTION)DESCRIPTION

           randpkt is a small utility that creates a trace file full of
           random packets.

           By creating many randomized packets of a certain type, you can
           test packet sniffers to see how well they handle malformed
           packets. The sniffer can never trust the data that it sees in the
           packet because you can always sniff a very bad packet that
           conforms to no standard. randpkt produces very bad packets.

           When creating packets of a certain type, randpkt uses a sample
           packet that is stored internally to randpkt. It uses this as the
           starting point for your random packets, and then adds extra random
           bytes to the end of this sample packet.

           For example, if you choose to create random ARP packets, randpkt
           will create a packet which contains a predetermined Ethernet II
           header, with the Type field set to ARP. After the Ethernet II
           header, it will put a random number of bytes with random values.

## [](#OPTIONS)OPTIONS

           -b <maxbytes>

               Default 5000.

               Defines the maximum number of bytes added to the sample
               packet. If you choose a maxbytes value that is less than the
               size of the sample packet, then your packets would contain
               only the sample packet... not much variance there! randpkt
               exits on that condition.

           -c <count>

               Default 1000.

               Defines the number of packets to generate.

           -F <file format>

               Default pcapng.

               Sets the file format of the output capture file. randpkt can
               write the file in several formats; randpkt -F provides a list
               of the available output formats. Note that not all output
               formats support all packet types.

           -h|--help
               Print the version number and options and exit.

           -r

               The packet type is determined randomly for each packet. This
               requires an output format that can support different
               encapsulations per packet, like pcapng.

           -t <type>

               Default Ethernet II frame.

               Defines the type of packet to generate:

                   arp             Address Resolution Protocol
                   bgp             Border Gateway Protocol
                   bvlc            BACnet Virtual Link Control
                   dns             Domain Name Service
                   eth             Ethernet
                   fddi            Fiber Distributed Data Interface
                   giop            General Inter-ORB Protocol
                   icmp            Internet Control Message Protocol
                   ip              Internet Protocol
                   ipv6            Internet Protocol Version 6
                   llc             Logical Link Control
                   m2m             WiMAX M2M Encapsulation Protocol
                   megaco          MEGACO
                   nbns            NetBIOS-over-TCP Name Service
                   ncp2222         NetWare Core Protocol
                   sctp            Stream Control Transmission Protocol
                   syslog          Syslog message
                   tds             TDS NetLib
                   tcp             Transmission Control Protocol
                   tr              Token-Ring
                   udp             User Datagram Protocol
                   usb             Universal Serial Bus
                   usb-linux       Universal Serial Bus with Linux specific header

           -v|--version
               Print the full version information and exit.

## [](#DIAGNOSTIC_OPTIONS)DIAGNOSTIC OPTIONS

           --log-level <level>
               Set the active log level. Supported levels in lowest to
               highest order are "noisy", "debug", "info", "message",
               "warning", "critical", and "error". Messages at each level and
               higher will be printed, for example "warning" prints
               "warning", "critical", and "error" messages and "noisy" prints
               all messages. Levels are case insensitive.

           --log-fatal <level>
               Abort the program if any messages are logged at the specified
               level or higher. For example, "warning" aborts on any
               "warning", "critical", or "error" messages.

           --log-fatal-count <count>
               The amount of fatal log messages which may pass before the
               program is aborted.

           --log-domains <list>
               Only print messages for the specified log domains, e.g.
               "GUI,Epan,sshdump". List of domains must be comma-separated.
               Can be negated with "!" as the first character (inverts the
               match).

           --log-debug <list>
               Force the specified domains to log at the "debug" level. List
               of domains must be comma-separated. Can be negated with "!" as
               the first character (inverts the match).

           --log-noisy <list>
               Force the specified domains to log at the "noisy" level. List
               of domains must be comma-separated. Can be negated with "!" as
               the first character (inverts the match).

           --log-fatal-domains <list>
               Abort the program if any messages are logged for the specified
               log domains. List of domains must be comma-separated.

           --log-file <path>
               Write log messages and stderr output to the specified file.

## [](#EXAMPLES)EXAMPLES

           To see a description of the randpkt options use:

               randpkt

           To generate a capture file with 1000 DNS packets use:

               randpkt -b 500 -t dns rand_dns.pcapng

           To generate a small capture file with just a single LLC frame use:

               randpkt -b 100 -c 1 -t llc single_llc.pcapng

## [](#SEE_ALSO)SEE ALSO

           pcap(3), editcap(1).SH COLOPHON This page is part of the wireshark
           (Interactively dump and analyze network traffic) project.
           Information about the project can be found at 
           ⟨https://www.wireshark.org/⟩. If you have a bug report for this
           manual page, see
           ⟨https://gitlab.com/wireshark/wireshark/-/issues⟩. This page was
           obtained from the project's upstream Git repository
           ⟨https://gitlab.com/wireshark/wireshark.git⟩ on 2026-08-04. (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.) If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                    2025-03-07                     RANDPKT(1)

------------------------------------------------------------------------

Pages that refer to this page: [randpktdump(1)](../man1/randpktdump.1.html)

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
