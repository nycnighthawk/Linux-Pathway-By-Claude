---
{"title": "setsid(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/setsid.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# setsid(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    setsid(2)                  System Calls Manual                  setsid(2)

## [](#NAME)NAME

           setsid - creates a session and sets the process group ID

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           pid_t setsid(void);

## [](#DESCRIPTION)DESCRIPTION

           setsid() creates a new session if the calling process is not a
           process group leader.  The calling process is the leader of the
           new session (i.e., its session ID is made the same as its process
           ID).  The calling process also becomes the process group leader of
           a new process group in the session (i.e., its process group ID is
           made the same as its process ID).

           The calling process will be the only process in the new process
           group and in the new session.

           Initially, the new session has no controlling terminal.  For
           details of how a session acquires a controlling terminal, see
           credentials(7).

## [](#RETURN_VALUE)RETURN VALUE

           On success, the (new) session ID of the calling process is
           returned.  On error, (pid_t) -1 is returned, and errno is set to
           indicate the error.

## [](#ERRORS)ERRORS

           EPERM  The process group ID of any process equals the PID of the
                  calling process.  Thus, in particular, setsid() fails if
                  the calling process is already a process group leader.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001, SVr4.

## [](#NOTES)NOTES

           A child created via fork(2) inherits its parent's session ID.  The
           session ID is preserved across an execve(2).

           A process group leader is a process whose process group ID equals
           its PID.  Disallowing a process group leader from calling setsid()
           prevents the possibility that a process group leader places itself
           in a new session while other processes in the process group remain
           in the original session; such a scenario would break the strict
           two-level hierarchy of sessions and process groups.  In order to
           be sure that setsid() will succeed, call fork(2) and have the
           parent _exit(3), while the child (which by definition can't be a
           process group leader) calls setsid().

           If a session has a controlling terminal, and the CLOCAL flag for
           that terminal is not set, and a terminal hangup occurs, then the
           session leader is sent a SIGHUP signal.

           If a process that is a session leader terminates, then a SIGHUP
           signal is sent to each process in the foreground process group of
           the controlling terminal.

## [](#SEE_ALSO)SEE ALSO

           setsid(1), getsid(2), setpgid(2), setpgrp(2), tcgetsid(3),
           credentials(7), sched(7)

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

    Linux man-pages 6.19            2026-06-05                      setsid(2)

------------------------------------------------------------------------

Pages that refer to this page: [runuser(1)](../man1/runuser.1.html),  [setsid(1)](../man1/setsid.1.html),  [su(1)](../man1/su.1.html),  [getsid(2)](../man2/getsid.2.html),  [setpgid(2)](../man2/setpgid.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [daemon(3)](../man3/daemon.3.html),  [posix_spawn(3)](../man3/posix_spawn.3.html),  [tcgetpgrp(3)](../man3/tcgetpgrp.3.html),  [credentials(7)](../man7/credentials.7.html),  [pthreads(7)](../man7/pthreads.7.html),  [pty(7)](../man7/pty.7.html),  [sched(7)](../man7/sched.7.html),  [signal-safety(7)](../man7/signal-safety.7.html)

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
