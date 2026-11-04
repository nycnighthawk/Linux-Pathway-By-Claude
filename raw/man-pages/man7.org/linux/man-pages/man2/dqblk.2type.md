---
{"title": "dqblk(2type) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/dqblk.2type.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# dqblk(2type) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dqblk(2type)                                                 dqblk(2type)

## [](#NAME)NAME

           dqblk - disk quota block

## [](#LIBRARY)LIBRARY

           Standard C library (libc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/quota.h>

           struct dqblk {
                uint64_t  dqb_bhardlimit;
                uint64_t  dqb_bsoftlimit;
                uint64_t  dqb_curspace;
                uint64_t  dqb_ihardlimit;
                uint64_t  dqb_isoftlimit;
                uint64_t  dqb_curinodes;
                uint64_t  dqb_btime;
                uint64_t  dqb_itime;

                uint32_t  dqb_valid;
           };

           #define QIF_BLIMITS   1
           #define QIF_SPACE     2
           #define QIF_ILIMITS   4
           #define QIF_INODES    8
           #define QIF_BTIME     16
           #define QIF_ITIME     32
           #define QIF_LIMITS    (QIF_BLIMITS | QIF_ILIMITS)
           #define QIF_USAGE     (QIF_SPACE | QIF_INODES)
           #define QIF_TIMES     (QIF_BTIME | QIF_ITIME)
           #define QIF_ALL       (QIF_LIMITS | QIF_USAGE | QIF_TIMES)

## [](#DESCRIPTION)DESCRIPTION

           .dqb_bhardlimit
           .dqb_bsoftlimit
                  Absolute and preferred limits on disk quota blocks.

           .dqb_curspace
                  Current occupied space (in bytes).

           .dqb_ihardlimit
           .dqb_isoftlimit
                  Absolute and preferred limits on number of allocated
                  inodes.

           .dqb_curinodes
                  Current number of allocated inodes.

           .dqb_btime
                  Time limit for excessive disk use.

           .dqb_itime
                  Time limit for excessive files.

           .dqb_valid
                  Bit mask of QIF_* constants.  It is set to indicate which
                  fields in the dqblk structure are valid.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.4.22.

## [](#SEE_ALSO)SEE ALSO

           Q_GETQUOTA(2const), Q_SETQUOTA(2const), nextdqblk(2type)

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

    Linux man-pages 6.19            2026-06-05                   dqblk(2type)

------------------------------------------------------------------------

Pages that refer to this page: [Q_GETNEXTQUOTA(2const)](../man2/Q_GETNEXTQUOTA.2const.html),  [Q_GETQUOTA(2const)](../man2/Q_GETQUOTA.2const.html),  [Q_SETQUOTA(2const)](../man2/Q_SETQUOTA.2const.html)

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
