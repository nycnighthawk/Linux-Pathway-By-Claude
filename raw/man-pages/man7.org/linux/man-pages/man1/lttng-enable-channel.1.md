---
{"title": "lttng-enable-channel(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lttng-enable-channel.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-enable-channel(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-ENABLE-CHANN(1)          LTTng Manual         LTTNG-ENABLE-CHANN(1)

## [](#NAME)NAME

           lttng-enable-channel - Create or enable LTTng channels

## [](#SYNOPSIS)SYNOPSIS

           Create a Linux kernel channel:

           lttng [GENERAL OPTIONS] enable-channel --kernel
                 [--discard | --overwrite] [--output=(mmap | splice)]
                 [--subbuf-size=SIZE] [--num-subbuf=COUNT]
                 [--switch-timer=PERIODUS] [--read-timer=PERIODUS]
                 [--monitor-timer=PERIODUS]
                 [--buffer-ownership=system] [--buffer-allocation=per-cpu]
                 [--tracefile-size=SIZE [--tracefile-count=COUNT]]
                 [--session=SESSION] CHANNEL

           Create a user space channel:

           lttng [GENERAL OPTIONS] enable-channel --userspace
                 [--overwrite |
                  [--discard] [--blocking-timeout=TIMEOUTUS]
                  [--auto-reclaim-memory=(off | consumed | older-than:AGEUS)]]
                 [--output=mmap] [--buffer-ownership=(user | process)]
                 [--buffer-allocation=(per-cpu | per-channel)]
                 [--buffer-preallocation=(preallocate | on-demand)]
                 [--subbuf-size=SIZE] [--num-subbuf=COUNT]
                 [--switch-timer=PERIODUS] [--read-timer=PERIODUS]
                 [--monitor-timer=PERIODUS] [--watchdog-timer=PERIODUS]
                 [--tracefile-size=SIZE [--tracefile-count=COUNT]]
                 [--session=SESSION] CHANNEL

           Enable channel(s):

           lttng [GENERAL OPTIONS] enable-channel (--userspace | --kernel)
                 [--session=SESSION] CHANNEL[,CHANNEL]...

## [](#DESCRIPTION)DESCRIPTION

           The lttng enable-channel command does one of:

           •   Create a channel named CHANNEL.

           •   Enable one or more disabled channels named CHANNEL (non-option
               argument, comma-separated).

           See lttng-concepts(7) to learn more about channels.

           The channel(s) to create or enable belong to:

           With the --session=SESSION option
               The recording session named SESSION.

           Without the --session option
               The current recording session (see lttng-concepts(7) to learn
               more about the current recording session).

           Note

               The lttng-enable-event(1) command can automatically create a
               default channel when no channel exists for the provided
               tracing domain.

           See the “EXAMPLES” section below for usage examples.

           List the channels of a given recording session with the
           lttng-list(1) and lttng-status(1) commands.

           Disable an enabled channel with the lttng-disable-channel(1)
           command.

           Important

               As of LTTng 2.15.1, you may NOT perform the following
               operations with the enable-channel command:

               •   Change an attribute of an existing channel.

               •   Enable a disabled channel once its recording session has
                   been active (started; see lttng-start(1)) at least once.

               •   Create a channel once its recording session has been
                   active at least once.

               •   Create a user space channel with a given buffer ownership
                   model (--buffer-ownership set to user or process) and
                   create a second user space channel with a different buffer
                   ownership model in the same recording session.

## [](#OPTIONS)OPTIONS

           See lttng(1) for GENERAL OPTIONS.

       Tracing domain
           One of:

           -k, --kernel
               Create or enable channels in the Linux kernel domain.

           -u, --userspace
               Create or enable channels in the user space domain.

       Recording target
           -s SESSION, --session=SESSION
               Create or enable channels in the recording session named
               SESSION instead of the current recording session.

       Buffer ownership model
           One of:

           --buffers-global
               Equivalent to --buffer-ownership=system.

               Deprecated.

           --buffer-ownership=MODEL
               Depending on MODEL:

               process
                   Allocate one set of ring buffers (one per CPU or one for
                   the whole channel, depending on --buffer-allocation) for
                   each instrumented process of:

                   If you connect to the root session daemon
                       All Unix users.

                       See the “Session daemon connection” section of
                       lttng(1) to learn how a user application connects to a
                       session daemon.

                   Otherwise
                       Your Unix user.

                   Only available with the --userspace option.

               system
                   Allocate a single set of ring buffers (one per CPU) for
                   the whole system.

                   Only available with the --kernel option.

                   As of LTTng 2.15.1, this is the default buffer ownership
                   model for the Linux kernel tracing domain, but this may
                   change in the future.

               user
                   Allocate one set of ring buffers (one per CPU or one for
                   the whole channel, depending on --buffer-allocation)
                   shared by all the instrumented processes of:

                   If you connect to the root session daemon
                       Each Unix user.

                       See the “Session daemon connection” section of
                       lttng(1) to learn how a user application connects to a
                       session daemon.

                   Otherwise
                       Your Unix user.

                   Only available with the --userspace option.

                   As of LTTng 2.15.1, this is the default buffer ownership
                   model for the user space tracing domain, but this may
                   change in the future.

           --buffers-pid
               Equivalent to --buffer-ownership=process.

               Deprecated.

           --buffers-uid
               Equivalent to --buffer-ownership=user.

               Deprecated.

       Buffer allocation policy
           --buffer-allocation=POLICY
               Depending on POLICY, allocate one ring buffer for:

               per-channel
                   The whole channel.

                   Setting --buffer-ownership to user or process determines
                   what entity gets a channel-wise ring buffer.

                   Only available with the --userspace option.

               per-cpu
                   Each CPU.

                   Setting --buffer-ownership to user, process, or system
                   determines what entity gets a set of per-CPU ring buffers.

                   Using this buffer allocation policy implies adding the
                   cpu_id context field, without any way to remove it, for
                   the created channel, similar to running:

                       $ lttng add-context --session=SESSION --channel=CHANNEL \
                                           --type=cpu_id

                   As of LTTng 2.15.1, this is the default buffer allocation
                   policy, but this may change in the future.

       Buffer preallocation policy
           --buffer-preallocation=POLICY
               Depending on POLICY, allocate:

               preallocate
                   The full backing memory for all ring buffers when you
                   create the channel.

                   This policy provides consistent performance but uses more
                   memory upfront. Use this policy to optimize instrumented
                   application startup time.

                   As of LTTng 2.15.1, this is the default buffer
                   preallocation policy, but this may change in the future.

               on-demand
                   Backing memory for ring buffers incrementally, as needed
                   during tracing.

                   This policy uses less initial memory but may introduce
                   slight performance overhead when allocating new memory
                   during tracing.

               Only available with the --userspace option.

       Automatic memory reclaim
           --auto-reclaim-memory=STRATEGY
               Set the automatic memory reclaim strategy to STRATEGY for the
               created channel.

               STRATEGY is one of:

               off (default)
                   No automatic memory reclaim.

               consumed
                   LTTng automatically reclaims the memory of sub-buffers as
                   soon as they’re consumed (read).

                   This strategy is not available for channels of recording
                   sessions in snapshot mode or without an output.

               older-than:AGEUS
                   LTTng automatically reclaims the memory of sub-buffers of
                   which the closing time exceeds AGEUS µs.

                   The ms (milliseconds), s (seconds), m (minutes), and
                   h (hours) suffixes are supported.

                   This is more or less equivalent to automatically running
                   the lttng-reclaim-memory(1) command. LTTng automatically
                   evaluates the eligibility of sub-buffers for a memory
                   reclaim operation at regular intervals (every half
                   AGEUS µs, but also at least a period defined at build
                   time) and reclaims sub-buffers of which the age of the
                   closing time have exceeded AGEUS µs.

                   More specifically:

                   If AGEUS > last stream activity age
                       Only sub-buffers of which the age, at the moment of
                       closing them, is greater than AGEUS are eligible for a
                       memory reclaim.

                   If AGEUS < last stream activity age
                       All sub-buffers are eligible and LTTng flushes the
                       targeted channel so that any open sub-buffer gets
                       closed to become eligible.

               Only available with the --userspace and --discard options.

       Event record loss mode
           --blocking-timeout=TIMEOUTUS
               Set the blocking timeout value of the channel to TIMEOUTUS µs
               for instrumented applications executed with a set
               LTTNG_UST_ALLOW_BLOCKING environment variable.

               TIMEOUTUS is one of:

               0 (default)
                   Do not block (non-blocking mode).

               inf
                   Block forever until a sub-buffer is available to write the
                   event record.

               N, a positive value
                   Wait for at most N µs when trying to write to a
                   sub-buffer. After N µs, discard the event record.

               This option is only available with both the --userspace and
               --discard options.

           One of:

           --discard
               Discard event records when there’s no available sub-buffer.

               As of LTTng 2.15.1, this is the default event record loss
               mode, but this may change in the future.

           --overwrite
               Overwrite the whole sub-buffer containing the oldest event
               records when there’s no available sub-buffer (flight recorder
               mode).

       Sub-buffers
           --num-subbuf=COUNT
               Use COUNT sub-buffers per ring buffer.

               The effective value is COUNT rounded up to the next power of
               two.

               Default values:

               --userspace and --buffer-ownership=user options
                   4

               --userspace and --buffer-ownership=process options
                   4

               --kernel and --buffer-ownership=system options
                   4

               metadata channel
                   2

           --output=TYPE
               Set the output type of the channel to TYPE.

               TYPE is one of:

               mmap
                   Share ring buffers between the tracer and the consumer
                   daemon with the mmap(2) system call.

               splice
                   Share ring buffers between the tracer and the consumer
                   daemon with the splice(2) system call.

                   Only available with the --kernel option.

               Default values:

               --userspace and --buffer-ownership=user options
                   mmap

               --userspace and --buffer-ownership=process options
                   mmap

               --kernel and --buffer-ownership=system options
                   splice

               metadata channel
                   mmap

           --subbuf-size=SIZE
               Set the size of each sub-buffer to SIZE bytes.

               The effective value is SIZE rounded up to the next power of
               two.

               The k (KiB), M (MiB), and G (GiB) suffixes are supported.

               The minimum sub-buffer size, for each tracer, is the maximum
               value between the default below and the system page size (see
               getconf(1) with the PAGE_SIZE variable).

               Default values:

               --userspace and --buffer-ownership=user options
                   524288

               --userspace and --buffer-ownership=process options
                   16384

               --kernel and --buffer-ownership=system options
                   1048576

               metadata channel
                   4096

       Trace files
           --tracefile-count=COUNT
               Limit the number of trace files which LTTng writes for this
               channel to COUNT.

               COUNT set to 0 means “unlimited”.

               Default: 0.

               You must also use the --tracefile-size option with this
               option.

           --tracefile-size=SIZE
               Set the maximum size of each trace file which LTTng writes for
               this channel to SIZE bytes.

               SIZE set to 0 means “unlimited”.

               Default: 0.

               Note
                   Data streams which LTTng writes for a channel configured
                   with this option may inaccurately report discarded event
                   records as of CTF 1.8 and CTF 2.

       Timers
           --monitor-timer=PERIODUS
               Set the period of the monitor timer of the channel to
               PERIODUS µs.

               Set PERIODUS to 0 to disable the monitor timer.

               Default values:

               --userspace and --buffer-ownership=user options
                   1000000

               --userspace and --buffer-ownership=process options
                   1000000

               --kernel and --buffer-ownership=system options
                   1000000

           --read-timer=PERIODUS
               Set the period of the read timer of the channel to
               PERIODUS µs.

               Set PERIODUS to 0 to disable the read timer.

               Default values:

               --userspace and --buffer-ownership=user options
                   0

               --userspace and --buffer-ownership=process options
                   0

               --kernel and --buffer-ownership=system options
                   200000

               metadata channel
                   0

           --switch-timer=PERIODUS
               Set the period of the switch timer of the channel to
               PERIODUS µs.

               Set PERIODUS to 0 to disable the switch timer.

               Default values:

               --userspace and --buffer-ownership=user options
                   0

               --userspace and --buffer-ownership=process options
                   0

               --kernel and --buffer-ownership=system options
                   0

               metadata channel
                   0

           --watchdog-timer=PERIODUS
               Set the period of the watchdog timer of the channel to
               PERIODUS µs.

               Set PERIODUS to 0 to disable the watchdog timer.

               You may only use this option with the --userspace and
               --buffer-ownership=user options.

               Default value: 2000000.

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

           Example 1. Create a Linux kernel channel with default attributes
           in the current recording session.

               The following command line only creates a new channel if my-
               channel doesn’t name an existing Linux kernel channel in the
               current recording session.

                   $ lttng enable-channel --kernel my-channel

           Example 2. Create a user space channel with a per-process buffer
           ownership model in a specific recording session.

               See the --session and --buffer-ownership options.

                   $ lttng enable-channel --session=my-session --userspace \
                                          --buffer-ownership=process my-channel

           Example 3. Create a user space channel with a per-user buffer
           ownership model (default) and a per-channel buffer allocation
           policy.

               See the --buffer-allocation option.

                   $ lttng enable-channel --userspace \
                                          --buffer-allocation=per-channel my-channel

           Example 4. Create a user space channel with an “on-demand”
           preallocation policy and an automatic memory reclaim.

               See the --buffer-preallocation and --auto-reclaim-memory
               options.

                   $ lttng enable-channel --userspace my-channel \
                                          --buffer-preallocation=on-demand \
                                          --auto-reclaim-memory=older-than:30s

           Example 5. Create a Linux kernel channel in the current recording
           session with four 32-MiB sub-buffers per ring buffer.

               See the --num-subbuf and --subbuf-size options.

                   $ lttng enable-channel --kernel my-channel \
                                          --num-subbuf=4 --subbuf-size=32M

           Example 6. Create a user space channel in the current recording
           session with trace file rotation.

               See the --tracefile-count and --tracefile-size options.

                   $ lttng enable-channel --userspace my-channel \
                                          --tracefile-count=16 --tracefile-size=8M

           Example 7. Enable two user space channels of a specific recording
           session.

                   $ lttng enable-channel --session=my-session --userspace \
                                          canal-d,rds

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

           lttng(1), lttng-disable-channel(1), lttng-list(1),
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

    LTTng 2.15.1                 18 December 2025       LTTNG-ENABLE-CHANN(1)

------------------------------------------------------------------------

Pages that refer to this page: [lttng(1)](../man1/lttng.1.html),  [lttng-add-context(1)](../man1/lttng-add-context.1.html),  [lttng-add-trigger(1)](../man1/lttng-add-trigger.1.html),  [lttng-create(1)](../man1/lttng-create.1.html),  [lttng-disable-channel(1)](../man1/lttng-disable-channel.1.html),  [lttng-enable-event(1)](../man1/lttng-enable-event.1.html),  [lttng-enable-rotation(1)](../man1/lttng-enable-rotation.1.html),  [lttng-list(1)](../man1/lttng-list.1.html),  [lttng-reclaim-memory(1)](../man1/lttng-reclaim-memory.1.html),  [lttng-regenerate(1)](../man1/lttng-regenerate.1.html),  [lttng-status(1)](../man1/lttng-status.1.html),  [lttng-ust(3)](../man3/lttng-ust.3.html),  [lttng-concepts(7)](../man7/lttng-concepts.7.html)

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
