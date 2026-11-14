---
{"title": "unexpand(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/unexpand.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# unexpand(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UNEXPAND(1P)            POSIX Programmer's Manual            UNEXPAND(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           unexpand — convert spaces to tabs

## [](#SYNOPSIS)SYNOPSIS

           unexpand [-a|-t tablist] [file...]

## [](#DESCRIPTION)DESCRIPTION

           The unexpand utility shall copy files or standard input to
           standard output, converting <blank> characters at the beginning of
           each line into the maximum number of <tab> characters followed by
           the minimum number of <space> characters needed to fill the same
           column positions originally filled by the translated <blank>
           characters. By default, tabstops shall be set at every eighth
           column position. Each <backspace> shall be copied to the output,
           and shall cause the column position count for tab calculations to
           be decremented; the count shall never be decremented to a value
           less than one.

## [](#OPTIONS)OPTIONS

           The unexpand utility shall conform to the Base Definitions volume
           of POSIX.1‐2017, Section 12.2, Utility Syntax Guidelines.

           The following options shall be supported:

           -a        In addition to translating <blank> characters at the
                     beginning of each line, translate all sequences of two
                     or more <blank> characters immediately preceding a tab
                     stop to the maximum number of <tab> characters followed
                     by the minimum number of <space> characters needed to
                     fill the same column positions originally filled by the
                     translated <blank> characters.

           -t tablist
                     Specify the tab stops. The application shall ensure that
                     the tablist option-argument is a single argument
                     consisting of a single positive decimal integer or
                     multiple positive decimal integers, separated by <blank>
                     or <comma> characters, in ascending order. If a single
                     number is given, tabs shall be set tablist column
                     positions apart instead of the default 8. If multiple
                     numbers are given, the tabs shall be set at those
                     specific column positions.

                     The application shall ensure that each tab-stop position
                     N is an integer value greater than zero, and the list
                     shall be in strictly ascending order. This is taken to
                     mean that, from the start of a line of output, tabbing
                     to position N shall cause the next character output to
                     be in the (N+1)th column position on that line. When the
                     -t option is not specified, the default shall be the
                     equivalent of specifying -t 8 (except for the
                     interaction with -a, described below).

                     No <space>-to-<tab> conversions shall occur for
                     characters at positions beyond the last of those
                     specified in a multiple tab-stop list.

                     When -t is specified, the presence or absence of the -a
                     option shall be ignored; conversion shall not be limited
                     to the processing of leading <blank> characters.

## [](#OPERANDS)OPERANDS

           The following operand shall be supported:

           file      A pathname of a text file to be used as input.

## [](#STDIN)STDIN

           See the INPUT FILES section.

## [](#INPUT_FILES)INPUT FILES

           The input files shall be text files.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           The following environment variables shall affect the execution of
           unexpand:

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
                     arguments and input files), the processing of <tab> and
                     <space> characters, and for the determination of the
                     width in column positions each character would occupy on
                     an output device.

           LC_MESSAGES
                     Determine the locale that should be used to affect the
                     format and contents of diagnostic messages written to
                     standard error.

           NLSPATH   Determine the location of message catalogs for the
                     processing of LC_MESSAGES.

## [](#ASYNCHRONOUS_EVENTS)ASYNCHRONOUS EVENTS

           Default.

## [](#STDOUT)STDOUT

           The standard output shall be equivalent to the input files with
           the specified <space>-to-<tab> conversions.

## [](#STDERR)STDERR

           The standard error shall be used only for diagnostic messages.

## [](#OUTPUT_FILES)OUTPUT FILES

           None.

## [](#EXTENDED_DESCRIPTION)EXTENDED DESCRIPTION

           None.

## [](#EXIT_STATUS)EXIT STATUS

           The following exit values shall be returned:

            0    Successful completion.

           >0    An error occurred.

## [](#CONSEQUENCES_OF_ERRORS)CONSEQUENCES OF ERRORS

           Default.

           The following sections are informative.

## [](#APPLICATION_USAGE)APPLICATION USAGE

           One non-intuitive aspect of unexpand is its restriction to leading
           <space> characters when neither -a nor -t is specified. Users who
           always want to convert all <space> characters in a file can easily
           alias unexpand to use the -a or -t 8 option.

## [](#EXAMPLES)EXAMPLES

           None.

## [](#RATIONALE)RATIONALE

           On several occasions, consideration was given to adding a -t
           option to the unexpand utility to complement the -t in expand (see
           expand(1p)).  The historical intent of unexpand was to translate
           multiple <blank> characters into tab stops, where tab stops were a
           multiple of eight column positions on most UNIX systems. An early
           proposal omitted -t because it seemed outside the scope of the
           User Portability Utilities option; it was not described in any of
           the base documents for IEEE Std 1003.2‐1992.  However, hard-coding
           tab stops every eight columns was not suitable for the
           international community and broke historical precedents for some
           vendors in the FORTRAN community, so -t was restored in
           conjunction with the list of valid extension categories considered
           by the standard developers. Thus, unexpand is now the logical
           converse of expand.

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           None.

## [](#SEE_ALSO)SEE ALSO

           expand(1p), tabs(1p)

           The Base Definitions volume of POSIX.1‐2017, Chapter 8,
           Environment Variables, Section 12.2, Utility Syntax Guidelines

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

    IEEE/The Open Group                2017                      UNEXPAND(1P)

------------------------------------------------------------------------

Pages that refer to this page: [expand(1p)](../man1/expand.1p.html),  [tabs(1p)](../man1/tabs.1p.html)

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
