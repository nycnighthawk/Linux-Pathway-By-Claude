---
{"title": "mergecap(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/mergecap.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mergecap(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DIAGNOSTIC OPTIONS](#DIAGNOSTIC_OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MERGECAP(1)                                                   MERGECAP(1)

## [](#NAME)NAME

           mergecap - Merges two or more capture files into one

## [](#SYNOPSIS)SYNOPSIS

           mergecap [ -a ] [ -F <file format> ] [ -I <IDB merge mode> ] [ -s
           <snaplen> ] [ -V ] [ --no-merging-comment ] -w <outfile>|-
           <infile> [<infile> ...]

           mergecap -h|--help

           mergecap -v|--version

## [](#DESCRIPTION)DESCRIPTION

           Mergecap is a program that combines multiple saved capture files
           into a single output file specified by the -w argument. Mergecap
           knows how to read pcap and pcapng capture files, including those
           of tcpdump, Wireshark and other tools that write captures in those
           formats.

           By default, Mergecap writes the capture file in pcapng format, and
           writes all of the packets from the input capture files to the
           output file.

           Mergecap is able to detect, read and write the same capture files
           that are supported by Wireshark. The input files don’t need a
           specific filename extension; the file format and an optional gzip,
           zstd or lz4 compression will be automatically detected. Near the
           beginning of the DESCRIPTION section of wireshark(1) or
           https://www.wireshark.org/docs/man-pages/wireshark.html is a
           detailed description of the way Wireshark handles this, which is
           the same way Mergecap handles this.

           Mergecap can write the file in several output formats. The -F flag
           can be used to specify the format in which to write the capture
           file, mergecap -F provides a list of the available output formats.

           Packets from the input files are merged in chronological order
           based on each frame’s timestamp, unless the -a flag is specified.
           Mergecap assumes that frames within a single capture file are
           already stored in chronological order. When the -a flag is
           specified, packets are copied directly from each input file to the
           output file, independent of each frame’s timestamp.

           The output file frame encapsulation type is set to the type of the
           input files if all input files have the same type. If not all of
           the input files have the same frame encapsulation type, the output
           file type is set to WTAP_ENCAP_PER_PACKET. Note that some capture
           file formats, most notably pcap, do not currently support
           WTAP_ENCAP_PER_PACKET. This combination will cause the output file
           creation to fail.

## [](#OPTIONS)OPTIONS

           -a

               Causes the frame timestamps to be ignored, writing all packets
               from the first input file followed by all packets from the
               second input file. By default, when -a is not specified, the
               contents of the input files are merged in chronological order
               based on each frame’s timestamp.

               Note: when merging, mergecap assumes that packets within a
               capture file are already in chronological order.

           -F  <file format>

               Sets the file format of the output capture file. Mergecap can
               write the file in several formats; mergecap -F provides a list
               of the available output formats. By default this is the pcapng
               format.

           -h|--help
               Print the version number and options and exit.

           -I  <IDB merge mode>

               Sets the Interface Description Block (IDB) merge mode to use
               during merging. mergecap -I provides a list of the available
               IDB merge modes.

               Every input file has one or more IDBs, which describe the
               interface(s) the capture was performed on originally. This
               includes encapsulation type, interface name, etc. When
               mergecap merges multiple input files, it has to merge these
               IDBs somehow for the new merged output file. This flag
               controls how that is accomplished. The currently available
               modes are:

               none: No merging of IDBs is performed, and instead all IDBs
               are copied to the merged output file.

               all: IDBs are merged only if all input files have the same
               number of IDBs, and each IDB matches their respective entry in
               the other files. (Only the IDBs that occur at the beginning of
               the files, before any packet blocks, are compared. IDBs that
               occur later in the files are merged with duplicates iff the
               initial IDBs were merged.) This is the default mode.

               any: Any and all duplicate IDBs are merged into one IDB,
               regardless of what file they are in.

               Note that an IDB is only considered a matching duplicate if it
               has the same encapsulation type, name, speed, time precision,
               comments, description, etc.

           -s  <snaplen>

               Sets the snapshot length to use when writing the data. If the
               -s flag is used to specify a snapshot length, frames in the
               input file with more captured data than the specified snapshot
               length will have only the amount of data specified by the
               snapshot length written to the output file. This may be useful
               if the program that is to read the output file cannot handle
               packets larger than a certain size (for example, the versions
               of snoop in Solaris 2.5.1 and Solaris 2.6 appear to reject
               Ethernet frames larger than the standard Ethernet MTU, making
               them incapable of handling gigabit Ethernet captures if jumbo
               frames were used).

           -v|--version
               Print the full version information and exit.

           -V
               Causes mergecap to print a number of messages while it’s
               working.

           -w  <outfile>|-
               Sets the output filename. If the name is '-', stdout will be
               used. If the --compress option is not given, then the filename
               extension is used to deduce the desired compression method, if
               any; e.g., if the name has the extension '.gz', then the
               output file is compressed to a gzip archive. This setting is
               mandatory.

           --compress <type>

               Compress the output file using the type compression format.
               --compress with no argument provides a list of the compression
               formats supported for writing. The type given takes precedence
               over the extension of outfile.

           --no-merging-comment

               Inhibit generating the capture comment "File created by
               merging:...". to the output file

               By default a multiline capture comment is generated to the
               output (merged) file that lists all of the files being merged.
               However, if the generated capture comment is longer than 65535
               bytes it is silently dropped.

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

           To merge two capture files together into a third capture file, in
           which the last packet of one file arrives 100 seconds before the
           first packet of another file, use the following sequence of
           commands.

           First, use:

               capinfos -aeS a.pcap b.pcap

           to determine the start and end times of the two capture files, as
           seconds since January 1, 1970, 00:00:00 UTC.

           If a.pcap starts at 1009932757 and b.pcap ends at 873660281, then
           the time adjustment to b.pcap that would make it end 100 seconds
           before a.pcap begins would be 1009932757 - 873660281 - 100 =
           136272376 seconds.

           Thus, the next step would be to use:

               editcap -t 136272376 b.pcap b-shifted.pcap

           to generate a version of b.pcap with its time stamps shifted
           136272376 ahead.

           Then the final step would be to use :

               mergecap -w compare.pcap a.pcap b-shifted.pcap

           to merge a.pcap and the shifted b.pcap into compare.pcap.

## [](#SEE_ALSO)SEE ALSO

           pcap(3), wireshark(1), tshark(1), dumpcap(1), editcap(1),
           text2pcap(1), pcap-filter(7) or tcpdump(8)

## [](#NOTES)NOTES

           Mergecap is based heavily upon editcap by Richard Sharpe
           <sharpe[AT]ns.aus.com> and Guy Harris <guy[AT]alum.mit.edu>.

           This is the manual page for Mergecap 4.7.3. Mergecap is part of
           the Wireshark distribution. The latest version of Wireshark can be
           found at https://www.wireshark.org.

           HTML versions of the Wireshark project man pages are available at
           https://www.wireshark.org/docs/man-pages.

## [](#AUTHORS)AUTHORS

           Original Author
           Scott Renfro <scott[AT]renfro.org>

           Contributors
           Bill Guyton <guyton[AT]bguyton.com>.SH COLOPHON This page is part
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

                                    2026-01-15                    MERGECAP(1)

------------------------------------------------------------------------

Pages that refer to this page: [capinfos(1)](../man1/capinfos.1.html),  [captype(1)](../man1/captype.1.html),  [dumpcap(1)](../man1/dumpcap.1.html),  [editcap(1)](../man1/editcap.1.html),  [reordercap(1)](../man1/reordercap.1.html),  [sharkd(1)](../man1/sharkd.1.html),  [stratoshark(1)](../man1/stratoshark.1.html),  [text2pcap(1)](../man1/text2pcap.1.html),  [tshark(1)](../man1/tshark.1.html),  [wireshark(1)](../man1/wireshark.1.html),  [netsniff-ng(8)](../man8/netsniff-ng.8.html)

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
