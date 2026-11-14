---
{"title": "setpgid(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/setpgrp.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# setpgid(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    setpgid(2)                 System Calls Manual                 setpgid(2)

## [](#NAME)NAME

           setpgid, getpgid, setpgrp, getpgrp - set/get process group

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           int setpgid(pid_t pid, pid_t pgid);
           pid_t getpgid(pid_t pid);

           pid_t getpgrp(void);                            /* POSIX.1 version */
           [[deprecated]] pid_t getpgrp(pid_t pid);        /* BSD version */

           int setpgrp(void);                              /* System V version */
           [[deprecated]] int setpgrp(pid_t pid, pid_t pgid);  /* BSD version */

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           getpgid():
               _XOPEN_SOURCE >= 500
                   || /* Since glibc 2.12: */ _POSIX_C_SOURCE >= 200809L

           setpgrp() (POSIX.1):
               _XOPEN_SOURCE >= 500
                   || /* Since glibc 2.19: */ _DEFAULT_SOURCE
                   || /* glibc <= 2.19: */ _SVID_SOURCE

           setpgrp() (BSD), getpgrp() (BSD):
               [These are available only before glibc 2.19]
               _BSD_SOURCE &&
                   ! (_POSIX_SOURCE || _POSIX_C_SOURCE || _XOPEN_SOURCE
                       || _GNU_SOURCE || _SVID_SOURCE)

## [](#DESCRIPTION)DESCRIPTION

           All of these interfaces are available on Linux, and are used for
           getting and setting the process group ID (PGID) of a process.  The
           preferred, POSIX.1-specified ways of doing this are:
           getpgrp(void), for retrieving the calling process's PGID; and
           setpgid(), for setting a process's PGID.

           setpgid() sets the PGID of the process specified by pid to pgid.
           If pid is zero, then the process ID of the calling process is
           used.  If pgid is zero, then the PGID of the process specified by
           pid is made the same as its process ID.  If setpgid() is used to
           move a process from one process group to another (as is done by
           some shells when creating pipelines), both process groups must be
           part of the same session (see setsid(2) and credentials(7)).  In
           this case, the pgid specifies an existing process group to be
           joined and the session ID of that group must match the session ID
           of the joining process.

           The POSIX.1 version of getpgrp(), which takes no arguments,
           returns the PGID of the calling process.

           getpgid() returns the PGID of the process specified by pid.  If
           pid is zero, the process ID of the calling process is used.
           (Retrieving the PGID of a process other than the caller is rarely
           necessary, and the POSIX.1 getpgrp() is preferred for that task.)

           The System V-style setpgrp(), which takes no arguments, is
           equivalent to setpgid(0, 0).

           The BSD-specific setpgrp() call, which takes arguments pid and
           pgid, is a wrapper function that calls

               setpgid(pid, pgid)

           Since glibc 2.19, the BSD-specific setpgrp() function is no longer
           exposed by <unistd.h>; calls should be replaced with the setpgid()
           call shown above.

           The BSD-specific getpgrp() call, which takes a single pid
           argument, is a wrapper function that calls

               getpgid(pid)

           Since glibc 2.19, the BSD-specific getpgrp() function is no longer
           exposed by <unistd.h>; calls should be replaced with calls to the
           POSIX.1 getpgrp() which takes no arguments (if the intent is to
           obtain the caller's PGID), or with the getpgid() call shown above.

## [](#RETURN_VALUE)RETURN VALUE

           On success, setpgid() and setpgrp() return zero.  On error, -1 is
           returned, and errno is set to indicate the error.

           The POSIX.1 getpgrp() always returns the PGID of the caller.

           getpgid(), and the BSD-specific getpgrp() return a process group
           on success.  On error, -1 is returned, and errno is set to
           indicate the error.

## [](#ERRORS)ERRORS

           EACCES An attempt was made to change the process group ID of one
                  of the children of the calling process and the child had
                  already performed an execve(2) (setpgid(), setpgrp()).

           EINVAL pgid is less than 0 (setpgid(), setpgrp()).

           EPERM  An attempt was made to move a process into a process group
                  in a different session, or to change the process group ID
                  of one of the children of the calling process and the child
                  was in a different session, or to change the process group
                  ID of a session leader (setpgid(), setpgrp()).

           EPERM  The target process group does not exist.  (setpgid(),
                  setpgrp()).

           ESRCH  For getpgid(): pid does not match any process.  For
                  setpgid(): pid is not the calling process and not a child
                  of the calling process.

## [](#STANDARDS)STANDARDS

           getpgid()
           setpgid()
           getpgrp() (no args)
                  POSIX.1-2024.

           setpgrp()
           getpgrp() (1 arg)
                  None.

## [](#HISTORY)HISTORY

           getpgid()
           setpgid()
           getpgrp() (no args)
                  POSIX.1-2001.

           setpgrp() (no args)
                  POSIX.1-2001.  Obsoleted in POSIX.1-2008.  Removed in
                  POSIX.1-2024.

           setpgrp() (2 args)
           getpgrp() (1 arg)
                  4.2BSD.

## [](#NOTES)NOTES

           A child created via fork(2) inherits its parent's process group
           ID.  The PGID is preserved across an execve(2).

           Each process group is a member of a session and each process is a
           member of the session of which its process group is a member.
           (See credentials(7).)

           A session can have a controlling terminal.  At any time, one (and
           only one) of the process groups in the session can be the
           foreground process group for the terminal; the remaining process
           groups are in the background.  If a signal is generated from the
           terminal (e.g., typing the interrupt key to generate SIGINT), that
           signal is sent to the foreground process group.  (See
           termios(3type) for a description of the characters that generate
           signals.)  Only the foreground process group may read(2) from the
           terminal; if a background process group tries to read(2) from the
           terminal, then the group is sent a SIGTTIN signal, which suspends
           it.  The tcgetpgrp(3) and tcsetpgrp(3) functions are used to
           get/set the foreground process group of the controlling terminal.

           The setpgid() and getpgrp() calls are used by programs such as
           bash(1) to create process groups in order to implement shell job
           control.

           If the termination of a process causes a process group to become
           orphaned, and if any member of the newly orphaned process group is
           stopped, then a SIGHUP signal followed by a SIGCONT signal will be
           sent to each process in the newly orphaned process group.  An
           orphaned process group is one in which the parent of every member
           of process group is either itself also a member of the process
           group or is a member of a process group in a different session
           (see also credentials(7)).

## [](#SEE_ALSO)SEE ALSO

           getuid(2), setsid(2), tcgetpgrp(3), tcsetpgrp(3), termios(3type),
           termios(7), credentials(7)

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

    Linux man-pages 6.19            2026-07-02                     setpgid(2)

------------------------------------------------------------------------

Pages that refer to this page: [setpgid(1)](../man1/setpgid.1.html),  [strace(1)](../man1/strace.1.html),  [fork(2)](../man2/fork.2.html),  [getsid(2)](../man2/getsid.2.html),  [setsid(2)](../man2/setsid.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [exit(3)](../man3/exit.3.html),  [id_t(3type)](../man3/id_t.3type.html),  [killpg(3)](../man3/killpg.3.html),  [posix_spawn(3)](../man3/posix_spawn.3.html),  [tcgetpgrp(3)](../man3/tcgetpgrp.3.html),  [credentials(7)](../man7/credentials.7.html),  [pthreads(7)](../man7/pthreads.7.html),  [signal-safety(7)](../man7/signal-safety.7.html)

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
