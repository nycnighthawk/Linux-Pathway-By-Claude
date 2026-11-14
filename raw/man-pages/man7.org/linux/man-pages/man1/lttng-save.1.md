---
{"title": "lttng-save(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lttng-save.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-save(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-SAVE(1)                  LTTng Manual                 LTTNG-SAVE(1)

## [](#NAME)NAME

           lttng-save - Save LTTng recording session configurations

## [](#SYNOPSIS)SYNOPSIS

           lttng [GENERAL OPTIONS] save [--force] [--output-path=DIR]
                 [--all | SESSION]

## [](#DESCRIPTION)DESCRIPTION

           The lttng save command saves to files the configurations of:

           With the SESSION argument
               The recording session named SESSION.

           Without the SESSION argument
               Implicit --all option: all the recording sessions of the
               connected session daemon for your Unix user, or for all users
               if your Unix user is root, as listed in the output of lttng
               list (see lttng-list(1)).

               See the “Session daemon connection” section of lttng(1) to
               learn how a user application connects to a session daemon.

           See lttng-concepts(7) to learn more about recording sessions.

           Use the save command in conjunction with the lttng-load(1) command
           to save and restore the complete configurations of recording
           sessions.

           The save command does NOT save tracing data, only the recording
           session parameters, including the channel and recording event rule
           configurations.

           The default output directory path is $LTTNG_HOME/.lttng/sessions
           ($LTTNG_HOME defaults to $HOME). Override the default output
           directory path with the --output-path option. Each recording
           session configuration file is named SNAME.lttng, where SNAME is
           the original recording session name.

           By default, the save command does NOT overwrite existing recording
           session configuration files: the command fails. Allow the save
           command to overwrite existing recording session configuration
           files with the --force option.

           See the “EXAMPLES” section below for usage examples.

## [](#OPTIONS)OPTIONS

           See lttng(1) for GENERAL OPTIONS.

           -a, --all
               Save all the recording session configurations of your Unix
               user, or of all users if your Unix user is root, as listed in
               the output of lttng-list(1), instead of the current recording
               session or the recording session named SESSION.

           -f, --force
               Overwrite existing recording session configuration files when
               saving.

           -o DIR, --output-path=DIR
               Save recording session configuration files to the directory
               DIR instead of $LTTNG_HOME/.lttng/sessions ($LTTNG_HOME
               defaults to $HOME).

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

           Example 1. Save all the recording session configurations to the
           default output directory.

                   $ lttng save

           Example 2. Save a specific recording session configuration to a
           specific output directory.

               See the --output-path option.

                   $ lttng save my-session --output-path=/path/to/sessions

           Example 3. Allow LTTng to overwrite existing recording session
           configuration files when saving.

               See the --force option.

                   $ lttng save --force

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

           lttng(1), lttng-load(1), lttng-concepts(7)

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

    LTTng 2.15.1                   14 June 2021                 LTTNG-SAVE(1)

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
