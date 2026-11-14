---
{"title": "Q_GETNEXTQUOTA(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/q_getnextquota.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# Q_GETNEXTQUOTA(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    Q_GETNEXTQUOTA(2const)                             Q_GETNEXTQUOTA(2const)

## [](#NAME)NAME

           Q_GETNEXTQUOTA - get disk quota limits and current usage for next
           user or group

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/quota.h>

           int quotactl(QCMD(Q_GETNEXTQUOTA, type), const char *_Nullable special,
                        int id, caddr_t addr);

           #include <sys/quota.h>    /* Definition of Q_* constants */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_quotactl_fd, int fd, QCMD(Q_GETNEXTQUOTA, type),
                       int id, struct nextdqblk *addr);

           #include <sys/quota.h>

           struct nextdqblk {
                uint64_t  dqb_bhardlimit;
                uint64_t  dqb_bsoftlimit;
                uint64_t  dqb_curspace;
                uint64_t  dqb_ihardlimit;
                uint64_t  dqb_isoftlimit;
                uint64_t  dqb_curinodes;
                uint64_t  dqb_btime;
                uint64_t  dqb_itime;

                uint32_t  dqb_valid;

                uint32_t  dqb_id;
           };

## [](#DESCRIPTION)DESCRIPTION

           This operation is the same as Q_GETQUOTA(2const), but it returns
           quota information for the next ID greater than or equal to id that
           has a quota set.

           The addr argument is a pointer to a nextdqblk structure whose
           fields are as for the dqblk(2type), except for the addition of a
           .dqb_id field that is used to return the ID for which quota
           information is being returned.

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

           quotactl(2), quotactl_fd(2), Q_GETQUOTA(2const), dqblk(2type)

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

    Linux man-pages 6.19            2026-06-05         Q_GETNEXTQUOTA(2const)

------------------------------------------------------------------------

Pages that refer to this page: [Q_GETQUOTA(2const)](../man2/Q_GETQUOTA.2const.html),  [quotactl(2)](../man2/quotactl.2.html),  [Q_XGETNEXTQUOTA(2const)](../man2/Q_XGETNEXTQUOTA.2const.html)

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
