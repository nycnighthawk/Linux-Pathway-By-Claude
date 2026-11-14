---
{"title": "s390_runtime_instr(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/s390_runtime_instr.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# s390_runtime_instr(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    s390_runtime_instr(2)      System Calls Manual      s390_runtime_instr(2)

## [](#NAME)NAME

           s390_runtime_instr - enable/disable s390 CPU run-time
           instrumentation

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <asm/runtime_instr.h> /* Definition of S390_* constants */
           #include <sys/syscall.h>       /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_s390_runtime_instr, int command, int signum);

           Note: glibc provides no wrapper for s390_runtime_instr(),
           necessitating the use of syscall(2).

## [](#DESCRIPTION)DESCRIPTION

           The s390_runtime_instr() system call starts or stops CPU run-time
           instrumentation for the calling thread.

           The command argument controls whether run-time instrumentation is
           started (S390_RUNTIME_INSTR_START, 1) or stopped
           (S390_RUNTIME_INSTR_STOP, 2) for the calling thread.

           The signum argument specifies the number of a real-time signal.
           This argument was used to specify a signal number that should be
           delivered to the thread if the run-time instrumentation buffer was
           full or if the run-time-instrumentation-halted interrupt had
           occurred.  This feature was never used, and in Linux 4.4 support
           for this feature was removed; thus, in current kernels, this
           argument is ignored.

## [](#RETURN_VALUE)RETURN VALUE

           On success, s390_runtime_instr() returns 0 and enables the thread
           for run-time instrumentation by assigning the thread a default
           run-time instrumentation control block.  The caller can then read
           and modify the control block and start the run-time
           instrumentation.  On error, -1 is returned and errno is set to
           indicate the error.

## [](#ERRORS)ERRORS

           EINVAL The value specified in command is not a valid command.

           EINVAL The value specified in signum is not a real-time signal
                  number.  From Linux 4.4 onwards, the signum argument has no
                  effect, so that an invalid signal number will not result in
                  an error.

           ENOMEM Allocating memory for the run-time instrumentation control
                  block failed.

           EOPNOTSUPP
                  The run-time instrumentation facility is not available.

## [](#STANDARDS)STANDARDS

           Linux on s390.

## [](#HISTORY)HISTORY

           Linux 3.7.  System z EC12.

## [](#NOTES)NOTES

           The asm/runtime_instr.h header file is available since Linux 4.16.

           Starting with Linux 4.4, support for signalling was removed, as
           was the check whether signum is a valid real-time signal.  For
           backwards compatibility with older kernels, it is recommended to
           pass a valid real-time signal number in signum and install a
           handler for that signal.

## [](#SEE_ALSO)SEE ALSO

           syscall(2), signal(7)

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

    Linux man-pages 6.19            2026-02-08          s390_runtime_instr(2)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html)

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
