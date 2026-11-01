---
{"title": "cacheflush(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/cacheflush.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# cacheflush(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    cacheflush(2)              System Calls Manual              cacheflush(2)

## [](#NAME)NAME

           cacheflush - flush contents of instruction and/or data cache

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/cachectl.h>

           int cacheflush(int nbytes;
                          void addr[nbytes], int nbytes, int cache);

           Note: On some architectures, there is no glibc wrapper for this
           system call; see VERSIONS.

## [](#DESCRIPTION)DESCRIPTION

           cacheflush() flushes the contents of the indicated cache(s) for
           the user addresses in the range addr to (addr+nbytes-1).  cache
           may be one of:

           ICACHE Flush the instruction cache.

           DCACHE Write back to memory and invalidate the affected valid
                  cache lines.

           BCACHE Same as (ICACHE|DCACHE).

## [](#RETURN_VALUE)RETURN VALUE

           cacheflush() returns 0 on success.  On error, it returns -1 and
           sets errno to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT Some or all of the address range addr to (addr+nbytes-1) is
                  not accessible.

           EINVAL cache is not one of ICACHE, DCACHE, or BCACHE (but see
                  BUGS).

## [](#VERSIONS)VERSIONS

           cacheflush() should not be used in programs intended to be
           portable.  On Linux, this call first appeared on the MIPS
           architecture, but nowadays, Linux provides a cacheflush() system
           call on some other architectures, but with different arguments.

       Architecture-specific variants
           glibc provides a wrapper for this system call, with the prototype
           shown in SYNOPSIS, for the following architectures: ARC, CSKY,
           MIPS, and NIOS2.

           On some other architectures, Linux provides this system call, with
           different arguments:

           M68K:
                  int cacheflush(unsigned long addr, int scope, int cache,
                                 unsigned long size);

           SH:
                  int cacheflush(unsigned long addr, unsigned long size, int op);

           NDS32:
                  int cacheflush(unsigned int start, unsigned int end, int cache);

           On the above architectures, glibc does not provide a wrapper for
           this system call; call it using syscall(2).

       GCC alternative
           Unless you need the finer grained control that this system call
           provides, you probably want to use the GCC built-in function
           __builtin___clear_cache(), which provides a portable interface
           across platforms supported by GCC and compatible compilers:

               void __builtin___clear_cache(void *begin, void *end);

           On platforms that don't require instruction cache flushes,
           __builtin___clear_cache() has no effect.

           Note: On some GCC-compatible compilers, the prototype for this
           built-in function uses char * instead of void * for the
           parameters.

## [](#STANDARDS)STANDARDS

           Historically, this system call was available on all MIPS UNIX
           variants including RISC/os, IRIX, Ultrix, NetBSD, OpenBSD, and
           FreeBSD (and also on some non-UNIX MIPS operating systems), so
           that the existence of this call in MIPS operating systems is a de-
           facto standard.

## [](#BUGS)BUGS

           Linux kernels older than Linux 2.6.11 ignore the addr and nbytes
           arguments, making this function fairly expensive.  Therefore, the
           whole cache is always flushed.

           This function always behaves as if BCACHE has been passed for the
           cache argument and does not do any error checking on the cache
           argument.

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

    Linux man-pages 6.19            2026-02-08                  cacheflush(2)

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
