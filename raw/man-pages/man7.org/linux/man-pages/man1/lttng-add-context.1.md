---
{"title": "lttng-add-context(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lttng-add-context.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-add-context(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-ADD-CONTEXT(1)           LTTng Manual          LTTNG-ADD-CONTEXT(1)

## [](#NAME)NAME

           lttng-add-context - Add context fields to be recorded by LTTng

## [](#SYNOPSIS)SYNOPSIS

           Add context fields to be recorded to the event records of one or
           more channels:

           lttng [GENERAL OPTIONS] add-context
                 (--kernel | --userspace | --jul | --log4j | --log4j2)
                 [--session=SESSION] [--channel=CHANNEL]
                 --type=TYPE [--type=TYPE]...

           List the available context field types:

           lttng [GENERAL OPTIONS] add-context --list

## [](#DESCRIPTION)DESCRIPTION

           The lttng add-context command can:

           Without the --list option
               Add one or more context fields to be recorded by LTTng to the
               event records of:

               With the --session=SESSION option
                   The recording session named SESSION.

               Without the --session option
                   The current recording session (see lttng-concepts(7) to
                   learn more about the current recording session).

               With the --channel=CHANNEL
                   The channel named CHANNEL.

               Without the --channel option
                   All the channels of the selected recording session.

           With the --list option
               List the available context field types.

           See lttng-concepts(7) to learn more about recording sessions and
           channels.

           Repeat the --type=TYPE option to add more than one context field
           to be recorded. TYPE is one of:

           •   A statically-known, or built-in context field name.

           •   A perf counter name:

               Per-CPU
                   Prefix: perf:cpu:

                   Only available with the --kernel option.

               Per-thread
                   Prefix: perf:thread:

                   Only available with the --userspace, --jul, --log4j, or
                   --log4j2 option.

               Add Performance Monitoring Unit (PMU) counter context fields
               by raw ID with the perf:cpu:raw:rN:NAME (--kernel option) or
               perf:thread:raw:rN:NAME (--userspace, --jul, --log4j, or
               --log4j2 option) types, with:

               N
                   A hexadecimal event descriptor which follows the
                   perf-record(1) format: a concatenation of the event number
                   and umask value which the manufacturer of the processor
                   provides.

                   The possible values for this part are processor-specific.

               NAME
                   Custom name to identify the counter.

           •   An LTTng application-specific context field name:

                   $app.PROVIDER:TYPE
               + PROVIDER:: Provider name.

               TYPE
                   Context type name.

               Only available with the --jul, --log4j, and --log4j2 options.

           Important

               Make sure to single-quote TYPE when you run the add-context
               command from a shell, as $ is a special character for variable
               substitution in most shells.

           Note

               As of LTTng 2.15.1, you may NOT add context fields to be
               recorded to the event records of a given channel once its
               recording session has been started (see lttng-start(1)) at
               least once.

           See the “EXAMPLES” section below for usage examples.

## [](#OPTIONS)OPTIONS

           See lttng(1) for GENERAL OPTIONS.

       Tracing domain
           One of:

           -j, --jul
               Add context fields to be recorded to the event records of one
               or more channels of the java.util.logging (JUL) tracing
               domain.

           -k, --kernel
               Add context fields to be recorded to the event records of one
               or more channels of the Linux kernel tracing domain.

           -l, --log4j
               Add context fields to be recorded to the event records of one
               or more channels of the Apache log4j 1.x tracing domain.

           --log4j2
               Add context fields to be recorded to the event records of one
               or more channels of the Apache Log4j 2 tracing domain.

           -u, --userspace
               Add context fields to be recorded to the event records of one
               or more channels of the user space tracing domain.

       Recording target
           -c CHANNEL, --channel=CHANNEL
               Add context fields to be recorded to the event records of a
               channel named CHANNEL instead of all the channels of the
               selected recording session.

           -s SESSION, --session=SESSION
               Add context fields to be recorded to the event records of one
               or more channels of the recording session named SESSION
               instead of the current recording session.

       Context field type
           --list
               List the available context field types.

               You may NOT use this option with the --channel, --session, or
               --type options.

           -t TYPE, --type=TYPE
               Add a context field having the type TYPE to be recorded.

               Repeat this option to add more than one context field.

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

           Example 1. List the available context field types.

               See the --list option.

                   $ lttng add-context --list

           Example 2. Add a single statically-known context field to be
           recorded to all the Linux kernel channels of the current recording
           session.

                   $ lttng add-context --kernel --type=pid

           Example 3. Add three statically-known context fields to be
           recorded to a specific user space channel of a specific recording
           session.

               See the --session and --channel options.

                   $ lttng add-context --userspace --session=my-session \
                                       --channel=my-channel \
                                       --type=vpid --type=procname --type=ip

           Example 4. Add a perf counter context field to be recorded to a
           specific Linux kernel channel of the current recording session.

               See the --channel option.

                   $ lttng add-context --kernel --channel=my-channel \
                                       --type=perf:cpu:cache-misses

           Example 5. Add an LTTng application-specific context field to be
           recorded to all the JUL channels of the current recording session.

                   $ lttng add-context --jul --type='$app.my_server:user_cnt'

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

           lttng(1), lttng-enable-channel(1), lttng-concepts(7)

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

    LTTng 2.15.1                   1 April 2025          LTTNG-ADD-CONTEXT(1)

------------------------------------------------------------------------

Pages that refer to this page: [lttng(1)](../man1/lttng.1.html),  [lttng-add-trigger(1)](../man1/lttng-add-trigger.1.html),  [lttng-enable-event(1)](../man1/lttng-enable-event.1.html),  [lttng-ust(3)](../man3/lttng-ust.3.html),  [babeltrace2-filter.lttng-utils.debug-info(7)](../man7/babeltrace2-filter.lttng-utils.debug-info.7.html),  [lttng-concepts(7)](../man7/lttng-concepts.7.html),  [lttng-event-rule(7)](../man7/lttng-event-rule.7.html)

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
