---
{"title": "idle(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/idle.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# idle(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    idle(2)                    System Calls Manual                    idle(2)

## [](#NAME)NAME

           idle - make process 0 idle

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           [[deprecated]] int idle(void);

## [](#DESCRIPTION)DESCRIPTION

           idle() is an internal system call used during bootstrap.  It marks
           the process's pages as swappable, lowers its priority, and enters
           the main scheduling loop.  idle() never returns.

           Only process 0 may call idle().  Any user process, even a process
           with superuser permission, will receive EPERM.

## [](#RETURN_VALUE)RETURN VALUE

           idle() never returns for process 0, and always returns -1 for a
           user process.

## [](#ERRORS)ERRORS

           EPERM  Always, for a user process.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Removed in Linux 2.3.13.

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

    Linux man-pages 6.19            2026-02-08                        idle(2)

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
