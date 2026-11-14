---
{"title": "proc_pid_timerslack_ns(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_pid_timerslack_ns.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_pid_timerslack_ns(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_pid_timerslack_ns(5)  File Formats Manual  proc_pid_timerslack_ns(5)

## [](#NAME)NAME

           /proc/pid/timerslack_ns - timer slack in nanoseconds

## [](#DESCRIPTION)DESCRIPTION

           /proc/pid/timerslack_ns (since Linux 4.6)
                  This file exposes the process's "current" timer slack
                  value, expressed in nanoseconds.  The file is writable,
                  allowing the process's timer slack value to be changed.
                  Writing 0 to this file resets the "current" timer slack to
                  the "default" timer slack value.  For further details, see
                  the discussion of PR_SET_TIMERSLACK in prctl(2).

                  Initially, permission to access this file was governed by a
                  ptrace access mode PTRACE_MODE_ATTACH_FSCREDS check (see
                  ptrace(2)).  However, this was subsequently deemed too
                  strict a requirement (and had the side effect that
                  requiring a process to have the CAP_SYS_PTRACE capability
                  would also allow it to view and change any process's
                  memory).  Therefore, since Linux 4.9, only the (weaker)
                  CAP_SYS_NICE capability is required to access this file.

## [](#SEE_ALSO)SEE ALSO

           proc(5)

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

    Linux man-pages 6.19            2026-02-08      proc_pid_timerslack_ns(5)

------------------------------------------------------------------------

Pages that refer to this page: [PR_GET_TIMERSLACK(2const)](../man2/PR_GET_TIMERSLACK.2const.html),  [PR_SET_TIMERSLACK(2const)](../man2/PR_SET_TIMERSLACK.2const.html),  [proc_pid(5)](../man5/proc_pid.5.html)

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
