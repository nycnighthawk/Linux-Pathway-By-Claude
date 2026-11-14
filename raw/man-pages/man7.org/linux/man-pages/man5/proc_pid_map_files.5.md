---
{"title": "proc_pid_map_files(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_pid_map_files.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_pid_map_files(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_pid_map_files(5)      File Formats Manual      proc_pid_map_files(5)

## [](#NAME)NAME

           /proc/pid/map_files/ - memory-mapped files

## [](#DESCRIPTION)DESCRIPTION

           /proc/pid/map_files/ (since Linux 3.3)
                  This subdirectory contains entries corresponding to memory-
                  mapped files (see mmap(2)).  Entries are named by memory
                  region start and end address pair (expressed as hexadecimal
                  numbers), and are symbolic links to the mapped files
                  themselves.  Here is an example, with the output wrapped
                  and reformatted to fit on an 80-column display:

                      # ls -l /proc/self/map_files/
                      lr-------- 1 root root 64 Apr 16 21:31
                                  3252e00000-3252e20000 -> /usr/lib64/ld-2.15.so
                      ...

                  Although these entries are present for memory regions that
                  were mapped with the MAP_FILE flag, the way anonymous
                  shared memory (regions created with the MAP_ANON |
                  MAP_SHARED flags) is implemented in Linux means that such
                  regions also appear on this directory.  Here is an example
                  where the target file is the deleted /dev/zero one:

                      lrw------- 1 root root 64 Apr 16 21:33
                                  7fc075d2f000-7fc075e6f000 -> /dev/zero (deleted)

                  Permission to access this file is governed by a ptrace
                  access mode PTRACE_MODE_READ_FSCREDS check; see ptrace(2).

                  Until Linux 4.3, this directory appeared only if the
                  CONFIG_CHECKPOINT_RESTORE kernel configuration option was
                  enabled.

                  Capabilities are required to read the contents of the
                  symbolic links in this directory: before Linux 5.9, the
                  reading process requires CAP_SYS_ADMIN in the initial user
                  namespace; since Linux 5.9, the reading process must have
                  either CAP_SYS_ADMIN or CAP_CHECKPOINT_RESTORE in the
                  initial (i.e., root) user namespace.

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

    Linux man-pages 6.19            2026-02-08          proc_pid_map_files(5)

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
