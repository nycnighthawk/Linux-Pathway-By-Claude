---
{"title": "ipc(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ipc.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ipc(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ipc(2)                     System Calls Manual                     ipc(2)

## [](#NAME)NAME

           ipc - System V IPC system calls

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/ipc.h>        /* Definition of needed constants */
           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_ipc, unsigned int call, int first,
                       unsigned long second, unsigned long third, void *ptr,
                       long fifth);

           Note: glibc provides no wrapper for ipc(), necessitating the use
           of syscall(2).

## [](#DESCRIPTION)DESCRIPTION

           ipc() is a common kernel entry point for the System V IPC calls
           for messages, semaphores, and shared memory.  call determines
           which IPC function to invoke; the other arguments are passed
           through to the appropriate call.

           User-space programs should call the appropriate functions by their
           usual names.  Only standard library implementors and kernel
           hackers need to know about ipc().

## [](#VERSIONS)VERSIONS

           On some architectures —for example x86-64 and ARM— there is no
           ipc() system call; instead, msgctl(2), semctl(2), shmctl(2), and
           so on really are implemented as separate system calls.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#SEE_ALSO)SEE ALSO

           msgctl(2), msgget(2), msgrcv(2), msgsnd(2), semctl(2), semget(2),
           semop(2), semtimedop(2), shmat(2), shmctl(2), shmdt(2), shmget(2),
           sysvipc(7)

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

    Linux man-pages 6.19            2026-02-08                         ipc(2)

------------------------------------------------------------------------

Pages that refer to this page: [semctl(2)](../man2/semctl.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [unimplemented(2)](../man2/unimplemented.2.html),  [seccomp_syscall_resolve_name(3)](../man3/seccomp_syscall_resolve_name.3.html),  [sysvipc(7)](../man7/sysvipc.7.html)

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
