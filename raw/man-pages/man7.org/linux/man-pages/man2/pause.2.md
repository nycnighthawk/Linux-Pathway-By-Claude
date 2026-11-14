---
{"title": "pause(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pause.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pause(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    pause(2)                   System Calls Manual                   pause(2)

## [](#NAME)NAME

           pause - wait for signal

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           int pause(void);

## [](#DESCRIPTION)DESCRIPTION

           pause() causes the calling process (or thread) to sleep until a
           signal is delivered that either terminates the process or causes
           the invocation of a signal-catching function.

## [](#RETURN_VALUE)RETURN VALUE

           pause() returns only when a signal was caught and the signal-
           catching function returned.  In this case, pause() returns -1, and
           errno is set to EINTR.

## [](#ERRORS)ERRORS

           EINTR  a signal was caught and the signal-catching function
                  returned.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001, SVr4, 4.3BSD.

## [](#SEE_ALSO)SEE ALSO

           kill(2), select(2), signal(2), sigsuspend(2)

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

    Linux man-pages 6.19            2026-02-08                       pause(2)

------------------------------------------------------------------------

Pages that refer to this page: [pmsleep(1)](../man1/pmsleep.1.html),  [alarm(2)](../man2/alarm.2.html),  [ptrace(2)](../man2/ptrace.2.html),  [sigaction(2)](../man2/sigaction.2.html),  [signal(2)](../man2/signal.2.html),  [sigprocmask(2)](../man2/sigprocmask.2.html),  [sigsuspend(2)](../man2/sigsuspend.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [wait(2)](../man2/wait.2.html),  [sigset(3)](../man3/sigset.3.html),  [sigvec(3)](../man3/sigvec.3.html),  [signal(7)](../man7/signal.7.html),  [signal-safety(7)](../man7/signal-safety.7.html)

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
