---
{"title": "PR_CAP_AMBIENT(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/PR_CAP_AMBIENT.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_CAP_AMBIENT(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_CAP_AMBIENT(2const)                             PR_CAP_AMBIENT(2const)

## [](#NAME)NAME

           PR_CAP_AMBIENT - read or change the ambient capability set of the
           calling thread

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_CAP_AMBIENT, long op, ...);

## [](#DESCRIPTION)DESCRIPTION

           Reads or changes the ambient capability set of the calling thread,
           according to the value of op, which must be one of the following:

           PR_CAP_AMBIENT_RAISE
           PR_CAP_AMBIENT_LOWER
           PR_CAP_AMBIENT_IS_SET
           PR_CAP_AMBIENT_CLEAR_ALL

## [](#RETURN_VALUE)RETURN VALUE

           On success, a nonnegative value is returned.  On error, -1 is
           returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL op is not a valid value.

## [](#VERSIONS)VERSIONS

           Higher-level interfaces layered on top of the above operations are
           provided in the libcap(3) library in the form of
           cap_get_ambient(3), cap_set_ambient(3), and cap_reset_ambient(3).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 4.3.

## [](#SEE_ALSO)SEE ALSO

           prctl(2), PR_CAP_AMBIENT_RAISE(2const),
           PR_CAP_AMBIENT_LOWER(2const), PR_CAP_AMBIENT_IS_SET(2const),
           PR_CAP_AMBIENT_CLEAR_ALL(2const), libcap(3), cap_get_ambient(3),
           cap_set_ambient(3), cap_reset_ambient(3)

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

    Linux man-pages 6.19            2026-02-08         PR_CAP_AMBIENT(2const)

------------------------------------------------------------------------

Pages that refer to this page: [PR_CAP_AMBIENT_CLEAR_ALL(2const)](../man2/PR_CAP_AMBIENT_CLEAR_ALL.2const.html),  [PR_CAP_AMBIENT_IS_SET(2const)](../man2/PR_CAP_AMBIENT_IS_SET.2const.html),  [PR_CAP_AMBIENT_LOWER(2const)](../man2/PR_CAP_AMBIENT_LOWER.2const.html),  [PR_CAP_AMBIENT_RAISE(2const)](../man2/PR_CAP_AMBIENT_RAISE.2const.html),  [prctl(2)](../man2/prctl.2.html)

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
