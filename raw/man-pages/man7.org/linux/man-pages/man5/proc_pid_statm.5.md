---
{"title": "proc_pid_statm(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_pid_statm.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_pid_statm(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_pid_statm(5)          File Formats Manual          proc_pid_statm(5)

## [](#NAME)NAME

           /proc/pid/statm - memory usage information

## [](#DESCRIPTION)DESCRIPTION

           /proc/pid/statm
                  Provides information about memory usage, measured in pages.
                  The columns are:

                      size       (1) total program size
                                 (same as VmSize in /proc/pid/status)
                      resident   (2) resident set size
                                 (inaccurate; same as VmRSS in /proc/pid/status)
                      shared     (3) number of resident shared pages
                                 (i.e., backed by a file)
                                 (inaccurate; same as RssFile+RssShmem in
                                 /proc/pid/status)
                      text       (4) text (code)
                      lib        (5) library (unused since Linux 2.6; always 0)
                      data       (6) data + stack
                      dt         (7) dirty pages (unused since Linux 2.6; always 0)

                  Some of these values are inaccurate because of a kernel-
                  internal scalability optimization.  If accurate values are
                  required, use /proc/pid/smaps or /proc/pid/smaps_rollup
                  instead, which are much slower but provide accurate,
                  detailed information.

## [](#SEE_ALSO)SEE ALSO

           proc(5), proc_pid_status(5)

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

    Linux man-pages 6.19            2026-02-08              proc_pid_statm(5)

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
