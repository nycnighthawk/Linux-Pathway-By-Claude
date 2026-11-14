---
{"title": "io_getevents(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/io_getevents.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# io_getevents(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    io_getevents(2)            System Calls Manual            io_getevents(2)

## [](#NAME)NAME

           io_getevents - read asynchronous I/O events from the completion
           queue

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/aio_abi.h>    /* Definition of *io_* types */
           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_io_getevents, aio_context_t ctx_id,
                       long min_nr, long nr, struct io_event *events,
                       struct timespec *timeout);

## [](#DESCRIPTION)DESCRIPTION

           Note: you probably want to use the io_getevents(3) wrapper
           function provided by libaio; see VERSIONS.

           The io_getevents() system call attempts to read at least min_nr
           events and up to nr events from the completion queue of the AIO
           context specified by ctx_id.

           The timeout argument specifies the amount of time to wait for
           events, and is specified as a relative timeout in a timespec(3)
           structure.

           The specified time will be rounded up to the system clock
           granularity and is guaranteed not to expire early.

           Specifying timeout as NULL means block indefinitely until at least
           min_nr events have been obtained.

## [](#RETURN_VALUE)RETURN VALUE

           On success, io_getevents() returns the number of events read.
           This may be 0, or a value less than min_nr, if the timeout
           expired.  It may also be a nonzero value less than min_nr, if the
           call was interrupted by a signal handler.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT Either events or timeout is an invalid pointer.

           EINTR  Interrupted by a signal handler; see signal(7).

           EINVAL ctx_id is invalid.

           EINVAL min_nr is out of range or nr is out of range.

           ENOSYS io_getevents() is not implemented on this architecture.

## [](#VERSIONS)VERSIONS

           libaio ⟨https://pagure.io/libaio⟩ provides a wrapper function with
           the same name, but different prototype and return value.  You
           probably want to use that wrapper.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.5.

## [](#SEE_ALSO)SEE ALSO

           io_cancel(2), io_destroy(2), io_setup(2), io_submit(2),
           io_getevents(3), timespec(3), aio(7), time(7)

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

    Linux man-pages 6.19            2026-04-11                io_getevents(2)

------------------------------------------------------------------------

Pages that refer to this page: [io_cancel(2)](../man2/io_cancel.2.html),  [io_destroy(2)](../man2/io_destroy.2.html),  [io_setup(2)](../man2/io_setup.2.html),  [io_submit(2)](../man2/io_submit.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [aio(7)](../man7/aio.7.html),  [signal(7)](../man7/signal.7.html)

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
