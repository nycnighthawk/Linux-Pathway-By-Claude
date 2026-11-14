---
{"title": "sched_setparam(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/sched_setparam.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sched_setparam(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sched_setparam(2)          System Calls Manual          sched_setparam(2)

## [](#NAME)NAME

           sched_setparam, sched_getparam - set and get scheduling parameters

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sched.h>

           int sched_setparam(pid_t pid, const struct sched_param *param);
           int sched_getparam(pid_t pid, struct sched_param *param);

           struct sched_param {
               ...
               int sched_priority;
               ...
           };

## [](#DESCRIPTION)DESCRIPTION

           sched_setparam() sets the scheduling parameters associated with
           the scheduling policy for the thread whose thread ID is specified
           in pid.  If pid is zero, then the parameters of the calling thread
           are set.  The interpretation of the argument param depends on the
           scheduling policy of the thread identified by pid.  See sched(7)
           for a description of the scheduling policies supported under
           Linux.

           sched_getparam() retrieves the scheduling parameters for the
           thread identified by pid.  If pid is zero, then the parameters of
           the calling thread are retrieved.

           sched_setparam() checks the validity of param for the scheduling
           policy of the thread.  The value param->sched_priority must lie
           within the range given by sched_get_priority_min(2) and
           sched_get_priority_max(2).

           For a discussion of the privileges and resource limits related to
           scheduling priority and policy, see sched(7).

           POSIX systems on which sched_setparam() and sched_getparam() are
           available define _POSIX_PRIORITY_SCHEDULING in <unistd.h>.

## [](#RETURN_VALUE)RETURN VALUE

           On success, sched_setparam() and sched_getparam() return 0.  On
           error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL Invalid arguments: param is NULL or pid is negative

           EINVAL (sched_setparam()) The argument param does not make sense
                  for the current scheduling policy.

           EPERM  (sched_setparam()) The caller does not have appropriate
                  privileges (Linux: does not have the CAP_SYS_NICE
                  capability).

           ESRCH  The thread whose ID is pid could not be found.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001.

## [](#SEE_ALSO)SEE ALSO

           getpriority(2), gettid(2), nice(2), sched_get_priority_max(2),
           sched_get_priority_min(2), sched_getaffinity(2),
           sched_getscheduler(2), sched_setaffinity(2), sched_setattr(2),
           sched_setscheduler(2), setpriority(2), capabilities(7), sched(7)

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

    Linux man-pages 6.19            2026-02-08              sched_setparam(2)

------------------------------------------------------------------------

Pages that refer to this page: [getrlimit(2)](../man2/getrlimit.2.html),  [gettid(2)](../man2/gettid.2.html),  [sched_get_priority_max(2)](../man2/sched_get_priority_max.2.html),  [sched_setattr(2)](../man2/sched_setattr.2.html),  [sched_setscheduler(2)](../man2/sched_setscheduler.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [posix_spawn(3)](../man3/posix_spawn.3.html),  [capabilities(7)](../man7/capabilities.7.html),  [credentials(7)](../man7/credentials.7.html),  [sched(7)](../man7/sched.7.html)

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
