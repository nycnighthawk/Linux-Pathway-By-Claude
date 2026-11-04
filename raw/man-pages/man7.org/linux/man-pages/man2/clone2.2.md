---
{"title": "clone2(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/clone2.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# clone2(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    clone2(2)                  System Calls Manual                  clone2(2)

## [](#NAME)NAME

           clone2, __clone2 - create a child process

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           // glibc wrapper:
           int __clone2(typeof(int (void *)) *fn,
                        void *stack_base, size_t stack_size,
                        int flags, void *arg, ...
                     /* pid_t *parent_tid, struct user_desc *tls,
                        pid_t *child_tid */ );

           // System call:
           long syscall(SYS_clone2, unsigned long flags, void *stack_base,
                       int stack_size,         /* Size of stack */
                       int *parent_tid, int *child_tid,
                       unsigned long tls);

## [](#DESCRIPTION)DESCRIPTION

           These interfaces are similar to clone(2) but for ia64.

           These interfaces operate in the same way as clone(2), except that
           stack_base points to the lowest address of the child's stack area,
           and stack_size specifies the size of the stack pointed to by
           stack_base.

## [](#RETURN_VALUE)RETURN VALUE

           See clone(2).

## [](#ERRORS)ERRORS

           See clone(2).

## [](#STANDARDS)STANDARDS

           None.

## [](#HISTORY)HISTORY

           Linux (ia64).

## [](#SEE_ALSO)SEE ALSO

           clone(2)

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

    Linux man-pages 6.19            2026-06-08                      clone2(2)

------------------------------------------------------------------------

Pages that refer to this page: [clone(2)](../man2/clone.2.html),  [syscalls(2)](../man2/syscalls.2.html)

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
