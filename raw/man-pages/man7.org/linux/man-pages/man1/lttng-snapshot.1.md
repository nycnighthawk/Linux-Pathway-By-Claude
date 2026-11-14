---
{"title": "lttng-snapshot(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lttng-snapshot.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-snapshot(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-SNAPSHOT(1)              LTTng Manual             LTTNG-SNAPSHOT(1)

## [](#NAME)NAME

           lttng-snapshot - Take a snapshot of an LTTng recording session

## [](#SYNOPSIS)SYNOPSIS

           Take a recording session snapshot:

           lttng [GENERAL OPTIONS] snapshot record [--max-size=SIZE]
                 [--name=NAME] [--session=SESSION]
                 [--ctrl-url=URL --data-url=URL | URL]

           Add a snapshot output to a recording session:

           lttng [GENERAL OPTIONS] snapshot add-output [--max-size=SIZE]
                 [--name=NAME] [--session=SESSION]
                 (--ctrl-url=URL --data-url=URL | URL)

           Show the snapshot output of a recording session:

           lttng [GENERAL OPTIONS] snapshot list-output [--session=SESSION]

           Remove the snapshot output from a recording session:

           lttng [GENERAL OPTIONS] snapshot del-output [--session=SESSION] 1

## [](#DESCRIPTION)DESCRIPTION

           The lttng snapshot command can take a snapshot of, add or remove a
           snapshot output, and show the snapshot output of:

           With the --session=SESSION option
               The recording session named SESSION.

           Without the --session option
               The current recording session (see lttng-concepts(7) to learn
               more about the current recording session).

           See lttng-concepts(7) to learn more about recording sessions.

           A snapshot is a dump of the current sub-buffers of all the
           channels of the selected recording session.

           When LTTng takes a snapshot, it sends the sub-buffer dump of the
           selected recording session to the local file system or over the
           network to a listening relay daemon (lttng-relayd(8)). See the
           “Snapshot output” section below to learn more.

           When LTTng takes a snapshot, it does NOT clear the sub-buffers of
           the selected recording session. In other words, different
           snapshots of the selected recording session can contain the same
           event records.

           You must have created the selected recording session in snapshot
           mode (see the --snapshot option of the lttng-create(1) command as
           well as lttng-concepts(7) to learn more about recording session
           modes) to use the snapshot command.

           A snapshot-session trigger action can also take a recording
           session snapshot (see lttng-add-trigger(1)).

           See the “EXAMPLES” section below for usage examples.

           If you want, instead, to keep all the trace data, but divide it
           into archived chunks which are then, like snapshots, ready to be
           processed, see the recording session rotation feature in
           lttng-concepts(7). Trace chunk archives do NOT overlap like
           snapshots can.

           Note

               Before you take a snapshot on a system with a high event
               throughput, the LTTng project recommends that you first run
               the lttng-stop(1) command. Otherwise, the snapshot could
               contain “holes”, the result of the tracers overwriting
               unconsumed trace packets during the snapshot operation.

               After LTTng writes the snapshot trace data, you can restart
               the recording session with the lttng-start(1) command.

       Snapshot output
           When you take a recording session snapshot with the record action,
           LTTng writes the snapshot trace files to:

           If you specify the URL non-option argument or the --ctrl-url and
           --data-url options
               The output defined by the URL non-option argument or by the
               arguments of the options.

               See lttng-create(1) for the format of URL.

           Otherwise
               The snapshot output of the selected recording session.

               Add a snapshot output to a recording session with the add-
               output action. As of LTTng 2.15.1, you may only add one
               snapshot output to a given recording session.

               When you create a snapshot mode recording session with the
               --snapshot option of the lttng-create(1) command, and without
               its --no-output option, the create command automatically adds
               a snapshot output named snapshot-1 to the created recording
               session:

               With its --output, --set-url, --ctrl-url, or --data-url
               options
                   Equivalent to using the add-output action with the
                   provided or equivalent URL(s) immediately after creating
                   the recording session.

               Otherwise
                   A subdirectory, under the $LTTNG_HOME/lttng-traces
                   ($LTTNG_HOME defaults to $HOME) directory, of which the
                   name contains the recording session name and the
                   date/time.

               Show the current snapshot output of a recording session with
               the list-output action.

               Remove the snapshot output of a recording session with the
               del-output action.

           For both the record and add-output actions:

           •   Assign a name to a snapshot output with the --name=NAME
               option.

               NAME becomes part of the snapshot trace file names which LTTng
               sends to this output.

           •   By default, the snapshot files can be as big as the sum of the
               sizes of all the sub-buffers of all the channels of the
               selected recording session.

               Set the maximum total size of all the snapshot trace files
               LTTng writes with the --max-size option.

## [](#OPTIONS)OPTIONS

           See lttng(1) for GENERAL OPTIONS.

       Recording target
           -s SESSION, --session=SESSION
               Take a snapshot of the sub-buffers of the recording session
               named SESSION instead of the current recording session.

       Output
           See the “Snapshot output” section above.

           -C URL, --ctrl-url=URL
               Set the control path URL to URL.

               You must also use the --data-url option.

               See lttng-create(1) for the format of URL.

           -D URL, --data-url=URL
               Set the trace data path URL to URL.

               You must also use the --ctrl-url option.

               See lttng-create(1) for the format of URL.

           -m SIZE, --max-size=SIZE
               Set the maximum total size of all the snapshot trace files
               LTTng writes when taking a snapshot to SIZE bytes.

               The k (KiB), M (MiB), and G (GiB) suffixes are supported.

           -n NAME, --name=NAME
               Assign the name NAME to the snapshot output.

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

           Example 1. Take a snapshot of the current recording session,
           sending the trace files to its snapshot output.

                   $ lttng snapshot record

           Example 2. Take a snapshot of a specific recording session, giving
           it a custom name.

               See the --session and --name options.

                   $ lttng snapshot record --session=my-session --name=SNAP

           Example 3. Take a snapshot of the current recording session,
           sending the trace files to a custom location.

               See the “Output directory” section of lttng-relayd(8) to
               understand where the relay daemon to connect to (3.96.87.215)
               writes the received traces.

                   $ lttng snapshot record net://3.96.87.215

           Example 4. Replace the snapshot output of a specific recording
           session with a local file system path.

               See the --session option.

                   $ lttng snapshot del-output --session=monk 1
                   $ lttng snapshot add-output --session=monk \
                                    file:///path/to/snapshots

           Example 5. Take a snapshot of the current recording session,
           making sure its size is not over 4 MiB.

               See the --max-size option.

                   $ lttng snapshot record --max-size=4M

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

           lttng(1), lttng-create(1), lttng-concepts(7)

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

    LTTng 2.15.1                   14 June 2021             LTTNG-SNAPSHOT(1)

------------------------------------------------------------------------

Pages that refer to this page: [lttng(1)](../man1/lttng.1.html),  [lttng-add-trigger(1)](../man1/lttng-add-trigger.1.html),  [lttng-create(1)](../man1/lttng-create.1.html),  [lttng-rotate(1)](../man1/lttng-rotate.1.html),  [lttng-concepts(7)](../man7/lttng-concepts.7.html)

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
