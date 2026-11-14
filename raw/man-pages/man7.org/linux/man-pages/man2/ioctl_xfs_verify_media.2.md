---
{"title": "ioctl_xfs_verify_media(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_xfs_verify_media.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ioctl_xfs_verify_media(2) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [I/O ERRORS](#I/O_ERRORS) \| [CONFORMING TO](#CONFORMING_TO) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                               |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IOCTL-XFS-VERIFY-MEDIA(2)  System Calls Manual  IOCTL-XFS-VERIFY-MEDIA(2)

## [](#NAME)NAME

           ioctl_xfs_verify_media - verify the media of the devices backing
           XFS

## [](#SYNOPSIS)SYNOPSIS

           #include <xfs/xfs_fs.h>

           int ioctl(int fd, XFS_IOC_VERIFY_MEDIA, struct xfs_verify_media
           *arg);

## [](#DESCRIPTION)DESCRIPTION

           Verify the media of a storage device backing an XFS filesystem.
           If errors are found, report the error to the kernel so that it can
           generate health events for the health monitoring system and
           fsnotify.  The verification request is conveyed in a structure of
           the following form:

               struct xfs_verify_media {
                    __u32     me_dev;
                    __u32     me_flags;
                    __u64     me_start_daddr;
                    __u64     me_end_daddr;
                    __u32     me_ioerror;
                    __u32     me_max_io_size;
                    __u32     me_rest_us;
                    __u32     me_pad;
               };

           The field me_pad must be zero.

           The field me_ioerror will be set if the ioctl returns success.

           The fields me_start_daddr and me_end_daddr are the range of the
           storage device to verify.  Both values must be in units of
           512-byte blocks.  The me_start_daddr field is inclusive, and the
           me_end_daddr field is exclusive.  If me_end_daddr is larger than
           the size of the device, the kernel will set it to the size of the
           device.

           If the system call returns success and any part of the storage
           device range was successfully verified, the me_start_daddr field
           will be updated to reflect the successful verification.  If after
           this update the me_start_daddr is equal to me_end_daddr, then the
           entire range was verified successfully.

           If not, then a media error was encountered and the caller should
           generate a series of secondary calls to this ioctl with smaller
           ranges to discover the exact location and type of media error.
           The type of media error will be written to the me_ioerror field.

           The me_max_io_size field, if nonzero, is an upper bound on the I/O
           operations that the kernel will issue to the block device.

           The me_rest_us is the time duration, in microseconds, for which
           the kernel will wait between issuing I/O operations.

           The field me_dev must be one of the following values:

               XFS_DEV_DATA
                      Verify the data device.

               XFS_DEV_LOG
                      Verify the external log device.

               XFS_DEV_RT
                      Verify the realtime device.

           The field me_flags is a bitmask of one of the following values:

               XFS_VERIFY_MEDIA_REPORT
                      Report all media errors to fsnotify.

           The me_max_io_size field, if nonzero, will be used as advice for
           the maximum size of the IO to send to the device.

           The me_rest_us field will cause the kernel to pause for this many
           microseconds between IO requests.

## [](#RETURN_VALUE)RETURN VALUE

           On runtime error, -1 is returned, and errno is set to indicate the
           error.  If 0 is returned, then start_daddr or ioerror will be
           updated.

## [](#ERRORS)ERRORS

           Error codes can be one of, but are not limited to, the following:

           EPERM  The calling process does not have sufficient privilege.

           EINVAL One or more of the arguments specified is invalid.

           EFAULT The arg structure could not be copied into the kernel.

           ENODEV The device is not present.

           ENOMEM There was not enough memory to perform the verification.

## [](#I/O_ERRORS)I/O ERRORS

           The ioerror field could be set to one of the following:

           0      The verification I/O succeeded.

           EOPNOTSUPP

           ETIMEDOUT
                  The kernel timed out the verification I/O command.

           ENOLINK
                  The transportation link to the storage device was down
                  temporarily.

           EREMOTEIO
                  The storage target controller suffered a critical error.

           ENODATA
                  The storage target media suffered a critical error.

           EILSEQ Storage protection metadata did not validate successfully.

           ENOMEM There was not enough memory to allocate an I/O request.

           ENODEV The storage device is offline.

           ETIME  The storage device timed out the I/O command.

           EINVAL The I/O request was rejected by the device for being
                  invalid.

           EIO    An I/O error occurred but no specific details are
                  available.

           This list is not exhaustive and may grow in the future.

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

    XFS                             2026-01-09      IOCTL-XFS-VERIFY-MEDIA(2)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/ioctl_xfs_verify_media.2.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
