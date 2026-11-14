---
{"title": "mmap2(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/mmap2.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mmap2(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mmap2(2)                   System Calls Manual                   mmap2(2)

## [](#NAME)NAME

           mmap2 - map files or devices into memory

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/mman.h>    /* Definition of MAP_* and PROT_* constants */
           #include <sys/syscall.h> /* Definition of SYS_* constants */
           #include <unistd.h>

           void *syscall(SYS_mmap2, unsigned long addr, unsigned long length,
                         unsigned long prot, unsigned long flags,
                         unsigned long fd, unsigned long pgoffset);

## [](#DESCRIPTION)DESCRIPTION

           This is probably not the system call that you are interested in;
           instead, see mmap(2), which describes the glibc wrapper function
           that invokes this system call.

           The mmap2() system call provides the same interface as mmap(2),
           except that the final argument specifies the offset into the file
           in 4096-byte units (instead of bytes, as is done by mmap(2)).
           This enables applications that use a 32-bit off_t to map large
           files (up to 2^44 bytes).

## [](#RETURN_VALUE)RETURN VALUE

           On success, mmap2() returns a pointer to the mapped area.  On
           error, -1 is returned and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT Problem with getting the data from user space.

           EINVAL (Various platforms where the page size is not 4096 bytes.)
                  offset * 4096 is not a multiple of the system page size.

           mmap2() can also return any of the errors described in mmap(2).

## [](#VERSIONS)VERSIONS

           On architectures where this system call is present, the glibc
           mmap() wrapper function invokes this system call rather than the
           mmap(2) system call.

           This system call does not exist on x86-64.

           On ia64, the unit for offset is actually the system page size,
           rather than 4096 bytes.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.3.31.

## [](#SEE_ALSO)SEE ALSO

           getpagesize(2), mmap(2), mremap(2), msync(2), shm_open(3)

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

    Linux man-pages 6.19            2026-02-08                       mmap2(2)

------------------------------------------------------------------------

Pages that refer to this page: [mmap(2)](../man2/mmap.2.html),  [remap_file_pages(2)](../man2/remap_file_pages.2.html),  [syscalls(2)](../man2/syscalls.2.html)

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
