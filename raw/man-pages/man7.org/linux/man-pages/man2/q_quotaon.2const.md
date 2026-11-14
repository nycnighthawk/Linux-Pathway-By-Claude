---
{"title": "Q_QUOTAON(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/q_quotaon.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# Q_QUOTAON(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    Q_QUOTAON(2const)                                       Q_QUOTAON(2const)

## [](#NAME)NAME

           Q_QUOTAON - turn on quotas for a filesystem

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/quota.h>

           int quotactl(QCMD(Q_QUOTAON, type), const char *_Nullable special,
                        int fmt, caddr_t quota_path);

           #include <sys/quota.h>    /* Definition of Q_* constants */
           #include <sys/syscall.h>  /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_quotactl_fd, int fd, QCMD(Q_QUOTAON, type));

## [](#DESCRIPTION)DESCRIPTION

           Turn on quotas for a filesystem.

           The fmt argument is the identification number of the quota format
           to be used.  Currently, there are three supported quota formats:

           QFMT_VFS_OLD
                  The original quota format.

           QFMT_VFS_V0
                  The standard VFS v0 quota format, which can handle 32-bit
                  UIDs and GIDs and quota limits up to 2^42 bytes and 2^32
                  inodes.

           QFMT_VFS_V1
                  A quota format that can handle 32-bit UIDs and GIDs and
                  quota limits of 2^63 - 1 bytes and 2^63 - 1 inodes.

           The quota_path argument points to the pathname of a file
           containing the quotas for the filesystem.  The quota file must
           exist; it is normally created with the quotacheck(8) program

           Quota information can be also stored in hidden system inodes for
           ext4, XFS, and other filesystems if the filesystem is configured
           so.  In this case, there are no visible quota files and there is
           no need to use quotacheck(8).  Quota information is always kept
           consistent by the filesystem and the Q_QUOTAON operation serves
           only to enable enforcement of quota limits.  The presence of
           hidden system inodes with quota information is indicated by the
           DQF_SYS_FILE flag in the dqi_flags field returned by the
           Q_GETINFO(2const) operation.

           The quotactl_fd() variant of this system call doesn't have the
           quota_path and fmt arguments, so the Q_QUOTAON operation of
           quotactl_fd() is only suitable for work with hidden system inodes.

           This operation requires privilege (CAP_SYS_ADMIN).

## [](#RETURN_VALUE)RETURN VALUE

           See quotactl(2).

## [](#ERRORS)ERRORS

           See quotactl(2).

           EACCES The quota file pointed to by quota_path exists, but is not
                  a regular file or is not on the filesystem pointed to by
                  special.

           EBUSY  Another Q_QUOTAON had already been performed.

           EINVAL The specified quota file is corrupted.

           ESRCH  The specified quota format was not found.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux.

## [](#SEE_ALSO)SEE ALSO

           quotactl(2), quotactl_fd(2), Q_QUOTAOFF(2const), quotacheck(8)

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

    Linux man-pages 6.19            2026-06-05              Q_QUOTAON(2const)

------------------------------------------------------------------------

Pages that refer to this page: [Q_GETFMT(2const)](../man2/Q_GETFMT.2const.html),  [Q_QUOTAOFF(2const)](../man2/Q_QUOTAOFF.2const.html),  [quotactl(2)](../man2/quotactl.2.html)

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
