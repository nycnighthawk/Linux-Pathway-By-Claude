---
{"title": "quotactl(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/quotactl_fd.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# quotactl(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [NOTES](#NOTES) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    quotactl(2)                System Calls Manual                quotactl(2)

## [](#NAME)NAME

           quotactl, quotactl_fd - manipulate disk quotas

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <xfs/xqm.h> /* Definition of Q_X* and XFS_QUOTA_* constants
                                   (or <linux/dqblk_xfs.h>; see NOTES) */
           #include <sys/quota.h>

           int quotactl(int op, const char *_Nullable special, int id,
                        caddr_t addr);

           #include <xfs/xqm.h> /* Definition of Q_X* and XFS_QUOTA_* constants
                                   (or <linux/dqblk_xfs.h>; see NOTES) */
           #include <sys/syscall.h>    /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_quotactl_fd, int fd, int op, int id, caddr_t addr);

## [](#DESCRIPTION)DESCRIPTION

           The quota system can be used to set per-user, per-group, and per-
           project limits on the amount of disk space used on a filesystem.
           For each user and/or group, a soft limit and a hard limit can be
           set for each filesystem.  The hard limit can't be exceeded.  The
           soft limit can be exceeded, but warnings will ensue.  Moreover,
           the user can't exceed the soft limit for more than grace period
           duration (one week by default) at a time; after this, the soft
           limit counts as a hard limit.

           The quotactl() and quotactl_fd() calls manipulate disk quotas.
           The difference between these functions is the way the filesystem
           being manipulated is specified, see description of the arguments
           below.  See NOTES for why one variant might be preferred over the
           other.

           The op argument indicates an operation to be applied to the user
           or group ID specified in id.  To initialize the op argument, use
           the QCMD(subop, type) macro.  The type value is either USRQUOTA,
           for user quotas, GRPQUOTA, for group quotas, or (since Linux 4.1)
           PRJQUOTA, for project quotas.  The subop value is described below.

           For quotactl(), the special argument is a pointer to a null-
           terminated string containing the pathname of the (mounted) block
           special device for the filesystem being manipulated.

           For quotactl_fd(), the fd argument is a file descriptor (which may
           be opened with the O_PATH flag) referring to a file or directory
           on the filesystem being manipulated.

           The addr argument is the address of an optional, operation-
           specific, data structure that is copied in or out of the system.
           The interpretation of addr is given with each operation below.

           The subop value is one of the following operations:

           Q_QUOTAON(2const)
           Q_QUOTAOFF(2const)
           Q_GETQUOTA(2const)
           Q_GETNEXTQUOTA(2const)
           Q_SETQUOTA(2const)
           Q_GETINFO(2const)
           Q_SETINFO(2const)
           Q_GETFMT(2const)
           Q_SYNC(2const)
           Q_GETSTATS(2const)

           For XFS filesystems making use of the XFS Quota Manager (XQM), the
           above operations are bypassed and the following operations are
           used:

           Q_XQUOTAON(2const)
           Q_XQUOTAOFF(2const)
           Q_XGETQUOTA(2const)
           Q_XGETNEXTQUOTA(2const)
           Q_XSETQLIM(2const)
           Q_XGETQSTAT(2const)
           Q_XGETQSTATV(2const)
           Q_XQUOTARM(2const)
           Q_XQUOTASYNC(2const)

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned; on error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT addr or special is invalid.

           EINVAL op or type is invalid.

           ENOENT The file specified by special or addr does not exist.

           ENOSYS The kernel has not been compiled with the CONFIG_QUOTA
                  option.

           ENOTBLK
                  special is not a block device.

           EPERM  The caller lacked the required privilege (CAP_SYS_ADMIN)
                  for the specified operation.

           ESRCH  No disk quota is found for the indicated user.  Quotas have
                  not been turned on for this filesystem.

## [](#NOTES)NOTES

       Alternative XFS header
           Instead of <xfs/xqm.h> one can use <linux/dqblk_xfs.h>, taking
           into account that there are several naming discrepancies:

           •  Quota enabling flags (of format XFS_QUOTA_[UGP]DQ_{ACCT,ENFD})
              are defined without a leading "X", as
              FS_QUOTA_[UGP]DQ_{ACCT,ENFD}.

           •  The same is true for XFS_{USER,GROUP,PROJ}_QUOTA quota type
              flags, which are defined as FS_{USER,GROUP,PROJ}_QUOTA.

           •  The dqblk_xfs.h header file defines its own XQM_USRQUOTA,
              XQM_GRPQUOTA, and XQM_PRJQUOTA constants for the available
              quota types, but their values are the same as for constants
              without the XQM_ prefix.

       quotactl() versus quotactl_fd()
           The original quotactl() variant of this system call requires
           specifying the block device containing the filesystem to operate
           on.  This makes it impossible to use in cases where the filesystem
           has no backing block device (e.g., tmpfs).  Even when the block
           device does exist, it might be difficult to locate (requires
           scanning /proc/self/mounts and even some filesystem-specific
           parsing in the case of, for example, bcachefs).  quotactl_fd()
           instead works on the mount point, which avoids this limitation and
           is simpler to use (since the filesystem to manipulate is typically
           specified by its mount point anyway).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           quotactl_fd()
                  Linux 5.14.

## [](#SEE_ALSO)SEE ALSO

           quota(1), getrlimit(2), quotacheck(8), quotaon(8)

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

    Linux man-pages 6.19            2026-06-05                    quotactl(2)

------------------------------------------------------------------------

Pages that refer to this page: [quota(1)](../man1/quota.1.html),  [quotasync(1)](../man1/quotasync.1.html),  [getrlimit(2)](../man2/getrlimit.2.html),  [Q_GETFMT(2const)](../man2/Q_GETFMT.2const.html),  [Q_GETINFO(2const)](../man2/Q_GETINFO.2const.html),  [Q_GETNEXTQUOTA(2const)](../man2/Q_GETNEXTQUOTA.2const.html),  [Q_GETQUOTA(2const)](../man2/Q_GETQUOTA.2const.html),  [Q_GETSTATS(2const)](../man2/Q_GETSTATS.2const.html),  [Q_QUOTAOFF(2const)](../man2/Q_QUOTAOFF.2const.html),  [Q_QUOTAON(2const)](../man2/Q_QUOTAON.2const.html),  [Q_SETINFO(2const)](../man2/Q_SETINFO.2const.html),  [Q_SETQUOTA(2const)](../man2/Q_SETQUOTA.2const.html),  [Q_SYNC(2const)](../man2/Q_SYNC.2const.html),  [Q_XGETNEXTQUOTA(2const)](../man2/Q_XGETNEXTQUOTA.2const.html),  [Q_XGETQSTAT(2const)](../man2/Q_XGETQSTAT.2const.html),  [Q_XGETQSTATV(2const)](../man2/Q_XGETQSTATV.2const.html),  [Q_XGETQUOTA(2const)](../man2/Q_XGETQUOTA.2const.html),  [Q_XQUOTAOFF(2const)](../man2/Q_XQUOTAOFF.2const.html),  [Q_XQUOTAON(2const)](../man2/Q_XQUOTAON.2const.html),  [Q_XQUOTARM(2const)](../man2/Q_XQUOTARM.2const.html),  [Q_XQUOTASYNC(2const)](../man2/Q_XQUOTASYNC.2const.html),  [Q_XSETQLIM(2const)](../man2/Q_XSETQLIM.2const.html),  [syscalls(2)](../man2/syscalls.2.html),  [rquota(3)](../man3/rquota.3.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [capabilities(7)](../man7/capabilities.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html),  [edquota(8)](../man8/edquota.8.html),  [pam_setquota(8)](../man8/pam_setquota.8.html),  [quotacheck(8)](../man8/quotacheck.8.html),  [quotaon(8)](../man8/quotaon.8.html),  [repquota(8)](../man8/repquota.8.html),  [setquota(8)](../man8/setquota.8.html)

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
