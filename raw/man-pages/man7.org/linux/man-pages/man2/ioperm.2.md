---
{"title": "ioperm(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioperm.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ioperm(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ioperm(2)                  System Calls Manual                  ioperm(2)

## [](#NAME)NAME

           ioperm - set port input/output permissions

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/io.h>

           int ioperm(unsigned long from, unsigned long num, int turn_on);

## [](#DESCRIPTION)DESCRIPTION

           ioperm() sets the port access permission bits for the calling
           thread for num bits starting from port address from.  If turn_on
           is nonzero, then permission for the specified bits is enabled;
           otherwise it is disabled.  If turn_on is nonzero, the calling
           thread must be privileged (CAP_SYS_RAWIO).

           Before Linux 2.6.8, only the first 0x3ff I/O ports could be
           specified in this manner.  For more ports, the iopl(2) system call
           had to be used (with a level argument of 3).  Since Linux 2.6.8,
           65,536 I/O ports can be specified.

           Permissions are inherited by the child created by fork(2) (but see
           HISTORY).  Permissions are preserved across execve(2); this is
           useful for giving port access permissions to unprivileged
           programs.

           This call is mostly for the i386 architecture.  On many other
           architectures it does not exist or will always return an error.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL Invalid values for from or num.

           EIO    (on PowerPC) This call is not supported.

           ENOMEM Out of memory.

           EPERM  The calling thread has insufficient privilege.

## [](#VERSIONS)VERSIONS

           glibc has an ioperm() prototype both in <sys/io.h> and in
           <sys/perm.h>.  Avoid the latter, it is available on i386 only.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Before Linux 2.4, permissions were not inherited by a child
           created by fork(2).

## [](#NOTES)NOTES

           The /proc/ioports file shows the I/O ports that are currently
           allocated on the system.

## [](#SEE_ALSO)SEE ALSO

           iopl(2), outb(2), capabilities(7)

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

    Linux man-pages 6.19            2025-05-17                      ioperm(2)

------------------------------------------------------------------------

Pages that refer to this page: [fork(2)](../man2/fork.2.html),  [ioctl_console(2)](../man2/ioctl_console.2.html),  [iopl(2)](../man2/iopl.2.html),  [outb(2)](../man2/outb.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [unimplemented(2)](../man2/unimplemented.2.html),  [mem(4)](../man4/mem.4.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [capabilities(7)](../man7/capabilities.7.html)

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
