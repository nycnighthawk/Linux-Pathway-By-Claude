---
{"title": "sched_setscheduler(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/sched_getscheduler.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sched_setscheduler(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sched_setscheduler(2)      System Calls Manual      sched_setscheduler(2)

## [](#NAME)NAME

           sched_setscheduler, sched_getscheduler - set and get scheduling
           policy/parameters

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sched.h>

           int sched_setscheduler(pid_t pid, int policy,
                                  const struct sched_param *param);
           int sched_getscheduler(pid_t pid);

## [](#DESCRIPTION)DESCRIPTION

           The sched_setscheduler() system call sets both the scheduling
           policy and parameters for the thread whose ID is specified in pid.
           If pid equals zero, the scheduling policy and parameters of the
           calling thread will be set.

           The scheduling parameters are specified in the param argument,
           which is a pointer to a structure of the following form:

               struct sched_param {
                   ...
                   int sched_priority;
                   ...
               };

           In the current implementation, the structure contains only one
           field, sched_priority.  The interpretation of param depends on the
           selected policy.

           Currently, Linux supports the following "normal" (i.e., non-real-
           time) scheduling policies as values that may be specified in
           policy:

           SCHED_OTHER
                  the standard round-robin time-sharing policy;

           SCHED_BATCH
                  for "batch" style execution of processes; and

           SCHED_IDLE
                  for running very low priority background jobs.

           For each of the above policies, param->sched_priority must be 0.

           Various "real-time" policies are also supported, for special time-
           critical applications that need precise control over the way in
           which runnable threads are selected for execution.  For the rules
           governing when a process may use these policies, see sched(7).
           The real-time policies that may be specified in policy are:

           SCHED_FIFO
                  a first-in, first-out policy; and

           SCHED_RR
                  a round-robin policy.

           For each of the above policies, param->sched_priority specifies a
           scheduling priority for the thread.  This is a number in the range
           returned by calling sched_get_priority_min(2) and
           sched_get_priority_max(2) with the specified policy.  On Linux,
           these system calls return, respectively, 1 and 99.

           Since Linux 2.6.32, the SCHED_RESET_ON_FORK flag can be ORed in
           policy when calling sched_setscheduler().  As a result of
           including this flag, children created by fork(2) do not inherit
           privileged scheduling policies.  See sched(7) for details.

           sched_getscheduler() returns the current scheduling policy of the
           thread identified by pid.  If pid equals zero, the policy of the
           calling thread will be retrieved.

## [](#RETURN_VALUE)RETURN VALUE

           On success, sched_setscheduler() returns zero.  On success,
           sched_getscheduler() returns the policy for the thread (a
           nonnegative integer).  On error, both calls return -1, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL Invalid arguments: pid is negative or param is NULL.

           EINVAL (sched_setscheduler()) policy is not one of the recognized
                  policies.

           EINVAL (sched_setscheduler()) param does not make sense for the
                  specified policy.

           EPERM  The calling thread does not have appropriate privileges.

           ESRCH  The thread whose ID is pid could not be found.

## [](#VERSIONS)VERSIONS

           POSIX.1 does not detail the permissions that an unprivileged
           thread requires in order to call sched_setscheduler(), and details
           vary across systems.  For example, the Solaris 7 manual page says
           that the real or effective user ID of the caller must match the
           real user ID or the save set-user-ID of the target.

           The scheduling policy and parameters are in fact per-thread
           attributes on Linux.  The value returned from a call to gettid(2)
           can be passed in the argument pid.  Specifying pid as 0 will
           operate on the attributes of the calling thread, and passing the
           value returned from a call to getpid(2) will operate on the
           attributes of the main thread of the thread group.  (If you are
           using the POSIX threads API, then use pthread_setschedparam(3),
           pthread_getschedparam(3), and pthread_setschedprio(3), instead of
           the sched_*(2) system calls.)

## [](#STANDARDS)STANDARDS

           POSIX.1-2024 (but see BUGS below).

           SCHED_BATCH and SCHED_IDLE are Linux-specific.

## [](#HISTORY)HISTORY

           POSIX.1-2001.

## [](#NOTES)NOTES

           Further details of the semantics of all of the above "normal" and
           "real-time" scheduling policies can be found in the sched(7)
           manual page.  That page also describes an additional policy,
           SCHED_DEADLINE, which is settable only via sched_setattr(2).

           POSIX systems on which sched_setscheduler() and
           sched_getscheduler() are available define
           _POSIX_PRIORITY_SCHEDULING in <unistd.h>.

## [](#BUGS)BUGS

           POSIX.1 says that on success, sched_setscheduler() should return
           the previous scheduling policy.  Linux sched_setscheduler() does
           not conform to this requirement, since it always returns 0 on
           success.

## [](#SEE_ALSO)SEE ALSO

           chrt(1), nice(2), sched_get_priority_max(2),
           sched_get_priority_min(2), sched_getaffinity(2), sched_getattr(2),
           sched_getparam(2), sched_rr_get_interval(2), sched_setaffinity(2),
           sched_setattr(2), sched_setparam(2), sched_yield(2),
           setpriority(2), capabilities(7), cpuset(7), sched(7)

## [](#COLOPHON)COLOPHON

           This  page  is  part  of the man-pages (Linux kernel and C library
           user-space interface documentation)  project.   Information  about
           the       project       can       be       found       at       
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug  report
           for            this           manual           page,           see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was  obtained  from  the  tarball  man-pages-6.19.tar.gz
           fetched                                                       from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩     on
           2026-09-09.   If  you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more  up-
           to-date   source   for  the  page,  or  you  have  corrections  or
           improvements to the information in this  COLOPHON  (which  is  not
           part   of   the   original   manual   page),   send   a   mail  to
           man-pages@man7.org

    Linux man-pages 6.19            2026-02-08          sched_setscheduler(2)

------------------------------------------------------------------------

Pages that refer to this page: [chrt(1)](../man1/chrt.1.html),  [uclampset(1)](../man1/uclampset.1.html),  [getrlimit(2)](../man2/getrlimit.2.html),  [gettid(2)](../man2/gettid.2.html),  [mlock(2)](../man2/mlock.2.html),  [nanosleep(2)](../man2/nanosleep.2.html),  [PR_SET_TIMERSLACK(2const)](../man2/PR_SET_TIMERSLACK.2const.html),  [sched_get_priority_max(2)](../man2/sched_get_priority_max.2.html),  [sched_setaffinity(2)](../man2/sched_setaffinity.2.html),  [sched_setattr(2)](../man2/sched_setattr.2.html),  [sched_setparam(2)](../man2/sched_setparam.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [id_t(3type)](../man3/id_t.3type.html),  [posix_spawn(3)](../man3/posix_spawn.3.html),  [proc_pid_stat(5)](../man5/proc_pid_stat.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [capabilities(7)](../man7/capabilities.7.html),  [cpuset(7)](../man7/cpuset.7.html),  [credentials(7)](../man7/credentials.7.html),  [sched(7)](../man7/sched.7.html)

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
