---
{"title": "lttng-concepts(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/lttng-concepts.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lttng-concepts(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INSTRUMENTATION POINT, EVENT RULE, AND EVENT](#INSTRUMENTATION_POINT,_EVENT_RULE,_AND_EVENT) \| [TRIGGER](#TRIGGER) \| [RECORDING SESSION](#RECORDING_SESSION) \| [TRACING DOMAIN](#TRACING_DOMAIN) \| [CHANNEL AND RING BUFFER](#CHANNEL_AND_RING_BUFFER) \| [RECORDING EVENT RULE AND EVENT RECORD](#RECORDING_EVENT_RULE_AND_EVENT_RECORD) \| [RESOURCES](#RESOURCES) \| [COPYRIGHT](#COPYRIGHT) \| [THANKS](#THANKS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LTTNG-CONCEPTS(7)              LTTng Manual             LTTNG-CONCEPTS(7)

## [](#NAME)NAME

           lttng-concepts - LTTng concepts

## [](#DESCRIPTION)DESCRIPTION

           This manual page documents the concepts of LTTng.

           Many other LTTng manual pages refer to this one so that you can
           understand what are the various LTTng objects and how they relate
           to each other.

           The concepts of LTTng 2.15.1 are:

           •   Instrumentation point, event rule, and event

           •   Trigger

           •   Recording session

           •   Tracing domain

           •   Channel and ring buffer

           •   Recording event rule and event record

## [](#INSTRUMENTATION_POINT,_EVENT_RULE,_AND_EVENT)INSTRUMENTATION POINT, EVENT RULE, AND EVENT

           An instrumentation point is a point, within a piece of software,
           which, when executed, creates an LTTng event.

           LTTng offers various types of instrumentation; see the
           “Instrumentation point types” section below to learn about them.

           An event rule is a set of conditions to match a set of events.

           When LTTng creates an event E, an event rule ER is said to match E
           when E satisfies all the conditions of ER. This concept is similar
           to a regular expression which matches a set of strings.

           When an event rule matches an event, LTTng emits the event,
           therefore attempting to execute one or more actions.

           Important

               The event creation and emission processes are documentation
               concepts to help understand the journey from an
               instrumentation point to the execution of actions.

               The actual creation of an event can be costly because LTTng
               needs to evaluate the arguments of the instrumentation point.

               In practice, LTTng implements various optimizations for the
               Linux kernel and user space tracing domains (see the “TRACING
               DOMAIN” section below) to avoid actually creating an event
               when the tracer knows, thanks to properties which are
               independent from the event payload and current context, that
               it would never emit such an event. Those properties are:

               •   The instrumentation point type (see the “Instrumentation
                   point types” section below).

               •   The instrumentation point name.

               •   The instrumentation point log level.

               •   For a recording event rule (see the “RECORDING EVENT RULE
                   AND EVENT RECORD” section below):

                   •   The status of the rule itself.

                   •   The status of the channel (see the “CHANNEL AND RING
                       BUFFER” section below).

                   •   The activity of the recording session (started or
                       stopped; see the “RECORDING SESSION” section below).

                   •   Whether or not the process for which LTTng would
                       create the event is allowed to record events (see
                       lttng-track(1)).

               In other words: if, for a given instrumentation point IP, the
               LTTng tracer knows that it would never emit an event,
               executing IP represents a simple boolean variable check and,
               for a Linux kernel recording event rule, a few process
               attribute checks.

           As of LTTng 2.15.1, there are two places where you can find an
           event rule:

           Recording event rule
               A specific type of event rule of which the action is to record
               the matched event as an event record.

               See the “RECORDING EVENT RULE AND EVENT RECORD” section below.

               Create or enable a recording event rule with the
               lttng-enable-event(1) command.

               List the recording event rules of a specific recording session
               and/or channel with the lttng-list(1) and lttng-status(1)
               commands.

           “Event rule matches” trigger condition (since LTTng 2.13)
               When the event rule of the trigger condition matches an event,
               LTTng can execute user-defined actions such as sending an
               LTTng notification, starting a recording session, and more.

               See lttng-add-trigger(1) and lttng-event-rule(7).

           For LTTng to emit an event E, E must satisfy all the basic
           conditions of an event rule ER, that is:

           •   The instrumentation point from which LTTng creates E has a
               specific type.

               See the “Instrumentation point types” section below.

           •   A pattern matches the name of E while another pattern doesn’t.

           •   The log level of the instrumentation point from which LTTng
               creates E is at least as severe as some value, or is exactly
               some value.

           •   The fields of the payload of E and the current context fields
               satisfy a filter expression.

           A recording event rule has additional, implicit conditions to
           satisfy. See the “RECORDING EVENT RULE AND EVENT RECORD” section
           below to learn more.

       Instrumentation point types
           As of LTTng 2.15.1, the available instrumentation point types are,
           depending on the tracing domain (see the “TRACING DOMAIN” section
           below):

           Linux kernel

               LTTng tracepoint
                   A statically defined point in the source code of the
                   kernel image or of a kernel module using the LTTng-modules
                   macros.

                   List the available Linux kernel tracepoints with lttng
                   list --kernel. See lttng-list(1) to learn more.

               Linux kernel system call
                   Entry, exit, or both of a Linux kernel system call.

                   List the available Linux kernel system call
                   instrumentation points with lttng list --kernel --syscall.
                   See lttng-list(1) to learn more.

               Linux kprobe
                   A single probe dynamically placed in the compiled kernel
                   code.

                   When you create such an instrumentation point, you set its
                   memory address or symbol name.

               Linux user space probe
                   A single probe dynamically placed at the entry of a
                   compiled user space application/library function through
                   the kernel.

                   When you create such an instrumentation point, you set:

                   With the ELF method
                       Its application/library path and its symbol name.

                   With the USDT method
                       Its application/library path, its provider name, and
                       its probe name.

                       “USDT” stands for SystemTap User-level Statically
                       Defined Tracing, a DTrace-style marker.

                   As of LTTng 2.15.1, LTTng only supports USDT probes which
                   are NOT reference-counted.

               Linux kretprobe
                   Entry, exit, or both of a Linux kernel function.

                   When you create such an instrumentation point, you set the
                   memory address or symbol name of its function.

           User space

               LTTng tracepoint
                   A statically defined point in the source code of a C/C++
                   application/library using the LTTng-UST macros.

                   List the available Linux kernel tracepoints with lttng
                   list --userspace. See lttng-list(1) to learn more.

           java.util.logging, Apache log4j 1.x, Apache Log4j 2, and Python

               Java or Python logging statement
                   A method call on a Java or Python logger attached to an
                   LTTng-UST handler.

                   List the available Java and Python loggers with lttng list
                   --jul, lttng list --log4j, lttng list --log4j2, and lttng
                   list --python. See lttng-list(1) to learn more.

## [](#TRIGGER)TRIGGER

           A trigger associates a condition to one or more actions.

           When the condition of a trigger is satisfied, LTTng attempts to
           execute its actions.

           As of LTTng 2.15.1, the available trigger conditions and actions
           are:

           Conditions

               •   The consumed buffer size of a given recording session (see
                   the “RECORDING SESSION” section below) becomes greater
                   than some value.

               •   The buffer usage of a given channel (see the “CHANNEL AND
                   RING BUFFER” section below) becomes greater than some
                   value.

               •   The buffer usage of a given channel becomes less than some
                   value.

               •   There’s an ongoing recording session rotation (see the
                   “Recording session rotation” section below).

               •   A recording session rotation becomes completed.

               •   An event rule matches an event.

                   As of LTTng 2.15.1, this is the only available condition
                   when you add a trigger with the lttng-add-trigger(1)
                   command. The other ones are available through the
                   liblttng-ctl C API.

           Actions

               •   Send a notification to a user application.

               •   Start a given recording session, like lttng-start(1) would
                   do.

               •   Stop a given recording session, like lttng-stop(1) would
                   do.

               •   Archive the current trace chunk of a given recording
                   session (rotate), like lttng-rotate(1) would do.

               •   Take a snapshot of a given recording session, like
                   lttng-snapshot(1) would do.

           A trigger belongs to a session daemon (see lttng-sessiond(8)), not
           to a specific recording session. For a given session daemon, each
           Unix user has its own, private triggers. Note, however, that the
           root Unix user may, for the root session daemon:

           •   Add a trigger as another Unix user.

           •   List all the triggers, regardless of their owner.

           •   Remove a trigger which belongs to another Unix user.

           For a given session daemon and Unix user, a trigger has a unique
           name.

           Add a trigger to a session daemon with the lttng-add-trigger(1)
           command.

           List the triggers of your Unix user (or of all users if your Unix
           user is root) with the lttng-list-triggers(1) command.

           Remove a trigger with the lttng-remove-trigger(1) command.

## [](#RECORDING_SESSION)RECORDING SESSION

           A recording session (named “tracing session” prior to LTTng 2.13)
           is a stateful dialogue between you and a session daemon (see
           lttng-sessiond(8)) for everything related to event recording.

           Everything that you do when you control LTTng tracers to record
           events happens within a recording session. In particular, a
           recording session:

           •   Has its own name, unique for a given session daemon.

           •   Has its own set of trace files, if any.

           •   Has its own state of activity (started or stopped).

               An active recording session is an implicit recording event
               rule condition (see the “RECORDING EVENT RULE AND EVENT
               RECORD” section below).

           •   Has its own mode (local, network streaming, snapshot, or
               live).

               See the “Recording session modes” section below to learn more.

           •   Has its own channels (see the “CHANNEL AND RING BUFFER”
               section below) to which are attached their own recording event
               rules.

           •   Has its own process attribute inclusion sets (see
               lttng-track(1)).

           Those attributes and objects are completely isolated between
           different recording sessions.

           A recording session is like an ATM session: the operations you do
           on the banking system through the ATM don’t alter the data of
           other users of the same system. In the case of the ATM, a session
           lasts as long as your bank card is inside. In the case of LTTng, a
           recording session lasts from the lttng-create(1) command to the
           lttng-destroy(1) command.

           A recording session belongs to a session daemon (see
           lttng-sessiond(8)). For a given session daemon, each Unix user has
           its own, private recording sessions. Note, however, that the root
           Unix user may operate on or destroy another user’s recording
           session.

           Create a recording session with the lttng-create(1) command.

           List the recording sessions of the connected session daemon with
           the lttng-list(1) command.

           Start and stop one or more recording session with the
           lttng-start(1) and lttng-stop(1) commands.

           Save and load a recording session with the lttng-save(1) and
           lttng-load(1) commands.

           Archive the current trace chunk of (rotate) a recording session
           with the lttng-rotate(1) command.

           Destroy one or more recording sessions with the lttng-destroy(1)
           command.

       Current recording session
           When you run the lttng-create(1) command, LTTng creates the
           $LTTNG_HOME/.lttngrc file if it doesn’t exist ($LTTNG_HOME
           defaults to $HOME).

           $LTTNG_HOME/.lttngrc contains the name of the current recording
           session.

           When you create a new recording session with the create command,
           LTTng updates the current recording session.

           The following lttng(1) commands select the current recording
           session if you don’t specify one:

           •   lttng-add-context(1)

           •   lttng-clear(1)

           •   lttng-destroy(1)

           •   lttng-disable-channel(1)

           •   lttng-disable-event(1)

           •   lttng-disable-rotation(1)

           •   lttng-enable-channel(1)

           •   lttng-enable-event(1)

           •   lttng-enable-rotation(1)

           •   lttng-regenerate(1)

           •   lttng-reclaim-memory(1)

           •   lttng-rotate(1)

           •   lttng-save(1)

           •   lttng-snapshot(1)

           •   lttng-start(1)

           •   lttng-status(1)

           •   lttng-stop(1)

           •   lttng-track(1)

           •   lttng-untrack(1)

           •   lttng-view(1)

           Set the current recording session manually with the
           lttng-set-session(1) command, without having to edit the .lttngrc
           file.

       Recording session modes
           LTTng offers four recording session modes:

           Local mode
               Write the trace data to the local file system.

           Network streaming mode
               Send the trace data over the network to a listening relay
               daemon (see lttng-relayd(8)).

           Snapshot mode
               Only write the trace data to the local file system or send it
               to a listening relay daemon (lttng-relayd(8)) when LTTng takes
               a snapshot.

               LTTng forces all the channels (see the “CHANNEL AND RING
               BUFFER” section below) to be created to be configured to be
               snapshot-ready.

               LTTng takes a snapshot of such a recording session when any of
               the following is true:

               •   You run the lttng-snapshot(1) command.

               •   LTTng executes a snapshot-session trigger action (see the
                   “TRIGGER” section above).

           Live mode
               Send the trace data over the network to a listening relay
               daemon (see lttng-relayd(8)) for live reading.

               An LTTng live reader (for example, babeltrace2(1)) can connect
               to the same relay daemon to receive trace data while the
               recording session is active.

       Recording session rotation
           A recording session rotation is the action of archiving the
           current trace chunk of the recording session to the file system.

           Once LTTng archives a trace chunk, it does NOT manage it anymore:
           you can read it, modify it, move it, or remove it.

           An archived trace chunk is a collection of metadata and data
           stream files which form a self-contained LTTng trace. See the
           “Trace chunk naming” section below to learn how LTTng names a
           trace chunk archive directory.

           The current trace chunk of a given recording session includes:

           •   The stream files which LTTng already wrote to the file system,
               and which are not part of a previously archived trace chunk,
               since the most recent event amongst:

               •   The first time the recording session was started, either
                   with the lttng-start(1) command or with a start-session
                   trigger action (see the “TRIGGER” section above).

               •   The last rotation, performed with:

                   •   An lttng-rotate(1) command.

                   •   A rotation schedule previously set with
                       lttng-enable-rotation(1).

                   •   An executed rotate-session trigger action (see the
                       “TRIGGER” section above).

           •   The content of all the non-flushed sub-buffers of the channels
               of the recording session.

       Trace chunk archive naming
           A trace chunk archive is a subdirectory of the archives
           subdirectory within the output directory of a recording session
           (see the --output option of the lttng-create(1) command and of
           lttng-relayd(8)).

           A trace chunk archive contains, through tracing domain and
           possibly UID/PID subdirectories, metadata and data stream files.

           A trace chunk archive is, at the same time:

           •   A self-contained LTTng trace.

           •   A member of a set of trace chunk archives which form the
               complete trace of a recording session.

           In other words, an LTTng trace reader can read both the recording
           session output directory (all the trace chunk archives), or a
           single trace chunk archive.

           When LTTng performs a recording session rotation, it names the
           resulting trace chunk archive as such, relative to the output
           directory of the recording session:

               archives/BEGIN-END-ID

           BEGIN
               Date and time of the beginning of the trace chunk archive with
               the ISO 8601-compatible YYYYmmddTHHMMSS±HHMM form, where
               YYYYmmdd is the date and HHMMSS±HHMM is the time with the time
               zone offset from UTC.

               Example: 20171119T152407-0500

           END
               Date and time of the end of the trace chunk archive with the
               ISO 8601-compatible YYYYmmddTHHMMSS±HHMM form, where YYYYmmdd
               is the date and HHMMSS±HHMM is the time with the time zone
               offset from UTC.

               Example: 20180118T152407+0930

           ID
               Unique numeric identifier of the trace chunk within its
               recording session.

           Trace chunk archive name example:

               archives/20171119T152407-0500-20171119T151422-0500-3

## [](#TRACING_DOMAIN)TRACING DOMAIN

           A tracing domain identifies a type of LTTng tracer.

           A tracing domain has its own properties and features.

           There are currently five available tracing domains:
           ┌───────────────────┬────────────────────┬──────────────────┐
           │ Tracing domain    │ “Event rule        │ Option for other │
           │                   │ matches” trigger   │ CLI commands     │
           │                   │ condition option   │                  │
           ├───────────────────┼────────────────────┼──────────────────┤
           │                   │                    │                  │
           │ Linux kernel      │ --type option      │ --kernel         │
           │                   │ starts with        │                  │
           │                   │ kernel:            │                  │
           ├───────────────────┼────────────────────┼──────────────────┤
           │                   │                    │                  │
           │ User space        │ --type option      │ --userspace      │
           │                   │ starts with user:  │                  │
           ├───────────────────┼────────────────────┼──────────────────┤
           │                   │                    │                  │
           │ java.util.logging │ --type option      │ --jul            │
           │ (JUL)             │ starts with jul:   │                  │
           ├───────────────────┼────────────────────┼──────────────────┤
           │                   │                    │                  │
           │ Apache log4j 1.x  │ --type option      │ --log4j          │
           │                   │ starts with log4j: │                  │
           ├───────────────────┼────────────────────┼──────────────────┤
           │                   │                    │                  │
           │ Apache Log4j 2    │ --type option      │ --log4j2         │
           │                   │ starts with        │                  │
           │                   │ log4j2:            │                  │
           ├───────────────────┼────────────────────┼──────────────────┤
           │                   │                    │                  │
           │ Python            │ --type option      │ --python         │
           │                   │ starts with        │                  │
           │                   │ python:            │                  │
           └───────────────────┴────────────────────┴──────────────────┘

           You must specify a tracing domain to target a type of LTTng tracer
           when using some lttng(1) commands to avoid ambiguity. For example,
           because the Linux kernel and user space tracing domains support
           named tracepoints as instrumentation points (see the
           “INSTRUMENTATION POINT, EVENT RULE, AND EVENT” section above), you
           need to specify a tracing domain when you create an event rule
           because both tracing domains could have tracepoints sharing the
           same name.

           You can create channels (see the “CHANNEL AND RING BUFFER” section
           below) in the Linux kernel and user space tracing domains. The
           other tracing domains have a single, default channel.

## [](#CHANNEL_AND_RING_BUFFER)CHANNEL AND RING BUFFER

           A channel is an object which is responsible for a set of ring
           buffers.

           Each ring buffer is divided into multiple sub-buffers. When a
           recording event rule (see the “RECORDING EVENT RULE AND EVENT
           RECORD” section below) matches an event, LTTng can record it to
           one or more sub-buffers of one or more channels.

           When you create a channel with the lttng-enable-channel(1)
           command, you set its final attributes, that is:

           •   Its buffering scheme.

               See the “Buffering scheme” section below.

           •   Its buffer preallocation policy.

               See the “Buffering preallocation policy” section below.

           •   Its automatic memory reclaim policy.

               See the “Memory reclaim” section below.

           •   What to do when there’s no space left for a new event record
               because all sub-buffers are full.

               See the “Event record loss mode” section below.

           •   The size of each ring buffer and how many sub-buffers a ring
               buffer has.

               See the “Sub-buffer size and count” section below.

           •   The size of each trace file LTTng writes for this channel and
               the maximum count of trace files.

               See the “Maximum trace file size and count” section below.

           •   The periods of its read, switch, monitor, and watchdog timers.

               See the “Timers” section below.

           •   For a Linux kernel channel: its output type (mmap(2) or
               splice(2)).

               See the --output option of the lttng-enable-channel(1)
               command.

           •   For a user space channel: the value of its blocking timeout.

               See the --blocking-timeout option of the
               lttng-enable-channel(1) command.

           Note that the lttng-enable-event(1) command can automatically
           create a default channel with sane defaults when no channel exists
           for the provided tracing domain.

           A channel is always associated to a tracing domain (see the
           “TRACING DOMAIN” section below). The java.util.logging (JUL),
           Apache log4j 1.x, Apache Log4j 2, and Python tracing domains each
           have a default channel which you can’t configure.

           A channel owns recording event rules.

           List the channels of a given recording session with the
           lttng-list(1) and lttng-status(1) commands.

           Disable an enabled channel with the lttng-disable-channel(1)
           command.

       Buffering scheme
           The buffering scheme of a channel is:

           •   The buffer ownership model: specifies whether the system, each
               Unix user, or each process owns its own ring buffers.

           •   The buffer allocation policy: specifies whether LTTng tracers
               allocate ring buffers per channel or per CPU.

           The following list shows how LTTng allocates ring buffers based on
           the values of the --buffer-ownership and --buffer-allocation
           options of the lttng-enable-channel(1) command. For all examples,
           assume that Unix user alice created the channel alice-chan and
           Unix user bob created the channel bob-chan:

           --buffer-ownership=user and --buffer-allocation=per-cpu

                   Channel alice-channel
                     For the data produced by any process of user alice
                       Ring buffer for CPU 0
                       Ring buffer for CPU 1
                       Ring buffer for CPU 2
                       Ring buffer for CPU 3
                   Channel bob-channel
                     For the data produced by any process of user bob
                       Ring buffer for CPU 0
                       Ring buffer for CPU 1
                       Ring buffer for CPU 2
                       Ring buffer for CPU 3

           --buffer-ownership=process and --buffer-allocation=per-cpu

                   Channel alice-channel
                     For the data produced by process my-db of user alice
                       Ring buffer for CPU 0
                       Ring buffer for CPU 1
                       Ring buffer for CPU 2
                       Ring buffer for CPU 3
                     For the data produced by process my-app of user alice
                       Ring buffer for CPU 0
                       Ring buffer for CPU 1
                       Ring buffer for CPU 2
                       Ring buffer for CPU 3
                   Channel bob-channel
                     For the data produced by process my-server of user bob
                       Ring buffer for CPU 0
                       Ring buffer for CPU 1
                       Ring buffer for CPU 2
                       Ring buffer for CPU 3

           --buffer-ownership=system and --buffer-allocation=per-cpu

                   Channel alice-channel
                     For the data of the Linux kernel
                       Ring buffer for CPU 0
                       Ring buffer for CPU 1
                       Ring buffer for CPU 2
                       Ring buffer for CPU 3
                   Channel bob-channel
                     For the data of the Linux kernel
                       Ring buffer for CPU 0
                       Ring buffer for CPU 1
                       Ring buffer for CPU 2
                       Ring buffer for CPU 3

           --buffer-ownership=user and --buffer-allocation=per-channel

                   Channel alice-channel
                     For the data produced by any process of user alice
                       Single ring buffer for all CPUs
                   Channel bob-channel
                     For the data produced by any process of user bob
                       Single ring buffer for all CPUs

           --buffer-ownership=user and --buffer-allocation=per-channel

                   Channel alice-channel
                     For the data produced by process my-db of user alice
                       Single ring buffer for all CPUs
                     For the data produced by process my-app of user alice
                       Single ring buffer for all CPUs
                   Channel bob-channel
                     For the data produced by process my-server of user bob
                       Single ring buffer for all CPUs

           The per-process buffer ownership model tends to consume more
           memory than the per-user option because systems generally have
           more instrumented processes than Unix users running instrumented
           processes. However, the per-process model ensures that one process
           having a high event throughput won’t fill all the shared
           sub-buffers of the same Unix user, only its own. It also provides
           complete isolation between processes: one process cannot read or
           corrupt the trace data of another.

       Buffer preallocation policy
           The buffer preallocation policy of a user space channel specifies
           when LTTng allocates the backing memory for the ring buffers of
           the channel.

           The available buffer preallocation policies are:

           Preallocate
               LTTng allocates the full backing memory for all ring buffers
               when you create the channel.

               This policy provides consistent performance but uses more
               memory upfront. Use this policy to optimize instrumented
               application startup time.

           On demand
               LTTng allocates backing memory for ring buffers incrementally,
               as needed during tracing.

               This policy uses less initial memory but may introduce slight
               performance overhead when allocating new memory during
               tracing.

           As of LTTng 2.15.1, the implicit buffer preallocation policy of a
           Linux kernel channel is always to preallocate backing memory.

           Set the buffer preallocation policy of a user space channel with
           the --buffer-preallocation option of the lttng-enable-channel(1)
           command.

       Memory reclaim
           A channel memory reclaim operation makes it possible to free
           memory which the eligible sub-buffers of a user space channel use.

           The channel memory reclaim operation behaviour depends on the
           configured event record loss mode (see the “Event record loss
           mode” section below) of the channel:

           Discard mode
               Only reclaim sub-buffers that have been both delivered
               (completed and ready to be consumed) and consumed, since
               unconsumed data would be lost forever.

           Overwrite mode
               Reclaim any delivered sub-buffer, since old data will be
               overwritten anyway: no need to wait for consumption.

           There are two ways to reclaim channel memory:

           Immediate reclaim
               Use the lttng-reclaim-memory(1) command.

           Automatic reclaim
               LTTng may automatically reclaim the memory of a user space
               channel.

               This is more or less equivalent to automatically running the
               lttng-reclaim-memory(1) command. LTTng automatically evaluates
               the eligibility of sub-buffers for a memory reclaim operation
               at regular intervals (every half the configured maximal age,
               but also at least a period defined at build time) and reclaims
               sub-buffers of which the age of the closing time have exceeded
               the age threshold.

               Use the --auto-reclaim-memory-older-than option of the
               lttng-enable-channel(1) command.

           In both cases, you may specify a sub-buffer age threshold: only
           sub-buffers of which the age of the closing time is older than the
           threshold are eligible for a memory reclaim. Moreover, with some
           age threshold T:

           If T > last stream activity age
               The sub-buffers of which the age, at the moment of closing
               them, is greater than T are eligible for a memory reclaim.

           If T < last stream activity age
               All the sub-buffers are eligible.

               The LTTng tracers flush for the targeted channel so that any
               open sub-buffer gets closed to become eligible.

       Event record loss mode
           When LTTng emits an event, LTTng can record it to a specific,
           available sub-buffer within the ring buffers of specific channels.
           When there’s no space left in a sub-buffer, the tracer marks it as
           consumable and another, available sub-buffer starts receiving the
           following event records. An LTTng consumer daemon eventually
           consumes the marked sub-buffer, which returns to the available
           state.

           In an ideal world, sub-buffers are consumed faster than they are
           filled. In the real world, however, all sub-buffers can be full at
           some point, leaving no space to record the following events.

           By default, LTTng-modules and LTTng-UST are non-blocking tracers:
           when there’s no available sub-buffer to record an event, it’s
           acceptable to lose event records when the alternative would be to
           cause substantial delays in the execution of the instrumented
           application. LTTng privileges performance over integrity; it aims
           at perturbing the instrumented application as little as possible
           in order to make the detection of subtle race conditions and rare
           interrupt cascades possible.

           Since LTTng 2.10, the LTTng user space tracer, LTTng-UST, supports
           a blocking mode. See the --blocking-timeout of the
           lttng-enable-channel(1) command to learn how to use the blocking
           mode.

           When it comes to losing event records because there’s no available
           sub-buffer, or because the blocking timeout of the channel is
           reached, the event record loss mode of the channel determines what
           to do. The available event record loss modes are:

           Discard mode
               Drop the newest event records until a sub-buffer becomes
               available.

               This is the only available mode when you specify a blocking
               timeout.

               With this mode, LTTng increments a count of lost event records
               when an event record is lost and saves this count to the
               trace. A trace reader can use the saved discarded event record
               count of the trace to decide whether or not to perform some
               analysis even if trace data is known to be missing.

           Overwrite mode
               Clear the sub-buffer containing the oldest event records and
               start writing the newest event records there.

               This mode is sometimes called flight recorder mode because
               it’s similar to a flight recorder
               <https://en.wikipedia.org/wiki/Flight_recorder>: always keep a
               fixed amount of the latest data. It’s also similar to the roll
               mode of an oscilloscope.

               Since LTTng 2.8, with this mode, LTTng writes to a given
               sub-buffer its sequence number within its data stream. With a
               local, network streaming, or live recording session (see the
               “Recording session modes” section above), a trace reader can
               use such sequence numbers to report lost packets. A trace
               reader can use the saved discarded sub-buffer (packet) count
               of the trace to decide whether or not to perform some analysis
               even if trace data is known to be missing.

               With this mode, LTTng doesn’t write to the trace the exact
               number of lost event records in the lost sub-buffers.

           Which mechanism you should choose depends on your context:
           prioritize the newest or the oldest event records in the ring
           buffer?

           Beware that, in overwrite mode, the tracer abandons a whole
           sub-buffer as soon as a there’s no space left for a new event
           record, whereas in discard mode, the tracer only discards the
           event record that doesn’t fit.

           Set the event record loss mode of a channel with the --discard and
           --overwrite options of the lttng-enable-channel(1) command.

           There are a few ways to decrease your probability of losing event
           records. The “Sub-buffer size and count” section below shows how
           to fine-tune the sub-buffer size and count of a channel to
           virtually stop losing event records, though at the cost of greater
           memory usage.

       Sub-buffer size and count
           A channel has one or more ring buffer for each CPU of the target
           system.

           See the “Buffering scheme” section above to learn how many ring
           buffers of a given channel are dedicated to each CPU or to the
           whole channel depending on its buffering scheme.

           Set the size of each sub-buffer the ring buffers of a channel
           contain with the --subbuf-size option of the
           lttng-enable-channel(1) command.

           Set the number of sub-buffers each ring buffer of a channel
           contains with the --num-subbuf option of the
           lttng-enable-channel(1) command.

           Note that LTTng switching the current sub-buffer of a ring buffer
           (marking a full one as consumable and switching to an available
           one for LTTng to record the next events) introduces noticeable CPU
           overhead. Knowing this, the following list presents a few
           practical situations along with how to configure the sub-buffer
           size and count for them:

           High event throughput
               In general, prefer large sub-buffers to lower the risk of
               losing event records.

               Having larger sub-buffers also ensures a lower sub-buffer
               switching frequency (see the “Timers” section below).

               The sub-buffer count is only meaningful if you create the
               channel in overwrite mode (see the “Event record loss mode”
               section above): in this case, if LTTng overwrites a
               sub-buffer, then the other sub-buffers are left unaltered.

           Low event throughput
               In general, prefer smaller sub-buffers since the risk of
               losing event records is low.

               Because LTTng emits events less frequently, the sub-buffer
               switching frequency should remain low and therefore the
               overhead of the tracer shouldn’t be a problem.

           Low memory system
               If your target system has a low memory limit, prefer fewer
               first, then smaller sub-buffers.

               Even if the system is limited in memory, you want to keep the
               sub-buffers as large as possible to avoid a high sub-buffer
               switching frequency.

           Note that LTTng uses CTF <https://diamon.org/ctf/> as its trace
           format (see the --trace-format option of the lttng-create(1)
           command), which means event record data is very compact. For
           example, the average LTTng kernel event record weights about
           32 bytes. Therefore, a sub-buffer size of 1 MiB is considered
           large.

           The previous scenarios highlight the major trade-off between a few
           large sub-buffers and more, smaller sub-buffers: sub-buffer
           switching frequency vs. how many event records are lost in
           overwrite mode. Assuming a constant event throughput and using the
           overwrite mode, the two following configurations have the same
           ring buffer total size:

           Two sub-buffers of 4 MiB each
               Expect a very low sub-buffer switching frequency, but if LTTng
               ever needs to overwrite a sub-buffer, half of the event
               records so far (4 MiB) are definitely lost.

           Eight sub-buffers of 1 MiB each
               Expect four times the tracer overhead of the configuration
               above, but if LTTng needs to overwrite a sub-buffer, only the
               eighth of event records so far (1 MiB) are definitely lost.

           In discard mode, the sub-buffer count parameter is pointless: use
           two sub-buffers and set their size according to your requirements.

       Maximum trace file size and count
           By default, trace files can grow as large as needed.

           Set the maximum size of each trace file that LTTng writes of a
           given channel with the --tracefile-size option of the
           lttng-enable-channel(1) command.

           When the size of a trace file reaches the fixed maximum size of
           the channel, LTTng creates another file to contain the next event
           records. LTTng appends a file count to each trace file name in
           this case.

           If you set the trace file size attribute when you create a
           channel, the maximum number of trace files that LTTng creates is
           unlimited by default. To limit them, use the --tracefile-count
           option of lttng-enable-channel(1). When the number of trace files
           reaches the fixed maximum count of the channel, LTTng overwrites
           the oldest trace file. This mechanism is called trace file
           rotation.

           Important

               Even if you don’t limit the trace file count, always assume
               that LTTng manages all the trace files of the recording
               session.

               In other words, there’s no safe way to know if LTTng still
               holds a given trace file open with the trace file rotation
               feature.

               The only way to obtain an unmanaged, self-contained LTTng
               trace before you destroy the recording session is with the
               recording session rotation feature (see the “Recording session
               rotation” section above), which is available since LTTng 2.11.

       Timers
           Each channel can have up to three optional timers:

           Switch timer
               When this timer expires, a sub-buffer switch happens: for each
               ring buffer of the channel, LTTng marks the current sub-buffer
               as consumable and switches to an available one to record the
               next events.

               A switch timer is useful to ensure that LTTng consumes and
               commits trace data to trace files or to a distant relay daemon
               (lttng-relayd(8)) periodically in case of a low event
               throughput.

               Such a timer is also convenient when you use large sub-buffers
               (see the “Sub-buffer size and count” section above) to cope
               with a sporadic high event throughput, even if the throughput
               is otherwise low.

               Set the period of the switch timer of a channel, or disable
               the timer altogether, with the --switch-timer option of the
               lttng-enable-channel(1) command.

           Read timer
               When this timer expires, LTTng checks for full, consumable
               sub-buffers.

               By default, the LTTng tracers use an asynchronous message
               mechanism to signal a full sub-buffer so that a consumer
               daemon can consume it.

               When such messages must be avoided, for example in real-time
               applications, use this timer instead.

               Set the period of the read timer of a channel, or disable the
               timer altogether, with the --read-timer option of the
               lttng-enable-channel(1) command.

           Monitor timer
               When this timer expires, the consumer daemon samples some
               channel statistics to evaluate the following trigger
               conditions:

                1. The consumed buffer size of a given recording session
                   becomes greater than some value.

                2. The buffer usage of a given channel becomes greater than
                   some value.

                3. The buffer usage of a given channel becomes less than some
                   value.

               If you disable the monitor timer of a channel C:

               •   The consumed buffer size value of the recording session
                   of C could be wrong for trigger condition type 1: the
                   consumed buffer size of C won’t be part of the grand
                   total.

               •   The buffer usage trigger conditions (types 2 and 3) for C
                   will never be satisfied.

               See the “TRIGGER” section above to learn more about triggers.

               Set the period of the monitor timer of a channel, or disable
               the timer altogether, with the --monitor-timer option of the
               lttng-enable-channel(1) command.

           Watchdog timer
               When this timer expires, LTTng performs health checks that
               detect recoverable issues and trigger corrective actions to
               keep trace recording running smoothly for the channel.

               As of LTTng 2.15.1, the only health check is a sub-buffer
               stall detection: with a user space channel having a per-user
               ownership model (see the Buffering scheme section above), an
               instrumented application writing to a sub-buffer may crash and
               make said sub-buffer “stalled”, that is, never released and
               unusable. This can reduce the effective capacity of the
               channel or even halt the consumption altogether. When the
               watchdog timer of a channel expires and LTTng detects this
               condition, it marks the stalled sub-buffer consumable/readable
               again.

               Set the period of the watchdog timer of a channel, or disable
               the timer altogether, with the --watchdog-timer option of the
               lttng-enable-channel(1) command.

## [](#RECORDING_EVENT_RULE_AND_EVENT_RECORD)RECORDING EVENT RULE AND EVENT RECORD

           A recording event rule is a specific type of event rule (see the
           “INSTRUMENTATION POINT, EVENT RULE, AND EVENT” section above) of
           which the action is to serialize and record the matched event as
           an event record.

           Set the explicit conditions of a recording event rule when you
           create it with the lttng-enable-event(1) command. A recording
           event rule also has the following implicit conditions:

           •   The recording event rule itself is enabled.

               A recording event rule is enabled on creation.

           •   The channel to which the recording event rule is attached is
               enabled.

               A channel is enabled on creation.

               See the “CHANNEL AND RING BUFFER” section above.

           •   The recording session of the recording event rule is active
               (started).

               A recording session is inactive (stopped) on creation.

               See the “RECORDING SESSION” section above.

           •   The process for which LTTng creates an event to match is
               allowed to record events.

               All processes are allowed to record events on recording
               session creation.

               Use the lttng-track(1) and lttng-untrack(1) commands to select
               which processes are allowed to record events based on specific
               process attributes.

           You always attach a recording event rule to a channel, which
           belongs to a recording session, when you create it.

           When a recording event rule ER matches an event E, LTTng attempts
           to serialize and record E to one of the available sub-buffers of
           the channel to which E is attached.

           When multiple matching recording event rules are attached to the
           same channel, LTTng attempts to serialize and record the matched
           event once. In the following example, the second recording event
           rule is redundant when both are enabled:

               $ lttng enable-event --userspace hello:world
               $ lttng enable-event --userspace hello:world --loglevel=INFO

           List the recording event rules of a specific recording session
           and/or channel with the lttng-list(1) and lttng-status(1)
           commands.

           Disable a recording event rule with the lttng-disable-event(1)
           command.

           As of LTTng 2.15.1, you cannot remove a recording event rule: it
           exists as long as its recording session exists.

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

           lttng(1), lttng-relayd(8), lttng-sessiond(8)

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

    LTTng 2.15.1                 4 December 2025            LTTNG-CONCEPTS(7)

------------------------------------------------------------------------

Pages that refer to this page: [lttng(1)](../man1/lttng.1.html),  [lttng-add-context(1)](../man1/lttng-add-context.1.html),  [lttng-add-trigger(1)](../man1/lttng-add-trigger.1.html),  [lttng-clear(1)](../man1/lttng-clear.1.html),  [lttng-create(1)](../man1/lttng-create.1.html),  [lttng-destroy(1)](../man1/lttng-destroy.1.html),  [lttng-disable-channel(1)](../man1/lttng-disable-channel.1.html),  [lttng-disable-event(1)](../man1/lttng-disable-event.1.html),  [lttng-disable-rotation(1)](../man1/lttng-disable-rotation.1.html),  [lttng-enable-channel(1)](../man1/lttng-enable-channel.1.html),  [lttng-enable-event(1)](../man1/lttng-enable-event.1.html),  [lttng-enable-rotation(1)](../man1/lttng-enable-rotation.1.html),  [lttng-list(1)](../man1/lttng-list.1.html),  [lttng-list-triggers(1)](../man1/lttng-list-triggers.1.html),  [lttng-load(1)](../man1/lttng-load.1.html),  [lttng-metadata(1)](../man1/lttng-metadata.1.html),  [lttng-reclaim-memory(1)](../man1/lttng-reclaim-memory.1.html),  [lttng-regenerate(1)](../man1/lttng-regenerate.1.html),  [lttng-remove-trigger(1)](../man1/lttng-remove-trigger.1.html),  [lttng-rotate(1)](../man1/lttng-rotate.1.html),  [lttng-save(1)](../man1/lttng-save.1.html),  [lttng-set-session(1)](../man1/lttng-set-session.1.html),  [lttng-snapshot(1)](../man1/lttng-snapshot.1.html),  [lttng-start(1)](../man1/lttng-start.1.html),  [lttng-status(1)](../man1/lttng-status.1.html),  [lttng-stop(1)](../man1/lttng-stop.1.html),  [lttng-track(1)](../man1/lttng-track.1.html),  [lttng-untrack(1)](../man1/lttng-untrack.1.html),  [lttng-event-rule(7)](../man7/lttng-event-rule.7.html),  [lttng-sessiond(8)](../man8/lttng-sessiond.8.html)

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
