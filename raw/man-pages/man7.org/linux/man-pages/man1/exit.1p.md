---
{"title": "exit(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/exit.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# exit(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    EXIT(1P)                POSIX Programmer's Manual                EXIT(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           exit — cause the shell to exit

## [](#SYNOPSIS)SYNOPSIS

           exit [n]

## [](#DESCRIPTION)DESCRIPTION

           The exit utility shall cause the shell to exit from its current
           execution environment with the exit status specified by the
           unsigned decimal integer n.  If the current execution environment
           is a subshell environment, the shell shall exit from the subshell
           environment with the specified exit status and continue in the
           environment from which that subshell environment was invoked;
           otherwise, the shell utility shall terminate with the specified
           exit status. If n is specified, but its value is not between 0 and
           255 inclusively, the exit status is undefined.

           A trap on EXIT shall be executed before the shell terminates,
           except when the exit utility is invoked in that trap itself, in
           which case the shell shall exit immediately.

## [](#OPTIONS)OPTIONS

           None.

## [](#OPERANDS)OPERANDS

           See the DESCRIPTION.

## [](#STDIN)STDIN

           Not used.

## [](#INPUT_FILES)INPUT FILES

           None.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           None.

## [](#ASYNCHRONOUS_EVENTS)ASYNCHRONOUS EVENTS

           Default.

## [](#STDOUT)STDOUT

           Not used.

## [](#STDERR)STDERR

           The standard error shall be used only for diagnostic messages.

## [](#OUTPUT_FILES)OUTPUT FILES

           None.

## [](#EXTENDED_DESCRIPTION)EXTENDED DESCRIPTION

           None.

## [](#EXIT_STATUS)EXIT STATUS

           The exit status shall be n, if specified, except that the behavior
           is unspecified if n is not an unsigned decimal integer or is
           greater than 255. Otherwise, the value shall be the exit value of
           the last command executed, or zero if no command was executed.
           When exit is executed in a trap action, the last command is
           considered to be the command that executed immediately preceding
           the trap action.

## [](#CONSEQUENCES_OF_ERRORS)CONSEQUENCES OF ERRORS

           Default.

           The following sections are informative.

## [](#APPLICATION_USAGE)APPLICATION USAGE

           None.

## [](#EXAMPLES)EXAMPLES

           Exit with a true value:

               exit 0

           Exit with a false value:

               exit 1

           Propagate error handling from within a subshell:

               (
                   command1 || exit 1
                   command2 || exit 1
                   exec command3
               ) > outputfile || exit 1
               echo "outputfile created successfully"

## [](#RATIONALE)RATIONALE

           As explained in other sections, certain exit status values have
           been reserved for special uses and should be used by applications
           only for those purposes:

            126    A file to be executed was found, but it was not an
                   executable utility.

            127    A utility to be executed was not found.

           >128    A command was interrupted by a signal.

           The behavior of exit when given an invalid argument or unknown
           option is unspecified, because of differing practices in the
           various historical implementations. A value larger than 255 might
           be truncated by the shell, and be unavailable even to a parent
           process that uses waitid() to get the full exit value. It is
           recommended that implementations that detect any usage error
           should cause a non-zero exit status (or, if the shell is
           interactive and the error does not cause the shell to abort, store
           a non-zero value in "$?"), but even this was not done historically
           in all shells.

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           None.

## [](#SEE_ALSO)SEE ALSO

           Section 2.14, Special Built-In Utilities

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

    IEEE/The Open Group                2017                          EXIT(1P)

------------------------------------------------------------------------

Pages that refer to this page: [return(1p)](../man1/return.1p.html),  [sh(1p)](../man1/sh.1p.html)

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
