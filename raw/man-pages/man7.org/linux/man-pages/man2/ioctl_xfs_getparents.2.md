---
{"title": "ioctl_xfs_getparents(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_xfs_getparents.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# ioctl_xfs_getparents(2) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SAMPLE PROGRAM](#SAMPLE_PROGRAM) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [CONFORMING TO](#CONFORMING_TO) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                       |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    IOCTL-XFS-GETPARENTS(2)    System Calls Manual    IOCTL-XFS-GETPARENTS(2)

## [](#NAME)NAME

           ioctl_xfs_getparents - query XFS directory parent information

## [](#SYNOPSIS)SYNOPSIS

           #include <xfs/xfs_fs.h>

           int ioctl(int fd, XFS_IOC_GETPARENTS, struct xfs_getparents *arg);

           int ioctl(int fd, XFS_IOC_GETPARENTS_BY_HANDLE, struct
           xfs_getparents_by_handle *arg);

## [](#DESCRIPTION)DESCRIPTION

           This command is used to retrieve the directory parent pointers of
           either the currently opened file or a file handle.  Parent
           pointers point upwards in the directory tree from a child file
           towards a parent directories.  Each entry in a parent directory
           must have a corresponding parent pointer in the child.

           Calling programs should allocate a large memory buffer and
           initialize a header of the following form:

               struct xfs_getparents {
                    struct xfs_attrlist_cursor  gp_cursor;
                    __u16                       gp_iflags;
                    __u16                       gp_oflags;
                    __u32                       gp_bufsize;
                    __u64                       __pad;
                    __u64                       gp_buffer;
               };

               struct xfs_getparents_by_handle {
                    struct xfs_handle           gph_handle;
                    struct xfs_getparents       gph_request;
               };

           The field gp_cursor tracks the progress of iterating through the
           parent pointers.  Calling programs must initialize this to zero
           before the first system call and must not touch it after that.

           The field gp_iflags control the behavior of the query operation
           and provide more information about the outcome of the operation.
           There are no input flags currently defined; this field must be
           zero.

           The field gp_oflags contains information about the query itself.
           Possibly output flags are:

               XFS_GETPARENTS_OFLAG_ROOT
                      The file queried was the root directory.

               XFS_GETPARENTS_OFLAG_DONE
                      There are no more parent pointers to query.

           The field __pad must be zero.

           The field gp_bufsize should be set to the size of the buffer, in
           bytes.

           The field gp_buffer should point to an output buffer for the
           parent pointer records.

           Parent pointer records are returned in the following form:

               struct xfs_getparents_rec {
                    struct xfs_handle           gpr_parent;
                    __u16                       gpr_reclen;
                    char                        gpr_name[];
               };

           The field gpr_parent is a file handle that can be used to open the
           parent directory.

           The field gpr_reclen will be set to the number of bytes used by
           this parent record.

           The array gpr_name will be set to a NULL-terminated byte sequence
           representing the filename stored in the parent pointer.  If the
           name is a zero-length string, the file queried has no parents.

## [](#SAMPLE_PROGRAM)SAMPLE PROGRAM

           Calling programs should allocate a large memory buffer, initialize
           the head structure to zeroes, set gp_bufsize to the size of the
           buffer, and call the ioctl.  The XFS_GETPARENTS_OFLAG_DONE flag
           will be set in gp_flags when there are no more parent pointers to
           be read.  The below code is an example of XFS_IOC_GETPARENTS
           usage:

           #include <stdio.h>
           #include <string.h>
           #include <errno.h>
           #include <xfs/linux.h>
           #include <xfs/xfs.h>
           #include <xfs/xfs_types.h>
           #include <xfs/xfs_fs.h>

           int main() {
                struct xfs_getparents gp = { };
                struct xfs_getparents_rec *gpr;
                int error, fd;

                gp.gp_buffer = (uintptr_t)malloc(65536);
                if (!gp.gp_buffer) {
                     perror("malloc");
                     return 1;
                }
                gp->gp_bufsize = 65536;

                fd = open("/mnt/test/foo.txt", O_RDONLY | O_CREAT);
                if (fd  == -1)
                     return errno;

                do {
                     error = ioctl(fd, XFS_IOC_GETPARENTS, gp);
                     if (error)
                          return error;

                     for (gpr = xfs_getparents_first_rec(&gp);
                          gpr != NULL;
                          gpr = xfs_getparents_next_rec(&gp, gpr)) {
                          if (gpr->gpr_name[0] == 0)
                               break;

                          printf("inode       = %llu\n",
                                    gpr->gpr_parent.ha_fid.fid_ino);
                          printf("generation  = %u\n",
                                    gpr->gpr_parent.ha_fid.fid_gen);
                          printf("name        = \"%s\"\n\n",
                                    gpr->gpr_name);
                     }
                } while (!(gp.gp_flags & XFS_GETPARENTS_OFLAG_DONE));

                return 0;
           }

## [](#RETURN_VALUE)RETURN VALUE

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           Error codes can be one of, but are not limited to, the following:

           EFSBADCRC
                  Metadata checksum validation failed while performing the
                  query.

           EFSCORRUPTED
                  Metadata corruption was encountered while performing the
                  query.

           EINVAL One or more of the arguments specified is invalid.

           EMSGSIZE
                  The record buffer was not large enough to store even a
                  single record.

           ENOMEM Not enough memory to retrieve parent pointers.

           EOPNOTSUPP
                  Repairs of the requested metadata object are not supported.

           EROFS  Filesystem is read-only and a repair was requested.

           ESHUTDOWN
                  Filesystem is shut down due to previous errors.

           EIO    An I/O error was encountered while performing the query.

## [](#CONFORMING_TO)CONFORMING TO

           This API is specific to XFS filesystem on the Linux kernel.

## [](#SEE_ALSO)SEE ALSO

           ioctl(2)

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

    XFS                             2024-04-09        IOCTL-XFS-GETPARENTS(2)

------------------------------------------------------------------------

[Copyright and license for this manual page](../man2/ioctl_xfs_getparents.2.license.html)

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
