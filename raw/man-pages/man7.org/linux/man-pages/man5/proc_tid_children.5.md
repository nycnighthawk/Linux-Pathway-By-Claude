---
{"title": "proc_tid_children(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_tid_children.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_tid_children(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_tid_children(5)       File Formats Manual       proc_tid_children(5)

## [](#NAME)NAME

           /proc/tid/children - child tasks

## [](#DESCRIPTION)DESCRIPTION

           /proc/tid/children (since Linux 3.5)
                  A space-separated list of child tasks of this task.  Each
                  child task is represented by its TID.

                  This option is intended for use by the checkpoint-restore
                  (CRIU) system, and reliably provides a list of children
                  only if all of the child processes are stopped or frozen.
                  It does not work properly if children of the target task
                  exit while the file is being read!  Exiting children may
                  cause non-exiting children to be omitted from the list.
                  This makes this interface even more unreliable than classic
                  PID-based approaches if the inspected task and its children
                  aren't frozen, and most code should probably not use this
                  interface.

                  Until Linux 4.2, the presence of this file was governed by
                  the CONFIG_CHECKPOINT_RESTORE kernel configuration option.
                  Since Linux 4.2, it is governed by the CONFIG_PROC_CHILDREN
                  option.

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

    Linux man-pages 6.19            2026-02-08           proc_tid_children(5)

------------------------------------------------------------------------

Pages that refer to this page: [proc_pid_task(5)](../man5/proc_pid_task.5.html)

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
