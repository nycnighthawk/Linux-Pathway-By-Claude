---
{"title": "getsid(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/getsid.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# getsid(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    getsid(2)                  System Calls Manual                  getsid(2)

## [](#NAME)NAME

           getsid - get session ID

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           pid_t getsid(pid_t pid);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           getsid():
               _XOPEN_SOURCE >= 500
                   || /* Since glibc 2.12: */ _POSIX_C_SOURCE >= 200809L

## [](#DESCRIPTION)DESCRIPTION

           getsid() returns the session ID of the process with process ID
           pid.  If pid is 0, getsid() returns the session ID of the calling
           process.

## [](#RETURN_VALUE)RETURN VALUE

           On success, a session ID is returned.  On error, (pid_t) -1 is
           returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EPERM  A process with process ID pid exists, but it is not in the
                  same session as the calling process, and the implementation
                  considers this an error.

           ESRCH  No process with process ID pid was found.

## [](#VERSIONS)VERSIONS

           Linux does not return EPERM.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           SVr4, SUSv1, Linux 2.0, POSIX.1-2001 XSI, POSIX.1-2008.

## [](#NOTES)NOTES

           See credentials(7) for a description of sessions and session IDs.

## [](#SEE_ALSO)SEE ALSO

           getpgid(2), setsid(2), credentials(7)

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

    Linux man-pages 6.19            2026-02-08                      getsid(2)

------------------------------------------------------------------------

Pages that refer to this page: [ps(1)](../man1/ps.1.html),  [setsid(2)](../man2/setsid.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [id_t(3type)](../man3/id_t.3type.html),  [sd_pid_get_owner_uid(3)](../man3/sd_pid_get_owner_uid.3.html),  [tcgetsid(3)](../man3/tcgetsid.3.html),  [utmp(5)](../man5/utmp.5.html),  [credentials(7)](../man7/credentials.7.html)

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
