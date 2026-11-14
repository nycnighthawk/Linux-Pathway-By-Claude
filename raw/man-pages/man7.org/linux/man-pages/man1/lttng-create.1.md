---
{"title": "lttng-create(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lttng-create.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-create(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-CREATE(1)                LTTng Manual               LTTNG-CREATE(1)

## [](#NAME)NAME

           lttng-create - Create an LTTng recording session

## [](#SYNOPSIS)SYNOPSIS

           Create a local mode recording session:

           lttng [GENERAL OPTIONS] create [SESSION] [--shm-path=DIR]
                 [--no-output | --output=DIR | --set-url=file://DIR]
                 [--trace-format=(default | ctf-1.8 | ctf-2)]

           Create a network streaming mode recording session:

           lttng [GENERAL OPTIONS] create [SESSION] [--shm-path=DIR]
                 (--set-url=URL | --ctrl-url=URL --data-url=URL)
                 [--trace-format=(default | ctf-1.8 | ctf-2)]

           Create a snapshot mode recording session:

           lttng [GENERAL OPTIONS] create [SESSION] --snapshot [--shm-path=DIR]
                 [--no-output | --output=DIR | --set-url=URL |
                  --ctrl-url=URL --data-url=URL]
                 [--trace-format=(default | ctf-1.8 | ctf-2)]

           Create a live mode recording session:

           lttng [GENERAL OPTIONS] create [SESSION] --live[=DELAYUS]
                 [--shm-path=DIR] [--set-url=URL | --ctrl-url=URL --data-url=URL]
                 [--trace-format=(default | ctf-1.8 | ctf-2)]

## [](#DESCRIPTION)DESCRIPTION

           The lttng create command creates a new recording session for your
           Unix user within the connected session daemon (see the “Session
           daemon connection” section of lttng(1) to learn how a user
           application connects to a session daemon).

           See lttng-concepts(7) to learn more about recording sessions.

           Without the SESSION argument, LTTng automatically generates a
           recording session name having the auto-YYYYmmdd-HHMMSS form, where
           YYYYmmdd and HHMMSS are the creation date and time. SESSION may
           NOT contain the character /.

           Specify the path of the directory containing the shared memory
           files holding the channel ring buffers with the --shm-path option.
           Specifying a location on an NVRAM file system makes it possible to
           recover the latest recorded trace data when the system reboots
           after a crash with the lttng-crash(1) utility. Note that, as of
           LTTng 2.15.1, this feature is only available for user space
           channels.

           By default, the create command automatically spawns:

           •   A session daemon for your Unix user if none is currently
               running.

               Override the path of the session daemon binary to spawn with
               the general --sessiond-path option.

               Avoid automatically spawning a session daemon with the general
               --no-sessiond option.

           •   A relay daemon (see lttng-relayd(8)) if all the following
               statements are true:

               •   You specify the --live option.

               •   You don’t specify any of the --set-url, --ctrl-url, or
                   --data-url options.

               •   No relay daemon is currently listening for TCP connections
                   on 127.0.0.1:5344 (default LTTng live reader connection
                   address and port).

               In this case, the create command spawns a relay daemon as
               such:

                   lttng-relayd --live-port=tcp://localhost:5344

               Override the path of the relay daemon binary to spawn with the
               general --relayd-path option.

           By default, the create command creates a recording session for
           which LTTng will write traces using the configured default format
           of lttng-sessiond(8) (see its --default-trace-format option). Use
           the a specific format with the --trace-format option.

           On success, the create command sets the current recording session
           (see lttng-concepts(7) to learn more) to the created recording
           session.

           See the “EXAMPLES” section below for usage examples.

           Show the status of the current recording session with the
           lttng-status(1) command.

           List the recording sessions of your Unix user, or of all users if
           your Unix user is root, within the connected session daemon with
           the lttng-list(1) command.

           Start and stop one or more recording sessions with the
           lttng-start(1) and lttng-stop(1) commands.

           Save and load a recording session with the lttng-save(1) and
           lttng-load(1) commands.

           Allow and disallow specific processes to record events with the
           lttng-track(1) and lttng-untrack(1) commands.

           Archive the current trace chunk of (rotate) a recording session
           with the lttng-rotate(1) command.

           Destroy one or more recording session with the lttng-destroy(1)
           command.

       Recording session modes
           As documented in lttng-concepts(7), LTTng offers four recording
           session modes:

           Local mode
               Write the trace data to the local file system.

               The trace data output directory is:

               With the --no-output option
                   None: the file system output is disabled.

               With the --output=DIR or --set-url=file://DIR option
                   The directory DIR.

               Otherwise
                   A subdirectory, under the $LTTNG_HOME/lttng-traces
                   ($LTTNG_HOME defaults to $HOME) directory, of which the
                   name contains the recording session name and the
                   date/time.

           Network streaming mode
               Send the trace data over the network to a listening relay
               daemon (see lttng-relayd(8)).

               Set the trace output destination with the --set-url option, or
               with the --ctrl-url and --data-url options (see the “URL
               format” section below).

           Snapshot mode (--snapshot option)
               Only write the trace data to the local file system or send it
               to a listening relay daemon (lttng-relayd(8)) when LTTng takes
               a snapshot (see the lttng-snapshot(1) command).

               With this mode, LTTng:

               With the --no-output option
                   Does NOT add any snapshot output to the created recording
                   session.

               With the --output option, the --set-url option, or the --ctrl-
               url and --data-url options
                   Adds a snapshot output named snapshot-1 using the provided
                   path or URL(s) to the created recording session.

               Otherwise
                   Adds an automatic snapshot output named snapshot-1 to the
                   created recording session.

                   The automatic snapshot output is a subdirectory, under the
                   $LTTNG_HOME/lttng-traces ($LTTNG_HOME defaults to $HOME)
                   directory, of which the name contains the recording
                   session name and the date/time.

           Live mode (--live option)
               Send the trace data over the network to a listening relay
               daemon (see lttng-relayd(8)) for live reading.

               Set the trace output destination with the --set-url=URL
               option, or with the --ctrl-url=URL and --data-url=URL options
               (see the “URL format” section below).  URL may NOT start with
               file://.

       URL format
           The argument of the --set-url=URL, --ctrl-url=URL, and --data-
           url=URL options is an URL.

           There are two available URL formats.

           Local format

                   file://TRACEDIR

               The file:// protocol targets the local file system: you may
               only use such an URL with the --set-url option when you create
               the recording session in local or snapshot mode (see the
               “Recording session modes” section above).

               TRACEDIR
                   Absolute path to the directory containing the trace data
                   on the local file system.

           Network format

                   NETPROTO://(HOST | IPADDR)[:CTRLPORT[:DATAPORT]][/TRACEDIR]

               This format is only available when you create the recording
               session in network streaming, snapshot (--snapshot), or live
               (--live) mode (see the “Recording session modes” section
               above).

               NETPROTO
                   Network protocol, amongst:

                   net
                       TCP over IPv4.

                       The default values of CTRLPORT and DATAPORT are
                       respectively 5342 and 5343.

                   net6
                       TCP over IPv6.

                       The default values of CTRLPORT and DATAPORT are
                       respectively 5342 and 5343.

                   tcp
                       Same as the net protocol.

                       You may only use this with the --ctrl-url and --data-
                       url options together.

                   tcp6
                       Same as the net6 protocol.

                       You can only be use this with the --ctrl-url and
                       --data-url options together.

               (HOST | IPADDR)
                   Hostname or IP address.

                   IPv6 address must be enclosed in square brackets ([
                   and ]); see RFC 2732
                   <https://www.ietf.org/rfc/rfc2732.txt>.

               CTRLPORT
                   Control TCP port.

               DATAPORT
                   Data TCP port.

               TRACEDIR
                   Path of the directory containing the trace data on the
                   remote file system.

                   This path is relative to the base output directory of the
                   LTTng relay daemon (see the --output option of
                   lttng-relayd(8)).

## [](#OPTIONS)OPTIONS

           See lttng(1) for GENERAL OPTIONS.

       Mode selection
           See the “Recording session modes” section above.

           At most one of:

           --live[=DELAYUS]
               Create the recording session in live mode.

               The optional DELAYUS argument is the maximum time (in µs) you
               can wait for the data to be flushed (sent to the connected
               LTTng relay daemon). The default value of DELAYUS is 1000000.

               Set the URL of the relay daemon to connect to with the --set-
               url option, or with the --ctrl-url and --data-url options,
               instead of using net://127.0.0.1.

               The session daemon must be able to connect to a listening
               relay daemon (see lttng-relayd(8)).

           --snapshot
               Create the recording session in snapshot mode.

               This is equivalent to:

               •   One of:

                   With the --no-output option
                       Not adding any snapshot output after LTTng creates the
                       recording session.

                   With the --output option, the --set-url option, or the
                   --ctrl-url and --data-url options
                       Adding a snapshot output named snapshot-1 using the
                       provided path or URL(s) immediately after LTTng
                       creates the recording session.

                   Otherwise
                       Adding an automatic snapshot output named snapshot-1
                       immediately after LTTng creates the recording session.

                       The automatic snapshot output is a subdirectory, under
                       the $LTTNG_HOME/lttng-traces ($LTTNG_HOME defaults to
                       $HOME) directory, of which the name contains the
                       recording session name and the date/time.

               •   Forcing all the channels to be created for the recording
                   session to be configured with the --override and
                   --output=mmap options (see lttng-enable-channel(1)).

       Output
           --no-output
               Depending on the recording session mode (see the “Recording
               session modes” section above):

               Local mode
                   Disable the file system output.

               Snapshot mode (--snapshot option)
                   Do NOT add a snapshot output after creating the recording
                   session.

           -o DIR, --output=DIR
               Equivalent to --set-url=file://DIR.

           --shm-path=DIR
               Set the path of the directory containing the shared memory
               files holding the channel ring buffers to DIR on the local
               file sytem.

               Note
                   As of LTTng 2.15.1, LTTng only considers this option for
                   user space (including Java and Python) channels, but this
                   may change in the future.

           -F FORMAT, --trace-format=FORMAT
               Set the output format of the created recording session to
               FORMAT.

               FORMAT is one of:

               default
                   Use the configured default format of lttng-sessiond(8)
                   (see its --default-trace-format option).

               ctf-1.8
                   CTF 1.8 <https://diamon.org/ctf/v1.8.3/> (legacy).

               ctf-2
                   CTF 2 <https://diamon.org/ctf/> (preferred).

               Default: default.

       URL
           See the “URL format” section above to learn more about the syntax
           of the URL argument of the following options.

           -C URL, --ctrl-url=URL
               Set the control path URL to URL.

               You must also use the --data-url option.

               Not available in local mode (see the “Recording session modes”
               section above).

               In snapshot mode, this is equivalent to using the --ctrl-url
               option of the add-output action of the lttng-snapshot(1)
               command immediately after creating the recording session.

           -D URL, --data-url=URL
               Set the trace data path URL to URL.

               You must also use the --ctrl-url option.

               Not available in local mode (see the “Recording session modes”
               section above).

               In snapshot mode, this is equivalent to using the --data-url
               option of the add-output action of the lttng-snapshot(1)
               command immediately after creating the recording session.

           -U URL, --set-url=URL
               Set the destination URL of the control path and trace data to
               URL.

               This URL remains unchanged as long as the recording session
               exists.

               Depending on the recording session mode (see the “Recording
               session modes” section above):

               Local mode
                   URL must start with file://, followed with the destination
                   directory path on the local file system.

               Network streaming and live modes
                   Equivalent to using both the --ctrl-url and --data-url
                   options.

               Snapshot mode (--snapshot option)
                   Equivalent to using the URL non-option argument of the
                   add-output action of the lttng-snapshot(1) command
                   immediately after creating the recording session.

       Program information
           -h, --help
               Show help.

               This option attempts to launch /usr/bin/man to view this
               manual page. Override the manual pager path with the
               LTTNG_MAN_BIN_PATH environment variable.

           --list-options
               List available command options and quit.

## [](#EXIT_STATUS)EXIT STATUS

           0
               Success

           1
               Command error

           2
               Undefined command

           3
               Fatal error

           4
               Command warning (something went wrong during the command)

## [](#ENVIRONMENT)ENVIRONMENT

           LTTNG_ABORT_ON_ERROR
               Set to 1 to abort the process after the first error is
               encountered.

           LTTNG_HOME
               Path to the LTTng home directory.

               Defaults to $HOME.

               Useful when the Unix user running the commands has a
               non-writable home directory.

           LTTNG_LIST_LEGACY
               Set to 1 to use the legacy output format (LTTng 2.14 and
               earlier) for the lttng-list(1) command instead of the modern
               output format.

               Note that the legacy output doesn’t show anything related to
               features introduced after LTTng 2.14.

           LTTNG_MAN_BIN_PATH
               Absolute path to the manual pager to use to read the LTTng
               command-line help (with lttng-help(1) or with the --help
               option) instead of /usr/bin/man.

           LTTNG_NO_UTF_8
               Set to 1 to NOT emit multi-byte UTF-8 sequences, even if the
               locale claims to support it.

           LTTNG_SESSION_CONFIG_XSD_PATH
               Path to the directory containing the session.xsd recording
               session configuration XML schema.

           LTTNG_SESSIOND_PATH
               Absolute path to the LTTng session daemon binary (see
               lttng-sessiond(8)) to spawn from the lttng-create(1) command.

               The --sessiond-path general option overrides this environment
               variable.

           LTTNG_TERM_COLOR
               Controls when to emit terminal SGR codes in the output.

               The NO_COLOR environment variable overrides this.

               One of:

               auto (default)
                   Only emit SGR codes when the standard output is connected
                   to a color-capable terminal.

               always
                   Always emit SGR codes.

               never
                   Never emit SGR codes.

           NO_COLOR
               If set and not empty, then it’s equivalent to setting
               LTTNG_TERM_COLOR to never.

               See NO_COLOR <https://no-color.org/> to learn more.

## [](#FILES)FILES

           $LTTNG_HOME/.lttngrc
               Unix user’s LTTng runtime configuration.

               This is where LTTng stores the name of the Unix user’s current
               recording session between executions of lttng(1).
               lttng-create(1) and lttng-set-session(1) set the current
               recording session.

           $LTTNG_HOME/lttng-traces
               Default output directory of LTTng traces in local and snapshot
               modes.

               Override this path with the --output option of the
               lttng-create(1) command.

           $LTTNG_HOME/.lttng
               Unix user’s LTTng runtime and configuration directory.

           $LTTNG_HOME/.lttng/sessions
               Default directory containing the Unix user’s saved recording
               session configurations (see lttng-save(1) and lttng-load(1)).

           /usr/local/etc/lttng/sessions
               Directory containing the system-wide saved recording session
               configurations (see lttng-save(1) and lttng-load(1)).

           Note

               $LTTNG_HOME defaults to the value of the HOME environment
               variable.

## [](#EXAMPLES)EXAMPLES

           Example 1. Create a normal mode recording session with a generated
           name.

                   $ lttng create

           Example 2. Create a normal mode recording session with a custom
           name.

                   $ lttng create my-session

           Example 3. Create a normal mode recording session with a specific
           output directory.

               See the --output option.

                   $ lttng create --output=/path/to/traces

           Example 4. Create a network streaming mode recording session.

               See the “Output directory” section of lttng-relayd(8) to
               understand where the relay daemon to connect to (10.0.0.242)
               writes the received traces.

               See the --set-url option.

                   $ lttng create --set-url=net://10.0.0.242/inv4

           Example 5. Create a snapshot mode recording session with a default
           snapshot output.

               See the --snapshot option.

                   $ lttng create --snapshot

           Example 6. Create a snapshot mode recording session with a custom
           snapshot output.

               See the --snapshot and --set-url options.

                   $ lttng create --snapshot \
                           --set-url=tcp://192.168.1.102:1234:5678/my-snapshots

           Example 7. Create a snapshot mode recording session with no
           snapshot output.

               See the --snapshot and --no-output options.

                   $ lttng create --snapshot --no-output

           Example 8. Create an LTTng live mode recording session with a
           default relay daemon URL.

               See the --live option.

                   $ lttng create --live

           Example 9. Create an LTTng live mode recording session with a
           custom live timer period and relay daemon URL.

               See the --live and --set-url options.

                   $ lttng create --live=250000 \
                                  --set-url=tcp://relayd34:4885:4886

           Example 10. Create a normal mode recording session with a custom
           directory containing the ring buffer shared memory files.

               See the --shm-path option.

                   $ lttng create my-session --shm-path=/mnt/nvram2/lttng

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

           lttng(1), lttng-destroy(1), lttng-enable-channel(1),
           lttng-list(1), lttng-rotate(1), lttng-save(1),
           lttng-set-session(1), lttng-start(1), lttng-status(1),
           lttng-track(1), lttng-concepts(7), lttng-relayd(8),
           lttng-sessiond(8)

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

    LTTng 2.15.1                  7 October 2025              LTTNG-CREATE(1)

------------------------------------------------------------------------

Pages that refer to this page: [lttng(1)](../man1/lttng.1.html),  [lttng-add-context(1)](../man1/lttng-add-context.1.html),  [lttng-add-trigger(1)](../man1/lttng-add-trigger.1.html),  [lttng-clear(1)](../man1/lttng-clear.1.html),  [lttng-crash(1)](../man1/lttng-crash.1.html),  [lttng-create(1)](../man1/lttng-create.1.html),  [lttng-destroy(1)](../man1/lttng-destroy.1.html),  [lttng-disable-channel(1)](../man1/lttng-disable-channel.1.html),  [lttng-disable-event(1)](../man1/lttng-disable-event.1.html),  [lttng-disable-rotation(1)](../man1/lttng-disable-rotation.1.html),  [lttng-enable-channel(1)](../man1/lttng-enable-channel.1.html),  [lttng-enable-event(1)](../man1/lttng-enable-event.1.html),  [lttng-enable-rotation(1)](../man1/lttng-enable-rotation.1.html),  [lttng-help(1)](../man1/lttng-help.1.html),  [lttng-list(1)](../man1/lttng-list.1.html),  [lttng-list-triggers(1)](../man1/lttng-list-triggers.1.html),  [lttng-load(1)](../man1/lttng-load.1.html),  [lttng-metadata(1)](../man1/lttng-metadata.1.html),  [lttng-reclaim-memory(1)](../man1/lttng-reclaim-memory.1.html),  [lttng-regenerate(1)](../man1/lttng-regenerate.1.html),  [lttng-remove-trigger(1)](../man1/lttng-remove-trigger.1.html),  [lttng-rotate(1)](../man1/lttng-rotate.1.html),  [lttng-save(1)](../man1/lttng-save.1.html),  [lttng-set-session(1)](../man1/lttng-set-session.1.html),  [lttng-snapshot(1)](../man1/lttng-snapshot.1.html),  [lttng-start(1)](../man1/lttng-start.1.html),  [lttng-status(1)](../man1/lttng-status.1.html),  [lttng-stop(1)](../man1/lttng-stop.1.html),  [lttng-track(1)](../man1/lttng-track.1.html),  [lttng-untrack(1)](../man1/lttng-untrack.1.html),  [lttng-version(1)](../man1/lttng-version.1.html),  [lttng-view(1)](../man1/lttng-view.1.html),  [babeltrace2-source.ctf.lttng-live(7)](../man7/babeltrace2-source.ctf.lttng-live.7.html),  [lttng-concepts(7)](../man7/lttng-concepts.7.html),  [lttng-relayd(8)](../man8/lttng-relayd.8.html),  [lttng-sessiond(8)](../man8/lttng-sessiond.8.html)

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
