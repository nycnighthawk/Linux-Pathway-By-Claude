---
{"title": "PR_SET_MDWE(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/PR_SET_MDWE.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_SET_MDWE(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_SET_MDWE(2const)                                   PR_SET_MDWE(2const)

## [](#NAME)NAME

           PR_SET_MDWE - set the Memory-Deny-Write-Execute protection mask
           for the calling process

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_SET_MDWE, unsigned long mask, 0L, 0L, 0L);

## [](#DESCRIPTION)DESCRIPTION

           Set the calling process' Memory-Deny-Write-Execute protection
           mask.  Once protection bits are set, they can not be changed.

           mask must be a bit mask of:

           PR_MDWE_REFUSE_EXEC_GAIN
                  New memory mappings can't be writable and executable.  Non-
                  executable mappings can't become executable.

           PR_MDWE_NO_INHERIT  (since Linux 6.6)
                  Do not propagate MDWE protection to child processes on
                  fork(2).  Setting this bit requires setting
                  PR_MDWE_REFUSE_EXEC_GAIN too.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL mask is not a valid value.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 6.3.

## [](#SEE_ALSO)SEE ALSO

           prctl(2), PR_GET_MDWE(2const)

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

    Linux man-pages 6.19            2026-01-17            PR_SET_MDWE(2const)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html),  [PR_GET_MDWE(2const)](../man2/PR_GET_MDWE.2const.html)

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
