---
{"title": "nice(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/nice.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nice(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    nice(2)                    System Calls Manual                    nice(2)

## [](#NAME)NAME

           nice - change process priority

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           int nice(int inc);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           nice():
               _XOPEN_SOURCE
                   || /* Since glibc 2.19: */ _DEFAULT_SOURCE
                   || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE

## [](#DESCRIPTION)DESCRIPTION

           nice() adds inc to the nice value for the calling thread.  (A
           higher nice value means a lower priority.)

           The range of the nice value is +19 (low priority) to -20 (high
           priority).  Attempts to set a nice value outside the range are
           clamped to the range.

           Traditionally, only a privileged process could lower the nice
           value (i.e., set a higher priority).  However, since Linux 2.6.12,
           an unprivileged process can decrease the nice value of a target
           process that has a suitable RLIMIT_NICE soft limit; see
           getrlimit(2) for details.

## [](#RETURN_VALUE)RETURN VALUE

           On success, the new nice value is returned (but see VERSIONS
           below).  On error, -1 is returned, and errno is set to indicate
           the error.

           A successful call can legitimately return -1.  To detect an error,
           set errno to 0 before the call, and check whether it is nonzero
           after nice() returns -1.

## [](#ERRORS)ERRORS

           EPERM  The calling process attempted to increase its priority by
                  supplying a negative inc but has insufficient privileges.
                  Under Linux, the CAP_SYS_NICE capability is required.  (But
                  see the discussion of the RLIMIT_NICE resource limit in
                  setrlimit(2).)

## [](#VERSIONS)VERSIONS

       C library/kernel differences
           POSIX.1 specifies that nice() should return the new nice value.
           However, the raw Linux system call returns 0 on success.
           Likewise, the nice() wrapper function provided in glibc 2.2.3 and
           earlier returns 0 on success.

           Since glibc 2.2.4, the nice() wrapper function provided by glibc
           provides conformance to POSIX.1 by calling getpriority(2) to
           obtain the new nice value, which is then returned to the caller.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001, SVr4, 4.3BSD.

## [](#NOTES)NOTES

           For further details on the nice value, see sched(7).

           Note: the addition of the "autogroup" feature in Linux 2.6.38
           means that the nice value no longer has its traditional effect in
           many circumstances.  For details, see sched(7).

## [](#SEE_ALSO)SEE ALSO

           nice(1), renice(1), fork(2), getpriority(2), getrlimit(2),
           setpriority(2), capabilities(7), sched(7)

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

    Linux man-pages 6.19            2026-02-08                        nice(2)

------------------------------------------------------------------------

Pages that refer to this page: [nice(1)](../man1/nice.1.html),  [getpriority(2)](../man2/getpriority.2.html),  [getrlimit(2)](../man2/getrlimit.2.html),  [sched_setaffinity(2)](../man2/sched_setaffinity.2.html),  [sched_setattr(2)](../man2/sched_setattr.2.html),  [sched_setparam(2)](../man2/sched_setparam.2.html),  [sched_setscheduler(2)](../man2/sched_setscheduler.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [capabilities(7)](../man7/capabilities.7.html),  [sched(7)](../man7/sched.7.html)

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
