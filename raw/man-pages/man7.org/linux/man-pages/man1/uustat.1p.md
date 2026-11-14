---
{"title": "uustat(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/uustat.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# uustat(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UUSTAT(1P)              POSIX Programmer's Manual              UUSTAT(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           uustat — uucp status enquiry and job control

## [](#SYNOPSIS)SYNOPSIS

           uustat [-q|-k jobid|-r jobid]

           uustat [-s system] [-u user]

## [](#DESCRIPTION)DESCRIPTION

           The uustat utility shall display the status of, or cancel,
           previously specified uucp requests, or provide general status on
           uucp connections to other systems.

           When no options are given, uustat shall write to standard output
           the status of all uucp requests issued by the current user.

           Typical implementations of this utility require a communications
           line configured to use the Base Definitions volume of
           POSIX.1‐2017, Chapter 11, General Terminal Interface, but other
           communications means may be used. On systems where there are no
           available communications means (either temporarily or
           permanently), this utility shall write an error message describing
           the problem and exit with a non-zero exit status.

## [](#OPTIONS)OPTIONS

           The uustat utility shall conform to the Base Definitions volume of
           POSIX.1‐2017, Section 12.2, Utility Syntax Guidelines.

           The following options shall be supported:

           -q        Write the jobs queued for each machine.

           -k jobid  Kill the uucp request whose job identification is jobid.
                     The application shall ensure that the killed uucp
                     request belongs to the person invoking uustat unless
                     that user has appropriate privileges.

           -r jobid  Rejuvenate jobid.  The files associated with jobid are
                     touched so that their modification time is set to the
                     current time. This prevents the cleanup program from
                     deleting the job until the jobs modification time
                     reaches the limit imposed by the program.

           -s system Write the status of all uucp requests for remote system
                     system.

           -u user   Write the status of all uucp requests issued by user.

## [](#OPERANDS)OPERANDS

           None.

## [](#STDIN)STDIN

           Not used.

## [](#INPUT_FILES)INPUT FILES

           None.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           The following environment variables shall affect the execution of
           uustat:

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
                     standard error, and informative messages written to
                     standard output.

           NLSPATH   Determine the location of message catalogs for the
                     processing of LC_MESSAGES.

## [](#ASYNCHRONOUS_EVENTS)ASYNCHRONOUS EVENTS

           Default.

## [](#STDOUT)STDOUT

           The standard output shall consist of information about each job
           selected, in an unspecified format. The information shall include
           at least the job ID, the user ID or name, and the remote system
           name.

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

           This utility is part of the UUCP Utilities option and need not be
           supported by all implementations.

## [](#EXAMPLES)EXAMPLES

           None.

## [](#RATIONALE)RATIONALE

           None.

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           None.

## [](#SEE_ALSO)SEE ALSO

           uucp(1p)

           The Base Definitions volume of POSIX.1‐2017, Chapter 8,
           Environment Variables, Chapter 11, General Terminal Interface,
           Section 12.2, Utility Syntax Guidelines

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

    IEEE/The Open Group                2017                        UUSTAT(1P)

------------------------------------------------------------------------

Pages that refer to this page: [uucp(1p)](../man1/uucp.1p.html),  [uux(1p)](../man1/uux.1p.html)

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
