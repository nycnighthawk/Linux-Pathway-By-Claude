---
{"title": "exit(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/exit.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# exit(2) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    exit(2)                    System Calls Manual                    exit(2)

## [](#NAME)NAME

           exit - terminate the calling thread

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           [[noreturn]] long syscall(SYS_exit, int status);

## [](#DESCRIPTION)DESCRIPTION

           exit() terminates the calling thread.

           By contrast with _exit(3), the exit() system call terminates only
           the calling thread, and actions such as reparenting child
           processes or sending SIGCHLD to the parent process are performed
           only if this is the last thread in the thread group.

## [](#RETURN_VALUE)RETURN VALUE

           exit() does not return.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux.

## [](#SEE_ALSO)SEE ALSO

           exit_group(2), _exit(3), exit(3), pthread_exit(3)

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

    Linux man-pages 6.19            2026-06-05                        exit(2)

------------------------------------------------------------------------

Pages that refer to this page: [exit_group(2)](../man2/exit_group.2.html),  [fork(2)](../man2/fork.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [exit(3)](../man3/exit.3.html),  [\_exit(3)](../man3/_exit.3.html),  [pmgetconfig(3)](../man3/pmgetconfig.3.html),  [pmnomem(3)](../man3/pmnomem.3.html)

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
