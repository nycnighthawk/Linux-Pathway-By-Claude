---
{"title": "lttng-reclaim-memory(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lttng-reclaim-memory.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-reclaim-memory(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-RECLAIM-MEMO(1)          LTTng Manual         LTTNG-RECLAIM-MEMO(1)

## [](#NAME)NAME

           lttng-reclaim-memory - Reclaim channel memory immediately

## [](#SYNOPSIS)SYNOPSIS

           lttng [GENERAL OPTIONS] reclaim-memory --userspace
                 [--no-wait] [--older-than=AGEUS]
                 [--session=SESSION] (--all | CHANNEL...)

## [](#DESCRIPTION)DESCRIPTION

           The lttng reclaim-memory command immediately reclaims memory for
           the sub-buffers of:

           With the --all option
               All the user space channels of the targeted session.

           With one or more CHANNEL arguments
               Each named user space channel.

           The targeted session is either:

           With the --session=SESSION argument
               The recording session named SESSION.

           Otherwise
               The current recording session (see lttng-concepts(7) to learn
               more about the current recording session).

           See lttng-concepts(7) to learn more about channel memory reclaim.

           The channel memory reclaim operation behaviour depends on the
           configured event record loss mode of the channel:

           Discard mode
               Only reclaim sub-buffers that have been both delivered
               (completed and ready to be consumed) and consumed, since
               unconsumed data would be lost forever.

           Overwrite mode
               Reclaim any delivered sub-buffer, since old data will be
               overwritten anyway: no need to wait for consumption.

           Specify a sub-buffer age threshold with the --older-than=AGEUS
           option: only sub-buffers of which the age of the closing time is
           older than AGEUS µs are eligible for a memory reclaim. Moreover:

           If AGEUS > last stream activity age
               The sub-buffers of which the age, at the moment of closing
               them, is greater than AGEUS µs are eligible for a memory
               reclaim.

           If AGEUS < last stream activity age
               All the sub-buffers are eligible.

               The LTTng tracers flush for the targeted channel so that any
               open sub-buffer gets closed to become eligible.

           By default, the command waits for the memory reclaim operation to
           complete and displays the number of reclaimed sub-buffers. Use the
           --no-wait option to exit immediately without waiting for
           completion.

           See the “EXAMPLES” section below for usage examples.

## [](#OPTIONS)OPTIONS

           See lttng(1) for GENERAL OPTIONS.

       Program information
           -h, --help
               Show help.

               This option attempts to launch /usr/bin/man to view this
               manual page. Override the manual pager path with the
               LTTNG_MAN_BIN_PATH environment variable.

           --list-options
               List available command options and quit.

           -a, --all
               Reclaim memory for all the user space channels of the targeted
               session.

           --older-than=AGEUS
               Only reclaim sub-buffers of which the age (µs) of the closing
               time is greater than AGEUS µs instead of reclaiming the memory
               of all eligible sub-buffers.

               The ms (milliseconds), s (seconds), m (minutes), and h (hours)
               suffixes are supported.

           --no-wait
               Do NOT wait for the memory reclaim operation to complete
               before exiting.

           -s SESSION, --session=SESSION
               Reclaim memory for channels of the recording session named
               SESSION.

           -u, --userspace
               Reclaim memory of a user space channel.

               As of LTTng 2.15.1, this option is mandatory.

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

           Example 1. Reclaim memory for all eligible sub-buffers of user
           space channel my-channel (current recording session).

                   $ lttng reclaim-memory --userspace my-channel

           Example 2. Reclaim memory for sub-buffers older than 2 s of user
           space channels mon-canal and mein-Kanal (current recording
           session).

                   $ lttng reclaim-memory --userspace --older-than=2s \
                                          mon-canal mein-Kanal

           Example 3. Reclaim memory for all user space channels of the
           recording session named my-session without waiting for completion.

                   $ lttng reclaim-memory --userspace --session=my-session \
                                          --no-wait --all

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

           lttng(1), lttng-concepts(7), lttng-enable-channel(1)

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

    LTTng 2.15.1                24 September 2025       LTTNG-RECLAIM-MEMO(1)

------------------------------------------------------------------------

Pages that refer to this page: [lttng(1)](../man1/lttng.1.html),  [lttng-enable-channel(1)](../man1/lttng-enable-channel.1.html),  [lttng-concepts(7)](../man7/lttng-concepts.7.html)

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
