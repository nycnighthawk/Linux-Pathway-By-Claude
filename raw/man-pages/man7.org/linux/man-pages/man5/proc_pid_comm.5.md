---
{"title": "proc_pid_comm(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_pid_comm.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_pid_comm(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_pid_comm(5)           File Formats Manual           proc_pid_comm(5)

## [](#NAME)NAME

           /proc/pid/comm - command name

## [](#DESCRIPTION)DESCRIPTION

           /proc/pid/comm (since Linux 2.6.33)
                  This file exposes the process's comm value—that is, the
                  command name associated with the process.  Different
                  threads in the same process may have different comm values,
                  accessible via /proc/pid/task/tid/comm.  A thread may
                  modify its comm value, or that of any of other thread in
                  the same thread group (see the discussion of CLONE_THREAD
                  in clone(2)), by writing to the file
                  /proc/self/task/tid/comm.  Strings longer than
                  TASK_COMM_LEN (16) characters (including the terminating
                  null byte) are silently truncated.

                  This file provides a superset of the prctl(2) PR_SET_NAME
                  and PR_GET_NAME operations, and is employed by
                  pthread_setname_np(3) when used to rename threads other
                  than the caller.  The value in this file is used for the %e
                  specifier in /proc/sys/kernel/core_pattern; see core(5).

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

    Linux man-pages 6.19            2026-02-08               proc_pid_comm(5)

------------------------------------------------------------------------

Pages that refer to this page: [PR_SET_NAME(2const)](../man2/PR_SET_NAME.2const.html),  [proc_pid(5)](../man5/proc_pid.5.html)

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
