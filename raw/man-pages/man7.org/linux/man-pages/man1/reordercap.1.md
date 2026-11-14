---
{"title": "reordercap(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/reordercap.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# reordercap(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DIAGNOSTIC OPTIONS](#DIAGNOSTIC_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    REORDERCAP(1)                                               REORDERCAP(1)

## [](#NAME)NAME

           reordercap - Reorder input file by timestamp into output file

## [](#SYNOPSIS)SYNOPSIS

           reordercap [ -n ] <infile> <outfile>

           reordercap -h|--help

           reordercap -v|--version

## [](#DESCRIPTION)DESCRIPTION

           Reordercap is a program that reads an input capture file and
           rewrites the frames to an output capture file, but with the frames
           sorted by increasing timestamp.

           This functionality may be useful when capture files have been
           created by combining frames from more than one well-synchronised
           source, but the frames have not been combined in strict time
           order.

           Reordercap writes the output capture file in the same format as
           the input capture file.

           Reordercap is able to detect, read and write the same capture
           files that are supported by Wireshark. The input file doesn’t need
           a specific filename extension; the file format and an optional
           gzip, zstd or lz4 compression will be automatically detected. Near
           the beginning of the DESCRIPTION section of wireshark(1) or
           https://www.wireshark.org/docs/man-pages/wireshark.html is a
           detailed description of the way Wireshark handles this, which is
           the same way reordercap handles this.

## [](#OPTIONS)OPTIONS

           -h|--help
               Print the version number and options and exit.

           -n
               When the -n option is used, reordercap will not write out the
               output file if it finds that the input file is already in
               order.

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

## [](#SEE_ALSO)SEE ALSO

           pcap(3), wireshark(1), tshark(1), dumpcap(1), editcap(1),
           mergecap(1), text2pcap(1), pcap-filter(7) or tcpdump(8)

## [](#NOTES)NOTES

           This is the manual page for Reordercap 4.7.3. Reordercap is part
           of the Wireshark distribution. The latest version of Wireshark can
           be found at https://www.wireshark.org.

           It may make sense to move this functionality into editcap, or
           perhaps mergecap, in which case reordercap could be retired.

           HTML versions of the Wireshark project man pages are available at
           https://www.wireshark.org/docs/man-pages.

## [](#AUTHORS)AUTHORS

           Original Author
           Martin Mathieson <martin.r.mathieson[AT]googlemail.com>.SH
           COLOPHON This page is part of the wireshark (Interactively dump
           and analyze network traffic) project. Information about the
           project can be found at ⟨https://www.wireshark.org/⟩. If you have
           a bug report for this manual page, see
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

                                    2025-03-07                  REORDERCAP(1)

------------------------------------------------------------------------

Pages that refer to this page: [editcap(1)](../man1/editcap.1.html)

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
