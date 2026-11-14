---
{"title": "fs_disk_quota(2type) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/fs_disk_quota.2type.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fs_disk_quota(2type) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    fs_disk_quota(2type)                                 fs_disk_quota(2type)

## [](#NAME)NAME

           fs_disk_quota - filesystem disk quota

## [](#LIBRARY)LIBRARY

           Standard C library (libc)

## [](#SYNOPSIS)SYNOPSIS

           #include <xfs/xqm.h>

           #define FS_DQUOT_VERSION  1  // fs_disk_quota.d_version

           #define XFS_USER_QUOTA    (1<<0)  // User quota type
           #define XFS_PROJ_QUOTA    (1<<1)  // Project quota type
           #define XFS_GROUP_QUOTA   (1<<2)  // Group quota type

           struct fs_disk_quota {
                int8_t    d_version;
                int8_t    d_flags;
                uint16_t  d_fieldmask;
                uint32_t  d_id;
                uint64_t  d_blk_hardlimit;
                uint64_t  d_blk_softlimit;
                uint64_t  d_ino_hardlimit;
                uint64_t  d_ino_softlimit;
                uint64_t  d_bcount;
                uint64_t  d_icount;
                int32_t   d_itimer;
                int32_t   d_btimer;
                uint16_t  d_iwarns;
                uint16_t  d_bwarns;
                int32_t   d_padding2;
                uint64_t  d_rtb_hardlimit;
                uint64_t  d_rtb_softlimit;
                uint64_t  d_rtbcount;
                int32_t   d_rtbtimer;
                uint16_t  d_rtbwarns;
                int16_t   d_padding3;
                char      d_padding4[8];
           };

## [](#DESCRIPTION)DESCRIPTION

           All the blk units are in BBs (Basic Blocks) of 512 bytes.

           .d_version
                  Version of this structure.

           .d_flags
                  XFS_{USER,PROJ,GROUP}_QUOTA

           .d_fieldmask
                  Field specifier.

           .d_id  User, project, or group ID.

           .d_blk_hardlimit
                  Absolute limit on disk blocks.

           .d_blk_softlimit
                  Preferred limit on disk blocks.

           .d_ino_hardlimit
                  Maximum # allocated inodes.

           .d_ino_softlimit
                  Preferred inode limit.

           .d_bcount
                  # disk blocks owned by the user.

           .d_icount
                  # inodes owned by the user.

           .d_itimer
                  Zero if within inode limits; if not, we refuse service.

           .d_btimer
                  Similar to above; for disk blocks.

           .d_iwarns
                  # warnings issued with respect to # of inodes.

           .d_bwarns
                  # warnings issued with respect to disk blocks.

           .d_padding2
                  Padding; reserved for future use.

           .d_rtb_hardlimit
                  Absolute limit on realtime (RT) disk blocks.

           .d_rtb_softlimit
                  Preferred limit on RT disk blocks.

           .d_rtbcount
                  # realtime blocks owned.

           .d_rtbtimer
                  Similar to above; for RT disk blocks.

           .d_rtbwarns
                  # warnings issued with respect to RT disk blocks.

           .d_padding3
                  Padding; reserved for future use.

           .d_padding4[8]
                  Yet more padding.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux.

## [](#SEE_ALSO)SEE ALSO

           Q_XGETQUOTA(2const), Q_XGETNEXTQUOTA(2const), Q_XSETQLIM(2const)

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

    Linux man-pages 6.19            2026-06-05           fs_disk_quota(2type)

------------------------------------------------------------------------

Pages that refer to this page: [Q_XGETNEXTQUOTA(2const)](../man2/Q_XGETNEXTQUOTA.2const.html),  [Q_XGETQUOTA(2const)](../man2/Q_XGETQUOTA.2const.html),  [Q_XQUOTARM(2const)](../man2/Q_XQUOTARM.2const.html),  [Q_XSETQLIM(2const)](../man2/Q_XSETQLIM.2const.html)

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
