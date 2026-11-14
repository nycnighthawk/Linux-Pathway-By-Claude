---
{"title": "lttng-load(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lttng-load.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-load(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-LOAD(1)                  LTTng Manual                 LTTNG-LOAD(1)

## [](#NAME)NAME

           lttng-load - Load LTTng recording session configurations

## [](#SYNOPSIS)SYNOPSIS

           lttng [GENERAL OPTIONS] load [--force] [--input-path=PATH]
                 [--override-url=URL] [--all | SESSION [--override-name=NAME]]

## [](#DESCRIPTION)DESCRIPTION

           The lttng load command loads the configurations of one or more
           recording sessions from files.

           See lttng-concepts(7) to learn more about recording sessions.

           Use the load command in conjunction with the lttng-save(1) command
           to save and restore the complete configurations of recording
           sessions. A recording session configuration includes the enabled
           channels and recording event rules, the context fields to be
           recorded, the recording activity, and more.

           Once LTTng loads one or more recording session configurations,
           they appear exactly as they were saved from the user’s point of
           view.

           LTTng searches the following directories, non-recursively, in this
           order for recording session configuration files:

            1. $LTTNG_HOME/.lttng/sessions ($LTTNG_HOME defaults to $HOME)

            2. /usr/local/etc/lttng/sessions

           Override the input path with the --input-path=PATH option. With
           this option, LTTng does NOT search the default directories above.
           PATH can be the path of one of:

           A directory

               With the SESSION argument
                   LTTng searches for the recording session configuration
                   named SESSION in all the files of the directory PATH and
                   loads it if found.

               Without the SESSION argument
                   The --all option is implicit: LTTng loads all the
                   recording session configurations found in all the files in
                   the directory PATH.

           A file

               With the SESSION argument
                   LTTng searches for the recording session configuration
                   named SESSION in the file PATH and loads it if found.

               Without the SESSION argument
                   The --all option is implicit: LTTng loads all the
                   recording session configurations found in the file PATH.

           Override the output URL of the loaded recording session
           configurations with the --override-url option.

           With the SESSION argument, override the name of the loaded
           recording session configuration with the --override-name option.

           By default, the load command does NOT overwrite existing recording
           sessions: the command fails. Allow the load command to overwrite
           existing recording sessions with the --force option.

           See the “EXAMPLES” section below for usage examples.

## [](#OPTIONS)OPTIONS

           See lttng(1) for GENERAL OPTIONS.

           -a, --all
               Load all the recording session configurations (default).

           -f, --force
               Overwrite existing recording sessions when loading.

           -i PATH, --input-path=PATH
               Load recording session configurations from PATH, either a
               directory or a file, instead of loading them from the default
               search directories.

           --override-name=NAME
               Override the name of the loaded recording session
               configuration, SESSION, with NAME.

           --override-url=URL
               Override the output URL of the loaded recording session
               configurations with URL.

               This is the equivalent of the --set-url option of
               lttng-create(1). The validity of the URL override depends on
               the type of recording session configurations to load. This
               option applies to all the loaded recording session
               configurations.

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

           Example 1. Load all the recording session configurations from the
           default search directories.

                   $ lttng load

           Example 2. Load all the recording session configurations from a
           specific directory.

               See the --input-path option.

                   $ lttng load --input-path=/path/to/sessions

           Example 3. Load a specific recording session configuration from
           the default search directories.

                   $ lttng load my-session

           Example 4. Allow LTTng to overwrite existing recording sessions
           when loading.

               See the --force option.

                   $ lttng load --force

           Example 5. Load a specific recording session configuration from a
           specific file, overriding its name.

               See the --input-path and --override-name options.

                   $ lttng load my-session --input-path=/path/to/sessions.lttng \
                                --override-name=new-test

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

           lttng(1), lttng-save(1), lttng-concepts(7)

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

    LTTng 2.15.1                   14 June 2021                 LTTNG-LOAD(1)

------------------------------------------------------------------------

Pages that refer to this page: [lttng(1)](../man1/lttng.1.html),  [lttng-add-context(1)](../man1/lttng-add-context.1.html),  [lttng-add-trigger(1)](../man1/lttng-add-trigger.1.html),  [lttng-clear(1)](../man1/lttng-clear.1.html),  [lttng-create(1)](../man1/lttng-create.1.html),  [lttng-destroy(1)](../man1/lttng-destroy.1.html),  [lttng-disable-channel(1)](../man1/lttng-disable-channel.1.html),  [lttng-disable-event(1)](../man1/lttng-disable-event.1.html),  [lttng-disable-rotation(1)](../man1/lttng-disable-rotation.1.html),  [lttng-enable-channel(1)](../man1/lttng-enable-channel.1.html),  [lttng-enable-event(1)](../man1/lttng-enable-event.1.html),  [lttng-enable-rotation(1)](../man1/lttng-enable-rotation.1.html),  [lttng-help(1)](../man1/lttng-help.1.html),  [lttng-list(1)](../man1/lttng-list.1.html),  [lttng-list-triggers(1)](../man1/lttng-list-triggers.1.html),  [lttng-load(1)](../man1/lttng-load.1.html),  [lttng-metadata(1)](../man1/lttng-metadata.1.html),  [lttng-reclaim-memory(1)](../man1/lttng-reclaim-memory.1.html),  [lttng-regenerate(1)](../man1/lttng-regenerate.1.html),  [lttng-remove-trigger(1)](../man1/lttng-remove-trigger.1.html),  [lttng-rotate(1)](../man1/lttng-rotate.1.html),  [lttng-save(1)](../man1/lttng-save.1.html),  [lttng-set-session(1)](../man1/lttng-set-session.1.html),  [lttng-snapshot(1)](../man1/lttng-snapshot.1.html),  [lttng-start(1)](../man1/lttng-start.1.html),  [lttng-status(1)](../man1/lttng-status.1.html),  [lttng-stop(1)](../man1/lttng-stop.1.html),  [lttng-track(1)](../man1/lttng-track.1.html),  [lttng-untrack(1)](../man1/lttng-untrack.1.html),  [lttng-version(1)](../man1/lttng-version.1.html),  [lttng-view(1)](../man1/lttng-view.1.html),  [lttng-concepts(7)](../man7/lttng-concepts.7.html)

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
