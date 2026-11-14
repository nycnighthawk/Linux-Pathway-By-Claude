---
{"title": "proc_pid_cwd(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_pid_cwd.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_pid_cwd(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_pid_cwd(5)            File Formats Manual            proc_pid_cwd(5)

## [](#NAME)NAME

           /proc/pid/cwd - symbolic link to current working directory

## [](#DESCRIPTION)DESCRIPTION

           /proc/pid/cwd
                  This is a symbolic link to the current working directory of
                  the process.  To find out the current working directory of
                  process 20, for instance, you can do this:

                      $ cd /proc/20/cwd; pwd -P

                  In a multithreaded process, the contents of this symbolic
                  link are not available if the main thread has already
                  terminated (typically by calling pthread_exit(3)).

                  Permission to dereference or read (readlink(2)) this
                  symbolic link is governed by a ptrace access mode
                  PTRACE_MODE_READ_FSCREDS check; see ptrace(2).

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

    Linux man-pages 6.19            2026-02-08                proc_pid_cwd(5)

------------------------------------------------------------------------

Pages that refer to this page: [proc_pid(5)](../man5/proc_pid.5.html)

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
