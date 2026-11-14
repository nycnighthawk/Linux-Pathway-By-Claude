---
{"title": "lttng-relayd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lttng-relayd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-relayd(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-RELAYD(8)                LTTng Manual               LTTNG-RELAYD(8)

## [](#NAME)NAME

           lttng-relayd - LTTng relay daemon

## [](#SYNOPSIS)SYNOPSIS

           lttng-relayd [--background | --daemonize] [--config=PATH]
                        [--control-port=URL] [--data-port=URL] [--fd-pool-size=COUNT]
                        [--live-port=URL] [--dynamic-port-allocation] [--output=DIR]
                        [--group=GROUP] [--verbose]... [--working-directory=DIR]
                        [--group-output-by-host | --group-output-by-session] [--disallow-clear]
                        [--pid-file=PATH] [--sig-parent]

## [](#DESCRIPTION)DESCRIPTION

           The Linux Trace Toolkit: next generation <https://lttng.org/> is
           an open-source software package used for correlated tracing of the
           Linux kernel, user applications, and user libraries.

           LTTng consists of Linux kernel modules (for Linux kernel tracing)
           and dynamically loaded libraries (for user application and library
           tracing).

           An LTTng relay daemon, lttng-relayd, is a program which receives
           trace data from (possibly remote) LTTng session/consumer daemons
           and which writes it to the local file system. The relay daemon
           also accepts LTTng live connections from compatible readers (for
           example, babeltrace2(1)); this is the recommended approach to read
           trace data while the remote recording session is active.

           By default, a relay daemon listens on all network interfaces to
           receive trace data, but only on localhost for LTTng live
           connections. Override the listening URLs with the --control-port,
           --data-port, and --live-port options (see the “URL format” section
           below). For example, use the --live-port=tcp://0.0.0.0:5344 option
           to make a relay daemon listen to LTTng live connections on all
           network interfaces.

           Once LTTng has completely sent a trace to a relay daemon RD, any
           LTTng trace reader can read the trace located on the local file
           system of RD.

           By default, lttng-relayd doesn’t start as a daemon. Make it a
           daemon with the --daemonize or --background option. With those
           options, lttng-relayd ensures the daemon is listening to incoming
           connections before it exits. Make lttng-relayd write its process
           ID to a file with the --pid-file option.

       Daemon configuration
           When you run lttng-relayd, it configures itself from, in this
           order:

            1. The INI configuration file /usr/local/etc/lttng/lttng.conf, if
               any.

            2. The INI configuration file $LTTNG_HOME/.lttng/lttng.conf, if
               any.

               $LTTNG_HOME defaults to $HOME.

            3. With the --config=PATH option: the INI configuration file
               PATH.

            4. The command-line options.

           Each step can override a previous configuration property.

           In INI configuration files, the session daemon only reads the
           properties under the relayd INI section. Each INI property is:

           Key
               The long name of a command-line option to set (see the
               “OPTIONS” section below).

           Value

               The selected command-line option accepts an argument
                   Option argument (string).

               The selected command-line option is a switch

                   true, yes, on
                       Enable the option.

                   false, no, off
                       Disable the option.

           INI configuration file example:

               [relayd]
               daemonize=yes
               live-port=tcp://0.0.0.0:4567
               disallow-clear=yes

       Output directory
           The relay daemon uses different output path patterns depending on:

           •   Its configuration.

               See the “Daemon configuration” section above.

           •   The recording session configuration of the connected peer.

           •   The LTTng session daemon (see lttng-sessiond(8)) version of
               the connected peer.

           Consider the following variables:

           BASE
               Base output directory: $LTTNG_HOME/lttng-traces ($LTTNG_HOME
               defaults to $HOME) or the argument of the --output option.

           HOSTNAME
               Hostname of the connected peer.

           SESSION
               Recording session name.

           DATETIME
               Unique recording session date/time.

           TRACEDIR
               Custom trace directory path (TRACEDIR part of the argument of
               the --set-url option of the lttng-create(1) command, if any).

           SESSIONDV
               The version of the LTTng session daemon of the connected peer.

           The relay daemon output path patterns are:

           With the --group-output-by-host option (hostname grouping)

               Without a custom trace directory

                       BASE/HOSTNAME/SESSION-DATETIME

               With a custom trace directory

                       BASE/HOSTNAME/TRACEDIR

           With the --group-output-by-session option (recording session
           grouping)

               Without a custom trace directory

                   SESSIONDV is at least 2.4

                           BASE/SESSION/HOSTNAME-DATETIME

                   Otherwise
                       Defaults to the hostname grouping pattern:

                           BASE/HOSTNAME/SESSION-DATETIME

               With a custom trace directory

                   SESSIONDV is at least 2.4

                           BASE/SESSION/HOSTNAME-DATETIME/TRACEDIR

                   Otherwise
                       Defaults to the hostname grouping pattern:

                           BASE/HOSTNAME/TRACEDIR

       URL format
           The argument of the --control-port=URL, --data-port=URL, and
           --live-port=URL options is an URL.

           The format of URL is:

               tcp://(HOST | IPADDR):PORT

           with:

           (HOST | IPADDR)
               Binding hostname or IP address.

               IPv6 address must be enclosed in square brackets ([ and ]);
               see RFC 2732 <https://www.ietf.org/rfc/rfc2732.txt>.

           PORT
               TCP port.

               If this value is 0 and the --dynamic-port-allocation option is
               set, then the operating system assigns a port number itself.

## [](#OPTIONS)OPTIONS

       General daemon configuration
           -b, --background
               Start as a Unix daemon, but keep file descriptors (console)
               open.

               With this option, lttng-relayd ensures the daemon is listening
               to incoming connections before it exits.

               Use the --daemonize option instead to close the file
               descriptors.

           -f PATH, --config=PATH
               Configure the daemon using the INI configuration file PATH in
               addition to the default configuration files and the
               command-line options.

               See the “Daemon configuration” section above.

           -d, --daemonize
               Start as a Unix daemon and close file descriptors (console).

               With this option, lttng-relayd ensures the daemon is listening
               to incoming connections before it exits.

               Use the --background option instead to keep the file
               descriptors open.

           -x, --disallow-clear
               Disallow clearing operations (see lttng-clear(1)).

               See also the LTTNG_RELAYD_DISALLOW_CLEAR environment variable.

           --dynamic-port-allocation
               Let the operating system assign the control, data, and live
               ports if their respective option is missing (--control-port,
               --data-port, and --live-port) or if their port number part
               is 0.

               With this option, lttng-relayd writes the control.port,
               data.port, and live.port files, as needed, to its runtime and
               configuration directory ($LTTNG_HOME/.lttng). Such a port file
               contains the textual port number (decimal) followed with a
               newline.

           --fd-pool-size=SIZE
               Set the size of the file descriptor pool to SIZE file
               descriptors.

               SIZE is the maximum number of file descriptors that the relay
               daemon may keep open simultaneously.

               Default: the soft RLIMIT_NOFILE resource limit of the process
               (see getrlimit(2)).

           -g GROUP, --group=GROUP
               Set the Unix tracing group to GROUP instead of tracing.

               This option is only meaningful when the root Unix user starts
               lttng-relayd.

               Members of the Unix tracing group may connect to the health
               check socket of the relay daemon.

               See also the LTTNG_RELAYD_HEALTH environment variable.

           -P PATH, --pid-file=PATH
               Write the process ID (PID) of the lttng-relayd process to
               PATH.

               Such a file contains the textual PID (decimal) followed with a
               newline.

               lttng-relayd doesn’t use this file and removes it when it
               exits.

           -S, --sig-parent
               Send the USR1 signal to the parent process to notify
               readiness.

               You can also use the --daemonize or --background option, in
               which case lttng-relayd ensures the daemon is ready to receive
               client commands before it exits.

           -v, --verbose
               Increase verbosity.

               Specify this option up to three times to get more levels of
               verbosity.

           -w DIR, --working-directory=DIR
               Set the working directory of the processes the relay daemon
               creates to DIR.

               See also the LTTNG_RELAYD_WORKING_DIRECTORY environment
               variable.

       Output
           See the “Output directory” section above to learn more.

           -p, --group-output-by-host
               Group the written trace directories by hostname.

               As of LTTng 2.15.1, this is the default output grouping
               strategy, but this may change in the future.

           -s, --group-output-by-session
               Group the written trace directories by recording session name
               instead of by hostname.

           -o DIR, --output=DIR
               Set the base output directory of the written trace directories
               to DIR.

       Ports
           See the “URL format” section above to learn more about the syntax
           of the URL argument of the following options.

           For the following options: if the --dynamic-port-allocation option
           is set and the port option is either missing or the port number
           part of URL is 0, then the operating system assigns a port number
           itself.

           -C URL, --control-port=URL
               Listen to control data on URL URL.

               Default: tcp://0.0.0.0:5342.

           -D URL, --data-port=URL
               Listen to trace data on URL URL.

               Default: tcp://0.0.0.0:5343.

           -L URL, --live-port=URL
               Listen to LTTng live connections on URL URL.

               Default: tcp://localhost:5344.

       Program information
           -h, --help
               Show help.

               This option attempts to launch /usr/bin/man to view this
               manual page. Override the manual pager path with the
               LTTNG_MAN_BIN_PATH environment variable.

           --list-options
               List available command options and quit.

           -V, --version
               Show version and quit.

## [](#EXIT_STATUS)EXIT STATUS

           0
               Success

           1
               Error

           3
               Fatal error

## [](#ENVIRONMENT)ENVIRONMENT

           LTTNG_ABORT_ON_ERROR
               Set to 1 to abort the process after the first error is
               encountered.

           LTTNG_NETWORK_SOCKET_TIMEOUT
               Socket connection, receive, and send timeout (milliseconds).

               Set to 0 or -1 to set an infinite timeout (default).

           LTTNG_RELAYD_DISALLOW_CLEAR
               Set to 1 to disallow clearing operations (see lttng-clear(1)).

               The --disallow-clear option overrides this environment
               variable.

           LTTNG_RELAYD_HEALTH
               Path to the health check socket of the relay daemon.

           LTTNG_RELAYD_TCP_KEEP_ALIVE
               Set to 1 to enable TCP keep-alive.

               The TCP keep-alive mechanism allows the detection of dead
               peers (lttng-sessiond(8)) in cases of unclean termination (for
               example, a hard reset) of a peer.

               Supported on Linux and Solaris only. The default behaviour of
               the TCP keep-alive mechanism is OS-specific.

               Search for tcp_keepalive in tcp(7) to learn more.

           LTTNG_RELAYD_TCP_KEEP_ALIVE_ABORT_THRESHOLD
               The time threshold (seconds) to abort a TCP connection after
               the keep-alive probing mechanism has failed.

               Set to 0 or -1 to use the value chosen by the operating system
               (default).

               Supported on Solaris 11 only.

               Search for tcp_keepalive_abort_threshold in tcp(7) to learn
               more.

           LTTNG_RELAYD_TCP_KEEP_ALIVE_IDLE_TIME
               Number of seconds a connection needs to be idle before TCP
               begins sending out keep-alive probes.

               Set to 0 or -1 to use the value chosen by the operating system
               (default).

               Supported on Linux and Solaris 11 only.

               On Solaris 11, the accepted values are -1, 0, and 10 to
               864000.

               Search for tcp_keepalive_time and tcp_keepalive_interval in
               tcp(7) on Solaris 11 to learn more.

           LTTNG_RELAYD_TCP_KEEP_ALIVE_MAX_PROBE_COUNT
               Maximum number of TCP keep-alive probes to send before giving
               up and killing the connection if no response is obtained from
               the other end.

               Set to 0 or -1 to use the value chosen by the operating system
               (default).

               Supported on Linux only.

               Search for tcp_keepalive_probes in tcp(7) to learn more.

           LTTNG_RELAYD_TCP_KEEP_ALIVE_PROBE_INTERVAL
               Number of seconds between TCP keep-alive probes.

               Set to 0 or -1 to use the value chosen by the operating system
               (default).

               Supported on Linux only.

               Search for tcp_keepalive_intvl in tcp(7) to learn more.

           LTTNG_RELAYD_WORKING_DIRECTORY
               Working directory of the processes the relay daemon creates.

               The --working-directory option overrides this environment
               variable.

## [](#FILES)FILES

           $LTTNG_HOME/.lttng
               Unix user’s LTTng runtime and configuration directory.

           $LTTNG_HOME/lttng-traces
               Default base output directory of LTTng traces.

               Override this path with the --output option.

           Note

               $LTTNG_HOME defaults to $HOME.

## [](#RESOURCES)RESOURCES

           •   LTTng project website <https://lttng.org>

           •   LTTng documentation <https://lttng.org/docs>

           •   LTTng bug tracker <https://bugs.lttng.org>

           •   Git repositories <https://git.lttng.org>

           •   GitHub organization <https://github.com/lttng>

           •   Continuous integration <https://ci.lttng.org/>

           •   Mailing list <https://lists.lttng.org/> for support and
               development: lttng-dev@lists.lttng.org

           •   IRC channel <irc://irc.oftc.net/lttng>: #lttng on irc.oftc.net

           •   Mastodon <https://mastodon.social/@lttng>

## [](#COPYRIGHT)COPYRIGHT

           This program is part of the LTTng-tools project.

           LTTng-tools is distributed under the GNU General Public License
           version 2 <http://www.gnu.org/licenses/old-
           licenses/gpl-2.0.en.html>. See the LICENSE
           <https://github.com/lttng/lttng-tools/blob/master/LICENSE> file
           for details.

## [](#THANKS)THANKS

           Special thanks to Michel Dagenais and the DORSAL laboratory
           <http://www.dorsal.polymtl.ca/> at École Polytechnique de Montréal
           for the LTTng journey.

           Also thanks to the Ericsson teams working on tracing which helped
           us greatly with detailed bug reports and unusual test cases.

## [](#SEE_ALSO)SEE ALSO

           babeltrace2(1), lttng(1), lttng-sessiond(8)

## [](#COLOPHON)COLOPHON

           This page is part of the LTTng-Tools (LTTng tools) project.
           Information about the project can be found at ⟨http://lttng.org/⟩.
           It is not known how to report bugs for this man page; if you know,
           please send a mail to man-pages@man7.org.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/lttng/lttng-tools.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    LTTng 2.15.1                   1 April 2025               LTTNG-RELAYD(8)

------------------------------------------------------------------------

Pages that refer to this page: [lttng(1)](../man1/lttng.1.html),  [lttng-clear(1)](../man1/lttng-clear.1.html),  [lttng-create(1)](../man1/lttng-create.1.html),  [lttng-destroy(1)](../man1/lttng-destroy.1.html),  [lttng-rotate(1)](../man1/lttng-rotate.1.html),  [lttng-snapshot(1)](../man1/lttng-snapshot.1.html),  [babeltrace2-source.ctf.lttng-live(7)](../man7/babeltrace2-source.ctf.lttng-live.7.html),  [lttng-concepts(7)](../man7/lttng-concepts.7.html)

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
