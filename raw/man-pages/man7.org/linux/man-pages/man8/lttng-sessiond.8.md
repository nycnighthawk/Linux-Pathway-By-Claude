---
{"title": "lttng-sessiond(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lttng-sessiond.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-sessiond(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-SESSIOND(8)              LTTng Manual             LTTNG-SESSIOND(8)

## [](#NAME)NAME

           lttng-sessiond - LTTng session daemon

## [](#SYNOPSIS)SYNOPSIS

           lttng-sessiond [--background | --daemonize] [--sig-parent]
                          [--config=PATH] [--group=GROUP] [--load=PATH]
                          [--default-trace-format=(ctf-1.8 | ctf-2)]
                          [--agent-tcp-port=PORT] [--pidfile=PATH]
                          [--apps-sock=PATH] [--client-sock=PATH]
                          [--no-kernel | [--kmod-probes=PROBE[,PROBE]...]
                                         [--extra-kmod-probes=PROBE[,PROBE]...]
                                         [--kconsumerd-err-sock=PATH]
                                         [--kconsumerd-cmd-sock=PATH]]
                          [--ustconsumerd32-err-sock=PATH]
                          [--ustconsumerd64-err-sock=PATH]
                          [--ustconsumerd32-cmd-sock=PATH]
                          [--ustconsumerd64-cmd-sock=PATH]
                          [--consumerd32-path=PATH] [--consumerd32-libdir=PATH]
                          [--consumerd64-path=PATH] [--consumerd64-libdir=PATH]
                          [--event-notifier-error-buffer-size-kernel=SLOTS]
                          [--event-notifier-error-buffer-size-userspace=SLOTS]
                          [--quiet | [--verbose]... [--verbose-consumer]]

## [](#DESCRIPTION)DESCRIPTION

           The Linux Trace Toolkit: next generation <https://lttng.org/> is
           an open-source software package used for correlated tracing of the
           Linux kernel, user applications, and user libraries.

           LTTng consists of Linux kernel modules (for Linux kernel tracing)
           and dynamically loaded libraries (for user application and library
           tracing).

           An LTTng session daemon, lttng-sessiond, is a program which:

           •   Manages recording sessions (see lttng-concepts(7) to learn
               more about recording sessions).

           •   Controls the various components (like tracers and consumer
               daemons) of LTTng.

           •   Sends asynchronous notifications to user applications.

           A session daemon receives commands from the lttng(1) command-line
           tool, as well as from any user application linked with the LTTng
           control library (liblttng-ctl).

           Each Unix user may have its own independent running session
           daemon. However, the lttng(1) tool must connect to the session
           daemon of the root user (the root session daemon) to control Linux
           kernel tracing.

           When you start lttng-sessiond as the root Unix user, a non-root
           Unix user can connect to it if it’s part of the Unix tracing
           group. By default, the name of the tracing group is tracing.
           Override the tracing group name with the --group option.

           See the “Session daemon connection” section of lttng(1) to learn
           how a user application connects to a session daemon.

           A session daemon manages trace data consumer daemons, spawning
           them when necessary. You do NOT need to manage the consumer
           daemons yourself.

           By default, lttng-sessiond doesn’t start as a daemon. Make it a
           daemon with the --daemonize or --background option. With those
           options, lttng-sessiond ensures the daemon is ready to receive
           client commands before it exits. Make lttng-sessiond write its
           process ID to a file with the --pidfile option.

           Note

               The LTTng project recommends that you start the session daemon
               at boot time for stable and long-term tracing.

           Note

               For an unprivileged Unix user running lttng-sessiond, the
               maximum number of file descriptors per process is usually
               1024. This limits the number of traceable applications, since,
               for each instrumented application, there are two file
               descriptors per CPU as well as one socket for bidirectional
               communication.

               For the root user, the limit is usually 65,535.

       Daemon configuration
           When you run lttng-sessiond, it configures itself from, in this
           order:

            1. The INI configuration file /usr/local/etc/lttng/lttng.conf, if
               any.

            2. The INI configuration file $LTTNG_HOME/.lttng/lttng.conf, if
               any.

               $LTTNG_HOME defaults to $HOME.

            3. With the --config=PATH option: the INI configuration file
               PATH.

            4. The command-line options.

           Each step can override a previous configuration property.

           In INI configuration files, the session daemon only reads the
           properties under the sessiond INI section. Each INI property is:

           Key
               The long name of a command-line option to set (see the
               “OPTIONS” section below).

           Value

               The selected command-line option accepts an argument
                   Option argument (string).

               The selected command-line option is a switch

                   true, yes, on
                       Enable the option.

                   false, no, off
                       Disable the option.

           INI configuration file example:

               [sessiond]
               daemonize=yes
               default-trace-format=ctf-1.8
               extra-kmod-probes=my-driver,other-module

       Recording session configuration loading
           When the session daemon starts, it loads recording session
           configurations from:

           Without the --load option
               In this order:

                1. All the files in $LTTNG_HOME/.lttng/sessions/auto.

                   $LTTNG_HOME defaults to $HOME.

                2. All the files in /usr/local/etc/lttng/sessions/auto.

               lttng-sessiond only loads recording session configuration
               files from the directories above if its UID and their UID are
               the same.

           With the --load=PATH option

               PATH is a directory
                   All the files in PATH.

               PATH is a file
                   The file PATH.

## [](#OPTIONS)OPTIONS

       General daemon configuration
           -b, --background
               Start as a Unix daemon, but keep file descriptors (console)
               open.

               With this option, lttng-sessiond ensures the daemon is ready
               to receive client commands before it exits.

               Use the --daemonize option instead to close the file
               descriptors.

           -f PATH, --config=PATH
               Configure the daemon using the INI configuration file PATH in
               addition to the default configuration files and the
               command-line options.

               See the “Daemon configuration” section above.

           -d, --daemonize
               Start as a Unix daemon and close file descriptors (console).

               With this option, lttng-sessiond ensures the daemon is ready
               to receive client commands before it exits.

               Use the --background option instead to keep the file
               descriptors open.

           --default-trace-format=FORMAT
               Set the default trace format of recording sessions to FORMAT.

               FORMAT is one of:

               ctf-1.8
                   CTF 1.8 <https://diamon.org/ctf/v1.8.3/> (legacy).

               ctf-2
                   CTF 2 <https://diamon.org/ctf/> (preferred).

               When a user application creates a recording session using the
               lttng-create(1) command or the liblttng-ctl API without
               explicitly specifying a trace format, lttng-sessiond uses
               FORMAT.

               Default: ctf-2.

               See also the LTTNG_SESSIOND_DEFAULT_TRACE_FORMAT environment
               variable.

           -g GROUP, --group=GROUP
               Set the Unix tracing group to GROUP instead of tracing.

               This option is only meaningful when the root Unix user starts
               lttng-sessiond.

               Members of the Unix tracing group may connect to the root
               session daemon and, therefore, control LTTng kernel tracing.

           -l PATH, --load=PATH
               Load recording session configurations from PATH, either a
               directory or a file, instead of loading them from the default
               search directories.

               See the “Recording session configuration loading” section
               above.

           -p PATH, --pidfile=PATH
               Write the process ID (PID) of the lttng-sessiond process to
               PATH.

               Such a file contains the textual PID (decimal) followed with a
               newline.

           -S, --sig-parent
               Send the USR1 signal to the parent process to notify
               readiness.

               You can also use the --daemonize or --background option, in
               which case lttng-sessiond ensures the daemon is ready to
               receive client commands before it exits.

       Linux kernel tracing
           At most one of:

           --extra-kmod-probes=PROBE[,PROBE]...
               For each PROBE argument, load the LTTng kernel probe module
               named lttng-probe-PROBE.ko, in addition to loading the default
               LTTng kernel probe modules.

               See also the LTTNG_EXTRA_KMOD_PROBES environment variable.

           --kmod-probes=PROBE[,PROBE]...
               Only load, for each PROBE argument, the LTTng kernel probe
               module named lttng-probe-PROBE.ko, instead of loading the
               default LTTng kernel probe modules.

               See also the LTTNG_KMOD_PROBES environment variable.

           --no-kernel
               Disable Linux kernel tracing.

       Paths and ports
           --agent-tcp-port=PORT
               Listen on TCP port PORT for agent application registration
               instead of a port within the range [5345, 5354]).

           -a PATH, --apps-sock=PATH
               Set the application Unix socket path to PATH.

               This option sets the application Unix socket path even if you
               set the LTTNG_UST_CTL_PATH environment variable.

           -c PATH, --client-sock=PATH
               Set the client Unix socket path to PATH.

           --consumerd32-libdir=PATH
               Set the 32-bit consumer daemon library directory to PATH.

               See also the LTTNG_CONSUMERD32_LIBDIR environment variable.

           --consumerd32-path=PATH
               Set the 32-bit consumer daemon binary path to PATH.

               See also the LTTNG_CONSUMERD32_BIN environment variable.

           --consumerd64-libdir=PATH
               Set the 64-bit consumer daemon library directory to PATH.

               See also the LTTNG_CONSUMERD64_LIBDIR environment variable.

           --consumerd64-path=PATH
               Set the 64-bit consumer daemon binary path to PATH.

               See also the LTTNG_CONSUMERD64_BIN environment variable.

           --kconsumerd-cmd-sock=PATH
               Set the command Unix socket path of the Linux kernel consumer
               daemon to PATH.

           --kconsumerd-err-sock=PATH
               Set the error Unix socket path of the Linux kernel consumer
               daemon to PATH.

           --ustconsumerd32-cmd-sock=PATH
               Set the Unix socket path of the 32-bit consumer daemon command
               to PATH.

           --ustconsumerd64-cmd-sock=PATH
               Set the Unix socket path of the 64-bit consumer daemon command
               to PATH.

           --ustconsumerd32-err-sock=PATH
               Set the Unix socket path of the 32-bit consumer daemon error
               to PATH.

           --ustconsumerd64-err-sock=PATH
               Set the Unix socket path of the 64-bit consumer daemon error
               to PATH.

       Buffer size of event notifier error counters
           --event-notifier-error-buffer-size-kernel=SLOTS
               Set the size of the kernel event notifier error counter
               buffers to SLOTS slots.

           --event-notifier-error-buffer-size-userspace=SLOTS
               Set the size of the user space event notifier error counter
               buffers to SLOTS slots.

           As of LTTng 2.15.1, a slot is a 32-bit counter, but this may
           change in the future.

       Verbosity
           -q, --quiet
               Suppress all messages, including warnings and errors.

               You may NOT use this option with the --verbose and --verbose-
               consumer options.

           -v, --verbose
               Increase verbosity.

               Specify this option up to three times to get more levels of
               verbosity.

               You may NOT use this option with the --quiet option.

           --verbose-consumer
               Increase the verbosity of the consumer daemons which this
               session daemon spawns.

               You may NOT use this option with the --quiet option.

       Program information
           -h, --help
               Show help.

               This option attempts to launch /usr/bin/man to view this
               manual page. Override the manual pager path with the
               LTTNG_MAN_BIN_PATH environment variable.

           --list-options
               List available command options and quit.

           -V, --version
               Show version and quit.

## [](#EXIT_STATUS)EXIT STATUS

           0
               Success

           1
               Error

           3
               Fatal error

## [](#ENVIRONMENT)ENVIRONMENT

           LTTNG_ABORT_ON_ERROR
               Set to 1 to abort the process after the first error is
               encountered.

           LTTNG_APP_SOCKET_TIMEOUT
               Timeout (in seconds) of the application socket when
               sending/receiving commands.

               After this period of time, lttng-sessiond unregisters the
               application.

               Set to 0 or -1 to set an infinite timeout.

               Default: 5.

           LTTNG_CONSUMERD32_BIN
               32-bit consumer daemon binary path.

               The --consumerd32-path option overrides this environment
               variable.

           LTTNG_CONSUMERD32_LIBDIR
               32-bit consumer daemon library directory path.

               The --consumerd32-libdir option overrides this environment
               variable.

           LTTNG_CONSUMERD64_BIN
               64-bit consumer daemon binary path.

               The --consumerd64-path option overrides this environment
               variable.

           LTTNG_CONSUMERD64_LIBDIR
               64-bit consumer daemon library directory path.

               The --consumerd64-libdir option overrides this environment
               variable.

           LTTNG_DEBUG_NOCLONE
               Set to 1 to disable the use of clone(2)/fork(2).

               Setting this environment variable is considered insecure, but
               it’s required to allow debuggers to work with lttng-sessiond
               on some operating systems.

           LTTNG_EXTRA_KMOD_PROBES
               Extra LTTng kernel probe modules to load.

               See the --extra-kmod-probes option which overrides this
               environment variable.

           LTTNG_KMOD_PROBES
               Exclusive LTTng kernel probe modules to load.

               See the --kmod-probes option which overrides this environment
               variable.

           LTTNG_NETWORK_SOCKET_TIMEOUT
               Socket connection, receive, and send timeout (milliseconds).

               Set to 0 or -1 to use the timeout of the operating system
               (default).

           LTTNG_RUNDIR
               The directory containing the control files instead of:

               Session daemon of the root user (root session daemon)
                   The value of the --with-lttng-system-rundir option when
                   configuring the build of the project (/var/run/lttng by
                   default).

               Other session daemon
                   $LTTNG_HOME/.lttng

               This environment variable is particularly useful to run
               multiple root session daemons.

           LTTNG_SESSION_CONFIG_XSD_PATH
               Recording session configuration XML schema definition (XSD)
               path.

           LTTNG_SESSIOND_DEFAULT_TRACE_FORMAT
               Default trace format of recording sessions.

               The value is either ctf-1.8 or ctf-2.

               Note
                   The --default-trace-format option overrides this
                   environment variable.

           LTTNG_UST_CTL_PATH
               Colon-delimited paths of the directories where lttng-sessiond
               places:

               •   The application registration Unix socket.

                   Note
                       The --apps-sock option overrides this specific path.

               •   The "wait" shared memory files to wake up instrumented
                   applications that are waiting for a session daemon to
                   start.

               •   The agent port file.

                   This file contains the TCP port the agents must connect to
                   to enable LTTng tracing.

               Any such directory must exist when you start lttng-sessiond.

               As of LTTng 2.15.1:

               •   lttng-sessiond ignores any path after the first colon (:)
                   and prints a warning.

               •   You cannot escape a colon within a specific path.

               When tracing an application, start it with the
               LTTNG_UST_APP_PATH environment variable set to the same value
               as this environment variable.

               If not set, the default directory path is the effective
               control file directory (see the LTTNG_RUNDIR environment
               variable).

## [](#FILES)FILES

           $LTTNG_HOME/.lttng
               Unix user’s LTTng runtime and configuration directory.

           $LTTNG_HOME/lttng-traces
               Default output directory of LTTng traces in local and snapshot
               modes.

               Override this path with the --output option of the
               lttng-create(1) command.

           $LTTNG_HOME/.lttng/sessions/auto
               Directory from which lttng-sessiond loads Unix user recording
               session configurations when starting.

               See the “Recording session configuration loading” section
               above to learn more.

           /usr/local/etc/lttng/sessions/auto
               Directory from which lttng-sessiond loads system-wide
               recording session configurations when starting.

               See the “Recording session configuration loading” section
               above to learn more.

           $LTTNG_HOME/.lttng/lttng.conf
               Unix user’s LTTng daemon INI configuration file.

               See the “Daemon configuration” section above to learn more.

           /usr/local/etc/lttng/lttng.conf
               System-wide LTTng daemon INI configuration file.

               See the “Daemon configuration” section above to learn more.

           Note

               $LTTNG_HOME defaults to $HOME.

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

    LTTng 2.15.1                  7 October 2025            LTTNG-SESSIOND(8)

------------------------------------------------------------------------

Pages that refer to this page: [lttng(1)](../man1/lttng.1.html),  [lttng-add-context(1)](../man1/lttng-add-context.1.html),  [lttng-add-trigger(1)](../man1/lttng-add-trigger.1.html),  [lttng-clear(1)](../man1/lttng-clear.1.html),  [lttng-create(1)](../man1/lttng-create.1.html),  [lttng-destroy(1)](../man1/lttng-destroy.1.html),  [lttng-disable-channel(1)](../man1/lttng-disable-channel.1.html),  [lttng-disable-event(1)](../man1/lttng-disable-event.1.html),  [lttng-disable-rotation(1)](../man1/lttng-disable-rotation.1.html),  [lttng-enable-channel(1)](../man1/lttng-enable-channel.1.html),  [lttng-enable-event(1)](../man1/lttng-enable-event.1.html),  [lttng-enable-rotation(1)](../man1/lttng-enable-rotation.1.html),  [lttng-help(1)](../man1/lttng-help.1.html),  [lttng-list(1)](../man1/lttng-list.1.html),  [lttng-list-triggers(1)](../man1/lttng-list-triggers.1.html),  [lttng-load(1)](../man1/lttng-load.1.html),  [lttng-metadata(1)](../man1/lttng-metadata.1.html),  [lttng-reclaim-memory(1)](../man1/lttng-reclaim-memory.1.html),  [lttng-regenerate(1)](../man1/lttng-regenerate.1.html),  [lttng-remove-trigger(1)](../man1/lttng-remove-trigger.1.html),  [lttng-rotate(1)](../man1/lttng-rotate.1.html),  [lttng-save(1)](../man1/lttng-save.1.html),  [lttng-set-session(1)](../man1/lttng-set-session.1.html),  [lttng-snapshot(1)](../man1/lttng-snapshot.1.html),  [lttng-start(1)](../man1/lttng-start.1.html),  [lttng-status(1)](../man1/lttng-status.1.html),  [lttng-stop(1)](../man1/lttng-stop.1.html),  [lttng-track(1)](../man1/lttng-track.1.html),  [lttng-untrack(1)](../man1/lttng-untrack.1.html),  [lttng-version(1)](../man1/lttng-version.1.html),  [lttng-view(1)](../man1/lttng-view.1.html),  [lttng-ust(3)](../man3/lttng-ust.3.html),  [lttng-concepts(7)](../man7/lttng-concepts.7.html),  [lttng-relayd(8)](../man8/lttng-relayd.8.html)

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
