---
{"title": "paste(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/paste.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# paste(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PASTE(1P)               POSIX Programmer's Manual               PASTE(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           paste — merge corresponding or subsequent lines of files

## [](#SYNOPSIS)SYNOPSIS

           paste [-s] [-d list] file...

## [](#DESCRIPTION)DESCRIPTION

           The paste utility shall concatenate the corresponding lines of the
           given input files, and write the resulting lines to standard
           output.

           The default operation of paste shall concatenate the corresponding
           lines of the input files. The <newline> of every line except the
           line from the last input file shall be replaced with a <tab>.

           If an end-of-file condition is detected on one or more input
           files, but not all input files, paste shall behave as though empty
           lines were read from the files on which end-of-file was detected,
           unless the -s option is specified.

## [](#OPTIONS)OPTIONS

           The paste utility shall conform to the Base Definitions volume of
           POSIX.1‐2017, Section 12.2, Utility Syntax Guidelines.

           The following options shall be supported:

           -d list   Unless a <backslash> character appears in list, each
                     character in list is an element specifying a delimiter
                     character. If a <backslash> character appears in list,
                     the <backslash> character and one or more characters
                     following it are an element specifying a delimiter
                     character as described below. These elements specify one
                     or more delimiters to use, instead of the default <tab>,
                     to replace the <newline> of the input lines. The
                     elements in list shall be used circularly; that is, when
                     the list is exhausted the first element from the list is
                     reused. When the -s option is specified:

                      *  The last <newline> in a file shall not be modified.

                      *  The delimiter shall be reset to the first element of
                         list after each file operand is processed.

                     When the -s option is not specified:

                      *  The <newline> characters in the file specified by
                         the last file operand shall not be modified.

                      *  The delimiter shall be reset to the first element of
                         list each time a line is processed from each file.

                     If a <backslash> character appears in list, it and the
                     character following it shall be used to represent the
                     following delimiter characters:

                     \n    <newline>.

                     \t    <tab>.

                     \\    <backslash> character.

                     \0    Empty string (not a null character). If '\0' is
                           immediately followed by the character 'x', the
                           character 'X', or any character defined by the
                           LC_CTYPE digit keyword (see the Base Definitions
                           volume of POSIX.1‐2017, Chapter 7, Locale), the
                           results are unspecified.

                     If any other characters follow the <backslash>, the
                     results are unspecified.

           -s        Concatenate all of the lines from each input file into
                     one line of output per file, in command line order. The
                     <newline> of every line except the last line in each
                     input file shall be replaced with a <tab>, unless
                     otherwise specified by the -d option. If an input file
                     is empty, the output line corresponding to that file
                     shall consist of only a <newline> character.

## [](#OPERANDS)OPERANDS

           The following operand shall be supported:

           file      A pathname of an input file. If '-' is specified for one
                     or more of the files, the standard input shall be used;
                     the standard input shall be read one line at a time,
                     circularly, for each instance of '-'.  Implementations
                     shall support pasting of at least 12 file operands.

## [](#STDIN)STDIN

           The standard input shall be used only if one or more file operands
           is '-'.  See the INPUT FILES section.

## [](#INPUT_FILES)INPUT FILES

           The input files shall be text files, except that line lengths
           shall be unlimited.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           The following environment variables shall affect the execution of
           paste:

           LANG      Provide a default value for the internationalization
                     variables that are unset or null. (See the Base
                     Definitions volume of POSIX.1‐2017, Section 8.2,
                     Internationalization Variables the precedence of
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

           Concatenated lines of input files shall be separated by the <tab>
           (or other characters under the control of the -d option) and
           terminated by a <newline>.

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

           If one or more input files cannot be opened when the -s option is
           not specified, a diagnostic message shall be written to standard
           error, but no output is written to standard output. If the -s
           option is specified, the paste utility shall provide the default
           behavior described in Section 1.4, Utility Description Defaults.

           The following sections are informative.

## [](#APPLICATION_USAGE)APPLICATION USAGE

           When the escape sequences of the list option-argument are used in
           a shell script, they must be quoted; otherwise, the shell treats
           the <backslash> as a special character.

           Conforming applications should only use the specific
           <backslash>-escaped delimiters presented in this volume of
           POSIX.1‐2017. Historical implementations treat '\x', where 'x' is
           not in this list, as 'x', but future implementations are free to
           expand this list to recognize other common escapes similar to
           those accepted by printf and other standard utilities.

           Most of the standard utilities work on text files. The cut utility
           can be used to turn files with arbitrary line lengths into a set
           of text files containing the same data. The paste utility can be
           used to create (or recreate) files with arbitrary line lengths.
           For example, if file contains long lines:

               cut -b 1-500 -n file > file1
               cut -b 501- -n file > file2

           creates file1 (a text file) with lines no longer than 500 bytes
           (plus the <newline>) and file2 that contains the remainder of the
           data from file.  Note that file2 is not a text file if there are
           lines in file that are longer than 500 + {LINE_MAX} bytes. The
           original file can be recreated from file1 and file2 using the
           command:

               paste -d "\0" file1 file2 > file

           The commands:

               paste -d "\0" ...
               paste -d "" ...

           are not necessarily equivalent; the latter is not specified by
           this volume of POSIX.1‐2017 and may result in an error. The
           construct '\0' is used to mean ``no separator'' because historical
           versions of paste did not follow the syntax guidelines, and the
           command:

               paste -d"" ...

           could not be handled properly by getopt().

## [](#EXAMPLES)EXAMPLES

            1. Write out a directory in four columns:

                   ls | paste - - - -

            2. Combine pairs of lines from a file into single lines:

                   paste -s -d "\t\n" file

## [](#RATIONALE)RATIONALE

           None.

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           None.

## [](#SEE_ALSO)SEE ALSO

           Section 1.4, Utility Description Defaults, cut(1p), grep(1p),
           pr(1p)

           The Base Definitions volume of POSIX.1‐2017, Chapter 7, Locale,
           Chapter 8, Environment Variables, Section 12.2, Utility Syntax
           Guidelines

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

    IEEE/The Open Group                2017                         PASTE(1P)

------------------------------------------------------------------------

Pages that refer to this page: [cut(1p)](../man1/cut.1p.html)

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
