---
{"title": "dqinfo(2type) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/dqinfo.2type.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# dqinfo(2type) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dqinfo(2type)                                               dqinfo(2type)

## [](#NAME)NAME

           dqinfo - disk quota information

## [](#LIBRARY)LIBRARY

           Standard C library (libc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/quota.h>

           struct dqinfo {
                uint64_t  dqi_bgrace;
                uint64_t  dqi_igrace;
                uint32_t  dqi_flags;
                uint32_t  dqi_valid;
           };

           /* Quota format QFMT_VFS_OLD */
           #define DQF_ROOT_SQUASH (1 << 0)

           /* Quota format QFMT_VFS_V0 / QFMT_VFS_V1 */
           #define DQF_SYS_FILE    (1 << 16)

           #define IIF_BGRACE  1
           #define IIF_IGRACE  2
           #define IIF_FLAGS   4
           #define IIF_ALL     (IIF_BGRACE | IIF_IGRACE | IIF_FLAGS)

## [](#DESCRIPTION)DESCRIPTION

       struct dqinfo
           .dqi_bgrace
                  Time before block soft limit becomes hard limit.

           .dqi_igrace
                  Time before inode soft limit becomes hard limit.

           .dqi_flags
                  Flags for quotafile (DQF_*).

           .dqi_valid
                  Bit mask of IIF_* constants.  It is set to indicate which
                  fields in the dqinfo structure are valid.

       DQF_*
           DQF_ROOT_SQUASH
                  Root squash enabled.

           DQF_SYS_FILE
                  Quota stored in a system file.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.4.22.

           Before Linux 4.0, DQF_ROOT_SQUASH had been defined privately as
           V1_DQF_RSQUASH.

## [](#SEE_ALSO)SEE ALSO

           Q_GETINFO(2const), Q_SETINFO(2const)

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

    Linux man-pages 6.19            2026-06-05                  dqinfo(2type)

------------------------------------------------------------------------

Pages that refer to this page: [Q_GETINFO(2const)](../man2/Q_GETINFO.2const.html),  [Q_SETINFO(2const)](../man2/Q_SETINFO.2const.html)

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
