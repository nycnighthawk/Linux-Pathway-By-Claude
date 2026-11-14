---
{"title": "proc_pid_pagemap(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_pid_pagemap.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_pid_pagemap(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_pid_pagemap(5)        File Formats Manual        proc_pid_pagemap(5)

## [](#NAME)NAME

           /proc/pid/pagemap - mapping of virtual pages

## [](#DESCRIPTION)DESCRIPTION

           /proc/pid/pagemap (since Linux 2.6.25)
                  This file shows the mapping of each of the process's
                  virtual pages into physical page frames or swap area.  It
                  contains one 64-bit value for each virtual page, with the
                  bits set as follows:

                  63     If set, the page is present in RAM.

                  62     If set, the page is in swap space

                  61 (since Linux 3.5)
                         The page is a file-mapped page or a shared anonymous
                         page.

                  60–58 (since Linux 3.11)
                         Zero

                  57 (since Linux 5.14)
                         If set, the page is write-protected through
                         userfaultfd(2).

                  56 (since Linux 4.2)
                         The page is exclusively mapped.

                  55 (since Linux 3.11)
                         PTE is soft-dirty (see the kernel source file
                         Documentation/admin-guide/mm/soft-dirty.rst).

                  54–0   If the page is present in RAM (bit 63), then these
                         bits provide the page frame number, which can be
                         used to index /proc/kpageflags and /proc/kpagecount.
                         If the page is present in swap (bit 62), then bits
                         4–0 give the swap type, and bits 54–5 encode the
                         swap offset.

                  Before Linux 3.11, bits 60–55 were used to encode the
                  base-2 log of the page size.

                  To employ /proc/pid/pagemap efficiently, use /proc/pid/maps
                  to determine which areas of memory are actually mapped and
                  seek to skip over unmapped regions.

                  The /proc/pid/pagemap file is present only if the
                  CONFIG_PROC_PAGE_MONITOR kernel configuration option is
                  enabled.

                  Permission to access this file is governed by a ptrace
                  access mode PTRACE_MODE_READ_FSCREDS check; see ptrace(2).

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

    Linux man-pages 6.19            2026-02-08            proc_pid_pagemap(5)

------------------------------------------------------------------------

Pages that refer to this page: [proc_pid(5)](../man5/proc_pid.5.html)

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
