---
{"title": "lttng-status(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lttng-status.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-status(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-STATUS(1)                LTTng Manual               LTTNG-STATUS(1)

## [](#NAME)NAME

           lttng-status - Show the status of the current LTTng recording
           session

## [](#SYNOPSIS)SYNOPSIS

           lttng [GENERAL OPTIONS] status [--channel=CHANNEL]
                 [--kernel] [--userspace] [--jul] [--log4j] [--log4j2] [--python]
                 [--style=(compact | breathe)] [--no-truncate]
                 [--mem-usage=(total | compact | full)]

## [](#DESCRIPTION)DESCRIPTION

           The lttng status command shows the status of the current recording
           session (see lttng-concepts(7) to learn more about the current
           recording session).

           This command is equivalent to:

               lttng [GENERAL OPTIONS] list CURSESSION [--channel=CHANNEL]
                     [--kernel] [--userspace]
                     [--jul] [--log4j] [--log4j2] [--python]
                     [--style=(compact | breathe)] [--no-truncate]
                     [--mem-usage=(total | compact | full)]

           where CURSESSION is the name of the current recording session.

           This command effectively forwards all its options to the
           lttng-list(1) command.

## [](#OPTIONS)OPTIONS

           See lttng(1) for GENERAL OPTIONS.

           -c CHANNEL, --channel=CHANNEL
               Only list the properties and recording event rules of the
               channel(s) named CHANNEL.

           -j, --jul
               Only list the java.util.logging recording event rules.

           -k, --kernel
               Only list the Linux kernel channels and their recording event
               rules.

           -l, --log4j
               Only list the Apache log4j 1.x recording event rules.

           --log4j2
               Only list the Apache Log4j 2 recording event rules.

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
                   Show the memory usage for each each CPU (if available).

           --no-truncate
               Do NOT truncate long output lines.

               By default, the command truncates lines, adding an ellipsis,
               to fit the current terminal width.

           -p, --python
               Only list the Python recording event rules.

           --style=STYLE
               Set the command output style to STYLE.

               STYLE is one of:

               breathe (default)
                   Add empty lines to make blocks of related information
                   stand out.

               compact
                   Make the the output compact.

           -u, --userspace
               Only list the user space channels and their recording event
               rules.

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

           lttng(1), lttng-create(1), lttng-list(1), lttng-set-session(1),
           lttng-concepts(7)

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

    LTTng 2.15.1                 27 October 2025              LTTNG-STATUS(1)

------------------------------------------------------------------------

Pages that refer to this page: [lttng(1)](../man1/lttng.1.html),  [lttng-create(1)](../man1/lttng-create.1.html),  [lttng-enable-channel(1)](../man1/lttng-enable-channel.1.html),  [lttng-enable-event(1)](../man1/lttng-enable-event.1.html),  [lttng-list(1)](../man1/lttng-list.1.html),  [lttng-concepts(7)](../man7/lttng-concepts.7.html)

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
