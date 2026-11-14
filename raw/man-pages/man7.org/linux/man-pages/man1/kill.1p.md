---
{"title": "kill(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/kill.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# kill(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KILL(1P)                POSIX Programmer's Manual                KILL(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           kill — terminate or signal processes

## [](#SYNOPSIS)SYNOPSIS

           kill -s signal_name pid...

           kill -l [exit_status]

           kill [-signal_name] pid...

           kill [-signal_number] pid...

## [](#DESCRIPTION)DESCRIPTION

           The kill utility shall send a signal to the process or processes
           specified by each pid operand.

           For each pid operand, the kill utility shall perform actions
           equivalent to the kill() function defined in the System Interfaces
           volume of POSIX.1‐2017 called with the following arguments:

            *  The value of the pid operand shall be used as the pid
               argument.

            *  The sig argument is the value specified by the -s option,
               -signal_number option, or the -signal_name option, or by
               SIGTERM, if none of these options is specified.

## [](#OPTIONS)OPTIONS

           The kill utility shall conform to the Base Definitions volume of
           POSIX.1‐2017, Section 12.2, Utility Syntax Guidelines, except that
           in the last two SYNOPSIS forms, the -signal_number and
           -signal_name options are usually more than a single character.

           The following options shall be supported:

           -l        (The letter ell.) Write all values of signal_name
                     supported by the implementation, if no operand is given.
                     If an exit_status operand is given and it is a value of
                     the '?'  shell special parameter (see Section 2.5.2,
                     Special Parameters and wait) corresponding to a process
                     that was terminated by a signal, the signal_name
                     corresponding to the signal that terminated the process
                     shall be written. If an exit_status operand is given and
                     it is the unsigned decimal integer value of a signal
                     number, the signal_name (the symbolic constant name
                     without the SIG prefix defined in the Base Definitions
                     volume of POSIX.1‐2017) corresponding to that signal
                     shall be written. Otherwise, the results are
                     unspecified.

           -s signal_name
                     Specify the signal to send, using one of the symbolic
                     names defined in the <signal.h> header. Values of
                     signal_name shall be recognized in a case-independent
                     fashion, without the SIG prefix. In addition, the
                     symbolic name 0 shall be recognized, representing the
                     signal value zero. The corresponding signal shall be
                     sent instead of SIGTERM.

           -signal_name
                     Equivalent to -s signal_name.

           -signal_number
                     Specify a non-negative decimal integer, signal_number,
                     representing the signal to be used instead of SIGTERM,
                     as the sig argument in the effective call to kill().
                     The correspondence between integer values and the sig
                     value used is shown in the following list.

                     The effects of specifying any signal_number other than
                     those listed below are undefined.

                     0     0

                     1     SIGHUP

                     2     SIGINT

                     3     SIGQUIT

                     6     SIGABRT

                     9     SIGKILL

                     14    SIGALRM

                     15    SIGTERM

                     If the first argument is a negative integer, it shall be
                     interpreted as a -signal_number option, not as a
                     negative pid operand specifying a process group.

## [](#OPERANDS)OPERANDS

           The following operands shall be supported:

           pid       One of the following:

                      1. A decimal integer specifying a process or process
                         group to be signaled.  The process or processes
                         selected by positive, negative, and zero values of
                         the pid operand shall be as described for the kill()
                         function. If process number 0 is specified, all
                         processes in the current process group shall be
                         signaled. For the effects of negative pid numbers,
                         see the kill() function defined in the System
                         Interfaces volume of POSIX.1‐2017. If the first pid
                         operand is negative, it should be preceded by "--"
                         to keep it from being interpreted as an option.

                      2. A job control job ID (see the Base Definitions
                         volume of POSIX.1‐2017, Section 3.204, Job Control
                         Job ID) that identifies a background process group
                         to be signaled. The job control job ID notation is
                         applicable only for invocations of kill in the
                         current shell execution environment; see Section
                         2.12, Shell Execution Environment.

           exit_status
                     A decimal integer specifying a signal number or the exit
                     status of a process terminated by a signal.

## [](#STDIN)STDIN

           Not used.

## [](#INPUT_FILES)INPUT FILES

           None.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           The following environment variables shall affect the execution of
           kill:

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

           When the -l option is not specified, the standard output shall not
           be used.

           When the -l option is specified, the symbolic name of each signal
           shall be written in the following format:

               "%s%c", <signal_name>, <separator>

           where the <signal_name> is in uppercase, without the SIG prefix,
           and the <separator> shall be either a <newline> or a <space>.  For
           the last signal written, <separator> shall be a <newline>.

           When both the -l option and exit_status operand are specified, the
           symbolic name of the corresponding signal shall be written in the
           following format:

               "%s\n", <signal_name>

## [](#STDERR)STDERR

           The standard error shall be used only for diagnostic messages.

## [](#OUTPUT_FILES)OUTPUT FILES

           None.

## [](#EXTENDED_DESCRIPTION)EXTENDED DESCRIPTION

           None.

## [](#EXIT_STATUS)EXIT STATUS

           The following exit values shall be returned:

            0    At least one matching process was found for each pid
                 operand, and the specified signal was successfully processed
                 for at least one matching process.

           >0    An error occurred.

## [](#CONSEQUENCES_OF_ERRORS)CONSEQUENCES OF ERRORS

           Default.

           The following sections are informative.

## [](#APPLICATION_USAGE)APPLICATION USAGE

           Process numbers can be found by using ps.

           The job control job ID notation is not required to work as
           expected when kill is operating in its own utility execution
           environment. In either of the following examples:

               nohup kill %1 &
               system("kill %1");

           the kill operates in a different environment and does not share
           the shell's understanding of job numbers.

## [](#EXAMPLES)EXAMPLES

           Any of the commands:

               kill -9 100 -165
               kill -s kill 100 -165
               kill -s KILL 100 -165

           sends the SIGKILL signal to the process whose process ID is 100
           and to all processes whose process group ID is 165, assuming the
           sending process has permission to send that signal to the
           specified processes, and that they exist.

           The System Interfaces volume of POSIX.1‐2017 and this volume of
           POSIX.1‐2017 do not require specific signal numbers for any
           signal_names.  Even the -signal_number option provides symbolic
           (although numeric) names for signals. If a process is terminated
           by a signal, its exit status indicates the signal that killed it,
           but the exact values are not specified. The kill -l option,
           however, can be used to map decimal signal numbers and exit status
           values into the name of a signal. The following example reports
           the status of a terminated job:

               job
               stat=$?
               if [ $stat -eq 0 ]
               then
                   echo job completed successfully.
               elif [ $stat -gt 128 ]
               then
                   echo job terminated by signal SIG$(kill -l $stat).
               else
                   echo job terminated with error code $stat.
               fi

           To send the default signal to a process group (say 123), an
           application should use a command similar to one of the following:

               kill -TERM -123
               kill -- -123

## [](#RATIONALE)RATIONALE

           The -l option originated from the C shell, and is also implemented
           in the KornShell. The C shell output can consist of multiple
           output lines because the signal names do not always fit on a
           single line on some terminal screens. The KornShell output also
           included the implementation-defined signal numbers and was
           considered by the standard developers to be too difficult for
           scripts to parse conveniently. The specified output format is
           intended not only to accommodate the historical C shell output,
           but also to permit an entirely vertical or entirely horizontal
           listing on systems for which this is appropriate.

           An early proposal invented the name SIGNULL as a signal_name for
           signal 0 (used by the System Interfaces volume of POSIX.1‐2017 to
           test for the existence of a process without sending it a signal).
           Since the signal_name 0 can be used in this case unambiguously,
           SIGNULL has been removed.

           An early proposal also required symbolic signal_names to be
           recognized with or without the SIG prefix. Historical versions of
           kill have not written the SIG prefix for the -l option and have
           not recognized the SIG prefix on signal_names.  Since neither
           applications portability nor ease-of-use would be improved by
           requiring this extension, it is no longer required.

           To avoid an ambiguity of an initial negative number argument
           specifying either a signal number or a process group, POSIX.1‐2008
           mandates that it is always considered the former by
           implementations that support the XSI option. It also requires that
           conforming applications always use the "--" options terminator
           argument when specifying a process group, unless an option is also
           specified.

           The -s option was added in response to international interest in
           providing some form of kill that meets the Utility Syntax
           Guidelines.

           The job control job ID notation is not required to work as
           expected when kill is operating in its own utility execution
           environment. In either of the following examples:

               nohup kill %1 &
               system("kill %1");

           the kill operates in a different environment and does not
           understand how the shell has managed its job numbers.

## [](#FUTURE_DIRECTIONS)FUTURE DIRECTIONS

           None.

## [](#SEE_ALSO)SEE ALSO

           Chapter 2, Shell Command Language, ps(1p), wait(1p)

           The Base Definitions volume of POSIX.1‐2017, Section 3.204, Job
           Control Job ID, Chapter 8, Environment Variables, Section 12.2,
           Utility Syntax Guidelines, signal.h(0p)

           The System Interfaces volume of POSIX.1‐2017, kill(3p)

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

    IEEE/The Open Group                2017                          KILL(1P)

------------------------------------------------------------------------

Pages that refer to this page: [signal.h(0p)](../man0/signal.h.0p.html),  [bg(1p)](../man1/bg.1p.html),  [fg(1p)](../man1/fg.1p.html),  [jobs(1p)](../man1/jobs.1p.html),  [ps(1p)](../man1/ps.1p.html),  [qdel(1p)](../man1/qdel.1p.html),  [qsig(1p)](../man1/qsig.1p.html),  [wait(1p)](../man1/wait.1p.html)

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
