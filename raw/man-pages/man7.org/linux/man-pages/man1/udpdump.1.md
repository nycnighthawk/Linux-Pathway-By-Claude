---
{"title": "udpdump(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/udpdump.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# udpdump(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UDPDUMP(1)                                                     UDPDUMP(1)

## [](#NAME)NAME

           udpdump - Provide a UDP receiver that gets packets from network
           devices (like Aruba routers) and exports them in PCAP format.

## [](#SYNOPSIS)SYNOPSIS

           udpdump [ --help ] [ --version ] [ --extcap-interfaces ] [
           --extcap-dlts ] [ --extcap-interface=<interface> ] [
           --extcap-config ] [ --capture ] [ --fifo=<path to file or pipe> ]
           [ --port=<port> ] [ --payload=<type> ]

## [](#DESCRIPTION)DESCRIPTION

           udpdump is a extcap tool that provides a UDP receiver that listens
           for exported datagrams coming from any source (like Aruba routers)
           and exports them in PCAP format. This provides the user two basic
           functionalities: the first one is to have a listener that prevents
           the localhost to send back an ICMP port-unreachable packet. The
           second one is to strip out the lower layers (layer 2, IP, UDP)
           that are useless (are used just as export vector). The format of
           the exported datagrams are EXPORTED_PDU, as specified in
           https://gitlab.com/wireshark/wireshark/-/raw/master/epan/exported_pdu.h

## [](#OPTIONS)OPTIONS

           --help
               Print program arguments.

           --version
               Print program version.

           --extcap-interfaces
               List available interfaces.

           --extcap-interface=<interface>
               Use specified interfaces.

           --extcap-dlts
               List DLTs of specified interface.

           --extcap-config
               List configuration options of specified interface.

           --capture
               Start capturing from specified interface save saved it in
               place specified by --fifo.

           --fifo=<path to file or pipe>
               Save captured packet to file or send it through pipe.

           --port=<port>
               Set the listener port. Port 5555 is the default.

           --payload=<type>
               Set the payload of the exported PDU. Default: data.

## [](#EXAMPLES)EXAMPLES

           To see program arguments:

               udpdump --help

           To see program version:

               udpdump --version

           To see interfaces:

               udpdump --extcap-interfaces

           Example output

               interface {value=udpdump}{display=UDP Listener remote capture}

           To see interface DLTs:

               udpdump --extcap-interface=udpdump --extcap-dlts

           Example output

               dlt {number=252}{name=udpdump}{display=Exported PDUs}

           To see interface configuration options:

               udpdump --extcap-interface=udpdump --extcap-config

           Example output

               arg {number=0}{call=--port}{display=Listen port}{type=unsigned}{range=1,65535}{default=5555}{tooltip=The port the receiver listens on}

           To capture:

               udpdump --extcap-interface=randpkt --fifo=/tmp/randpkt.pcapng --capture

               Note

               To stop capturing CTRL+C/kill/terminate the application.

## [](#SEE_ALSO)SEE ALSO

           wireshark(1), tshark(1), dumpcap(1), extcap(4)

## [](#NOTES)NOTES

           udpdump is part of the Wireshark distribution. The latest version
           of Wireshark can be found at https://www.wireshark.org.

           HTML versions of the Wireshark project man pages are available at
           https://www.wireshark.org/docs/man-pages.

## [](#AUTHORS)AUTHORS

           Original Author
           Dario Lombardo <lomato[AT]gmail.com>.SH COLOPHON This page is part
           of the wireshark (Interactively dump and analyze network traffic)
           project. Information about the project can be found at 
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

                                    2025-03-07                     UDPDUMP(1)

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
