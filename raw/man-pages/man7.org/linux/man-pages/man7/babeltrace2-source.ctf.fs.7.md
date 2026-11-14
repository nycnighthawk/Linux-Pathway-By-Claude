---
{"title": "babeltrace2-source.ctf.fs(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/babeltrace2-source.ctf.fs.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# babeltrace2-source.ctf.fs(7) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INITIALIZATION PARAMETERS](#INITIALIZATION_PARAMETERS) \| [PORTS](#PORTS) \| [QUERY OBJECTS](#QUERY_OBJECTS) \| [BUGS](#BUGS) \| [RESOURCES](#RESOURCES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BABELTRACE2-SOURCE()                                 BABELTRACE2-SOURCE()

## [](#NAME)NAME

           babeltrace2-source.ctf.fs - Babeltrace 2: File system CTF source
           component class

## [](#DESCRIPTION)DESCRIPTION

           A Babeltrace 2 source.ctf.fs message iterator reads one or more
           CTF 1.8 (see <https://diamon.org/ctf/v1.8.3/>) or CTF 2 (see
           <https://diamon.org/ctf/>) data streams on the file system and
           emits corresponding messages.

               CTF data streams on
               the file system
                 |
                 |   +---------------------+
                 |   |      src.ctf.fs     |
                 |   |                     |
                 '-->|    ...5c847 | 0 | 0 @--> Stream 0 messages
                     |    ...5c847 | 0 | 1 @--> Stream 1 messages
                     |    ...5c847 | 0 | 2 @--> Stream 2 messages
                     +---------------------+

           See babeltrace2-intro(7) to learn more about the Babeltrace 2
           project and its core concepts.

       Input
           A source.ctf.fs component opens a single logical CTF trace. A
           logical CTF trace contains one or more physical CTF traces. A
           physical CTF trace on the file system is a directory which
           contains:

           •   One metadata stream file named metadata.

           •   One or more data stream files, that is, any file with a name
               that does not start with .  and which isn’t metadata.

           •   Optional: One LTTng (see <https://lttng.org/>) index directory
               named index.

           If the logical CTF trace to handle contains more than one physical
           CTF trace, then all the physical CTF traces, depending on the CTF
           version:

           CTF 1.8
               Must have a trace UUID and all UUIDs must be the same.

           CTF 2
               Must have a trace name and a trace unique ID (UID), and all
               trace namespaces (if any), names, and UIDs must be the same.

           Opening more than one physical CTF trace to constitute a single
           logical CTF trace is needed to support LTTng’s tracing session
           rotation feature, for example (see lttng-rotate(1) starting from
           LTTng 2.11). In that case, the component elects the largest
           metadata stream, considering the total count of data stream
           classes and event record classes, as the one to use to decode the
           data streams of all the physical traces.

           You specify which physical CTF traces to open and read with the
           inputs array parameter. Each entry in this array is the path to a
           physical CTF trace directory, that is, the directory directly
           containing the stream files.

           A source.ctf.fs component doesn’t recurse into directories to find
           CTF traces. However, the component class provides the
           babeltrace.support-info query object which indicates whether or
           not a given directory looks like a CTF trace directory (see
           “babeltrace.support-info”).

           The component creates one output port for each logical CTF data
           stream. More than one physical CTF data stream file can support a
           single logical CTF data stream (LTTng’s trace file rotation and
           tracing session rotation can cause this).

           If two or more data stream files contain the same packets, then a
           source.ctf.fs message iterator reads each of them only once so
           that it never emits duplicated messages. This feature makes it
           possible, for example, to open overlapping LTTng snapshots (see
           <https://lttng.org/docs/#doc-taking-a-snapshot>) with a single
           source.ctf.fs component and silently discard the duplicated
           packets.

       Trace quirks
           Many tracers produce CTF traces. A source.ctf.fs component makes
           some effort to support as many CTF traces as possible, even those
           with malformed streams.

           In general, for a CTF 1.8 trace:

           •   If the timestamp_begin or timestamp_end packet context field
               class exists, but it’s not mapped to a clock class, and
               there’s only one clock class at this point in the metadata
               stream, then the component maps the field class to this unique
               clock class.

           A source.ctf.fs component has special quirk handling for some
           LTTng (see <https://lttng.org/>) and barectf (see
           <https://lttng.org/>) traces, depending on the tracer version:

           All LTTng versions

               •   For CTF 1.8 traces, the component sets the origin of the
                   monotonic clock class to the Unix epoch so that different
                   LTTng traces are always correlatable.

                   This is the equivalent of setting the force-clock-class-
                   origin-unix-epoch parameter to true.

               •   For a given data stream, for all the contiguous last
                   packets of which the timestamp_end context field is 0, the
                   message iterator uses the time of the last event record of
                   the packet as the time of the packet end message.

                   This is useful for the traces which lttng-crash(1)
                   generates.

           LTTng-UST up to, but excluding, 2.11.0, LTTng-modules up to, but
           excluding, 2.9.13, LTTng-modules from 2.10.0 to 2.10.9

               •   For a given packet, the message iterator uses the time of
                   the last event record of the packet as the time of the
                   packet end message, ignoring the timestamp_end packet
                   context field.

           barectf up to, but excluding, 2.3.1

               •   For a given packet, the message iterator uses the time of
                   the first event record of the packet as the time of the
                   packet beginning message, ignoring the timestamp_begin
                   packet context field.

       Message Interchange Protocol (MIP) specifics
           A source.ctf.fs component can open and decode, depending on the
           effective MIP version:

           MIP 0
               CTF 1.8 traces.

           MIP 1
               CTF 1.8 and CTF 2 traces.

           While the CTF 1.8 metadata stream (TSDL) features naturally map to
           the MIP 0 API and the CTF 2 ones to the MIP 1 API, a source.ctf.fs
           component makes a best effort to represent CTF 1.8 features when
           working with MIP 1. In particular, a source.ctf.fs component:

           •   For an LTTng trace:

               •   Sets the namespace of any libbabeltrace2 trace to
                   lttng.org,2009.

               •   Sets the origin of any libbabeltrace2 clock class to the
                   Unix epoch.

           •   If the UUID of a CTF trace is available, then sets the UID of
               the corresponding libbabeltrace2 trace to the textual
               representation of the trace UUID and its name to an empty
               string.

           •   Sets the UID of a libbabeltrace2 clock class to the textual
               representation of the UUID of its corresponding CTF clock
               class, if available.

           •   Makes the accuracy of any libbabeltrace2 clock class unknown.

           When reading a CTF 2 metadata stream (therefore working with
           MIP 1), a source.ctf.fs component:

           •   Sets the log level of a libbabeltrace2 event class from the
               value of the log-level attribute, under either the
               lttng.org,2009 or babeltrace.org,2020 namespace, of its
               corresponding CTF event record class as such:

               "emergency"
                   BT_EVENT_CLASS_LOG_LEVEL_EMERGENCY

               "alert"
                   BT_EVENT_CLASS_LOG_LEVEL_ALERT

               "critical"
                   BT_EVENT_CLASS_LOG_LEVEL_CRITICAL

               "error"
                   BT_EVENT_CLASS_LOG_LEVEL_ERROR

               "warning"
                   BT_EVENT_CLASS_LOG_LEVEL_WARNING

               "notice"
                   BT_EVENT_CLASS_LOG_LEVEL_NOTICE

               "info"
                   BT_EVENT_CLASS_LOG_LEVEL_INFO

               "debug:system"
                   BT_EVENT_CLASS_LOG_LEVEL_DEBUG_SYSTEM

               "debug:program"
                   BT_EVENT_CLASS_LOG_LEVEL_DEBUG_PROGRAM

               "debug:process"
                   BT_EVENT_CLASS_LOG_LEVEL_DEBUG_PROCESS

               "debug:module"
                   BT_EVENT_CLASS_LOG_LEVEL_DEBUG_MODULE

               "debug:unit"
                   BT_EVENT_CLASS_LOG_LEVEL_DEBUG_UNIT

               "debug:function"
                   BT_EVENT_CLASS_LOG_LEVEL_DEBUG_FUNCTION

               "debug:line"
                   BT_EVENT_CLASS_LOG_LEVEL_DEBUG_LINE

               "debug:debug"
                   BT_EVENT_CLASS_LOG_LEVEL_DEBUG

           •   Sets the EMF URI of a libbabeltrace2 event class from the
               value of the emf-uri attribute, under either the
               lttng.org,2009 or babeltrace.org,2020 namespace, of its
               corresponding CTF event record class.

       CTF compliance
           A source.ctf.fs component decodes traces as per CTF 1.8 (see
           <https://diamon.org/ctf/v1.8.3/>) or CTF 2 (see
           <https://diamon.org/ctf/>), except:

           •   It only supports fixed-length bit array field classes with
               sizes from 1 to 64 bits.

               This includes fixed-length integers and fixed-length floating
               point numbers:

               CTF 1.8 (TSDL)
                   integer, enum, and floating_point blocks.

               CTF 2
                   fixed-length-bit-array, fixed-length-bit-map, fixed-
                   length-boolean, fixed-length-unsigned-integer, fixed-
                   length-signed-integer, and fixed-length-floating-point-
                   number types.

           •   It only supports the following CTF 2 variable-length integer
               field values:

               variable-length-unsigned-integer
                   0 to 18,446,744,073,709,551,615 (unsigned 64-bit integer
                   range).

               variable-length-signed-integer
                   -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
                   (signed 64-bit integer range).

           •   It only supports 32-bit and 64-bit fixed-length floating point
               number classes:

               CTF 1.8 (TSDL)
                   floating_point block.

               CTF 2
                   fixed-length-floating-point-number type.

           •   It doesn’t support TSDL § 4.1.6 (“GNU/C bitfields”).

           •   It doesn’t support TSDL callsite blocks: the CTF 1.8 parser
               simply ignores them.

           •   It only supports a single clock class (TSDL clock block or
               CTF 2 clock-class fragment) reference per data stream class
               (TSDL stream block or CTF 2 data-stream-class fragment).

           •   It doesn’t support the checksum, compression, and encryption
               features of CTF 1.8 metadata stream packets.

## [](#INITIALIZATION_PARAMETERS)INITIALIZATION PARAMETERS

           clock-class-offset-ns=NS [optional signed integer]
               Add NS nanoseconds to the offset of all the clock classes that
               the component creates.

               You can combine this parameter with the clock-class-offset-s
               parameter.

           clock-class-offset-s=SEC [optional signed integer]
               Add SEC seconds to the offset of all the clock classes that
               the component creates.

               You can combine this parameter with the clock-class-offset-ns
               parameter.

           force-clock-class-origin-unix-epoch=VAL [optional boolean]
               If VAL is true, then force the origin of all clock classes
               that the component creates to have a Unix epoch origin,
               whatever the detected tracer.

               Default: false.

           inputs=DIRS [array of strings]
               Open and read the physical CTF traces located in DIRS.

               Each element of DIRS is the path to a physical CTF trace
               directory containing the trace stream files.

               All the specified physical CTF traces must belong to the same
               logical CTF trace. See “Input” to learn more about logical and
               physical CTF traces.

           trace-name=NAME [optional string]
               Set the name of the trace object that the component creates to
               NAME.

## [](#PORTS)PORTS

               +--------------------+
               |     src.ctf.fs     |
               |                    |
               |   ...5c847 | 0 | 1 @
               |                ... @
               +--------------------+

       Output
           A source.ctf.fs component creates one output port for each logical
           CTF data stream. See “Input” to learn more about logical and
           physical CTF data streams.

           Each output port name has one of the following forms:

               TRACE-ID | STREAM-CLASS-ID | STREAM-ID
               TRACE-ID | STREAM-ID

           The component uses the second form when the stream class ID isn’t
           available.

           TRACE-ID
               If the namespace NS, name NAME, and UID UID of the trace are
               available, then the exact string:

                   {namespace: `NS`, name: `NAME`, uid: `UID`}

               If the namespace of the trace isn’t available, but the name
               NAME and UID UID are, then the exact string:

                   {name: `NAME`, uid: `UID`}

               Otherwise, the absolute directory path of the trace.

                   Note
                   The namespace of any LTTng trace is lttng.org,2009. If a
                   CTF 1.8 trace has a UUID, then its corresponding
                   libbabeltrace2 trace always has a name and a UID (the
                   textual representation of the UUID).

           STREAM-CLASS-ID
               Stream class ID.

           STREAM-ID
               Stream ID if available, otherwise the absolute file path of
               the stream.

## [](#QUERY_OBJECTS)QUERY OBJECTS

       babeltrace.support-info
           See babeltrace2-query-babeltrace.support-info(7) to learn more
           about this query object.

           For a directory input which is the path to a CTF trace directory,
           the result object contains:

           weight
               0.75

           group
               If the namespace NS, name NAME, and UID UID of the trace are
               available, then the exact string:

                   namespace: NS, name: NAME, uid: UID

               If the namespace of the trace isn’t available, but the name
               NAME and UID UID are, then the exact string:

                   name: NAME, uid: UID

               Otherwise, the entry doesn’t exist.

                   Note
                   The namespace of any LTTng trace is lttng.org,2009. If a
                   CTF 1.8 trace has a UUID, then its corresponding
                   libbabeltrace2 trace always has a name and a UID (the
                   textual representation of the UUID).

           You can leverage the group entry of this query object to assemble
           many physical CTF traces as a single logical CTF trace (see
           “Input” to learn more about logical and physical CTF traces). This
           is how the babeltrace2-convert(1) command makes it possible to
           specify as non-option arguments the paths to multiple physical CTF
           traces which belong to the same logical CTF trace and create a
           single source.ctf.fs component.

       babeltrace.trace-infos
           See babeltrace2-query-babeltrace.trace-infos(7) to learn more
           about this query object.

       metadata-info
           You can query the metadata-info object for a specific CTF trace to
           get its plain text metadata stream as well as whether or not it’s
           packetized.

           Parameters:

           path=PATH [string]
               Path to the physical CTF trace directory which contains the
               metadata file.

           Result object (map):

           is-packetized [boolean]
               True if the metadata stream file is packetized.

               This is only relevant for a CTF 1.8 metadata stream. Always
               false with a CTF 2 metadata stream.

           text [string]
               Plain text metadata stream.

               The exact contents of the metadata stream file for a CTF 2
               metadata stream.

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

           babeltrace2-intro(7), babeltrace2-plugin-ctf(7), lttng-crash(1)

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

                                                         BABELTRACE2-SOURCE()

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
