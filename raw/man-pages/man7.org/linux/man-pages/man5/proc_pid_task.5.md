---
{"title": "proc_pid_task(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_pid_task.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_pid_task(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_pid_task(5)           File Formats Manual           proc_pid_task(5)

## [](#NAME)NAME

           /proc/pid/task/, /proc/tid/, /proc/thread-self/ - thread
           information

## [](#DESCRIPTION)DESCRIPTION

           /proc/pid/task/ (since Linux 2.6.0)
                  This is a directory that contains one subdirectory for each
                  thread in the process.  The name of each subdirectory is
                  the numerical thread ID (tid) of the thread (see
                  gettid(2)).

                  Within each of these subdirectories, there is a set of
                  files with the same names and contents as under the
                  /proc/pid directories.  For attributes that are shared by
                  all threads, the contents for each of the files under the
                  task/tid subdirectories will be the same as in the
                  corresponding file in the parent /proc/pid directory (e.g.,
                  in a multithreaded process, all of the task/tid/cwd files
                  will have the same value as the /proc/pid/cwd file in the
                  parent directory, since all of the threads in a process
                  share a working directory).  For attributes that are
                  distinct for each thread, the corresponding files under
                  task/tid may have different values (e.g., various fields in
                  each of the task/tid/status files may be different for each
                  thread), or they might not exist in /proc/pid at all.

                  In a multithreaded process, the contents of the
                  /proc/pid/task directory are not available if the main
                  thread has already terminated (typically by calling
                  pthread_exit(3)).

                  See also:

                  proc_tid_children(5).

           /proc/tid/
                  There is a numerical subdirectory for each running thread
                  that is not a thread group leader (i.e., a thread whose
                  thread ID is not the same as its process ID); the
                  subdirectory is named by the thread ID.  Each one of these
                  subdirectories contains files and subdirectories exposing
                  information about the thread with the thread ID tid.  The
                  contents of these directories are the same as the
                  corresponding /proc/pid/task/tid directories.

                  The /proc/tid subdirectories are not visible when iterating
                  through /proc with getdents(2) (and thus are not visible
                  when one uses ls(1) to view the contents of /proc).
                  However, the pathnames of these directories are visible to
                  (i.e., usable as arguments in) system calls that operate on
                  pathnames.

           /proc/thread-self/ (since Linux 3.17)
                  This directory refers to the thread accessing the /proc
                  filesystem, and is identical to the /proc/self/task/tid
                  directory named by the process thread ID (tid) of the same
                  thread.

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

    Linux man-pages 6.19            2026-02-08               proc_pid_task(5)

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
