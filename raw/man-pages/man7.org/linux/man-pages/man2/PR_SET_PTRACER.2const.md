---
{"title": "PR_SET_PTRACER(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/PR_SET_PTRACER.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_SET_PTRACER(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_SET_PTRACER(2const)                             PR_SET_PTRACER(2const)

## [](#NAME)NAME

           PR_SET_PTRACER - allow processes to ptrace(2) the calling process

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_SET_PTRACER, long pid);

## [](#DESCRIPTION)DESCRIPTION

           This is meaningful only when the Yama LSM is enabled and in mode 1
           ("restricted ptrace", visible via /proc/sys/kernel/yama/
           ptrace_scope).

           When a "ptracer process ID" is passed in pid, the caller is
           declaring that the ptracer process can ptrace(2) the calling
           process as if it were a direct process ancestor.

           Each PR_SET_PTRACER operation replaces the previous "ptracer
           process ID".

           Employing PR_SET_PTRACER with pid set to 0 clears the caller's
           "ptracer process ID".  If pid is PR_SET_PTRACER_ANY, the ptrace
           restrictions introduced by Yama are effectively disabled for the
           calling process.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL pid is not 0, PR_SET_PTRACER_ANY, nor the PID of an
                  existing process.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 3.4.

## [](#SEE_ALSO)SEE ALSO

           prctl(2)

           For further information, see the kernel source file Documentation/
           admin-guide/LSM/Yama.rst.

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

    Linux man-pages 6.19            2026-02-08         PR_SET_PTRACER(2const)

------------------------------------------------------------------------

Pages that refer to this page: [setpriv(1)](../man1/setpriv.1.html),  [prctl(2)](../man2/prctl.2.html)

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
