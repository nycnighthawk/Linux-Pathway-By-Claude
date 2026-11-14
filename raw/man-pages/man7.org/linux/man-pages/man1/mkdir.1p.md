---
{"title": "mkdir(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/mkdir.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mkdir(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MKDIR(1P)               POSIX Programmer's Manual               MKDIR(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           mkdir — make directories

## [](#SYNOPSIS)SYNOPSIS

           mkdir [-p] [-m mode] dir...

## [](#DESCRIPTION)DESCRIPTION

           The mkdir utility shall create the directories specified by the
           operands, in the order specified.

           For each dir operand, the mkdir utility shall perform actions
           equivalent to the mkdir() function defined in the System
           Interfaces volume of POSIX.1‐2017, called with the following
           arguments:

            1. The dir operand is used as the path argument.

            2. The value of the bitwise-inclusive OR of S_IRWXU, S_IRWXG, and
               S_IRWXO is used as the mode argument. (If the -m option is
               specified, the value of the mkdir() mode argument is
               unspecified, but the directory shall at no time have
               permissions less restrictive than the -m mode option-
               argument.)

## [](#OPTIONS)OPTIONS

           The mkdir utility shall conform to the Base Definitions volume of
           POSIX.1‐2017, Section 12.2, Utility Syntax Guidelines.

           The following options shall be supported:

           -m mode   Set the file permission bits of the newly-created
                     directory to the specified mode value. The mode option-
                     argument shall be the same as the mode operand defined
                     for the chmod utility. In the symbolic_mode strings, the
                     op characters '+' and '-' shall be interpreted relative
                     to an assumed initial mode of a=rwx; '+' shall add
                     permissions to the default mode, '-' shall delete
                     permissions from the default mode.

           -p        Create any missing intermediate pathname components.

                     For each dir operand that does not name an existing
                     directory, before performing the actions described in
                     the DESCRIPTION above, the mkdir utility shall create
                     any pathname components of the path prefix of dir that
                     do not name an existing directory by performing actions
                     equivalent to first calling the mkdir() function with
                     the following arguments:

                      1. A pathname naming the missing pathname component,
                         ending with a trailing <slash> character, as the
                         path argument

                      2. The value zero as the mode argument

                     and then calling the chmod() function with the following
                     arguments:

                      1. The same path argument as in the mkdir() call

                      2. The value (S_IWUSR|S_IXUSR|~filemask)&0777 as the
                         mode argument, where filemask is the file mode
                         creation mask of the process (see the System
                         Interfaces volume of POSIX.1‐2017, umask(3p))

                     Each dir operand that names an existing directory shall
                     be ignored without error.

## [](#OPERANDS)OPERANDS

           The following operand shall be supported:

           dir       A pathname of a directory to be created.

## [](#STDIN)STDIN

           Not used.

## [](#INPUT_FILES)INPUT FILES

           None.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           The following environment variables shall affect the execution of
           mkdir:

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

            0    All the specified directories were created successfully, or
                 the -p option was specified and all the specified
                 directories either already existed or were created
                 successfully.

           >0    An error occurred.

## [](#CONSEQUENCES_OF_ERRORS)CONSEQUENCES OF ERRORS

           Default.

           The following sections are informative.

## [](#APPLICATION_USAGE)APPLICATION USAGE

           The default file mode for directories is a=rwx (777 on most
           systems) with selected permissions removed in accordance with the
           file mode creation mask. For intermediate pathname components
           created by mkdir, the mode is the default modified by u+wx so that
           the subdirectories can always be created regardless of the file
           mode creation mask; if different ultimate permissions are desired
           for the intermediate directories, they can be changed afterwards
           with chmod.

           Note that some of the requested directories may have been created
           even if an error occurs.

## [](#EXAMPLES)EXAMPLES

           None.

## [](#RATIONALE)RATIONALE

           The System V -m option was included to control the file mode.

           The System V -p option was included to create any needed
           intermediate directories and to complement the functionality
           provided by rmdir for removing directories in the path prefix as
           they become empty.  Because no error is produced if any path
           component already exists, the -p option is also useful to ensure
           that a particular directory exists.

           The functionality of mkdir is described substantially through a
           reference to the mkdir() function in the System Interfaces volume
           of POSIX.1‐2017. For example, by default, the mode of the
           directory is affected by the file mode creation mask in accordance
           with the specified behavior of the mkdir() function. In this way,
           there is less duplication of effort required for describing
           details of the directory creation.

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           None.

## [](#SEE_ALSO)SEE ALSO

           chmod(1p), rm(1p), rmdir(1p), umask(1p)

           The Base Definitions volume of POSIX.1‐2017, Chapter 8,
           Environment Variables, Section 12.2, Utility Syntax Guidelines

           The System Interfaces volume of POSIX.1‐2017, mkdir(3p), umask(3p)

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

    IEEE/The Open Group                2017                         MKDIR(1P)

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
