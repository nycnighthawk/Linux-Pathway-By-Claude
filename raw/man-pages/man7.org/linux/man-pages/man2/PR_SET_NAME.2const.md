---
{"title": "PR_SET_NAME(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/PR_SET_NAME.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_SET_NAME(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [FILES](#FILES) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_SET_NAME(2const)                                   PR_SET_NAME(2const)

## [](#NAME)NAME

           PR_SET_NAME, PR_GET_NAME - operations on a process or thread

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_SET_NAME, const char *name);
           int prctl(PR_GET_NAME, char name[16]);

## [](#DESCRIPTION)DESCRIPTION

           PR_SET_NAME
                  Set the name of the calling thread, using the value in the
                  location pointed to by name.

                  The name can be up to 16 bytes long, including the
                  terminating null byte.  If the length of the string,
                  including the terminating null byte, exceeds 16 bytes, the
                  string is silently truncated.

           PR_GET_NAME (since Linux 2.6.11)
                  Return the name of the calling thread, in the buffer
                  pointed to by name.  The returned string will be null-
                  terminated.

           This is the same attribute that can be set via
           pthread_setname_np(3) and retrieved using pthread_getname_np(3).

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT name is an invalid address.

## [](#FILES)FILES

           /proc/self/task/tid/comm
                  The attribute is likewise accessible via this file (see
                  proc_pid_comm(5)), where tid is the thread ID of the
                  calling thread, as returned by gettid(2).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           PR_SET_NAME
                  Linux 2.6.9.

           PR_GET_NAME
                  Linux 2.6.11.

## [](#SEE_ALSO)SEE ALSO

           prctl(2), pthread_setname_np(3), pthread_getname_np(3),
           proc_pid_comm(5)

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

    Linux man-pages 6.19            2026-02-08            PR_SET_NAME(2const)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html)

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
