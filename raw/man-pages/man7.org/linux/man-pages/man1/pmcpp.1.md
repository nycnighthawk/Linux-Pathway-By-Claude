---
{"title": "pmcpp(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmcpp.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmcpp(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMCPP(1)                 General Commands Manual                 PMCPP(1)

## [](#NAME)NAME

           pmcpp - simple preprocessor for the Performance Co-Pilot

## [](#SYNOPSIS)SYNOPSIS

           pmcpp [-Prs?]  [-D name[=value] ...]  [-I dir ...]  [[infile]
           [outfile]]

## [](#DESCRIPTION)DESCRIPTION

           pmcpp provides a very simple pre-processor originally designed for
           manipulating Performance Metric Name Space (PMNS) files for the
           Performance Co-Pilot (PCP), but later generalized to provide
           conditional blocks, include file processing, in-line shell command
           execution and macro substitution for arbitrary files.  It is most
           commonly used internally to process the PMNS file(s) after
           pmLoadNameSpace(3) or pmLoadASCIINameSpace(3) is called and to
           pre-process the configuration files for pmlogger(1).

           Input lines are read from infile (or standard input if infile is
           not specified), processed and written to outfile (standard output
           if outfile is not specified).

           All C-style comments of the form /* ... */ are stripped from the
           input stream.

           There are no predefined macros for pmcpp although macros may be
           defined on the command line using the -D option, where name and
           value must follow the same rules as described below for the
           #define directive.

           pmcpp accepts the following directives in the input stream (like
           cpp(1)):

           •  #include "filename"
              or
              #include <filename>
              In either case the directory search path for filename tries
              filename first, then the directory for the command line infile
              (if any), followed by any directories named in -I command line
              arguments, and finally the $PCP_VAR_DIR/pmns directory (the
              latter is for backwards compatibility with earlier versions of
              pmcpp and the implied used from pmLoadASCIINameSpace(3)).
              #include directives may be nested, up to a maximum depth of 5.

           •  #shell "command"
              or
              #shell 'command'
              The shell command will be executed and the standard output is
              inserted into the stream of data to be processed by pmcpp.
              Functionally this is similar to a #include directive, except
              input lines are read from a command rather than a file.  The
              #shell directive is most useful for including or excluding
              #define or #undef directives based on run-time logic in the
              command.

           •  #define name value
              or
              #define name "value"
              or
              #define name 'value'
              Defines a value for the macro name which must be a valid C-
              style name, so leading alphabetic or underscore followed by
              zero or more alphanumerics or underscores.  value is optional
              (and defaults to an empty string).  There is no character
              escape mechanism, but either single quotes or double quotes may
              be used to define a value with special characters or embedded
              horizontal white space (no newlines).

           •  #undef name
              Removes the macro definition, if any, for name.

           •  #ifdef name
              ...
              #endif
              or
              #ifndef name
              ...
              #endif
              The enclosing lines will be stripped or included, depending if
              the macro name is defined or not.

           •  #else
              Within a #ifdef or #ifndef block, #else may be used to delimit
              lines to be included if the preceding ``if'' condition is
              false.

           Macro substitution is achieved by breaking the input stream into
           words separated by white space or characters that are not valid in
           a macro name, i.e. not alphanumeric and not underscore.  Each word
           is checked and if it matches a macro name, the word is replaced by
           the macro value, otherwise the word is unchanged.

           There is generally one output line for each input line, although
           the line may be empty if the text has been stripped due to the
           handling of comments or conditional directives.  When there is a
           change in the input stream, an additional output line is generated
           of the form:

                     # lineno "filename"

           to indicate the following line of output corresponds to line
           number lineno of the input file filename.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -D name[=value], --define=name[=value]
                Defines a macro with an optional value, as described earlier.

           -I dir, --include=dir
                An additional directory to search for include files.

           -P   Suppresses the generation of the linemarker lines, described
                above.

           -s, --shell
                Changes the expected input style from C-like to shell-like
                (where # is a comment prefix).  This forces the following
                changes in pmcpp behaviour:
                •  The control prefix character changes from # to %, so for
                   example %include instead of #include, and %ifdef instead
                   of #ifdef.
                •  No C-style comment stripping is performed.

           -r, --restrict
                Provide finer control of macro expansion - this option
                restricts macro substitution to words that match the patterns
                #name or #{name} or if -s is specified, then %name or
                %{name}.  In this mode, the macro name alone in the input
                stream will never be expanded, however in control lines (like
                #ifdef) the macro name should appear alone with out the
                prefix character or the curly braces (refer to the EXAMPLES
                below).

           -?, --help
                Display usage message and exit.

           Important cpp(1) features that are not supported by pmcpp include:
           •  Macros with parameters - the pmcpp macros support only
              parameterless string substitution.
           •  #if expr
              ...
              #endif
           •  Nested use of #ifdef or #ifndef.
           •  Stripping C++ style comments, as in // comment.
           •  Error recovery - the first error encountered by pmcpp will be
              fatal.
           •  cpp(1) command line options like -o, -W, -U, and -x.

## [](#EXAMPLES)EXAMPLES

           ┌──────────────────────────────────────────────┐
           │ Command: pmcpp                               │
           ├────────────────────────┬─────────────────────┤
           │ Input                  │ Output              │
           ├────────────────────────┼─────────────────────┤
           │                        │ # 1 "<stdin>"       │
           │ #define MYDOMAIN 27    │                     │
           │                        │                     │
           │ root {                 │ root {              │
           │     foo   MYDOMAIN:0:0 │    foo   27:0:0     │
           │ }                      │ }                   │
           └────────────────────────┴─────────────────────┘

           For the following examples, the file frequencies contains the
           lines:
                   %define dk_freq 1minute
                   %define cpu_freq '15 sec'

           ┌────────────────────────────────────────────────────────────────────┐
           │ Command: pmcpp -rs                                                 │
           ├───────────────────────────────────┬────────────────────────────────┤
           │ Input                             │ Output                         │
           ├───────────────────────────────────┼────────────────────────────────┤
           │ # get logging frequencies         │ # get logging frequencies      │
           │ # e.g. dk_freq macro              │ # e.g. dk_freq macro           │
           │ %include "frequencies"            │                                │
           │                                   │                                │
           │ log mandatory on %dk_freq {       │ log mandatory on 1minute {     │
           │     disk.dev                      │    disk.dev                    │
           │ }                                 │ }                              │
           │                                   │                                │
           │ # note no %want_cpu here          │ # note no %want_cpu here       │
           │ %ifdef want_cpu                   │                                │
           │ %define cpu_pfx 'kernel.all.cpu.' │                                │
           │ log mandatory on %cpu_freq {      │                                │
           │     %{cpu_pfx}user                │                                │
           │     %{cpu_pfx}sys                 │                                │
           │ }                                 │                                │
           │ %endif                            │                                │
           └───────────────────────────────────┴────────────────────────────────┘

           ┌───────────────────────────────────────────────────────────────────┐
           │ Command: pmcpp -rs -D want_cpu                                    │
           ├───────────────────────────────────┬───────────────────────────────┤
           │ Input                             │ Output                        │
           ├───────────────────────────────────┼───────────────────────────────┤
           │ # get logging frequencies         │ # get logging frequencies     │
           │ # e.g. dk_freq macro              │ # e.g. dk_freq macro          │
           │ %include "frequencies"            │                               │
           │                                   │                               │
           │ log mandatory on %dk_freq {       │ log mandatory on 1min {       │
           │     disk.dev                      │    disk.dev                   │
           │ }                                 │ }                             │
           │                                   │                               │
           │ # note no %want_cpu here          │ # note no %want_cpu here      │
           │ %ifdef want_cpu                   │                               │
           │ %define cpu_pfx 'kernel.all.cpu.' │                               │
           │ log mandatory on %cpu_freq {      │ log mandatory on 15 sec {     │
           │     %{cpu_pfx}user                │    kernel.all.cpu.user        │
           │     %{cpu_pfx}sys                 │    kernel.all.cpu.sys         │
           │ }                                 │ }                             │
           │ %endif                            │                               │
           └───────────────────────────────────┴───────────────────────────────┘

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#SEE_ALSO)SEE ALSO

           cpp(1), pmLoadASCIINameSpace(3), pmLoadNameSpace(3), pcp.conf(5),
           pcp.env(5) and PMNS(5).

## [](#COLOPHON)COLOPHON

           This page is part of the PCP (Performance Co-Pilot) project.
           Information about the project can be found at 
           ⟨http://www.pcp.io/⟩.  If you have a bug report for this manual
           page, send it to pcp@groups.io.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/performancecopilot/pcp.git⟩ on 2026-08-04.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-08-04.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Performance Co-Pilot                                             PMCPP(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmlogger(1)](../man1/pmlogger.1.html),  [pmloadasciinamespace(3)](../man3/pmloadasciinamespace.3.html),  [pmns(5)](../man5/pmns.5.html)

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
