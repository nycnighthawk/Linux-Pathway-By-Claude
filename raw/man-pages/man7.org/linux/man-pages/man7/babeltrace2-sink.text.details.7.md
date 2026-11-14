---
{"title": "babeltrace2-sink.text.details(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/babeltrace2-sink.text.details.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# babeltrace2-sink.text.details(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INITIALIZATION PARAMETERS](#INITIALIZATION_PARAMETERS) \| [PORTS](#PORTS) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [BUGS](#BUGS) \| [RESOURCES](#RESOURCES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BABELTRACE2-SINK.(7)       Babeltrace 2 manual       BABELTRACE2-SINK.(7)

## [](#NAME)NAME

           babeltrace2-sink.text.details - Babeltrace 2: Detailed plain text
           sink component class

## [](#DESCRIPTION)DESCRIPTION

           A Babeltrace 2 sink.text.details component deterministically
           prints the messages it consumes, with all the possible details, to
           the standard output.

                           +-------------------+
                           | sink.text.details |
                           |                   +--> Detailed messages to the
               Messages -->@ in                |    standard output
                           +-------------------+

           See babeltrace2-intro(7) to learn more about the Babeltrace 2
           project and its core concepts.

           The purpose of a sink.text.details component is to always print
           the same text for the same sequence of consumed messages, whatever
           the build configuration of the Babeltrace 2 project. This can be
           helpful for testing, debugging, and support.

           The output format is optimized for human reading, with colors when
           the terminal supports it. You can control how the component prints
           color codes with the color parameter.

           To achieve a reproducible output, a sink.text.details component
           sorts the members of all unordered sets before it prints them. For
           example, the component sorts enumeration field class mappings by
           label and, for each mapping, sorts the contained ranges.

           In normal mode, each message has at least three lines, the three
           first being:

            1. Timing information (cycles and nanoseconds since origin).

               Example:

                   [102,423,274,041,829 cycles, 1,441,852,841,550,867,846 ns from origin]

            2. Unique stream identifier.

               To be able to follow a specific trace object (the name and
               UUID properties of a trace object are optional), the component
               assigns a unique numeric ID to the trace object when it first
               encounters it in a stream beginning message.

               Example:

                   {Trace 1, Stream class ID 0, Stream ID 2}

            3. Message type and basic information.

               Examples:

                   Packet beginning:

                   Event `lttng_ust_statedump:build_id` (Class ID 2):

           What follows depend on the specific message type. The component
           prints all the available properties and fields in a
           human-readable, structured format.

           When a sink.text.details component consumes a stream beginning or
           an event message, it can print a metadata block for all the
           metadata objects which it did not print yet. You can use the with-
           metadata parameter to disable this.

           You can hide specific properties with the with-stream-class-name,
           with-stream-class-namespace, with-stream-name, with-time, with-
           trace-name, with-uid, and with-uuid parameters.

           To make the component hide many message details and print a single
           message per line, you can enable the compact mode with the compact
           parameter.

## [](#INITIALIZATION_PARAMETERS)INITIALIZATION PARAMETERS

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

           compact=VAL [optional boolean]
               If VAL is true, then enable compact mode.

               In compact mode, the component prints one line per message,
               omitting many details about messages. This is useful if you
               only need the time, type, and very basic information of
               messages.

               In compact mode, the component still prints the full metadata
               blocks. You can remove such blocks with the with-metadata
               parameter.

               Default: false.

           with-metadata=VAL [optional boolean]
               If VAL is false, then don’t print metadata blocks.

               Default: true.

           with-stream-class-name=VAL [optional boolean]
               If VAL is false, then don’t print stream class names.

               Default: true.

           with-stream-class-namespace=VAL [optional boolean]
               If VAL is false, then don’t print stream class namespaces.

               Default: true.

           with-stream-name=VAL [optional boolean]
               If VAL is false, then don’t print stream names.

               Default: true.

           with-time=VAL [optional boolean]
               If VAL is false, then don’t print timing information.

               Default: true.

           with-trace-name=VAL [optional boolean]
               If VAL is false, then don’t print trace names.

               Default: true.

           with-uid=VAL [optional boolean]
               If VAL is false, then don’t print unique IDs (UIDs).

               Default: true.

           with-uuid=VAL [optional boolean]
               If VAL is false, then don’t print UUIDs.

               Default: true.

## [](#PORTS)PORTS

               +-------------------+
               | sink.text.details |
               |                   |
               @ in                |
               +-------------------+

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

Pages that refer to this page: [babeltrace2(1)](../man1/babeltrace2.1.html),  [babeltrace2-plugin-text(7)](../man7/babeltrace2-plugin-text.7.html)

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
