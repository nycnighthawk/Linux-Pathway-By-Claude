---
{"title": "UFFDIO_COPY(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/uffdio_copy.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# UFFDIO_COPY(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UFFDIO_COPY(2const)                                   UFFDIO_COPY(2const)

## [](#NAME)NAME

           UFFDIO_COPY - atomically copy a continuous memory chunk into the
           userfault registered range

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/userfaultfd.h>  /* Definition of UFFD* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, UFFDIO_COPY, struct uffdio_copy *argp);

           #include <linux/userfaultfd.h>

           struct uffdio_copy {
               __u64  dst;   /* Destination of copy */
               __u64  src;   /* Source of copy */
               __u64  len;   /* Number of bytes to copy */
               __u64  mode;  /* Flags controlling behavior of copy */
               __s64  copy;  /* Number of bytes copied, or negated error */
           };

## [](#DESCRIPTION)DESCRIPTION

           Atomically copy a continuous memory chunk into the userfault
           registered range and optionally wake up the blocked thread.

           The following value may be bitwise ORed in mode to change the
           behavior of the UFFDIO_COPY operation:

           UFFDIO_COPY_MODE_DONTWAKE
                  Do not wake up the thread that waits for page-fault
                  resolution

           UFFDIO_COPY_MODE_WP
                  Copy the page with read-only permission.  This allows the
                  user to trap the next write to the page, which will block
                  and generate another write-protect userfault message.  This
                  is used only when both UFFDIO_REGISTER_MODE_MISSING and
                  UFFDIO_REGISTER_MODE_WP modes are enabled for the
                  registered range.

           The copy field is used by the kernel to return the number of bytes
           that was actually copied, or an error (a negated errno-style
           value).  The copy field is output-only; it is not read by the
           UFFDIO_COPY operation.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  In this case, the entire area was
           copied.

           On error, -1 is returned and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EAGAIN The number of bytes copied (i.e., the value returned in the
                  copy field) does not equal the value that was specified in
                  the len field.

           EINVAL Either dst or len was not a multiple of the system page
                  size, or the range specified by src and len or dst and len
                  was invalid.

           EINVAL An invalid bit was specified in the mode field.

           ENOENT (since Linux 4.11)
                  The faulting process has changed its virtual memory layout
                  simultaneously with an outstanding UFFDIO_COPY operation.

           ENOSPC (from Linux 4.11 until Linux 4.13)
                  The faulting process has exited at the time of a
                  UFFDIO_COPY operation.

           ESRCH (since Linux 4.13)
                  The faulting process has exited at the time of a
                  UFFDIO_COPY operation.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 4.3.

## [](#EXAMPLES)EXAMPLES

           See userfaultfd(2).

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), ioctl_userfaultfd(2), userfaultfd(2)

           linux.git/Documentation/admin-guide/mm/userfaultfd.rst

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

    Linux man-pages 6.19            2026-02-08            UFFDIO_COPY(2const)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_userfaultfd(2)](../man2/ioctl_userfaultfd.2.html)

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
