---
{"title": "lttng-add-trigger(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lttng-add-trigger.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-add-trigger(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-ADD-TRIGGER(1)           LTTng Manual          LTTNG-ADD-TRIGGER(1)

## [](#NAME)NAME

           lttng-add-trigger - Add an LTTng trigger

## [](#SYNOPSIS)SYNOPSIS

           lttng [GENERAL OPTIONS] add-trigger [--name=NAME] [--owner-uid=UID]
                 --condition=CONDTYPE [CONDARGS]
                 --action=ACTTYPE [ACTARGS] [--action=ACTTYPE [ACTARGS]]...

## [](#DESCRIPTION)DESCRIPTION

           The lttng add-trigger command creates and adds an LTTng trigger to
           the connected session daemon (see lttng-sessiond(8)).

           See lttng-concepts(7) to learn more about LTTng triggers.

           By default, the add-trigger command automatically assigns a name,
           unique for a given session daemon and Unix user, to the added
           trigger. Assign a custom name with the --name.

           The add-trigger command adds a trigger for your Unix user. If your
           Unix user is root, you may add the trigger as another user with
           the --owner-uid option.

           Specify the condition of the trigger to add with a condition
           specifier and its actions with one or more action specifiers. The
           order of the action specifiers is significant: LTTng attempts to
           execute the actions of a firing trigger in this order.

           See the “EXAMPLES” section below for usage examples.

           List the triggers of your Unix user, or of all users if your Unix
           user is root, with the lttng-list-triggers(1) command.

           Remove a trigger with the lttng-remove-trigger(1) command.

       Condition specifier
           Synopsis:

               --condition=CONDTYPE [CONDARGS]

           A condition specifier is the --condition option, which specifies
           the type of condition CONDTYPE, followed, depending on CONDTYPE,
           with zero or more arguments CONDARGS.

           The available condition types are:

           channel-buffer-usage-ge, channel-buffer-usage-le
               Synopses:

                   --condition=channel-buffer-usage-ge --session=SESSION
                   --channel=CHANNEL
                   --domain=(kernel | user | jul | log4j | log4j2 | python)
                   (--threshold-ratio=RATIO | --threshold-size=SIZE)

                   --condition=channel-buffer-usage-le --session=SESSION
                   --channel=CHANNEL
                   --domain=(kernel | user | jul | log4j | log4j2 | python)
                   (--threshold-ratio=RATIO | --threshold-size=SIZE)

               A channel-buffer-usage-ge or channel-buffer-usage-le condition
               is considered satisfied when the ring buffer usage of the
               channel CHANNEL (within the recording session SESSION and the
               tracing domain specified by --domain) becomes greater/less
               than or equal to either:

               With the --threshold-size=SIZE option
                   SIZE bytes.

                   SIZE supports the k (KiB), M (MiB), and G (GiB) suffixes.

               With the --threshold-ratio=RATIO option
                   RATIO times the total size of the ring buffer of the
                   targeted channel.

                   RATIO is a floating point number from 0 to 1.

               Every time the monitor timer (see the --monitor-timer option
               of lttng-enable-channel(1)) of a channel expires, LTTng
               updates its statistics, including its buffer usage. This is
               when LTTng tries to evaluate channel-buffer-usage-ge and
               channel-buffer-usage-le conditions.

               The short options -c, -d, -s, and -t are aliases of --channel,
               --domain, --session, and --threshold-size.

           event-rule-matches
               Synopsis:

                   --condition=event-rule-matches [--capture=CDESCR]... ERSPEC

               An event-rule-matches condition is considered satisfied when
               the event rule specified with ERSPEC matches an event.

               See lttng-event-rule(7) to learn how to specify an event rule
               (ERSPEC part).

               Capture event record and context fields with one or more
               --capture options (see the “Capture descriptor” section below
               to learn more). When an event-rule-matches condition with
               capture descriptors is satisfied, the captured field values
               are available in the evaluation object of the condition using
               the liblttng-ctl C API.

               Important
                   Make sure to single-quote CDESCR when you run the add-
                   trigger command from a shell, as capture descriptors can
                   include characters having a special meaning for most
                   shells.

           session-consumed-size-ge
               Synopsis:

                   --condition=session-consumed-size-ge --session=SESSION
                   --threshold-size=THRESHOLD

               A session-consumed-size-ge condition is considered satisfied
               when the total consumed size of the tracing data of all the
               channels of the recording session SESSION becomes greater than
               or equal to THRESHOLD bytes.

               Every time the monitor timer (see the --monitor-timer option
               of lttng-enable-channel(1)) of a channel expires, LTTng
               updates the statistics, like the total consumed tracing data
               size, of its owning recording session. This is when LTTng
               tries to evaluate session-consumed-size-ge conditions.

               THRESHOLD supports the k (KiB), M (MiB), and G (GiB) suffixes.

               The short options -s and -t are aliases of --session and
               --threshold-size.

           session-rotation-starts, session-rotation-finishes
               Synopses:

                   --condition=session-rotation-starts --session=SESSION

                   --condition=session-rotation-finishes --session=SESSION

               A session-rotation-starts or session-rotation-finishes
               condition is considered satisfied when the rotation operation
               (see lttng-rotate(1)) of the recording session SESSION starts
               or finishes.

               The short option -s is an alias of --session.

       Capture descriptor
           A capture descriptor is a textual expression which describes how
           to read an event record or context field.

           The argument of a --capture option, when using an “event rule
           matches” condition specifier (event-rule-matches), is a capture
           descriptor.

           A capture descriptor expression is one of:

           NAME
               An event record field named NAME.

               The supported event record field types are:

               •   Integer

               •   Enumeration (integral value)

               •   Floating point number

               •   Static array of integers

               •   Dynamic array (“sequence”) of integers

               •   Text string

               Examples: my_field, target_cpu, ip.

           $ctx.NAME
               A statically-known context field named NAME.

               List the available statically-known context field names with
               lttng-add-context(1). As of LTTng 2.15.1, context field names
               starting with perf: aren’t supported.

               Examples: $ctx.prio, $ctx.gid, $ctx.preemptible.

           $app.PROVIDER.NAME
               An application-specific context field named NAME from the
               provider PROVIDER.

               See lttng-add-context(1) to learn more about
               application-specific context fields.

               Example: $app.server:cur_user.

           EXPR[INDEX]
               The element at index INDEX of the array field (static or
               dynamic) identified by the expression EXPR.

               INDEX must be a constant, positive integral value.

               Examples: ip[3], user_ids[15].

           If, when an event rule matches, a given capture descriptor doesn’t
           identify an existing event or context field, then the captured
           value is reported as being unavailable. This applies to:

           •   A nonexistent event record field name.

           •   A nonexistent statically-known context field name.

           •   A nonexistent application-specific context field name.

           •   An out-of-bounds array field index.

       Action specifier
           Synopsis:

               --action=ACTTYPE [ACTARGS]

           An action specifier is the --action option, which specifies the
           type of action ACTTYPE, followed, depending on ACTTYPE, with zero
           or more arguments ACTARGS.

           The available action types are:

           Notify
               Synopsis:

                   --action=notify [--rate-policy=POLICY]

               Sends a notification through the notification mechanism of the
               session daemon (see lttng-sessiond(8)).

               The session daemon sends details about the condition
               evaluation along with the notification.

               As of LTTng 2.15.1, you can write a C/C++ program to receive
               LTTng notifications (see the liblttng-ctl C headers).

               See below for the --rate-policy option.

           Start a recording session
               Synopsis:

                   --action=start-session SESSION [--rate-policy=POLICY]

               Starts the recording session named SESSION like lttng-start(1)
               would.

               If no recording session has the name SESSION when LTTng is
               ready to execute the action, LTTng does nothing.

               See below for the --rate-policy option.

           Stop a recording session
               Synopsis:

                   --action=stop-session SESSION [--rate-policy=POLICY]

               Stops the recording session named SESSION like lttng-stop(1)
               would.

               If no recording session has the name SESSION when LTTng is
               ready to execute the action, LTTng does nothing.

               See below for the --rate-policy option.

           Rotate a recording session
               Synopsis:

                   --action=rotate-session SESSION [--rate-policy=POLICY]

               Archives the current trace chunk of the recording session
               named SESSION like lttng-rotate(1) would.

               If no recording session has the name SESSION when LTTng is
               ready to execute the action, LTTng does nothing.

               See below for the --rate-policy option.

           Take a recording session snapshot
               Synopsis:

                   --action=snapshot-session SESSION [--name=NAME]
                                             [--max-size=SIZE]
                                             [--path=PATH | --url=URL |
                                              (--ctrl-url=URL --data-url=URL)]
                                             [--rate-policy=POLICY]

               Takes a snapshot of the recording session named SESSION like
               lttng-snapshot(1) would.

               When the condition of the trigger is satisfied, the recording
               session named SESSION, if any, must be a snapshot-mode
               recording session (see lttng-create(1)).

               If no recording session has the name SESSION when LTTng is
               ready to execute the action, LTTng does nothing.

               See the add-output action of the lttng-snapshot(1) command to
               learn about the snapshot output options: --name/-n, --max-
               size/-m, --url, --ctrl-url/-C, and --data-url/-D. The --path
               option specifies to write the snapshot to the local
               directory PATH.

           See below for the --rate-policy option.

           Common action options (as of LTTng 2.15.1):

           --rate-policy=POLICY
               Set the rate policy of the action to POLICY instead of every:1
               (always execute).

               A trigger which “fires” (its condition is satisfied) leads to
               an execution request for each of its actions, in order. An
               execution request of a given action A first increments the
               execution request count C of A. An execution request can then
               become an actual execution when C satisfies the rate policy
               of A.

               POLICY is one of:

               once-after:COUNT
                   Only execute A when C is equal to COUNT.

                   In other words, execute A a single time after COUNT
                   execution requests.

               every:COUNT
                   Only execute A when C is a multiple of COUNT.

                   In other words, execute A every COUNT execution requests.

               COUNT must be an integer greater than 0.

               As of LTTng 2.15.1, you can use this option with any action
               type, but new action types in the future may not support it.

## [](#OPTIONS)OPTIONS

       Identification
           --name=NAME
               Set the unique name of the trigger to add to NAME instead of
               the add-trigger command automatically assigning one.

           --owner-uid=UID
               Add the trigger as the Unix user having the user ID UID.

               You may only use this option if your Unix user is root.

       Specifier
           --condition=CONDTYPE
               Introductory option for a condition specifier of type
               CONDTYPE.

               See the “Condition specifier” section above to learn more.

           --action=ACTTYPE
               Introductory option for an action specifier of type ACTTYPE.

               See the “Action specifier” section above to learn more.

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

           Example 1. Add an “event rule matches” trigger of which the action
           is to send a notification.

               The event-rule-matches trigger condition below specifies an
               event rule which matches any Linux system call entry event
               with a name starting with exec.

                   $ lttng add-trigger --condition=event-rule-matches \
                                       --type=syscall:entry \
                                       --name='exec*' --action=notify

           Example 2. Add an “event rule matches” trigger of which the action
           is to stop a recording session and then rotate it.

               The event-rule-matches trigger condition below specifies an
               event rule which matches any user space tracepoint event with
               a name starting with my_app: and with a log level at least as
               severe as a warning.

               The order of the --action options below is significant.

                   $ lttng add-trigger --condition=event-rule-matches \
                                       --type=user --name='my_app:*' \
                                       --log-level=TRACE_WARNING.. \
                                       --action=stop-session my-session \
                                       --action=rotate-session my-session

               See lttng-concepts(7) to learn more about recording sessions
               and rotations.

           Example 3. Add an “event rule matches” trigger with a specific
           name.

               The event-rule-matches trigger condition below specifies an
               event rule which matches events which LTTng creates from the
               my-logger Python logger.

               The added trigger is named my-trigger, a unique name for your
               Unix user.

               See the --name option.

                   $ lttng add-trigger --name=my-trigger \
                                       --condition=event-rule-matches \
                                       --type=python --name=my-logger \
                                       --action=snapshot-session my-session

           Example 4. Add an “event rule matches” trigger as another Unix
           user.

               The command line below adds a trigger as the mireille Unix
               user.

               Your Unix user must be root to use the --owner-uid option.

               The condition of the trigger specifies an event rule which
               matches LTTng kernel tracepoint events with a name which
               starts with sched.

                   # lttng add-trigger --owner-uid=$(id --user mireille) \
                                       --condition=event-rule-matches \
                                       --type=kernel --name='sched*' \
                                       --action=notify

           Example 5. Add an “event rule matches” trigger with a notification
           action to be executed every 10 times.

               The event-rule-matches trigger condition below specifies an
               event rule which matches all user space tracepoint events.

               See the --rate-policy option above.

                   $ lttng add-trigger --condition=event-rule-matches \
                                       --type=user --action=notify \
                                       --rate-policy=every:10

           Example 6. Add an “event rule matches” trigger with a recording
           session starting action to be executed a single time after
           40 times.

               The event-rule-matches trigger condition below specifies an
               event rule which matches any Linux system call event (entry
               and exit) of which the fd event record field is less than 3.

               See the --rate-policy option above.

                   $ lttng add-trigger --condition=event-rule-matches \
                                       --type=syscall --filter='fd < 3' \
                                       --action=start-session my-session \
                                       --rate-policy=once-after:40

           Example 7. Add a “recording session consumed data size becomes
           greater than” trigger of which the action is to rotate the
           recording session.

               The session-consumed-size-ge trigger condition below is
               considered satisfied when the total consumed size of the
               recording session named my-session becomes greater than or
               equal to 100 MiB.

                   $ lttng add-trigger --condition=session-consumed-size-ge \
                                       --session=my-session --threshold-size=100M \
                                       --action=rotate-session my-session

               See lttng-concepts(7) to learn more about recording sessions
               and rotations.

           Example 8. Add a “channel buffer usage becomes greater than or
           equal to” trigger of which the actions are to send a notification
           and to rotate the recording session.

               The channel-buffer-usage-ge trigger condition below is
               considered satisfied when the ring buffer usage of the Linux
               kernel channel named my-channel within the recording session
               named my-session becomes greater than or equal to 512 KiB.

               The order of the --action options below is significant.

                   $ lttng add-trigger --condition=channel-buffer-usage-ge \
                                       --session=my-session --channel=my-channel \
                                       --domain=kernel --threshold-size=512k \
                                       --action=notify \
                                       --action=rotate-session my-session

               See lttng-concepts(7) to learn more about recording sessions,
               channels, and rotations.

           Example 9. Add a “recording session rotation finishes” trigger of
           which the action is to send a notification.

               The session-rotation-finishes trigger condition below is
               considered satisfied when a rotation of the recording session
               named my-session finishes.

                   $ lttng add-trigger --condition=session-rotation-finishes \
                                       --session=my-session --action=notify

               See lttng-concepts(7) to learn more about recording sessions
               and rotations.

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

           lttng(1), lttng-list-triggers(1), lttng-remove-trigger(1),
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

    LTTng 2.15.1                 9 December 2025         LTTNG-ADD-TRIGGER(1)

------------------------------------------------------------------------

Pages that refer to this page: [lttng(1)](../man1/lttng.1.html),  [lttng-list-triggers(1)](../man1/lttng-list-triggers.1.html),  [lttng-remove-trigger(1)](../man1/lttng-remove-trigger.1.html),  [lttng-rotate(1)](../man1/lttng-rotate.1.html),  [lttng-snapshot(1)](../man1/lttng-snapshot.1.html),  [lttng-start(1)](../man1/lttng-start.1.html),  [lttng-stop(1)](../man1/lttng-stop.1.html),  [lttng-concepts(7)](../man7/lttng-concepts.7.html),  [lttng-event-rule(7)](../man7/lttng-event-rule.7.html)

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
