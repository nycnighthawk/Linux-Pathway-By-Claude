---
{"title": "ioctl_xfs_health_fd_on_monitored_fs(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_xfs_health_fd_on_monitored_fs.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# ioctl_xfs_health_fd_on_monitored_fs(2) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [CONFORMING TO](#CONFORMING_TO) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IOCTL-XFS...NITORED-FS(2)  System Calls Manual  IOCTL-XFS...NITORED-FS(2)

## [](#NAME)NAME

           ioctl_xfs_health_fd_on_monitored_fs - check if the given fd
           belongs to the same fs being monitored

## [](#SYNOPSIS)SYNOPSIS

           #include <xfs/xfs_fs.h>

           int ioctl(int healthmon_fd, XFS_IOC_HEALTH_FD_ON_MONITORED_FS,
           struct xfs_health_file_on_monitored_fs *arg);

## [](#DESCRIPTION)DESCRIPTION

           This XFS healthmon fd ioctl asks the kernel driver if the file
           descriptor passed in via arg points to a file on the same
           filesystem that is being monitored by healthmon_fd.  The file
           descriptor is conveyed in a structure of the following form:

               struct xfs_health_file_on_monitored_fs {
                    __s32 fd;
                    __u32 flags;
               };

           The field flags must be zero.

           The field fd is a descriptor of an open file.

           The argument healthmon_fd must be a file opened via the
           XFS_IOC_HEALTH_MONITOR ioctl.

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.
           If the file descriptor points to a file on the same filesystem
           that is being monitored, 0 is returned.

## [](#ERRORS)ERRORS

           Error codes can be one of, but are not limited to, the following:

           ESTALE The open file is not on the same filesystem that is being
                  monitored.

           EINVAL One or more of the arguments specified is invalid.

           EBADF  arg.fd does not refer to an open file.

           EFAULT The arg structure could not be copied into the kernel.

           ENOTTY healthmon_fd is not a XFS health monitoring file.

## [](#CONFORMING_TO)CONFORMING TO

           This API is specific to XFS filesystem on the Linux kernel.

## [](#SEE_ALSO)SEE ALSO

           ioctl_xfs_health_monitor(2)

## [](#COLOPHON)COLOPHON

           This page is part of the xfsprogs (utilities for XFS filesystems)
           project.  Information about the project can be found at 
           ⟨http://xfs.org/⟩.  If you have a bug report for this manual page,
           send it to linux-xfs@vger.kernel.org.  This page was obtained from
           the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/fs/xfs/xfsprogs-dev.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-17.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    XFS                             2026-01-04      IOCTL-XFS...NITORED-FS(2)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_xfs_health_monitor(2)](../man2/ioctl_xfs_health_monitor.2.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/ioctl_xfs_health_fd_on_monitored_fs.2.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
