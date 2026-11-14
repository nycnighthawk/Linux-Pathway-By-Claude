---
{"title": "proc_filesystems(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_filesystems.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_filesystems(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_filesystems(5)        File Formats Manual        proc_filesystems(5)

## [](#NAME)NAME

           /proc/filesystems - supported filesystems

## [](#DESCRIPTION)DESCRIPTION

           /proc/filesystems
                  A text listing of the filesystems which are supported by
                  the kernel, namely filesystems which were compiled into the
                  kernel or whose kernel modules are currently loaded.  (See
                  also filesystems(5).)  If a filesystem is marked with
                  "nodev", this means that it does not require a block device
                  to be mounted (e.g., virtual filesystem, network
                  filesystem).

                  Incidentally, this file may be used by mount(8) when no
                  filesystem is specified and it didn't manage to determine
                  the filesystem type.  Then filesystems contained in this
                  file are tried (excepted those that are marked with
                  "nodev").

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

    Linux man-pages 6.19            2026-02-08            proc_filesystems(5)

------------------------------------------------------------------------

Pages that refer to this page: [fsopen(2)](../man2/fsopen.2.html),  [proc(5)](../man5/proc.5.html)

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
