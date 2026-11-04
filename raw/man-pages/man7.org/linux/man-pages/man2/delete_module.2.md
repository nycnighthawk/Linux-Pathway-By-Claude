---
{"title": "delete_module(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/delete_module.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# delete_module(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    delete_module(2)           System Calls Manual           delete_module(2)

## [](#NAME)NAME

           delete_module - unload a kernel module

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <fcntl.h>            /* Definition of O_* constants */
           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_delete_module, const char *name, unsigned int flags);

           Note: glibc provides no wrapper for delete_module(), necessitating
           the use of syscall(2).

## [](#DESCRIPTION)DESCRIPTION

           The delete_module() system call attempts to remove the unused
           loadable module entry identified by name.  If the module has an
           exit function, then that function is executed before unloading the
           module.  The flags argument is used to modify the behavior of the
           system call, as described below.  This system call requires
           privilege.

           Module removal is attempted according to the following rules:

           (1)  If there are other loaded modules that depend on (i.e., refer
                to symbols defined in) this module, then the call fails.

           (2)  Otherwise, if the reference count for the module (i.e., the
                number of processes currently using the module) is zero, then
                the module is immediately unloaded.

           (3)  If a module has a nonzero reference count, then the behavior
                depends on the bits set in flags.  In normal usage (see
                NOTES), the O_NONBLOCK flag is always specified, and the
                O_TRUNC flag may additionally be specified.

                The various combinations for flags have the following effect:

                flags == O_NONBLOCK
                       The call returns immediately, with an error.

                flags == (O_NONBLOCK | O_TRUNC)
                       The module is unloaded immediately, regardless of
                       whether it has a nonzero reference count.

                (flags & O_NONBLOCK) == 0
                       If flags does not specify O_NONBLOCK, the following
                       steps occur:

                       •  The module is marked so that no new references are
                          permitted.

                       •  If the module's reference count is nonzero, the
                          caller is placed in an uninterruptible sleep state
                          (TASK_UNINTERRUPTIBLE) until the reference count is
                          zero, at which point the call unblocks.

                       •  The module is unloaded in the usual way.

           The O_TRUNC flag has one further effect on the rules described
           above.  By default, if a module has an init function but no exit
           function, then an attempt to remove the module fails.  However, if
           O_TRUNC was specified, this requirement is bypassed.

           Using the O_TRUNC flag is dangerous!  If the kernel was not built
           with CONFIG_MODULE_FORCE_UNLOAD, this flag is silently ignored.
           (Normally, CONFIG_MODULE_FORCE_UNLOAD is enabled.)  Using this
           flag taints the kernel (TAINT_FORCED_RMMOD).

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EBUSY  The module is not "live" (i.e., it is still being
                  initialized or is already marked for removal); or, the
                  module has an init function but has no exit function, and
                  O_TRUNC was not specified in flags.

           EFAULT name refers to a location outside the process's accessible
                  address space.

           ENOENT No module by that name exists.

           EPERM  The caller was not privileged (did not have the
                  CAP_SYS_MODULE capability), or module unloading is disabled
                  (see /proc/sys/kernel/modules_disabled in proc(5)).

           EWOULDBLOCK
                  Other modules depend on this module; or, O_NONBLOCK was
                  specified in flags, but the reference count of this module
                  is nonzero and O_TRUNC was not specified in flags.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           The delete_module() system call is not supported by glibc.  No
           declaration is provided in glibc headers, but, through a quirk of
           history, glibc versions before glibc 2.23 did export an ABI for
           this system call.  Therefore, in order to employ this system call,
           it is (before glibc 2.23) sufficient to manually declare the
           interface in your code; alternatively, you can invoke the system
           call using syscall(2).

       Linux 2.4 and earlier
           In Linux 2.4 and earlier, the system call took only one argument:

              int delete_module(const char *name);

           If name is NULL, all unused modules marked auto-clean are removed.

           Some further details of differences in the behavior of
           delete_module() in Linux 2.4 and earlier are not currently
           explained in this manual page.

## [](#NOTES)NOTES

           The uninterruptible sleep that may occur if O_NONBLOCK is omitted
           from flags is considered undesirable, because the sleeping process
           is left in an unkillable state.  As at Linux 3.7, specifying
           O_NONBLOCK is optional, but in future kernels it is likely to
           become mandatory.

## [](#SEE_ALSO)SEE ALSO

           create_module(2), init_module(2), query_module(2), lsmod(8),
           modprobe(8), rmmod(8)

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

    Linux man-pages 6.19            2026-02-08               delete_module(2)

------------------------------------------------------------------------

Pages that refer to this page: [create_module(2)](../man2/create_module.2.html),  [get_kernel_syms(2)](../man2/get_kernel_syms.2.html),  [init_module(2)](../man2/init_module.2.html),  [query_module(2)](../man2/query_module.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [unimplemented(2)](../man2/unimplemented.2.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [capabilities(7)](../man7/capabilities.7.html)

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
