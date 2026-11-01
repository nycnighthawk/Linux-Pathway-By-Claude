---
{"title": "io_submit(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/io_submit.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# io_submit(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    io_submit(2)               System Calls Manual               io_submit(2)

## [](#NAME)NAME

           io_submit - submit asynchronous I/O blocks for processing

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/aio_abi.h>
           #include <sys/syscall.h>    /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_io_submit, aio_context_t ctx_id,
                       long n, struct iocb *iocbpp[n]);

## [](#DESCRIPTION)DESCRIPTION

           Note: you probably want to use the io_setup(3) wrapper function
           provided by libaio; see VERSIONS.

           The io_submit() system call queues n I/O request blocks for
           processing in the AIO context ctx_id.  The iocbpp argument should
           be an array of n AIO control blocks, which will be submitted to
           context ctx_id.

           The iocb (I/O control block) structure defined in linux/aio_abi.h
           defines the parameters that control the I/O operation.

               #include <linux/aio_abi.h>

               struct iocb {
                   __u64   aio_data;
                   __u32   PADDED(aio_key, aio_rw_flags);
                   __u16   aio_lio_opcode;
                   __s16   aio_reqprio;
                   __u32   aio_fildes;
                   __u64   aio_buf;
                   __u64   aio_nbytes;
                   __s64   aio_offset;
                   __u64   aio_reserved2;
                   __u32   aio_flags;
                   __u32   aio_resfd;
               };

           The fields of this structure are as follows:

           aio_data
                  This data is copied into the data field of the io_event
                  structure upon I/O completion (see io_getevents(2)).

           aio_key
                  This is an internal field used by the kernel.  Do not
                  modify this field after an io_submit() call.

           aio_rw_flags
                  This defines the R/W flags passed with structure.  The
                  valid values are:

                  RWF_APPEND (since Linux 4.16)
                         Append data to the end of the file.  See the
                         description of the flag of the same name in
                         pwritev2(2) as well as the description of O_APPEND
                         in open(2).  The aio_offset field is ignored.  The
                         file offset is not changed.

                  RWF_DSYNC (since Linux 4.13)
                         Write operation complete according to requirement of
                         synchronized I/O data integrity.  See the
                         description of the flag of the same name in
                         pwritev2(2) as well the description of O_DSYNC in
                         open(2).

                  RWF_HIPRI (since Linux 4.13)
                         High priority request, poll if possible

                  RWF_NOWAIT (since Linux 4.14)
                         Don't wait if the I/O will block for operations such
                         as file block allocations, dirty page flush, mutex
                         locks, or a congested block device inside the
                         kernel.  If any of these conditions are met, the
                         control block is returned immediately with a return
                         value of -EAGAIN in the res field of the io_event
                         structure (see io_getevents(2)).

                  RWF_SYNC (since Linux 4.13)
                         Write operation complete according to requirement of
                         synchronized I/O file integrity.  See the
                         description of the flag of the same name in
                         pwritev2(2) as well the description of O_SYNC in
                         open(2).

                  RWF_NOAPPEND (since Linux 6.9)
                         Do not honor O_APPEND open(2) flag.  See the
                         description of RWF_NOAPPEND in pwritev2(2).

                  RWF_ATOMIC (since Linux 6.11)
                         Write a block of data such that a write will never
                         be torn from power fail or similar.  See the
                         description of RWF_ATOMIC in pwritev2(2).  For usage
                         with IOCB_CMD_PWRITEV, the upper vector limit is
                         stx_atomic_write_segments_max.  See
                         STATX_WRITE_ATOMIC and stx_atomic_write_segments_max
                         description in statx(2).

           aio_lio_opcode
                  This defines the type of I/O to be performed by the iocb
                  structure.  The valid values are defined by the enum
                  defined in linux/aio_abi.h:

                      enum {
                          IOCB_CMD_PREAD = 0,
                          IOCB_CMD_PWRITE = 1,
                          IOCB_CMD_FSYNC = 2,
                          IOCB_CMD_FDSYNC = 3,
                          IOCB_CMD_POLL = 5,
                          IOCB_CMD_NOOP = 6,
                          IOCB_CMD_PREADV = 7,
                          IOCB_CMD_PWRITEV = 8,
                      };

           aio_reqprio
                  This defines the requests priority.

           aio_fildes
                  The file descriptor on which the I/O operation is to be
                  performed.

           aio_buf
                  This is the buffer used to transfer data for a read or
                  write operation.

           aio_nbytes
                  This is the size of the buffer pointed to by aio_buf.

           aio_offset
                  This is the file offset at which the I/O operation is to be
                  performed.

           aio_flags
                  This is the set of flags associated with the iocb
                  structure.  The valid values are:

                  IOCB_FLAG_RESFD
                         Asynchronous I/O control must signal the file
                         descriptor mentioned in aio_resfd upon completion.

                  IOCB_FLAG_IOPRIO (since Linux 4.18)
                         Interpret the aio_reqprio field as an IOPRIO_VALUE
                         as defined by linux/ioprio.h.

           aio_resfd
                  The file descriptor to signal in the event of asynchronous
                  I/O completion.

## [](#RETURN_VALUE)RETURN VALUE

           On success, io_submit() returns the number of iocbs submitted
           (which may be less than n, or 0 if n is zero).

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EAGAIN Insufficient resources are available to queue any iocbs.

           EBADF  The file descriptor specified in the first iocb is invalid.

           EFAULT One of the data structures points to invalid data.

           EINVAL The AIO context specified by ctx_id is invalid.

           EINVAL n is less than 0.

           EINVAL The iocb at *iocbpp[0] is not properly initialized.

           EINVAL The operation specified is invalid for the file descriptor
                  in the iocb.

           EINVAL The value in the aio_reqprio field is invalid.

           ENOSYS io_submit() is not implemented on this architecture.

           EPERM  The aio_reqprio field is set with the class
                  IOPRIO_CLASS_RT, but the submitting context does not have
                  the CAP_SYS_ADMIN capability.

## [](#VERSIONS)VERSIONS

           libaio ⟨https://pagure.io/libaio⟩ provides a wrapper function with
           the same name, but different prototype and return value.  You
           probably want to use that wrapper.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.5.

## [](#SEE_ALSO)SEE ALSO

           io_cancel(2), io_destroy(2), io_getevents(2), io_setup(2),
           io_submit(3), aio(7)

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

    Linux man-pages 6.19            2026-04-11                   io_submit(2)

------------------------------------------------------------------------

Pages that refer to this page: [F_GET_SEALS(2const)](../man2/F_GET_SEALS.2const.html),  [io_cancel(2)](../man2/io_cancel.2.html),  [io_destroy(2)](../man2/io_destroy.2.html),  [io_getevents(2)](../man2/io_getevents.2.html),  [io_setup(2)](../man2/io_setup.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [aio(7)](../man7/aio.7.html)

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
