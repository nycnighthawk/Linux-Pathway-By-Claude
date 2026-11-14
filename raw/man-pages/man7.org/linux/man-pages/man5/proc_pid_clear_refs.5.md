---
{"title": "proc_pid_clear_refs(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_pid_clear_refs.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_pid_clear_refs(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_pid_clear_refs(5)     File Formats Manual     proc_pid_clear_refs(5)

## [](#NAME)NAME

           /proc/pid/clear_refs - reset the PG_Referenced and ACCESSED/YOUNG
           bits

## [](#DESCRIPTION)DESCRIPTION

           /proc/pid/clear_refs (since Linux 2.6.22)

                  This is a write-only file, writable only by owner of the
                  process.

                  The following values may be written to the file:

                  1 (since Linux 2.6.22)
                         Reset the PG_Referenced and ACCESSED/YOUNG bits for
                         all the pages associated with the process.  (Before
                         Linux 2.6.32, writing any nonzero value to this file
                         had this effect.)

                  2 (since Linux 2.6.32)
                         Reset the PG_Referenced and ACCESSED/YOUNG bits for
                         all anonymous pages associated with the process.

                  3 (since Linux 2.6.32)
                         Reset the PG_Referenced and ACCESSED/YOUNG bits for
                         all file-mapped pages associated with the process.

                  Clearing the PG_Referenced and ACCESSED/YOUNG bits provides
                  a method to measure approximately how much memory a process
                  is using.  One first inspects the values in the
                  "Referenced" fields for the VMAs shown in /proc/pid/smaps
                  to get an idea of the memory footprint of the process.  One
                  then clears the PG_Referenced and ACCESSED/YOUNG bits and,
                  after some measured time interval, once again inspects the
                  values in the "Referenced" fields to get an idea of the
                  change in memory footprint of the process during the
                  measured interval.  If one is interested only in inspecting
                  the selected mapping types, then the value 2 or 3 can be
                  used instead of 1.

                  Further values can be written to affect different
                  properties:

                  4 (since Linux 3.11)
                         Clear the soft-dirty bit for all the pages
                         associated with the process.  This is used (in
                         conjunction with /proc/pid/pagemap) by the check-
                         point restore system to discover which pages of a
                         process have been dirtied since the file
                         /proc/pid/clear_refs was written to.

                  5 (since Linux 4.0)
                         Reset the peak resident set size ("high water mark")
                         to the process's current resident set size value.

                  Writing any value to /proc/pid/clear_refs other than those
                  listed above has no effect.

                  The /proc/pid/clear_refs file is present only if the
                  CONFIG_PROC_PAGE_MONITOR kernel configuration option is
                  enabled.

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

    Linux man-pages 6.19            2026-02-08         proc_pid_clear_refs(5)

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
