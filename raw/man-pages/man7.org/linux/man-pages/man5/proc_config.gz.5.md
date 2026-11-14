---
{"title": "proc_config.gz(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_config.gz.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_config.gz(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_config.gz(5)          File Formats Manual          proc_config.gz(5)

## [](#NAME)NAME

           /proc/config.gz - kernel build configuration

## [](#DESCRIPTION)DESCRIPTION

           /proc/config.gz (since Linux 2.6)
                  This file exposes the configuration options that were used
                  to build the currently running kernel, in the same format
                  as they would be shown in the .config file that resulted
                  when configuring the kernel (using make xconfig, make
                  config, or similar).  The file contents are compressed;
                  view or search them using zcat(1) and zgrep(1).  As long as
                  no changes have been made to the following file, the
                  contents of /proc/config.gz are the same as those provided
                  by:

                      cat /lib/modules/$(uname -r)/build/.config

                  /proc/config.gz is provided only if the kernel is
                  configured with CONFIG_IKCONFIG_PROC.

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

    Linux man-pages 6.19            2026-02-08              proc_config.gz(5)

------------------------------------------------------------------------

Pages that refer to this page: [proc(5)](../man5/proc.5.html)

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
