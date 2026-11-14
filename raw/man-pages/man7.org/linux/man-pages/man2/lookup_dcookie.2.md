---
{"title": "lookup_dcookie(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/lookup_dcookie.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lookup_dcookie(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lookup_dcookie(2)          System Calls Manual          lookup_dcookie(2)

## [](#NAME)NAME

           lookup_dcookie - return a directory entry's path

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(size_t size;
                       SYS_lookup_dcookie, uint64_t cookie, char buffer[size],
                       size_t size);

           Note: glibc provides no wrapper for lookup_dcookie(),
           necessitating the use of syscall(2).

## [](#DESCRIPTION)DESCRIPTION

           Look up the full path of the directory entry specified by the
           value cookie.  The cookie is an opaque identifier uniquely
           identifying a particular directory entry.  The buffer given is
           filled in with the full path of the directory entry.

           For lookup_dcookie() to return successfully, the kernel must still
           hold a cookie reference to the directory entry.

## [](#RETURN_VALUE)RETURN VALUE

           On success, lookup_dcookie() returns the length of the path string
           copied into the buffer.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT The buffer was not valid.

           EINVAL The kernel has no registered cookie/directory entry
                  mappings at the time of lookup, or the cookie does not
                  refer to a valid directory entry.

           ENAMETOOLONG
                  The name could not fit in the buffer.

           ENOMEM The kernel could not allocate memory for the temporary
                  buffer holding the path.

           EPERM  The process does not have the capability CAP_SYS_ADMIN
                  required to look up cookie values.

           ERANGE The buffer was not large enough to hold the path of the
                  directory entry.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.5.43.

           The ENAMETOOLONG error was added in Linux 2.5.70.

## [](#NOTES)NOTES

           lookup_dcookie() is a special-purpose system call, currently used
           only by the oprofile(1) profiler.  It relies on a kernel driver to
           register cookies for directory entries.

           The path returned may be suffixed by the string " (deleted)" if
           the directory entry has been removed.

## [](#SEE_ALSO)SEE ALSO

           oprofile(1)

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

    Linux man-pages 6.19            2026-02-08              lookup_dcookie(2)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html),  [capabilities(7)](../man7/capabilities.7.html)

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
