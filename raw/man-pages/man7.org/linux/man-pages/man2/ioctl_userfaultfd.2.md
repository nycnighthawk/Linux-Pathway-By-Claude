---
{"title": "ioctl_userfaultfd(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_userfaultfd.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# ioctl_userfaultfd(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ioctl_userfaultfd(2)       System Calls Manual       ioctl_userfaultfd(2)

## [](#NAME)NAME

           ioctl_userfaultfd - create a file descriptor for handling page
           faults in user space

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/userfaultfd.h>  /* Definition of UFFD* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, int op, ...);

## [](#DESCRIPTION)DESCRIPTION

           Various ioctl(2) operations can be performed on a userfaultfd
           object (created by a call to userfaultfd(2)) using calls of the
           form:

               ioctl(fd, op, argp);

           In the above, fd is a file descriptor referring to a userfaultfd
           object, op is one of the operations listed below, and argp is a
           pointer to a data structure that is specific to op.

           The various ioctl(2) operations are described below.  The
           UFFDIO_API, UFFDIO_REGISTER, and UFFDIO_UNREGISTER operations are
           used to configure userfaultfd behavior.  These operations allow
           the caller to choose what features will be enabled and what kinds
           of events will be delivered to the application.  The remaining
           operations are range operations.  These operations enable the
           calling application to resolve page-fault events.

           UFFDIO_API(2const)
           UFFDIO_REGISTER(2const)
           UFFDIO_UNREGISTER(2const)
           UFFDIO_COPY(2const)
           UFFDIO_MOVE(2const)
           UFFDIO_ZEROPAGE(2const)
           UFFDIO_WAKE(2const)
           UFFDIO_WRITEPROTECT(2const)
           UFFDIO_RWPROTECT(2const)
           UFFDIO_CONTINUE(2const)
           UFFDIO_POISON(2const)
           UFFDIO_SET_MODE(2const)

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           The following general errors can occur for all of the operations
           described above:

           EFAULT argp does not point to a valid memory address.

           EINVAL (For all operations except UFFDIO_API.)  The userfaultfd
                  object has not yet been enabled (via the UFFDIO_API
                  operation).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#EXAMPLES)EXAMPLES

           See userfaultfd(2).

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), mmap(2), userfaultfd(2)

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

    Linux man-pages 6.19            2026-06-04           ioctl_userfaultfd(2)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl(2)](../man2/ioctl.2.html),  [UFFDIO_API(2const)](../man2/UFFDIO_API.2const.html),  [UFFDIO_CONTINUE(2const)](../man2/UFFDIO_CONTINUE.2const.html),  [UFFDIO_COPY(2const)](../man2/UFFDIO_COPY.2const.html),  [UFFDIO_MOVE(2const)](../man2/UFFDIO_MOVE.2const.html),  [UFFDIO_POISON(2const)](../man2/UFFDIO_POISON.2const.html),  [UFFDIO_REGISTER(2const)](../man2/UFFDIO_REGISTER.2const.html),  [UFFDIO_RWPROTECT(2const)](../man2/UFFDIO_RWPROTECT.2const.html),  [UFFDIO_SET_MODE(2const)](../man2/UFFDIO_SET_MODE.2const.html),  [UFFDIO_UNREGISTER(2const)](../man2/UFFDIO_UNREGISTER.2const.html),  [UFFDIO_WAKE(2const)](../man2/UFFDIO_WAKE.2const.html),  [UFFDIO_WRITEPROTECT(2const)](../man2/UFFDIO_WRITEPROTECT.2const.html),  [UFFDIO_ZEROPAGE(2const)](../man2/UFFDIO_ZEROPAGE.2const.html),  [userfaultfd(2)](../man2/userfaultfd.2.html)

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
