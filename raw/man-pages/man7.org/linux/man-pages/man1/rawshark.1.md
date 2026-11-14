---
{"title": "rawshark(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/rawshark.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rawshark(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INPUT](#INPUT) \| [OUTPUT](#OUTPUT) \| [OPTIONS](#OPTIONS) \| [DISSECTION OPTIONS](#DISSECTION_OPTIONS) \| [DIAGNOSTIC OPTIONS](#DIAGNOSTIC_OPTIONS) \| [READ FILTER SYNTAX](#READ_FILTER_SYNTAX) \| [FILES](#FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                      |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RAWSHARK(1)                                                   RAWSHARK(1)

## [](#NAME)NAME

           rawshark - Dump and analyze raw pcap data

## [](#SYNOPSIS)SYNOPSIS

           rawshark [ -d <encap:linktype>|<proto:protoname> ] [ -F <field to
           display> ] [ -l ] [ -m <bytes> ] [ -o <preference setting> ] ... [
           -p ] [ -r <pipe>|- ] [ -R <read (display) filter> ] [ -s ] [ -S
           <field format> ] [ options ]

           rawshark -h|--help

           rawshark -v|--version

## [](#DESCRIPTION)DESCRIPTION

           Rawshark reads a stream of packets from a file or pipe, and prints
           a line describing its output, followed by a set of matching fields
           for each packet on stdout.

## [](#INPUT)INPUT

           Unlike TShark, Rawshark makes no assumptions about encapsulation
           or input. The -d and -r flags must be specified in order for it to
           run. One or more -F flags should be specified in order for the
           output to be useful. The other flags listed above follow the same
           conventions as Wireshark and TShark.

           Rawshark expects input records with the following format by
           default. This matches the format of the packet header and packet
           data in a pcap-formatted file on disk.

               struct rawshark_rec_s {
                   uint32_t ts_sec;      /* Time stamp (seconds) */
                   uint32_t ts_usec;     /* Time stamp (microseconds) */
                   uint32_t caplen;      /* Length of the packet buffer */
                   uint32_t len;         /* "On the wire" length of the packet */
                   uint8_t data[caplen]; /* Packet data */
               };

           If -p is supplied rawshark expects the following format. This
           matches the struct pcap_pkthdr structure and packet data used in
           libpcap or Npcap. This structure’s format is platform-dependent;
           the size of the tv_sec field in the struct timeval structure could
           be 32 bits or 64 bits. For rawshark to work, the layout of the
           structure in the input must match the layout of the structure in
           rawshark. Note that this format will probably be the same as the
           previous format if rawshark is a 32-bit program, but will not
           necessarily be the same if rawshark is a 64-bit program.

               struct rawshark_rec_s {
                   struct timeval ts;    /* Time stamp */
                   uint32_t caplen;      /* Length of the packet buffer */
                   uint32_t len;         /* "On the wire" length of the packet */
                   uint8_t data[caplen]; /* Packet data */
               };

           In either case, the endianness (byte ordering) of each integer
           must match the system on which rawshark is running.

## [](#OUTPUT)OUTPUT

           If one or more fields are specified via the -F flag, Rawshark
           prints the number, field type, and display format for each field
           on the first line as "packet number" 0. For each record, the
           packet number, matching fields, and a "1" or "0" are printed to
           indicate if the field matched any supplied display filter. A "-"
           is used to signal the end of a field description and at the end of
           each packet line. For example, the flags -F ip.src -F dns.qry.type
           might generate the following output:

               0 FT_IPv4 BASE_NONE - 1 FT_UINT16 BASE_HEX -
               1 1="1" 0="192.168.77.10" 1 -
               2 1="1" 0="192.168.77.250" 1 -
               3 0="192.168.77.10" 1 -
               4 0="74.125.19.104" 1 -

           Note that packets 1 and 2 are DNS queries, and 3 and 4 are not.
           Adding -R "not dns" still prints each line, but there’s an
           indication that packets 1 and 2 didn’t pass the filter:

               0 FT_IPv4 BASE_NONE - 1 FT_UINT16 BASE_HEX -
               1 1="1" 0="192.168.77.10" 0 -
               2 1="1" 0="192.168.77.250" 0 -
               3 0="192.168.77.10" 1 -
               4 0="74.125.19.104" 1 -

           Also note that the output may be in any order, and that multiple
           matching fields might be displayed.

## [](#OPTIONS)OPTIONS

           -d  <encapsulation>

               Specify how the packet data should be dissected. The
               encapsulation is of the form type:value, where type is one of:

               encap:name Packet data should be dissected using the
               libpcap/Npcap data link type (DLT) name, e.g. encap:EN10MB for
               Ethernet. Names are converted using
               pcap_datalink_name_to_val(). A complete list of DLTs can be
               found at https://www.tcpdump.org/linktypes.html.

               encap:number Packet data should be dissected using the
               libpcap/Npcap LINKTYPE_ number, e.g. encap:105 for raw IEEE
               802.11 or encap:101 for raw IP.

               proto:protocol Packet data should be passed to the specified
               Wireshark protocol dissector, e.g. proto:http for HTTP data.

           -F  <field to display>

               Add the matching field to the output. Fields are any valid
               display filter field. More than one -F flag may be specified,
               and each field can match multiple times in a given packet. A
               single field may be specified per -F flag. If you want to
               apply a display filter, use the -R flag.

           -h|--help
               Print the version number and options and exit.

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
               Visual C++ C library.)

               This may be useful when piping the output of TShark to another
               program, as it means that the program to which the output is
               piped will see the dissected data for a packet as soon as
               TShark sees the packet and generates that output, rather than
               seeing it only when the standard output buffer containing that
               data fills up.

           -m  <memory limit bytes>
               Limit rawshark’s memory usage to the specified number of
               bytes. POSIX (non-Windows) only.

           -o  <preference>:<value>

               Set a preference value, overriding the default value and any
               value read from a preference file. The argument to the option
               is a string of the form prefname:value, where prefname is the
               name of the preference (which is the same name that would
               appear in the preference file), and value is the value to
               which it should be set.

           -p

               Assume that packet data is preceded by a pcap_pkthdr struct as
               defined in pcap.h. On some systems the size of the timestamp
               data will be different from the data written to disk. On other
               systems they are identical and this flag has no effect.

           -r  <pipe>|-

               Read packet data from input source. It can be either the name
               of a FIFO (named pipe) or ``-'' to read data from the standard
               input, and must have the record format specified above.

               If you are sending data to rawshark from a parent process on
               Windows you should not close rawshark’s standard input handle
               prematurely, otherwise the C runtime might trigger an
               exception.

           -R|--read-filter <read (display) filter>

               Cause the specified filter (which uses the syntax of
               read/display filters, rather than that of capture filters) to
               be applied before printing the output. Read filters and
               display filters are synonymous in rawshark.

           -s
               Allows standard pcap files to be used as input, by skipping
               over the 24 byte pcap file header.

           -S

               Use the specified format string to print each field. The
               following formats are supported:

               %D Field name or description, e.g. "Type" for dns.qry.type

               %N Base 10 numeric value of the field.

               %S String value of the field.

               For something similar to Wireshark’s standard display ("Type:
               A (1)") you could use %D: %S (%N).

           -v|--version
               Print the full version information and exit.

           -Y|--display-filter <read (display) filter>

               Cause the specified filter (which uses the syntax of
               read/display filters, rather than that of capture filters) to
               be applied before printing the output. Read filters and
               display filters are synonymous in rawshark.

## [](#DISSECTION_OPTIONS)DISSECTION OPTIONS

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

## [](#READ_FILTER_SYNTAX)READ FILTER SYNTAX

           For a complete table of protocol and protocol fields that are
           filterable in Rawshark see the wireshark-filter(4) manual page.

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

               If this environment variable is set, Rawshark will call
               abort(3) when a dissector bug is encountered. abort(3) will
               cause the program to exit abnormally; if you are running
               Rawshark in a debugger, it should halt in the debugger and
               allow inspection of the process, and, if you are not running
               it in a debugger, it will, on some OSes, assuming your
               environment is configured correctly, generate a core dump
               file. This can be useful to developers attempting to
               troubleshoot a problem with a protocol dissector.

           WIRESHARK_ABORT_ON_TOO_MANY_ITEMS

               If this environment variable is set, Rawshark will call
               abort(3) if a dissector tries to add too many items to a tree
               (generally this is an indication of the dissector not breaking
               out of a loop soon enough). abort(3) will cause the program to
               exit abnormally; if you are running Rawshark in a debugger, it
               should halt in the debugger and allow inspection of the
               process, and, if you are not running it in a debugger, it
               will, on some OSes, assuming your environment is configured
               correctly, generate a core dump file. This can be useful to
               developers attempting to troubleshoot a problem with a
               protocol dissector.

## [](#SEE_ALSO)SEE ALSO

           wireshark-filter(4), wireshark(1), tshark(1), editcap(1), pcap(3),
           dumpcap(1), text2pcap(1), pcap-filter(7) or tcpdump(8)

## [](#NOTES)NOTES

           This is the manual page for Rawshark 4.7.3. Rawshark is part of
           the Wireshark distribution. The latest version of Wireshark can be
           found at https://www.wireshark.org.

           HTML versions of the Wireshark project man pages are available at
           https://www.wireshark.org/docs/man-pages.

## [](#AUTHORS)AUTHORS

           Rawshark uses the same packet dissection code that Wireshark does,
           as well as using many other modules from Wireshark; see the list
           of authors in the Wireshark man page for a list of authors of that
           code..SH COLOPHON This page is part of the wireshark
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

                                    2025-03-07                    RAWSHARK(1)

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
