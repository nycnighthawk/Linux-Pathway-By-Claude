---
{"title": "F_GETPIPE_SZ(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/F_GETPIPE_SZ.2const.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# F_GETPIPE_SZ(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    F_GETPIPE_SZ(2const)                                 F_GETPIPE_SZ(2const)

## [](#NAME)NAME

           F_GETPIPE_SZ, F_SETPIPE_SZ - get/set the capacity of a pipe

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #define _GNU_SOURCE
           #include <fcntl.h>

           int fcntl(int fd, F_SETPIPE_SZ, int arg);
           int fcntl(int fd, F_GETPIPE_SZ);

## [](#DESCRIPTION)DESCRIPTION

           F_SETPIPE_SZ
                  Change the capacity of the pipe referred to by fd to be at
                  least arg bytes.  An unprivileged process can adjust the
                  pipe capacity to any value between the system page size and
                  the limit defined in /proc/sys/fs/pipe-max-size (see
                  proc_sys_fs(5)).  Attempts to set the pipe capacity below
                  the page size are silently rounded up to the page size.
                  Attempts by an unprivileged process to set the pipe
                  capacity above the limit in /proc/sys/fs/pipe-max-size
                  yield the error EPERM; a privileged process
                  (CAP_SYS_RESOURCE) can override the limit.

                  When allocating the buffer for the pipe, the kernel may use
                  a capacity larger than arg, if that is convenient for the
                  implementation.  (In the current implementation, the
                  allocation is the next higher power-of-two page-size
                  multiple of the requested size.)  The actual capacity (in
                  bytes) that is set is returned as the function result.

                  Attempting to set the pipe capacity smaller than the amount
                  of buffer space currently used to store data produces the
                  error EBUSY.

                  Note that because of the way the pages of the pipe buffer
                  are employed when data is written to the pipe, the number
                  of bytes that can be written may be less than the nominal
                  size, depending on the size of the writes.

           F_GETPIPE_SZ
                  Return (as the function result) the capacity of the pipe
                  referred to by fd.

## [](#RETURN_VALUE)RETURN VALUE

           The pipe capacity.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           See fcntl(2).

           EBUSY  op is F_SETPIPE_SZ and the new pipe capacity specified in
                  arg is smaller than the amount of buffer space currently
                  used to store data in the pipe.

           EPERM  op is F_SETPIPE_SZ and the soft or hard user pipe limit has
                  been reached; see pipe(7).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.35.

## [](#SEE_ALSO)SEE ALSO

           fcntl(2)

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

    Linux man-pages 6.19            2025-09-21           F_GETPIPE_SZ(2const)

------------------------------------------------------------------------

Pages that refer to this page: [fcntl(2)](../man2/fcntl.2.html)

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
