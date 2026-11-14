---
{"title": "lttng-disable-event(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lttng-disable-event.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-disable-event(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-DISABLE-EVEN(1)          LTTng Manual         LTTNG-DISABLE-EVEN(1)

## [](#NAME)NAME

           lttng-disable-event - Disable LTTng recording event rules

## [](#SYNOPSIS)SYNOPSIS

           Disable one or more recording event rules matching Linux kernel
           events:

           lttng [GENERAL OPTIONS] disable-event --kernel
                 [--tracepoint | --syscall | --probe | --function]
                 (--all-events | NAME[,NAME]...)
                 [--session=SESSION] [--channel=CHANNEL]

           Disable one or more recording event rules matching user space
           tracepoint or Java/Python logging events:

           lttng [GENERAL OPTIONS] disable-event
                 (--userspace | --jul | --log4j | --log4j2 |--python) [--tracepoint]
                 (--all-events | NAME[,NAME]...)
                 [--session=SESSION] [--channel=CHANNEL]

## [](#DESCRIPTION)DESCRIPTION

           The lttng disable-event command disables one or more enabled
           recording event rules previously created with the
           lttng-enable-event(1) command which belong to:

           With the --session=SESSION option
               The recording session named SESSION.

           Without the --session option
               The current recording session (see lttng-concepts(7) to learn
               more about the current recording session).

           With the --channel=CHANNEL option
               The channel named CHANNEL.

           Without the --channel option
               The channel named channel0.

               If there’s more than one channel for the selected recording
               session and domain, the disable-event command fails.

           See lttng-concepts(7) to learn more about recording event rules.

           As of LTTng 2.15.1, the disable-event command can only find
           recording event rules to disable by their instrumentation point
           type and event name conditions. Therefore, you cannot disable
           recording event rules having a specific instrumentation point log
           level condition, for example.

           With the --kernel option and no instrumentation point type
           condition option, the disable-event command disables one or more
           Linux kernel recording event rules regardless of their
           instrumentation point type.

           List the recording event rules of a given recording session and/or
           channel with the lttng-list(1) command.

           Without the --all-events option, the disable-event command
           disables one recording event rule per NAME argument. NAME is the
           exact event name condition pattern of the recording event rule to
           disable, as listed in the output of lttng list (see
           lttng-list(1)).

           You may disable an enabled recording event rule regardless of the
           activity (started or stopped) of its recording session (see
           lttng-start(1) and lttng-stop(1)).

           See the “EXAMPLES” section below for usage examples.

## [](#OPTIONS)OPTIONS

           See lttng(1) for GENERAL OPTIONS.

       Tracing domain
           One of:

           -j, --jul
               Disable recording event rules in the java.util.logging (JUL)
               domain.

           -k, --kernel
               Disable recording event rules in the Linux kernel domain.

           -l, --log4j
               Disable recording event rules in the Apache log4j 1.x domain.

           --log4j2
               Disable recording event rules in the Apache Log4j 2 domain.

           -p, --python
               Disable recording event rules in the Python domain.

           -u, --userspace
               Disable recording event rules in the user space tracing
               domain.

       Recording target
           -c CHANNEL, --channel=CHANNEL
               Disable recording event rules attached to the channel named
               CHANNEL instead of channel0.

           -s SESSION, --session=SESSION
               Disable recording event rules in the recording session named
               SESSION instead of the current recording session.

       Instrumentation point type condition
           At most one of:

           --function
               Only disable recording event rules which match Linux kretprobe
               events.

               Only available with the --kernel option.

           --probe
               Only disable recording event rules which match Linux kprobe
               events.

               Only available with the --kernel option.

           --syscall
               Only disable recording event rules which match Linux system
               call events.

               Only available with the --kernel option.

           --tracepoint
               Only disable recording event rules which match:

               With the --kernel or --userspace option
                   LTTng tracepoint events.

               With the --jul, --log4j, --log4j2, or --python option
                   Logging events.

       Event name condition
           -a, --all-events
               Disable recording event rules regardless of their event name
               condition.

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

           Example 1. Disable all Linux kernel tracepoint recording event
           rules in the default channel of the current recording session.

               See the --all-events option.

                   $ lttng disable-event --kernel --tracepoint --all-events

           Example 2. Disable specific Apache log4j 1.x recording event rules
           in the default channel of a specific recording session.

               See the --session option.

                   $ lttng disable-event --session=my-session --log4j \
                                         MySingleton,MyProxy,MyFacade

           Example 3. Disable all user space recording event rules in a
           specific channel of the current recording session.

               See the --channel option.

                   $ lttng disable-event --channel=my-channel --userspace \
                                         --all-events

           Example 4. Disable specific Linux kernel system call recording
           event rules in the default channel of the current recording
           session.

                   $ lttng disable-event --kernel --syscall pipe2,eventfd

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

           lttng(1), lttng-enable-event(1), lttng-list(1), lttng-concepts(7)

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

    LTTng 2.15.1                   1 April 2025         LTTNG-DISABLE-EVEN(1)

------------------------------------------------------------------------

Pages that refer to this page: [lttng(1)](../man1/lttng.1.html),  [lttng-enable-event(1)](../man1/lttng-enable-event.1.html),  [lttng-concepts(7)](../man7/lttng-concepts.7.html)

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
