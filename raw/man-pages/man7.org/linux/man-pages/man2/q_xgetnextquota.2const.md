---
{"title": "Q_XGETNEXTQUOTA(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/q_xgetnextquota.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# Q_XGETNEXTQUOTA(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    Q_XGETNEXTQUOTA(2const)                           Q_XGETNEXTQUOTA(2const)

## [](#NAME)NAME

           Q_XGETNEXTQUOTA - get disk quota limits for next user or group for
           an XFS filesystem

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <xfs/xqm.h>      /* See quotactl(2) */
           #include <sys/quota.h>

           int quotactl(QCMD(Q_XGETNEXTQUOTA, type), const char *_Nullable special,
                        int id, caddr_t addr);

           #include <xfs/xqm.h>      /* See quotactl_fd(2) */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_quotactl_fd, int fd, QCMD(Q_XGETNEXTQUOTA, type),
                        int id, struct fs_disk_quota *addr);

## [](#DESCRIPTION)DESCRIPTION

           This operation is the same as Q_XGETQUOTA(2const), but it returns
           (in the fs_disk_quota(2type) structure pointed to by addr) quota
           information for the next ID greater than or equal to id that has a
           quota set.

           Since fs_disk_quota(2type) already has q_id field, no separate
           structure type is needed (in contrast with Q_GETQUOTA(2const) and
           Q_GETNEXTQUOTA(2const)).

## [](#RETURN_VALUE)RETURN VALUE

           See quotactl(2).

## [](#ERRORS)ERRORS

           See quotactl(2).

           ESRCH  There is no ID greater than or equal to id that has an
                  active quota.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 4.6.

## [](#SEE_ALSO)SEE ALSO

           quotactl(2), quotactl_fd(2), Q_XGETQUOTA(2const),
           fs_disk_quota(2type)

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

    Linux man-pages 6.19            2026-06-05        Q_XGETNEXTQUOTA(2const)

------------------------------------------------------------------------

Pages that refer to this page: [fs_disk_quota(2type)](../man2/fs_disk_quota.2type.html),  [quotactl(2)](../man2/quotactl.2.html),  [Q_XGETQUOTA(2const)](../man2/Q_XGETQUOTA.2const.html)

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
