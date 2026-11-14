---
{"title": "stratoshark(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stratoshark.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stratoshark(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DISSECTION OPTIONS](#DISSECTION_OPTIONS) \| [DIAGNOSTIC OPTIONS](#DIAGNOSTIC_OPTIONS) \| [FILES](#FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STRATOSHARK(1)                                             STRATOSHARK(1)

## [](#NAME)NAME

           stratoshark - System call and event log analyzer

## [](#SYNOPSIS)SYNOPSIS

           stratoshark [ -i <capture source>|- ] [ -f <capture filter> ] [ -Y
           <display filter> ] [ -w <outfile> ] [ options ] [ <infile> ]

           stratoshark -h|--help

           stratoshark -v|--version

## [](#DESCRIPTION)DESCRIPTION

           Stratoshark is a GUI system call and log analyzer. It lets you
           interactively browse system calls and log messages from a live
           system or from a previously saved capture file. Stratoshark's
           native capture file format is scap, which is used by the sysdig
           CLI tool and by Falco.

           Stratoshark's main window shows 3 views of each event. It shows a
           summary line, briefly describing what the event is. An event
           details display is shown, allowing you to drill down to exact
           field that you interested in. Finally, a hex dump shows you
           exactly what the event data looks like on disk or over the wire.

           In addition, Stratoshark has some features that make it unique. It
           can assemble all the syscalls in a file descriptor stream and show
           you the ASCII (or EBCDIC, or hex) data in that conversation.
           Display filters in Stratoshark are very powerful; more fields are
           filterable in Stratoshark than in other tools, and the syntax you
           can use to create your filters is richer. As Stratoshark
           progresses, expect more and more fields to be supported.

           Event capturing is performed by the libscap and libsinsp
           libraries. The capture filter syntax follows the rules of the
           libscap. This syntax is different from the display filter syntax.

           Compressed file support uses (and therefore requires) the zlib
           library. If the zlib library is not present, Stratoshark will
           compile, but will be unable to read compressed files.

           The pathname of a capture file to be read can be specified with
           the -r option or can be specified as a command-line argument.

## [](#OPTIONS)OPTIONS

           Stratoshark supports a wide variety of command line options. Most
           users will want to start it without any options and configure it
           from the application menus instead. Those users may wish to skip
           this section.

           -a|--autostop  <capture autostop condition>

               Specify a criterion that specifies when Stratoshark should
               stop writing to a capture file. The criterion is of the form
               test:value, where test is one of:

               duration:value Stop writing to a capture file after value
               seconds have elapsed. Floating point values (e.g. 0.5) are
               allowed.

               files:value Stop writing to capture files after value number
               of files were written.

               filesize:value Stop writing to a capture file after it reaches
               a size of value kB. If this option is used together with the
               -b option, Stratoshark will stop writing to the current
               capture file and switch to the next one if filesize is
               reached. Note that the filesize is limited to a maximum value
               of 2 TB, although you might have problems viewing the file in
               the GUI before then if the number of events exceeds 231
               (2147483648).

               events:value Stop writing to a capture file after it contains
               value events. Acts the same as -c<capture event count>.

           -b|--ring-buffer  <capture ring buffer option>

               Cause Stratoshark to run in "multiple files" mode. In
               "multiple files" mode, Stratoshark will write to several
               capture files. When the first capture file fills up,
               Stratoshark will switch writing to the next file and so on.

               The created filenames are based on the filename given with the
               -w flag, the number of the file and on the creation date and
               time, e.g. outfile_00001_20260714120117.pcap,
               outfile_00002_20260714120523.pcap, ...

               With the files option it’s also possible to form a "ring
               buffer". This will fill up new files until the number of files
               specified, at which point Stratoshark will discard the data in
               the first file and start writing to that file and so on. If
               the files option is not set, new files filled up until one of
               the capture stop conditions match (or until the disk is full).

               The criterion is of the form key:value, where key is one of:

               duration:value switch to the next file after value seconds
               have elapsed, even if the current file is not completely
               filled up. Floating point values (e.g. 0.5) are allowed.

               files:value begin again with the first file after value number
               of files were written (form a ring buffer). This value must be
               less than 100000. Caution should be used when using large
               numbers of files: some filesystems do not handle many files in
               a single directory well. The files criterion requires one of
               the other criteria to be specified to control when to go to
               the next file. It should be noted that each -b parameter takes
               exactly one criterion; to specify two criteria, each must be
               preceded by the -b option.

               filesize:value switch to the next file after it reaches a size
               of value kB. Note that the filesize is limited to a maximum
               value of 2 TB, although you might have problems viewing the
               file in the GUI before then if the number of events exceeds
               231 (2147483648).

               interval:value switch to the next file when the time is an
               exact multiple of value seconds.

               events:value switch to the next file after it contains value
               events.

               Example: -b filesize:1000 -b files:5 results in a ring buffer
               of five files of size one megabyte each.

           -c  <capture event count>
               Set the maximum number of events to read when capturing live
               data. Acts the same as -a events:<capture event count>.

           -C  <configuration profile>
               Start with the given configuration profile.

           --capture-comment <comment>

               When performing a capture file from the command line, with the
               -k flag, add a capture comment to the output file, if
               supported by the capture format.

               This option may be specified multiple times. Note that
               Stratoshark currently only displays the first comment of a
               capture file.

           -D|--list-sources
               Print a list of the sources from which Stratoshark can
               capture, and exit. For each source, a number and a source
               name, possibly followed by a text description of the source,
               is printed. The source name or the number can be supplied to
               the -i flag to specify a source from which to capture.

           --display <X display to use>
               Specifies the X display to use. A hostname and screen
               (otherhost:0.0) or just a screen (:0.0) can be specified. This
               option is not available under macOS or Windows.

           -f  <capture filter>

               Set the capture filter expression.

               This option can occur multiple times. If used before the first
               occurrence of the -i option, it sets the default capture
               filter expression. If used after an -i option, it sets the
               capture filter expression for the source specified by the last
               -i option occurring before this option. If the capture filter
               expression is not set specifically, the default capture filter
               expression is used if provided.

               Pre-defined capture filter names, as shown in the GUI menu
               item Capture→Capture Filters, can be used by prefixing the
               argument with "predef:". Example: -f
               "predef:MyPredefinedHostOnlyFilter"

           --fullscreen

               Start Stratoshark in full screen mode (kiosk mode). To exit
               from fullscreen mode, open the View menu and select the Full
               Screen option. Alternatively, press the F11 key (or Ctrl + Cmd
               + F for macOS).

           -g  <event number>
               After reading in a capture file using the -r flag, go to the
               given event number.

           -h|--help
               Print the version number and options and exit.

           -H
               Hide the capture info dialog during live capture.

           -i|--source  <capture source>|-

               Set the name of the capture source or pipe to use for live
               capture.

               Capture source names should match one of the names or numbers
               listed in "stratoshark -D" (described above).

               If no source is specified, Stratoshark searches the list of
               sources, choosing the first source. If there are no sources at
               all, Stratoshark reports an error and doesn’t start the
               capture.

               Pipe names should be either the name of a FIFO (named pipe) or
               "-" to read data from the standard input. On Windows systems,
               pipe names must be of the form "\\.\pipe\pipename". Data read
               from pipes must be in standard scap format. Scap data must
               have the same endianness as the capturing host.

               This option can occur multiple times.

           -j
               Use after -J to change the behavior when no exact match is
               found for the filter. With this option select the first event
               before.

           -J  <jump filter>

               After reading in a capture file using the -r flag, jump to the
               event matching the filter (display filter syntax). If no exact
               match is found the first event after that is selected.

           -k

               Start the capture session immediately. If the -i flag was
               specified, the capture uses the specified source. Otherwise,
               Stratoshark searches the list of sources and uses the first
               source. If there are no sources, Stratoshark reports an error
               and doesn’t start the capture.

           -l
               Turn on automatic scrolling if the event display is being
               updated automatically as events arrive during a capture (as
               specified by the -S flag).

           -L|--list-data-link-types
               List the data link types supported by the interface and exit.

           --list-time-stamp-types
               List time stamp types supported for the interface. If no time
               stamp type can be set, no time stamp types are listed.

           -o  <preference/recent setting>

               Set a preference or recent value, overriding the default value
               and any value read from a preference/recent file. The argument
               to the flag is a string of the form prefname:value, where
               prefname is the name of the preference/recent value (which is
               the same name that would appear in the preference/recent
               file), and value is the value to which it should be set.

               If prefname is "uat", you can override settings in various
               user access tables using the form "uat:uat filename:uat
               record". uat filename must be the name of a UAT file, e.g.
               user_dlts. uat_record must be in the form of a valid record
               for that file, including quotes. For instance, to specify a
               user DLT from the command line, you would use

                   -o "uat:user_dlts:\"User 0 (DLT=147)\",\"cops\",\"0\",\"\",\"0\",\"\""

           -P <path setting>

               Special path settings usually detected automatically. This is
               used for special cases, e.g. starting Stratoshark from a known
               location on an USB stick.

               The criterion is of the form key:path, where key is one of:

               persconf:path path of personal configuration files, like the
               preferences files.

               persdata:path path of personal data files, it’s the folder
               initially opened. After the very first initialization, the
               recent file will keep the folder last used.

           -r|--read-file  <infile>
               Read event data from infile, can be any supported capture file
               format (including compressed files). It’s not possible to use
               named pipes or stdin here, unlike TShark! To capture from a
               pipe or from stdin use -i -.

           -R|--read-filter  <read (display) filter>
               When reading a capture file specified with the -r flag, causes
               the specified filter (which uses the syntax of display
               filters, rather than that of capture filters) to be applied to
               all events read from the capture file; events not matching the
               filter are discarded.

           -S
               Automatically update the event display as events are coming
               in.

           --temp-dir <directory>

               Specifies the directory into which temporary files (including
               capture files) are to be written. The default behavior on
               UNIX-compatible systems, such as Linux, macOS, \*BSD, Solaris,
               and AIX, is to use the environment variable $TMPDIR if set,
               and the system default, typically /tmp, if it is not. On
               Windows, the %TEMP% environment variable is used, which
               typically defaults to %USERPROFILE%\AppData\Local\Temp.

           --time-stamp-type <type>
               Change the sources’s timestamp method. See
               --list-time-stamp-types.

           --update-interval  <interval>
               Set the length of time in milliseconds between new event
               reports during a capture. Also sets the granularity of file
               duration conditions. The default value is 100ms.

           -v|--version
               Print the full version information and exit.

           -w  <outfile>
               Set the default capture file name, or '-' for standard output.

           -X <eXtension options>

               Specify an option to be passed to an Stratoshark module. The
               eXtension option is in the form extension_key:value, where
               extension_key can be:

               lua_script:lua_script_filename tells Stratoshark to load the
               given script in addition to the default Lua scripts.

               lua_scriptnum:argument tells Stratoshark to pass the given
               argument to the lua script identified by 'num', which is the
               number indexed order of the 'lua_script' command. For example,
               if only one script was loaded with '-X lua_script:my.lua',
               then '-X lua_script1:foo' will pass the string 'foo' to the
               'my.lua' script. If two scripts were loaded, such as '-X
               lua_script:my.lua' and '-X lua_script:other.lua' in that
               order, then a '-X lua_script2:bar' would pass the string 'bar'
               to the second lua script, namely 'other.lua'.

               stdin_descr:description tells Stratoshark to use the given
               description when capturing from standard input (-i -).

           -Y|--display-filter  <displaY filter>
               Start with the given display filter.

           -z  <statistics>

               Get Stratoshark to collect various types of statistics and
               display the result in a window that updates in semi-real time.

               Some of the currently implemented statistics are:

           -z help
               Display all possible values for -z.

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

               See the tshark(1) manual page for more examples.

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

               Note: Whenever the preferences are saved by using the Save
               button in the Edit:Preferences dialog box, your personal
               preferences file will be overwritten with the new settings,
               destroying any comments and unknown/obsolete settings that
               were in the file.

           Recent

               The recent file contains personal settings (mostly GUI
               related) such as the current Wireshark window size. The file
               is saved at program exit and read in at program start
               automatically. Note: The command line flag -o may be used to
               override settings from this file.

               The settings in this file have the same format as in the
               preferences files, and the same directory as for the personal
               preferences file is used.

               Note: Whenever Wireshark is closed, your recent file will be
               overwritten with the new settings, destroying any comments and
               unknown/obsolete settings that were in the file.

           Disabled (Enabled) Protocols

               The disabled_protos files contain system-wide and personal
               lists of protocols that have been disabled, so that their
               dissectors are never called. The files contain protocol names,
               one per line, where the protocol name is the same name that
               would be used in a display filter for the protocol:

                   http
                   tcp     # a comment

               If a protocol is listed in the global disabled_protos file it
               cannot be enabled by the user. Thus it is not displayed in the
               Analyze::Enabled Protocols dialog box.

               The global disabled_protos file uses the same directory as the
               global preferences file.

               The personal disabled_protos file uses the same directory as
               the personal preferences file.

               The disabled_protos files list only protocols that are enabled
               by default but have been disabled; protocols that are disabled
               by default (such as some postdissectors) are not listed. There
               are analogous enabled_protos files for protocols that are
               disabled by default but have been enabled.

               Note: Whenever the disabled protocols list is saved by using
               the Save button in the Analyze:Enabled Protocols dialog box,
               your personal disabled protocols file will be overwritten with
               the new settings, destroying any comments that were in the
               file.

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

           Capture Filters

               The cfilters files contain system-wide and personal capture
               filters. Each line contains one filter, starting with the
               string displayed in the dialog box in quotation marks,
               followed by the filter string itself:

                   "HTTP" port 80
                   "DCERPC" port 135

               The global cfilters file uses the same directory as the global
               preferences file.

               The personal cfilters file uses the same directory as the
               personal preferences file. It is written through the
               Capture:Capture Filters dialog.

               If the global cfilters file exists, it is used only if the
               personal cfilters file does not exist; global and personal
               capture filters are not merged.

           Display Filters

               The dfilters files contain system-wide and personal display
               filters. Each line contains one filter, starting with the
               string displayed in the dialog box in quotation marks,
               followed by the filter string itself:

                   "HTTP" http
                   "DCERPC" dcerpc

               The global dfilters file uses the same directory as the global
               preferences file.

               The personal dfilters file uses the same directory as the
               personal preferences file. It is written through the
               Analyze:Display Filters dialog.

               If the global dfilters file exists, it is used only if the
               personal dfilters file does not exist; global and personal
               display filters are not merged.

           Display Filter Macros

               The dmacros files contain system-wide and personal display
               filter macros. Each line contains one filter, starting with
               the string displayed in the dialog box in quotation marks,
               followed by the macro expression itself:

                   "private_ipv6" ipv6 && $1 == fc00::/7
                   "private_ethernet" $1[0] & 0x0F == 2
                   "private_ipv4" $1 == 192.168.0.0/16 or $1 == 172.16.0.0/12 or $1 == 10.0.0.0/8

               The global dmacros file uses the same directory as the global
               preferences file.

               The personal dmacros file uses the same directory as the
               personal preferences file. It is written through the
               Analyze:Display Filter Macros dialog.

               If the global dmacros file exists, it is used only if the
               personal dmacros file does not exist; global and personal
               display filters are not merged.

               Prior to Wireshark 4.4, a dfilter_macros file with a somewhat
               different syntax was used. That file is looked for at startup
               if a dmacros file is not found and used to migrate to the new
               format.

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

           WIRESHARK_ABORT_ON_DISSECTOR_BUG
               If this environment variable is set, Stratoshark will call
               abort(3) when a dissector bug is encountered. abort(3) will
               cause the program to exit abnormally; if you are running
               Stratoshark in a debugger, it should halt in the debugger and
               allow inspection of the process, and, if you are not running
               it in a debugger, it will, on some OSes, assuming your
               environment is configured correctly, generate a core dump
               file. This can be useful to developers attempting to
               troubleshoot a problem with a protocol dissector.

           WIRESHARK_ABORT_ON_TOO_MANY_ITEMS
               If this environment variable is set, Stratoshark will call
               abort(3) if a dissector tries to add too many items to a tree
               (generally this is an indication of the dissector not breaking
               out of a loop soon enough). abort(3) will cause the program to
               exit abnormally; if you are running Stratoshark in a debugger,
               it should halt in the debugger and allow inspection of the
               process, and, if you are not running it in a debugger, it
               will, on some OSes, assuming your environment is configured
               correctly, generate a core dump file. This can be useful to
               developers attempting to troubleshoot a problem with a
               protocol dissector.

           WIRESHARK_QUIT_AFTER_CAPTURE
               Cause Stratoshark to exit after the end of the capture
               session. This doesn’t automatically start a capture; you must
               still use -k to do that. You must also specify an autostop
               condition, e.g. -c or -a duration:.... This means that you
               will not be able to see the results of the capture after it
               stops; it’s primarily useful for testing.

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

## [](#AUTHORS)AUTHORS

           Stratoshark would not be the powerful, featureful application it
           is without the generous contributions of hundreds of developers.

           A complete list of authors can be found in the AUTHORS file in
           Wireshark’s source code repository.

## [](#SEE_ALSO)SEE ALSO

           wireshark-filter(4), strato(1), editcap(1), dumpcap(1),
           mergecap(1)

## [](#NOTES)NOTES

           This is the manual page for Stratoshark 0.10.3. The latest version
           of Stratoshark can be found at https://stratoshark.org/.

           HTML versions of the Wireshark project man pages are available at
           https://www.wireshark.org/docs/man-pages/. This page is part of
           the wireshark (Interactively dump and analyze network traffic)
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

                                    2026-01-15                 STRATOSHARK(1)

------------------------------------------------------------------------

Pages that refer to this page: [dumpcalls(1)](../man1/dumpcalls.1.html),  [falcodump(1)](../man1/falcodump.1.html),  [sshdig(1)](../man1/sshdig.1.html),  [strato(1)](../man1/strato.1.html)

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
