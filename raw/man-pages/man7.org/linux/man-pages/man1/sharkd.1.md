---
{"title": "sharkd(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/sharkd.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sharkd(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DIAGNOSTIC OPTIONS](#DIAGNOSTIC_OPTIONS) \| [JSON-RPC METHODS](#JSON-RPC_METHODS) \| [EXAMPLES](#EXAMPLES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SHARKD(1)                                                       SHARKD(1)

## [](#NAME)NAME

           sharkd - Interactively dump and analyze network traffic using
           JSON-RPC.

## [](#SYNOPSIS)SYNOPSIS

           sharkd [ -a|--api <socket> ] [ --foreground ] [
           -C|--config-profile <configuration profile> ]

           sharkd -

           sharkd -h|--help

           sharkd -v|--version

## [](#DESCRIPTION)DESCRIPTION

           Sharkd is a daemon variant of Wireshark that provides a JSON-based
           API for performing network protocol analysis. It uses the same
           dissection engine as Wireshark and TShark, enabling programmatic
           access to packet dissection, filtering, and analysis capabilities.

           Sharkd can operate in two modes: console mode and daemon mode.

           In console mode, sharkd reads reads JSON-RPC requests from
           standard input and writes responses to standard output. This mode
           is activated by passing - as the argument or by running sharkd
           without the -a option.

           In daemon mode, sharkd listens on a Unix domain socket or TCP
           socket for incoming connections, forking a new session process for
           each client. This mode is activated by passing the -a option with
           a socket specification.

           Requests and responses are encoded as JSON objects, one per line.
           See JSON-RPC METHODS below for a complete list of method calls.

           For full details on the JSON-RPC API, see
           https://wiki.wireshark.org/Development/sharkd.

               Warning

               Sharkd should not be exposed to untrusted users. Unfiltered
               access to sharkd could potentially result in information
               disclosure or arbitrary command execution.

## [](#OPTIONS)OPTIONS

           -a <socket>, --api <socket>

               Listen on the specified socket for incoming client connections
               instead of reading from the console. When this option is used,
               sharkd runs as a daemon, forking a new session process for
               each client connection.

               Supported socket types:

               unix:path
                   Listen on a Unix domain socket at path. For example,
                   unix:/tmp/sharkd.sock. On Linux, abstract sockets are
                   supported by prefixing the name with @, for example
                   unix:@sharkd; abstract sockets only support connections
                   from peers with the same effective UID. Unix domain
                   sockets are available on Windows 10 version 1803 and
                   later, including Windows Server 2019.

               tcp:address:port
                   Listen on a TCP socket bound to address on port. For
                   example, tcp:127.0.0.1:4446. For IPv6 addresses, enclose
                   the address in square brackets, e.g. tcp:[[::1]:5678. For
                   security reasons, TCP sockets are only available on
                   Windows builds by default and only loopback addresses are
                   supported, i.e. an IPv4 address in the 127.0.0.0/8 address
                   space or the ::1 IPv6 loopback address.

               If no -a option is provided, or if sharkd - is used, sharkd
               will accept commands via the console (standard input).

           --foreground
               When running in daemon mode, do not detach from the
               controlling terminal. By default, sharkd forks into the
               background when a socket is specified with the -a option.

           -C <configuration profile>, --config-profile <configuration
           profile>
               Start with the specified configuration profile.

           -h, --help
               Print the version number and options and exit.

           -v, --version
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

## [](#JSON-RPC_METHODS)JSON-RPC METHODS

           Sharkd accepts newline-delimited JSON-RPC requests. Each request
           must include a jsonrpc field set to "2.0", a method field, and an
           id field. The following methods are supported:

           analyse
               Analyse the loaded capture file and return summary
               information.

           bye
               Terminate the session.

           check
               Check or compile a display filter.

           complete
               Provide field name completion suggestions.

           download
               Download captured data or reassembled objects.

           dumpconf
               Dump current preference values.

           field
               Get information about a specific display filter field.

           fields
               List all available display filter fields.

           follow
               Follow a stream (TCP, UDP, HTTP, etc.).

           frame
               Get detailed information about a specific frame.

           frames
               Get a list of frames (packets) from the loaded capture file.

           info
               Get information about available dissectors, taps, and
               statistics.

           intervals
               Get frame interval data for the loaded capture file.

           iograph
               Get I/O graph data for the loaded capture file.

           load
               Load a capture file for analysis.

           setcomment
               Set a comment on a specific frame.

           setconf
               Set a Wireshark preference value.

           status
               Get the status of the currently loaded capture file.

           tap
               Run a tap on the loaded capture file.

## [](#EXAMPLES)EXAMPLES

           To run sharkd in console mode:

               sharkd -

           To run sharkd as a daemon listening on a Unix domain socket:

               sharkd -a unix:/tmp/sharkd.sock

           To run sharkd as a daemon with a specific configuration profile:

               sharkd -a unix:/tmp/sharkd.sock -C myprofile

           To keep the daemon in the foreground for debugging:

               sharkd -a unix:/tmp/sharkd.sock --foreground

           An example console session, loading a file and getting its status:

               $ echo '{"jsonrpc":"2.0","id":1,"method":"load","params":{"file":"/path/to/capture.pcapng"}}' | sharkd -
               $ echo '{"jsonrpc":"2.0","id":2,"method":"status"}' | sharkd -

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
               If this environment variable is set, TShark will call abort(3)
               when a dissector bug is encountered. abort(3) will cause the
               program to exit abnormally; if you are running TShark in a
               debugger, it should halt in the debugger and allow inspection
               of the process, and, if you are not running it in a debugger,
               it will, on some OSes, assuming your environment is configured
               correctly, generate a core dump file. This can be useful to
               developers attempting to troubleshoot a problem with a
               protocol dissector.

           WIRESHARK_ABORT_ON_TOO_MANY_ITEMS
               If this environment variable is set, TShark will call abort(3)
               if a dissector tries to add too many items to a tree
               (generally this is an indication of the dissector not breaking
               out of a loop soon enough). abort(3) will cause the program to
               exit abnormally; if you are running TShark in a debugger, it
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

           wireshark-filter(4), wireshark(1), editcap(1), pcap(3),
           dumpcap(1), text2pcap(1), mergecap(1), pcap-filter(7) or
           tcpdump(8)

## [](#NOTES)NOTES

           This is the manual page for Sharkd 4.7.3. Sharkd is part of the
           Wireshark distribution. The latest version of Wireshark can be
           found at https://www.wireshark.org.

           HTML versions of the Wireshark project man pages are available at
           https://www.wireshark.org/docs/man-pages.

## [](#AUTHORS)AUTHORS

           Sharkd was written by Jakub Zawadzki. Sharkd uses the same packet
           dissection code that Wireshark does, as well as using many other
           modules from Wireshark; see the list of authors in the Wireshark
           man page for a list of authors of that code..SH COLOPHON This page
           is part of the wireshark (Interactively dump and analyze network
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

                                    2026-08-03                      SHARKD(1)

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
