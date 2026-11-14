---
{"title": "lttng-list(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lttng-list.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-list(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-LIST(1)                  LTTng Manual                 LTTNG-LIST(1)

## [](#NAME)NAME

           lttng-list - List LTTng recording sessions and instrumentation
           points

## [](#SYNOPSIS)SYNOPSIS

           List the recording sessions:

           lttng [GENERAL OPTIONS] list

           List the tracing domains of a recording session:

           lttng [GENERAL OPTIONS] list --domain SESSION

           List the channels and recording event rules of a recording
           session:

           lttng [GENERAL OPTIONS] list [--channel=CHANNEL] SESSION
                 [--kernel] [--userspace] [--jul] [--log4j] [--log4j2] [--python]
                 [--style=(compact | breathe)] [--no-truncate]
                 [--mem-usage=(total | compact | full)]

           List the available LTTng tracepoints, Linux system calls, and/or
           Java/Python loggers:

           lttng [GENERAL OPTIONS] list
                 [--kernel [--syscall]] [--userspace [--fields]]
                 [--jul] [--log4j] [--log4j2] [--python]

## [](#DESCRIPTION)DESCRIPTION

           The lttng list command lists:

           Without arguments
               The recording sessions of your Unix user, or of all users if
               your Unix user is root, within the connected session daemon.

               See the “Session daemon connection” section of lttng(1) to
               learn how a user application connects to a session daemon.

               The command shows recording session properties such as their
               output directories/URLs and whether or not they’re active.

               The name of the current recording session is underlined.

           With the SESSION argument

               With the --domain option
                   The tracing domains of the recording session named
                   SESSION.

               Without the --domain option

                   With the --channel=CHANNEL option
                       The recording event rules of the channel(s) CHANNEL of
                       the recording session named SESSION.

                   Without the --channel option
                       The channels of the recording session named SESSION
                       and their recording event rules.

                   By default, the command shows the total memory usage of
                   each channel. Control the memory usage display mode with
                   the --mem-usage option.

                   Use the dedicated tracing domain options (--kernel,
                   --userspace, --jul, --log4j, --log4j2, and --python) to
                   only show specific channels.

           Without the SESSION argument and with at least one dedicated
           tracing domain option

               With the --kernel option

                   Without the --syscall option
                       The available LTTng kernel tracepoints.

                   With the --syscall option
                       The available instrumented Linux system calls.

               With the --userspace option
                   The available LTTng user space tracepoints.

                   Also list the available instrumentation point fields with
                   the --fields option.

               With the --jul, --log4j, --log4j2, and/or --python options
                   The available java.util.logging, Apache log4j 1.x, Apache
                   Log4j 2 and/or Python logger names.

           See lttng-concepts(7) to learn more about recording sessions,
           tracing domains, channels, recording event rules, and
           instrumentation points.

           By default, the command adds empty lines between blocks of related
           information. Remove those empty lines with the --style=compact
           option.

           This command shows colored text when the terminal supports it.
           Override the terminal coloring behaviour with the LTTNG_TERM_COLOR
           and NO_COLOR environment variables.

           See the “EXAMPLES” section below for usage examples.

           List the channels and recording event rules of the current
           recording session (see lttng-concepts(7) to learn more) with the
           lttng-status(1) command.

       Visual language
           The lttng list command uses a structured visual language designed
           to make complex tracing configurations easier to read and scan. It
           combines terminal colors, Unicode symbols, and indentation to
           express hierarchy, state, and metadata.

           Color semantics:
           ┌─────────┬─────────────────────────┐
           │ Color   │ Meaning                 │
           ├─────────┼─────────────────────────┤
           │         │                         │
           │ Green   │ Enabled, active, or     │
           │         │ valid items.            │
           ├─────────┼─────────────────────────┤
           │         │                         │
           │ Red     │ Disabled, inactive, or  │
           │         │ invalid items.          │
           ├─────────┼─────────────────────────┤
           │         │                         │
           │ Cyan    │ Important object nodes: │
           │         │ recording sessions,     │
           │         │ tracing domains,        │
           │         │ channels, and event     │
           │         │ rules.                  │
           │         │                         │
           │         │ Those nodes act as      │
           │         │ section headers.        │
           ├─────────┼─────────────────────────┤
           │         │                         │
           │ Yellow  │ Metadata such as counts │
           │         │ and timestamps.         │
           ├─────────┼─────────────────────────┤
           │         │                         │
           │ Magenta │ Warning information.    │
           └─────────┴─────────────────────────┘

           Symbolic conventions:
           ┌─────────┬──────────────────────────┐
           │ Symbol  │ Meaning                  │
           ├─────────┼──────────────────────────┤
           │         │                          │
           │ • and ◼ │ Active/inactive          │
           │         │ recording session.       │
           ├─────────┼──────────────────────────┤
           │         │                          │
           │ ✓ and × │ Enabled/disabled channel │
           │         │ or event rule.           │
           ├─────────┼──────────────────────────┤
           │         │                          │
           │ 🞂       │ Attribute or attribute   │
           │         │ group.                   │
           ├─────────┼──────────────────────────┤
           │         │                          │
           │ ┆       │ Vertical continuation.   │
           └─────────┴──────────────────────────┘

## [](#OPTIONS)OPTIONS

           See lttng(1) for GENERAL OPTIONS.

       Tracing domain
           -j, --jul

               Without the SESSION argument
                   List the java.util.logging logger names.

               With the SESSION argument
                   Only list the java.util.logging recording event rules.

           -k, --kernel

               Without the SESSION argument
                   List the LTTng kernel instrumentation points.

               With the SESSION argument
                   Only list the Linux kernel channels and their recording
                   event rules.

           -l, --log4j

               Without the SESSION argument
                   List the Apache log4j 1.x logger names.

               With the SESSION argument
                   Only list the Apache log4j 1.x recording event rules.

           --log4j2

               Without the SESSION argument
                   List the Apache Log4j 2 logger names.

               With the SESSION argument
                   Only list the Apache Log4j 2 recording event rules.

           -p, --python

               Without the SESSION argument
                   List the Python logger names.

               With the SESSION argument
                   Only list the Python recording event rules.

           -u, --userspace

               Without the SESSION argument
                   List the LTTng user space tracepoints.

               With the SESSION argument
                   Only list the user space channels and their recording
                   event rules.

       Filtering
           -c CHANNEL, --channel=CHANNEL
               Only list the properties and recording event rules of the
               channel(s) named CHANNEL.

               Only available with the SESSION argument.

           -d, --domain
               Show the tracing domains of the recording session named
               SESSION.

           -f, --fields
               When listing user space tracepoints, also show their fields if
               they’re available.

           --syscall
               When listing LTTng kernel instrumentation points, only list
               Linux system calls.

       Display
           --mem-usage=MODE
               Set the channel memory usage display mode to MODE.

               MODE is one of:

               total (default)
                   Show the total memory usage of the channel.

               compact
                   Show the memory usage for each Unix user or process,
                   depending on the buffer ownership model of the channel
                   (see the --buffer-ownership option of
                   lttng-enable-channel(1)).

               full
                   Show the memory usage for each CPU (if available).

               Only available with the SESSION argument.

           --no-truncate
               Do NOT truncate long output lines.

               By default, the command truncates lines, adding an ellipsis,
               to fit the current terminal width.

           --style=STYLE
               Set the command output style to STYLE.

               STYLE is one of:

               breathe (default)
                   Add empty lines to make blocks of related information
                   stand out.

               compact
                   Make the the output compact.

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

           Example 1. List the recording sessions.

                   $ lttng list

           Example 2. Show the details of a specific recording session.

                   $ lttng list my-session

           Example 3. List the available Linux kernel system call
           instrumentation points.

                   $ lttng list --kernel --syscall

           Example 4. List the available user space tracepoints with their
           fields.

               See the --fields option.

                   $ lttng list --userspace --fields

           Example 5. List the tracing domains of a specific recording
           session having at least one channel.

               See the --domain option.

                   $ lttng list --domain my-session

           Example 6. Show the details of a specific channel, including its
           current data stream infos, in a specific recording session.

               See the --channel option.

                   $ lttng list my-session --channel=channel0 --stream-info-details

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

           lttng(1), lttng-concepts(7)

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

    LTTng 2.15.1                 2 December 2025                LTTNG-LIST(1)

------------------------------------------------------------------------

Pages that refer to this page: [lttng(1)](../man1/lttng.1.html),  [lttng-add-context(1)](../man1/lttng-add-context.1.html),  [lttng-add-trigger(1)](../man1/lttng-add-trigger.1.html),  [lttng-clear(1)](../man1/lttng-clear.1.html),  [lttng-create(1)](../man1/lttng-create.1.html),  [lttng-destroy(1)](../man1/lttng-destroy.1.html),  [lttng-disable-channel(1)](../man1/lttng-disable-channel.1.html),  [lttng-disable-event(1)](../man1/lttng-disable-event.1.html),  [lttng-disable-rotation(1)](../man1/lttng-disable-rotation.1.html),  [lttng-enable-channel(1)](../man1/lttng-enable-channel.1.html),  [lttng-enable-event(1)](../man1/lttng-enable-event.1.html),  [lttng-enable-rotation(1)](../man1/lttng-enable-rotation.1.html),  [lttng-help(1)](../man1/lttng-help.1.html),  [lttng-list(1)](../man1/lttng-list.1.html),  [lttng-list-triggers(1)](../man1/lttng-list-triggers.1.html),  [lttng-load(1)](../man1/lttng-load.1.html),  [lttng-metadata(1)](../man1/lttng-metadata.1.html),  [lttng-reclaim-memory(1)](../man1/lttng-reclaim-memory.1.html),  [lttng-regenerate(1)](../man1/lttng-regenerate.1.html),  [lttng-remove-trigger(1)](../man1/lttng-remove-trigger.1.html),  [lttng-rotate(1)](../man1/lttng-rotate.1.html),  [lttng-save(1)](../man1/lttng-save.1.html),  [lttng-set-session(1)](../man1/lttng-set-session.1.html),  [lttng-snapshot(1)](../man1/lttng-snapshot.1.html),  [lttng-start(1)](../man1/lttng-start.1.html),  [lttng-status(1)](../man1/lttng-status.1.html),  [lttng-stop(1)](../man1/lttng-stop.1.html),  [lttng-track(1)](../man1/lttng-track.1.html),  [lttng-untrack(1)](../man1/lttng-untrack.1.html),  [lttng-version(1)](../man1/lttng-version.1.html),  [lttng-view(1)](../man1/lttng-view.1.html),  [lttng-ust(3)](../man3/lttng-ust.3.html),  [lttng-concepts(7)](../man7/lttng-concepts.7.html),  [lttng-event-rule(7)](../man7/lttng-event-rule.7.html)

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
