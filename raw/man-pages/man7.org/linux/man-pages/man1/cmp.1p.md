---
{"title": "cmp(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/cmp.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cmp(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CMP(1P)                 POSIX Programmer's Manual                 CMP(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           cmp — compare two files

## [](#SYNOPSIS)SYNOPSIS

           cmp [-l|-s] file1 file2

## [](#DESCRIPTION)DESCRIPTION

           The cmp utility shall compare two files. The cmp utility shall
           write no output if the files are the same. Under default options,
           if they differ, it shall write to standard output the byte and
           line number at which the first difference occurred. Bytes and
           lines shall be numbered beginning with 1.

## [](#OPTIONS)OPTIONS

           The cmp utility shall conform to the Base Definitions volume of
           POSIX.1‐2017, Section 12.2, Utility Syntax Guidelines.

           The following options shall be supported:

           -l        (Lowercase ell.) Write the byte number (decimal) and the
                     differing bytes (octal) for each difference.

           -s        Write nothing to standard output or standard error when
                     files differ; indicate differing files through exit
                     status only.  It is unspecified whether a diagnostic
                     message is written to standard error when an error is
                     encountered; if a message is not written, the error is
                     indicated through exit status only.

## [](#OPERANDS)OPERANDS

           The following operands shall be supported:

           file1     A pathname of the first file to be compared. If file1 is
                     '-', the standard input shall be used.

           file2     A pathname of the second file to be compared. If file2
                     is '-', the standard input shall be used.

           If both file1 and file2 refer to standard input or refer to the
           same FIFO special, block special, or character special file, the
           results are undefined.

## [](#STDIN)STDIN

           The standard input shall be used only if the file1 or file2
           operand refers to standard input. See the INPUT FILES section.

## [](#INPUT_FILES)INPUT FILES

           The input files can be any file type.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           The following environment variables shall affect the execution of
           cmp:

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
                     standard error and informative messages written to
                     standard output.

           NLSPATH   Determine the location of message catalogs for the
                     processing of LC_MESSAGES.

## [](#ASYNCHRONOUS_EVENTS)ASYNCHRONOUS EVENTS

           Default.

## [](#STDOUT)STDOUT

           In the POSIX locale, results of the comparison shall be written to
           standard output. When no options are used, the format shall be:

               "%s %s differ: char %d, line %d\n", file1, file2,
                   <byte number>, <line number>

           When the -l option is used, the format shall be:

               "%d %o %o\n", <byte number>, <differing byte>,
                   <differing byte>

           for each byte that differs. The first <differing byte> number is
           from file1 while the second is from file2.  In both cases,
           <byte number> shall be relative to the beginning of the file,
           beginning with 1.

           No output shall be written to standard output when the -s option
           is used.

## [](#STDERR)STDERR

           The standard error shall be used only for diagnostic messages. If
           the -l option is used and file1 and file2 differ in length, or if
           the -s option is not used and file1 and file2 are identical for
           the entire length of the shorter file, in the POSIX locale the
           following diagnostic message shall be written:

               "cmp: EOF on %s%s\n", <name of shorter file>, <additional info>

           The <additional info> field shall either be null or a string that
           starts with a <blank> and contains no <newline> characters. Some
           implementations report on the number of lines in this case.

           If the -s option is used and an error occurs, it is unspecified
           whether a diagnostic message is written to standard error.

## [](#OUTPUT_FILES)OUTPUT FILES

           None.

## [](#EXTENDED_DESCRIPTION)EXTENDED DESCRIPTION

           None.

## [](#EXIT_STATUS)EXIT STATUS

           The following exit values shall be returned:

            0    The files are identical.

            1    The files are different; this includes the case where one
                 file is identical to the first part of the other.

           >1    An error occurred.

## [](#CONSEQUENCES_OF_ERRORS)CONSEQUENCES OF ERRORS

           Default.

           The following sections are informative.

## [](#APPLICATION_USAGE)APPLICATION USAGE

           Although input files to cmp can be any type, the results might not
           be what would be expected on character special device files or on
           file types not described by the System Interfaces volume of
           POSIX.1‐2017. Since this volume of POSIX.1‐2017 does not specify
           the block size used when doing input, comparisons of character
           special files need not compare all of the data in those files.

           For files which are not text files, line numbers simply reflect
           the presence of a <newline>, without any implication that the file
           is organized into lines.

           Since the behavior of -s differs between implementations as to
           whether error messages are written, the only way to ensure
           consistent behavior of cmp when -s is used is to redirect standard
           error to /dev/null.

           If error messages are wanted, instead of using -s standard output
           should be redirected to /dev/null, and anything written to
           standard error should be discarded if the exit status is 1. For
           example:

               silent_cmp() {
                   # compare files with no output except error messages
                   message=$(cmp "$@" 2>&1 >/dev/null)
                   status=$?
                   case $status in
                   (0|1) ;;
                   (*) printf '%s\n' "$message" ;;
                   esac
                   return $status
               }

## [](#EXAMPLES)EXAMPLES

           None.

## [](#RATIONALE)RATIONALE

           The global language in Section 1.4, Utility Description Defaults
           indicates that using two mutually-exclusive options together
           produces unspecified results. Some System V implementations
           consider the option usage:

               cmp -l -s ...

           to be an error. They also treat:

               cmp -s -l ...

           as if no options were specified. Both of these behaviors are
           considered bugs, but are allowed.

           The word char in the standard output format comes from historical
           usage, even though it is actually a byte number. When cmp is
           supported in other locales, implementations are encouraged to use
           the word byte or its equivalent in another language. Users should
           not interpret this difference to indicate that the functionality
           of the utility changed between locales.

           Some implementations report on the number of lines in the
           identical-but-shorter file case. This is allowed by the inclusion
           of the <additional info> fields in the output format. The
           restriction on having a leading <blank> and no <newline>
           characters is to make parsing for the filename easier. It is
           recognized that some filenames containing white-space characters
           make parsing difficult anyway, but the restriction does aid
           programs used on systems where the names are predominantly well
           behaved.

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           Future versions of this standard may require that diagnostic
           messages are written to standard error when the -s option is
           specified.

## [](#SEE_ALSO)SEE ALSO

           comm(1p), diff(1p)

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

    IEEE/The Open Group                2017                           CMP(1P)

------------------------------------------------------------------------

Pages that refer to this page: [comm(1p)](../man1/comm.1p.html),  [diff(1p)](../man1/diff.1p.html)

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
