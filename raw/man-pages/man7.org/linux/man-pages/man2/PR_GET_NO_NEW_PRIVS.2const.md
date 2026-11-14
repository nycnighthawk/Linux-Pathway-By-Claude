---
{"title": "PR_GET_NO_NEW_PRIVS(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/PR_GET_NO_NEW_PRIVS.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_GET_NO_NEW_PRIVS(2const) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [FILES](#FILES) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_GET_NO_NEW_PRIVS(2const)                   PR_GET_NO_NEW_PRIVS(2const)

## [](#NAME)NAME

           PR_GET_NO_NEW_PRIVS - get the calling thread's no_new_privs
           attribute

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_GET_NO_NEW_PRIVS, 0L, 0L, 0L, 0L);

## [](#DESCRIPTION)DESCRIPTION

           Return the value of the no_new_privs attribute for the calling
           thread.  A value of 0 indicates the regular execve(2) behavior.  A
           value of 1 indicates execve(2) will operate in the privilege-
           restricting mode described in PR_SET_NO_NEW_PRIVS(2const).

## [](#RETURN_VALUE)RETURN VALUE

           On success, PR_GET_NO_NEW_PRIVS returns the boolean value
           described above.  On error, -1 is returned, and errno is set to
           indicate the error.

## [](#FILES)FILES

           /proc/pid/status
                  Since Linux 4.10, the value of a thread's no_new_privs
                  attribute can be viewed via the NoNewPrivs field in this
                  file.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 3.5.

## [](#SEE_ALSO)SEE ALSO

           prctl(2), PR_SET_NO_NEW_PRIVS(2const)

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

    Linux man-pages 6.19            2026-02-08    PR_GET_NO_NEW_PRIVS(2const)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html),  [PR_SET_NO_NEW_PRIVS(2const)](../man2/PR_SET_NO_NEW_PRIVS.2const.html)

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
