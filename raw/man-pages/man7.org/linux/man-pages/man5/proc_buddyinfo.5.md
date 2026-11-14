---
{"title": "proc_buddyinfo(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_buddyinfo.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_buddyinfo(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_buddyinfo(5)          File Formats Manual          proc_buddyinfo(5)

## [](#NAME)NAME

           /proc/buddyinfo - memory fragmentation

## [](#DESCRIPTION)DESCRIPTION

           /proc/buddyinfo
                  This file contains information which is used for diagnosing
                  memory fragmentation issues.  Each line starts with the
                  identification of the node and the name of the zone which
                  together identify a memory region.  This is then followed
                  by the count of available chunks of a certain order in
                  which these zones are split.  The size in bytes of a
                  certain order is given by the formula:

                      (2^order) * PAGE_SIZE

                  The binary buddy allocator algorithm inside the kernel will
                  split one chunk into two chunks of a smaller order (thus
                  with half the size) or combine two contiguous chunks into
                  one larger chunk of a higher order (thus with double the
                  size) to satisfy allocation requests and to counter memory
                  fragmentation.  The order matches the column number, when
                  starting to count at zero.

                  For example on an x86-64 system:
             Node 0, zone     DMA     1    1    1    0    2    1    1    0    1    1    3
             Node 0, zone   DMA32    65   47    4   81   52   28   13   10    5    1  404
             Node 0, zone  Normal   216   55  189  101   84   38   37   27    5    3  587

                  In this example, there is one node containing three zones
                  and there are 11 different chunk sizes.  If the page size
                  is 4 kilobytes, then the first zone called DMA (on x86 the
                  first 16 megabyte of memory) has 1 chunk of 4 kilobytes
                  (order 0) available and has 3 chunks of 4 megabytes (order
                  10) available.

                  If the memory is heavily fragmented, the counters for
                  higher order chunks will be zero and allocation of large
                  contiguous areas will fail.

                  Further information about the zones can be found in
                  /proc/zoneinfo.

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

    Linux man-pages 6.19            2026-02-08              proc_buddyinfo(5)

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
