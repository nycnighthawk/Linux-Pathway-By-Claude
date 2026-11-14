---
{"title": "getpagesize(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/getpagesize.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# getpagesize(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    getpagesize(2)             System Calls Manual             getpagesize(2)

## [](#NAME)NAME

           getpagesize - get memory page size

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           int getpagesize(void);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           getpagesize():
               Since glibc 2.20:
                   _DEFAULT_SOURCE || ! (_POSIX_C_SOURCE >= 200112L)
               glibc 2.12 to glibc 2.19:
                   _BSD_SOURCE || ! (_POSIX_C_SOURCE >= 200112L)
               Before glibc 2.12:
                   _BSD_SOURCE || _XOPEN_SOURCE >= 500

## [](#DESCRIPTION)DESCRIPTION

           The function getpagesize() returns the number of bytes in a memory
           page, where "page" is a fixed-length block, the unit for memory
           allocation and file mapping performed by mmap(2).

## [](#VERSIONS)VERSIONS

           A user program should not hard-code a page size, neither as a
           literal nor using the PAGE_SIZE macro, because some architectures
           support multiple page sizes.

           This manual page is in section 2 because Alpha, SPARC, and SPARC64
           all have a Linux system call getpagesize() though other
           architectures do not, and use the ELF auxiliary vector instead.

## [](#STANDARDS)STANDARDS

           None.

## [](#HISTORY)HISTORY

           4.2BSD, SVr4, SUSv1.  In SUSv2 the getpagesize() call was labeled
           LEGACY, and it was removed in POSIX.1-2001.

           glibc 2.0 returned a constant even on architectures with multiple
           page sizes.

## [](#SEE_ALSO)SEE ALSO

           mmap(2), sysconf(3)

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

    Linux man-pages 6.19            2026-02-08                 getpagesize(2)

------------------------------------------------------------------------

Pages that refer to this page: [fincore(1)](../man1/fincore.1.html),  [strace(1)](../man1/strace.1.html),  [mmap2(2)](../man2/mmap2.2.html),  [mmap(2)](../man2/mmap.2.html),  [mremap(2)](../man2/mremap.2.html),  [remap_file_pages(2)](../man2/remap_file_pages.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [aligned_alloc(3)](../man3/aligned_alloc.3.html),  [numa(3)](../man3/numa.3.html)

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
