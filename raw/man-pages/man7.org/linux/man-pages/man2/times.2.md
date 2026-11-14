---
{"title": "times(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/times.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# times(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    times(2)                   System Calls Manual                   times(2)

## [](#NAME)NAME

           times - get process times

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/times.h>

           clock_t times(struct tms *buf);

## [](#DESCRIPTION)DESCRIPTION

           times() stores the current process times in the struct tms that
           buf points to.  The struct tms is as defined in <sys/times.h>:

               struct tms {
                   clock_t tms_utime;  /* user time */
                   clock_t tms_stime;  /* system time */
                   clock_t tms_cutime; /* user time of children */
                   clock_t tms_cstime; /* system time of children */
               };

           The tms_utime field contains the CPU time spent executing
           instructions of the calling process.  The tms_stime field contains
           the CPU time spent executing inside the kernel while performing
           tasks on behalf of the calling process.

           The tms_cutime field contains the sum of the tms_utime and
           tms_cutime values for all waited-for terminated children.  The
           tms_cstime field contains the sum of the tms_stime and tms_cstime
           values for all waited-for terminated children.

           Times for terminated children (and their descendants) are added in
           at the moment wait(2) or waitpid(2) returns their process ID.  In
           particular, times of grandchildren that the children did not wait
           for are never seen.

           All times reported are in clock ticks.

## [](#RETURN_VALUE)RETURN VALUE

           times() returns the number of clock ticks that have elapsed since
           an arbitrary point in the past.  The return value may overflow the
           possible range of type clock_t.  On error, (clock_t) -1 is
           returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT tms points outside the process's address space.

## [](#VERSIONS)VERSIONS

           On Linux, the buf argument can be specified as NULL, with the
           result that times() just returns a function result.  However,
           POSIX does not specify this behavior, and most other UNIX
           implementations require a non-NULL value for buf.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001, SVr4, 4.3BSD.

           In POSIX.1-1996 the symbol CLK_TCK (defined in <time.h>) is
           mentioned as obsolescent.  It is obsolete now.

           Before Linux 2.6.9, if the disposition of SIGCHLD is set to
           SIG_IGN, then the times of terminated children are automatically
           included in the tms_cstime and tms_cutime fields, although
           POSIX.1-2001 says that this should happen only if the calling
           process wait(2)s on its children.  This nonconformance is
           rectified in Linux 2.6.9 and later.

           On Linux, the “arbitrary point in the past” from which the return
           value of times() is measured has varied across kernel versions.
           On Linux 2.4 and earlier, this point is the moment the system was
           booted.  Since Linux 2.6, this point is (2^32/HZ) - 300 seconds
           before system boot time.  This variability across kernel versions
           (and across UNIX implementations), combined with the fact that the
           returned value may overflow the range of clock_t, means that a
           portable application would be wise to avoid using this value.  To
           measure changes in elapsed time, use clock_gettime(2) instead.

           SVr1-3 returns long and the struct members are of type time_t
           although they store clock ticks, not seconds since the Epoch.  V7
           used long for the struct members, because it had no type time_t
           yet.

## [](#NOTES)NOTES

           The number of clock ticks per second can be obtained using:

               sysconf(_SC_CLK_TCK);

           Note that clock(3) also returns a value of type clock_t, but this
           value is measured in units of CLOCKS_PER_SEC, not the clock ticks
           used by times().

## [](#BUGS)BUGS

           A limitation of the Linux system call conventions on some
           architectures (notably i386) means that on Linux 2.6 there is a
           small time window (41 seconds) soon after boot when times() can
           return -1, falsely indicating that an error occurred.  The same
           problem can occur when the return value wraps past the maximum
           value that can be stored in clock_t.

## [](#SEE_ALSO)SEE ALSO

           time(1), getrusage(2), wait(2), clock(3), sysconf(3), time(7)

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

    Linux man-pages 6.19            2026-02-08                       times(2)

------------------------------------------------------------------------

Pages that refer to this page: [time(1)](../man1/time.1.html),  [fork(2)](../man2/fork.2.html),  [getrusage(2)](../man2/getrusage.2.html),  [sigaction(2)](../man2/sigaction.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [clock(3)](../man3/clock.3.html),  [clock_t(3type)](../man3/clock_t.3type.html),  [getauxval(3)](../man3/getauxval.3.html),  [pmwebtimerregister(3)](../man3/pmwebtimerregister.3.html),  [proc_pid_stat(5)](../man5/proc_pid_stat.5.html),  [pthreads(7)](../man7/pthreads.7.html),  [rpm-lua(7)](../man7/rpm-lua.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [time(7)](../man7/time.7.html)

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
