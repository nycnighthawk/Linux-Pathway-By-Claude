---
{"title": "getresuid(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/getresuid.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# getresuid(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    getresuid(2)               System Calls Manual               getresuid(2)

## [](#NAME)NAME

           getresuid, getresgid - get real, effective, and saved user/group
           IDs

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #define _GNU_SOURCE         /* See feature_test_macros(7) */
           #include <unistd.h>

           int getresuid(uid_t *ruid, uid_t *euid, uid_t *suid);
           int getresgid(gid_t *rgid, gid_t *egid, gid_t *sgid);

## [](#DESCRIPTION)DESCRIPTION

           getresuid() returns the real UID, the effective UID, and the saved
           set-user-ID of the calling process, in the arguments ruid, euid,
           and suid, respectively.  getresgid() performs the analogous task
           for the process's group IDs.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT One of the arguments specified an address outside the
                  calling program's address space.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024 XSI.

## [](#HISTORY)HISTORY

           Linux 2.1.44, glibc 2.3.2, POSIX.1-2024 XSI.

           The original Linux getresuid() and getresgid() system calls
           supported only 16-bit user and group IDs.  Subsequently, Linux 2.4
           added getresuid32() and getresgid32(), supporting 32-bit IDs.  The
           glibc getresuid() and getresgid() wrapper functions transparently
           deal with the variations across kernel versions.

## [](#SEE_ALSO)SEE ALSO

           getuid(2), setresuid(2), setreuid(2), setuid(2), credentials(7)

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

    Linux man-pages 6.19            2026-02-08                   getresuid(2)

------------------------------------------------------------------------

Pages that refer to this page: [getgid(2)](../man2/getgid.2.html),  [getuid(2)](../man2/getuid.2.html),  [setresuid(2)](../man2/setresuid.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [id_t(3type)](../man3/id_t.3type.html),  [credentials(7)](../man7/credentials.7.html)

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
