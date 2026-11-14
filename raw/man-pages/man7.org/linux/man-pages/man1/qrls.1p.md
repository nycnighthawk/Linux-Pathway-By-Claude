---
{"title": "qrls(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/qrls.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# qrls(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    QRLS(1P)                POSIX Programmer's Manual                QRLS(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           qrls — release batch jobs

## [](#SYNOPSIS)SYNOPSIS

           qrls [-h hold_list] job_identifier...

## [](#DESCRIPTION)DESCRIPTION

           A batch job might have one or more holds, which prevent the batch
           job from executing. A batch job from which all the holds have been
           removed becomes eligible for execution and is said to have been
           released. A batch job hold is removed by sending a request to the
           batch server that manages the batch job. The qrls utility is a
           user-accessible client of batch services that requests holds be
           removed from one or more batch jobs.

           The qrls utility shall remove one or more holds from those batch
           jobs for which a batch job_identifier is presented to the utility.

           The qrls utility shall remove holds from batch jobs in the order
           in which their batch job_identifiers are presented to the utility.

           If the qrls utility fails to process a batch job_identifier
           successfully, the utility shall proceed to process the remaining
           batch job_identifiers, if any.

           The qrls utility shall remove holds on each batch job by sending a
           Release Job Request to the batch server that manages the batch
           job.

           The qrls utility shall not exit until the holds have been removed
           from the batch job corresponding to each successfully processed
           batch job_identifier.

## [](#OPTIONS)OPTIONS

           The qrls utility shall conform to the Base Definitions volume of
           POSIX.1‐2017, Section 12.2, Utility Syntax Guidelines.

           The following option shall be supported by the implementation:

           -h hold_list
                     Define the types of holds to be removed from the batch
                     job.

                     The qrls -h option shall accept a value for the
                     hold_list option-argument that is a string of
                     alphanumeric characters in the portable character set
                     (see the Base Definitions volume of POSIX.1‐2017,
                     Section 6.1, Portable Character Set).

                     The qrls utility shall accept a value for the hold_list
                     option-argument that is a string of one or more of the
                     characters 'u', 's', or 'o', or the single character
                     'n'.

                     For each unique character in the hold_list option-
                     argument, the qrls utility shall add a value to the
                     Hold_Types attribute of the batch job as follows, each
                     representing a different hold type:

                     u     USER

                     s     SYSTEM

                     o     OPERATOR

                     If any of these characters are duplicated in the
                     hold_list option-argument, the duplicates shall be
                     ignored.

                     An existing Hold_Types attribute can be cleared by the
                     following hold type:

                     n     NO_HOLD

                     The qrls utility shall consider it an error if any hold
                     type other than 'n' is combined with hold type 'n'.

                     Strictly conforming applications shall not repeat any of
                     the characters 'u', 's', 'o', or 'n' within the
                     hold_list option-argument. The qrls utility shall permit
                     the repetition of characters, but shall not assign
                     additional meaning to the repeated characters.

                     An implementation may define other hold types. The
                     conformance document for an implementation shall
                     describe any additional hold types, how they are
                     specified, their internal behavior, and how they affect
                     the behavior of the utility.

                     If the -h option is not presented to the qrls utility,
                     the implementation shall remove the USER hold in the
                     Hold_Types attribute.

## [](#OPERANDS)OPERANDS

           The qrls utility shall accept one or more operands that conform to
           the syntax for a batch job_identifier (see Section 3.3.1, Batch
           Job Identifier).

## [](#STDIN)STDIN

           Not used.

## [](#INPUT_FILES)INPUT FILES

           None.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           The following environment variables shall affect the execution of
           qrls:

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

           In addition to the default behavior, the qrls utility shall not be
           required to write a diagnostic message to standard error when the
           error reply received from a batch server indicates that the batch
           job_identifier does not exist on the server. Whether or not the
           qrls utility waits to output the diagnostic message while
           attempting to locate the job on other servers is implementation-
           defined.

           The following sections are informative.

## [](#APPLICATION_USAGE)APPLICATION USAGE

           None.

## [](#EXAMPLES)EXAMPLES

           None.

## [](#RATIONALE)RATIONALE

           The qrls utility allows users, operators, and administrators to
           remove holds from jobs.

           The qrls utility does not support any job selection options or
           wildcard arguments. Users may acquire a list of jobs selected by
           attributes using the qselect utility. For example, a user could
           select all of their held jobs.

           The -h option allows the user to specify the type of hold that is
           to be removed. This option allows for USER, SYSTEM, OPERATOR, and
           implementation-defined hold types. The batch server that manages
           the batch job will verify whether the user is authorized to remove
           the specified hold for the batch job. If more than one type of
           hold has been placed on the batch job, a user may wish to remove
           only some of them.

           Mail is not required on release because the administrator has the
           tools and libraries to build this option if required.

           The qrls utility is a new utility vis-a-vis existing practice; it
           has been defined in this volume of POSIX.1‐2017 as the natural
           complement to the qhold utility.

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           The qrls utility may be removed in a future version.

## [](#SEE_ALSO)SEE ALSO

           Chapter 3, Batch Environment Services, qhold(1p), qselect(1p)

           The Base Definitions volume of POSIX.1‐2017, Section 6.1, Portable
           Character Set, Chapter 8, Environment Variables, Section 12.2,
           Utility Syntax Guidelines

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

    IEEE/The Open Group                2017                          QRLS(1P)

------------------------------------------------------------------------

Pages that refer to this page: [qalter(1p)](../man1/qalter.1p.html),  [qselect(1p)](../man1/qselect.1p.html)

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
