---
{"title": "unimplemented(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/phys.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# unimplemented(2) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                             |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UNIMPLEMENTED(2)           System Calls Manual           UNIMPLEMENTED(2)

## [](#NAME)NAME

           afs_syscall, break, fattach, fdetach, ftime, getmsg, getpmsg,
           gtty, isastream, lock, madvise1, mpx, prof, profil, putmsg,
           putpmsg, security, stty, tuxcall, ulimit, vserver - unimplemented
           system calls

## [](#SYNOPSIS)SYNOPSIS

           Unimplemented system calls.

## [](#DESCRIPTION)DESCRIPTION

           These system calls are not implemented in the Linux kernel.

## [](#RETURN_VALUE)RETURN VALUE

           These system calls always return -1 and set errno to ENOSYS.

## [](#NOTES)NOTES

           Note that ftime(3), profil(3), and ulimit(3) are implemented as
           library functions.

           Some system calls, like alloc_hugepages(2), free_hugepages(2),
           ioperm(2), iopl(2), and vm86(2) exist only on certain
           architectures.

           Some system calls, like ipc(2), create_module(2), init_module(2),
           and delete_module(2) exist only when the Linux kernel was built
           with support for them.

## [](#SEE_ALSO)SEE ALSO

           syscalls(2)

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

    Linux man-pages 6.19            2026-02-08               UNIMPLEMENTED(2)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl(2)](../man2/ioctl.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [systemd.exec(5)](../man5/systemd.exec.5.html)

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
