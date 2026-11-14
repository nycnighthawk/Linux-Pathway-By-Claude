---
{"title": "what(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/what.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# what(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    WHAT(1P)                POSIX Programmer's Manual                WHAT(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           what — identify SCCS files (DEVELOPMENT)

## [](#SYNOPSIS)SYNOPSIS

           what [-s] file...

## [](#DESCRIPTION)DESCRIPTION

           The what utility shall search the given files for all occurrences
           of the pattern that get (see get(1p)) substitutes for the %Z%
           keyword ("@(#)") and shall write to standard output what follows
           until the first occurrence of one of the following:

               "   >   newline   \   NUL

## [](#OPTIONS)OPTIONS

           The what utility shall conform to the Base Definitions volume of
           POSIX.1‐2017, Section 12.2, Utility Syntax Guidelines.

           The following option shall be supported:

           -s        Quit after finding the first occurrence of the pattern
                     in each file.

## [](#OPERANDS)OPERANDS

           The following operands shall be supported:

           file      A pathname of a file to search.

## [](#STDIN)STDIN

           Not used.

## [](#INPUT_FILES)INPUT FILES

           The input files shall be of any file type.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           The following environment variables shall affect the execution of
           what:

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

## [](#ASYNCHRONOUS_EVENTS)ASYNCHRONOUS EVENTS

           Default.

## [](#STDOUT)STDOUT

           The standard output shall consist of the following for each file
           operand:

               "%s:\n\t%s\n", <pathname>, <identification string>

## [](#STDERR)STDERR

           The standard error shall be used only for diagnostic messages.

## [](#OUTPUT_FILES)OUTPUT FILES

           None.

## [](#EXTENDED_DESCRIPTION)EXTENDED DESCRIPTION

           None.

## [](#EXIT_STATUS)EXIT STATUS

           The following exit values shall be returned:

           0     Any matches were found.

           1     Otherwise.

## [](#CONSEQUENCES_OF_ERRORS)CONSEQUENCES OF ERRORS

           Default.

           The following sections are informative.

## [](#APPLICATION_USAGE)APPLICATION USAGE

           The what utility is intended to be used in conjunction with the
           SCCS command get, which automatically inserts identifying
           information, but it can also be used where the information is
           inserted by any other means.

           When the string "@(#)" is included in a library routine in a
           shared library, it might not be found in an a.out file using that
           library routine.

## [](#EXAMPLES)EXAMPLES

           If the C-language program in file f.c contains:

               char ident[] = "@(#)identification information";

           and f.c is compiled to yield f.o and a.out, then the command:

               what f.c f.o a.out

           writes:

               f.c:
                   identification information
                   ...
               f.o:
                   identification information
                   ...
               a.out:
                   identification information
                   ...

## [](#RATIONALE)RATIONALE

           None.

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           None.

## [](#SEE_ALSO)SEE ALSO

           get(1p)

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

    IEEE/The Open Group                2017                          WHAT(1P)

------------------------------------------------------------------------

Pages that refer to this page: [admin(1p)](../man1/admin.1p.html),  [get(1p)](../man1/get.1p.html),  [prs(1p)](../man1/prs.1p.html),  [sccs(1p)](../man1/sccs.1p.html)

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
