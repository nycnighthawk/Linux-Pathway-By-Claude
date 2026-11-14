---
{"title": "write(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/write.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# write(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    WRITE(1P)               POSIX Programmer's Manual               WRITE(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           write — write to another user

## [](#SYNOPSIS)SYNOPSIS

           write user_name [terminal]

## [](#DESCRIPTION)DESCRIPTION

           The write utility shall read lines from the standard input and
           write them to the terminal of the specified user. When first
           invoked, it shall write the message:

               Message from sender-login-id (sending-terminal) [date]...

           to user_name.  When it has successfully completed the connection,
           the sender's terminal shall be alerted twice to indicate that what
           the sender is typing is being written to the recipient's terminal.

           If the recipient wants to reply, this can be accomplished by
           typing:

               write sender-login-id [sending-terminal]

           upon receipt of the initial message. Whenever a line of input as
           delimited by an NL, EOF, or EOL special character (see the Base
           Definitions volume of POSIX.1‐2017, Chapter 11, General Terminal
           Interface) is accumulated while in canonical input mode, the
           accumulated data shall be written on the other user's terminal.
           Characters shall be processed as follows:

            *  Typing <alert> shall write the <alert> character to the
               recipient's terminal.

            *  Typing the erase and kill characters shall affect the sender's
               terminal in the manner described by the termios interface in
               the Base Definitions volume of POSIX.1‐2017, Chapter 11,
               General Terminal Interface.

            *  Typing the interrupt or end-of-file characters shall cause
               write to write an appropriate message ("EOT\n" in the POSIX
               locale) to the recipient's terminal and exit.

            *  Typing characters from LC_CTYPE classifications print or space
               shall cause those characters to be sent to the recipient's
               terminal.

            *  When and only when the stty iexten local mode is enabled, the
               existence and processing of additional special control
               characters and multi-byte or single-byte functions is
               implementation-defined.

            *  Typing other non-printable characters shall cause
               implementation-defined sequences of printable characters to be
               written to the recipient's terminal.

           To write to a user who is logged in more than once, the terminal
           argument can be used to indicate which terminal to write to;
           otherwise, the recipient's terminal is selected in an
           implementation-defined manner and an informational message is
           written to the sender's standard output, indicating which terminal
           was chosen.

           Permission to be a recipient of a write message can be denied or
           granted by use of the mesg utility. However, a user's privilege
           may further constrain the domain of accessibility of other users'
           terminals. The write utility shall fail when the user lacks
           appropriate privileges to perform the requested action.

## [](#OPTIONS)OPTIONS

           None.

## [](#OPERANDS)OPERANDS

           The following operands shall be supported:

           user_name Login name of the person to whom the message shall be
                     written. The application shall ensure that this operand
                     is of the form returned by the who utility.

           terminal  Terminal identification in the same format provided by
                     the who utility.

## [](#STDIN)STDIN

           Lines to be copied to the recipient's terminal are read from
           standard input.

## [](#INPUT_FILES)INPUT FILES

           None.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           The following environment variables shall affect the execution of
           write:

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
                     arguments and input files). If the recipient's locale
                     does not use an LC_CTYPE equivalent to the sender's, the
                     results are undefined.

           LC_MESSAGES
                     Determine the locale that should be used to affect the
                     format and contents of diagnostic messages written to
                     standard error and informative messages written to
                     standard output.

           NLSPATH   Determine the location of message catalogs for the
                     processing of LC_MESSAGES.

## [](#ASYNCHRONOUS_EVENTS)ASYNCHRONOUS EVENTS

           If an interrupt signal is received, write shall write an
           appropriate message on the recipient's terminal and exit with a
           status of zero. It shall take the standard action for all other
           signals.

## [](#STDOUT)STDOUT

           An informational message shall be written to standard output if a
           recipient is logged in more than once.

## [](#STDERR)STDERR

           The standard error shall be used only for diagnostic messages.

## [](#OUTPUT_FILES)OUTPUT FILES

           The recipient's terminal is used for output.

## [](#EXTENDED_DESCRIPTION)EXTENDED DESCRIPTION

           None.

## [](#EXIT_STATUS)EXIT STATUS

           The following exit values shall be returned:

            0    Successful completion.

           >0    The addressed user is not logged on or the addressed user
                 denies permission.

## [](#CONSEQUENCES_OF_ERRORS)CONSEQUENCES OF ERRORS

           Default.

           The following sections are informative.

## [](#APPLICATION_USAGE)APPLICATION USAGE

           The talk utility is considered by some users to be a more usable
           utility on full-screen terminals.

## [](#EXAMPLES)EXAMPLES

           None.

## [](#RATIONALE)RATIONALE

           The write utility was included in this volume of POSIX.1‐2017
           since it can be implemented on all terminal types. The standard
           developers considered the talk utility, which cannot be
           implemented on certain terminals, to be a ``better''
           communications interface. Both of these programs are in widespread
           use on historical implementations. Therefore, the standard
           developers decided that both utilities should be specified.

           The format of the terminal name is unspecified, but the
           descriptions of ps, talk, who, and write require that they all use
           or accept the same format.

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           None.

## [](#SEE_ALSO)SEE ALSO

           mesg(1p), talk(1p), who(1p)

           The Base Definitions volume of POSIX.1‐2017, Chapter 8,
           Environment Variables, Chapter 11, General Terminal Interface

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

    IEEE/The Open Group                2017                         WRITE(1P)

------------------------------------------------------------------------

Pages that refer to this page: [logger(1p)](../man1/logger.1p.html),  [mesg(1p)](../man1/mesg.1p.html),  [talk(1p)](../man1/talk.1p.html)

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
