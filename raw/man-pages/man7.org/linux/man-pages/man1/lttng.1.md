---
{"title": "lttng(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lttng.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [COMMANDS](#COMMANDS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG(1)                       LTTng Manual                      LTTNG(1)

## [](#NAME)NAME

           lttng - Control LTTng tracing

## [](#SYNOPSIS)SYNOPSIS

           lttng [--group=GROUP] [--mi=xml] [--no-sessiond | --sessiond-path=PATH]
                 [--relayd-path=PATH] [--quiet | -verbose...]
                 COMMAND [COMMAND OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           The Linux Trace Toolkit: next generation <https://lttng.org/> is
           an open-source software package used for correlated tracing of the
           Linux kernel, user applications, and user libraries.

           LTTng consists of Linux kernel modules (for Linux kernel tracing)
           and dynamically loaded libraries (for user application and library
           tracing).

           The lttng command-line tool, as well as any user application
           linked with the LTTng control library (liblttng-ctl), sends
           commands to a listening LTTng session daemon (lttng-sessiond(8)).
           A session daemon:

           •   Manages recording sessions (see lttng-concepts(7) to learn
               more about recording sessions).

           •   Controls the various components (like tracers and consumer
               daemons) of LTTng.

           •   Sends asynchronous notifications to user applications.

           By default, the lttng-create(1) command automatically spawns:

           •   A session daemon for your Unix user if none is currently
               running.

               Override the path of the session daemon binary to spawn with
               the --sessiond-path option.

               Avoid automatically spawning a session daemon with the --no-
               sessiond option.

           •   A relay daemon (see lttng-relayd(8)) if all the following
               statements are true:

               •   You specify the --live option.

               •   You don’t specify any of the --set-url, --ctrl-url, or
                   --data-url options.

               •   No relay daemon is currently listening for TCP connections
                   on 127.0.0.1:5344 (default LTTng live reader connection
                   address and port).

               Override the path of the relay daemon binary to spawn with the
               --relayd-path option.

           Note

               The LTTng project recommends that you start the session daemon
               at boot time for stable and long-term tracing.

           See lttng-concepts(7) to learn more about the foundational
           concepts of LTTng.

           The lttng tool offers a subcommand-based command-line interface.
           The “COMMANDS” section below lists the available commands.

       Session daemon connection
           For most of its commands, the lttng tool needs to connect to a
           listening LTTng session daemon (lttng-sessiond(8)) to control
           LTTng tracing.

           Each Unix user may have its own independent running session
           daemon. However, the lttng tool must connect to the session daemon
           of the root user (the root session daemon) to control Linux kernel
           tracing.

           How the lttng tool chooses which session daemon to connect to is
           as follows:

           If your Unix user is root
               Connect to the root session daemon.

           If your Unix user is not root

               If your Unix user is part of the Unix tracing group
                   Try to connect to the root session daemon.

                   If the root session daemon isn’t running, connect to the
                   session daemon of your Unix user.

               If your Unix user is not part of the tracing group
                   Connect to the session daemon of your Unix user.

           The name of the Unix tracing group is one of:

           With the --group=GROUP option of the root session daemon (‐
           lttng-sessiond(8))
               GROUP

               In that case, you must use the --group=GROUP option, with the
               same GROUP argument, of the lttng tool.

           Without the --group option of the root session daemon
               tracing

           LTTng-instrumented user applications automatically register to
           both the root and user session daemons. This makes it possible for
           both session daemons to list the available instrumented
           applications and their instrumentation points (see lttng-list(1)).

## [](#OPTIONS)OPTIONS

           -g GROUP, --group=GROUP
               Set the name of the Unix tracing group to GROUP instead of
               tracing.

               You must use this option to be able to connect to a root
               session daemon (lttng-sessiond(8)) which was started with its
               own --group=GROUP option.

           -m xml, --mi=xml
               Print the command result using a stable XML machine interface
               (MI) output instead of the default, unstable human-readable
               output.

               With this mode, lttng prints the resulting XML document to the
               standard output, while it prints any error/warning to the
               standard error with an unstable, human-readable format.

               If any error occurs during the execution of lttng, the command
               exits with a status different than 0, and lttng does NOT
               guarantee the syntax and data validity of its MI output.

               An XML schema definition (XSD) file used for validation of the
               MI output is available: see the src/common/mi_lttng.xsd file
               in the LTTng-tools source tree.

           -n, --no-sessiond
               Do not automatically spawn a session daemon for your Unix user
               when running the lttng-create(1) command.

               You may NOT use this option with the --sessiond-path option.

           -q, --quiet
               Suppress all messages, including warnings and errors.

               You may NOT use this option with the --verbose option.

           --sessiond-path=PATH
               Set the absolute path of the session daemon binary to spawn
               from the lttng-create(1) command to PATH.

               You may NOT use this option with the --no-sessiond option.

           --relayd-path=PATH
               Set the absolute path of the relay daemon binary to spawn from
               the lttng-create(1) command to PATH.

           -v, --verbose
               Increase verbosity.

               Specify this option up to three times to get more levels of
               verbosity.

               You may NOT use this option with the --quiet option.

       Program information
           -h, --help
               Show help.

               This option attempts to launch /usr/bin/man to view this
               manual page. Override the manual pager path with the
               LTTNG_MAN_BIN_PATH environment variable.

           --list-options
               List available command options and quit.

           --list-commands
               List available commands and quit.

           -V, --version
               Show version and quit.

## [](#COMMANDS)COMMANDS

           The following commands also have their own --help option.

       Recording session
           ┌───────────────────────────┬──────────────────────────┐
           │ Command                   │ Description              │
           ├───────────────────────────┼──────────────────────────┤
           │                           │                          │
           │ lttng-create(1)           │ Create a recording       │
           │                           │ session.                 │
           ├───────────────────────────┼──────────────────────────┤
           │                           │                          │
           │ lttng-destroy(1)          │ Destroy recording        │
           │                           │ sessions.                │
           ├───────────────────────────┼──────────────────────────┤
           │                           │                          │
           │ lttng-disable-rotation(1) │ Unset a recording        │
           │                           │ session rotation         │
           │                           │ schedule.                │
           ├───────────────────────────┼──────────────────────────┤
           │                           │                          │
           │ lttng-enable-rotation(1)  │ Set a recording session  │
           │                           │ rotation schedule.       │
           ├───────────────────────────┼──────────────────────────┤
           │                           │                          │
           │ lttng-load(1)             │ Load recording session   │
           │                           │ configurations.          │
           ├───────────────────────────┼──────────────────────────┤
           │                           │                          │
           │ lttng-regenerate(1)       │ Regenerate specific      │
           │                           │ recording session data.  │
           ├───────────────────────────┼──────────────────────────┤
           │                           │                          │
           │ lttng-rotate(1)           │ Archive the current      │
           │                           │ trace chunk of a         │
           │                           │ recording session.       │
           ├───────────────────────────┼──────────────────────────┤
           │                           │                          │
           │ lttng-save(1)             │ Save recording session   │
           │                           │ configurations.          │
           ├───────────────────────────┼──────────────────────────┤
           │                           │                          │
           │ lttng-set-session(1)      │ Set the current          │
           │                           │ recording session.       │
           ├───────────────────────────┼──────────────────────────┤
           │                           │                          │
           │ lttng-snapshot(1)         │ Take a recording session │
           │                           │ snapshot.                │
           ├───────────────────────────┼──────────────────────────┤
           │                           │                          │
           │ lttng-start(1)            │ Start recording          │
           │                           │ sessions.                │
           ├───────────────────────────┼──────────────────────────┤
           │                           │                          │
           │ lttng-status(1)           │ Show the status of the   │
           │                           │ current recording        │
           │                           │ session.                 │
           ├───────────────────────────┼──────────────────────────┤
           │                           │                          │
           │ lttng-stop(1)             │ Stop recording sessions. │
           └───────────────────────────┴──────────────────────────┘

       Channel
           ┌──────────────────────────┬──────────────────────────┐
           │ Command                  │ Description              │
           ├──────────────────────────┼──────────────────────────┤
           │                          │                          │
           │ lttng-add-context(1)     │ Add context fields to be │
           │                          │ recorded.                │
           ├──────────────────────────┼──────────────────────────┤
           │                          │                          │
           │ lttng-disable-channel(1) │ Disable channels.        │
           ├──────────────────────────┼──────────────────────────┤
           │                          │                          │
           │ lttng-enable-channel(1)  │ Create or enable a       │
           │                          │ channel.                 │
           ├──────────────────────────┼──────────────────────────┤
           │                          │                          │
           │ lttng-reclaim-memory(1)  │ Reclaim channel memory.  │
           └──────────────────────────┴──────────────────────────┘

       Recording event rule
           ┌────────────────────────┬─────────────────────────┐
           │ Command                │ Description             │
           ├────────────────────────┼─────────────────────────┤
           │                        │                         │
           │ lttng-disable-event(1) │ Disable recording event │
           │                        │ rules.                  │
           ├────────────────────────┼─────────────────────────┤
           │                        │                         │
           │ lttng-enable-event(1)  │ Create or enable        │
           │                        │ recording event rules.  │
           └────────────────────────┴─────────────────────────┘

       Information
           ┌───────────────┬─────────────────────────┐
           │ Command       │ Description             │
           ├───────────────┼─────────────────────────┤
           │               │                         │
           │ lttng-list(1) │ List recording sessions │
           │               │ and instrumentation     │
           │               │ points.                 │
           └───────────────┴─────────────────────────┘

       Resource tracking
           ┌──────────────────┬──────────────────────────┐
           │ Command          │ Description              │
           ├──────────────────┼──────────────────────────┤
           │                  │                          │
           │ lttng-track(1)   │ Allow specific processes │
           │                  │ to record events.        │
           ├──────────────────┼──────────────────────────┤
           │                  │                          │
           │ lttng-untrack(1) │ Disallow specific        │
           │                  │ processes to record      │
           │                  │ events.                  │
           └──────────────────┴──────────────────────────┘

       Trigger
           ┌─────────────────────────┬───────────────────┐
           │ Command                 │ Description       │
           ├─────────────────────────┼───────────────────┤
           │                         │                   │
           │ lttng-add-trigger(1)    │ Add a trigger.    │
           ├─────────────────────────┼───────────────────┤
           │                         │                   │
           │ lttng-list-triggers(1)  │ List triggers.    │
           ├─────────────────────────┼───────────────────┤
           │                         │                   │
           │ lttng-remove-trigger(1) │ Remove a trigger. │
           └─────────────────────────┴───────────────────┘

       Miscellaneous
           ┌──────────────────┬──────────────────────────┐
           │ Command          │ Description              │
           ├──────────────────┼──────────────────────────┤
           │                  │                          │
           │ lttng-help(1)    │ Show the help of a       │
           │                  │ command.                 │
           ├──────────────────┼──────────────────────────┤
           │                  │                          │
           │ lttng-version(1) │ Show LTTng-tools version │
           │                  │ information.             │
           ├──────────────────┼──────────────────────────┤
           │                  │                          │
           │ lttng-view(1)    │ Launch a trace reader.   │
           └──────────────────┴──────────────────────────┘

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

           lttng-concepts(7) lttng-relayd(8), lttng-sessiond(8)

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

    LTTng 2.15.1                 4 December 2025                     LTTNG(1)

------------------------------------------------------------------------

Pages that refer to this page: [lttng(1)](../man1/lttng.1.html),  [lttng-add-context(1)](../man1/lttng-add-context.1.html),  [lttng-add-trigger(1)](../man1/lttng-add-trigger.1.html),  [lttng-clear(1)](../man1/lttng-clear.1.html),  [lttng-crash(1)](../man1/lttng-crash.1.html),  [lttng-create(1)](../man1/lttng-create.1.html),  [lttng-destroy(1)](../man1/lttng-destroy.1.html),  [lttng-disable-channel(1)](../man1/lttng-disable-channel.1.html),  [lttng-disable-event(1)](../man1/lttng-disable-event.1.html),  [lttng-disable-rotation(1)](../man1/lttng-disable-rotation.1.html),  [lttng-enable-channel(1)](../man1/lttng-enable-channel.1.html),  [lttng-enable-event(1)](../man1/lttng-enable-event.1.html),  [lttng-enable-rotation(1)](../man1/lttng-enable-rotation.1.html),  [lttng-help(1)](../man1/lttng-help.1.html),  [lttng-list(1)](../man1/lttng-list.1.html),  [lttng-list-triggers(1)](../man1/lttng-list-triggers.1.html),  [lttng-load(1)](../man1/lttng-load.1.html),  [lttng-metadata(1)](../man1/lttng-metadata.1.html),  [lttng-reclaim-memory(1)](../man1/lttng-reclaim-memory.1.html),  [lttng-regenerate(1)](../man1/lttng-regenerate.1.html),  [lttng-remove-trigger(1)](../man1/lttng-remove-trigger.1.html),  [lttng-rotate(1)](../man1/lttng-rotate.1.html),  [lttng-save(1)](../man1/lttng-save.1.html),  [lttng-set-session(1)](../man1/lttng-set-session.1.html),  [lttng-snapshot(1)](../man1/lttng-snapshot.1.html),  [lttng-start(1)](../man1/lttng-start.1.html),  [lttng-status(1)](../man1/lttng-status.1.html),  [lttng-stop(1)](../man1/lttng-stop.1.html),  [lttng-track(1)](../man1/lttng-track.1.html),  [lttng-untrack(1)](../man1/lttng-untrack.1.html),  [lttng-version(1)](../man1/lttng-version.1.html),  [lttng-view(1)](../man1/lttng-view.1.html),  [lttng-health-check(3)](../man3/lttng-health-check.3.html),  [lttng-ust(3)](../man3/lttng-ust.3.html),  [lttng-ust-cyg-profile(3)](../man3/lttng-ust-cyg-profile.3.html),  [lttng-ust-dl(3)](../man3/lttng-ust-dl.3.html),  [lttng_ust_tracef(3)](../man3/lttng_ust_tracef.3.html),  [lttng_ust_tracelog(3)](../man3/lttng_ust_tracelog.3.html),  [babeltrace2-filter.lttng-utils.debug-info(7)](../man7/babeltrace2-filter.lttng-utils.debug-info.7.html),  [lttng-concepts(7)](../man7/lttng-concepts.7.html),  [lttng-event-rule(7)](../man7/lttng-event-rule.7.html),  [lttng-relayd(8)](../man8/lttng-relayd.8.html),  [lttng-sessiond(8)](../man8/lttng-sessiond.8.html)

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
