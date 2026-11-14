---
{"title": "fold(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/fold.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fold(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FOLD(1P)                POSIX Programmer's Manual                FOLD(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           fold — filter for folding lines

## [](#SYNOPSIS)SYNOPSIS

           fold [-bs] [-w width] [file...]

## [](#DESCRIPTION)DESCRIPTION

           The fold utility is a filter that shall fold lines from its input
           files, breaking the lines to have a maximum of width column
           positions (or bytes, if the -b option is specified). Lines shall
           be broken by the insertion of a <newline> such that each output
           line (referred to later in this section as a segment) is the
           maximum width possible that does not exceed the specified number
           of column positions (or bytes). A line shall not be broken in the
           middle of a character. The behavior is undefined if width is less
           than the number of columns any single character in the input would
           occupy.

           If the <carriage-return>, <backspace>, or <tab> characters are
           encountered in the input, and the -b option is not specified, they
           shall be treated specially:

           <backspace>
                     The current count of line width shall be decremented by
                     one, although the count never shall become negative. The
                     fold utility shall not insert a <newline> immediately
                     before or after any <backspace>, unless the following
                     character has a width greater than 1 and would cause the
                     line width to exceed width.

           <carriage-return>
                     The current count of line width shall be set to zero.
                     The fold utility shall not insert a <newline>
                     immediately before or after any <carriage-return>.

           <tab>     Each <tab> encountered shall advance the column position
                     pointer to the next tab stop. Tab stops shall be at each
                     column position n such that n modulo 8 equals 1.

## [](#OPTIONS)OPTIONS

           The fold utility shall conform to the Base Definitions volume of
           POSIX.1‐2017, Section 12.2, Utility Syntax Guidelines.

           The following options shall be supported:

           -b        Count width in bytes rather than column positions.

           -s        If a segment of a line contains a <blank> within the
                     first width column positions (or bytes), break the line
                     after the last such <blank> meeting the width
                     constraints. If there is no <blank> meeting the
                     requirements, the -s option shall have no effect for
                     that output segment of the input line.

           -w width  Specify the maximum line length, in column positions (or
                     bytes if -b is specified). The results are unspecified
                     if width is not a positive decimal number. The default
                     value shall be 80.

## [](#OPERANDS)OPERANDS

           The following operand shall be supported:

           file      A pathname of a text file to be folded. If no file
                     operands are specified, the standard input shall be
                     used.

## [](#STDIN)STDIN

           The standard input shall be used if no file operands are
           specified, and shall be used if a file operand is '-' and the
           implementation treats the '-' as meaning standard input.
           Otherwise, the standard input shall not be used.  See the INPUT
           FILES section.

## [](#INPUT_FILES)INPUT FILES

           If the -b option is specified, the input files shall be text files
           except that the lines are not limited to {LINE_MAX} bytes in
           length. If the -b option is not specified, the input files shall
           be text files.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           The following environment variables shall affect the execution of
           fold:

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
                     arguments and input files), and for the determination of
                     the width in column positions each character would
                     occupy on a constant-width font output device.

           LC_MESSAGES
                     Determine the locale that should be used to affect the
                     format and contents of diagnostic messages written to
                     standard error.

           NLSPATH   Determine the location of message catalogs for the
                     processing of LC_MESSAGES.

## [](#ASYNCHRONOUS_EVENTS)ASYNCHRONOUS EVENTS

           Default.

## [](#STDOUT)STDOUT

           The standard output shall be a file containing a sequence of
           characters whose order shall be preserved from the input files,
           possibly with inserted <newline> characters.

## [](#STDERR)STDERR

           The standard error shall be used only for diagnostic messages.

## [](#OUTPUT_FILES)OUTPUT FILES

           None.

## [](#EXTENDED_DESCRIPTION)EXTENDED DESCRIPTION

           None.

## [](#EXIT_STATUS)EXIT STATUS

           The following exit values shall be returned:

            0    All input files were processed successfully.

           >0    An error occurred.

## [](#CONSEQUENCES_OF_ERRORS)CONSEQUENCES OF ERRORS

           Default.

           The following sections are informative.

## [](#APPLICATION_USAGE)APPLICATION USAGE

           The cut and fold utilities can be used to create text files out of
           files with arbitrary line lengths. The cut utility should be used
           when the number of lines (or records) needs to remain constant.
           The fold utility should be used when the contents of long lines
           need to be kept contiguous.

           The fold utility is frequently used to send text files to printers
           that truncate, rather than fold, lines wider than the printer is
           able to print (usually 80 or 132 column positions).

## [](#EXAMPLES)EXAMPLES

           An example invocation that submits a file of possibly long lines
           to the printer (under the assumption that the user knows the line
           width of the printer to be assigned by lp):

               fold -w 132 bigfile | lp

## [](#RATIONALE)RATIONALE

           Although terminal input in canonical processing mode requires the
           erase character (frequently set to <backspace>) to erase the
           previous character (not byte or column position), terminal output
           is not buffered and is extremely difficult, if not impossible, to
           parse correctly; the interpretation depends entirely on the
           physical device that actually displays/prints/stores the output.
           In all known internationalized implementations, the utilities
           producing output for mixed column-width output assume that a
           <backspace> character backs up one column position and outputs
           enough <backspace> characters to return to the start of the
           character when <backspace> is used to provide local line motions
           to support underlining and emboldening operations. Since fold
           without the -b option is dealing with these same constraints,
           <backspace> is always treated as backing up one column position
           rather than backing up one character.

           Historical versions of the fold utility assumed 1 byte was one
           character and occupied one column position when written out. This
           is no longer always true. Since the most common usage of fold is
           believed to be folding long lines for output to limited-length
           output devices, this capability was preserved as the default case.
           The -b option was added so that applications could fold files with
           arbitrary length lines into text files that could then be
           processed by the standard utilities. Note that although the width
           for the -b option is in bytes, a line is never split in the middle
           of a character.  (It is unspecified what happens if a width is
           specified that is too small to hold a single character found in
           the input followed by a <newline>.)

           The tab stops are hardcoded to be every eighth column to meet
           historical practice. No new method of specifying other tab stops
           was invented.

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           None.

## [](#SEE_ALSO)SEE ALSO

           cut(1p)

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

    IEEE/The Open Group                2017                          FOLD(1P)

------------------------------------------------------------------------

Pages that refer to this page: [cut(1p)](../man1/cut.1p.html),  [id(1p)](../man1/id.1p.html)

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
