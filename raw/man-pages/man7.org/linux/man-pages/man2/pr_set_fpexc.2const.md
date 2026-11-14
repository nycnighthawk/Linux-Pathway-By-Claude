---
{"title": "PR_SET_FPEXC(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pr_set_fpexc.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_SET_FPEXC(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_SET_FPEXC(2const)                                 PR_SET_FPEXC(2const)

## [](#NAME)NAME

           PR_SET_FPEXC - set the floating-point exception mode

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_SET_FPEXC, unsigned long mode);

## [](#DESCRIPTION)DESCRIPTION

           Set floating-point exception mode to mode, which can be one of the
           following values.

           PR_FP_EXC_SW_ENABLE
                  Use FPEXC for FP exception enables.

           PR_FP_EXC_DIV
                  Use FPEXC for floating-point divide by zero.

           PR_FP_EXC_OVF
                  Use FPEXC for floating-point overflow.

           PR_FP_EXC_UND
                  Use FPEXC for floating-point underflow.

           PR_FP_EXC_RES
                  Use FPEXC for floating-point inexact result.

           PR_FP_EXC_INV
                  Use FPEXC for floating-point invalid operation.

           PR_FP_EXC_DISABLED
                  Use FPEXC for FP exceptions disabled.

           PR_FP_EXC_NONRECOV
                  Use FPEXC for async nonrecoverable exception mode.

           PR_FP_EXC_ASYNC
                  Use FPEXC for async recoverable exception mode.

           PR_FP_EXC_PRECISE
                  Use FPEXC for precise exception mode.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL mode is not a valid value.

## [](#STANDARDS)STANDARDS

           Linux.  PowerPC only.

## [](#HISTORY)HISTORY

           Linux 2.4.21, 2.5.32.  (PowerPC)

## [](#SEE_ALSO)SEE ALSO

           prctl(2), PR_GET_FPEXC(2const)

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

    Linux man-pages 6.19            2026-02-08           PR_SET_FPEXC(2const)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html),  [PR_GET_FPEXC(2const)](../man2/PR_GET_FPEXC.2const.html)

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
