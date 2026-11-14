---
{"title": "sdjournal(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/sdjournal.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sdjournal(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SDJOURNAL(1)                                                 SDJOURNAL(1)

## [](#NAME)NAME

           sdjournal - Provide an interface to capture systemd journal
           entries.

## [](#SYNOPSIS)SYNOPSIS

           sdjournal [ --help ] [ --version ] [ --extcap-interfaces ] [
           --extcap-dlts ] [ --extcap-interface=<interface> ] [
           --extcap-config ] [ --capture ] [ --fifo=<path to file or pipe> ]
           [ --start-from=<entry count> ]

## [](#DESCRIPTION)DESCRIPTION

           sdjournal is an extcap tool that allows one to capture systemd
           journal entries. It can be used to correlate system events with
           network traffic.

           Supported interfaces:

            1. sdjournal

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
               Start capturing from specified interface and write raw packet
               data to the location specified by --fifo.

           --fifo=<path to file or pipe>
               Save captured packet to file or send it through pipe.

           --start-from=<entry count>

               Start from the last <entry count> entries, similar to the "-n"
               or "--lines" argument for the tail(1) command. Values prefixed
               with a + sign start from the beginning of the journal,
               otherwise the count starts from the end. The default value is
               10. To include all entries use +0.

## [](#EXAMPLES)EXAMPLES

           To see program arguments:

               sdjournal --help

           To see program version:

               sdjournal --version

           To see interfaces:

               sdjournal --extcap-interfaces

           Only one interface (sdjournal) is supported.

           Example output

               interface {value=sdjournal}{display=systemd journal capture}

           To see interface DLTs:

               sdjournal --extcap-interface=sdjournal --extcap-dlts

           Example output

               dlt {number=147}{name=sdjournal}{display=USER0}

           To see interface configuration options:

               sdjournal --extcap-interface=sdjournal --extcap-config

           Example output

               arg {number=0}{call=--start-from}{display=Starting position}{type=string}
                   {tooltip=The journal starting position. Values with a leading "+" start from the beginning, similar to the "tail" command}

           To capture:

               sdjournal --extcap-interface=sdjournal --fifo=/tmp/sdjournal.pcap --capture

           To capture all entries since the system was booted:

               sdjournal --extcap-interface=sdjournal --fifo=/tmp/sdjournal.pcap --capture --start-from +0

               Note

               To stop capturing CTRL+C/kill/terminate the application.

## [](#SEE_ALSO)SEE ALSO

           wireshark(1), tshark(1), dumpcap(1), extcap(4), tcpdump(1)

## [](#NOTES)NOTES

           sdjournal is part of the Wireshark distribution. The latest
           version of Wireshark can be found at https://www.wireshark.org.

           HTML versions of the Wireshark project man pages are available at
           https://www.wireshark.org/docs/man-pages.

## [](#AUTHORS)AUTHORS

           Original Author
           Gerald Combs <gerald[AT]wireshark.org>.SH COLOPHON This page is
           part of the wireshark (Interactively dump and analyze network
           traffic) project. Information about the project can be found at 
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

                                    2025-03-07                   SDJOURNAL(1)

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
