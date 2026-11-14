---
{"title": "proc_pid_mounts(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_pid_mounts.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_pid_mounts(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_pid_mounts(5)         File Formats Manual         proc_pid_mounts(5)

## [](#NAME)NAME

           /proc/pid/mounts - mounted filesystems

## [](#DESCRIPTION)DESCRIPTION

           /proc/pid/mounts (since Linux 2.4.19)
                  This file lists all the filesystems currently mounted in
                  the process's mount namespace (see mount_namespaces(7)).
                  The format of this file is documented in fstab(5).

                  Since Linux 2.6.15, this file is pollable: after opening
                  the file for reading, a change in this file (i.e., a
                  filesystem mount or unmount) causes select(2) to mark the
                  file descriptor as having an exceptional condition, and
                  poll(2) and epoll_wait(2) mark the file as having a
                  priority event (POLLPRI).  (Before Linux 2.6.30, a change
                  in this file was indicated by the file descriptor being
                  marked as readable for select(2), and being marked as
                  having an error condition for poll(2) and epoll_wait(2).)

           /proc/mounts
                  Before Linux 2.4.19, this file was a list of all the
                  filesystems currently mounted on the system.  With the
                  introduction of per-process mount namespaces in Linux
                  2.4.19 (see mount_namespaces(7)), this file became a link
                  to /proc/self/mounts, which lists the mounts of the
                  process's own mount namespace.  The format of this file is
                  documented in fstab(5).

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

    Linux man-pages 6.19            2026-02-08             proc_pid_mounts(5)

------------------------------------------------------------------------

Pages that refer to this page: [proc(5)](../man5/proc.5.html),  [proc_pid(5)](../man5/proc_pid.5.html)

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
