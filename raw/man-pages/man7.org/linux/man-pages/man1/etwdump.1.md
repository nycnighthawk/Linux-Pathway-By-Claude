---
{"title": "etwdump(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/etwdump.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# etwdump(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ETWDUMP(1)                                                     ETWDUMP(1)

## [](#NAME)NAME

           etwdump - Provide an interface to read Event Tracing for Windows
           (ETW)

## [](#SYNOPSIS)SYNOPSIS

           etwdump [ --help ] [ --version ] [ --extcap-interfaces ] [
           --extcap-dlts ] [ --extcap-interface=<interface> ] [
           --extcap-config ] [ --capture ] [ --fifo=<path to file or pipe> ]
           [ --iue=<Should undecidable events be included> ] [ --etlfile=<etl
           file> ] [ --params=<filter parameters> ]

## [](#DESCRIPTION)DESCRIPTION

           etwdump is a extcap tool that provides access to a event trace log
           file or an event trace live session. It is only used to display
           event trace on Windows that includes readable text message and
           different protocols (like MBIM and IP packets).

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

           --iue=<Should undecidable events be included>
               Choose if the undecidable event is included.

           --etlfile=<Etl file>
               Select etl file to display in Wireshark.

           --params=<filter parameters>
               Input providers, keyword and level filters for the etl file
               and live session.

## [](#EXAMPLES)EXAMPLES

           To see program arguments:

               etwdump --help

           To see program version:

               etwdump --version

           To see interfaces:

               etwdump --extcap-interfaces

           Example output

               interface {value=etwdump}{display=ETW reader}

           To see interface DLTs:

               etwdump --extcap-interface=etwdump --extcap-dlts

           Example output

               dlt {number=1}{name=etwdump}{display=DLT_ETW}

           To see interface configuration options:

               etwdump --extcap-interface=etwdump --extcap-config

           Example output

               arg {number=0}{call=--etlfile}{display=etl file}{type=fileselect}{tooltip=Select etl file to display in Wireshark}{group=Capture}
               arg {number=1}{call=--params}{display=filter parameters}{type=string}{tooltip=Input providers, keyword and level filters for the etl file and live session}{group=Capture}
               arg {number=2}{call=--iue}{display=Should undecidable events be included}{type=boolflag}{default=false}{tooltip=Choose if the undecidable event is included}{group=Capture}

           To capture:

               etwdump --extcap-interface etwdump --fifo=/tmp/etw.pcapng --capture --params "--p=Microsoft-Windows-Wmbclass-Opn --p=Microsoft-Windows-wmbclass --k=0xff --l=4"
               etwdump --extcap-interface etwdump --fifo=/tmp/etw.pcapng --capture --params "--p=Microsoft-Windows-Wmbclass-Opn --p=Microsoft-Windows-NDIS-PacketCapture"

               Note

               To stop capturing CTRL+C/kill/terminate the application.

## [](#SEE_ALSO)SEE ALSO

           wireshark(1), tshark(1), dumpcap(1), extcap(4)

## [](#NOTES)NOTES

           etwdump is part of the Wireshark distribution. The latest version
           of Wireshark can be found at https://www.wireshark.org.

           HTML versions of the Wireshark project man pages are available at
           https://www.wireshark.org/docs/man-pages.

## [](#AUTHORS)AUTHORS

           Original Author
           Odysseus Yang
           wiresharkyyh@outlook.com This page is part of the wireshark
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

                                    2025-03-07                     ETWDUMP(1)

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
