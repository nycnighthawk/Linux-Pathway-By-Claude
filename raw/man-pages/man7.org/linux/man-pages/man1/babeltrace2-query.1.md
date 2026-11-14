---
{"title": "babeltrace2-query(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/babeltrace2-query.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# babeltrace2-query(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [FILES](#FILES) \| [EXIT STATUS](#EXIT_STATUS) \| [BUGS](#BUGS) \| [RESOURCES](#RESOURCES) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BABELTRACE2-QUERY(1)       Babeltrace 2 manual       BABELTRACE2-QUERY(1)

## [](#NAME)NAME

           babeltrace2-query - Query an object from a Babeltrace 2 component
           class

## [](#SYNOPSIS)SYNOPSIS

           babeltrace2 [GENERAL OPTIONS] query [--params=PARAMS]
                       COMP-CLS-TYPE.PLUGIN-NAME.COMP-CLS-NAME OBJECT

## [](#DESCRIPTION)DESCRIPTION

           The query command queries the object named OBJECT from the
           component class named COMP-CLS-NAME of the type COMP-CLS-TYPE
           found in the Babeltrace 2 plugin named PLUGIN-NAME and prints the
           results.

           See babeltrace2-intro(7) to learn more about the Babeltrace 2
           project and its core concepts.

           The available values for COMP-CLS-TYPE are:

           source, src
               Source component class.

           filter, flt
               Filter component class.

           sink
               Sink component class.

           The exact object names and the parameters that a given component
           class expects are described in its own documentation.
           babeltrace2-help(1) can generally provide this information.

           You can use the --params option to pass parameters to the query
           operation of the component class.

           The output of the query command can look like YAML (see
           <https://yaml.org/>), but it’s not guaranteed to be
           YAML-compliant.

           See “EXAMPLES” for usage examples.

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

       Query parameters
           -p PARAMS, --params=PARAMS
               Set the query parameters to PARAMS.

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

       Command information
           -h, --help
               Show the command help and quit.

## [](#EXAMPLES)EXAMPLES

           Example 1. Query the available tracing sessions of a local LTTng
           relay daemon.

               $ babeltrace2 query src.ctf.lttng-live sessions \
                                   --params='url="net://localhost"'

           Example 2. Query the metadata info (includes the decoded plain
           text) of a CTF trace located on the local file system.

               $ babeltrace2 query src.ctf.fs metadata-info \
                                   --params='inputs=["/path/to/trace"]'

           Example 3. Query the trace infos of a CTF trace located on the
           local file system.

               $ babeltrace2 query src.ctf.fs babeltrace.trace-infos \
                                   --params='inputs=["/path/to/trace"]'

           Example 4. Query some object from a sink component class without
           parameters.

               $ babeltrace2 query sink.my-plugin.my-sink some-object

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

           babeltrace2-intro(7), babeltrace2(1)

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

    Babeltrace 2.2.0rc1         14 September 2019        BABELTRACE2-QUERY(1)

------------------------------------------------------------------------

Pages that refer to this page: [babeltrace2(1)](../man1/babeltrace2.1.html),  [babeltrace2-intro(7)](../man7/babeltrace2-intro.7.html),  [babeltrace2-query-babeltrace.support-info(7)](../man7/babeltrace2-query-babeltrace.support-info.7.html),  [babeltrace2-query-babeltrace.trace-infos(7)](../man7/babeltrace2-query-babeltrace.trace-infos.7.html)

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
