---
{"title": "getcpu(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/getcpu.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# getcpu(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    getcpu(2)                  System Calls Manual                  getcpu(2)

## [](#NAME)NAME

           getcpu - determine CPU and NUMA node on which the calling thread
           is running

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #define _GNU_SOURCE             /* See feature_test_macros(7) */
           #include <sched.h>

           int getcpu(unsigned int *_Nullable cpu, unsigned int *_Nullable node);

## [](#DESCRIPTION)DESCRIPTION

           The getcpu() system call identifies the processor and node on
           which the calling thread or process is currently running and
           writes them into the integers pointed to by the cpu and node
           arguments.  The processor is a unique small integer identifying a
           CPU.  The node is a unique small identifier identifying a NUMA
           node.  When either cpu or node is NULL nothing is written to the
           respective pointer.

           The information placed in cpu is guaranteed to be current only at
           the time of the call: unless the CPU affinity has been fixed using
           sched_setaffinity(2), the kernel might change the CPU at any time.
           (Normally this does not happen because the scheduler tries to
           minimize movements between CPUs to keep caches hot, but it is
           possible.)  The caller must allow for the possibility that the
           information returned in cpu and node is no longer current by the
           time the call returns.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT Arguments point outside the calling process's address
                  space.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.19 (x86-64 and i386), glibc 2.29.

       C library/kernel differences
           The kernel system call has a third argument:

               int getcpu(unsigned int *cpu, unsigned int *node,
                          struct getcpu_cache *tcache);

           The tcache argument is unused since Linux 2.6.24, and (when
           invoking the system call directly) should be specified as NULL,
           unless portability to Linux 2.6.23 or earlier is required.

           In Linux 2.6.23 and earlier, if the tcache argument was non-NULL,
           then it specified a pointer to a caller-allocated buffer in
           thread-local storage that was used to provide a caching mechanism
           for getcpu().  Use of the cache could speed getcpu() calls, at the
           cost that there was a very small chance that the returned
           information would be out of date.  The caching mechanism was
           considered to cause problems when migrating threads between CPUs,
           and so the argument is now ignored.

## [](#NOTES)NOTES

           Linux makes a best effort to make this call as fast as possible.
           (On some architectures, this is done via an implementation in the
           vdso(7).)  The intention of getcpu() is to allow programs to make
           optimizations with per-CPU data or for NUMA optimization.

## [](#SEE_ALSO)SEE ALSO

           mbind(2), sched_setaffinity(2), set_mempolicy(2), sched_getcpu(3),
           cpuset(7), vdso(7)

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

    Linux man-pages 6.19            2026-02-08                      getcpu(2)

------------------------------------------------------------------------

Pages that refer to this page: [get_mempolicy(2)](../man2/get_mempolicy.2.html),  [mbind(2)](../man2/mbind.2.html),  [sched_setaffinity(2)](../man2/sched_setaffinity.2.html),  [set_mempolicy(2)](../man2/set_mempolicy.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [sched_getcpu(3)](../man3/sched_getcpu.3.html),  [cpuset(7)](../man7/cpuset.7.html)

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
