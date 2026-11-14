---
{"title": "proc_kpageflags(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_kpageflags.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_kpageflags(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_kpageflags(5)         File Formats Manual         proc_kpageflags(5)

## [](#NAME)NAME

           /proc/kpageflags - physical pages frame masks

## [](#DESCRIPTION)DESCRIPTION

           /proc/kpageflags (since Linux 2.6.25)
                  This file contains 64-bit masks corresponding to each
                  physical page frame; it is indexed by page frame number
                  (see the discussion of /proc/pid/pagemap).  The bits are as
                  follows:

                          0   -   KPF_LOCKED
                          1   -   KPF_ERROR
                          2   -   KPF_REFERENCED
                          3   -   KPF_UPTODATE
                          4   -   KPF_DIRTY
                          5   -   KPF_LRU
                          6   -   KPF_ACTIVE
                          7   -   KPF_SLAB
                          8   -   KPF_WRITEBACK
                          9   -   KPF_RECLAIM
                         10   -   KPF_BUDDY
                         11   -   KPF_MMAP            (since Linux 2.6.31)
                         12   -   KPF_ANON            (since Linux 2.6.31)
                         13   -   KPF_SWAPCACHE       (since Linux 2.6.31)
                         14   -   KPF_SWAPBACKED      (since Linux 2.6.31)
                         15   -   KPF_COMPOUND_HEAD   (since Linux 2.6.31)
                         16   -   KPF_COMPOUND_TAIL   (since Linux 2.6.31)
                         17   -   KPF_HUGE            (since Linux 2.6.31)
                         18   -   KPF_UNEVICTABLE     (since Linux 2.6.31)
                         19   -   KPF_HWPOISON        (since Linux 2.6.31)
                         20   -   KPF_NOPAGE          (since Linux 2.6.31)
                         21   -   KPF_KSM             (since Linux 2.6.32)
                         22   -   KPF_THP             (since Linux 3.4)
                         23   -   KPF_BALLOON         (since Linux 3.18)
                         24   -   KPF_ZERO_PAGE       (since Linux 4.0)
                         25   -   KPF_IDLE            (since Linux 4.3)
                         26   -   KPF_PGTABLE         (since Linux 4.18)

                  For further details on the meanings of these bits, see the
                  kernel source file
                  Documentation/admin-guide/mm/pagemap.rst.  Before Linux
                  2.6.29, KPF_WRITEBACK, KPF_RECLAIM, KPF_BUDDY, and
                  KPF_LOCKED did not report correctly.

                  The /proc/kpageflags file is present only if the
                  CONFIG_PROC_PAGE_MONITOR kernel configuration option is
                  enabled.

## [](#SEE_ALSO)SEE ALSO

           proc(5)

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

    Linux man-pages 6.19            2026-02-08             proc_kpageflags(5)

------------------------------------------------------------------------

Pages that refer to this page: [proc(5)](../man5/proc.5.html)

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
