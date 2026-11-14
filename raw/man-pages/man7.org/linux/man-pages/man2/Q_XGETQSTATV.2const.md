---
{"title": "Q_XGETQSTATV(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/Q_XGETQSTATV.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# Q_XGETQSTATV(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    Q_XGETQSTATV(2const)                                 Q_XGETQSTATV(2const)

## [](#NAME)NAME

           Q_XGETQSTATV - get XFS-specific quota information

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <xfs/xqm.h>      /* See quotactl(2) */
           #include <sys/quota.h>

           int quotactl(QCMD(Q_XGETQSTATV, type), const char *_Nullable special, 0,
                        caddr_t addr);

           #include <xfs/xqm.h>      /* See quotactl_fd(2) */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_quotactl_fd, int fd, QCMD(Q_XGETQSTATV, type), 0,
                       struct fs_quota_statv *addr);

           #include <xfs/xqm.h>      /* See quotactl_fd(2) */

           #define FS_QSTATV_VERSION1  1

           struct fs_quota_statv {
                int8_t    qs_version;
                uint8_t   qs_pad1;
                uint16_t  qs_flags;
                uint32_t  qs_incoredqs;
                struct fs_qfilestatv  qs_uquota;
                struct fs_qfilestatv  qs_gquota;
                struct fs_qfilestatv  qs_pquota;
                int32_t   qs_btimelimit;
                int32_t   qs_itimelimit;
                int32_t   qs_rtbtimelimit;
                uint16_t  qs_bwarnlimit;
                uint16_t  qs_iwarnlimit;
                uint64_t  qs_pad2[8];
           };

           struct fs_qfilestatv {
                uint64_t  qfs_ino;
                uint64_t  qfs_nblks;
                uint32_t  qfs_nextents;
                uint32_t  qfs_pad;
           };

## [](#DESCRIPTION)DESCRIPTION

           Returns XFS filesystem-specific quota information in the
           fs_quota_statv pointed to by addr.

           This version of the operation (compared to Q_XGETQSTAT(2const))
           uses a structure with proper versioning support, along with
           appropriate layout (all fields are naturally aligned) and padding
           to avoiding special compat handling; it also provides the ability
           to get statistics regarding the project quota file.

       struct fs_quota_statv
           .qs_version
                  This field should be filled with the version of the
                  structure supported by the callee (for now, only
                  FS_QSTAT_VERSION1 is supported).  The kernel will fill the
                  structure in accordance with the version provided.

           .qs_pad1
                  Pad for 16-bit alignment.

           .qs_flags
                  XFS_QUOTA_* flags.

           .qs_incoredqs
                  Number of dquots incore.

           .qs_uquota
                  User quota information.

           .qs_gquota
                  Group quota information.

           .qs_pquota
                  Project quota information.

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

           .qs_pad2
                  For future proofing.

       struct fs_qfilestatv
           .qfs_ino
                  Inode number.

           .qfs_nblks
                  Number of BBs 512-byte-blocks.

           .qfs_nextents
                  Number of extents.

           .qfs_pad
                  Pad for 8-byte alignment.

## [](#RETURN_VALUE)RETURN VALUE

           See quotactl(2).

## [](#ERRORS)ERRORS

           See quotactl(2).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux.

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

    Linux man-pages 6.19            2026-06-05           Q_XGETQSTATV(2const)

------------------------------------------------------------------------

Pages that refer to this page: [quotactl(2)](../man2/quotactl.2.html),  [Q_XGETQSTAT(2const)](../man2/Q_XGETQSTAT.2const.html)

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
