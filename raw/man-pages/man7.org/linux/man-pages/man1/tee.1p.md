---
{"title": "tee(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/tee.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tee(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TEE(1P)                 POSIX Programmer's Manual                 TEE(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           tee — duplicate standard input

## [](#SYNOPSIS)SYNOPSIS

           tee [-ai] [file...]

## [](#DESCRIPTION)DESCRIPTION

           The tee utility shall copy standard input to standard output,
           making a copy in zero or more files. The tee utility shall not
           buffer output.

           If the -a option is not specified, output files shall be written
           (see Section 1.1.1.4, File Read, Write, and Creation.

## [](#OPTIONS)OPTIONS

           The tee utility shall conform to the Base Definitions volume of
           POSIX.1‐2017, Section 12.2, Utility Syntax Guidelines.

           The following options shall be supported:

           -a        Append the output to the files.

           -i        Ignore the SIGINT signal.

## [](#OPERANDS)OPERANDS

           The following operands shall be supported:

           file      A pathname of an output file. If a file operand is '-',
                     it shall refer to a file named -; implementations shall
                     not treat it as meaning standard output.  Processing of
                     at least 13 file operands shall be supported.

## [](#STDIN)STDIN

           The standard input can be of any type.

## [](#INPUT_FILES)INPUT FILES

           None.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           The following environment variables shall affect the execution of
           tee:

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
                     arguments).

           LC_MESSAGES
                     Determine the locale that should be used to affect the
                     format and contents of diagnostic messages written to
                     standard error.

           NLSPATH   Determine the location of message catalogs for the
                     processing of LC_MESSAGES.

## [](#ASYNCHRONOUS_EVENTS)ASYNCHRONOUS EVENTS

           Default, except that if the -i option was specified, SIGINT shall
           be ignored.

## [](#STDOUT)STDOUT

           The standard output shall be a copy of the standard input.

## [](#STDERR)STDERR

           The standard error shall be used only for diagnostic messages.

## [](#OUTPUT_FILES)OUTPUT FILES

           If any file operands are specified, the standard input shall be
           copied to each named file.

## [](#EXTENDED_DESCRIPTION)EXTENDED DESCRIPTION

           None.

## [](#EXIT_STATUS)EXIT STATUS

           The following exit values shall be returned:

            0    The standard input was successfully copied to all output
                 files.

           >0    An error occurred.

## [](#CONSEQUENCES_OF_ERRORS)CONSEQUENCES OF ERRORS

           If a write to any successfully opened file operand fails, writes
           to other successfully opened file operands and standard output
           shall continue, but the exit status shall be non-zero. Otherwise,
           the default actions specified in Section 1.4, Utility Description
           Defaults apply.

           The following sections are informative.

## [](#APPLICATION_USAGE)APPLICATION USAGE

           The tee utility is usually used in a pipeline, to make a copy of
           the output of some utility.

           The file operand is technically optional, but tee is no more
           useful than cat when none is specified.

## [](#EXAMPLES)EXAMPLES

           Save an unsorted intermediate form of the data in a pipeline:

               ... | tee unsorted | sort > sorted

## [](#RATIONALE)RATIONALE

           The buffering requirement means that tee is not allowed to use
           ISO C standard fully buffered or line-buffered writes. It does not
           mean that tee has to do 1-byte reads followed by 1-byte writes.

           It should be noted that early versions of BSD ignore any invalid
           options and accept a single '-' as an alternative to -i.  They
           also print a message if unable to open a file:

               "tee: cannot access %s\n", <pathname>

           Historical implementations ignore write errors. This is explicitly
           not permitted by this volume of POSIX.1‐2017.

           Some historical implementations use O_APPEND when providing append
           mode; others use the lseek() function to seek to the end-of-file
           after opening the file without O_APPEND. This volume of
           POSIX.1‐2017 requires functionality equivalent to using O_APPEND;
           see Section 1.1.1.4, File Read, Write, and Creation.

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           None.

## [](#SEE_ALSO)SEE ALSO

           Chapter 1, Introduction, cat(1p)

           The Base Definitions volume of POSIX.1‐2017, Chapter 8,
           Environment Variables, Section 12.2, Utility Syntax Guidelines

           The System Interfaces volume of POSIX.1‐2017, lseek(3p)

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

    IEEE/The Open Group                2017                           TEE(1P)

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
