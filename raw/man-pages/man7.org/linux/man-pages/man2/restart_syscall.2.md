---
{"title": "restart_syscall(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/restart_syscall.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# restart_syscall(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    restart_syscall(2)         System Calls Manual         restart_syscall(2)

## [](#NAME)NAME

           restart_syscall - restart a system call after interruption by a
           stop signal

## [](#SYNOPSIS)SYNOPSIS

           long restart_syscall(void);

           Note: There is no glibc wrapper for this system call; see NOTES.

## [](#DESCRIPTION)DESCRIPTION

           The restart_syscall() system call is used to restart certain
           system calls after a process that was stopped by a signal (e.g.,
           SIGSTOP or SIGTSTP) is later resumed after receiving a SIGCONT
           signal.  This system call is designed only for internal use by the
           kernel.

           restart_syscall() is used for restarting only those system calls
           that, when restarted, should adjust their time-related parameters—
           namely poll(2) (since Linux 2.6.24), nanosleep(2) (since Linux
           2.6), clock_nanosleep(2) (since Linux 2.6), and futex(2), when
           employed with the FUTEX_WAIT (since Linux 2.6.22) and
           FUTEX_WAIT_BITSET (since Linux 2.6.31) operations.
           restart_syscall() restarts the interrupted system call with a time
           argument that is suitably adjusted to account for the time that
           has already elapsed (including the time where the process was
           stopped by a signal).  Without the restart_syscall() mechanism,
           restarting these system calls would not correctly deduct the
           already elapsed time when the process continued execution.

## [](#RETURN_VALUE)RETURN VALUE

           The return value of restart_syscall() is the return value of
           whatever system call is being restarted.

## [](#ERRORS)ERRORS

           errno is set as per the errors for whatever system call is being
           restarted by restart_syscall().

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.

## [](#NOTES)NOTES

           There is no glibc wrapper for this system call, because it is
           intended for use only by the kernel and should never be called by
           applications.

           The kernel uses restart_syscall() to ensure that when a system
           call is restarted after a process has been stopped by a signal and
           then resumed by SIGCONT, then the time that the process spent in
           the stopped state is counted against the timeout interval
           specified in the original system call.  In the case of system
           calls that take a timeout argument and automatically restart after
           a stop signal plus SIGCONT, but which do not have the
           restart_syscall() mechanism built in, then, after the process
           resumes execution, the time that the process spent in the stop
           state is not counted against the timeout value.  Notable examples
           of system calls that suffer this problem are ppoll(2), select(2),
           and pselect(2).

           From user space, the operation of restart_syscall() is largely
           invisible: to the process that made the system call that is
           restarted, it appears as though that system call executed and
           returned in the usual fashion.

## [](#SEE_ALSO)SEE ALSO

           sigaction(2), sigreturn(2), signal(7)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2026-02-08             restart_syscall(2)

------------------------------------------------------------------------

Pages that refer to this page: [lsfd(1)](../man1/lsfd.1.html),  [clock_nanosleep(2)](../man2/clock_nanosleep.2.html),  [futex(2)](../man2/futex.2.html),  [nanosleep(2)](../man2/nanosleep.2.html),  [poll(2)](../man2/poll.2.html),  [ptrace(2)](../man2/ptrace.2.html),  [select(2)](../man2/select.2.html),  [sigaction(2)](../man2/sigaction.2.html),  [sigreturn(2)](../man2/sigreturn.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [signal(7)](../man7/signal.7.html)

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
