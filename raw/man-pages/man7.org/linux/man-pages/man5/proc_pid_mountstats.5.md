---
{"title": "proc_pid_mountstats(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_pid_mountstats.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_pid_mountstats(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_pid_mountstats(5)     File Formats Manual     proc_pid_mountstats(5)

## [](#NAME)NAME

           /proc/pid/mountstats - mount statistics

## [](#DESCRIPTION)DESCRIPTION

           /proc/pid/mountstats (since Linux 2.6.17)
                  This file exports information (statistics, configuration
                  information) about the mounts in the process's mount
                  namespace (see mount_namespaces(7)).  Lines in this file
                  have the form:

                      device /dev/sda7 mounted on /home with fstype ext3 [stats]
                      (       1      )            ( 2 )             (3 ) (  4  )

                  The fields in each line are:

                  (1)  The name of the mounted device (or "nodevice" if there
                       is no corresponding device).

                  (2)  The mount point within the filesystem tree.

                  (3)  The filesystem type.

                  (4)  Optional statistics and configuration information.
                       Currently (as at Linux 2.6.26), only NFS filesystems
                       export information via this field.

                  This file is readable only by the owner of the process.

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

    Linux man-pages 6.19            2026-02-08         proc_pid_mountstats(5)

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
