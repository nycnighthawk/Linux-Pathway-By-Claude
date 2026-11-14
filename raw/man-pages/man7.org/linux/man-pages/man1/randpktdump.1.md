---
{"title": "randpktdump(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/randpktdump.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# randpktdump(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RANDPKTDUMP(1)                                             RANDPKTDUMP(1)

## [](#NAME)NAME

           randpktdump - Provide an interface to generate random captures
           using randpkt

## [](#SYNOPSIS)SYNOPSIS

           randpktdump [ --help ] [ --version ] [ --extcap-interfaces ] [
           --extcap-dlts ] [ --extcap-interface=<interface> ] [
           --extcap-config ] [ --capture ] [ --fifo=<path to file or pipe> ]
           [ --maxbytes=<bytes> ] [ --count=<num> ] [ --delay=<ms> ] [
           --random-type=<true|false> ] [ --all-random=<true|false> ] [
           --type=<packet type> ]

## [](#DESCRIPTION)DESCRIPTION

           randpktdump is a extcap tool that provides access to the random
           packet generator (randpkt). It is mainly used for testing and
           educational purpose.

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

           --maxbytes=<bytes>
               Set the max number of bytes per packet.

           --count=<num>
               Number of packets to generate (-1 for infinite).

           --delay=<ms>
               Wait a number of milliseconds after writing each packet.

           --random-type
               Choose a random packet type for all packets if set to true.

           --all-random
               Choose a different random packet type for each packet if set
               to true.

           --type=<packet type>
               Use the selected packet type. To list all the available packet
               type, run randpktdump --help.

## [](#EXAMPLES)EXAMPLES

           To see program arguments:

               randpktdump --help

           To see program version:

               randpktdump --version

           To see interfaces:

               randpktdump --extcap-interfaces

           Example output

               interface {value=randpkt}{display=Random packet generator}

           To see interface DLTs:

               randpktdump --extcap-interface=randpkt --extcap-dlts

           Example output

               dlt {number=1}{name=randpkt}{display=Ethernet}

           To see interface configuration options:

               randpktdump --extcap-interface=randpkt --extcap-config

           Example output

               arg {number=0}{call=--maxbytes}{display=Max bytes in a packet}{type=unsigned}{range=1,5000}{default=5000}{tooltip=The max number of bytes in a packet}
               arg {number=1}{call=--count}{display=Number of packets}{type=long}{default=1000}{tooltip=Number of packets to generate (-1 for infinite)}
               arg {number=2}{call=--delay}{display=Packet delay (ms)}{type=long}{default=0}{tooltip=Milliseconds to wait after writing each packet}
               arg {number=3}{call=--random-type}{display=Random type}{type=boolflag}{default=false}{tooltip=The packets type is randomly chosen}
               arg {number=4}{call=--all-random}{display=All random packets}{type=boolflag}{default=false}{tooltip=Packet type for each packet is randomly chosen}
               arg {number=5}{call=--type}{display=Type of packet}{type=selector}{tooltip=Type of packet to generate}
               value {arg=5}{value=arp}{display=Address Resolution Protocol}
               [...]
               value {arg=5}{value=usb-linux}{display=Universal Serial Bus with Linux specific header}

           To capture:

               randpktdump --extcap-interface=randpkt --fifo=/tmp/randpkt.pcapng --capture

               Note

               To stop capturing CTRL+C/kill/terminate the application.

## [](#SEE_ALSO)SEE ALSO

           wireshark(1), tshark(1), dumpcap(1), extcap(4), randpkt(1)

## [](#NOTES)NOTES

           randpktdump is part of the Wireshark distribution. The latest
           version of Wireshark can be found at https://www.wireshark.org.

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

                                    2025-03-07                 RANDPKTDUMP(1)

------------------------------------------------------------------------

Pages that refer to this page: [extcap(4)](../man4/extcap.4.html)

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
