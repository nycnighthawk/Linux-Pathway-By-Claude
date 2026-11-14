---
{"title": "getopts(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/getopts.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# getopts(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GETOPTS(1P)             POSIX Programmer's Manual             GETOPTS(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           getopts — parse utility options

## [](#SYNOPSIS)SYNOPSIS

           getopts optstring name [arg...]

## [](#DESCRIPTION)DESCRIPTION

           The getopts utility shall retrieve options and option-arguments
           from a list of parameters. It shall support the Utility Syntax
           Guidelines 3 to 10, inclusive, described in the Base Definitions
           volume of POSIX.1‐2017, Section 12.2, Utility Syntax Guidelines.

           Each time it is invoked, the getopts utility shall place the value
           of the next option in the shell variable specified by the name
           operand and the index of the next argument to be processed in the
           shell variable OPTIND.  Whenever the shell is invoked, OPTIND
           shall be initialized to 1.

           When the option requires an option-argument, the getopts utility
           shall place it in the shell variable OPTARG.  If no option was
           found, or if the option that was found does not have an option-
           argument, OPTARG shall be unset.

           If an option character not contained in the optstring operand is
           found where an option character is expected, the shell variable
           specified by name shall be set to the <question-mark> ('?')
           character. In this case, if the first character in optstring is a
           <colon> (':'), the shell variable OPTARG shall be set to the
           option character found, but no output shall be written to standard
           error; otherwise, the shell variable OPTARG shall be unset and a
           diagnostic message shall be written to standard error. This
           condition shall be considered to be an error detected in the way
           arguments were presented to the invoking application, but shall
           not be an error in getopts processing.

           If an option-argument is missing:

            *  If the first character of optstring is a <colon>, the shell
               variable specified by name shall be set to the <colon>
               character and the shell variable OPTARG shall be set to the
               option character found.

            *  Otherwise, the shell variable specified by name shall be set
               to the <question-mark> character, the shell variable OPTARG
               shall be unset, and a diagnostic message shall be written to
               standard error. This condition shall be considered to be an
               error detected in the way arguments were presented to the
               invoking application, but shall not be an error in getopts
               processing; a diagnostic message shall be written as stated,
               but the exit status shall be zero.

           When the end of options is encountered, the getopts utility shall
           exit with a return value greater than zero; the shell variable
           OPTIND shall be set to the index of the first operand, or the
           value "$#"+1 if there are no operands; the name variable shall be
           set to the <question-mark> character. Any of the following shall
           identify the end of options: the first "--" argument that is not
           an option-argument, finding an argument that is not an option-
           argument and does not begin with a '-', or encountering an error.

           The shell variables OPTIND and OPTARG shall be local to the caller
           of getopts and shall not be exported by default.

           The shell variable specified by the name operand, OPTIND, and
           OPTARG shall affect the current shell execution environment; see
           Section 2.12, Shell Execution Environment.

           If the application sets OPTIND to the value 1, a new set of
           parameters can be used: either the current positional parameters
           or new arg values. Any other attempt to invoke getopts multiple
           times in a single shell execution environment with parameters
           (positional parameters or arg operands) that are not the same in
           all invocations, or with an OPTIND value modified to be a value
           other than 1, produces unspecified results.

## [](#OPTIONS)OPTIONS

           None.

## [](#OPERANDS)OPERANDS

           The following operands shall be supported:

           optstring A string containing the option characters recognized by
                     the utility invoking getopts.  If a character is
                     followed by a <colon>, the option shall be expected to
                     have an argument, which should be supplied as a separate
                     argument. Applications should specify an option
                     character and its option-argument as separate arguments,
                     but getopts shall interpret the characters following an
                     option character requiring arguments as an argument
                     whether or not this is done. An explicit null option-
                     argument need not be recognized if it is not supplied as
                     a separate argument when getopts is invoked. (See also
                     the getopt() function defined in the System Interfaces
                     volume of POSIX.1‐2017.) The characters <question-mark>
                     and <colon> shall not be used as option characters by an
                     application. The use of other option characters that are
                     not alphanumeric produces unspecified results. If the
                     option-argument is not supplied as a separate argument
                     from the option character, the value in OPTARG shall be
                     stripped of the option character and the '-'.  The first
                     character in optstring determines how getopts behaves if
                     an option character is not known or an option-argument
                     is missing.

           name      The name of a shell variable that shall be set by the
                     getopts utility to the option character that was found.

           The getopts utility by default shall parse positional parameters
           passed to the invoking shell procedure. If args are given, they
           shall be parsed instead of the positional parameters.

## [](#STDIN)STDIN

           Not used.

## [](#INPUT_FILES)INPUT FILES

           None.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           The following environment variables shall affect the execution of
           getopts:

           LANG      Provide a default value for the internationalization
                     variables that are unset or null. (See the Base
                     Definitions volume of POSIX.1‐2017, Section 8.2,
                     Internationalization Variables for the precedence of
                     internationalization variables used to determine the
                     values of locale categories.)

           LC_ALL    If set to a non-empty string value, override the values
                     of all the other internationalization variables.

           LC_CTYPE  Determine the locale for the interpretation of sequences
                     of bytes of text data as characters (for example,
                     single-byte as opposed to multi-byte characters in
                     arguments and input files).

           LC_MESSAGES
                     Determine the locale that should be used to affect the
                     format and contents of diagnostic messages written to
                     standard error.

           NLSPATH   Determine the location of message catalogs for the
                     processing of LC_MESSAGES.

           OPTIND    This variable shall be used by the getopts utility as
                     the index of the next argument to be processed.

## [](#ASYNCHRONOUS_EVENTS)ASYNCHRONOUS EVENTS

           Default.

## [](#STDOUT)STDOUT

           Not used.

## [](#STDERR)STDERR

           Whenever an error is detected and the first character in the
           optstring operand is not a <colon> (':'), a diagnostic message
           shall be written to standard error with the following information
           in an unspecified format:

            *  The invoking program name shall be identified in the message.
               The invoking program name shall be the value of the shell
               special parameter 0 (see Section 2.5.2, Special Parameters) at
               the time the getopts utility is invoked. A name equivalent to:

                   basename "$0"

               may be used.

            *  If an option is found that was not specified in optstring,
               this error is identified and the invalid option character
               shall be identified in the message.

            *  If an option requiring an option-argument is found, but an
               option-argument is not found, this error shall be identified
               and the invalid option character shall be identified in the
               message.

## [](#OUTPUT_FILES)OUTPUT FILES

           None.

## [](#EXTENDED_DESCRIPTION)EXTENDED DESCRIPTION

           None.

## [](#EXIT_STATUS)EXIT STATUS

           The following exit values shall be returned:

            0    An option, specified or unspecified by optstring, was found.

           >0    The end of options was encountered or an error occurred.

## [](#CONSEQUENCES_OF_ERRORS)CONSEQUENCES OF ERRORS

           Default.

           The following sections are informative.

## [](#APPLICATION_USAGE)APPLICATION USAGE

           Since getopts affects the current shell execution environment, it
           is generally provided as a shell regular built-in. If it is called
           in a subshell or separate utility execution environment, such as
           one of the following:

               (getopts abc value "$@")
               nohup getopts ...
               find . -exec getopts ... \;

           it does not affect the shell variables in the caller's
           environment.

           Note that shell functions share OPTIND with the calling shell even
           though the positional parameters are changed. If the calling shell
           and any of its functions uses getopts to parse arguments, the
           results are unspecified.

## [](#EXAMPLES)EXAMPLES

           The following example script parses and displays its arguments:

               aflag=
               bflag=
               while getopts ab: name
               do
                   case $name in
                   a)    aflag=1;;
                   b)    bflag=1
                         bval="$OPTARG";;
                   ?)   printf "Usage: %s: [-a] [-b value] args\n" $0
                         exit 2;;
                   esac
               done
               if [ ! -z "$aflag" ]; then
                   printf "Option -a specified\n"
               fi
               if [ ! -z "$bflag" ]; then
                   printf 'Option -b "%s" specified\n' "$bval"
               fi
               shift $(($OPTIND - 1))
               printf "Remaining arguments are: %s\n$*"

## [](#RATIONALE)RATIONALE

           The getopts utility was chosen in preference to the System V
           getopt utility because getopts handles option-arguments containing
           <blank> characters.

           The OPTARG variable is not mentioned in the ENVIRONMENT VARIABLES
           section because it does not affect the execution of getopts; it is
           one of the few ``output-only'' variables used by the standard
           utilities.

           The <colon> is not allowed as an option character because that is
           not historical behavior, and it violates the Utility Syntax
           Guidelines. The <colon> is now specified to behave as in the
           KornShell version of the getopts utility; when used as the first
           character in the optstring operand, it disables diagnostics
           concerning missing option-arguments and unexpected option
           characters. This replaces the use of the OPTERR variable that was
           specified in an early proposal.

           The formats of the diagnostic messages produced by the getopts
           utility and the getopt() function are not fully specified because
           implementations with superior (``friendlier'') formats objected to
           the formats used by some historical implementations. The standard
           developers considered it important that the information in the
           messages used be uniform between getopts and getopt().  Exact
           duplication of the messages might not be possible, particularly if
           a utility is built on another system that has a different getopt()
           function, but the messages must have specific information included
           so that the program name, invalid option character, and type of
           error can be distinguished by a user.

           Only a rare application program intercepts a getopts standard
           error message and wants to parse it. Therefore, implementations
           are free to choose the most usable messages they can devise. The
           following formats are used by many historical implementations:

               "%s: illegal option -- %c\n", <program name>, <option character>

               "%s: option requires an argument -- %c\n", <program name>, \
                   <option character>

           Historical shells with built-in versions of getopt() or getopts
           have used different formats, frequently not even indicating the
           option character found in error.

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           None.

## [](#SEE_ALSO)SEE ALSO

           Section 2.5.2, Special Parameters

           The Base Definitions volume of POSIX.1‐2017, Chapter 8,
           Environment Variables, Section 12.2, Utility Syntax Guidelines

           The System Interfaces volume of POSIX.1‐2017, getopt(3p)

## [](#COPYRIGHT)COPYRIGHT

           Portions of this text are reprinted and reproduced in electronic
           form from IEEE Std 1003.1-2017, Standard for Information
           Technology -- Portable Operating System Interface (POSIX), The
           Open Group Base Specifications Issue 7, 2018 Edition, Copyright
           (C) 2018 by the Institute of Electrical and Electronics Engineers,
           Inc and The Open Group.  In the event of any discrepancy between
           this version and the original IEEE and The Open Group Standard,
           the original IEEE and The Open Group Standard is the referee
           document. The original Standard can be obtained online at
           http://www.opengroup.org/unix/online.html .

           Any typographical or formatting errors that appear in this page
           are most likely to have been introduced during the conversion of
           the source files to man page format. To report such errors, see
           https://www.kernel.org/doc/man-pages/reporting_bugs.html .

    IEEE/The Open Group                2017                       GETOPTS(1P)

------------------------------------------------------------------------

Pages that refer to this page: [pax(1p)](../man1/pax.1p.html),  [getopt(3p)](../man3/getopt.3p.html)

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
