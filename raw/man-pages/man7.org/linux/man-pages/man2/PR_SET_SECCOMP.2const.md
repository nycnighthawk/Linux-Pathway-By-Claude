---
{"title": "PR_SET_SECCOMP(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/PR_SET_SECCOMP.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_SET_SECCOMP(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_SET_SECCOMP(2const)                             PR_SET_SECCOMP(2const)

## [](#NAME)NAME

           PR_SET_SECCOMP - set the secure computing mode

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           [[deprecated]]
           int prctl(PR_SET_SECCOMP, long mode, ...);

           [[deprecated]]
           int prctl(PR_SET_SECCOMP, SECCOMP_MODE_STRICT);
           [[deprecated]]
           int prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER,
                     struct sock_fprog *filter);

## [](#DESCRIPTION)DESCRIPTION

           Set the secure computing (seccomp) mode for the calling thread, to
           limit the available system calls.  The more recent seccomp(2)
           system call provides a superset of the functionality of
           PR_SET_SECCOMP, and is the preferred interface for new
           applications.

           The seccomp mode is selected via mode.  The seccomp constants are
           defined in <linux/seccomp.h>.  The following values can be
           specified:

           SECCOMP_MODE_STRICT (since Linux 2.6.23)
                  See the description of SECCOMP_SET_MODE_STRICT in
                  seccomp(2).

                  This operation is available only if the kernel is
                  configured with CONFIG_SECCOMP enabled.

           SECCOMP_MODE_FILTER (since Linux 3.5)
                  The allowed system calls are defined by a pointer to a
                  Berkeley Packet Filter passed in filter.  It can be
                  designed to filter arbitrary system calls and system call
                  arguments.  See the description of SECCOMP_SET_MODE_FILTER
                  in seccomp(2).

                  This operation is available only if the kernel is
                  configured with CONFIG_SECCOMP_FILTER enabled.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EACCES mode is SECCOMP_MODE_FILTER, but the process does not have
                  the CAP_SYS_ADMIN capability or has not set the
                  no_new_privs attribute (see PR_SET_NO_NEW_PRIVS(2const)).

           EFAULT mode is SECCOMP_MODE_FILTER, and filter is an invalid
                  address.

           EINVAL mode is not a valid value.

           EINVAL The kernel was not configured with CONFIG_SECCOMP.

           EINVAL mode is SECCOMP_MODE_FILTER, and the kernel was not
                  configured with CONFIG_SECCOMP_FILTER.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.23.

## [](#SEE_ALSO)SEE ALSO

           prctl(2), PR_GET_SECCOMP(2const), seccomp(2)

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

    Linux man-pages 6.19            2026-02-08         PR_SET_SECCOMP(2const)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html),  [PR_GET_SECCOMP(2const)](../man2/PR_GET_SECCOMP.2const.html)

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
