---
{"title": "dpauxmon(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dpauxmon.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dpauxmon(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DPAUXMON(1)                                                   DPAUXMON(1)

## [](#NAME)NAME

           dpauxmon - Provide interfaces to capture DisplayPort AUX channel
           data.

## [](#SYNOPSIS)SYNOPSIS

           dpauxmon [ --help ] [ --version ] [ --extcap-interfaces ] [
           --extcap-dlts ] [ --extcap-interface=<interface> ] [
           --extcap-config ] [ --extcap-capture-filter=<capture filter> ] [
           --capture ] [ --fifo=<path to file or pipe> ] [
           --interface_id=<Interface ID to capture> ]

           dpauxmon --extcap-interfaces

           dpauxmon --extcap-interface=<interface> --extcap-dlts

           dpauxmon --extcap-interface=<interface> --extcap-config

           dpauxmon --extcap-interface=<interface> --fifo=<path to file or
           pipe> --capture --interface_id=interface_id

## [](#DESCRIPTION)DESCRIPTION

           dpauxmon is an extcap tool that can capture DisplayPort AUX
           channel data from linux kernel drivers using the generic netlink
           interface.

           Supported interfaces:

            1. dpauxmon

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
               Start capturing from specified interface and save it in place
               specified by --fifo.

           --fifo=<path to file or pipe>
               Save captured packet to file or send it through pipe.

           --interface_idt=<interface id>
               The interface for capture.

## [](#EXAMPLES)EXAMPLES

           To see program arguments:

               dpauxmon --help

           To see program version:

               dpauxmon --version

           To see interfaces:

               dpauxmon --extcap-interfaces

           Only one interface (dpauxmon) is supported.

           Example output

               interface {value=dpauxmon}{display=DisplayPort AUX channel capture}

           To see interface DLTs:

               dpauxmon --extcap-interface=dpauxmon --extcap-dlts

           Example output

               dlt {number=275}{name=dpauxmon}{display=DisplayPort AUX channel monitor DLT}

           To see interface configuration options:

               dpauxmon --extcap-interface=dpauxmon --extcap-config

           Example output

               dpauxmon --extcap-interface=dpauxmon --extcap-config
               arg {number=0}{call=--interface_id}{display=Interface Id}
                   {type=unsigned}{tooltip=The Interface Id}
                   {required=true}

           To capture:

               dpauxmon --extcap-interface=dpauxmon --fifo=/tmp/dpauxmon.pcap --capture --interface_id 0

## [](#SEE_ALSO)SEE ALSO

           wireshark(1), tshark(1), dumpcap(1), extcap(4)

## [](#NOTES)NOTES

           dpauxmon is part of the Wireshark distribution. The latest version
           of Wireshark can be found at https://www.wireshark.org.

           HTML versions of the Wireshark project man pages are available at
           https://www.wireshark.org/docs/man-pages.

## [](#AUTHORS)AUTHORS

           Original Author
           Dirk Eibach <dirk.eibach[AT]gdsys.cc>.SH COLOPHON This page is
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

                                    2025-03-07                    DPAUXMON(1)

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
