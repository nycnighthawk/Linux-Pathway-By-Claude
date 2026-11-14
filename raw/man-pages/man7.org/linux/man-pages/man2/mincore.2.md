---
{"title": "mincore(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/mincore.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mincore(2) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mincore(2)                 System Calls Manual                 mincore(2)

## [](#NAME)NAME

           mincore - determine whether pages are resident in memory

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/mman.h>

           int mincore(size_t length;
                       void addr[length], size_t length, unsigned char *vec);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           mincore():
               Since glibc 2.19:
                   _DEFAULT_SOURCE
               glibc 2.19 and earlier:
                   _BSD_SOURCE || _SVID_SOURCE

## [](#DESCRIPTION)DESCRIPTION

           mincore() returns a vector that indicates whether pages of the
           calling process's virtual memory are resident in core (RAM), and
           so will not cause a disk access (page fault) if referenced.  The
           kernel returns residency information about the pages starting at
           the address addr, and continuing for length bytes.

           The addr argument must be a multiple of the system page size.  The
           length argument need not be a multiple of the page size, but since
           residency information is returned for whole pages, length is
           effectively rounded up to the next multiple of the page size.  One
           may obtain the page size (PAGE_SIZE) using sysconf(_SC_PAGESIZE).

           The vec argument must point to an array containing at least
           (length+PAGE_SIZE-1) / PAGE_SIZE bytes.  On return, the least
           significant bit of each byte will be set if the corresponding page
           is currently resident in memory, and be clear otherwise.  (The
           settings of the other bits in each byte are undefined; these bits
           are reserved for possible later use.)  Of course the information
           returned in vec is only a snapshot: pages that are not locked in
           memory can come and go at any moment, and the contents of vec may
           already be stale by the time this call returns.

## [](#RETURN_VALUE)RETURN VALUE

           On success, mincore() returns zero.  On error, -1 is returned, and
           errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EAGAIN kernel is temporarily out of resources.

           EFAULT vec points to an invalid address.

           EINVAL addr is not a multiple of the page size.

           ENOMEM length is greater than (TASK_SIZE - addr).  (This could
                  occur if a negative value is specified for length, since
                  that value will be interpreted as a large unsigned
                  integer.)  In Linux 2.6.11 and earlier, the error EINVAL
                  was returned for this condition.

           ENOMEM addr to addr + length contained unmapped memory.

## [](#STANDARDS)STANDARDS

           None.

## [](#HISTORY)HISTORY

           SunOS 4.1, 4.4BSD, FreeBSD 2.2, Solaris 8, Linux 2.3.99pre1, glibc
           2.2, NetBSD 1.5, OpenBSD 2.9, AIX 5.1.

## [](#BUGS)BUGS

           Before Linux 2.6.21, mincore() did not return correct information
           for MAP_PRIVATE mappings, or for nonlinear mappings (established
           using remap_file_pages(2)).

## [](#SEE_ALSO)SEE ALSO

           fincore(1), madvise(2), mlock(2), mmap(2), posix_fadvise(2),
           posix_madvise(3)

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

    Linux man-pages 6.19            2026-02-16                     mincore(2)

------------------------------------------------------------------------

Pages that refer to this page: [fincore(1)](../man1/fincore.1.html),  [madvise(2)](../man2/madvise.2.html),  [mlock(2)](../man2/mlock.2.html),  [mmap(2)](../man2/mmap.2.html),  [posix_fadvise(2)](../man2/posix_fadvise.2.html),  [syscalls(2)](../man2/syscalls.2.html)

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
