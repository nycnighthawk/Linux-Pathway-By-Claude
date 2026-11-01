---
{"title": "cachestat(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/cachestat.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# cachestat(2) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [CAVEATS](#CAVEATS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    cachestat(2)               System Calls Manual               cachestat(2)

## [](#NAME)NAME

           cachestat - query the page cache statistics of a file

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/mman.h>

           int cachestat(unsigned int fd, struct cachestat_range *cstat_range,
                         struct cachestat *cstat, unsigned int flags);

           struct cachestat_range {
               __u64 off;
               __u64 len;
           };

           struct cachestat {
               __u64 nr_cache;
               __u64 nr_dirty;
               __u64 nr_writeback;
               __u64 nr_evicted;
               __u64 nr_recently_evicted;
           };

## [](#DESCRIPTION)DESCRIPTION

           cachestat() queries the number of cached pages, dirty pages, pages
           marked for writeback, evicted pages, and recently evicted pages in
           the byte range specified by .off and .len in the cachestat_range
           structure.

           An evicted page is one that was previously in the page cache but
           has since been evicted.  A page is considered recently evicted if
           its reentry into the cache would indicate active usage under
           memory pressure.

           The results are returned in a cachestat structure, pointed to by
           the cstat argument.

           The .off and .len fields must be non-negative.  If .len > 0, the
           queried range is [.off, .off+.len].  If len == 0, the range is
           from .off to the end of the file.

           The flags argument is reserved for future use and must be set to
           0.

           Currently, hugetlbfs files are not supported.

## [](#RETURN_VALUE)RETURN VALUE

           On success, cachestat() returns 0.  On error, -1 is returned, and
           errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT cstat or cstat_range point to an invalid address.

           EINVAL Invalid flags value.

           EBADF  Invalid file descriptor.

           EOPNOTSUPP
                  The file descriptor refers to a hugetlbfs file, which is
                  unsupported.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 6.5.

## [](#CAVEATS)CAVEATS

           Note that the status of a page may change after cachestat()
           retrieves it but before the values are returned to the
           application; thus, the values may be slightly outdated.

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

    Linux man-pages 6.19            2025-06-28                   cachestat(2)

------------------------------------------------------------------------

Pages that refer to this page: [fincore(1)](../man1/fincore.1.html)

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
