---
{"title": "babeltrace2-sink.text.pretty(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/babeltrace2-sink.text.pretty.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# babeltrace2-sink.text.pretty(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INITIALIZATION PARAMETERS](#INITIALIZATION_PARAMETERS) \| [PORTS](#PORTS) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [BUGS](#BUGS) \| [RESOURCES](#RESOURCES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BABELTRACE2-SINK.(7)       Babeltrace 2 manual       BABELTRACE2-SINK.(7)

## [](#NAME)NAME

           babeltrace2-sink.text.pretty - Babeltrace 2: Pretty-printing sink
           component class

## [](#DESCRIPTION)DESCRIPTION

           A Babeltrace 2 sink.text.pretty component pretty-prints the
           events, discarded events, and discarded packets messages it
           consumes to the standard output or to a file.

                           +------------------+
                           | sink.text.pretty |
                           |                  +--> Pretty-printed messages to
               Messages -->@ in               |    the standard output or a file and
                           +------------------+    to the standard error

           See babeltrace2-intro(7) to learn more about the Babeltrace 2
           project and its core concepts.

           By default, a sink.text.pretty component pretty-prints to the
           standard output. You can use the path parameter to make the
           component write to a file instead.

           The component prints warnings on the standard error stream when it
           consumes a discarded events or discarded packets message.

           If you don’t use the path parameter and the standard output of the
           application is connected to a color-capable terminal, the
           component emits terminal color codes to enhance the text output.
           You can use the color parameter to force the color support or to
           disable it.

           This component class is equivalent to the text output format of
           babeltrace(1) (Babeltrace 1 command-line tool).

## [](#INITIALIZATION_PARAMETERS)INITIALIZATION PARAMETERS

           clock-cycles=VAL [optional boolean]
               If VAL is true, then print event times in clock cycles instead
               of hours, minutes, seconds, and nanoseconds.

               Default: false.

           clock-date=VAL [optional boolean]
               If VAL is true, then print event times and dates.

               Default: false.

           clock-gmt=VAL [optional boolean]
               If VAL is true, then print event times in the GMT time zone
               instead of the local time zone.

               Default: false.

           clock-seconds=VAL [optional boolean]
               If VAL is true, then print event times in seconds instead of
               hours, minutes, seconds, and nanoseconds.

               Default: false.

           color=(never | auto | always) [optional string]
               Force the terminal color support, one of:

               auto (default)
                   Only emit terminal color codes when the standard output
                   and error streams are connected to a color-capable
                   terminal.

               never
                   Never emit terminal color codes.

               always
                   Always emit terminal color codes.

               The BABELTRACE_TERM_COLOR environment variable overrides this
               parameter.

           field-default=(show | hide) [optional string]
               By default, show or hide all the fields. This sets the default
               value of all the parameters which start with field-.

           field-emf=VAL [optional boolean]
               Show or hide the Eclipse Modeling Framework URI field of the
               event.

               Default, depending on the field-default parameter:

               show
                   True

               hide
                   False

               Not set
                   False

           field-loglevel=VAL [optional boolean]
               Show or hide the logging level field of the event.

               Default, depending on the field-default parameter:

               show
                   True

               hide
                   False

               Not set
                   False

           field-trace=VAL [optional boolean]
               Show or hide the trace name field.

               Default, depending on the field-default parameter:

               show
                   True

               hide
                   False

               Not set
                   False

           field-trace:domain=VAL [optional boolean]
               Show or hide the tracing domain field.

               Default, depending on the field-default parameter:

               show
                   True

               hide
                   False

               Not set
                   False

           field-trace:hostname=VAL [optional boolean]
               Show or hide the hostname field.

               Default, depending on the field-default parameter:

               show
                   True

               hide
                   False

               Not set
                   True

           field-trace:procname=VAL [optional boolean]
               Show or hide the process name field.

               Default, depending on the field-default parameter:

               show
                   True

               hide
                   False

               Not set
                   True

           field-trace:vpid=VAL [optional boolean]
               Show or hide the virtual process ID field.

               Default, depending on the field-default parameter:

               show
                   True

               hide
                   False

               Not set
                   True

           name-default=(show | hide) [optional string]
               By default, show or hide all the names. This sets the default
               value of all the parameters which start with name-.

           name-header=VAL [optional boolean]
               Show or hide the field names in the header scopes.

               Default, depending on the name-default parameter:

               show
                   True

               hide
                   False

               Not set
                   False

           name-context=VAL [optional boolean]
               Show or hide the field names in the context scopes.

               Default, depending on the name-default parameter:

               show
                   True

               hide
                   False

               Not set
                   True

           name-payload=VAL [optional boolean]
               Show or hide the field names in the event payload scopes.

               Default, depending on the name-default parameter:

               show
                   True

               hide
                   False

               Not set
                   True

           name-scope=VAL [optional boolean]
               Show or hide the scope names.

               Default, depending on the name-default parameter:

               show
                   True

               hide
                   False

               Not set
                   False

           no-delta=VAL [optional boolean]
               If VAL is true, then don’t print the time delta between
               consecutive lines.

               Default: false.

           path=PATH [optional string]
               Print the text output to the file PATH instead of the standard
               output.

           print-enum-flags=VAL [optional boolean]
               If VAL if true, then try to print enumeration field values as
               a pipe-delimited (|) list of bit flags, if it applies.

               When printing the value of an enumeration field without any
               corresponding mapping, a sink.text.pretty component splits the
               value into its individual bit values: if each set bit has a
               corresponding mapping, then it considers that those mappings
               are in fact bit flags.

               If a set bit has no corresponding mapping, then the component
               prints <unknown>.

               Default: false.

           verbose=VAL [optional boolean]
               If VAL if true, then turn the verbose mode on.

               Default: false.

## [](#PORTS)PORTS

               +------------------+
               | sink.text.pretty |
               |                  |
               @ in               |
               +------------------+

       Input
           in
               Single input port.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

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

           babeltrace2-intro(7), babeltrace2-plugin-text(7)

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

    Babeltrace 2.2.0rc1          15 January 2025         BABELTRACE2-SINK.(7)

------------------------------------------------------------------------

Pages that refer to this page: [babeltrace2(1)](../man1/babeltrace2.1.html),  [babeltrace2-convert(1)](../man1/babeltrace2-convert.1.html),  [babeltrace2-plugin-text(7)](../man7/babeltrace2-plugin-text.7.html)

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
