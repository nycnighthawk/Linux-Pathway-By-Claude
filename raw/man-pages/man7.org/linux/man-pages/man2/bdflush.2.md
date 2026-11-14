---
{"title": "bdflush(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/bdflush.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# bdflush(2) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    bdflush(2)                 System Calls Manual                 bdflush(2)

## [](#NAME)NAME

           bdflush - start, flush, or tune buffer-dirty-flush daemon

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/kdaemon.h>

           int bdflush(int func, long data);

## [](#DESCRIPTION)DESCRIPTION

           This system call used to turn the calling process into the bdflush
           daemon, or tune it, or flush the "old buffers".  It then
           progressively lost all of that functionality.

           See fs/buffer.c in the kernel version you're interested in to see
           what it actually does there.

## [](#ERRORS)ERRORS

           ENOSYS (this system call is unimplemented)

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           This system call was introduced in Linux 1.1.3, became effectively
           obsolete in Linux 1.3.50, mostly useless in Linux 2.3.23, entirely
           useless in Linux 2.5.12, officially deprecated in Linux 2.5.52,
           and removed outright in Linux 5.15.

           Sometimes, if func was even, data actually represented a pointer.

           The header and prototype were removed in glibc 2.23.

## [](#SEE_ALSO)SEE ALSO

           sync(1), fsync(2), sync(2)

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

    Linux man-pages 6.19            2026-02-08                     bdflush(2)

------------------------------------------------------------------------

Pages that refer to this page: [fsync(2)](../man2/fsync.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [capabilities(7)](../man7/capabilities.7.html)

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
