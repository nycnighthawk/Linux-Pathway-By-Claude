---
{"title": "exec(1p) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/exec.1p.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# exec(1p) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [PROLOG](#PROLOG) \| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERANDS](#OPERANDS) \| [STDIN](#STDIN) \| [INPUT FILES](#INPUT_FILES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [ASYNCHRONOUS EVENTS](#ASYNCHRONOUS_EVENTS) \| [STDOUT](#STDOUT) \| [STDERR](#STDERR) \| [OUTPUT FILES](#OUTPUT_FILES) \| [EXTENDED DESCRIPTION](#EXTENDED_DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [CONSEQUENCES OF ERRORS](#CONSEQUENCES_OF_ERRORS) \| [APPLICATION USAGE](#APPLICATION_USAGE) \| [EXAMPLES](#EXAMPLES) \| [RATIONALE](#RATIONALE) \| [FUTURE DIRECTIONS](#FUTURE_DIRECTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    EXEC(1P)                POSIX Programmer's Manual                EXEC(1P)

## [](#PROLOG)PROLOG

           This manual page is part of the POSIX Programmer's Manual.  The
           Linux implementation of this interface may differ (consult the
           corresponding Linux manual page for details of Linux behavior), or
           the interface may not be implemented on Linux.

## [](#NAME)NAME

           exec — execute commands and open, close, or copy file descriptors

## [](#SYNOPSIS)SYNOPSIS

           exec [command [argument...]]

## [](#DESCRIPTION)DESCRIPTION

           The exec utility shall open, close, and/or copy file descriptors
           as specified by any redirections as part of the command.

           If exec is specified without command or arguments, and any file
           descriptors with numbers greater than 2 are opened with associated
           redirection statements, it is unspecified whether those file
           descriptors remain open when the shell invokes another utility.
           Scripts concerned that child shells could misuse open file
           descriptors can always close them explicitly, as shown in one of
           the following examples.

           If exec is specified with command, it shall replace the shell with
           command without creating a new process. If arguments are
           specified, they shall be arguments to command.  Redirection
           affects the current shell execution environment.

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

           If command is specified, exec shall not return to the shell;
           rather, the exit status of the process shall be the exit status of
           the program implementing command, which overlaid the shell. If
           command is not found, the exit status shall be 127. If command is
           found, but it is not an executable utility, the exit status shall
           be 126. If a redirection error occurs (see Section 2.8.1,
           Consequences of Shell Errors), the shell shall exit with a value
           in the range 1-125. Otherwise, exec shall return a zero exit
           status.

## [](#CONSEQUENCES_OF_ERRORS)CONSEQUENCES OF ERRORS

           Default.

           The following sections are informative.

## [](#APPLICATION_USAGE)APPLICATION USAGE

           None.

## [](#EXAMPLES)EXAMPLES

           Open readfile as file descriptor 3 for reading:

               exec 3< readfile

           Open writefile as file descriptor 4 for writing:

               exec 4> writefile

           Make file descriptor 5 a copy of file descriptor 0:

               exec 5<&0

           Close file descriptor 3:

               exec 3<&-

           Cat the file maggie by replacing the current shell with the cat
           utility:

               exec cat maggie

## [](#RATIONALE)RATIONALE

           Most historical implementations were not conformant in that:

               foo=bar exec cmd

           did not pass foo to cmd.

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

    IEEE/The Open Group                2017                          EXEC(1P)

------------------------------------------------------------------------

Pages that refer to this page: [fcntl.h(0p)](../man0/fcntl.h.0p.html),  [stdarg.h(0p)](../man0/stdarg.h.0p.html),  [unistd.h(0p)](../man0/unistd.h.0p.html),  [awk(1p)](../man1/awk.1p.html),  [c99(1p)](../man1/c99.1p.html),  [command(1p)](../man1/command.1p.html),  [fort77(1p)](../man1/fort77.1p.html),  [make(1p)](../man1/make.1p.html),  [newgrp(1p)](../man1/newgrp.1p.html),  [sh(1p)](../man1/sh.1p.html),  [xargs(1p)](../man1/xargs.1p.html),  [aio_error(3p)](../man3/aio_error.3p.html),  [aio_read(3p)](../man3/aio_read.3p.html),  [aio_return(3p)](../man3/aio_return.3p.html),  [aio_write(3p)](../man3/aio_write.3p.html),  [alarm(3p)](../man3/alarm.3p.html),  [atexit(3p)](../man3/atexit.3p.html),  [chmod(3p)](../man3/chmod.3p.html),  [close(3p)](../man3/close.3p.html),  [confstr(3p)](../man3/confstr.3p.html),  [environ(3p)](../man3/environ.3p.html),  [exit(3p)](../man3/exit.3p.html),  [fcntl(3p)](../man3/fcntl.3p.html),  [fexecve(3p)](../man3/fexecve.3p.html),  [fork(3p)](../man3/fork.3p.html),  [fstatvfs(3p)](../man3/fstatvfs.3p.html),  [getenv(3p)](../man3/getenv.3p.html),  [getitimer(3p)](../man3/getitimer.3p.html),  [getopt(3p)](../man3/getopt.3p.html),  [getpgid(3p)](../man3/getpgid.3p.html),  [getpgrp(3p)](../man3/getpgrp.3p.html),  [getpid(3p)](../man3/getpid.3p.html),  [getppid(3p)](../man3/getppid.3p.html),  [getrlimit(3p)](../man3/getrlimit.3p.html),  [getsid(3p)](../man3/getsid.3p.html),  [glob(3p)](../man3/glob.3p.html),  [lio_listio(3p)](../man3/lio_listio.3p.html),  [mknod(3p)](../man3/mknod.3p.html),  [mlock(3p)](../man3/mlock.3p.html),  [mlockall(3p)](../man3/mlockall.3p.html),  [mmap(3p)](../man3/mmap.3p.html),  [nice(3p)](../man3/nice.3p.html),  [open(3p)](../man3/open.3p.html),  [posix_spawn(3p)](../man3/posix_spawn.3p.html),  [posix_trace_create(3p)](../man3/posix_trace_create.3p.html),  [posix_trace_event(3p)](../man3/posix_trace_event.3p.html),  [posix_trace_eventid_equal(3p)](../man3/posix_trace_eventid_equal.3p.html),  [posix_typed_mem_open(3p)](../man3/posix_typed_mem_open.3p.html),  [pthread_atfork(3p)](../man3/pthread_atfork.3p.html),  [pthread_sigmask(3p)](../man3/pthread_sigmask.3p.html),  [putenv(3p)](../man3/putenv.3p.html),  [readdir(3p)](../man3/readdir.3p.html),  [semop(3p)](../man3/semop.3p.html),  [setegid(3p)](../man3/setegid.3p.html),  [setenv(3p)](../man3/setenv.3p.html),  [seteuid(3p)](../man3/seteuid.3p.html),  [setgid(3p)](../man3/setgid.3p.html),  [setlocale(3p)](../man3/setlocale.3p.html),  [setpgid(3p)](../man3/setpgid.3p.html),  [setpgrp(3p)](../man3/setpgrp.3p.html),  [setregid(3p)](../man3/setregid.3p.html),  [setuid(3p)](../man3/setuid.3p.html),  [shmat(3p)](../man3/shmat.3p.html),  [shmdt(3p)](../man3/shmdt.3p.html),  [shm_open(3p)](../man3/shm_open.3p.html),  [sigaction(3p)](../man3/sigaction.3p.html),  [sigaltstack(3p)](../man3/sigaltstack.3p.html),  [sighold(3p)](../man3/sighold.3p.html),  [signal(3p)](../man3/signal.3p.html),  [sigpending(3p)](../man3/sigpending.3p.html),  [system(3p)](../man3/system.3p.html),  [times(3p)](../man3/times.3p.html),  [ulimit(3p)](../man3/ulimit.3p.html),  [umask(3p)](../man3/umask.3p.html),  [wait(3p)](../man3/wait.3p.html),  [waitid(3p)](../man3/waitid.3p.html),  [wordexp(3p)](../man3/wordexp.3p.html)

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
