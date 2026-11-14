---
{"title": "pkey_alloc(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pkey_free.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pkey_alloc(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    pkey_alloc(2)              System Calls Manual              pkey_alloc(2)

## [](#NAME)NAME

           pkey_alloc, pkey_free - allocate or free a protection key

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #define _GNU_SOURCE             /* See feature_test_macros(7) */
           #include <sys/mman.h>

           int pkey_alloc(unsigned int flags, unsigned int access_rights);
           int pkey_free(int pkey);

## [](#DESCRIPTION)DESCRIPTION

           pkey_alloc() allocates a protection key (pkey) and allows it to be
           passed to pkey_mprotect(2).

           The pkey_alloc() flags is reserved for future use and currently
           must always be specified as 0.

           The pkey_alloc() access_rights argument may contain zero or more
           disable operations:

           PKEY_DISABLE_ACCESS
                  Disable all data access to memory covered by the returned
                  protection key.

           PKEY_DISABLE_WRITE
                  Disable write access to memory covered by the returned
                  protection key.

           pkey_free() frees a protection key and makes it available for
           later allocations.  After a protection key has been freed, it may
           no longer be used in any protection-key-related operations.

           An application should not call pkey_free() on any protection key
           which has been assigned to an address range by pkey_mprotect(2)
           and which is still in use.  The behavior in this case is undefined
           and may result in an error.

## [](#RETURN_VALUE)RETURN VALUE

           On success, pkey_alloc() returns a positive protection key value.
           On success, pkey_free() returns zero.  On error, -1 is returned,
           and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL pkey, flags, or access_rights is invalid.

           ENOSPC (pkey_alloc()) All protection keys available for the
                  current process have been allocated.  The number of keys
                  available is architecture-specific and implementation-
                  specific and may be reduced by kernel-internal use of
                  certain keys.  There are currently 15 keys available to
                  user programs on x86.

                  This error will also be returned if the processor or
                  operating system does not support protection keys.
                  Applications should always be prepared to handle this
                  error, since factors outside of the application's control
                  can reduce the number of available pkeys.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 4.9, glibc 2.27.

## [](#NOTES)NOTES

           pkey_alloc() is always safe to call regardless of whether or not
           the operating system supports protection keys.  It can be used in
           lieu of any other mechanism for detecting pkey support and will
           simply fail with the error ENOSPC if the operating system has no
           pkey support.

           The kernel guarantees that the contents of the hardware rights
           register (PKRU) will be preserved only for allocated protection
           keys.  Any time a key is unallocated (either before the first call
           returning that key from pkey_alloc() or after it is freed via
           pkey_free()), the kernel may make arbitrary changes to the parts
           of the rights register affecting access to that key.

## [](#EXAMPLES)EXAMPLES

           See pkeys(7).

## [](#SEE_ALSO)SEE ALSO

           pkey_mprotect(2), pkeys(7)

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

    Linux man-pages 6.19            2026-02-08                  pkey_alloc(2)

------------------------------------------------------------------------

Pages that refer to this page: [mprotect(2)](../man2/mprotect.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [pkeys(7)](../man7/pkeys.7.html)

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
