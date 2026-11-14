---
{"title": "chgrp(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/chgrp.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# chgrp(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CHGRP(1P)               POSIX Programmer's Manual               CHGRP(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           chgrp — change the file group ownership

## [](#SYNOPSIS)SYNOPSIS

           chgrp [-h] group file...

           chgrp -R [-H|-L|-P] group file...

## [](#DESCRIPTION)DESCRIPTION

           The chgrp utility shall set the group ID of the file named by each
           file operand to the group ID specified by the group operand.

           For each file operand, or, if the -R option is used, each file
           encountered while walking the directory trees specified by the
           file operands, the chgrp utility shall perform actions equivalent
           to the chown() function defined in the System Interfaces volume of
           POSIX.1‐2017, called with the following arguments:

            *  The file operand shall be used as the path argument.

            *  The user ID of the file shall be used as the owner argument.

            *  The specified group ID shall be used as the group argument.

           Unless chgrp is invoked by a process with appropriate privileges,
           the set-user-ID and set-group-ID bits of a regular file shall be
           cleared upon successful completion; the set-user-ID and set-group-
           ID bits of other file types may be cleared.

## [](#OPTIONS)OPTIONS

           The chgrp utility shall conform to the Base Definitions volume of
           POSIX.1‐2017, Section 12.2, Utility Syntax Guidelines.

           The following options shall be supported by the implementation:

           -h        For each file operand that names a file of type symbolic
                     link, chgrp shall attempt to set the group ID of the
                     symbolic link instead of the file referenced by the
                     symbolic link.

           -H        If the -R option is specified and a symbolic link
                     referencing a file of type directory is specified on the
                     command line, chgrp shall change the group of the
                     directory referenced by the symbolic link and all files
                     in the file hierarchy below it.

           -L        If the -R option is specified and a symbolic link
                     referencing a file of type directory is specified on the
                     command line or encountered during the traversal of a
                     file hierarchy, chgrp shall change the group of the
                     directory referenced by the symbolic link and all files
                     in the file hierarchy below it.

           -P        If the -R option is specified and a symbolic link is
                     specified on the command line or encountered during the
                     traversal of a file hierarchy, chgrp shall change the
                     group ID of the symbolic link. The chgrp utility shall
                     not follow the symbolic link to any other part of the
                     file hierarchy.

           -R        Recursively change file group IDs. For each file operand
                     that names a directory, chgrp shall change the group of
                     the directory and all files in the file hierarchy below
                     it. Unless a -H, -L, or -P option is specified, it is
                     unspecified which of these options will be used as the
                     default.

           Specifying more than one of the mutually-exclusive options -H, -L,
           and -P shall not be considered an error. The last option specified
           shall determine the behavior of the utility.

## [](#OPERANDS)OPERANDS

           The following operands shall be supported:

           group     A group name from the group database or a numeric group
                     ID. Either specifies a group ID to be given to each file
                     named by one of the file operands. If a numeric group
                     operand exists in the group database as a group name,
                     the group ID number associated with that group name is
                     used as the group ID.

           file      A pathname of a file whose group ID is to be modified.

## [](#STDIN)STDIN

           Not used.

## [](#INPUT_FILES)INPUT FILES

           None.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           The following environment variables shall affect the execution of
           chgrp:

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

           The following exit values shall be returned:

            0    The utility executed successfully and all requested changes
                 were made.

           >0    An error occurred.

## [](#CONSEQUENCES_OF_ERRORS)CONSEQUENCES OF ERRORS

           Default.

           The following sections are informative.

## [](#APPLICATION_USAGE)APPLICATION USAGE

           Only the owner of a file or the user with appropriate privileges
           may change the owner or group of a file.

           Some implementations restrict the use of chgrp to a user with
           appropriate privileges when the group specified is not the
           effective group ID or one of the supplementary group IDs of the
           calling process.

## [](#EXAMPLES)EXAMPLES

           None.

## [](#RATIONALE)RATIONALE

           The System V and BSD versions use different exit status codes.
           Some implementations used the exit status as a count of the number
           of errors that occurred; this practice is unworkable since it can
           overflow the range of valid exit status values. The standard
           developers chose to mask these by specifying only 0 and >0 as exit
           values.

           The functionality of chgrp is described substantially through
           references to chown().  In this way, there is no duplication of
           effort required for describing the interactions of permissions,
           multiple groups, and so on.

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           None.

## [](#SEE_ALSO)SEE ALSO

           chmod(1p), chown(1p)

           The Base Definitions volume of POSIX.1‐2017, Chapter 8,
           Environment Variables, Section 12.2, Utility Syntax Guidelines

           The System Interfaces volume of POSIX.1‐2017, chown(3p)

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

    IEEE/The Open Group                2017                         CHGRP(1P)

------------------------------------------------------------------------

Pages that refer to this page: [chown(1p)](../man1/chown.1p.html)

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
