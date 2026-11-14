---
{"title": "PR_SET_MM_START_DATA(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pr_set_mm_end_data.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_SET_MM_START_DATA(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_SET_MM_START_DATA(2const)                 PR_SET_MM_START_DATA(2const)

## [](#NAME)NAME

           PR_SET_MM_START_DATA, PR_SET_MM_END_DATA - modify kernel memory
           map descriptor fields

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_SET_MM, PR_SET_MM_START_DATA, unsigned long addr, 0L, 0L);
           int prctl(PR_SET_MM, PR_SET_MM_END_DATA, unsigned long addr, 0L, 0L);

## [](#DESCRIPTION)DESCRIPTION

           PR_SET_MM_START_DATA
                  Set the address above which initialized and uninitialized
                  (bss) data are placed.  The corresponding memory area must
                  be readable and writable, but not executable or shareable.

           PR_SET_MM_END_DATA
                  Set the address below which initialized and uninitialized
                  (bss) data are placed.  The corresponding memory area must
                  be readable and writable, but not executable or shareable.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL addr is greater than TASK_SIZE (the limit on the size of
                  the user address space for this architecture).

           EINVAL The permissions of the corresponding memory area are not as
                  required.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 3.3.

## [](#SEE_ALSO)SEE ALSO

           prctl(2)

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

    Linux man-pages 6.19            2026-02-08   PR_SET_MM_START_DATA(2const)

------------------------------------------------------------------------

Pages that refer to this page: [PR_SET_MM(2const)](../man2/PR_SET_MM.2const.html),  [PR_SET_MM_MAP(2const)](../man2/PR_SET_MM_MAP.2const.html)

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
