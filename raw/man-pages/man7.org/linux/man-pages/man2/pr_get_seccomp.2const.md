---
{"title": "PR_GET_SECCOMP(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pr_get_seccomp.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_GET_SECCOMP(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [FILES](#FILES) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_GET_SECCOMP(2)          System Calls Manual          PR_GET_SECCOMP(2)

## [](#NAME)NAME

           PR_GET_SECCOMP - get the secure computing mode

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_GET_SECCOMP);

## [](#DESCRIPTION)DESCRIPTION

           Return the secure computing mode of the calling thread.

           If the caller is not in secure computing mode, this operation
           returns 0; if the caller is in strict secure computing mode, then
           the prctl() call will cause a SIGKILL signal to be sent to the
           process.  If the caller is in filter mode, and this system call is
           allowed by the seccomp filters, it returns 2; otherwise, the
           process is killed with a SIGKILL signal.

           This operation is available only if the kernel is configured with
           CONFIG_SECCOMP enabled.

## [](#RETURN_VALUE)RETURN VALUE

           On success, this call returns the nonnegative value described
           above.  On error, -1 is returned, and errno is set to indicate the
           error; or the process is killed.

## [](#ERRORS)ERRORS

           EINVAL The kernel was not configured with CONFIG_SECCOMP.

           SIGKILL
                  The caller is in strict secure computing mode.

           SIGKILL
                  The caller is in filter mode, and this system call is not
                  allowed by the seccomp filters.

## [](#FILES)FILES

           /proc/pid/status
                  Since Linux 3.8, the Seccomp field of this file provides a
                  method of obtaining the same information, without the risk
                  that the process is killed; see proc_pid_status(5).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.23.

## [](#SEE_ALSO)SEE ALSO

           prctl(2), PR_SET_SECCOMP(2const), seccomp(2)

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

    Linux man-pages 6.19            2026-02-08              PR_GET_SECCOMP(2)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html),  [PR_SET_SECCOMP(2const)](../man2/PR_SET_SECCOMP.2const.html)

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
