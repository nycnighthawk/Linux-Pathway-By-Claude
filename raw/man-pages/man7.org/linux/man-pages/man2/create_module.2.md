---
{"title": "create_module(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/create_module.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# create_module(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    create_module(2)           System Calls Manual           create_module(2)

## [](#NAME)NAME

           create_module - create a loadable module entry

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/module.h>

           [[deprecated]] caddr_t create_module(const char *name, size_t size);

## [](#DESCRIPTION)DESCRIPTION

           Note: This system call is present only before Linux 2.6.

           create_module() attempts to create a loadable module entry and
           reserve the kernel memory that will be needed to hold the module.
           This system call requires privilege.

## [](#RETURN_VALUE)RETURN VALUE

           On success, returns the kernel address at which the module will
           reside.  On error, -1 is returned and errno is set to indicate the
           error.

## [](#ERRORS)ERRORS

           EEXIST A module by that name already exists.

           EFAULT name is outside the program's accessible address space.

           EINVAL The requested size is too small even for the module header
                  information.

           ENOMEM The kernel could not allocate a contiguous block of memory
                  large enough for the module.

           ENOSYS create_module() is not supported in this version of the
                  kernel (e.g., Linux 2.6 or later).

           EPERM  The caller was not privileged (did not have the
                  CAP_SYS_MODULE capability).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Removed in Linux 2.6.

           This obsolete system call is not supported by glibc.  No
           declaration is provided in glibc headers, but, through a quirk of
           history, glibc versions before glibc 2.23 did export an ABI for
           this system call.  Therefore, in order to employ this system call,
           it was sufficient to manually declare the interface in your code;
           alternatively, you could invoke the system call using syscall(2).

## [](#SEE_ALSO)SEE ALSO

           delete_module(2), init_module(2), query_module(2)

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

    Linux man-pages 6.19            2025-05-17               create_module(2)

------------------------------------------------------------------------

Pages that refer to this page: [delete_module(2)](../man2/delete_module.2.html),  [get_kernel_syms(2)](../man2/get_kernel_syms.2.html),  [init_module(2)](../man2/init_module.2.html),  [query_module(2)](../man2/query_module.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [unimplemented(2)](../man2/unimplemented.2.html),  [systemd.exec(5)](../man5/systemd.exec.5.html)

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
