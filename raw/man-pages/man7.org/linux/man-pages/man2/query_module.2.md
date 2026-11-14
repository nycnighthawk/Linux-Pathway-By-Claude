---
{"title": "query_module(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/query_module.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# query_module(2) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [VERSIONS](#VERSIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    query_module(2)            System Calls Manual            query_module(2)

## [](#NAME)NAME

           query_module - query the kernel for various bits pertaining to
           modules

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/module.h>

           [[deprecated]] int query_module(size_t bufsize;
                                           const char *name, int which,
                                           void buf[bufsize], size_t bufsize,
                                           size_t *ret);

## [](#DESCRIPTION)DESCRIPTION

           Note: This system call is present only before Linux 2.6.

           query_module() requests information from the kernel about loadable
           modules.  The returned information is placed in the buffer pointed
           to by buf.  The caller must specify the size of buf in bufsize.
           The precise nature and format of the returned information depend
           on the operation specified by which.  Some operations require name
           to identify a currently loaded module, some allow name to be NULL,
           indicating the kernel proper.

           The following values can be specified for which:

           0      Returns success, if the kernel supports query_module().
                  Used to probe for availability of the system call.

           QM_MODULES
                  Returns the names of all loaded modules.  The returned
                  buffer consists of a sequence of null-terminated strings;
                  ret is set to the number of modules.

           QM_DEPS
                  Returns the names of all modules used by the indicated
                  module.  The returned buffer consists of a sequence of
                  null-terminated strings; ret is set to the number of
                  modules.

           QM_REFS
                  Returns the names of all modules using the indicated
                  module.  This is the inverse of QM_DEPS.  The returned
                  buffer consists of a sequence of null-terminated strings;
                  ret is set to the number of modules.

           QM_SYMBOLS
                  Returns the symbols and values exported by the kernel or
                  the indicated module.  The returned buffer is an array of
                  structures of the following form

                      struct module_symbol {
                          unsigned long value;
                          unsigned long name;
                      };

                  followed by null-terminated strings.  The value of name is
                  the character offset of the string relative to the start of
                  buf; ret is set to the number of symbols.

           QM_INFO
                  Returns miscellaneous information about the indicated
                  module.  The output buffer format is:

                      struct module_info {
                          unsigned long address;
                          unsigned long size;
                          unsigned long flags;
                      };

                  where address is the kernel address at which the module
                  resides, size is the size of the module in bytes, and flags
                  is a mask of MOD_RUNNING, MOD_AUTOCLEAN, and so on, that
                  indicates the current status of the module (see the Linux
                  kernel source file include/linux/module.h).  ret is set to
                  the size of the module_info structure.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT At least one of name, buf, or ret was outside the program's
                  accessible address space.

           EINVAL Invalid which; or name is NULL (indicating "the kernel"),
                  but this is not permitted with the specified value of
                  which.

           ENOENT No module by that name exists.

           ENOSPC The buffer size provided was too small.  ret is set to the
                  minimum size needed.

           ENOSYS query_module() is not supported in this version of the
                  kernel (e.g., Linux 2.6 or later).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#VERSIONS)VERSIONS

           Removed in Linux 2.6.

           Some of the information that was formerly available via
           query_module() can be obtained from /proc/modules, /proc/kallsyms,
           and the files under the directory /sys/module.

           The query_module() system call is not supported by glibc.  No
           declaration is provided in glibc headers, but, through a quirk of
           history, glibc does export an ABI for this system call.
           Therefore, in order to employ this system call, it is sufficient
           to manually declare the interface in your code; alternatively, you
           can invoke the system call using syscall(2).

## [](#SEE_ALSO)SEE ALSO

           create_module(2), delete_module(2), get_kernel_syms(2),
           init_module(2), lsmod(8), modinfo(8)

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

    Linux man-pages 6.19            2025-09-07                query_module(2)

------------------------------------------------------------------------

Pages that refer to this page: [create_module(2)](../man2/create_module.2.html),  [delete_module(2)](../man2/delete_module.2.html),  [get_kernel_syms(2)](../man2/get_kernel_syms.2.html),  [init_module(2)](../man2/init_module.2.html),  [syscalls(2)](../man2/syscalls.2.html)

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
