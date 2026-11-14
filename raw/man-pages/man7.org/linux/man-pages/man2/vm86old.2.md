---
{"title": "vm86(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/vm86old.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# vm86(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    vm86(2)                    System Calls Manual                    vm86(2)

## [](#NAME)NAME

           vm86old, vm86 - enter virtual 8086 mode

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/vm86.h>

           int vm86old(struct vm86_struct *info);
           int vm86(unsigned long fn, struct vm86plus_struct *v86);

## [](#DESCRIPTION)DESCRIPTION

           The system call vm86() was introduced in Linux 0.97p2.  In Linux
           2.1.15 and 2.0.28, it was renamed to vm86old(), and a new vm86()
           was introduced.  The definition of struct vm86_struct was changed
           in 1.1.8 and 1.1.9.

           These calls cause the process to enter VM86 mode (virtual-8086 in
           Intel literature), and are used by dosemu.

           VM86 mode is an emulation of real mode within a protected mode
           task.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT This return value is specific to i386 and indicates a
                  problem with getting user-space data.

           ENOSYS This return value indicates the call is not implemented on
                  the present architecture.

           EPERM  Saved kernel stack exists.  (This is a kernel sanity check;
                  the saved stack should exist only within vm86 mode itself.)

## [](#STANDARDS)STANDARDS

           Linux on 32-bit Intel processors.

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

    Linux man-pages 6.19            2026-02-08                        vm86(2)

------------------------------------------------------------------------

Pages that refer to this page: [modify_ldt(2)](../man2/modify_ldt.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [unimplemented(2)](../man2/unimplemented.2.html),  [systemd.exec(5)](../man5/systemd.exec.5.html)

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
