---
{"title": "io_destroy(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/io_destroy.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# io_destroy(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    io_destroy(2)              System Calls Manual              io_destroy(2)

## [](#NAME)NAME

           io_destroy - destroy an asynchronous I/O context

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/aio_abi.h>    /* Definition of aio_context_t */
           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_io_destroy, aio_context_t ctx_id);

## [](#DESCRIPTION)DESCRIPTION

           Note: you probably want to use the io_destroy(3) wrapper function
           provided by libaio; see VERSIONS.

           The io_destroy() system call will attempt to cancel all
           outstanding asynchronous I/O operations against ctx_id, will block
           on the completion of all operations that could not be canceled,
           and will destroy the ctx_id.

## [](#RETURN_VALUE)RETURN VALUE

           On success, io_destroy() returns 0.  On error, -1 is returned, and
           errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT ctx_id was not a valid address.

           EINVAL The AIO context specified by ctx_id is invalid.

           ENOSYS io_destroy() is not implemented on this architecture.

## [](#VERSIONS)VERSIONS

           libaio ⟨https://pagure.io/libaio⟩ provides a wrapper function with
           the same name, but different prototype and return value.  You
           probably want to use that wrapper.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.5.

## [](#SEE_ALSO)SEE ALSO

           io_cancel(2), io_getevents(2), io_setup(2), io_submit(2),
           io_destroy(3), aio(7)

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

    Linux man-pages 6.19            2026-04-11                  io_destroy(2)

------------------------------------------------------------------------

Pages that refer to this page: [io_cancel(2)](../man2/io_cancel.2.html),  [io_getevents(2)](../man2/io_getevents.2.html),  [io_setup(2)](../man2/io_setup.2.html),  [io_submit(2)](../man2/io_submit.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [io_destroy(3)](../man3/io_destroy.3.html),  [aio(7)](../man7/aio.7.html)

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
