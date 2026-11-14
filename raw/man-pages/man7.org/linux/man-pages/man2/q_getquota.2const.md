---
{"title": "Q_GETQUOTA(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/q_getquota.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# Q_GETQUOTA(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    Q_GETQUOTA(2const)                                     Q_GETQUOTA(2const)

## [](#NAME)NAME

           Q_GETQUOTA - get disk quota limits and current usage for user or
           group

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/quota.h>

           int quotactl(QCMD(Q_GETQUOTA, type), const char *_Nullable special,
                        int id, caddr_t addr);

           #include <sys/quota.h>    /* Definition of Q_* constants */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_quotactl_fd, int fd, QCMD(Q_GETQUOTA, type),
                       int id, struct dqblk *addr);

## [](#DESCRIPTION)DESCRIPTION

           Get disk quota limits and current usage for user or group id.

           The addr argument is a pointer to a dqblk(2type) structure.

           Currently, the kernel fills in all entries of the dqblk(2type)
           structure and marks them as valid in the .dqb_valid field.

           Unprivileged users may retrieve only their own quotas; a
           privileged user (CAP_SYS_ADMIN) can retrieve the quotas of any
           user.

## [](#RETURN_VALUE)RETURN VALUE

           See quotactl(2).

## [](#ERRORS)ERRORS

           See quotactl(2).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux.

## [](#SEE_ALSO)SEE ALSO

           quotactl(2), quotactl_fd(2), Q_GETNEXTQUOTA(2const), dqblk(2type)

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

    Linux man-pages 6.19            2026-06-05             Q_GETQUOTA(2const)

------------------------------------------------------------------------

Pages that refer to this page: [dqblk(2type)](../man2/dqblk.2type.html),  [Q_GETNEXTQUOTA(2const)](../man2/Q_GETNEXTQUOTA.2const.html),  [quotactl(2)](../man2/quotactl.2.html),  [Q_XGETNEXTQUOTA(2const)](../man2/Q_XGETNEXTQUOTA.2const.html)

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
