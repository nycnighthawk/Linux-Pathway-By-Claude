---
{"title": "strato(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/strato.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# strato(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DISSECTION OPTIONS](#DISSECTION_OPTIONS) \| [DIAGNOSTIC OPTIONS](#DIAGNOSTIC_OPTIONS) \| [FILES](#FILES) \| [OUTPUT](#OUTPUT) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STRATO(1)                                                       STRATO(1)

## [](#NAME)NAME

           strato - Dump and analyze system calls and event logs

## [](#SYNOPSIS)SYNOPSIS

           strato [ -i <capture source>|- ] [ -f <capture filter> ] [ -2 ] [
           -r <infile> ] [ -w <outfile>|- ] [ options ] [ <filter> ]

           strato -h|--help

           strato -v|--version

## [](#DESCRIPTION)DESCRIPTION

           strato is a system call and log analyzer. It lets you capture
           system call and log events from a live source, or read events from
           a previously saved capture file, either printing a decoded form of
           those events to the standard output or writing the packets to a
           file. strato's native capture file format is scap format, which is
           also the format used by Stratoshark, Falco, sysdig and various
           other tools.

           Without any options set, strato will work much like sysdig. It
           will use the libscap and libsinsp to capture traffic from the
           first available source and displays a summary line on the standard
           output for each received packet.

           When run with the -r option, specifying a capture file from which
           to read, strato will again work much like sysdig, reading packets
           from the file and displaying a summary line on the standard output
           for each packet read. strato is able to detect, read and write the
           same capture files that are supported by Stratoshark. The input
           file doesn’t need a specific filename extension; the file format
           and an optional gzip, Zstandard, or LZ4 compression will be
           automatically detected. Near the beginning of the DESCRIPTION
           section of wireshark(1) or
           https://www.wireshark.org/docs/man-pages/wireshark.html is a
           detailed description of the way Wireshark handles this, which is
           the same way strato handles this.

           Compressed file support uses (and therefore requires) the zlib
           library. If the zlib library is not present when compiling strato,
           it will be possible to compile it, but the resulting program will
           be unable to read compressed files. Similarly, LZ4 and ZStandard
           also require their respective libraries.

           When displaying events on the standard output, strato writes, by
           default, a summary line containing the fields specified by the
           preferences file (which are also the fields displayed in the
           packet list pane in Wireshark), although if it’s writing packets
           as it captures them, rather than writing packets from a saved
           capture file, it won’t show the "frame number" field. If the -V
           option is specified, it instead writes a view of the details of
           the packet, showing all the fields of all protocols in the packet.
           If the -O option is specified, it will only show the full details
           for the protocols specified, and show only the top-level detail
           line for all other protocols. Use the output of "strato -G
           protocols" to find the abbreviations of the protocols you can
           specify. If the -P option is specified with either the -V or -O
           options, both the summary line for the entire packet and the
           details will be displayed.

           Packet capturing is performed with the pcap library. That library
           supports specifying a filter expression; packets that don’t match
           that filter are discarded. The -f option is used to specify a
           capture filter. The syntax of a capture filter is defined by the
           pcap library; this syntax is different from the display filter
           syntax described below, and the filtering mechanism is limited in
           its abilities.

           Display filters in strato, which allow you to select which packets
           are to be decoded or written to a file, are very powerful; more
           fields are filterable in strato than in other protocol analyzers,
           and the syntax you can use to create your filters is richer. As
           strato progresses, expect more and more protocol fields to be
           allowed in display filters. Display filters use the same syntax as
           display and color filters in Wireshark; a display filter is
           specified with the -Y option.

           Display filters can be specified when capturing or when reading
           from a capture file. Note that capture filters are much more
           efficient than display filters, and it may be more difficult for
           strato to keep up with a busy network if a display filter is
           specified for a live capture, so you might be more likely to lose
           packets if you’re using a display filter.

           A capture or display filter can either be specified with the -f or
           -Y option, respectively, in which case the entire filter
           expression must be specified as a single argument (which means
           that if it contains spaces, it must be quoted), or can be
           specified with command-line arguments after the option arguments,
           in which case all the arguments after the filter arguments are
           treated as a filter expression. If the filter is specified with
           command-line arguments after the option arguments, it’s a capture
           filter if a capture is being done (i.e., if no -r option was
           specified) and a display filter if a capture file is being read
           (i.e., if a -r option was specified).

           If the -w option is specified when capturing packets or reading
           from a capture file, strato does not display packets on the
           standard output. Instead, it writes the packets to a capture file
           with the name specified by the -w option. Note that display
           filters are currently not supported when capturing and saving the
           captured packets.

           If you want to write the decoded form of packets to a file, run
           strato without the -w option, and redirect its standard output to
           the file (do not use the -w option).

           If you want the packets to be displayed to the standard output and
           also saved to a file, specify the -P option in addition to the -w
           option to have the summary line displayed, specify the -V option
           in addition to the -w option to have the details of the packet
           displayed, and specify the -O option, with a list of protocols, to
           have the full details of the specified protocols and the top-level
           detail line for all other protocols to be displayed. If the -P
           option is used together with the -V or -O option, the summary line
           will be displayed along with the detail lines.

           When writing packets to a file, strato, by default, writes the
           file in pcapng format, and writes all of the packets it sees to
           the output file. The -F option can be used to specify the format
           in which to write the file. The list of available file formats is
           displayed by the -F option without a value. However, for a live
           capture, you can only specify a file format supported by
           dumpcap(1), viz. pcapng or pcap. The --compress option can be used
           to specify a compression method as well; the list of supported
           compression methods for writing can be displayed by the --compress
           method without an argument. If the --compress option is not given,
           then the desired compression method, if any, is deduced from the
           extension of the filename given as argument to the -w option.

           When capturing packets, strato writes to the standard error an
           initial line listing the interfaces from which packets are being
           captured and, if packet information isn’t being displayed to the
           terminal, writes a continuous count of packets captured to the
           standard output. If the -q option is specified, neither the
           continuous count nor the packet information will be displayed;
           instead, at the end of the capture, a count of packets captured
           will be displayed. If the -Q option is specified, neither the
           initial line, nor the packet information, nor any packet counts
           will be displayed. If the -q or -Q option is used, the -P, -V, or
           -O option can be used to cause the corresponding output to be
           displayed even though other output is suppressed.

           When reading packets, the -q and -Q option will suppress the
           display of the packet summary or details; this would be used if -z
           options are specified in order to display statistics, so that only
           the statistics, not the packet information, is displayed.

           The -G option is a special mode that simply causes strato to dump
           one of several types of internal glossaries and then exit.

## [](#OPTIONS)OPTIONS

           -2

               Perform a two-pass analysis. This causes strato to buffer
               output until the entire first pass is done, but allows it to
               fill in fields that require future knowledge, such as
               'response in frame #' fields. Also permits reassembly frame
               dependencies to be calculated correctly. This requires the
               ability to seek backwards on the input, and as such cannot be
               used with live captures or when reading from a pipe or FIFO.

           -a|--autostop  <capture autostop condition>

               Specify a criterion that specifies when strato is to stop
               writing to a capture file. The criterion is of the form
               test:value, where test is one of:

               duration:value Stop writing to a capture file after value
               seconds have elapsed. Floating point values (e.g. 0.5) are
               allowed.

               files:value Stop writing to capture files after value number
               of files were written.

               filesize:value Stop writing to a capture file after it reaches
               a size of value kB. If this option is used together with the
               -b option, strato will stop writing to the current capture
               file and switch to the next one if filesize is reached. When
               reading a capture file, strato will stop reading the file
               after the number of bytes read exceeds this number (the
               complete packet  will be read, so more bytes than this number
               may be read). Note that the filesize is limited to a maximum
               value of 2 TB, although you might have problems before then if
               the number of packets exceeds exceeds 232 (4294967296).

               packets:value switch to the next file after it contains value
               packets. This does not include any packets that do not pass
               the display filter, so it may differ from -c<capture packet
               count>.

           -A  <user>:<password>

               Specify a user and a password when strato captures from a
               rpcap:// interface where authentication is required.

               This option is available with libpcap with enabled remote
               support.

           -b|--ring-buffer  <capture ring buffer option>

               Cause strato to run in "multiple files" mode. In "multiple
               files" mode, strato will write to several capture files. When
               the first capture file fills up, strato will switch writing to
               the next file and so on.

               The created filenames are based on the filename given with the
               -w option, the number of the file and on the creation date and
               time, e.g. outfile_00001_20260714120117.pcap,
               outfile_00002_20260714120523.pcap, ...

               With the files option it’s also possible to form a "ring
               buffer". This will fill up new files until the number of files
               specified, at which point strato will discard the data in the
               first file and start writing to that file and so on. If the
               files option is not set, new files filled up until one of the
               capture stop conditions match (or until the disk is full).

               The criterion is of the form key:value, where key is one of:

               duration:value switch to the next file after value seconds
               have elapsed, even if the current file is not completely
               filled up. Floating point values (e.g. 0.5) are allowed.

               files:value begin again with the first file after value number
               of files were written (form a ring buffer). This value must be
               less than 100000. Caution should be used when using large
               numbers of files: some filesystems do not handle many files in
               a single directory well. The files criterion requires either
               duration, interval or filesize to be specified to control when
               to go to the next file. It should be noted that each -b
               parameter takes exactly one criterion; to specify two
               criterion, each must be preceded by the -b option.

               filesize:value switch to the next file after it reaches a size
               of value kB. Note that the filesize is limited to a maximum
               value of 2 TB, although you might have problems before then if
               the number of packets exceeds exceeds 232 (4294967296).

               interval:value switch to the next file when the time is an
               exact multiple of value seconds. For example, use 3600 to
               switch to a new file every hour on the hour.

               packets:value switch to the next file after it contains value
               packets.

               printname:filename print the name of the most recently written
               file to filename after the file is closed. filename can be
               stdout or - for standard output, or stderr for standard error.

               nametimenum:value Choose between two save filename templates.
               If value is 1, make running file number part before start time
               part; this is the original and default behaviour (e.g.
               log_00001_20260714164426.pcap). If value is greater than 1,
               make start time part before running number part (e.g.
               log_20210828164426_00001.pcap). The latter makes alphabetical
               sorting order equal to creation time order, and keeps related
               multiple file sets in same directory close to each other.

               Example: strato -b filesize:1000 -b files:5 results in a ring
               buffer of five files of size one megabyte each.

           -B|--buffer-size  <capture buffer size>

               Set capture buffer size (in MiB, default is 2 MiB). This is
               used by the capture driver to buffer packet data until that
               data can be written to disk. If you encounter packet drops
               while capturing, try to increase this size. Note that, while
               strato attempts to set the buffer size to 2 MiB by default,
               and can be told to set it to a larger value, the system or
               interface on which you’re capturing might silently limit the
               capture buffer size to a lower value or raise it to a higher
               value.

               This is available on UNIX-compatible systems, such as Linux,
               macOS, \*BSD, Solaris, and AIX, with libpcap 1.0.0 or later,
               and on Windows. It is not available on UNIX-compatible systems
               with earlier versions of libpcap.

               This option can occur multiple times. If used before the first
               occurrence of the -i option, it sets the default capture
               buffer size. If used after an -i option, it sets the capture
               buffer size for the interface specified by the last -i option
               occurring before this option. If the capture buffer size is
               not set specifically, the default capture buffer size is used
               instead.

           -c  <capture packet count>

               Set the maximum number of packets to read when capturing live
               data. If reading a capture file, set the maximum number of
               packets to read. This includes any packets that do not pass
               the display filter, so it may differ from -a packets:<capture
               packet count>.

           -C  <configuration profile>

               Run with the given configuration profile. If used in
               conjunction with --global-profile, then the global profile
               with the associated name would be used.

           -D|--list-interfaces

               Print a list of the interfaces on which strato can capture,
               and exit. For each network interface, a number and an
               interface name, possibly followed by a text description of the
               interface, is printed. The interface name or the number can be
               supplied to the -i flag to specify an interface on which to
               capture. The number can be useful on Windows systems, where
               the interfaces have long names that usually contain a GUID.

           -e  <field>

               Add a field to the list of fields to display if -T
               ek|fields|json|pdml is selected. This option can be used
               multiple times on the command line. At least one field must be
               provided if the -T fields option is selected. Column types may
               be used prefixed with "_ws.col." Prefixing the field name with
               an at sign (@) will display the data as hex bytes.

               Example: strato -T fields -e frame.number -e ip.addr -e udp -e
               _ws.col.info

               Fields are separated by tab characters by default. -E controls
               the format of the printed fields. Giving a protocol rather
               than a single field will print the protocol summary (subtree
               label) from the packet details as a single field. If the
               protocol summary contains only the protocol name (e.g.
               "Hypertext Transfer Protocol") then the protocol filter name
               ("http") will be printed.

           -E  <field print option>

               Set an option controlling the printing of fields when -T
               fields is selected.

               Options are:

               bom=y|n If y, prepend output with the UTF-8 byte order mark
               (hexadecimal ef, bb, bf). Defaults to n.

               header=y|n If y, print a list of the field names given using
               -e as the first line of the output; the field name will be
               separated using the same character as the field values.
               Defaults to n.

               separator=/t|/s|<character> Set the separator character to use
               for fields. If /t tab will be used (this is the default), if
               /s, a single space will be used. Otherwise any character that
               can be accepted by the command line as part of the option may
               be used.

               occurrence=f|l|a Select which occurrence to use for fields
               that have multiple occurrences. If f the first occurrence will
               be used, if l the last occurrence will be used and if a all
               occurrences will be used (this is the default).

               aggregator=,|/s|<character> Set the aggregator character to
               use for fields that have multiple occurrences. If , a comma
               will be used (this is the default), if /s, a single space will
               be used. Otherwise any character that can be accepted by the
               command line as part of the option may be used.

               quote=d|s|n Set the quote character to use to surround fields.
               d uses double-quotes, s single-quotes, n no quotes (the
               default). If the quote character appears in a field value, it
               will be escaped by being duplicated.

               escape=y|n If y, the whitespace control characters (tab, line
               feed, carriage return, form feed, and vertical tab) backspace,
               and the backslash will be replaced in field values by C-style
               escapes, e.g. "\n" for line feed. If n, field value strings
               will be printed as-is. Defaults to y.

           -f  <capture filter>

               Set the capture filter expression.

               This option can occur multiple times. If used before the first
               occurrence of the -i option, it sets the default capture
               filter expression. If used after an -i option, it sets the
               capture filter expression for the interface specified by the
               last -i option occurring before this option. If the capture
               filter expression is not set specifically, the default capture
               filter expression is used if provided.

               Pre-defined capture filter names, as shown in the GUI menu
               item Capture→Capture Filters, can be used by prefixing the
               argument with "predef:". Example: strato -f
               "predef:MyPredefinedHostOnlyFilter"

           -F  <file format>
               Set the file format of the output capture file written using
               the -w option. The output written with the -w option is raw
               packet data, not text, so there is no -F option to request
               text output. The option -F without a value will list the
               available formats. The default is the pcapng format (unless
               the default has been changed in preferences.) .

           -g
               This option causes the output file(s) to be created with
               group-read permission (meaning that the output file(s) can be
               read by other members of the calling user’s group).

           -G  <report type>

               The -G option will cause strato to dump one of several types
               of glossaries and then exit. The glossary type is now
               mandatory; previous versions generated the fields report by
               default when no type was given. With one exception, the
               reports reflect the current configuration, including that
               given by a -C option or as modified by other command line
               options. Using the report type of help lists all the current
               report types.

               The available report types include:

               column-formats Dumps the column formats understood by strato.
               There is one record per line. The fields are tab-delimited.

               Field 1
                   format string (e.g. "%rD")

               Field 2
                   text description of format string (e.g. "Dest port
                   (resolved)")

               Field 3
                   field abbreviation used for the column text (e.g.
                   "_ws.col.res_dst_port")

               This report is followed by a usage example that demonstrates
               how to change the columns by overriding the gui.column.format
               preference value with -o.

               currentprefs  Dumps a copy of the current preferences file to
               stdout.

               decodes Dumps the "layer type"/"decode as" associations to
               stdout. There is one record per line. The fields are
               tab-delimited.

               Field 1
                   layer type, e.g. "tcp.port"

               Field 2
                   selector in decimal

               Field 3
                   "decode as" name, e.g. "http"

               defaultprefs  Dumps a default preferences file to stdout. This
               report is unaffected by other command line arguments.

               dissectors  Dumps a list of registered dissectors to stdout.
               There is one record per line. The fields are tab-delimited.

               Field 1
                   dissector name

               Field 2
                   dissector description

               dissector-tables  Dumps a list of dissector tables to stdout.
               There is one record per line. The fields are tab-delimited.

               Field 1
                   dissector table name, e.g. "tcp.port"

               Field 2
                   name used for the dissector table in the GUI

               Field 3
                   type (textual representation of the ftenum type, or
                   "heuristic")

               Field 4
                   base for display (for integer types)

               Field 5
                   protocol name

               Field 6
                   "decode as" support (for non-heuristic tables)

               elastic-mapping[,filter]  Dumps the ElasticSearch mapping file
               to stdout. Fields falling in the default case (string) won’t
               be mapped.

               filter is an optional list of comma separated protocol filter
               names that limits the generated mapping file to the specified
               protocols, to avoid a huge mapping file that can choke some
               software (such as Kibana). E.g.,

                   strago -G elastic-mapping,ip,udp,dns

               enterprises Dumps the IANA Private Enterprise Number (PEN)
               table.

               fieldcount  Dumps the number of header fields to stdout.

               fields[,prefix]  Dumps the contents of the registration
               database to stdout. An independent program can take this
               output and format it into nice tables or HTML or whatever.
               There is one record per line. Each record is either a protocol
               or a header field, differentiated by the first field. The
               fields are tab-delimited.

               Protocols

               Field 1
                   'P'

               Field 2
                   descriptive protocol name

               Field 3
                   protocol abbreviation

               Header Fields

               Field 1
                   'F'

               Field 2
                   descriptive field name

               Field 3
                   field abbreviation

               Field 4
                   type (textual representation of the ftenum type)

               Field 5
                   parent protocol abbreviation

               Field 6
                   base for display (for integer types); "parent bitfield
                   width" for FT_BOOLEAN

               Field 7
                   bitmask: format: hex: 0x....

               Field 8
                   blurb describing field

               An optional search prefix argument can be given to fields, in
               which case the output is limited to protocols and fields whose
               abbreviation starts with the search prefix.

               Search Output

               Field 1
                   protocol or field abbreviation

               Field 2
                   descriptive protocol or field name

               folders Dumps various folders used by strato. This is
               essentially the same data reported in Wireshark’s About |
               Folders tab. There is one record per line. The fields are
               tab-delimited.

               Field 1
                   Folder type (e.g "Personal configuration:")

               Field 2
                   Folder location (e.g. "/home/vagrant/.config/wireshark/")

               ftypes Dumps the "ftypes" (fundamental types) understood by
               strato. There is one record per line. The fields are
               tab-delimited.

               Field 1
                   FTYPE (e.g "FT_IPv6")

               Field 2
                   text description of type (e.g. "IPv6 address")

               heuristic-decodes Dumps the heuristic decodes currently
               installed. There is one record per line. The fields are
               tab-delimited.

               Field 1
                   heuristic dissector table name (e.g. "tcp")

               Field 2
                   name of heuristic decoder (e.g. "ucp")

               Field 3
                   heuristic enabled (e.g. "T" or "F")

               Field 4
                   heuristic enabled by default (e.g. "T" or "F")

               Field 5
                   heuristic short name (e.g. "ucp_tcp")

               Field 6
                   heuristic display name (e.g. "UCP over TCP")

               help Displays the available report types.

               manuf Dumps the MAC address lookup table in manuf format.

               plugins Dumps the plugins currently installed. There is one
               record per line. The fields are tab-delimited.

               Field 1
                   plugin library/Lua script/extcap executable (e.g.
                   "gryphon.so")

               Field 2
                   plugin version (e.g. 0.0.4)

               Field 3
                   plugin type ("dissector", "tap", "file type", etc.)

               Field 4
                   full path to plugin file

               profiles[,filter]  Dumps a list of profiles. Specific profile
               types can be listed with the "global", "personal", or "all"
               filters. By default, "all" are shown.

               Field 1
                   Profile name

               Field 2
                   Type of profile (personal, global, default)

               protocols Dumps the protocols in the registration database to
               stdout. An independent program can take this output and format
               it into nice tables or HTML or whatever. There is one record
               per line. The fields are tab-delimited.

               Field 1
                   protocol name

               Field 2
                   protocol short name

               Field 3
                   protocol filter name

               Field 4
                   protocol enabled (e.g. "T" or "F")

               Field 5
                   protocol enabled by default (e.g. "T" or "F")

               Field 6
                   protocol can toggle (e.g. "T" or "F")

               services Dumps the TCP, UDP, and SCTP transport service (port)
               table.

               values Dumps the value_strings, range_strings or true/false
               strings for fields that have them. There is one record per
               line. Fields are tab-delimited. There are three types of
               records: Value String, Range String and True/False String. The
               first field, 'V', 'R' or 'T', indicates the type of record.

               Value Strings

               Field 1
                   'V'

               Field 2
                   field abbreviation to which this value string corresponds

               Field 3
                   Integer value

               Field 4
                   String

               Range Strings

               Field 1
                   'R'

               Field 2
                   field abbreviation to which this range string corresponds

               Field 3
                   Integer value: lower bound

               Field 4
                   Integer value: upper bound

               Field 5
                   String

               True/False Strings

               Field 1
                   'T'

               Field 2
                   field abbreviation to which this true/false string
                   corresponds

               Field 3
                   True String

               Field 4
                   False String

           -h|--help
               Print the version number and options and exit.

           -H  <input hosts file>

               Read a list of entries from a "hosts" file, which will then be
               written to a capture file. Implies -W n. Can be called
               multiple times.

               The "hosts" file format is documented at
               https://en.wikipedia.org/wiki/Hosts_(file).

           -i|--interface  <capture interface> | -

               Set the name of the network interface or pipe to use for live
               packet capture.

               Network interface names should match one of the names listed
               in "strato -D" (described above); a number, as reported by
               "strato -D", can also be used.

               If no interface is specified, strato searches the list of
               interfaces, choosing the first non-loopback interface if there
               are any non-loopback interfaces, and choosing the first
               loopback interface if there are no non-loopback interfaces. If
               there are no interfaces at all, strato reports an error and
               doesn’t start the capture.

               Pipe names should be either the name of a FIFO (named pipe) or
               "-" to read data from the standard input. On Windows systems,
               pipe names must be of the form "\\.\pipe\pipename". Data read
               from pipes must be in standard pcapng or pcap format. Pcapng
               data must have the same endianness as the capturing host.

               This option can occur multiple times. When capturing from
               multiple interfaces, the capture file will be saved in pcapng
               format.

           -j  <protocol match filter>

               Protocol match filter used for ek|json|jsonraw|pdml output
               file types. Only the protocol’s parent node is included. Child
               nodes are only included if explicitly specified in the filter.

               Example: strato -T json -j "ip ip.flags http"

           -J  <protocol match filter>

               Protocol top level filter used for ek|json|jsonraw|pdml output
               file types. The protocol’s parent node and all child nodes are
               included. Lower-level protocols must be explicitly specified
               in the filter.

               Example: strato -T pdml -J "tcp http"

           -l

               Flush the standard output after the information for each
               packet is printed. (This is not, strictly speaking,
               line-buffered if -V was specified; however, it is the same as
               line-buffered if -V wasn’t specified, as only one line is
               printed for each packet, and, as -l is normally used when
               piping a live capture to a program or script, so that output
               for a packet shows up as soon as the packet is seen and
               dissected, it should work just as well as true line-buffering.
               We do this as a workaround for a deficiency in the Microsoft
               Visual C++ C library.) This also sets --update-interval to 0
               ms.

               This may be useful when piping the output of strato to another
               program, as it means that the program to which the output is
               piped will see the dissected data for a packet as soon as
               strato sees the packet and generates that output, rather than
               seeing it only when the standard output buffer containing that
               data fills up.

           -L|--list-data-link-types
               List the data link types supported by the interface and exit.
               The reported link types can be used for the -y option.

           -o  <preference>:<value>

               Set a preference value, overriding the default value and any
               value read from a preference file. The argument to the option
               is a string of the form prefname:value, where prefname is the
               name of the preference (which is the same name that would
               appear in the preference file), and value is the value to
               which it should be set.

                   Note

                   strato does not save preferences, so use this for
                   temporary changes for a single execution. To permanently
                   set a preference, change it in the Wireshark GUI or edit
                   the preference file directly, creating multiple
                   configuration profiles if you need different preference
                   sets for different occasions.

           -O  <protocols>

               Similar to the -V option, but causes strato to only show a
               detailed view of the comma-separated list of protocols
               specified, and show only the top-level detail line for all
               other protocols, rather than a detailed view of all protocols.
               Use the output of "strato -G protocols" to find the
               abbreviations of the protocols you can specify.

           -P|--print

               Decode and display the packet summary or details, even if
               writing raw packet data using the -w option, and even if
               packet output is otherwise suppressed with -Q.

           -q

               When capturing packets, don’t display the continuous count of
               packets captured that is normally shown when saving a capture
               to a file; instead, just display, at the end of the capture, a
               count of packets captured. On systems that support the SIGINFO
               signal, such as various BSDs, you can cause the current count
               to be displayed by typing your "status" character (typically
               control-T, although it might be set to "disabled" by default
               on at least some BSDs, so you’d have to explicitly set it to
               use it).

               When reading a capture file, or when capturing and not saving
               to a file, don’t print packet information; this is useful if
               you’re using a -z option to calculate statistics and don’t
               want the packet information printed, just the statistics.

           -Q

               When capturing packets, don’t display, on the standard error,
               the initial message indicating on which interfaces the capture
               is being done, the continuous count of packets captured shown
               when saving a capture to a file, and the final message giving
               the count of packets captured. Only true errors are displayed
               on the standard error.

               This outputs less than the -q option, so the interface name
               and total packet count and the end of a capture are not sent
               to stderr.

               When reading a capture file, or when capturing and not saving
               to a file, don’t print packet information; this is useful if
               you’re using a -z option to calculate statistics and don’t
               want the packet information printed, just the statistics.

           -r|--read-file  <infile>

               Read packet data from infile, can be any supported capture
               file format (including compressed files). It is possible to
               use named pipes or stdin (-) here but only with certain
               capture file formats (in particular: those that can be read
               without seeking backwards.)

                   Tip

                   Reading a live capture from the standard out of another
                   process through a pipe can circumvent restrictions that
                   apply to strato during live capture, such as file formats
                   or compression.

           -R|--read-filter  <Read filter>

               Cause the specified filter (which uses the syntax of
               read/display filters, rather than that of capture filters) to
               be applied during the first pass of analysis. Packets not
               matching the filter are not considered for future passes. Only
               makes sense with multiple passes, see -2. For regular
               filtering on single-pass dissect see -Y instead.

               Note that forward-looking fields such as 'response in frame #'
               cannot be used with this filter, since they will not have been
               calculated when this filter is applied.

           -s|--snapshot-length  <capture snaplen>

               Set the default snapshot length to use when capturing live
               data. No more than snaplen bytes of each network packet will
               be read into memory, or saved to disk. A value of 0 specifies
               a snapshot length of 262144, so that the full packet is
               captured; this is the default.

               This option can occur multiple times. If used before the first
               occurrence of the -i option, it sets the default snapshot
               length. If used after an -i option, it sets the snapshot
               length for the interface specified by the last -i option
               occurring before this option. If the snapshot length is not
               set specifically, the default snapshot length is used if
               provided.

           -S  <separator>
               Set the line separator to be printed between packets.

           -T  ek|fields|json|jsonraw|pdml|ps|psml|tabs|text

               Set the format of the output when viewing decoded packet data.
               The options are one of:

               ek Newline delimited JSON format for bulk import into
               Elasticsearch. It can be used with -j or -J to specify which
               protocols to include or with -x to include raw hex-encoded
               packet data. If -P is specified it will print the packet
               summary only, with both -P and -V it will print the packet
               summary and packet details. If neither -P or -V are used it
               will print the packet details only. Example of usage to import
               data into Elasticsearch:

                   strato -T ek -j "http tcp ip" -P -V -x -r file.pcap > file.json
                   curl -H "Content-Type: application/x-ndjson" -XPOST http://elasticsearch:9200/_bulk --data-binary "@file.json"

               Elastic requires a mapping file to be loaded as template for
               packets-* index in order to convert Wireshark types to elastic
               types. This file can be auto-generated with the command
               "strato -G elastic-mapping". Since the mapping file can be
               huge, protocols can be selected by using the option
               --elastic-mapping-filter:

                   strato -G elastic-mapping --elastic-mapping-filter ip,udp,dns

               or adding the filter directly to the -G elastic-mapping
               option:

                   strato -G elastic-mapping,ip,udp,dns

               fields The values of fields specified with the -e option, in a
               form specified by the -E option. For example,

                   strato -T fields -E separator=, -E quote=d

               would generate comma-separated values (CSV) output suitable
               for importing into your favorite spreadsheet program.

               json JSON file format. It can be used with -j or -J to specify
               which protocols to include or with -x option to include raw
               hex-encoded packet data. Example of usage:

                   strato -T json -r file.pcap
                   strato -T json -j "http tcp ip" -x -r file.pcap

               jsonraw JSON file format including only raw hex-encoded packet
               data. It can be used with -j or -J to specify which protocols
               to include. Example of usage:

                   strato -T jsonraw -r file.pcap
                   strato -T jsonraw -j "http tcp ip" -x -r file.pcap

               pdml Packet Details Markup Language, an XML-based format for
               the details of a decoded packet. This information is
               equivalent to the packet details printed with the -V option.
               Using the --color option will add color attributes to pdml
               output. These attributes are nonstandard.

               ps PostScript for a human-readable one-line summary of each of
               the packets, or a multi-line view of the details of each of
               the packets, depending on whether the -V option was specified.

               psml Packet Summary Markup Language, an XML-based format for
               the summary information of a decoded packet. This information
               is equivalent to the information shown in the one-line summary
               printed by default. Using the --color option will add color
               attributes to pdml output. These attributes are nonstandard.

               tabs Similar to the default text report except the
               human-readable one-line summary of each packet will include an
               ASCII horizontal tab (0x09) character as a delimiter between
               each column.

               text Text of a human-readable one-line summary of each of the
               packets, or a multi-line view of the details of each of the
               packets, depending on whether the -V option was specified.
               This is the default.

           --temp-dir <directory>

               Specifies the directory into which temporary files (including
               capture files) are to be written. The default behavior on
               UNIX-compatible systems, such as Linux, macOS, \*BSD, Solaris,
               and AIX, is to use the environment variable $TMPDIR if set,
               and the system default, typically /tmp, if it is not. On
               Windows, the %TEMP% environment variable is used, which
               typically defaults to %USERPROFILE%\AppData\Local\Temp.

           -U <tap name>

               PDUs export, exports PDUs from infile to outfile according to
               the tap name given. Use -Y to filter.

               Enter an empty tap name "" or a tap name of ? to get a list of
               available names.

           -v|--version
               Print the full version information and exit.

           -V
               Cause strato to print a view of the packet details.

           -w  <outfile> | -

               Write raw packet data to outfile or to the standard output if
               outfile is '-'. The -F and --compress options can be used to
               control the file format and compression method. If the latter
               is not given, then the extension may be used to deduce the
               desired compression algorithm, if supported, e.g. a gzip
               archive for '.gz'.

                   Note

                   -w provides raw packet data, not text. If you want text
                   output you need to redirect stdout (e.g. using '>'), don’t
                   use the -w option for this.

           -W  <file format option>

               Save extra information in the file if the format supports it.
               For example,

                   strato -F pcapng -W n

               will save host name resolution records along with captured
               packets.

               Future versions of strato may automatically change the capture
               format to pcapng as needed.

               The argument is a string that may contain the following
               letter:

               n write network address resolution information (pcapng only)

           -x
               Cause strato to print a hex and ASCII dump of the packet data
               after printing the summary and/or details, if either are also
               being displayed.

           --hexdump <hexoption>

               Cause strato to print a hex and ASCII dump of the packet data
               with the ability to select which data sources to dump, how to
               format or exclude the ASCII dump text, and whether to print
               the frame timestamp as preamble.

               This option (and -x) can occur multiple times on the command
               line, and the hex dump will only be printed once. In the case
               of conflicting options, the last options given will be used.
               The possible <hexoption> values are:

               all
                   Enable hexdump, generate hexdump blocks for all data
                   sources associated with each frame. Used to negate earlier
                   use of --hexdump frames. The -x option displays all data
                   sources by default.

               frames
                   Enable hexdump, generate hexdump blocks only for the frame
                   data. Use this option to exclude from hexdump output any
                   hexdump blocks for secondary data sources such as
                   'Bitstring tvb', 'Reassembled TCP', 'De-chunked entity
                   body', etc.

               ascii
                   Enable hexdump, with undelimited ASCII dump text. Used to
                   negate earlier use of --hexdump delimit or --hexdump
                   noascii. The -x option displays undelimited ASCII dump
                   text by default.

               delimit
                   Enable hexdump with the ASCII dump text delimited with '|'
                   characters. This is useful to unambiguously determine the
                   last of the hex byte text and start of the ASCII dump
                   text.

               noascii
                   Enable hexdump without printing any ASCII dump text.

               time
                   Enable hexdump and print each frame timestamp as preamble.
                   The -t option can be used to change the timestamp format.

               notime
                   Enable hexdump without print each frame timestamp as
                   preamble.

               help
                   Display --hexdump specific help then exit.

               The use of --hexdump <hexoption> is particularly useful to
               generate output that can be used to create a pcap or pcapng
               file from a capture file type such as Microsoft NetMon 2.x
               which strato and Wireshark can read but can not directly do a
               "Save as" nor export packets from.

               Examples:

               Generate hexdump output, with only the frame data source, with
               delimited ASCII dump text, and with each frame hex block
               preceded by a human readable timestamp in the local time zone
               that is directly usable by the text2pcap utility:

                   strato ... --hexdump frames --hexdump delimit --hexdump time -t ad \
                       | text2pcap -t 'ISO' - MYNEWPCAPNG

               Generate hexdump output, with only the frame data source, with
               the default ASCII dump text with no delimiter, and with each
               frame hex block preceded by a human readable timestamp in UTC
               that is directly usable by the text2pcap utility with the -a
               option:

                   strato ... --hexdump frames --hexdump time -t ud \
                       | text2pcap -a -t 'ISO' - MYNEWPCAPNG

               Generate hexdump output, with only the frame data source, with
               no ASCII dump text, and with each frame hex block preceded by
               an epoch timestamp that is directly usable by the text2pcap
               utility:

                   strato ... --hexdump frames --hexdump noascii --hexdump time -t e \
                       | text2pcap -t %s.%f - MYNEWPCAPNG

           -X <eXtension options>

               Specify an option to be passed to a strato module. The
               eXtension option is in the form extension_key:value, where
               extension_key can be:

               lua_script:lua_script_filename tells strato to load the given
               script in addition to the default Lua scripts.

               lua_scriptnum:argument tells strato to pass the given argument
               to the lua script identified by 'num', which is the number
               indexed order of the 'lua_script' command. For example, if
               only one script was loaded with '-X lua_script:my.lua', then
               '-X lua_script1:foo' will pass the string 'foo' to the
               'my.lua' script. If two scripts were loaded, such as '-X
               lua_script:my.lua' and '-X lua_script:other.lua' in that
               order, then a '-X lua_script2:bar' would pass the string 'bar'
               to the second lua script, namely 'other.lua'.

               read_format:file_format tells strato to use the given file
               format to read in the file (the file given in the -r command
               option). Providing no file_format argument, or an invalid one,
               will produce a list of available file formats to use. For
               example,

                   strato -r rtcp_broken.pcapng -X read_format:"MIME Files Format" -V

               will display the internal file structure  and allow access to
               the file-pcapng fields.

           -Y|--display-filter  <displaY filter>

               Cause the specified filter (which uses the syntax of
               read/display filters, rather than that of capture filters) to
               be applied before printing a decoded form of packets or
               writing packets to a file. Packets matching the filter are
               printed or written to file; packets that the matching packets
               depend upon (e.g., fragments), are not printed but are written
               to file; packets not matching the filter nor depended upon are
               discarded rather than being printed or written.

               Use this instead of -R for filtering using single-pass
               analysis. If doing two-pass analysis (see -2) then only
               packets matching the read filter (if there is one) will be
               checked against this filter.

           -M  <auto session reset>

               Automatically reset internal session when reached to specified
               number of packets. For example,

                   strato -M 100000

               will reset session every 100000 packets.

               This feature does not support -2 two-pass analysis

           -z  <statistics>

               Get strato to collect various types of statistics and display
               the result after finishing reading the capture file. Use the
               -q option if you’re reading a capture file and only want the
               statistics printed, not any per-packet information.

               Statistics are calculated independently of the normal
               per-packet output, unaffected by the main display filter.
               However, most have their own optional filter parameter, and
               only packets that match that filter (and any capture filter or
               read filter) will be used in the calculations.

               Note that the -z proto option is different - it doesn’t cause
               statistics to be gathered and printed when the capture is
               complete, it modifies the regular packet summary output to
               include the values of fields specified with the option.
               Therefore you must not use the -q option, as that option would
               suppress the printing of the regular packet summary output,
               and must also not use the -V option, as that would cause
               packet detail information rather than packet summary
               information to be printed.

               Some of the currently implemented statistics are:

           -z help
               Display all possible values for -z.

           -z container_io,tree[,filter]
               Calculate file I/O statistics for containers.

           -z expert[,error|,warn|,note|,chat|,comment][,filter]

               Collects information about all expert info, and will display
               them in order, grouped by severity.

               Example: -z expert,sip will show expert items of all severity
               for frames that match the sip protocol.

               This option can be used multiple times on the command line.

               Example: -z "expert,note,tcp" will only collect expert items
               for frames that include the tcp protocol, with a severity of
               note or higher.

           --capture-comment <comment>

               Add a capture comment to the output file, if supported by the
               output file format.

               This option may be specified multiple times. Note that
               Wireshark currently only displays the first comment of a
               capture file.

           --list-time-stamp-types
               List time stamp types supported for the interface. If no time
               stamp type can be set, no time stamp types are listed.

           --no-optimize
               Do not run the libpcap optimizer when generating code for a
               capture filter. This is useful if you suspect a bug in the
               optimizer.

           This option can occur multiple times. If used before the first
           occurrence of the -i option, capture filters are not optimized for
           all interfaces. If used after an -i option, the capture filter for
           the interface specified by the last -i option occurring before
           this option is not optimized.

           --time-stamp-type <type>
               Change the interface’s timestamp method.

           --update-interval  <interval>
               Set the length of time in milliseconds between new packet
               reports during a capture. Also sets the granularity of file
               duration conditions. The default value is 100ms.

           --color
               Enable coloring of packets according to standard Wireshark
               color filters. On Windows colors are limited to the standard
               console character attribute colors. Other platforms require a
               terminal that handles 24-bit "true color" terminal escape
               sequences. See https://wiki.wireshark.org/ColoringRules for
               more information on configuring color filters.

           --no-duplicate-keys
               If a key appears multiple times in an object, only write it a
               single time with as value a json array containing all the
               separate values. (Only works with -T json)

           --elastic-mapping-filter <protocol>,<protocol>,...

               When generating the ElasticSearch mapping file, only put the
               specified protocols in it, to avoid a huge mapping file that
               can choke some software (such as Kibana). The option takes a
               list of wanted protocol abbreviations, separated by comma.

               Example: ip,udp,dns puts only those three protocols in the
               mapping file.

           --export-objects <protocol>,<destdir>

               Export all objects within a protocol into directory destdir.
               The available values for protocol can be listed with
               --export-objects help.

               The objects are directly saved in the given directory.
               Filenames are dependent on the dissector, but typically it is
               named after the basename of a file. Duplicate files are not
               overwritten, instead an increasing number is appended before
               the file extension.

               This interface is subject to change, adding the possibility to
               filter on files.

           --print-timers
               Output JSON containing elapsed times for each pass strato does
               to process a capture file and the sum elapsed time for all
               passes. The per-pass output contains the total elapsed time
               and aggregate counters for per-packet operations (dissection
               and filtering).

           --compress <type>

               Compress the output file using the type compression format.
               --compress with no argument provides a list of the compression
               formats supported for writing. The type given takes precedence
               over the extension of outfile.

## [](#DISSECTION_OPTIONS)DISSECTION OPTIONS

           -d  <layer type>==<selector>,<decode-as protocol>

               Like Wireshark’s Decode As... feature, this lets you specify
               how a layer type should be dissected. If the layer type in
               question (for example, tcp.port or udp.port for a TCP or UDP
               port number) has the specified selector value, packets should
               be dissected as the specified protocol.

               Example 1. Decode As Port

                   -d tcp.port==8888,http will decode any traffic running
                   over TCP port 8888 as HTTP.

               Example 2. Decode As Port Range

                   -d tcp.port==8888-8890,http will decode any traffic
                   running over TCP ports 8888, 8889 or 8890 as HTTP.

               Example 3. Decode As Port Range via Length

                   -d tcp.port==8888:3,http will decode any traffic running
                   over the three TCP ports 8888, 8889 or 8890 as HTTP.

               Using an invalid selector or protocol will print out a list of
               valid selectors and protocol names, respectively.

               Example 4. Decode As List of Selectors

                   -d . is a quick way to get a list of valid selectors.

               Example 5. Decode As List of Values for a Selector

                   -d ethertype==0x0800,. is a quick way to get a list of
                   protocols that can be selected with an ethertype.

           --disable-all-protocols
               Disable dissection of all protocols.

           --disable-protocol <proto_name>[,<proto_name>,...]
               Disable dissection of proto_name. Use a proto_name of ALL to
               override your chosen profile’s default enabled protocol list
               and temporarily disable all protocols.

           --disable-heuristic <short_name>
               Disable dissection of heuristic protocol.

           --enable-protocol <proto_name>[,<proto_name>,...]

               Enable dissection of proto_name. Use a proto_name of ALL to
               override your chosen profile’s default disabled protocol list
               and temporarily enable all protocols which are enabled by
               default.

               If a protocol is implicated in both --disable-protocol and
               --enable-protocol, the protocol is enabled. This allows you to
               temporarily disable all protocols but a list of exceptions.
               Example: --disable-protocol ALL --enable-protocol eth,ip

           --enable-heuristic <short_name>
               Enable dissection of heuristic protocol.

           -K  <keytab>

               Load kerberos crypto keys from the specified keytab file. This
               option can be used multiple times to load keys from several
               files.

               Example: -K krb5.keytab

           -n
               Disable network object name resolution (such as hostname, TCP
               and UDP port names); the -N option might override this one.

           -N  <name resolving flags>

               Turn on name resolving only for particular types of addresses
               and port numbers, with name resolving for other types of
               addresses and port numbers turned off. This option (along with
               -n) can be specified multiple times; the last value given
               overrides earlier ones. This option and -n override the
               options from the preferences, including preferences set via
               the -o option. If both -N and -n options are not present, the
               values from the preferences are used, which default to -N dmN.

               The argument is a string that may contain the letters:

               d to enable resolution from captured DNS packets

               g to enable IP address geolocation information lookup from
               configured MaxMind databases

               m to enable MAC address resolution

               n to enable network address resolution

               N to enable using external resolvers (e.g., DNS) for network
               address resolution; no effect without n also enabled.

               s to enable address resolution using SNI information found in
               captured handshake packets

               t to enable transport-layer port number resolution

               v to enable VLAN IDs to names resolution

                   Caution

                   In tshark single-pass mode, external resolution and
                   geolocation lookup is performed synchronously. For live
                   captures, which are always in single-pass mode, this makes
                   it more difficult for dissection to keep up with a busy
                   network, possibly leading to dropped packets.

           --only-protocols <protocols>
               Only enable dissection of these protocols, comma separated.
               Disable everything else.

           -t  (a|ad|adoy|d|dd|e|r|rc|u|ud|udoy)[.[N]]|.[N]

               Set the format of the packet timestamp displayed in the
               default time column. The format can be one of:

               a absolute: The absolute time, as local time in your time
               zone, is the actual time the packet was captured, with no date
               displayed

               ad absolute with date: The absolute date, displayed as
               YYYY-MM-DD, and time, as local time in your time zone, is the
               actual time and date the packet was captured

               adoy absolute with date using day of year: The absolute date,
               displayed as YYYY/DOY, and time, as local time in your time
               zone, is the actual time and date the packet was captured

               d delta: The delta time is the time since the previous packet
               was captured

               dd delta_displayed: The delta_displayed time is the time since
               the previous displayed packet was captured

               e epoch: The time in seconds since epoch (Jan 1, 1970
               00:00:00)

               r relative: The relative time is the time elapsed between the
               first packet and the current packet

               rc relative to capture start: The relative to capture start
               time is the time elapsed between the start of the capturing
               and the current packet

               u UTC: The absolute time, as UTC with a "Z" suffix, is the
               actual time the packet was captured, with no date displayed

               ud UTC with date: The absolute date, displayed as YYYY-MM-DD,
               and time, as UTC with a "Z" suffix, is the actual time and
               date the packet was captured

               udoy UTC with date using day of year: The absolute date,
               displayed as YYYY/DOY, and time, as UTC with a "Z" suffix, is
               the actual time and date the packet was captured

               .[N] Set the precision: N is the number of decimals (0 through
               9). If using "." without N, automatically determine precision
               from trace.

               The default format is relative with precision based on capture
               format.

           -u <s|hms>

               Specifies how packet timestamp formats in -t which are
               relative times (i.e. relative, delta, and delta_displayed) are
               displayed. Valid choices are:

               s for seconds

               hms for hours, minutes, and seconds

               The default format is seconds.

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

## [](#FILES)FILES

           These files contain various Wireshark configuration settings.

           Preferences

               The preferences files contain global (system-wide) and
               personal preference settings. If the system-wide preference
               file exists, it is read first, overriding the default
               settings. If the personal preferences file exists, it is read
               next, overriding any previous values. Note: If the command
               line flag -o is used (possibly more than once), it will in
               turn override values from the preferences files.

               The preferences settings are in the form prefname:value, one
               per line, where prefname is the name of the preference and
               value is the value to which it should be set; white space is
               allowed between : and value. A preference setting can be
               continued on subsequent lines by indenting the continuation
               lines with white space. A # character starts a comment that
               runs to the end of the line:

                   # Vertical scrollbars should be on right side?
                   # TRUE or FALSE (case-insensitive).
                   gui.scrollbar_on_right: TRUE

               The global preferences file is looked for in the wireshark
               directory under the share subdirectory of the main
               installation directory. On macOS, this would typically be
               /Application/Wireshark.app/Contents/Resources/share; on other
               UNIX-compatible systems, such as Linux, \*BSD, Solaris, and
               AIX, this would typically be /usr/share/wireshark/preferences
               for system-installed packages and
               /usr/local/share/wireshark/preferences for locally-installed
               packages; on Windows, this would typically be C:\Program
               Files\Wireshark\preferences.

               On UNIX-compatible systems, the personal preferences file is
               looked for in $XDG_CONFIG_HOME/wireshark/preferences, (or, if
               $XDG_CONFIG_HOME/wireshark does not exist while
               $HOME/.wireshark does exist, $HOME/.wireshark/preferences);
               this is typically $HOME/.config/wireshark/preferences. On
               Windows, the personal preferences file is looked for in
               %APPDATA%\Wireshark\preferences (or, if %APPDATA% isn’t
               defined, %USERPROFILE%\Application
               Data\Wireshark\preferences).

           Disabled (Enabled) Protocols

               The disabled_protos files contain system-wide and personal
               lists of protocols that have been disabled, so that their
               dissectors are never called. The files contain protocol names,
               one per line, where the protocol name is the same name that
               would be used in a display filter for the protocol:

                   http
                   tcp     # a comment

               If a protocol is listed in the global disabled_protos file it
               cannot be enabled by the user.

               The global disabled_protos file uses the same directory as the
               global preferences file.

               The personal disabled_protos file uses the same directory as
               the personal preferences file.

               The disabled_protos files list only protocols that are enabled
               by default but have been disabled; protocols that are disabled
               by default (such as some postdissectors) are not listed. There
               are analogous enabled_protos files for protocols that are
               disabled by default but have been enabled.

           Heuristic Dissectors

               The heuristic_protos files contain system-wide and personal
               lists of heuristic dissectors and indicate whether they are
               enabled or disabled. The files contain heuristic dissector
               unique short names, one per line, followed by a comma and 0
               for disabled and 1 for enabled:

                   quic,1
                   rtcp_stun,1
                   rtcp_udp,1
                   rtp_stun,0
                   rtp_udp,0
                   tls_tcp,1

               The global heuristic_protos file uses the same directory as
               the global preferences file.

               The personal heuristic_protos file uses the same directory as
               the personal preferences file.

           Name Resolution (hosts)

               Entries in hosts files in the global and personal preferences
               directory are used to resolve IPv4 and IPv6 addresses before
               any other attempts are made to resolve them. The file has the
               standard hosts file syntax; each line contains one IP address
               and name, separated by whitespace. The personal hosts file, if
               present, overrides the one in the global directory.

               Capture filter name resolution is handled by libpcap on
               UNIX-compatible systems, such as Linux, macOS, \*BSD, Solaris,
               and AIX, and Npcap on Windows. As such the Wireshark personal
               hosts file will not be consulted for capture filter name
               resolution.

           Name Resolution (subnets)

               If an IPv4 address cannot be translated via name resolution
               (no exact match is found) then a partial match is attempted
               via the subnets file. Both the global subnets file and
               personal subnets files are used if they exist.

               Each line of this file consists of an IPv4 address, a subnet
               mask length separated only by a / and a name separated by
               whitespace. While the address must be a full IPv4 address, any
               values beyond the mask length are subsequently ignored.

               An example is:

               # Comments must be prepended by the # sign! 192.168.0.0/24
               ws_test_network

               A partially matched name will be printed as
               "subnet-name.remaining-address". For example, "192.168.0.1"
               under the subnet above would be printed as
               "ws_test_network.1"; if the mask length above had been 16
               rather than 24, the printed address would be
               "ws_test_network.0.1".

           Name Resolution (ethers)

               The ethers files are consulted to correlate 6-byte EUI-48 and
               8-byte EUI-64 hardware addresses to names. First the personal
               ethers file is tried and if an address is not found there the
               global ethers file is tried next.

               The file has a similar format to that defined by ethers(5) on
               some UNIX-like systems. Each line contains one hardware
               address and name, separated by whitespace (tabs or spaces).
               The hexadecimal digits of the hardware address are separated
               by colons (:), dashes (-) or periods (.). The same separator
               character must be used consistently in an address. A #
               indicates a comment that extends to the rest of the line. Both
               6-byte MAC and 8-byte EUI-64 addresses are supported. The
               following four lines are valid lines of an ethers file:

                   ff:ff:ff:ff:ff:ff          Broadcast
                   c0-00-ff-ff-ff-ff          TR_broadcast
                   00.00.00.00.00.00          Zero_broadcast
                   00:00:00:00:00:00:00:00    EUI64_zero_broadcast

               Note that this accepts a greater variety of formats than the
               file defined by ethers(5) on most UN*X systems.

               The global ethers file is looked for in the /etc directory on
               UNIX-compatible systems, such as Linux, macOS, \*BSD, Solaris,
               and AIX, and in the main installation directory (for example,
               C:\Program Files\Wireshark) on Windows systems.

               The personal ethers file is looked for in the same directory
               as the personal preferences file.

               Capture filter name resolution is handled by libpcap on
               UNIX-compatible systems and Npcap on Windows. As such the
               Wireshark personal ethers file will not be consulted for
               capture filter name resolution.

           Name Resolution (manuf)

               The manuf file is used to match the 3-byte vendor portion of a
               6-byte hardware address with the manufacturer’s name; it can
               also contain well-known MAC addresses and address ranges
               specified with a netmask. The format of the file is similar
               the ethers files, except that entries such as:

                   00:00:0C      Cisco     Cisco Systems, Inc

               can be provided, with the 3-byte OUI and both an abbreviated
               and long name for a vendor, and entries such as:

                   00-00-0C-07-AC/40     All-HSRP-routers

               can be specified, with a MAC address and a mask indicating how
               many bits of the address must match. The above entry, for
               example, has 40 significant bits, or 5 bytes, and would match
               addresses from 00-00-0C-07-AC-00 through 00-00-0C-07-AC-FF.
               The mask need not be a multiple of 8.

               A global manuf file is looked for in the same directory as the
               global preferences file, and a personal manuf file is looked
               for in the same directory as the personal preferences file.

               In earlier versions of Wireshark, official information from
               the IEEE Registration Authority was distributed in this format
               as the global manuf file. This information is now compiled in
               to speed program startup, but the internal information can be
               written out in this format with tshark -G manuf.

               In addition to the manuf file, another file with the same
               format, wka, is looked for in the global directory. This file
               is distributed with Wireshark, and contains data about
               well-known MAC addresses and address ranges assembled from
               various non IEEE but respected sources.

           Name Resolution (services)

               The services file is used to translate port numbers into
               names. Both the global services file and personal services
               files are used if they exist.

               The file has the standard services file syntax; each line
               contains one (service) name and one transport identifier
               separated by white space. The transport identifier includes
               one port number and one transport protocol name (typically
               tcp, udp, or sctp) separated by a /.

               An example is:

               mydns       5045/udp     # My own Domain Name Server mydns
               5045/tcp     # My own Domain Name Server

               In earlier versions of Wireshark, official information from
               the IANA Registry was distributed in this format as the global
               services file. This information is now compiled in to speed
               program startup, but the internal information can be written
               out in this format with tshark -G services.

           Name Resolution (ipxnets)

               The ipxnets files are used to correlate 4-byte IPX network
               numbers to names. First the global ipxnets file is tried and
               if that address is not found there the personal one is tried
               next.

               The format is the same as the ethers file, except that each
               address is four bytes instead of six. Additionally, the
               address can be represented as a single hexadecimal number, as
               is more common in the IPX world, rather than four hex octets.
               For example, these four lines are valid lines of an ipxnets
               file:

                   C0.A8.2C.00              HR
                   c0-a8-1c-00              CEO
                   00:00:BE:EF              IT_Server1
                   110f                     FileServer3

               The global ipxnets file is looked for in the /etc directory on
               UNIX-compatible systems, such as Linux, macOS, \*BSD, Solaris,
               and AIX, and in the main installation directory (for example,
               C:\Program Files\Wireshark) on Windows systems.

               The personal ipxnets file is looked for in the same directory
               as the personal preferences file.

           Name Resolution (ss7pcs)

               The ss7pcs file is used to translate SS7 point codes to names.
               It is read from the personal configuration directory.

               Each line in this file consists of one network indicator
               followed by a dash followed by a point code in decimal and a
               node name separated by whitespace. An example is:

                   2-1234 MyPointCode1

           Name Resolution (vlans)

               The vlans file is used to translate VLAN tag IDs into names.
               It is read from the personal configuration directory.

               Each line in this file consists of one VLAN tag ID separated
               by whitespace from a name. An example is:

                   123    Server-Lan
                   2049   HR-Client-LAN

           Color Filters (Coloring Rules)

               The colorfilters files contain system-wide and personal color
               filters. Each line contains one filter, starting with the
               string displayed in the dialog box, followed by the
               corresponding display filter. Then the background and
               foreground colors are appended:

                   # a comment
                   @tcp@tcp@[59345,58980,65534][0,0,0]
                   @udp@udp@[28834,57427,65533][0,0,0]

               The global colorfilters file uses the same directory as the
               global preferences file.

               The personal colorfilters file uses the same directory as the
               personal preferences file. It is written through the
               View:Coloring Rules dialog.

               If the global colorfilters file exists, it is used only if the
               personal colorfilters file does not exist; global and personal
               color filters are not merged.

           Plugins

               Wireshark looks for plugins in both a personal plugin folder
               and a global plugin folder.

               On UNIX-compatible systems, such as Linux, macOS, \*BSD,
               Solaris, and AIX, the global plugin directory is
               lib/wireshark/plugins/ (on some systems substitute lib64 for
               lib) under the main installation directory (for example,
               /usr/local/lib/wireshark/plugins/). The personal plugin
               directory is $HOME/.local/lib/wireshark/plugins.

               On macOS, if Wireshark is installed as an application bundle,
               the global plugin folder is instead
               %APPDIR%/Contents/PlugIns/wireshark.

               On Windows, the global plugin folder is plugins/ under the
               main installation directory (for example, C:\Program
               Files\Wireshark\plugins\). The personal plugin folder is
               %APPDATA%\Wireshark\plugins (or, if %APPDATA% isn’t defined,
               %USERPROFILE%\Application Data\Wireshark\plugins).

               Lua plugins are stored in the plugin folders; compiled plugins
               are stored in subfolders of the plugin folders, with the
               subfolder name being the Wireshark minor version number (X.Y).
               There is another hierarchical level for each Wireshark plugin
               type (libwireshark, libwiretap and codecs). For example, the
               location for a libwireshark plugin foo.so (foo.dll on Windows)
               would be PLUGINDIR/X.Y/epan (libwireshark used to be called
               libepan; the other folder names are codecs and wiretap).

                   Note

                   On UNIX-compatible systems, Lua plugins (but not binary
                   plugins) may also be placed in
                   $XDG_CONFIG_HOME/wireshark/plugins, (or, if
                   $XDG_CONFIG_HOME/wireshark does not exist while
                   $HOME/.wireshark does exist, $HOME/.wireshark/plugins.)

               Note that a dissector plugin module may support more than one
               protocol; there is not necessarily a one-to-one correspondence
               between dissector plugin modules and protocols. Protocols
               supported by a dissector plugin module are enabled and
               disabled in the same way as protocols built into Wireshark.

## [](#OUTPUT)OUTPUT

           strato uses UTF-8 to represent strings internally. In some cases
           the output might not be valid. For example, a dissector might
           generate invalid UTF-8 character sequences. Programs reading
           strato output should expect UTF-8 and be prepared for invalid
           output.

           If strato detects that it is writing to a TTY on a UNIX-compatible
           system, such as Linux, macOS, \*BSD, Solaris, and AIX, and the
           locale does not support UTF-8, output will be re-encoded to match
           the current locale.

           If strato detects that it is writing to the console on Windows,
           dissection output will be encoded as UTF-16LE. Other output will
           be UTF-8. If extended characters don’t display properly in your
           terminal you might try setting your console code page to UTF-8
           (chcp 65001) and using a modern terminal application if possible.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           WIRESHARK_CONFIG_DIR
               This environment variable overrides the location of personal
               configuration files. On UNIX-compatible systems, such as
               Linux, macOS, \*BSD, Solaris, and AIX, it defaults to
               $XDG_CONFIG_HOME/wireshark (or, if that directory doesn’t
               exist but $HOME/.wireshark does exist, $HOME/.wireshark); this
               is typically $HOME/.config/wireshark. On Windows, it defaults
               to %APPDATA%\Wireshark (or, if %APPDATA% isn’t defined,
               %USERPROFILE%\Application Data\Wireshark). Available since
               Wireshark 3.0.

           WIRESHARK_DEBUG_WMEM_OVERRIDE
               Setting this environment variable forces the wmem framework to
               use the specified allocator backend for all allocations,
               regardless of which backend is normally specified by the code.
               This is mainly useful to developers when testing or debugging.
               See README.wmem in the source distribution for details.

           WIRESHARK_RUN_FROM_BUILD_DIRECTORY
               This environment variable causes the plugins and other data
               files to be loaded from the build directory (where the program
               was compiled) rather than from the standard locations. It has
               no effect when the program in question is running with root
               (or setuid) permissions on UNIX-compatible systems, such as
               Linux, macOS, \*BSD, Solaris, and AIX.

           WIRESHARK_DATA_DIR
               This environment variable causes the various data files to be
               loaded from a directory other than the standard locations. It
               has no effect when the program in question is running with
               root (or setuid) permissions on UNIX-compatible systems.

           WIRESHARK_EXTCAP_DIR
               This environment variable causes the various extcap programs
               and scripts to be run from a directory other than the standard
               locations. It has no effect when the program in question is
               running with root (or setuid) permissions on UNIX-compatible
               systems.

           WIRESHARK_PLUGIN_DIR
               This environment variable causes the various plugins to be
               loaded from a directory other than the standard locations. It
               has no effect when the program in question is running with
               root (or setuid) permissions on UNIX-compatible systems.

           ERF_RECORDS_TO_CHECK
               This environment variable controls the number of ERF records
               checked when deciding if a file really is in the ERF format.
               Setting this environment variable a number higher than the
               default (20) would make false positives less likely.

           IPFIX_RECORDS_TO_CHECK
               This environment variable controls the number of IPFIX records
               checked when deciding if a file really is in the IPFIX format.
               Setting this environment variable a number higher than the
               default (20) would make false positives less likely.

           WIRESHARK_ABORT_ON_DISSECTOR_BUG
               If this environment variable is set, strato will call abort(3)
               when a dissector bug is encountered. abort(3) will cause the
               program to exit abnormally; if you are running strato in a
               debugger, it should halt in the debugger and allow inspection
               of the process, and, if you are not running it in a debugger,
               it will, on some OSes, assuming your environment is configured
               correctly, generate a core dump file. This can be useful to
               developers attempting to troubleshoot a problem with a
               protocol dissector.

           WIRESHARK_ABORT_ON_TOO_MANY_ITEMS
               If this environment variable is set, strato will call abort(3)
               if a dissector tries to add too many items to a tree
               (generally this is an indication of the dissector not breaking
               out of a loop soon enough). abort(3) will cause the program to
               exit abnormally; if you are running strato in a debugger, it
               should halt in the debugger and allow inspection of the
               process, and, if you are not running it in a debugger, it
               will, on some OSes, assuming your environment is configured
               correctly, generate a core dump file. This can be useful to
               developers attempting to troubleshoot a problem with a
               protocol dissector.

           WIRESHARK_LOG_LEVEL
               This environment variable controls the verbosity of diagnostic
               messages to the console. From less verbose to most verbose
               levels can be critical, warning, message, info, debug or
               noisy. Levels above the current level are also active. Levels
               critical and error are always active.

           WIRESHARK_LOG_FATAL
               Sets the fatal log level. Fatal log levels cause the program
               to abort. This level can be set to Error, critical or warning.
               Error is always fatal and is the default.

           WIRESHARK_LOG_DOMAINS
               This environment variable selects which log domains are
               active. The filter is given as a case-insensitive comma
               separated list. If set only the included domains will be
               enabled. The default domain is always considered to be
               enabled. Domain filter lists can be preceded by '!' to invert
               the sense of the match.

           WIRESHARK_LOG_DEBUG
               List of domains with debug log level. This sets the level of
               the provided log domains and takes precedence over the active
               domains filter. If preceded by '!' this disables the debug
               level instead.

           WIRESHARK_LOG_NOISY
               Same as above but for noisy log level instead.

## [](#SEE_ALSO)SEE ALSO

           wireshark-filter(4), stratoshark(1), editcap(1), dumpcap(1)

## [](#NOTES)NOTES

           This is the manual page for strato 0.10.3. strato is part of the
           Stratoshark distribution. The latest version of Stratoshark can be
           found at https://stratoshark.org/.

           HTML versions of the Wireshark project man pages are available at
           https://www.wireshark.org/docs/man-pages.

## [](#AUTHORS)AUTHORS

           strato uses the same dissection code as Stratoshark and Wireshark,
           as well as using many other modules from Stratoshark and
           Wireshark; see the list of authors in the Wireshark man page for a
           list of authors of that code..SH COLOPHON This page is part of the
           wireshark (Interactively dump and analyze network traffic)
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

                                    2026-05-24                      STRATO(1)

------------------------------------------------------------------------

Pages that refer to this page: [dumpcalls(1)](../man1/dumpcalls.1.html),  [falcodump(1)](../man1/falcodump.1.html),  [sshdig(1)](../man1/sshdig.1.html),  [stratoshark(1)](../man1/stratoshark.1.html)

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
