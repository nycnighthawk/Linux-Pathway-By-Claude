---
{"title": "iopl(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/iopl.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# iopl(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    iopl(2)                    System Calls Manual                    iopl(2)

## [](#NAME)NAME

           iopl - change I/O privilege level

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/io.h>

           [[deprecated]] int iopl(int level);

## [](#DESCRIPTION)DESCRIPTION

           iopl() changes the I/O privilege level of the calling thread, as
           specified by the two least significant bits in level.

           The I/O privilege level for a normal thread is 0.  Permissions are
           inherited from parents to children.

           This call is deprecated, is significantly slower than ioperm(2),
           and is only provided for older X servers which require access to
           all 65536 I/O ports.  It is mostly for the i386 architecture.  On
           many other architectures it does not exist or will always return
           an error.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL level is greater than 3.

           ENOSYS This call is unimplemented.

           EPERM  The calling thread has insufficient privilege to call
                  iopl(); the CAP_SYS_RAWIO capability is required to raise
                  the I/O privilege level above its current value.

## [](#VERSIONS)VERSIONS

           glibc2 has a prototype both in <sys/io.h> and in <sys/perm.h>.
           Avoid the latter, it is available on i386 only.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Prior to Linux 5.5 iopl() allowed the thread to disable interrupts
           while running at a higher I/O privilege level.  This will probably
           crash the system, and is not recommended.

           Prior to Linux 3.7, on some architectures (such as i386),
           permissions were inherited by the child produced by fork(2) and
           were preserved across execve(2).  This behavior was inadvertently
           changed in Linux 3.7, and won't be reinstated.

## [](#SEE_ALSO)SEE ALSO

           ioperm(2), outb(2), capabilities(7)

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

    Linux man-pages 6.19            2026-02-08                        iopl(2)

------------------------------------------------------------------------

Pages that refer to this page: [ioperm(2)](../man2/ioperm.2.html),  [outb(2)](../man2/outb.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [unimplemented(2)](../man2/unimplemented.2.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [capabilities(7)](../man7/capabilities.7.html)

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
