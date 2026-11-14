---
{"title": "PR_SET_CHILD_SUBREAPER(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/PR_SET_CHILD_SUBREAPER.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_SET_CHILD_SUBREAPER(2const) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_SET_CHILD_SUBREAPER(2const)             PR_SET_CHILD_SUBREAPER(2const)

## [](#NAME)NAME

           PR_SET_CHILD_SUBREAPER - set/unset the "child subreaper" attribute
           of the calling process

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_SET_CHILD_SUBREAPER, long set);

## [](#DESCRIPTION)DESCRIPTION

           If set is nonzero, set the "child subreaper" attribute of the
           calling process; if set is zero, unset the attribute.

           A subreaper fulfills the role of init(1) for its descendant
           processes.  When a process becomes orphaned (i.e., its immediate
           parent terminates), then that process will be reparented to the
           nearest still living ancestor subreaper.  Subsequently, calls to
           getppid(2) in the orphaned process will now return the PID of the
           subreaper process, and when the orphan terminates, it is the
           subreaper process that will receive a SIGCHLD signal and will be
           able to wait(2) on the process to discover its termination status.

           The setting of the "child subreaper" attribute is not inherited by
           children created by fork(2) and clone(2).  The setting is
           preserved across execve(2).

           Establishing a subreaper process is useful in session management
           frameworks where a hierarchical group of processes is managed by a
           subreaper process that needs to be informed when one of the
           processes—for example, a double-forked daemon—terminates (perhaps
           so that it can restart that process).  Some init(1) frameworks
           (e.g., systemd(1)) employ a subreaper process for similar reasons.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 3.4.

## [](#SEE_ALSO)SEE ALSO

           prctl(2), PR_GET_CHILD_SUBREAPER(2const)

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

    Linux man-pages 6.19            2026-02-08 PR_SET_CHILD_SUBREAPER(2const)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html),  [PR_GET_CHILD_SUBREAPER(2const)](../man2/PR_GET_CHILD_SUBREAPER.2const.html),  [PR_SET_PDEATHSIG(2const)](../man2/PR_SET_PDEATHSIG.2const.html)

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
