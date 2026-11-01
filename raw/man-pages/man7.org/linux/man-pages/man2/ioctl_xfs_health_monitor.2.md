---
{"title": "ioctl_xfs_health_monitor(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_xfs_health_monitor.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# ioctl_xfs_health_monitor(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [EVENT FORMAT](#EVENT_FORMAT) \| [CONFORMING TO](#CONFORMING_TO) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                   |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IOCTL-XFS-...TH-MONITOR(2) System Calls Manual IOCTL-XFS-...TH-MONITOR(2)

## [](#NAME)NAME

           ioctl_xfs_health_monitor - read filesystem health events from the
           kernel

## [](#SYNOPSIS)SYNOPSIS

           #include <xfs/xfs_fs.h>

           int ioctl(int dest_fd, XFS_IOC_HEALTH_MONITOR, struct
           xfs_health_monitor *arg);

## [](#DESCRIPTION)DESCRIPTION

           This XFS ioctl asks the kernel driver to create a pseudo-file from
           which information about adverse filesystem health events can be
           read.  This new file will be installed into the file descriptor
           table of the calling process as a read-only file, and will have
           the close-on-exec flag set.

           The specific behaviors of this health monitor file are requested
           via a structure of the following form:

               struct xfs_health_monitor {
                    __u64 flags;
                    __u8  format;
                    __u8  pad[23];
               };

           The field pad must be zero.

           The field format controls the format of the event data that can be
           read:

               XFS_HEALTH_MONITOR_FMT_V0
                      Event data will be presented in discrete objects of
                      type struct xfs_health_monitor_event.  See below for
                      more information.

           The field flags control the behavior of the monitor.

               XFS_HEALTH_MONITOR_VERBOSE
                      Return all health events, including affirmations of
                      healthy metadata.

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.
           Otherwise, the return value is a new file descriptor.

## [](#ERRORS)ERRORS

           Error codes can be one of, but are not limited to, the following:

           EEXIST Health monitoring is already active for this filesystem.

           EPERM  The caller does not have permission to open a health
                  monitor.  Calling programs must have administrative
                  capability, run in the initial user namespace, and the fd
                  passed to ioctl must be the root directory of an XFS
                  filesystem.

           EINVAL One or more of the arguments specified is invalid.

           EFAULT The argument could not be copied into the kernel.

           ENOMEM There was not sufficient memory to construct the health
                  monitor.

## [](#EVENT_FORMAT)EVENT FORMAT

           Calling programs retrieve XFS health events by calling read(2) on
           the returned file descriptor.  The read buffer must be large
           enough to hold at least one event object.  Partial objects will
           not be returned; instead, a short read will occur.

           Events will be returned in the following format:

               struct xfs_health_monitor_event {
                    __u32     domain;
                    __u32     type;
                    __u64     time_ns;

                    union {
                         struct xfs_health_monitor_lost lost;
                         struct xfs_health_monitor_fs fs;
                         struct xfs_health_monitor_group group;
                         struct xfs_health_monitor_inode inode;
                         struct xfs_health_monitor_shutdown shutdown;
                         struct xfs_health_monitor_media media;
                         struct xfs_health_monitor_filerange filerange;
                    } e;

                    __u64     pad[2];
               };

           The field time_ns records the timestamp at which the health event
           was generated, in units of nanoseconds since the Unix epoch.

           The field pad will be zero.

           The field domain indicates the scope of the filesystem affected by
           the event:

               XFS_HEALTH_MONITOR_DOMAIN_MOUNT
                      The entire filesystem is affected.

               XFS_HEALTH_MONITOR_DOMAIN_FS
                      Metadata concerning the entire filesystem is affected.
                      Details are available through the fs field.

               XFS_HEALTH_MONITOR_DOMAIN_AG
                      Metadata concerning a specific allocation group is
                      affected.  Details are available through the group
                      field.

               XFS_HEALTH_MONITOR_DOMAIN_RTGROUP
                      Metadata concerning a specific realtime allocation
                      group is affected.  Details are available through the
                      group field.

               XFS_HEALTH_MONITOR_DOMAIN_INODE
                      File metadata is affected.  Details are available
                      through the inode field.

               XFS_HEALTH_MONITOR_DOMAIN_DATADEV
                      The main data volume is affected.  Details are
                      available through the media field.

               XFS_HEALTH_MONITOR_DOMAIN_RTDEV
                      The realtime volume is affected.  Details are available
                      through the media field.

               XFS_HEALTH_MONITOR_DOMAIN_LOGDEV
                      The external log is affected.  Details are available
                      through the media field.

               XFS_HEALTH_MONITOR_DOMAIN_FILERANGE
                      File data is affected.  Details are available through
                      the filerange field.

           The field type indicates what was affected by a health event:

               The following types apply to events from the MOUNT domain.

                   XFS_HEALTH_MONITOR_TYPE_RUNNING
                          This filesystem health monitor is now running.

                   XFS_HEALTH_MONITOR_TYPE_LOST
                          Health events were lost.  Details are available
                          through the lost field.

                   XFS_HEALTH_MONITOR_TYPE_UNMOUNT
                          The filesystem is being unmounted.

                   XFS_HEALTH_MONITOR_TYPE_SHUTDOWN
                          The filesystem has shut down due to problems.
                          Details are available through the shutdown field.

               The following three types apply to events from the FS, AG,
               RTGROUP, and INODE domains.

                   XFS_HEALTH_MONITOR_TYPE_SICK
                          Filesystem metadata has been scanned by online fsck
                          and found to be corrupt.

                   XFS_HEALTH_MONITOR_TYPE_CORRUPT
                          A metadata corruption problem was encountered
                          during a filesystem operation outside of fsck.

                   XFS_HEALTH_MONITOR_TYPE_HEALTHY
                          Filesystem metadata has either been scanned by
                          online fsck and found to be in good condition, or
                          it has been repaired to good condition.

               The following type applies to events from the DATADEV, RTDEV,
               and LOGDEV domains.

                   XFS_HEALTH_MONITOR_TYPE_MEDIA_ERROR
                          A media error has been observed on one of the
                          storage devices that can be attached to an XFS
                          filesystem.

               The following types apply to events from the FILERANGE domain.

                   XFS_HEALTH_MONITOR_TYPE_BUFREAD
                          An attempt to read (or readahead) from a file
                          failed with an I/O error.

                   XFS_HEALTH_MONITOR_TYPE_BUFWRITE
                          An attempt to write dirty data to storage failed
                          with an I/O error.

                   XFS_HEALTH_MONITOR_TYPE_DIOREAD
                          A direct read of file data from storage failed with
                          an I/O error.

                   XFS_HEALTH_MONITOR_TYPE_DIOWRITE
                          A direct write of file data to storage failed with
                          an I/O error.

                   XFS_HEALTH_MONITOR_TYPE_DATALOST
                          A latent media error was discovered on the storage
                          backing part of this file.

           The union e contains further details about the health event:

               The kernel will use no more than 32KiB of memory per
               monitoring file to queue health events.  If this limit is
               exceeded, an event will be generated to describe how many
               events were lost:

                   struct xfs_health_monitor_lost {
                        __u64     count;
                   };

               The count field records the number of events lost.

               If whole-filesystem metadata experiences a health event, the
               exact type of that metadata is recorded as follows:

                   struct xfs_health_monitor_fs {
                        __u32     mask;
                   };

               The mask field will contain XFS_FSOP_GEOM_SICK_* flags that
               are documented in the ioctl_xfs_fsgeometry(2) manual page.

               If an allocation group (realtime or data) experiences a health
               event, the exact type and location of the metadata is recorded
               as follows:

                   struct xfs_health_monitor_group {
                        __u32     mask;
                        __u32     gno;
                   };

               The mask field will contain XFS_AG_SICK_* flags that are
               documented in the ioctl_xfs_ag_geometry(2) manual page, or the
               XFS_RTGROUP_SICK_* flags that are documented by the
               ioctl_xfs_rtgroup_geometry(2) manual page.

               The gno field will contain the group number.

               If a file experiences a health event, the exact type and
               handle to the file is recorded as follows:

                   struct xfs_health_monitor_inode {
                        __u32     mask;
                        __u32     gen;
                        __u64     ino;
                   };

               The mask field will contain XFS_BS_SICK_* flags that are
               documented by the ioctl_xfs_bulkstat(2) manual page.

               The ino and gen fields describe a handle to the affected file.

               If the filesystem shuts down abnormally, the exact reasons are
               recorded as follows:

                   struct xfs_health_monitor_shutdown {
                        __u32     reasons;
                   };

               The reasons field is a combination of the following values:

                   XFS_HEALTH_SHUTDOWN_META_IO_ERROR
                          Metadata I/O errors were encountered.

                   XFS_HEALTH_SHUTDOWN_LOG_IO_ERROR
                          Log I/O errors were encountered.

                   XFS_HEALTH_SHUTDOWN_FORCE_UMOUNT
                          The filesystem was forcibly shut down by an
                          administrator.

                   XFS_HEALTH_SHUTDOWN_CORRUPT_INCORE
                          In-memory metadata are corrupt.

                   XFS_HEALTH_SHUTDOWN_CORRUPT_ONDISK
                          On-disk metadata are corrupt.

                   XFS_HEALTH_SHUTDOWN_DEVICE_REMOVED
                          Storage devices were removed.

               If a media error is discovered on the storage device, the
               exact location is recorded as follows:

                   struct xfs_health_monitor_media {
                        __u64     daddr;
                        __u64     bbcount;
                   };

               The daddr and bbcount fields describe the range of the storage
               that were lost.  Both are provided in units of 512-byte
               blocks.

               If a problem is discovered with regular file data, the handle
               of the file and the exact range of the file are recorded as
               follows:

                   struct xfs_health_monitor_filerange {
                        __u64     pos;
                        __u64     len;
                        __u64     ino;
                        __u32     gen;
                        __u32     error;
                   };

               The ino and gen fields describe a handle to the affected file.
               The pos and len fields describe the range of the file data
               that are affected.  Both are provided in units of bytes.

               The error field describes the error that occurred.  See the
               errno(3) manual page for more information.

## [](#CONFORMING_TO)CONFORMING TO

           This API is specific to XFS filesystem on the Linux kernel.

## [](#SEE_ALSO)SEE ALSO

           ioctl_xfs_health_fd_on_monitored_fs(2)

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

    XFS                             2026-01-04     IOCTL-XFS-...TH-MONITOR(2)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_xfs_health_fd_on_monitored_fs(2)](../man2/ioctl_xfs_health_fd_on_monitored_fs.2.html),  [ioctl_xfs_verify_media(2)](../man2/ioctl_xfs_verify_media.2.html)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/ioctl_xfs_health_monitor.2.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
