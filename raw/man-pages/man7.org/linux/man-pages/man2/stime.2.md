---
{"title": "stime(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/stime.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stime(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    stime(2)                   System Calls Manual                   stime(2)

## [](#NAME)NAME

           stime - set time

## [](#SYNOPSIS)SYNOPSIS

           #include <time.h>

           [[deprecated]] int stime(const time_t *t);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           stime():
               Since glibc 2.19:
                   _DEFAULT_SOURCE
               glibc 2.19 and earlier:
                   _SVID_SOURCE

## [](#DESCRIPTION)DESCRIPTION

           NOTE: This function is deprecated; use clock_settime(2) instead.

           stime() sets the system's idea of the time and date.  The time,
           pointed to by t, is measured in seconds since the Epoch,
           1970-01-01 00:00:00 +0000 (UTC).  stime() may be executed only by
           the superuser.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT Error in getting information from user space.

           EPERM  The calling process has insufficient privilege.  Under
                  Linux, the CAP_SYS_TIME privilege is required.

## [](#STANDARDS)STANDARDS

           None.

## [](#HISTORY)HISTORY

           SVr4.

           Starting with glibc 2.31, this function is no longer available to
           newly linked applications and is no longer declared in <time.h>.

## [](#SEE_ALSO)SEE ALSO

           date(1), settimeofday(2), capabilities(7)

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

    Linux man-pages 6.19            2026-02-08                       stime(2)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html),  [time_t(3type)](../man3/time_t.3type.html),  [rtc(4)](../man4/rtc.4.html),  [capabilities(7)](../man7/capabilities.7.html)

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
