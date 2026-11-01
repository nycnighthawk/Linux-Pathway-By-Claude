---
{"title": "get_kernel_syms(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/get_kernel_syms.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# get_kernel_syms(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    get_kernel_syms(2)         System Calls Manual         get_kernel_syms(2)

## [](#NAME)NAME

           get_kernel_syms - retrieve exported kernel and module symbols

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/module.h>

           [[deprecated]] int get_kernel_syms(struct kernel_sym *table);

## [](#DESCRIPTION)DESCRIPTION

           Note: This system call is present only before Linux 2.6.

           If table is NULL, get_kernel_syms() returns the number of symbols
           available for query.  Otherwise, it fills in a table of
           structures:

               struct kernel_sym {
                   unsigned long value;
                   char          name[60];
               };

           The symbols are interspersed with magic symbols of the form
           #module-name with the kernel having an empty name.  The value
           associated with a symbol of this form is the address at which the
           module is loaded.

           The symbols exported from each module follow their magic module
           tag and the modules are returned in the reverse of the order in
           which they were loaded.

## [](#RETURN_VALUE)RETURN VALUE

           On success, returns the number of symbols copied to table.  On
           error, -1 is returned and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           There is only one possible error return:

           ENOSYS get_kernel_syms() is not supported in this version of the
                  kernel.

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

## [](#BUGS)BUGS

           There is no way to indicate the size of the buffer allocated for
           table.  If symbols have been added to the kernel since the program
           queried for the symbol table size, memory will be corrupted.

           The length of exported symbol names is limited to 59 characters.

           Because of these limitations, this system call is deprecated in
           favor of query_module(2) (which is itself nowadays deprecated in
           favor of other interfaces described on its manual page).

## [](#SEE_ALSO)SEE ALSO

           create_module(2), delete_module(2), init_module(2),
           query_module(2)

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

    Linux man-pages 6.19            2025-05-17             get_kernel_syms(2)

------------------------------------------------------------------------

Pages that refer to this page: [query_module(2)](../man2/query_module.2.html),  [syscalls(2)](../man2/syscalls.2.html)

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
