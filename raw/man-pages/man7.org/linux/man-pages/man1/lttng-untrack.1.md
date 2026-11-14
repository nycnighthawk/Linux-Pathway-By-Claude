---
{"title": "lttng-untrack(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lttng-untrack.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-untrack(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-UNTRACK(1)               LTTng Manual              LTTNG-UNTRACK(1)

## [](#NAME)NAME

           lttng-untrack - Disallow specific processes to record LTTng events

## [](#SYNOPSIS)SYNOPSIS

           Disallow specific processes to record Linux kernel events:

           lttng [GENERAL OPTIONS] untrack --kernel [--session=SESSION]
                 (--pid=PID[,PID]... | --vpid=VPID[,VPID]... |
                  --uid=UID[,UID]... | --vuid=VUSER[,VUSER]... |
                  --gid=GID[,GID]... | --vgid=VGROUP[,VGROUP]...)...

           lttng [GENERAL OPTIONS] untrack --kernel [--session=SESSION]
                 --all (--pid | --vpid | --uid | --vuid | --gid | --vgid)...

           Disallow specific processes to record user space events:

           lttng [GENERAL OPTIONS] untrack --userspace [--session=SESSION]
                 (--vpid=VPID[,VPID]... | --vuid=VUSER[,VUSER]... |
                  --vgid=VGROUP[,VGROUP]...)...

           lttng [GENERAL OPTIONS] untrack --userspace [--session=SESSION]
                 --all (--vpid | --vgid | --vuid)...

## [](#DESCRIPTION)DESCRIPTION

           The lttng untrack command disallows one or more processes to
           record LTTng events based on their attributes within:

           With the --session=SESSION option
               The recording session named SESSION.

           Without the --session option
               The current recording session (see lttng-concepts(7) to learn
               more about the current recording session).

           See lttng-concepts(7) to learn more about recording sessions and
           recording event rules.

           The untrack command removes values from inclusion sets of process
           attributes. See lttng-track(1) to learn more about inclusion sets.

           See the “EXAMPLES” section below for usage examples.

       Inclusion set example
           A common operation is to create a recording session (see
           lttng-create(1)), remove all the entries from the Linux kernel
           process ID inclusion set, start recording, and then manually add
           PIDs while the recording session is active.

           Assume the maximum system PID is 7 for this example.

            1. Command:

                   $ lttng create

               Initial inclusion set:

                   [0] [1] [2] [3] [4] [5] [6] [7]

            2. Command:

                   $ lttng untrack --kernel --all --pid

               Inclusion set:

                   [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]

            3. Commands:

                   $ lttng enable-event --kernel ...
                   $ lttng start
                   $ # ...
                   $ lttng track --kernel --pid=3,5

               Inclusion set:

                   [ ] [ ] [ ] [3] [ ] [5] [ ] [ ]

            4. Command:

                   $ lttng track --kernel --pid=2

               Inclusion set:

                   [ ] [ ] [2] [3] [ ] [5] [ ] [ ]

## [](#OPTIONS)OPTIONS

           See lttng(1) for GENERAL OPTIONS.

       Tracing domain
           One of:

           -k, --kernel
               Remove values from one or more Linux kernel inclusion sets.

           -u, --userspace
               Remove values from one or more user space inclusion sets.

       Recording target
           -s SESSION, --session=SESSION
               Remove values from one or more inclusion sets of the recording
               session named SESSION instead of the current recording
               session.

       Inclusion set selection
           -p [PID[,PID]...], --pid[=PID[,PID]...]
               For each PID argument, remove PID from the process ID
               inclusion set of the selected recording session and domain.

               PID is the process ID attribute of a process as seen from the
               root PID namespace (see pid_namespaces(7)).

               Only available with --kernel option.

           --vpid[=VPID[,VPID]...]
               For each VPID argument, remove VPID from the virtual process
               ID inclusion set of the selected recording session and domain.

               VPID is the virtual process ID attribute of a process as seen
               from the PID namespace of the process (see pid_namespaces(7)).

           --uid[=USER[,USER]...]
               For each USER argument, remove USER from the user ID inclusion
               set of the selected recording session and domain.

               USER is either:

               •   The real user ID (see getuid(3)) of a process as seen from
                   the root user namespace (see user_namespaces(7)).

               •   A user name.

                   The connected LTTng session daemon (see lttng-sessiond(8))
                   performs the user name resolution on removal from the user
                   ID inclusion set.

               Only available with --kernel option.

           --vuid[=VUSER[,VUSER]...]
               For each VUSER argument, remove VUSER from the virtual user ID
               inclusion set of the selected recording session and domain.

               VUSER is either:

               •   The real user ID (see getuid(3)) of a process as seen from
                   the user namespace (see user_namespaces(7)).

               •   A user name.

                   The connected LTTng session daemon (see lttng-sessiond(8))
                   performs the user name resolution on removal from the
                   virtual user ID inclusion set.

           --gid[=GROUP[,GROUP]...]
               For each GROUP argument, remove GROUP from the group ID
               inclusion set of the selected recording session and domain.

               GROUP is either:

               •   The real group ID (see getgid(3)) of a process as seen
                   from the root user namespace (see user_namespaces(7)).

               •   A group name.

                   The connected LTTng session daemon (see lttng-sessiond(8))
                   performs the group name resolution on removal from the
                   group ID inclusion set.

               Only available with --kernel option.

           --vgid[=VGROUP[,VGROUP]...]
               For each VGROUP argument, remove VGROUP from the virtual group
               ID inclusion set of the selected recording session and domain.

               VGROUP is either:

               •   The real group ID (see getgid(3)) of a process as seen
                   from the user namespace (see user_namespaces(7)).

               •   A group name.

                   The connected LTTng session daemon (see lttng-sessiond(8))
                   performs the group name resolution on removal from the
                   virtual group ID inclusion set.

       Inclusion set operation
           -a, --all
               With one or more empty --pid, --vpid, --uid, --vuid, --gid,
               and --vgid options: clear the selected inclusion sets.

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

           Example 1. Remove the PIDs 1728 and 3775 from the Linux kernel
           process ID inclusion set of the current recording session.

               See the --pid option.

                   $ lttng untrack --kernel --pid=1728,3775

           Example 2. Remove the IDs of a specific groups from the user space
           virtual group ID inclusion set of a specific recording session.

               See the --vgid and --session options.

                   $ lttng untrack --userspace --session=my-session \
                                   --vgid=docker,mysql

           Example 3. Remove all the user IDs from the Linux kernel user ID
           inclusion set of the current recording session.

               See the --all and --uid options.

                   $ lttng untrack --kernel --all --uid

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

           lttng(1), lttng-track(1), lttng-concepts(7)

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

    LTTng 2.15.1                   14 June 2021              LTTNG-UNTRACK(1)

------------------------------------------------------------------------

Pages that refer to this page: [lttng(1)](../man1/lttng.1.html),  [lttng-create(1)](../man1/lttng-create.1.html),  [lttng-enable-event(1)](../man1/lttng-enable-event.1.html),  [lttng-track(1)](../man1/lttng-track.1.html),  [lttng-concepts(7)](../man7/lttng-concepts.7.html)

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
