---
{"title": "Q_XQUOTASYNC(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/Q_XQUOTASYNC.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# Q_XQUOTASYNC(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    Q_XQUOTASYNC(2const)                                 Q_XQUOTASYNC(2const)

## [](#NAME)NAME

           Q_XQUOTASYNC - no-op

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <xfs/xqm.h>      /* See quotactl(2) */
           #include <sys/quota.h>

           [[deprecated]]
           int quotactl(QCMD(Q_XQUOTASYNC, type), NULL, 0, NULL);

           #include <xfs/xqm.h>      /* See quotactl_fd(2) */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           [[deprecated]]
           int syscall(SYS_quotactl_fd, int fd, QCMD(Q_XQUOTASYNC, type));

## [](#DESCRIPTION)DESCRIPTION

           This operation was an XFS quota equivalent to Q_SYNC(2const), but
           it is no-op since Linux 3.4, as sync(1) writes quota information
           to disk now (in addition to the other filesystem metadata that it
           writes out).

## [](#RETURN_VALUE)RETURN VALUE

           See quotactl(2)

## [](#ERRORS)ERRORS

           See quotactl(2)

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.15.  No-op since Linux 3.4.

## [](#SEE_ALSO)SEE ALSO

           quotactl(2), quotactl_fd(2)

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

    Linux man-pages 6.19            2026-06-05           Q_XQUOTASYNC(2const)

------------------------------------------------------------------------

Pages that refer to this page: [quotactl(2)](../man2/quotactl.2.html)

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
