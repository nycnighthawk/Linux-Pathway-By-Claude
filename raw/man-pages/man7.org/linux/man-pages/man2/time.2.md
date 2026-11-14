---
{"title": "time(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/time.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# time(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    time(2)                    System Calls Manual                    time(2)

## [](#NAME)NAME

           time - get time in seconds

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <time.h>

           time_t time(time_t *_Nullable tloc);

## [](#DESCRIPTION)DESCRIPTION

           time() returns the time as the number of seconds since the Epoch,
           1970-01-01 00:00:00 +0000 (UTC).

           If tloc is non-NULL, the return value is also stored in the memory
           pointed to by tloc.

## [](#RETURN_VALUE)RETURN VALUE

           On success, the value of time in seconds since the Epoch is
           returned.  On error, ((time_t) -1) is returned, and errno is set
           to indicate the error.

## [](#ERRORS)ERRORS

           EOVERFLOW
                  The time cannot be represented as a time_t value.  This can
                  happen if an executable with 32-bit time_t is run on a
                  64-bit kernel when the time is 2038-01-19 03:14:08 UTC or
                  later.  However, when the system time is out of time_t
                  range in other situations, the behavior is undefined.

           EFAULT tloc points outside your accessible address space (but see
                  BUGS).

                  On systems where the C library time() wrapper function
                  invokes an implementation provided by the vdso(7) (so that
                  there is no trap into the kernel), an invalid address may
                  instead trigger a SIGSEGV signal.

## [](#VERSIONS)VERSIONS

           POSIX.1 defines seconds since the Epoch using a formula that
           approximates the number of seconds between a specified time and
           the Epoch.  This formula takes account of the facts that all years
           that are evenly divisible by 4 are leap years, but years that are
           evenly divisible by 100 are not leap years unless they are also
           evenly divisible by 400, in which case they are leap years.  This
           value is not the same as the actual number of seconds between the
           time and the Epoch, because of leap seconds and because system
           clocks are not required to be synchronized to a standard
           reference.  Linux systems normally follow the POSIX requirement
           that this value ignore leap seconds, so that conforming systems
           interpret it consistently; see POSIX.1-2018 Rationale A.4.16.

           Applications intended to run after 2038 should use ABIs with
           time_t wider than 32 bits; see time_t(3type).

       C library/kernel differences
           On some architectures, an implementation of time() is provided in
           the vdso(7).

## [](#STANDARDS)STANDARDS

           C11, POSIX.1-2024.

## [](#HISTORY)HISTORY

           SVr4, 4.3BSD, C89, POSIX.1-2001, V7.

## [](#BUGS)BUGS

           Error returns from this system call are indistinguishable from
           successful reports that the time is a few seconds before the
           Epoch, so the C library wrapper function never sets errno as a
           result of this call.

           The tloc argument is obsolescent and should always be NULL in new
           code.  When tloc is NULL, the call cannot fail.

## [](#SEE_ALSO)SEE ALSO

           date(1), gettimeofday(2), ctime(3), ftime(3), time(7), vdso(7)

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

    Linux man-pages 6.19            2026-02-08                        time(2)

------------------------------------------------------------------------

Pages that refer to this page: [clock_getres(2)](../man2/clock_getres.2.html),  [gettimeofday(2)](../man2/gettimeofday.2.html),  [seccomp(2)](../man2/seccomp.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [ctime(3)](../man3/ctime.3.html),  [difftime(3)](../man3/difftime.3.html),  [ftime(3)](../man3/ftime.3.html),  [getdate(3)](../man3/getdate.3.html),  [misc_conv(3)](../man3/misc_conv.3.html),  [pmtimeval(3)](../man3/pmtimeval.3.html),  [\_\_ppc_get_timebase(3)](../man3/__ppc_get_timebase.3.html),  [pthread_cond_init(3)](../man3/pthread_cond_init.3.html),  [pthread_tryjoin_np(3)](../man3/pthread_tryjoin_np.3.html),  [strftime(3)](../man3/strftime.3.html),  [strptime(3)](../man3/strptime.3.html),  [time_t(3type)](../man3/time_t.3type.html),  [tzset(3)](../man3/tzset.3.html),  [uuid_time(3)](../man3/uuid_time.3.html),  [rtc(4)](../man4/rtc.4.html),  [rpmbuild-config(5)](../man5/rpmbuild-config.5.html),  [tzfile(5)](../man5/tzfile.5.html),  [utmp(5)](../man5/utmp.5.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [time(7)](../man7/time.7.html),  [lsof(8)](../man8/lsof.8.html)

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
