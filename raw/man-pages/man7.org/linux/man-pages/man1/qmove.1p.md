---
{"title": "qmove(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/qmove.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# qmove(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    QMOVE(1P)               POSIX Programmer's Manual               QMOVE(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           qmove — move batch jobs

## [](#SYNOPSIS)SYNOPSIS

           qmove destination job_identifier...

## [](#DESCRIPTION)DESCRIPTION

           To move a batch job is to remove the batch job from the batch
           queue in which it resides and instantiate the batch job in another
           batch queue.  A batch job is moved by a request to the batch
           server that manages the batch job. The qmove utility is a user-
           accessible batch client that requests the movement of one or more
           batch jobs.

           The qmove utility shall move those batch jobs, and only those
           batch jobs, for which a batch job_identifier is presented to the
           utility.

           The qmove utility shall move batch jobs in the order in which the
           corresponding batch job_identifiers are presented to the utility.

           If the qmove utility fails to process a batch job_identifier
           successfully, the utility shall proceed to process the remaining
           batch job_identifiers, if any.

           The qmove utility shall move batch jobs by sending a Move Job
           Request to the batch server that manages each batch job. The qmove
           utility shall not exit before the batch jobs corresponding to all
           successfully processed batch job_identifiers have been moved.

## [](#OPTIONS)OPTIONS

           None.

## [](#OPERANDS)OPERANDS

           The qmove utility shall accept one operand that conforms to the
           syntax for a destination (see Section 3.3.2, Destination).

           The qmove utility shall accept one or more operands that conform
           to the syntax for a batch job_identifier (see Section 3.3.1, Batch
           Job Identifier).

## [](#STDIN)STDIN

           Not used.

## [](#INPUT_FILES)INPUT FILES

           None.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           The following environment variables shall affect the execution of
           qmove:

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
                     arguments).

           LC_MESSAGES
                     Determine the locale that should be used to affect the
                     format and contents of diagnostic messages written to
                     standard error.

           LOGNAME   Determine the login name of the user.

## [](#ASYNCHRONOUS_EVENTS)ASYNCHRONOUS EVENTS

           Default.

## [](#STDOUT)STDOUT

           None.

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

           In addition to the default behavior, the qmove utility shall not
           be required to write a diagnostic message to standard error when
           the error reply received from a batch server indicates that the
           batch job_identifier does not exist on the server. Whether or not
           the qmove utility waits to output the diagnostic message while
           attempting to locate the job on other servers is implementation-
           defined.

           The following sections are informative.

## [](#APPLICATION_USAGE)APPLICATION USAGE

           None.

## [](#EXAMPLES)EXAMPLES

           None.

## [](#RATIONALE)RATIONALE

           The qmove utility allows users to move jobs between queues.

           The alternative to using the qmove utility—deleting the batch job
           and requeuing it—entails considerably more typing.

           Since the means of selecting jobs based on attributes has been
           encapsulated in the qselect utility, the only option of the qmove
           utility concerns authorization. The -u option provides the user
           with the convenience of changing the user identifier under which
           the batch job will execute. Minimalism and consistency have taken
           precedence over convenience; the -u option has been deleted
           because the equivalent capability exists with the -u option of the
           qalter utility.

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           The qmove utility may be removed in a future version.

## [](#SEE_ALSO)SEE ALSO

           Chapter 3, Batch Environment Services, qalter(1p), qselect(1p)

           The Base Definitions volume of POSIX.1‐2017, Chapter 8,
           Environment Variables

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

    IEEE/The Open Group                2017                         QMOVE(1P)

------------------------------------------------------------------------

Pages that refer to this page: [qalter(1p)](../man1/qalter.1p.html)

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
