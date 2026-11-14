---
{"title": "sched_rr_get_interval(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/sched_rr_get_interval.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sched_rr_get_interval(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sched_rr_get_interval(2)   System Calls Manual   sched_rr_get_interval(2)

## [](#NAME)NAME

           sched_rr_get_interval - get the SCHED_RR interval for the named
           process

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sched.h>

           int sched_rr_get_interval(pid_t pid, struct timespec *tp);

## [](#DESCRIPTION)DESCRIPTION

           sched_rr_get_interval() writes into the timespec(3) structure
           pointed to by tp the round-robin time quantum for the process
           identified by pid.  The specified process should be running under
           the SCHED_RR scheduling policy.

           If pid is zero, the time quantum for the calling process is
           written into *tp.

## [](#RETURN_VALUE)RETURN VALUE

           On success, sched_rr_get_interval() returns 0.  On error, -1 is
           returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT Problem with copying information to user space.

           EINVAL Invalid pid.

           ENOSYS The system call is not yet implemented (only on rather old
                  kernels).

           ESRCH  Could not find a process with the ID pid.

## [](#VERSIONS)VERSIONS

       Linux
           Linux 3.9 added a new mechanism for adjusting (and viewing) the
           SCHED_RR quantum: the /proc/sys/kernel/sched_rr_timeslice_ms file
           exposes the quantum as a millisecond value, whose default is 100.
           Writing 0 to this file resets the quantum to the default value.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001.

       Linux
           POSIX does not specify any mechanism for controlling the size of
           the round-robin time quantum.  Older Linux kernels provide a
           (nonportable) method of doing this.  The quantum can be controlled
           by adjusting the process's nice value (see setpriority(2)).
           Assigning a negative (i.e., high) nice value results in a longer
           quantum; assigning a positive (i.e., low) nice value results in a
           shorter quantum.  The default quantum is 0.1 seconds; the degree
           to which changing the nice value affects the quantum has varied
           somewhat across kernel versions.  This method of adjusting the
           quantum was removed starting with Linux 2.6.24.

## [](#NOTES)NOTES

           POSIX systems on which sched_rr_get_interval() is available define
           _POSIX_PRIORITY_SCHEDULING in <unistd.h>.

## [](#SEE_ALSO)SEE ALSO

           timespec(3), sched(7)

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

    Linux man-pages 6.19            2026-02-08       sched_rr_get_interval(2)

------------------------------------------------------------------------

Pages that refer to this page: [sched_setattr(2)](../man2/sched_setattr.2.html),  [sched_setscheduler(2)](../man2/sched_setscheduler.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [proc_sys_kernel(5)](../man5/proc_sys_kernel.5.html),  [sched(7)](../man7/sched.7.html)

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
