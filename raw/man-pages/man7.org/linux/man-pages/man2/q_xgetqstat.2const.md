---
{"title": "Q_XGETQSTAT(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/q_xgetqstat.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# Q_XGETQSTAT(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    Q_XGETQSTAT(2const)                                   Q_XGETQSTAT(2const)

## [](#NAME)NAME

           Q_XGETQSTAT - get XFS-specific quota information

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <xfs/xqm.h>      /* See quotactl(2) */
           #include <sys/quota.h>

           int quotactl(QCMD(Q_XGETQSTAT, type), const char *_Nullable special, 0,
                        caddr_t addr);

           #include <xfs/xqm.h>      /* See quotactl_fd(2) */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_quotactl_fd, int fd, QCMD(Q_XGETQSTAT, type), 0,
                       struct fs_quota_stat *addr);

           #include <xfs/xqm.h>      /* See quotactl(2) */

           #define FS_QSTAT_VERSION  1  /* fs_quota_stat.qs_version */

           struct fs_quota_stat {
                int8_t    qs_version;
                uint16_t  qs_flags;
                int8_t    qs_pad;
                struct fs_qfilestat  qs_uquota;
                struct fs_qfilestat  qs_gquota;
                uint32_t  qs_incoredqs;
                int32_t   qs_btimelimit;
                int32_t   qs_itimelimit;
                int32_t   qs_rtbtimelimit;
                uint16_t  qs_bwarnlimit;
                uint16_t  qs_iwarnlimit;
           };

           struct fs_qfilestat {
                uint64_t  qfs_ino;
                uint64_t  qfs_nblks;
                uint32_t  qfs_nextents;
           };

## [](#DESCRIPTION)DESCRIPTION

           Returns XFS filesystem-specific quota information in the
           fs_quota_stat structure pointed by addr.

           This is useful for finding out how much space is used to store
           quota information, and also to get the quota on/off status of a
           given local XFS filesystem.

       struct fs_quota_stat
           .qs_version
                  Version number for future changes.

           .qs_flags
                  XFS_QUOTA_{U,P,G}DQ_{ACCT,ENFD}

           .qs_pad
                  Unused.

           .qs_uquota
                  User quota storage information.

           .qs_gquota
                  Group quota storage information.

           .qs_incoredqs
                  Number of dquots in core.

           .qs_btimelimit
                  Limit for blocks timer.

           .qs_itimelimit
                  Limit for inodes timer.

           .qs_rtbtimelimit
                  Limit for RT blocks timer.

           .qs_bwarnlimit
                  Limit for # of warnings.

           .qs_iwarnlimit
                  Limit for # of warnings.

       struct fs_quota_stat
           .qfs_ino
                  Inode number.

           .qfs_nblks
                  Number of BBs 512-byte-blocks.

           .qfs_nextents
                  Number of extents.

## [](#RETURN_VALUE)RETURN VALUE

           See quotactl(2).

## [](#ERRORS)ERRORS

           See quotactl(2).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux.

## [](#SEE_ALSO)SEE ALSO

           quotactl(2), quotactl_fd(2), Q_XGETQSTATV(2const)

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

    Linux man-pages 6.19            2026-06-05            Q_XGETQSTAT(2const)

------------------------------------------------------------------------

Pages that refer to this page: [quotactl(2)](../man2/quotactl.2.html),  [Q_XGETQSTATV(2const)](../man2/Q_XGETQSTATV.2const.html)

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
