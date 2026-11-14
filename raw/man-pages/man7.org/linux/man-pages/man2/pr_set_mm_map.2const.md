---
{"title": "PR_SET_MM_MAP(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pr_set_mm_map.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_SET_MM_MAP(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_SET_MM_MAP(2const)                               PR_SET_MM_MAP(2const)

## [](#NAME)NAME

           PR_SET_MM_MAP, PR_SET_MM_MAP_SIZE - modify kernel memory map
           descriptor fields

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_SET_MM, PR_SET_MM_MAP,
                     struct prctl_mm_map *map, unsigned long size, 0L);
           int prctl(PR_SET_MM, PR_SET_MM_MAP_SIZE, unsigned int *size, 0L, 0L);

## [](#DESCRIPTION)DESCRIPTION

           PR_SET_MM_MAP
                  Provides one-shot access to all the addresses modifyable
                  with PR_SET_MM(2const) by passing in a struct prctl_mm_map
                  (as defined in <linux/prctl.h>).  The size argument should
                  provide the size of the struct.

           PR_SET_MM_MAP_SIZE
                  Returns (via the size argument) the size of the struct
                  prctl_mm_map the kernel expects.  This allows user space to
                  find a compatible struct.

           These features are available only if the kernel is built with the
           CONFIG_CHECKPOINT_RESTORE option enabled.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL The third argument is an invalid address.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 3.18.

## [](#SEE_ALSO)SEE ALSO

           prctl(2), PR_SET_MM(2const), PR_SET_MM_START_CODE(2const),
           PR_SET_MM_END_CODE(2const), PR_SET_MM_START_DATA(2const),
           PR_SET_MM_END_DATA(2const), PR_SET_MM_START_STACK(2const),
           PR_SET_MM_START_BRK(2const), PR_SET_MM_BRK(2const),
           PR_SET_MM_ARG_START(2const), PR_SET_MM_ARG_END(2const),
           PR_SET_MM_ENV_START(2const), PR_SET_MM_ENV_END(2const),
           PR_SET_MM_EXE_FILE(2const)

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

    Linux man-pages 6.19            2026-02-08          PR_SET_MM_MAP(2const)

------------------------------------------------------------------------

Pages that refer to this page: [PR_SET_MM(2const)](../man2/PR_SET_MM.2const.html)

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
