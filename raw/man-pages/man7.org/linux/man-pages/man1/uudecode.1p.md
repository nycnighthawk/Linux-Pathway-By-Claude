---
{"title": "uudecode(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/uudecode.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# uudecode(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UUDECODE(1P)            POSIX Programmer's Manual            UUDECODE(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           uudecode — decode a binary file

## [](#SYNOPSIS)SYNOPSIS

           uudecode [-o outfile] [file]

## [](#DESCRIPTION)DESCRIPTION

           The uudecode utility shall read a file, or standard input if no
           file is specified, that includes data created by the uuencode
           utility. The uudecode utility shall scan the input file, searching
           for data compatible with one of the formats specified in uuencode,
           and attempt to create or overwrite the file described by the data
           (or overridden by the -o option). The pathname shall be contained
           in the data or specified by the -o option. The file access
           permission bits and contents for the file to be produced shall be
           contained in that data. The mode bits of the created file (other
           than standard output) shall be set from the file access permission
           bits contained in the data; that is, other attributes of the mode,
           including the file mode creation mask (see umask), shall not
           affect the file being produced. If either of the op characters '+'
           and '-' (see chmod) are specified in symbolic mode, the initial
           mode on which those operations are based is unspecified.

           If the pathname of the file resolves to an existing file and the
           user does not have write permission on that file, uudecode shall
           terminate with an error. If the pathname of the file resolves to
           an existing file and the user has write permission on that file,
           the existing file shall be overwritten and, if possible, the mode
           bits of the file (other than standard output) shall be set as
           described above; if the mode bits cannot be set, uudecode shall
           not treat this as an error.

           If the input data was produced by uuencode on a system with a
           different number of bits per byte than on the target system, the
           results of uudecode are unspecified.

## [](#OPTIONS)OPTIONS

           The uudecode utility shall conform to the Base Definitions volume
           of POSIX.1‐2017, Section 12.2, Utility Syntax Guidelines.

           The following option shall be supported by the implementation:

           -o outfile
                     A pathname of a file that shall be used instead of any
                     pathname contained in the input data. Specifying an
                     outfile option-argument of /dev/stdout shall indicate
                     standard output.

## [](#OPERANDS)OPERANDS

           The following operand shall be supported:

           file      The pathname of a file containing the output of
                     uuencode.

## [](#STDIN)STDIN

           See the INPUT FILES section.

## [](#INPUT_FILES)INPUT FILES

           The input files shall be files containing the output of uuencode.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           The following environment variables shall affect the execution of
           uudecode:

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

           If the file data header encoded by uuencode is - or /dev/stdout,
           or the -o /dev/stdout option overrides the file data, the standard
           output shall be in the same format as the file originally encoded
           by uuencode.  Otherwise, the standard output shall not be used.

## [](#STDERR)STDERR

           The standard error shall be used only for diagnostic messages.

## [](#OUTPUT_FILES)OUTPUT FILES

           The output file shall be in the same format as the file originally
           encoded by uuencode.

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

           The user who is invoking uudecode must have write permission on
           any file being created.

           The output of uuencode is essentially an encoded bit stream that
           is not cognizant of byte boundaries. It is possible that a 9-bit
           byte target machine can process input from an 8-bit source, if it
           is aware of the requirement, but the reverse is unlikely to be
           satisfying. Of course, the only data that is meaningful for such a
           transfer between architectures is generally character data.

## [](#EXAMPLES)EXAMPLES

           None.

## [](#RATIONALE)RATIONALE

           Input files are not necessarily text files, as stated by an early
           proposal. Although the uuencode output is a text file, that output
           could have been wrapped within another file or mail message that
           is not a text file.

           The -o option is not historical practice, but was added at the
           request of WG15 so that the user could override the target
           pathname without having to edit the input data itself.

           In early drafts, the [-o outfile] option-argument allowed the use
           of - to mean standard output. The symbol - has only been used
           previously in POSIX.1‐2008 as a standard input indicator.  The
           standard developers did not wish to overload the meaning of - in
           this manner. The /dev/stdout concept exists on most modern
           systems. The /dev/stdout syntax does not refer to a new special
           file. It is just a magic cookie to specify standard output.

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           None.

## [](#SEE_ALSO)SEE ALSO

           chmod(1p), umask(1p), uuencode(1p)

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

    IEEE/The Open Group                2017                      UUDECODE(1P)

------------------------------------------------------------------------

Pages that refer to this page: [uuencode(1p)](../man1/uuencode.1p.html)

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
