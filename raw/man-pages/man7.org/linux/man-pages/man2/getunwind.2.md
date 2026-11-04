---
{"title": "getunwind(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/getunwind.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# getunwind(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    getunwind(2)               System Calls Manual               getunwind(2)

## [](#NAME)NAME

           getunwind - copy the unwind data to caller's buffer

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/unwind.h>
           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           [[deprecated]] long syscall(size_t buf_size;
                                       SYS_getunwind, void buf[buf_size],
                                       size_t buf_size);

## [](#DESCRIPTION)DESCRIPTION

           Note: this system call is obsolete.

           The IA-64-specific getunwind() system call copies the kernel's
           call frame unwind data into the buffer pointed to by buf and
           returns the size of the unwind data; this data describes the gate
           page (kernel code that is mapped into user space).

           The size of the buffer buf is specified in buf_size.  The data is
           copied only if buf_size is greater than or equal to the size of
           the unwind data and buf is not NULL; otherwise, no data is copied,
           and the call succeeds, returning the size that would be needed to
           store the unwind data.

           The first part of the unwind data contains an unwind table.  The
           rest contains the associated unwind information, in no particular
           order.  The unwind table contains entries of the following form:

               u64 start;      (64-bit address of start of function)
               u64 end;        (64-bit address of end of function)
               u64 info;       (BUF-relative offset to unwind info)

           An entry whose start value is zero indicates the end of the table.
           For more information about the format, see the IA-64 Software
           Conventions and Runtime Architecture manual.

## [](#RETURN_VALUE)RETURN VALUE

           On success, getunwind() returns the size of the unwind data.  On
           error, -1 is returned and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           getunwind() fails with the error EFAULT if the unwind info can't
           be stored in the space specified by buf.

## [](#STANDARDS)STANDARDS

           Linux on IA-64.

## [](#HISTORY)HISTORY

           Linux 2.4.

           This system call has been deprecated.  The modern way to obtain
           the kernel's unwind data is via the vdso(7).

## [](#SEE_ALSO)SEE ALSO

           getauxval(3)

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

    Linux man-pages 6.19            2026-02-08                   getunwind(2)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html)

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
