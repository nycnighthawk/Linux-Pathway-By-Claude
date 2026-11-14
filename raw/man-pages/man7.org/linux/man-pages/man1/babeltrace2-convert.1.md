---
{"title": "babeltrace2-convert(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/babeltrace2-convert.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# babeltrace2-convert(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [FILES](#FILES) \| [EXIT STATUS](#EXIT_STATUS) \| [BUGS](#BUGS) \| [RESOURCES](#RESOURCES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BABELTRACE2-CONVERT(1)     Babeltrace 2 manual     BABELTRACE2-CONVERT(1)

## [](#NAME)NAME

           babeltrace2-convert - Convert one or more traces to a given format

## [](#SYNOPSIS)SYNOPSIS

           Pretty-print (plain text) the events, in order, of one or more
           traces:

           babeltrace2 [GENERAL OPTIONS] [convert] [--retry-duration=TIME-US]
                       [--allowed-mip-versions=VERSION] TRACE-PATH...

           Convert one or more traces to a given format:

           babeltrace2 [GENERAL OPTIONS] [convert] [--retry-duration=TIME-US]
                       [--allowed-mip-versions=VERSION] CONVERSION ARGS

           Get the equivalent babeltrace2-run(1) command arguments to convert
           one or more traces to a given format:

           babeltrace2 [GENERAL OPTIONS] [convert] [--retry-duration=TIME-US]
                       [--allowed-mip-versions=VERSION]
                       (--run-args | --run-args-0) CONVERSION ARGS

           Print the metadata text of a CTF trace:

           babeltrace2 [GENERAL OPTIONS] [convert] [--output=OUTPATH]
                       --output-format=ctf-metadata TRACE-PATH

           Print the available remote LTTng tracing sessions (see
           <https://lttng.org/docs/#doc-lttng-live>):

           babeltrace2 [GENERAL OPTIONS] [convert] [--output=OUTPATH]
                       --input-format=lttng-live URL

## [](#DESCRIPTION)DESCRIPTION

           The convert command converts one or more traces to a given format,
           possibly with filters in the conversion path.

           See babeltrace2-intro(7) to learn more about the Babeltrace 2
           project and its core concepts.

               Note

               convert is the default babeltrace2(1) command: you generally
               don’t need to specify its name. The following commands are
               equivalent if the ... part doesn’t start with the name of
               another babeltrace2(1) command, like run or list-plugins:

                   $ babeltrace2 convert ...
                   $ babeltrace2 ...

               If you need to make sure that you are executing the convert
               command, then use babeltrace2 convert explicitly.

           More specifically, the convert command creates a conversion graph.

           A conversion graph is a specialized trace processing graph focused
           on the conversion of one or more traces to another format,
           possibly filtering or modifying their events and other messages in
           the process. A conversion graph is a linear chain of components
           once the source streams are merged:

               +----------+
               | source 1 @-.
               +----------+ |
                            |  +-------+
               +----------+ '->@       |    +---------+    +------------+
               | source 2 @--->@ muxer @--->@ trimmer @--->@ debug-info @-.
               +----------+ .->@       |    +---------+    +------------+ |
                            |  +-------+                                  |
               +----------+ |    .----------------------------------------'
               |   ...    @-'    |  +---------------+    +------+
               +----------+      '->@ other filters |--->@ sink |
                                    +---------------+    +------+

           Note that the trimmer, debugging information, and other filters
           are optional. See “Create implicit components from options” to
           learn how to enable them.

           If you need another trace processing graph layout, then use the
           more flexible babeltrace2-run(1) command.

           Like with the babeltrace2-run(1) command, you can create
           components explicitly with the --component option (see “Create
           explicit components”). You can also use one of the many specific
           convert command options (see “Create implicit components from
           options”) and non-option arguments (see “Create implicit
           components from non-option arguments”) to create implicit
           components.

           An implicit component is a component which is created and added to
           the conversion graph without an explicit instantiation through the
           --component option. An implicit component is easier to create than
           an explicit component: this is why the convert command exists, as
           you can also create and run a conversion graph with the generic
           babeltrace2-run(1) command.

           For example, you can specify one or more CTF trace path as
           non-option arguments to pretty-print the merged events to the
           standard output:

               $ babeltrace2 /path/to/trace /path/to/other/trace

           This is the equivalent of creating and connecting together:

           •   One source.ctf.fs components with its inputs initialization
               parameter set to /path/to/trace.

           •   One source.ctf.fs components with its inputs initialization
               parameter set to /path/to/other/trace.

           •   A filter.utils.muxer component.

           •   A sink.text.pretty component.

           This creates the following conversion graph:

               +------------+    +-----------------+    +------------------+
               | src.ctf.fs |    | flt.utils.muxer |    | sink.text.pretty |
               |  [ctf-fs]  |    |     [muxer]     |    |     [pretty]     |
               |            |    |                 |    |                  |
               |    stream0 @--->@ in0         out @--->@ in               |
               |    stream1 @--->@ in1             |    +------------------+
               |    stream2 @--->@ in2             |
               |    stream3 @--->@ in3             |
               +------------+    |                 |
                                 |                 |
               +------------+    |                 |
               | src.ctf.fs |    |                 |
               | [ctf-fs-2] |    |                 |
               |            |    |                 |
               |    stream0 @--->@ in4             |
               |    stream1 @--->@ in5             |
               +------------+    @ in6             |
                                 +-----------------+

           It’s equivalent to the following babeltrace2-run(1) command line:

               $ babeltrace2 run --component=ctf-fs:src.ctf.fs \
                                 --params='inputs=["/path/to/trace"] \
                                 --component=ctf-fs-2:src.ctf.fs \
                                 --params='inputs=["/path/to/other/trace"] \
                                 --component=muxer:filter.utils.muxer \
                                 --component=pretty:sink.text.pretty \
                                 --connect=ctf*:muxer --connect=muxer:pretty

           You can use the --run-args option to make the convert command
           print its equivalent run command arguments instead of creating and
           running the conversion graph. The printed arguments are escaped
           for shells, which means you can use them as is on the command line
           and possibly add more options to the run command:

               $ babeltrace2 run $(babeltrace2 --run-args /path/to/trace) ...

           The --run-args-0 option is like the --run-args option, but the
           printed arguments are NOT escaped and they’re separated by a null
           character instead of a space. This is useful if the resulting
           arguments aren’t the direct input of a shell, for example if
           passed to xargs -0.

           See “EXAMPLES” for usage examples.

       Create explicit components
           To explicitly create a component, use the --component option. This
           option specifies:

           •   Optional: The name of the component.

           •   The type of the component class to instantiate: source,
               filter, or sink.

           •   The name of the plugin in which to find the component class to
               instantiate.

           •   The name of the component class to instantiate.

           You can use the --component option multiple times to create
           multiple components. You can instantiate the same component class
           multiple times as different component instances.

           Immediately following a --component option on the command line,
           the created component is known as the current component (until the
           next --component option or non-option argument).

           The following command-line options apply to the current component:

           --log-level=LVL
               Set the log level of the current component to LVL.

           --params=PARAMS
               Add PARAMS to the initialization parameters of the current
               component.

               If PARAMS contains a key which exists in the initialization
               parameters of the current component, then replace the
               parameter.

           See “EXAMPLES” for usage examples.

       Create implicit components from non-option arguments
           When you specify a non-option argument to the convert command, it
           tries to find one or more components which can handle this
           argument.

           For example, with this command line:

               $ babeltrace2 /path/to/trace

           If /path/to/trace is a CTF trace directory, then the convert
           command creates a source.ctf.fs component to handle this specific
           trace.

           This automatic source component discovery mechanism is possible
           thanks to component classes which support the babeltrace.support-
           info query object (see
           babeltrace2-query-babeltrace.support-info(7)).

           The non-option argument can be a directory. If no component can
           handle that specific directory, then the convert command traverses
           that directory and recursively tries to find compatible components
           for each file and subdirectory. This means that a single
           non-option argument can lead to the creation of many implicit
           components.

           The following command-line options apply to ALL the implicit
           components created from the last non-option argument:

           --log-level=LVL
               Set the log level of those implicit components to LVL.

           --params=PARAMS
               Add PARAMS to the initialization parameters of those implicit
               components.

               For a given implicit component, if PARAMS contains a key which
               exists in the initialization parameters of this component,
               then replace the parameter.

           Note that it’s also possible for two non-option arguments to cause
           the creation of a single implicit component. For example, if you
           specify:

               $ babeltrace2 /path/to/chunk1 /path/to/chunk2

           where /path/to/chunk1 and /path/to/chunk2 are paths to chunks of
           the same logical CTF trace, then the convert command creates a
           single source.ctf.fs component which receives both paths at
           initialization time. When this happens, any --log-level or
           --params option that you specify to one of them applies to the
           single implicit component. For example:

               $ babeltrace2 /path/to/chunk1 --params=clock-class-offset-s=450 \
                             /path/to/chunk2 --params=clock-class-offset-ns=98 \
                             --log-level=INFO

           Here, the single implicit component gets both clock-class-offset-s
           and clock-class-offset-ns initialization parameters, as well as
           the INFO log level.

           For backward compatibility with the babeltrace(1) program, the
           convert command ignores any non-option argument which does not
           cause the creation of any component. In that case, it emits a
           warning log statement and continues.

       Create implicit components from options
           There are many ways to create implicit components from options
           with the convert command:

           •   To create an implicit filter.utils.trimmer component (stream
               trimmer), specify the --begin, --end, or --timerange option.

               Examples:

                   $ babeltrace2 /path/to/trace --begin=22:14:38 --end=22:15:07

                   $ babeltrace2 /path/to/trace --timerange=22:14:38,22:15:07

                   $ babeltrace2 /path/to/trace --end=12:31:04.882928015

           •   To create an implicit filter.lttng-utils.debug-info (add
               debugging information to compatible LTTng events), specify any
               of the --debug-info, --debug-info-dir, --debug-info-full-path,
               or --debug-info-target-prefix options.

               Examples:

                   $ babeltrace2 /path/to/trace --debug-info

                   $ babeltrace2 /path/to/trace \
                                 --debug-info-target-prefix=/tmp/tgt-root

                   $ babeltrace2 /path/to/trace --debug-info-full-path

           •   To create an implicit sink.text.pretty component
               (pretty-printing text output to the standard output or to a
               file), specify no other sink components, explicit or implicit.

               The implicit sink.text.pretty component exists by default. If
               any other explicit or implicit sink component exists, then the
               convert command doesn’t automatically create the implicit
               sink.text.pretty component.

               The --clock-cycles, --clock-date, --clock-gmt, --clock-
               seconds, --color, --fields, --names, and --no-delta options
               all apply to the implicit sink.text.pretty component.

               The --output option without --output-format=ctf makes the
               implicit sink.text.pretty component write its content to a
               file, except the warnings for backward compatibility with the
               babeltrace(1) program.

               Examples:

                   $ babeltrace2 /path/to/trace

                   $ babeltrace2 /path/to/trace --no-delta

                   $ babeltrace2 /path/to/trace --output=/tmp/pretty-out

           •   To create an implicit sink.utils.dummy component (no output),
               specify the --output-format=dummy option.

               Example:

                   $ babeltrace2 /path/to/trace --output-format=dummy

           •   To create an implicit sink.ctf.fs component (CTF traces
               written to the file system), specify the --output-format=ctf
               and the --output=DIR (base output directory) options.

               Example:

                   $ babeltrace2 /path/to/input/trace --output-format=ctf \
                                 --output=my-traces

               As of this version, a sink.ctf.fs component generates CTF 2
               (see <https://diamon.org/ctf/>) traces by default. To write
               CTF 1.8 (see <https://diamon.org/ctf/v1.8.3/>) traces, create
               an explicit sink.ctf.fs component (see “Create explicit
               components”) and use the ctf-version="1" initialization
               parameter:

                   $ babeltrace2 /path/to/input/trace --component=sink.ctf.fs \
                                 --params='path="my-traces",ctf-version="1"'

           You can combine multiple methods to create multiple implicit
           components. For example, you can trim an LTTng (CTF) trace, add
           debugging information to it, and write it as another CTF trace:

               $ babeltrace2 /path/to/input/trace --timerange=22:14:38,22:15:07 \
                             --debug-info --output-format=ctf --output=out-dir

           The equivalent babeltrace2-run(1) command of this convert command
           is:

               $ babeltrace2 run --component=auto-disc-source-ctf-fs:source.ctf.fs \
                                 --params='inputs=["/path/to/input/trace"]' \
                                 --component=sink-ctf-fs:sink.ctf.fs \
                                 --params='path="out-dir"' \
                                 --component=muxer:filter.utils.muxer \
                                 --component=trimmer:filter.utils.trimmer \
                                 --params='begin="22:14:38"' \
                                 --params='end="22:15:07"' \
                                 --component=debug-info:filter.lttng-utils.debug-info \
                                 --connect=auto-disc-source-ctf-fs:muxer \
                                 --connect=muxer:trimmer \
                                 --connect=trimmer:debug-info \
                                 --connect=debug-info:sink-ctf-fs

           The order of the implicit component options documented in this
           subsection isn’t significant.

           See “EXAMPLES” for more examples.

## [](#OPTIONS)OPTIONS

       General
           You can use those options before the command name.

           See babeltrace2(1) for more details.

           -d, --debug
               Legacy option: this is equivalent to --log-level=TRACE.

           -l LVL, --log-level=LVL
               Set the log level of all known Babeltrace 2 loggers to LVL.

           --omit-home-plugin-path
               Don’t search for plugins in
               $HOME/.local/lib/babeltrace2/plugins.

           --omit-system-plugin-path
               Don’t search for plugins in
               /usr/local/lib/babeltrace2/plugins.

           --plugin-path=PATH[:PATH]...
               Add PATH to the list of paths in which plugins can be found.

           -v, --verbose
               Legacy option: this is equivalent to --log-level=INFO.

       Explicit component creation
           See “Create explicit components” to learn how to use the following
           option.

           -c [NAME:]COMP-CLS-TYPE.PLUGIN-NAME.COMP-CLS-NAME,
           --component=[NAME:]COMP-CLS-TYPE.PLUGIN-NAME.COMP-CLS-NAME
               Create a component named NAME (if specified) from the
               component class of type COMP-CLS-TYPE named COMP-CLS-NAME
               found in the plugin named PLUGIN-NAME, and set it as the
               current component.

               The available values for COMP-CLS-TYPE are:

               source, src
                   Source component class.

               filter, flt
                   Filter component class.

               sink
                   Sink component class.

       Common component creation
           See “Create explicit components” and “Create implicit components
           from non-option arguments” to learn how to use the following
           options.

           The following options apply to either the current explicit
           component (last --component option) or to ALL the implicit
           components created from the last non-option argument.

           -l LVL, --log-level=LVL
               Set the log level of the current component(s) to LVL.

               The available values for LVL are:

               NONE, N
                   Logging is disabled.

               FATAL, F
                   Severe errors that lead the execution to abort
                   immediately.

                   This level should be enabled in production.

               ERROR, E
                   Errors that might still allow the execution to continue.

                   Usually, once one or more errors are reported at this
                   level, the application, plugin, or library won’t perform
                   any more useful task, but it should still exit cleanly.

                   This level should be enabled in production.

               WARN, WARNING, W
                   Unexpected situations which still allow the execution to
                   continue.

                   This level should be enabled in production.

               INFO, I
                   Informational messages that highlight progress or
                   important states of the application, plugins, or library.

                   This level can be enabled in production.

               DEBUG, D
                   Debugging information, with a higher level of details than
                   the TRACE level.

                   This level should NOT be enabled in production.

               TRACE, T
                   Low-level debugging context information.

                   This level should NOT be enabled in production.

           -p PARAMS, --params=PARAMS
               Add PARAMS to the initialization parameters of the current
               component(s).

               If PARAMS contains a key which exists in the initialization
               parameters of the current component(s), then replace the
               parameter.

               The format of PARAMS is a comma-separated list of NAME=VALUE
               assignments:

                   NAME=VALUE[,NAME=VALUE]...

               NAME
                   Parameter name (C identifier plus the :, ., and -
                   characters).

               VALUE
                   One of:

                   •   null, nul, NULL: null value.

                   •   true, TRUE, yes, YES: true boolean value.

                   •   false, FALSE, no, NO: false boolean value.

                   •   Binary (0b prefix), octal (0 prefix), decimal, or
                       hexadecimal (0x prefix) unsigned (with + prefix) or
                       signed 64-bit integer.

                   •   Double precision floating point number (scientific
                       notation is accepted).

                   •   Unquoted string with no special characters, and not
                       matching any of the null and boolean value symbols
                       above.

                   •   Double-quoted string (accepts escape characters).

                   •   Array, formatted as an opening [, a comma-separated
                       list of VALUE, and a closing ].

                   •   Map, formatted as an opening {, a comma-separated list
                       of NAME=VALUE assignments, and a closing }.

                   You may put whitespaces around the individual =
                   (assignment), , (separator), [ (array beginning), ] (array
                   end), { (map beginning), and } (map end) characters.

               Example:

                   --params='many=null, fresh=yes, condition=false, squirrel=-782329,
                             play=+23, observe=3.14, simple=beef,
                             needs-quotes="some string",
                             escape.chars-are:allowed="a \" quote",
                             things=[1, "hello", 2.71828],
                             frog={slow=2, bath=[bike, 23], blind=NO}'

                   Important
                   Like in the example above, make sure to single-quote the
                   whole argument when you run this command from a shell, as
                   it can contain many special characters.

       Legacy options to create implicit components
           -i FORMAT, --input-format=FORMAT
               Force the convert command to create components from a specific
               component class for non-option arguments (see “Create implicit
               components from non-option arguments”), or list available
               remote LTTng tracing sessions.

               The available values for FORMAT are:

               ctf
                   Use the source.ctf.fs component class.

                   Each non-option argument of the command line is a CTF
                   trace or CTF trace chunk.

                   See babeltrace2-source.ctf.fs(7) to learn more about this
                   component class.

               lttng-live
                   Depending on the format of the first non-option argument:

                   net[4]://RDHOST[:RDPORT]
                       List the available remote LTTng tracing sessions for
                       the LTTng relay daemon at the address RDHOST and port
                       RDPORT (5344 if not specified), and then exit.

                   net[4]://RDHOST[:RDPORT]/host/TGTHOST/SESSION
                       Use the source.ctf.lttng-live component class.

                       See babeltrace2-source.ctf.lttng-live(7) to learn more
                       about this component class and the URL format.

               You can specify at most one --input-format option.

           -o FORMAT, --output-format=FORMAT
               Create an implicit sink component with format FORMAT or print
               the metadata text of a CTF trace.

               The available values for FORMAT are:

               text
                   Create an implicit sink.text.pretty component.

                   See “Implicit sink.text.pretty component”.

                   See babeltrace2-sink.text.pretty(7) to learn more about
                   this component class.

               ctf
                   Create an implicit sink.ctf.fs component. Specify the base
                   output path with the --output option.

                   As of this version, a sink.ctf.fs component generates
                   CTF 2 (see <https://diamon.org/ctf/>) traces by default.
                   To write CTF 1.8 (see <https://diamon.org/ctf/v1.8.3/>)
                   traces, create an explicit sink.ctf.fs component (see
                   “Create explicit components”) and use the ctf-version="1"
                   initialization parameter.

                   See babeltrace2-sink.ctf.fs(7) to learn more about this
                   component class.

               dummy
                   Create an implicit sink.utils.dummy component.

                   See babeltrace2-sink.utils.dummy(7) to learn more about
                   this component class.

               ctf-metadata
                   Print the metadata text of a CTF trace and exit.

                   The first non-option argument specifies the path to the
                   CTF trace.

               You can specify at most one --output-format option.

       Implicit source.ctf.fs component(s)
           See babeltrace2-source.ctf.fs(7) to learn more about this
           component class.

           --clock-force-correlate
               Set the force-clock-class-origin-unix-epoch initialization
               parameter of all the implicit source.ctf.fs components to
               true.

               The force-clock-class-origin-unix-epoch initialization
               parameter makes all the created clock classes have a Unix
               epoch origin. This is useful to force the clock classes of
               multiple traces to be compatible even if they’re not
               inherently.

           --clock-offset=SEC
               Set the clock-class-offset-s initialization parameter of all
               the implicit source.ctf.fs components to SEC.

               The clock-class-offset-s initialization parameter adds SEC
               seconds to the offsets of all the clock classes that the
               component creates.

               You can combine this option with --clock-offset-ns.

           --clock-offset-ns=NS
               Set the clock-class-offset-ns initialization parameter of all
               the implicit source.ctf.fs components to NS.

               The clock-class-offset-ns initialization parameter adds NS
               nanoseconds to the offsets of all the clock classes that the
               component creates.

               You can combine this option with --clock-offset-s.

       Implicit filter.utils.trimmer component
           If you specify at least one of the following options, you create
           an implicit filter.utils.trimmer component.

           See babeltrace2-filter.utils.trimmer(7) to learn more about this
           component class.

           --begin=TIME
               Set the begin initialization parameter of the component to
               TIME.

               You cannot use this option with the --timerange option.

               The format of TIME is one of:

                   YYYY-MM-DD HH:II[:SS[.NANO]]
                   HH:II[:SS[.NANO]]
                   [-]SEC[.NANO]

               YYYY
                   4-digit year.

               MM
                   2-digit month (January is 01).

               DD
                   2-digit day.

               HH
                   2-digit hour (24-hour format).

               II
                   2-digit minute.

               SS
                   2-digit second.

               NANO
                   Nanoseconds (up to nine digits).

               SEC
                   Seconds since origin.

           --end=TIME
               Set the end initialization parameter of the component to TIME.

               You cannot use this option with the --timerange option.

               See the --begin option for the format of TIME.

           --timerange=BEGIN,END
               Equivalent to --begin=BEGIN and --end=END.

               You can also surround the whole argument with [ and ].

       Implicit filter.lttng-utils.debug-info component
           If you specify at least one of the following options, you create
           an implicit filter.lttng-utils.debug-info component. This
           component only alters compatible LTTng events.

           See babeltrace2-filter.lttng-utils.debug-info(7) to learn more
           about this component class.

           --debug-info
               Create an implicit filter.lttng-utils.debug-info component.

               This option is useless if you specify any of the options
               below.

           --debug-info-dir=DIR
               Set the debug-info-dir initialization parameter of the
               component to DIR.

               The debug-info-dir parameter indicates where the component
               should find the debugging information it needs if it’s not
               found in the actual executable files.

           --debug-info-full-path
               Set the full-path initialization parameter of the component to
               true.

               When the full-path parameter is true, the component writes the
               full (absolute) paths to files in its debugging information
               fields instead of just the short names.

           --debug-info-target-prefix=PREFIX
               Set the target-prefix initialization parameter of the
               component to PREFIX.

               The target-prefix parameter is a path to prepend to the paths
               to executables recorded in the trace. For example, if a trace
               contains the executable path /usr/bin/ls in its state dump
               events, and you specify --debug-info-target-
               prefix=/home/user/boards/xyz/root, then the component opens
               the /home/user/boards/xyz/root/usr/bin/ls file to find
               debugging information.

       Implicit sink.text.pretty component
           If you specify at least one of the following options, then you
           force the sink component of the convert command to be an implicit
           sink.text.pretty component.

           See babeltrace2-sink.text.pretty(7) to learn more about this
           component class.

           --clock-cycles
               Set the clock-seconds initialization parameter of the
               component to true.

               The clock-cycles parameter makes the component print the event
               time in clock cycles.

           --clock-date
               Set the clock-date initialization parameter of the component
               to true.

               The clock-date parameter makes the component print the date
               and the time of events.

           --clock-gmt
               Set the clock-gmt initialization parameter of the component to
               true.

               The clock-gmt parameter makes the component not apply the
               local timezone to the printed times.

           --clock-seconds
               Set the clock-seconds initialization parameter of the
               component to true.

               The clock-seconds parameter makes the component print the
               event times in seconds since the Unix epoch.

           --color=WHEN
               Set the color initialization parameter of the component to
               WHEN.

               The available values for WHEN are:

               auto
                   Only emit terminal color codes when the standard output
                   and error streams are connected to a color-capable
                   terminal.

               never
                   Never emit terminal color codes.

               always
                   Always emit terminal color codes.

               The auto and always values have no effect if the
               BABELTRACE_TERM_COLOR environment variable is set to NEVER.

           --fields=FIELD[,FIELD]...
               For each FIELD, set the field-FIELD initialization parameter
               of the component to true.

               For example, --fields=trace,loglevel,emf sets the field-trace,
               field-loglevel, and field-emf initialization parameters to
               true.

               The available value for FIELD are:

               •   trace

               •   trace:hostname

               •   trace:domain

               •   trace:procname

               •   trace:vpid

               •   loglevel

               •   emf

               •   callsite

           --names=NAME[,NAME]...
               For each NAME, set the name-NAME initialization parameter of
               the component to true.

               For example, --names=payload,scope sets the name-payload and
               name-scope initialization parameters to true.

               The available value for NAME are:

               •   payload

               •   context

               •   scope

               •   header

           --no-delta
               Set the no-delta initialization parameter of the component to
               true.

               When the no-delta parameter is true, the component doesn’t
               print the duration since the last event on the line.

       Shared options
           -w PATH, --output=PATH
               With --output-format=ctf-metadata or --input-format=lttng-live
               (when printing the available remote LTTng tracing sessions),
               write the text to the file PATH instead of the standard
               output.

               When you specify --output-format=ctf, set the path
               initialization parameter of the implicit sink.ctf.fs component
               to PATH.

               Without any specified sink component, explicit or implicit,
               force the sink component of the convert command to be an
               implicit sink.text.pretty component and set its path
               initialization parameter to PATH.

               See babeltrace2-sink.ctf.fs(7) and
               babeltrace2-sink.text.pretty(7) to learn more about those
               component classes.

       Equivalent babeltrace2 run arguments
           --run-args
               Print the equivalent babeltrace2-run(1) arguments instead of
               creating and running the conversion graph.

               The printed arguments are space-separated and individually
               escaped for safe shell input.

               You cannot use this option with the --run-args-0 or --stream-
               intersection option.

           --run-args-0
               Print the equivalent babeltrace2-run(1) arguments instead of
               creating and running the conversion graph.

               The printed arguments are separated with a null character and
               NOT escaped for safe shell input.

               You cannot use this option with the --run-args or --stream-
               intersection option.

       Conversion graph configuration
           -m VERSION, --allowed-mip-versions=VERSION
               Only allow the conversion graph to honour version VERSION (0
               or 1) of the Message Interchange Protocol (MIP) instead of
               allowing both versions.

           --retry-duration=TIME-US
               Set the duration of a single retry to TIME-US µs when a sink
               component reports "try again later" (busy network or file
               system, for example).

               Default: 100000 (100 ms).

           --stream-intersection
               Enable the stream intersection mode.

               In this mode, for each trace, the convert command filters out
               the events and other messages which aren’t in the time range
               where all the trace streams are active.

               To use this option, all the source components, explicit and
               implicit, must have classes which support the
               babeltrace.trace-infos query object (see
               babeltrace2-query-babeltrace.trace-infos(7)). The only
               component class of the Babeltrace 2 project which supports
               this query object is source.ctf.fs.

               You cannot use this option with the --run-args or --run-args-0
               option.

       Other legacy options
           The following options exist for backward compatibility with the
           babeltrace(1) program.

           -d, --debug
               Legacy option: this is equivalent to --log-level=TRACE, where
               --log-level is the general option (not the --log-level option
               of this command).

           -v, --verbose
               Legacy option: this is equivalent to --log-level=INFO, where
               --log-level is the general option (not the --log-level option
               of this command).

               This option also sets the verbose parameter of the implicit
               sink.text.pretty component (see
               babeltrace2-sink.text.pretty(7)) to true.

       Command information
           -h, --help
               Show the command help and quit.

## [](#EXAMPLES)EXAMPLES

           Example 1. Pretty-print the events, in order, of one or more CTF
           traces.

               $ babeltrace2 my-ctf-traces

               $ babeltrace2 my-ctf-traces

               $ babeltrace2 my-ctf-trace-1 my-ctf-trace-2 my-ctf-trace-3

           Example 2. Trim a CTF trace and pretty-print the events.

               $ babeltrace2 my-ctf-trace --begin=22:55:43.658582931 \
                                          --end=22:55:46.967687564

               $ babeltrace2 my-trace --begin=22:55:43.658582931

               $ babeltrace2 my-trace --end=22:55:46.967687564

               $ babeltrace2 my-trace --timerange=22:55:43,22:55:46.967687564

           Example 3. Trim a CTF trace, enable the stream intersection mode,
           and write a CTF trace.

               $ babeltrace2 my-ctf-trace --stream-intersection \
                             --timerange=22:55:43,22:55:46.967687564 \
                             --output-format=ctf --output=out-ctf-trace

           Example 4. Print the available remote LTTng sessions (through
           LTTng live).

               $ babeltrace2 --input-format=lttng-live net://localhost

           Example 5. Pretty-print LTTng live events.

               $ babeltrace2 net://localhost/host/myhostname/my-session-name

           Example 6. Record LTTng live traces to the file system (as CTF 1.8
           traces).

               $ babeltrace2 net://localhost/host/myhostname/my-session-name \
                             --params=session-not-found-action=end \
                             --component=sink.ctf.fs \
                             --params='path="out-ctf-traces",ctf-version="1"'

           Example 7. Read a CTF trace as fast as possible using a dummy
           output.

               $ babeltrace2 my-trace --output-format=dummy

           Example 8. Read three CTF traces in stream intersection mode, add
           debugging information, and pretty-print them to a file.

               $ babeltrace2 ctf-trace1 ctf-trace2 ctf-trace3 --stream-intersection \
                             --debug-info --output=pretty-out

           Example 9. Pretty-print a CTF trace and traces from an explicit
           source component, with the event times showed in seconds since the
           Unix epoch.

               $ babeltrace2 ctf-trace --component=src.my-plugin.my-src \
                             --params='path="spec-trace",output-some-event-type=yes' \
                             --clock-seconds

           Example 10. Send LTTng live events to an explicit sink component.

               $ babeltrace2 net://localhost/host/myhostname/mysession \
                             --component=sink.my-plugin.my-sink

           Example 11. Trim a CTF trace, add debugging information, apply an
           explicit filter component, and write as a CTF trace.

               $ babeltrace2 /path/to/ctf/trace --timerange=22:14:38,22:15:07 \
                             --debug-info --component=filter.my-plugin.my-filter \
                             --params=criteria=xyz,ignore-abc=yes \
                             --output-format=ctf --output=out-ctf-trace

           Example 12. Print the metadata text of a CTF trace.

               $ babeltrace2 /path/to/ctf/trace --output-format=ctf-metadata

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

       Babeltrace 2 library
           BABELTRACE_EXEC_ON_ABORT=CMDLINE
               Execute the command line CMDLINE, as parsed like a UNIX 98
               shell, when any part of the Babeltrace 2 project unexpectedly
               aborts.

               The application only aborts when the executed command returns,
               ignoring its exit status.

               This environment variable is ignored when the application has
               the setuid or the setgid access right flag set.

           BABELTRACE_TERM_COLOR=(AUTO | NEVER | ALWAYS)
               Force the terminal color support for the babeltrace2(1)
               program and the project plugins.

               The available values are:

               AUTO
                   Only emit terminal color codes when the standard output
                   and error streams are connected to a color-capable
                   terminal.

               NEVER
                   Never emit terminal color codes.

               ALWAYS
                   Always emit terminal color codes.

           BABELTRACE_TERM_COLOR_BRIGHT_MEANS_BOLD=0
               Set to 0 to emit SGR (see
               <https://en.wikipedia.org/wiki/ANSI_escape_code>) codes 90
               to 97 for bright colors instead of bold (SGR code 1) and
               standard color codes (SGR codes 30 to 37).

           BABELTRACE_PLUGIN_PATH=PATHS
               Set the list of directories, in order, in which dynamic
               plugins can be found before other directories are considered
               to PATHS (colon-separated, or semicolon on Windows).

           LIBBABELTRACE2_DISABLE_PYTHON_PLUGINS=1
               Disable the loading of any Babeltrace 2 Python plugin.

           LIBBABELTRACE2_FORCE_COMPONENT_LOG_LEVEL=SPEC
               Force the log level of all or specific components added to any
               trace processing graph.

               SPEC is one of:

               •   A single log level value LVL.

                   In this case, libbabeltrace2 overrides the log level
                   specified when adding any component to any trace
                   processing graph.

               •   A semicolon-delimited list of PAT:LVL specifiers.

                   PAT is a globbing pattern where only the wildcard
                   character, *, is special: it matches zero or more
                   characters. You must escape the *, ?, [, and \ characters
                   with \.

                   LVL is a log level value.

                   In this case, libbabeltrace2 overrides the log level
                   specified when adding a component of which the name
                   matches PAT to any trace processing graph.

               libbabeltrace2 dynamically checks this environment variable
               before adding a component to a trace processing graph, meaning
               you can modify it at any time with setenv(3).

               The available values for LVL are:

               NONE, N
                   Logging is disabled.

               FATAL, F
                   Severe errors that lead the execution to abort
                   immediately.

                   This level should be enabled in production.

               ERROR, E
                   Errors that might still allow the execution to continue.

                   Usually, once one or more errors are reported at this
                   level, the application, plugin, or library won’t perform
                   any more useful task, but it should still exit cleanly.

                   This level should be enabled in production.

               WARN, WARNING, W
                   Unexpected situations which still allow the execution to
                   continue.

                   This level should be enabled in production.

               INFO, I
                   Informational messages that highlight progress or
                   important states of the application, plugins, or library.

                   This level can be enabled in production.

               DEBUG, D
                   Debugging information, with a higher level of details than
                   the TRACE level.

                   This level should NOT be enabled in production.

               TRACE, T
                   Low-level debugging context information.

                   This level should NOT be enabled in production.

               Example:

                   *ctf*:I;my-sink:D;*:W

           LIBBABELTRACE2_INIT_LOG_LEVEL=LVL
               Force the initial log level of the Babeltrace 2 library to be
               LVL.

               If this environment variable is set, then it overrides the log
               level set by the --log-level option for the Babeltrace 2
               library logger.

               The available values for LVL are:

               NONE, N
                   Logging is disabled.

               FATAL, F
                   Severe errors that lead the execution to abort
                   immediately.

                   This level should be enabled in production.

               ERROR, E
                   Errors that might still allow the execution to continue.

                   Usually, once one or more errors are reported at this
                   level, the application, plugin, or library won’t perform
                   any more useful task, but it should still exit cleanly.

                   This level should be enabled in production.

               WARN, WARNING, W
                   Unexpected situations which still allow the execution to
                   continue.

                   This level should be enabled in production.

               INFO, I
                   Informational messages that highlight progress or
                   important states of the application, plugins, or library.

                   This level can be enabled in production.

               DEBUG, D
                   Debugging information, with a higher level of details than
                   the TRACE level.

                   This level should NOT be enabled in production.

               TRACE, T
                   Low-level debugging context information.

                   This level should NOT be enabled in production.

           LIBBABELTRACE2_NO_DLCLOSE=1
               Make the Babeltrace 2 library leave any dynamically loaded
               modules (plugins and plugin providers) open at exit. This can
               be useful for debugging purposes.

           LIBBABELTRACE2_PLUGIN_PROVIDER_DIR=DIR
               Set the directory from which the Babeltrace 2 library
               dynamically loads plugin provider shared objects to DIR.

               If this environment variable is set, then it overrides the
               default plugin provider directory.

       Babeltrace 2 Python bindings
           BABELTRACE_PYTHON_BT2_LOG_LEVEL=LVL
               Force the Babeltrace 2 Python bindings log level to be LVL.

               If this environment variable is set, then it overrides the log
               level set by the --log-level option for the Python bindings
               logger.

               The available values for LVL are:

               NONE, N
                   Logging is disabled.

               FATAL, F
                   Severe errors that lead the execution to abort
                   immediately.

                   This level should be enabled in production.

               ERROR, E
                   Errors that might still allow the execution to continue.

                   Usually, once one or more errors are reported at this
                   level, the application, plugin, or library won’t perform
                   any more useful task, but it should still exit cleanly.

                   This level should be enabled in production.

               WARN, WARNING, W
                   Unexpected situations which still allow the execution to
                   continue.

                   This level should be enabled in production.

               INFO, I
                   Informational messages that highlight progress or
                   important states of the application, plugins, or library.

                   This level can be enabled in production.

               DEBUG, D
                   Debugging information, with a higher level of details than
                   the TRACE level.

                   This level should NOT be enabled in production.

               TRACE, T
                   Low-level debugging context information.

                   This level should NOT be enabled in production.

       CLI
           BABELTRACE_CLI_LOG_LEVEL=LVL
               Force the log level of the log level babeltrace2 CLI to be
               LVL.

               If this environment variable is set, then it overrides the log
               level set by the --log-level option for the CLI logger.

               The available values for LVL are:

               NONE, N
                   Logging is disabled.

               FATAL, F
                   Severe errors that lead the execution to abort
                   immediately.

                   This level should be enabled in production.

               ERROR, E
                   Errors that might still allow the execution to continue.

                   Usually, once one or more errors are reported at this
                   level, the application, plugin, or library won’t perform
                   any more useful task, but it should still exit cleanly.

                   This level should be enabled in production.

               WARN, WARNING, W
                   Unexpected situations which still allow the execution to
                   continue.

                   This level should be enabled in production.

               INFO, I
                   Informational messages that highlight progress or
                   important states of the application, plugins, or library.

                   This level can be enabled in production.

               DEBUG, D
                   Debugging information, with a higher level of details than
                   the TRACE level.

                   This level should NOT be enabled in production.

               TRACE, T
                   Low-level debugging context information.

                   This level should NOT be enabled in production.

           BABELTRACE_CLI_WARN_COMMAND_NAME_DIRECTORY_CLASH=0
               Disable the warning message which babeltrace2-convert(1)
               prints when you convert a trace with a relative path that’s
               also the name of a babeltrace2 command.

           BABELTRACE_DEBUG=1
               Legacy variable: equivalent to setting the --log-level option
               to TRACE.

           BABELTRACE_VERBOSE=1
               Legacy variable: equivalent to setting the --log-level option
               to INFO.

## [](#FILES)FILES

           $HOME/.local/lib/babeltrace2/plugins
               User plugin directory.

           /usr/local/lib/babeltrace2/plugins
               System plugin directory.

           /usr/local/lib/babeltrace2/plugin-providers
               System plugin provider directory.

## [](#EXIT_STATUS)EXIT STATUS

           0 on success, 1 otherwise.

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

           This command is part of the Babeltrace 2 project.

           Babeltrace is distributed under the MIT license (see
           <https://opensource.org/licenses/MIT>).

## [](#SEE_ALSO)SEE ALSO

           babeltrace2-intro(7), babeltrace2(1), babeltrace2-run(1)

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

    Babeltrace 2.2.0rc1          13 December 2024      BABELTRACE2-CONVERT(1)

------------------------------------------------------------------------

Pages that refer to this page: [babeltrace2(1)](../man1/babeltrace2.1.html),  [babeltrace2-convert(1)](../man1/babeltrace2-convert.1.html),  [babeltrace2-help(1)](../man1/babeltrace2-help.1.html),  [babeltrace2-list-plugins(1)](../man1/babeltrace2-list-plugins.1.html),  [babeltrace2-query(1)](../man1/babeltrace2-query.1.html),  [babeltrace2-run(1)](../man1/babeltrace2-run.1.html),  [babeltrace2-intro(7)](../man7/babeltrace2-intro.7.html),  [babeltrace2-query-babeltrace.support-info(7)](../man7/babeltrace2-query-babeltrace.support-info.7.html),  [babeltrace2-query-babeltrace.trace-infos(7)](../man7/babeltrace2-query-babeltrace.trace-infos.7.html),  [babeltrace2-source.ctf.fs(7)](../man7/babeltrace2-source.ctf.fs.7.html)

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
