---
{"title": "ioctl_xfs_scrubv_metadata(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_xfs_scrubv_metadata.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# ioctl_xfs_scrubv_metadata(2) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [CONFORMING TO](#CONFORMING_TO) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IOCTL-XFS...V-METADATA(2)  System Calls Manual  IOCTL-XFS...V-METADATA(2)

## [](#NAME)NAME

           ioctl_xfs_scrubv_metadata - check a lot of XFS filesystem metadata

## [](#SYNOPSIS)SYNOPSIS

           #include <xfs/xfs_fs.h>

           int ioctl(int dest_fd, XFS_IOC_SCRUBV_METADATA, struct
           xfs_scrub_vec_head *arg);

## [](#DESCRIPTION)DESCRIPTION

           This XFS ioctl asks the kernel driver to examine several pieces of
           filesystem metadata for errors or suboptimal metadata.  Multiple
           scrub types can be invoked to target a single filesystem object.
           See ioctl_xfs_scrub_metadata(2) for a discussion of metadata
           validation, and documentation of the various XFS_SCRUB_TYPE and
           XFS_SCRUB_FLAGS values referenced below.

           The types and location of the metadata to scrub are conveyed as a
           vector with a header of the following form:

               struct xfs_scrub_vec_head {
                    __u64 svh_ino;
                    __u32 svh_gen;
                    __u32 svh_agno;
                    __u32 svh_flags;
                    __u16 svh_rest_us;
                    __u16 svh_nr;
                    __u64 svh_reserved;
                    __u64 svh_vectors;
               };

           The field svh_ino, svh_gen, and svh_agno correspond to the sm_ino,
           sm_gen, and sm_agno fields of the regular scrub ioctl.  Exactly
           one filesystem object can be specified in a single call.  The
           kernel will proceed with each vector in svh_vectors until progress
           is no longer possible.

           The field svh_rest_us specifies an amount of time to pause between
           each scrub invocation to give the system a chance to process other
           requests.

           The field svh_nr specifies the number of vectors in the
           svh_vectors array.

           The field svh_vectors is a pointer to an array of struct
           xfs_scrub_vec structures.

           The field svh_reserved must be zero.

           Each vector has the following form:

               struct xfs_scrub_vec {
                    __u32 sv_type;
                    __u32 sv_flags;
                    __s32 sv_ret;
                    __u32 sv_reserved;
               };

           The fields sv_type and sv_flags indicate the type of metadata to
           check and the behavioral changes that userspace will permit of the
           kernel.  The sv_flags field will be updated upon completion of the
           scrub call.  See the documentation of XFS_SCRUB_TYPE_* and
           XFS_SCRUB_[IO]FLAG_* values in ioctl_xfs_scrub_metadata(2) for a
           detailed description of their purpose.

           If a vector's sv_type field is set to the value
           XFS_SCRUB_TYPE_BARRIER, the kernel will stop processing vectors
           and return to userspace if a scrubber flags corruption by setting
           one of the XFS_SCRUB_OFLAG_* values in sv_flags or returns an
           operation error in sv_ret.  Otherwise, the kernel returns only
           after processing all vectors.

           The sv_ret field is set to the return value of the scrub function.
           See the RETURN VALUE section of the ioctl_xfs_scrub_metadata(2)
           manual page for more information.

           The sv_reserved field must be zero.

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           Error codes can be one of, but are not limited to, the following:

           EINVAL One or more of the arguments specified is invalid.

           EINTR  The operation was interrupted.

           ENOMEM There was not sufficient memory to perform the scrub or
                  repair operation.

           EFAULT A memory fault was encountered while reading or writing the
                  vector.

## [](#CONFORMING_TO)CONFORMING TO

           This API is specific to XFS filesystem on the Linux kernel.

## [](#NOTES)NOTES

           These operations may block other filesystem operations for a long
           time.  A calling process can stop the operation by being sent a
           fatal signal, but non-fatal signals are blocked.

## [](#SEE_ALSO)SEE ALSO

           ioctl(2) ioctl_xfs_scrub_metadata(2) xfs_scrub(8) xfs_repair(8)

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

    XFS                             2024-05-21      IOCTL-XFS...V-METADATA(2)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/ioctl_xfs_scrubv_metadata.2.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
