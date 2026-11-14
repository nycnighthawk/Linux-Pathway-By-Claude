---
{"title": "__riscv_flush_icache(3) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/riscv_flush_icache.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# \_\_riscv_flush_icache(3) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    __riscv_flush_icache(3)  Library Functions Manual __riscv_flush_icache(3)

## [](#NAME)NAME

           __riscv_flush_icache - Flush icaches on RISC-V

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/cachectl.h>

           int __riscv_flush_icache(void *start, void *end, unsigned long flags);

## [](#DESCRIPTION)DESCRIPTION

           __riscv_flush_icache() enforces ordering between stores and
           instruction cache fetches.

           The range of addresses over which ordering is enforced is
           specified by start and end.

           The flags argument controls the extent of this ordering, with the
           default behavior (a flags value of 0) being to enforce the fence
           on all threads in the current process.  Setting the
           SYS_RISCV_FLUSH_ICACHE_LOCAL bit allows users to indicate that
           enforcing ordering on only the current thread is necessary.  All
           other bits in flags are reserved.

## [](#STANDARDS)STANDARDS

           Linux on RISC-V.

## [](#HISTORY)HISTORY

           Linux 4.15.  glibc 2.27.

## [](#SEE_ALSO)SEE ALSO

           syscall(2)

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

    Linux man-pages 6.19            2026-02-08        __riscv_flush_icache(3)

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
