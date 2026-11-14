---
{"title": "proc_pid(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_pid.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_pid(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_pid(5)                File Formats Manual                proc_pid(5)

## [](#NAME)NAME

           /proc/pid/, /proc/self/ - process information

## [](#DESCRIPTION)DESCRIPTION

           /proc/pid/
                  There is a numerical subdirectory for each running process;
                  the subdirectory is named by the process ID.  Each
                  /proc/pid subdirectory contains the pseudo-files and
                  directories described below.

                  The files inside each /proc/pid directory are normally
                  owned by the effective user and effective group ID of the
                  process.  However, as a security measure, the ownership is
                  made root:root if the process's "dumpable" attribute is set
                  to a value other than 1.

                  Before Linux 4.11, root:root meant the "global" root user
                  ID and group ID (i.e., UID 0 and GID 0 in the initial user
                  namespace).  Since Linux 4.11, if when the last time the
                  process called execve(2), it was in a noninitial user
                  namespace that has a valid mapping for user (group) ID 0
                  inside the namespace, then the user (group) ownership of
                  the files under /proc/pid is instead made the same as the
                  root user (group) ID of the namespace.  This means that
                  inside a container, things work as expected for the
                  container "root" user.

                  The process's "dumpable" attribute may change for the
                  following reasons:

                  •  The attribute was explicitly set via the prctl(2)
                     PR_SET_DUMPABLE operation.

                  •  The attribute was reset to the value in the file
                     /proc/sys/fs/suid_dumpable (described below), for the
                     reasons described in prctl(2).

                  Resetting the "dumpable" attribute to 1 reverts the
                  ownership of the /proc/pid/* files to the process's
                  effective UID and GID.  Note, however, that if the
                  effective UID or GID is subsequently modified, then the
                  "dumpable" attribute may be reset, as described in
                  prctl(2).  Therefore, it may be desirable to reset the
                  "dumpable" attribute after making any desired changes to
                  the process's effective UID or GID.

                  See also:

                  proc_pid_attr(5)
                  proc_pid_autogroup(5)
                  proc_pid_auxv(5)
                  proc_pid_cgroup(5)
                  proc_pid_clear_refs(5)
                  proc_pid_cmdline(5)
                  proc_pid_comm(5)
                  proc_pid_coredump_filter(5)
                  proc_pid_cpuset(5)
                  proc_pid_cwd(5)
                  proc_pid_environ(5)
                  proc_pid_exe(5)
                  proc_pid_fd(5)
                  proc_pid_fdinfo(5)
                  proc_pid_gid_map(5)
                  proc_pid_io(5)
                  proc_pid_limits(5)
                  proc_pid_map_files(5)
                  proc_pid_maps(5)
                  proc_pid_mem(5)
                  proc_pid_mountinfo(5)
                  proc_pid_mounts(5)
                  proc_pid_mountstats(5)
                  proc_pid_net(5)
                  proc_pid_ns(5)
                  proc_pid_numa_maps(5)
                  proc_pid_oom_adj(5)
                  proc_pid_oom_score(5)
                  proc_pid_oom_score_adj(5)
                  proc_pid_pagemap(5)
                  proc_pid_personality(5)
                  proc_pid_projid_map(5)
                  proc_pid_root(5)
                  proc_pid_seccomp(5)
                  proc_pid_setgroups(5)
                  proc_pid_smaps(5)
                  proc_pid_stack(5)
                  proc_pid_stat(5)
                  proc_pid_statm(5)
                  proc_pid_status(5)
                  proc_pid_syscall(5)
                  proc_pid_task(5)
                  proc_pid_timers(5)
                  proc_pid_timerslack_ns(5)
                  proc_pid_uid_map(5)
                  proc_pid_wchan(5)

           /proc/self/
                  This directory refers to the process accessing the /proc
                  filesystem, and is identical to the /proc directory named
                  by the process ID of the same process.

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

    Linux man-pages 6.19            2026-03-18                    proc_pid(5)

------------------------------------------------------------------------

Pages that refer to this page: [PR_SET_DUMPABLE(2const)](../man2/PR_SET_DUMPABLE.2const.html),  [proc(5)](../man5/proc.5.html)

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
