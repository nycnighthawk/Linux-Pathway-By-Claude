---
{"title": "gettimeofday(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/gettimeofday.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# gettimeofday(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    gettimeofday(2)            System Calls Manual            gettimeofday(2)

## [](#NAME)NAME

           gettimeofday, settimeofday - get / set time

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/time.h>

           [[deprecated]]
           int gettimeofday(struct timeval *restrict tv,
                            struct timezone *_Nullable restrict tz);
           [[deprecated]]
           int settimeofday(const struct timeval *tv,
                            const struct timezone *_Nullable tz);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           settimeofday():
               Since glibc 2.19:
                   _DEFAULT_SOURCE
               glibc 2.19 and earlier:
                   _BSD_SOURCE

## [](#DESCRIPTION)DESCRIPTION

           The functions gettimeofday() and settimeofday() can get and set
           the time as well as a timezone.

           The tv argument is a struct timeval (as specified in
           <sys/time.h>):

               struct timeval {
                   time_t      tv_sec;     /* seconds */
                   suseconds_t tv_usec;    /* microseconds */
               };

           and gives the number of seconds and microseconds since the Epoch
           (see time(2)).

           The tz argument is a struct timezone:

               struct timezone {
                   int tz_minuteswest;     /* minutes west of Greenwich */
                   int tz_dsttime;         /* type of DST correction */
               };

           If either tv or tz is NULL, the corresponding structure is not set
           or returned.  (However, compilation warnings will result if tv is
           NULL.)

           The use of the timezone structure is obsolete; the tz argument
           should normally be specified as NULL.  See VERSIONS.

           Under Linux, there are some peculiar "warp clock" semantics
           associated with the settimeofday() system call if on the very
           first call (after booting) that has a non-NULL tz argument, the tv
           argument is NULL and the tz_minuteswest field is nonzero.  (The
           tz_dsttime field should be zero for this case.)  In such a case it
           is assumed that the CMOS clock is on local time, and that it has
           to be incremented by this amount to get UTC system time.  No doubt
           it is a bad idea to use this feature.

## [](#RETURN_VALUE)RETURN VALUE

           gettimeofday() and settimeofday() return 0 for success.  On error,
           -1 is returned and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT One of tv or tz pointed outside the accessible address
                  space.

           EINVAL (settimeofday()): timezone is invalid.

           EINVAL (settimeofday()): tv.tv_sec is negative or tv.tv_usec is
                  outside the range [0, 999,999].

           EINVAL (since Linux 4.3)
                  (settimeofday()): An attempt was made to set the time to a
                  value less than the current value of the CLOCK_MONOTONIC
                  clock (see clock_gettime(2)).

           EPERM  The calling process has insufficient privilege to call
                  settimeofday(); under Linux the CAP_SYS_TIME capability is
                  required.

## [](#VERSIONS)VERSIONS

       C library/kernel differences
           On some architectures, an implementation of gettimeofday() is
           provided in the vdso(7).

           The kernel accepts NULL for both tv and tz.  The timezone argument
           is ignored by glibc and musl, and not passed to/from the kernel.
           Android's bionic passes the timezone argument to/from the kernel,
           but Android does not update the kernel timezone based on the
           device timezone in Settings, so the kernel's timezone is typically
           UTC.

## [](#STANDARDS)STANDARDS

           None.

## [](#HISTORY)HISTORY

           4.3BSD, SVr4.  SUSv1 and POSIX.1-2001 XSI described gettimeofday()
           but not settimeofday().  POSIX.1-2008 XSI marked gettimeofday() as
           obsolete, recommending the use of clock_gettime(2) instead.
           Likewise, clock_settime(2) should be used instead of
           settimeofday().  POSIX.1-2024 removed gettimeofday().

           Traditionally, the fields of struct timeval were of type long.

       The tz_dsttime field
           On a non-Linux kernel, with glibc, the tz_dsttime field of struct
           timezone will be set to a nonzero value by gettimeofday() if the
           current timezone has ever had or will have a daylight saving rule
           applied.  In this sense it exactly mirrors the meaning of
           daylight(3) for the current zone.  On Linux, with glibc, the
           setting of the tz_dsttime field of struct timezone has never been
           used by settimeofday() or gettimeofday().  Thus, the following is
           purely of historical interest.

           On old systems, the field tz_dsttime contains a symbolic constant
           (values are given below) that indicates in which part of the year
           Daylight Saving Time is in force.  (Note: this value is constant
           throughout the year: it does not indicate that DST is in force, it
           just selects an algorithm.)  The daylight saving time algorithms
           defined are as follows:

               DST_NONE     /* not on DST */
               DST_USA      /* USA style DST */
               DST_AUST     /* Australian style DST */
               DST_WET      /* Western European DST */
               DST_MET      /* Middle European DST */
               DST_EET      /* Eastern European DST */
               DST_CAN      /* Canada */
               DST_GB       /* Great Britain and Eire */
               DST_RUM      /* Romania */
               DST_TUR      /* Turkey */
               DST_AUSTALT  /* Australian style with shift in 1986 */

           Of course, it turned out that the period in which Daylight Saving
           Time is in force cannot be given by a simple algorithm, one per
           country; indeed, this period is determined by unpredictable
           political decisions.  So this method of representing timezones has
           been abandoned.

## [](#NOTES)NOTES

           The time returned by gettimeofday() is affected by discontinuous
           jumps in the system time (e.g., if the system administrator
           manually changes the system time).  If you need a monotonically
           increasing clock, see clock_gettime(2).

           Macros for operating on timeval structures are described in
           timeradd(3).

## [](#SEE_ALSO)SEE ALSO

           date(1), adjtimex(2), clock_gettime(2), time(2), ctime(3),
           ftime(3), timeradd(3), capabilities(7), time(7), vdso(7),
           hwclock(8)

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

    Linux man-pages 6.19            2026-02-08                gettimeofday(2)

------------------------------------------------------------------------

Pages that refer to this page: [adjtimex(2)](../man2/adjtimex.2.html),  [alarm(2)](../man2/alarm.2.html),  [clock_getres(2)](../man2/clock_getres.2.html),  [getitimer(2)](../man2/getitimer.2.html),  [seccomp(2)](../man2/seccomp.2.html),  [stime(2)](../man2/stime.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [time(2)](../man2/time.2.html),  [timerfd_create(2)](../man2/timerfd_create.2.html),  [adjtime(3)](../man3/adjtime.3.html),  [ctime(3)](../man3/ctime.3.html),  [difftime(3)](../man3/difftime.3.html),  [ftime(3)](../man3/ftime.3.html),  [pmdaeventarray(3)](../man3/pmdaeventarray.3.html),  [pmtimeval(3)](../man3/pmtimeval.3.html),  [pthread_cond_init(3)](../man3/pthread_cond_init.3.html),  [timeradd(3)](../man3/timeradd.3.html),  [timeval(3type)](../man3/timeval.3type.html),  [tzset(3)](../man3/tzset.3.html),  [uuid_time(3)](../man3/uuid_time.3.html),  [rtc(4)](../man4/rtc.4.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [capabilities(7)](../man7/capabilities.7.html),  [time(7)](../man7/time.7.html),  [vdso(7)](../man7/vdso.7.html),  [hwclock(8)](../man8/hwclock.8.html),  [mount(8)](../man8/mount.8.html)

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
