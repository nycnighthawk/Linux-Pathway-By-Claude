---
{"title": "babeltrace2-intro(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/babeltrace2-intro.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# babeltrace2-intro(7) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [WHAT IS BABELTRACE 2?](#WHAT_IS_BABELTRACE_2?) \| [BABELTRACE 2 CONCEPTS](#BABELTRACE_2_CONCEPTS) \| [TRACE PROCESSING GRAPH REPRESENTATION](#TRACE_PROCESSING_GRAPH_REPRESENTATION) \| [BUGS](#BUGS) \| [RESOURCES](#RESOURCES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BABELTRACE2-INTRO(7)       Babeltrace 2 manual       BABELTRACE2-INTRO(7)

## [](#NAME)NAME

           babeltrace2-intro - Introduction to Babeltrace 2

## [](#DESCRIPTION)DESCRIPTION

           This manual page is an introduction to the Babeltrace 2 project.

           The “WHAT IS BABELTRACE 2?” section describes the parts of the
           project and shows the major changes from Babeltrace 1 to
           Babeltrace 2 while the “BABELTRACE 2 CONCEPTS” section defines the
           core concepts of Babeltrace 2.

           The “TRACE PROCESSING GRAPH REPRESENTATION” section shows how some
           concepts are visually represented in other Babeltrace 2 manual
           pages.

## [](#WHAT_IS_BABELTRACE_2?)WHAT IS BABELTRACE 2?

           Babeltrace 2 is an open-source software project of which the
           purpose is to process or convert traces (see
           <https://en.wikipedia.org/wiki/Tracing_(software)>).

           The Babeltrace 2 project includes the following parts:

           Babeltrace 2 library (libbabeltrace2)
               A shared library with a C API.

               With libbabeltrace2, you can programmatically create plugins
               and component classes, build and run trace processing graphs,
               and more (see the “BABELTRACE 2 CONCEPTS” section for more
               details about those concepts).

               All the other Babeltrace 2 parts rely on this library.

           babeltrace2 command-line program
               A command-line interface which uses libbabeltrace2 to load
               plugins, create a trace processing graph, create components,
               connect their ports correctly, and run the graph.

               You can also use babeltrace2 to list the available plugins or
               to query an object from a component class.

               See babeltrace2(1).

           Babeltrace 2 Python bindings
               A Python 3 package (bt2) which offers a Pythonic interface of
               libbabeltrace2.

               You can perform the same operations which are available in
               libbabeltrace2 with the Python bindings, but more conveniently
               and with less code. However, the Python bindings are less
               performant than libbabeltrace2.

           Babeltrace 2 project plugins
               The Babeltrace 2 plugins shipped with the project.

               Those plugins aren’t special in that they only rely on
               libbabeltrace2 and you don’t need them to use libbabeltrace2,
               babeltrace2(1), or the Python bindings. However, the project
               plugins provide many widely used trace format
               encoders/decoders as well as common trace processing graph
               utilities.

               The Babeltrace 2 project plugins are:

               ctf
                   Common Trace Format (see <https://diamon.org/ctf/>) (CTF)
                   input/output, including the LTTng live source.

                   See babeltrace2-plugin-ctf(7).

               lttng-utils
                   Graph utilities specific to LTTng (see
                   <https://lttng.org/>) traces.

                   See babeltrace2-plugin-lttng-utils(7).

               text
                   Plain text input/output.

                   See babeltrace2-plugin-text(7).

               utils
                   Common graph utilities (muxer, trimmer, counter, dummy
                   sink).

                   See babeltrace2-plugin-utils(7).

       Changes since Babeltrace 1
           This manual page is an introduction to Babeltrace 2, a rewrite of
           Babeltrace 1 with a focus on extensibility, flexibility, and
           interoperability.

           Babeltrace 1 exists since 2010.

           You can install both projects on the same file system as there are
           no file name conflicts.

           The major improvements brought by Babeltrace 2 are:

           General

               •   Full plugin support: any user can distribute a
                   Babeltrace 2 plugin and, as long as libbabeltrace2 finds
                   it, any application linked to libbabeltrace2 can load it
                   and use it.

                   Plugins aren’t just trace format encoders and decoders:
                   they package source, filter, and sink component classes so
                   that you can connect specialized, reusable components
                   together in a trace processing graph to create a
                   customized trace conversion or analysis device.

                   This modular strategy is much like how the FFmpeg (see
                   <https://www.ffmpeg.org/>), GStreamer (see
                   <https://gstreamer.freedesktop.org/>), and DirectShow (see
                   <https://en.wikipedia.org/wiki/DirectShow>) projects
                   approach media stream processing.

               •   All the parts of the Babeltrace 2 project run on the major
                   operating systems, including Windows and macOS.

               •   Some component classes, such as sink.text.pretty (similar
                   to the text output format of babeltrace(1)) and
                   sink.text.details, can write color codes to the standard
                   output when it’s connected to a color-enabled terminal.

                   The Babeltrace 2 log, printed to the standard output, can
                   also be colorized.

           Command-line interface

               •   Whereas you can convert traces from one format to another
                   with the Babeltrace 1 CLI tool, babeltrace(1), you can
                   also execute a custom trace manipulation task with
                   babeltrace2(1) thanks to the babeltrace2-run(1) command.

               •   The babeltrace2-convert(1) command features an automatic
                   source component discovery algorithm to find the best
                   suited components to create for a given non-option
                   argument (file or directory path, or custom string like an
                   LTTng live (see <https://lttng.org>) URL).

                   For example:

                       $ babeltrace2 /path/to/ctf/trace

                       $ babeltrace2 net://localhost/host/myhost/my-session

           CTF (see <https://diamon.org/ctf/>) 1.8 and 2 input/output

               •   The source.ctf.fs component class, which is more or less
                   the equivalent of the Babeltrace 1 ctf input format, has
                   features not found in Babeltrace 1:

                   •   The component handles many trace quirks which are the
                       results of known tracer bugs and corner cases
                       (LTTng-UST, LTTng-modules, and barectf (see
                       <https://github.com/efficios/barectf>)), making it
                       possible to decode malformed packets.

                   •   The component merges CTF traces sharing the same
                       identity into a single, logical trace.

                       This feature supports LTTng 2.11’s tracing session
                       rotation trace chunks.

               •   With a sink.ctf.fs component, you can create CTF traces on
                   the file system.

                   With babeltrace2(1), you can use the --output-format=ctf
                   and --output options to create an implicit sink.ctf.fs
                   component.

                   For example:

                       $ babeltrace2 /path/to/input/trace \
                                     --output-format=ctf --output=trace-dir

           LTTng live (see <https://lttng.org>) input

               •   The babeltrace(1) command exits successfully when it
                   cannot find an LTTng live (--input-format=lttng-live
                   option) tracing session.

                   The session-not-found-action initialization parameter
                   controls what a source.ctf.lttng-live message iterator
                   does when it cannot find the remote tracing session.

                   If the action is end, then the message iterator does like
                   babeltrace(1) and simply ends successfully.

                   If the action is continue (the default), then the message
                   iterator never ends: it keeps on trying until the tracing
                   session exists, indeed subscribing to the session.

           Library

               •   libbabeltrace2 shares nothing with libbabeltrace.

                   The Babeltrace 2 library C API has features such as:

                   •   A single header file.

                   •   Function precondition and postcondition checking.

                   •   Object-oriented model with shared and unique objects.

                   •   Strict C typing and const correctness.

                   •   User-extensible classes.

                   •   Rich, thread-safe error reporting.

                   •   Per-component and per-subsystem logging levels.

                   •   Trace intermediate representation (IR) objects to make
                       the API trace-format-agnostic.

                   •   A versioned protocol for message interchange between
                       components to enable forward and backward
                       compatibility.

               •   You can build the library in developer mode to enable an
                   extensive set of function precondition and postcondition
                   checks.

                   The developer mode can help detect programming errors
                   early when you develop a Babeltrace 2 plugin or an
                   application using libbabeltrace2.

                   See the project README for build-time requirements and
                   detailed build instructions.

## [](#BABELTRACE_2_CONCEPTS)BABELTRACE 2 CONCEPTS

           This section defines the main concepts of the Babeltrace 2
           project.

           These concepts translate into types and functions in
           libbabeltrace2 and its Python bindings, but also as command-line
           actions and options in the babeltrace2 program. The other
           Babeltrace 2 manual pages assume that you are familiar with the
           following definitions.

           Some Babeltrace 2 concepts are interdependent: it’s normal to jump
           from one definition to another to understand the big picture.

           Component class
               A reusable class which you can instantiate as one or more
               components within a trace processing graph.

               There are three types of component classes used to create the
               three types of components: source, filter, and sink.

               A component class implements methods, one of which is an
               initialization method, or constructor, to create a component.
               You pass initialization parameters to this method to customize
               the created component. For example, the initialization method
               of the source.ctf.fs component class accepts a mandatory
               inputs parameter which is an array of file system path(s) to
               the CTF trace(s). It also accepts an optional clock-class-
               offset-ns parameter which is an offset, in nanoseconds, to add
               to all the clock classes (descriptors of stream clocks) found
               in the metadata stream of the traces.

               A component class can have a description and a help text.

           Component
               A node within a trace processing graph.

               There are three types of components:

               Source component
                   An input component which produces messages.

                   Examples: CTF files input, log file input, LTTng live
                   input, random event generator.

               Filter component
                   An intermediate component which can transform the messages
                   it consumes, augment them, sort them, discard them, or
                   create new ones.

                   Examples: filter which removes messages based on an
                   expression, filter which adds debugging information to
                   selected events, message muxer, trace trimmer.

               Sink component
                   An output component which consumes messages and usually
                   writes them to one or more formatted files.

                   Examples: log file output, CTF files output,
                   pretty-printed plain text output.

               Components are connected together within a trace processing
               graph through their ports. Source components have output
               ports, sink components have input ports, and filter components
               have both.

               A component is the instance of a component class. The terms
               component and component class instance are equivalent.

               Within a trace processing graph, each component has a unique
               name. This isn’t the name of its component class, but an
               instance name. If human is a component class name, then Nancy
               and John could be component names.

               Once a graph is configured (the first time it runs), you
               cannot add components to it for the remaining graph lifetime.

           Port
               A connection point, on a component, from which are sent or
               where are received messages when the trace processing graph
               runs.

               An output port is from where messages are sent. An input port
               is where messages are received. Source components have output
               ports, sink components have input ports, and filter components
               have both.

               You can only connect an output port to a single input port.

               All ports don’t need to be connected.

               A filter or sink component receiving messages from its input
               ports is said to consume messages.

               The link between an output port and input port is a
               connection.

               Once a graph is configured (the first time it runs), you
               cannot connect ports for the remaining graph lifetime.

           Connection
               The link between an output port and an input port through
               which messages flow when a trace processing graph runs.

           Message iterator
               An iterator on an input port of which the returned elements
               are messages.

               A component or another message iterator can create many
               message iterators on a single input port, before or while the
               trace processing graph runs.

           Message
               The element of a message iterator.

               Messages flow from output ports to input ports.

               A source component message iterator produces messages, while a
               sink component consumes them. A filter component message
               iterator can both consume and produce messages.

               The main types of messages are:

               Event
                   A trace event record within a packet or within a stream.

               Packet beginning
                   The beginning of a packet within a stream.

                   A packet is a conceptual container of events.

               Packet end
                   The end of a packet within a stream.

               Stream beginning
                   The beginning of a stream.

                   A stream is a conceptual container of packets and/or
                   events.

                   Usually, a given source component output port sends packet
                   and event messages which belong to a single stream, but
                   it’s not required.

               Stream end
                   The end of a stream.

               Discarded events
                   A count of discarded events within a given time interval
                   for a given stream.

               Discarded packets
                   A count of discarded packets within a given time interval
                   for a given stream.

               The Message Interchange Protocol (MIP) dictates the expected
               types, order, and contents of messages. When you create a
               trace processing graph, you specify a MIP version, and all the
               components of said graph must comply with the selected
               protocol. This feature is what makes forward and backward
               compatibility possible when a Babeltrace 2 release changes the
               libbabeltrace2 API.

           Trace processing graph
               A filter graph (see
               <https://en.wikipedia.org/wiki/Filter_graph>) where nodes are
               components and messages flow from output ports to input ports.

               You can build a trace processing graph with libbabeltrace2,
               with the Babeltrace 2 Python bindings, or with the
               babeltrace2-run(1) and babeltrace2-convert(1) CLI commands.

               When a trace processing graph runs, the sink components
               consume messages from their input ports, making all the graph
               message iterators work one message at a time to perform the
               trace conversion or analysis duty.

           Plugin
               A container, or package, of component classes as a shared
               library or Python module.

               Each component class within a plugin has a type (source,
               filter, or sink) and a name. The type and name pair is unique
               within a given plugin.

               libbabeltrace2 can load a plugin (.so, .dll, or .py file) at
               run time: the result is a plugin object in which you can find
               a specific component class and instantiate it within a trace
               processing graph as a component.

               The babeltrace2 program uses the
               COMP-CLS-TYPE.PLUGIN-NAME.COMP-CLS-NAME format to identify a
               specific component class within a specific plugin.
               COMP-CLS-TYPE is either source (or src), filter (or flt), or
               sink.

               You can list the available Babeltrace 2 plugins with the
               babeltrace2-list-plugins(1) command.

           Query
               An operation with which you can get a named object from a
               component class, possibly with custom query parameters.

               The plain text metadata stream of a CTF trace and the
               available LTTng live sessions of a given LTTng relay daemon
               are examples of query objects.

               You can use libbabeltrace2, the Babeltrace 2 Python bindings,
               or the babeltrace2-query(1) CLI command to query a component
               class object.

## [](#TRACE_PROCESSING_GRAPH_REPRESENTATION)TRACE PROCESSING GRAPH REPRESENTATION

           In the Babeltrace 2 manual pages, a component is represented with
           a box. The box has the component class type, plugin name, and
           component class name at the top. Just below, between square
           brackets, is its component name within the trace processing graph.
           Each port is represented with an @ symbol on the border(s) of the
           component box with its name inside the box. Output ports are on
           the right border of the box while input ports are on its left
           border.

           For example, here’s a source component box:

               +------------+
               | src.ctf.fs |
               |  [my-src]  |
               |            |
               |    stream0 @
               |    stream1 @
               |    stream2 @
               +------------+

           This one is an instance of the source.ctf.fs component class named
           my-src. It has three output ports named stream0, stream1, and
           stream2.

           A trace processing graph is represented with multiple component
           boxes connected together. The connections are arrows from output
           ports to input ports.

           For example, here’s a simple conversion graph:

               +------------+    +-----------------+    +------------------+
               | src.ctf.fs |    | flt.utils.muxer |    | sink.text.pretty |
               |    [ctf]   |    |     [muxer]     |    |      [text]      |
               |            |    |                 |    |                  |
               |    stream0 @--->@ in0         out @--->@ in               |
               |    stream1 @--->@ in1             |    +------------------+
               |    stream2 @--->@ in2             |
               +------------+    @ in3             |
                                 +-----------------+

           Note that input port in3 of component muxer isn’t connected in
           this example.

           Sometimes, we symbolically represent other resources which are
           consumed from or produced by components. In this case, arrows are
           used, but they don’t go to or from port symbols (@), except for
           messages. For example, in the graph above, the ctf source
           component consumes a CTF trace and the text sink component prints
           plain text to the terminal, so here’s a more complete diagram:

               CTF trace
                 |
                 |   +------------+    +-----------------+    +------------------+
                 |   | src.ctf.fs |    | flt.utils.muxer |    | sink.text.pretty |
                 '-->|    [ctf]   |    |     [muxer]     |    |      [text]      |
                     |            |    |                 |    |                  |
                     |    stream0 @--->@ in0         out @--->@ in               |
                     |    stream1 @--->@ in1             |    +-----+------------+
                     |    stream2 @--->@ in2             |          |
                     +------------+    @ in3             |          '--> Terminal
                                       +-----------------+

           Here’s another example of a more complex graph which splits a
           specific stream using some criteria:

               +------------+    +-----------------+    +------------------+
               | src.ctf.fs |    | flt.utils.muxer |    | sink.text.pretty |
               |  [ctf-in]  |    |     [muxer]     |    |      [text]      |
               |            |    |                 |    |                  |
               |    stream0 @--->@ in0         out @--->@ in               |
               |    stream1 @--->@ in1             |    +------------------+
               |    stream2 @-.  @ in2             |
               +------------+ |  +-----------------+      +-------------+
                              |                           | sink.ctf.fs |
                              |                           |  [ctf-out0] |
                              |  +-------------------+    |             |
                              |  | flt.some.splitter | .->@ in          |
                              |  |     [splitter]    | |  +-------------+
                              |  |                   | |
                              '->@ in              A @-'  +-------------+
                                 |                 B @-.  | sink.ctf.fs |
                                 +-------------------+ |  |  [ctf-out1] |
                                                       |  |             |
                                                       '->@ in          |
                                                          +-------------+

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

           This manual page is part of the Babeltrace 2 project.

           Babeltrace is distributed under the MIT license (see
           <https://opensource.org/licenses/MIT>).

## [](#SEE_ALSO)SEE ALSO

           babeltrace2(1)

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

    Babeltrace 2.2.0rc1          10 January 2025         BABELTRACE2-INTRO(7)

------------------------------------------------------------------------

Pages that refer to this page: [babeltrace2(1)](../man1/babeltrace2.1.html),  [babeltrace2-convert(1)](../man1/babeltrace2-convert.1.html),  [babeltrace2-help(1)](../man1/babeltrace2-help.1.html),  [babeltrace2-list-plugins(1)](../man1/babeltrace2-list-plugins.1.html),  [babeltrace2-query(1)](../man1/babeltrace2-query.1.html),  [babeltrace2-run(1)](../man1/babeltrace2-run.1.html),  [babeltrace2-filter.lttng-utils.debug-info(7)](../man7/babeltrace2-filter.lttng-utils.debug-info.7.html),  [babeltrace2-filter.utils.muxer(7)](../man7/babeltrace2-filter.utils.muxer.7.html),  [babeltrace2-filter.utils.trimmer(7)](../man7/babeltrace2-filter.utils.trimmer.7.html),  [babeltrace2-plugin-ctf(7)](../man7/babeltrace2-plugin-ctf.7.html),  [babeltrace2-plugin-lttng-utils(7)](../man7/babeltrace2-plugin-lttng-utils.7.html),  [babeltrace2-plugin-text(7)](../man7/babeltrace2-plugin-text.7.html),  [babeltrace2-plugin-utils(7)](../man7/babeltrace2-plugin-utils.7.html),  [babeltrace2-query-babeltrace.support-info(7)](../man7/babeltrace2-query-babeltrace.support-info.7.html),  [babeltrace2-query-babeltrace.trace-infos(7)](../man7/babeltrace2-query-babeltrace.trace-infos.7.html),  [babeltrace2-sink.ctf.fs(7)](../man7/babeltrace2-sink.ctf.fs.7.html),  [babeltrace2-sink.text.details(7)](../man7/babeltrace2-sink.text.details.7.html),  [babeltrace2-sink.text.pretty(7)](../man7/babeltrace2-sink.text.pretty.7.html),  [babeltrace2-sink.utils.counter(7)](../man7/babeltrace2-sink.utils.counter.7.html),  [babeltrace2-sink.utils.dummy(7)](../man7/babeltrace2-sink.utils.dummy.7.html),  [babeltrace2-source.ctf.fs(7)](../man7/babeltrace2-source.ctf.fs.7.html),  [babeltrace2-source.ctf.lttng-live(7)](../man7/babeltrace2-source.ctf.lttng-live.7.html),  [babeltrace2-source.text.dmesg(7)](../man7/babeltrace2-source.text.dmesg.7.html)

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
