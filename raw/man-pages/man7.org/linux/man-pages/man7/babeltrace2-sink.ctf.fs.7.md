---
{"title": "babeltrace2-sink.ctf.fs(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/babeltrace2-sink.ctf.fs.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# babeltrace2-sink.ctf.fs(7) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INITIALIZATION PARAMETERS](#INITIALIZATION_PARAMETERS) \| [PORTS](#PORTS) \| [BUGS](#BUGS) \| [RESOURCES](#RESOURCES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BABELTRACE2-SINK.(7)       Babeltrace 2 manual       BABELTRACE2-SINK.(7)

## [](#NAME)NAME

           babeltrace2-sink.ctf.fs - Babeltrace 2: File system CTF sink
           component class

## [](#DESCRIPTION)DESCRIPTION

           A Babeltrace 2 sink.ctf.fs component writes the messages it
           consumes to one or more CTF (see <https://diamon.org/ctf/>) 1.8 or
           CTF 2 traces on the file system.

                           +-------------+
                           | sink.ctf.fs |
                           |             +--> CTF trace(s) on
               Messages -->@ in          |    the file system
                           +-------------+

           See babeltrace2-intro(7) to learn more about the Babeltrace 2
           project and its core concepts.

           The ctf-version parameter controls the CTF version of the
           resulting traces.

           As of this version, a sink.ctf.fs component may only write:

           CTF 1.8 traces
               When working under version 0 of the Message Interchange
               Protocol (MIP).

           CTF 2 traces
               When working under version 1 of the MIP.

           Therefore, the "get supported MIP versions" method of a
           sink.ctf.fs component class reports to support only MIP 0 with the
           ctf-version parameter set to 1 and only MIP 1 with ctf-version set
           to 2.

           A sink.ctf.fs component doesn’t merge traces: it writes the
           messages of different input traces to different output traces.

       Trace IR to CTF 1.8 translation
           A sink.ctf.fs component makes a best effort to write CTF 1.8
           traces that are semantically equivalent to the input traces. As of
           this version, with the ctf-version parameter set to 1, the
           following field class translations can occur:

           •   The component translates a boolean field class to a CTF
               unsigned 8-bit integer field class.

               The value of the unsigned integer field is 0 when the value of
               the boolean field is false and 1 when it’s true.

           •   The component translates a bit array field to a CTF unsigned
               integer field class having the same length.

           •   The component translates an option field class to a CTF
               variant field class where the options are an empty structure
               field class and the optional field class itself.

               The empty structure field is selected when the option field
               has no field.

           In all the cases above, the component adds a comment in the
           metadata stream, above the field class, to indicate that a special
           translation occurred.

           The component doesn’t translate any user attribute: a CTF 1.8
           metadata stream has no way to represent them.

       Trace IR to CTF 2 translation
           As of this version, with the ctf-version parameter set to 2:

           •   The component sets the sink.ctf.fs attribute, under the
               babeltrace.org,2020 namespace, of the preamble fragment to
               true.

           •   The structure member class names of packet context field
               classes having a CTF 2 role have the metadata stream UUID as a
               prefix to avoid clashes with user member classes.

               For example, the packet content length member class could be
               named afe9ed0e-ce73-413f-8956-83663bab2047-content_size.

           •   The component translates an event class log level to the log-
               level attribute under the babeltrace.org,2020 namespace as
               such:

               BT_EVENT_CLASS_LOG_LEVEL_EMERGENCY
                   "emergency"

               BT_EVENT_CLASS_LOG_LEVEL_ALERT
                   "alert"

               BT_EVENT_CLASS_LOG_LEVEL_CRITICAL
                   "critical"

               BT_EVENT_CLASS_LOG_LEVEL_ERROR
                   "error"

               BT_EVENT_CLASS_LOG_LEVEL_WARNING
                   "warning"

               BT_EVENT_CLASS_LOG_LEVEL_NOTICE
                   "notice"

               BT_EVENT_CLASS_LOG_LEVEL_INFO
                   "info"

               BT_EVENT_CLASS_LOG_LEVEL_DEBUG_SYSTEM
                   "debug:system"

               BT_EVENT_CLASS_LOG_LEVEL_DEBUG_PROGRAM
                   "debug:program"

               BT_EVENT_CLASS_LOG_LEVEL_DEBUG_PROCESS
                   "debug:process"

               BT_EVENT_CLASS_LOG_LEVEL_DEBUG_MODULE
                   "debug:module"

               BT_EVENT_CLASS_LOG_LEVEL_DEBUG_UNIT
                   "debug:unit"

               BT_EVENT_CLASS_LOG_LEVEL_DEBUG_FUNCTION
                   "debug:function"

               BT_EVENT_CLASS_LOG_LEVEL_DEBUG_LINE
                   "debug:line"

               BT_EVENT_CLASS_LOG_LEVEL_DEBUG
                   "debug:debug"

           •   The component translates an event class EMF URI to the emf-uri
               attribute under the babeltrace.org,2020 namespace as a JSON
               string.

           •   When the component needs to generate a length/selector field
               class F for dynamic field classes without a length/selector
               field:

               •   The structure member name of F is unspecified.

               •   F contains the attribute is-key-only, under the
                   babeltrace.org,2020 namespace, set to true.

           •   The component doesn’t translate trace and stream user
               attributes: a CTF 2 metadata stream has no way to represent
               them.

       Input message constraints
           Because of limitations in CTF regarding how discarded events and
           packets are encoded:

           •   If a stream class supports discarded events and the ignore-
               discarded-events parameter is NOT true:

               •   The stream class must support packets.

               •   Discarded events messages must have times.

               •   Any discarded events message must occur between a packet
                   end and a packet beginning message.

               •   The beginning time of a discarded events message must be
                   the same as the time of the last packet end message.

               •   The end time of a discarded events message must be the
                   same as the time of the next packet end message.

               •   Time ranges of discarded events messages must not overlap.

           •   If a stream class supports discarded packets and the ignore-
               discarded-packets parameter is NOT true:

               •   The stream class must support packets.

               •   Discarded packets messages must have times.

               •   The beginning time of a discarded events message must be
                   the same as the time of the last packet end message.

               •   The end time of a discarded events message must be the
                   same as the time of the next packet beginning message.

               •   Time ranges of discarded packets messages must not
                   overlap.

           The messages which a source.ctf.fs component creates satisfy all
           the requirements above.

           If a discarded events or packets message has no events/packets
           count, then the sink.ctf.fs component adds 1 to the counter of the
           corresponding CTF stream.

       Alignment and byte order
           A sink.ctf.fs component always aligns data fields as such:

           Fixed-length bit array fields with a size which isn’t a multiple
           of 8
               1-bit.

           All other scalar fields (fixed-length bit array, null-terminated
           string, BLOB)
               8-bit.

           The component writes fields using the native byte order of the
           machine. As of this version, there’s no way to force a custom byte
           order.

       Output path
           The path of a CTF trace is the directory which directly contains
           the metadata and data stream files.

           The current strategy to build a path in which to write the streams
           of a given input trace is, in this order:

            1. If the assume-single-trace parameter is true, then the output
               trace path to use for the single input trace is the directory
               specified by the path parameter.

            2. If the component recognizes the input trace as an LTTng (2.11
               or greater) trace, then it checks specific trace environment
               values to build a trace path relative to the directory
               specified by the path parameter:

               Linux kernel domain

                       HOST/SNAME-STIME/kernel

               User space domain, per-UID buffering

                       HOST/SNAME-STIME/ust/uid/UID/ARCHW-bit

               User space domain, per-PID buffering

                       HOST/SNAME-STIME/ust/pid/PNAME-PID-PTIME

               With:

               HOST
                   Target hostname.

               SNAME
                   Tracing session name.

               STIME
                   Tracing session creation date/time.

               UID
                   User ID.

               ARCHW
                   Architecture width (32 or 64).

               PNAME
                   Process name.

               PID
                   Process ID.

               PTIME
                   Process date/time.

            3. If the input trace has a name, then the component sanitizes
               this name and uses it as a relative path to the directory
               specified by the path parameter.

               The trace name sanitization operation:

               •   Replaces .  subdirectories with _.

               •   Replaces ..  subdirectories with __.

               •   Removes any trailing / character.

            4. The component uses the subdirectory trace relative to the
               directory specified by the path parameter.

           In all the cases above, if the effective output trace path already
           exists on the file system, then the component appends a numeric
           suffix to the name of the last subdirectory. The suffix starts
           at 0 and increments until the path doesn’t exist.

## [](#INITIALIZATION_PARAMETERS)INITIALIZATION PARAMETERS

           assume-single-trace=VAL [optional boolean]
               If VAL is true, then assume that the component only receives
               messages related to a single input trace.

               This parameter affects how the component builds the output
               trace path (see “Output path”).

               Default: false.

           ctf-version=VERSION [optional string]
               Write traces following version VERSION of CTF, where VERSION
               is one of:

               1, 1.8
                   CTF 1.8.

               2, 2.0
                   CTF 2.

               Default: 2.

           ignore-discarded-events=VAL [optional boolean]
               If VAL is true, then ignore discarded events messages.

               Default: false.

           ignore-discarded-packets=VAL [optional boolean]
               If VAL is true, then ignore discarded packets messages.

               Default: false.

           path=PATH [string]
               Base output path.

               See “Output path” to learn how the component uses this
               parameter to build the output path for a given input trace.

           quiet=VAL [optional boolean]
               If VAL is true, then don’t write anything to the standard
               output.

               Default: false.

## [](#PORTS)PORTS

               +-------------+
               | sink.ctf.fs |
               |             |
               @ in          |
               +-------------+

       Input
           in
               Single input port.

## [](#BUGS)BUGS

           If you encounter any issue or usability problem, please report it
           on the Babeltrace bug tracker (see
           <https://bugs.lttng.org/projects/babeltrace>).

## [](#RESOURCES)RESOURCES

           The Babeltrace project shares some communication channels with the
           LTTng project (see <https://lttng.org/>).

           •   Babeltrace website (see <https://babeltrace.org/>)

           •   Mailing list (see <https://lists.lttng.org>) for support and
               development: lttng-dev@lists.lttng.org

           •   IRC channel (see <irc://irc.oftc.net/lttng>): #lttng on
               irc.oftc.net

           •   Bug tracker (see <https://bugs.lttng.org/projects/babeltrace>)

           •   Git repository (see
               <https://git.efficios.com/?p=babeltrace.git>)

           •   GitHub project (see <https://github.com/efficios/babeltrace>)

           •   Continuous integration (see
               <https://ci.lttng.org/view/Babeltrace/>)

           •   Code review (see
               <https://review.lttng.org/q/project:babeltrace>)

## [](#AUTHORS)AUTHORS

           The Babeltrace 2 project is the result of hard work by many
           regular developers and occasional contributors.

           The current project maintainer is Jérémie Galarneau
           <mailto:jeremie.galarneau@efficios.com>.

## [](#COPYRIGHT)COPYRIGHT

           This component class is part of the Babeltrace 2 project.

           Babeltrace is distributed under the MIT license (see
           <https://opensource.org/licenses/MIT>).

## [](#SEE_ALSO)SEE ALSO

           babeltrace2-intro(7), babeltrace2-plugin-ctf(7)

## [](#COLOPHON)COLOPHON

           This page is part of the babeltrace (trace read and write
           libraries and a trace converter) project.  Information about the
           project can be found at ⟨http://www.efficios.com/babeltrace⟩.  If
           you have a bug report for this manual page, send it to
           lttng-dev@lists.lttng.org.  This page was obtained from the
           project's upstream Git repository
           ⟨git://git.efficios.com/babeltrace.git⟩ on 2026-08-03.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-17.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Babeltrace 2.2.0rc1          16 October 2024         BABELTRACE2-SINK.(7)

------------------------------------------------------------------------

Pages that refer to this page: [babeltrace2(1)](../man1/babeltrace2.1.html),  [babeltrace2-convert(1)](../man1/babeltrace2-convert.1.html),  [babeltrace2-plugin-ctf(7)](../man7/babeltrace2-plugin-ctf.7.html)

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
