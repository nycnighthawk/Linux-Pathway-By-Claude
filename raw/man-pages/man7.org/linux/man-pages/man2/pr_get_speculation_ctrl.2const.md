---
{"title": "PR_GET_SPECULATION_CTRL(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pr_get_speculation_ctrl.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_GET_SPECULATION_CTRL(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_GET_SPECULATION_CTRL(2const)           PR_GET_SPECULATION_CTRL(2const)

## [](#NAME)NAME

           PR_GET_SPECULATION_CTRL - get the state of a speculation
           misfeature for the calling thread

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_GET_SPECULATION_CTRL, long misfeature, 0L, 0L, 0L);

## [](#DESCRIPTION)DESCRIPTION

           Return the state of the speculation misfeature specified in
           misfeature.

           Currently, misfeature must be one of:

           PR_SPEC_STORE_BYPASS
                  Get the state of the speculative store bypass misfeature.

           PR_SPEC_INDIRECT_BRANCH (since Linux 4.20)
                  Get the state of the indirect branch speculation
                  misfeature.

           The return value uses bits 0-4 with the following meaning:

           PR_SPEC_PRCTL
                  Mitigation can be controlled per thread by
                  PR_SET_SPECULATION_CTRL(2const).

           PR_SPEC_ENABLE
                  The speculation feature is enabled, mitigation is disabled.

           PR_SPEC_DISABLE
                  The speculation feature is disabled, mitigation is enabled.

           PR_SPEC_FORCE_DISABLE
                  Same as PR_SPEC_DISABLE but cannot be undone.

           PR_SPEC_DISABLE_NOEXEC (since Linux 5.1)
                  Same as PR_SPEC_DISABLE, but the state will be cleared on
                  execve(2).

           If all bits are 0, then the CPU is not affected by the speculation
           misfeature.

           If PR_SPEC_PRCTL is set, then per-thread control of the mitigation
           is available.  If not set, PR_SET_SPECULATION_CTRL(2const) for the
           speculation misfeature will fail.

## [](#RETURN_VALUE)RETURN VALUE

           On success, PR_GET_SPECULATION_CTRL returns the nonnegative value
           described above.  On error, -1 is returned, and errno is set to
           indicate the error.

## [](#ERRORS)ERRORS

           ENODEV The kernel or CPU does not support the requested
                  speculation misfeature.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 4.17.

## [](#SEE_ALSO)SEE ALSO

           prctl(2), PR_SET_SPECULATION_CTRL(2const)

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

    Linux man-pages 6.19            2026-02-08PR_GET_SPECULATION_CTRL(2const)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html),  [PR_SET_SPECULATION_CTRL(2const)](../man2/PR_SET_SPECULATION_CTRL.2const.html)

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
