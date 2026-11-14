---
{"title": "nl(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/nl.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nl(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NL(1P)                  POSIX Programmer's Manual                  NL(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           nl — line numbering filter

## [](#SYNOPSIS)SYNOPSIS

           nl [-p] [-b type] [-d delim] [-f type] [-h type] [-i incr] [-l num]
               [-n format] [-s sep] [-v startnum] [-w width] [file]

## [](#DESCRIPTION)DESCRIPTION

           The nl utility shall read lines from the named file or the
           standard input if no file is named and shall reproduce the lines
           to standard output. Lines shall be numbered on the left.
           Additional functionality may be provided in accordance with the
           command options in effect.

           The nl utility views the text it reads in terms of logical pages.
           Line numbering shall be reset at the start of each logical page. A
           logical page consists of a header, a body, and a footer section.
           Empty sections are valid. Different line numbering options are
           independently available for header, body, and footer (for example,
           no numbering of header and footer lines while numbering blank
           lines only in the body).

           The starts of logical page sections shall be signaled by input
           lines containing nothing but the following delimiter characters:
                              ┌────────────┬────────────┐
                              │    Line    │  Start of  │
                              ├────────────┼────────────┤
                              │ \:\:\:     │ Header     │
                              │ \:\:       │ Body       │
                              │ \:         │ Footer     │
                              └────────────┴────────────┘

           Unless otherwise specified, nl shall assume the text being read is
           in a single logical page body.

## [](#OPTIONS)OPTIONS

           The nl utility shall conform to the Base Definitions volume of
           POSIX.1‐2017, Section 12.2, Utility Syntax Guidelines.  Only one
           file can be named.

           The following options shall be supported:

           -b type   Specify which logical page body lines shall be numbered.
                     Recognized types and their meaning are:

                     a       Number all lines.

                     t       Number only non-empty lines.

                     n       No line numbering.

                     pstring Number only lines that contain the basic regular
                             expression specified in string.

                     The default type for logical page body shall be t (text
                     lines numbered).

           -d delim  Specify the delimiter characters that indicate the start
                     of a logical page section. These can be changed from the
                     default characters "\:" to two user-specified
                     characters. If only one character is entered, the second
                     character shall remain the default character ':'.

           -f type   Specify the same as b type except for footer. The
                     default for logical page footer shall be n (no lines
                     numbered).

           -h type   Specify the same as b type except for header. The
                     default type for logical page header shall be n (no
                     lines numbered).

           -i incr   Specify the increment value used to number logical page
                     lines. The default shall be 1.

           -l num    Specify the number of blank lines to be considered as
                     one. For example, -l 2 results in only the second
                     adjacent blank line being numbered (if the appropriate
                     -h a, -b a, or -f a option is set). The default shall be
                     1.

           -n format Specify the line numbering format. Recognized values
                     are: ln, left justified, leading zeros suppressed; rn,
                     right justified, leading zeros suppressed; rz, right
                     justified, leading zeros kept. The default format shall
                     be rn (right justified).

           -p        Specify that numbering should not be restarted at
                     logical page delimiters.

           -s sep    Specify the characters used in separating the line
                     number and the corresponding text line. The default sep
                     shall be a <tab>.

           -v startnum
                     Specify the initial value used to number logical page
                     lines. The default shall be 1.

           -w width  Specify the number of characters to be used for the line
                     number. The default width shall be 6.

## [](#OPERANDS)OPERANDS

           The following operand shall be supported:

           file      A pathname of a text file to be line-numbered.

## [](#STDIN)STDIN

           The standard input shall be used if no file operand is specified,
           and shall be used if the file operand is '-' and the
           implementation treats the '-' as meaning standard input.
           Otherwise, the standard input shall not be used.  See the INPUT
           FILES section.

## [](#INPUT_FILES)INPUT FILES

           The input file shall be a text file.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           The following environment variables shall affect the execution of
           nl:

           LANG      Provide a default value for the internationalization
                     variables that are unset or null. (See the Base
                     Definitions volume of POSIX.1‐2017, Section 8.2,
                     Internationalization Variables for the precedence of
                     internationalization variables used to determine the
                     values of locale categories.)

           LC_ALL    If set to a non-empty string value, override the values
                     of all the other internationalization variables.

           LC_COLLATE
                     Determine the locale for the behavior of ranges,
                     equivalence classes, and multi-character collating
                     elements within regular expressions.

           LC_CTYPE  Determine the locale for the interpretation of sequences
                     of bytes of text data as characters (for example,
                     single-byte as opposed to multi-byte characters in
                     arguments and input files), the behavior of character
                     classes within regular expressions, and for deciding
                     which characters are in character class graph (for the
                     -b t, -f t, and -h t options).

           LC_MESSAGES
                     Determine the locale that should be used to affect the
                     format and contents of diagnostic messages written to
                     standard error.

           NLSPATH   Determine the location of message catalogs for the
                     processing of LC_MESSAGES.

## [](#ASYNCHRONOUS_EVENTS)ASYNCHRONOUS EVENTS

           Default.

## [](#STDOUT)STDOUT

           The standard output shall be a text file in the following format:

               "%s%s%s", <line number>, <separator>, <input line>

           where <line number> is one of the following numeric formats:

           %6d       When the rn format is used (the default; see -n).

           %06d      When the rz format is used.

           %-6d      When the ln format is used.

           <empty>   When line numbers are suppressed for a portion of the
                     page; the <separator> is also suppressed.

           In the preceding list, the number 6 is the default width; the -w
           option can change this value.

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

           In using the -d delim option, care should be taken to escape
           characters that have special meaning to the command interpreter.

## [](#EXAMPLES)EXAMPLES

           The command:

               nl -v 10 -i 10 -d \!+ file1

           numbers file1 starting at line number 10 with an increment of 10.
           The logical page delimiter is "!+".  Note that the '!'  has to be
           escaped when using csh as a command interpreter because of its
           history substitution syntax.  For ksh and sh the escape is not
           necessary, but does not do any harm.

## [](#RATIONALE)RATIONALE

           None.

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           None.

## [](#SEE_ALSO)SEE ALSO

           pr(1p)

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

    IEEE/The Open Group                2017                            NL(1P)

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
