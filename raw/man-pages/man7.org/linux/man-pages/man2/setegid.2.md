---
{"title": "seteuid(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/setegid.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# seteuid(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    seteuid(2)                 System Calls Manual                 seteuid(2)

## [](#NAME)NAME

           seteuid, setegid - set effective user or group ID

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           int seteuid(uid_t euid);
           int setegid(gid_t egid);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           seteuid(), setegid():
               _POSIX_C_SOURCE >= 200112L
                   || /* glibc <= 2.19: */ _BSD_SOURCE

## [](#DESCRIPTION)DESCRIPTION

           seteuid() sets the effective user ID of the calling process.
           Unprivileged processes may only set the effective user ID to the
           real user ID, the effective user ID or the saved set-user-ID.

           Precisely the same holds for setegid() with "group" instead of
           "user".

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

           Note: there are cases where seteuid() can fail even when the
           caller is UID 0; it is a grave security error to omit checking for
           a failure return from seteuid().

## [](#ERRORS)ERRORS

           EINVAL The target user or group ID is not valid in this user
                  namespace.

           EPERM  In the case of seteuid(): the calling process is not
                  privileged (does not have the CAP_SETUID capability in its
                  user namespace) and euid does not match the current real
                  user ID, current effective user ID, or current saved set-
                  user-ID.

                  In the case of setegid(): the calling process is not
                  privileged (does not have the CAP_SETGID capability in its
                  user namespace) and egid does not match the current real
                  group ID, current effective group ID, or current saved set-
                  group-ID.

## [](#VERSIONS)VERSIONS

           Setting the effective user (group) ID to the saved set-user-ID
           (saved set-group-ID) is possible since Linux 1.1.37 (1.1.38).  On
           an arbitrary system one should check _POSIX_SAVED_IDS.

           Under glibc 2.0, seteuid(euid) is equivalent to setreuid(-1, euid)
           and hence may change the saved set-user-ID.  Under glibc 2.1 and
           later, it is equivalent to setresuid(-1, euid, -1) and hence does
           not change the saved set-user-ID.  Analogous remarks hold for
           setegid(), with the difference that the change in implementation
           from setregid(-1, egid) to setresgid(-1, egid, -1) occurred in
           glibc 2.2 or 2.3 (depending on the hardware architecture).

           According to POSIX.1, seteuid() (setegid()) need not permit euid
           (egid) to be the same value as the current effective user (group)
           ID, and some implementations do not permit this.

       C library/kernel differences
           On Linux, seteuid() and setegid() are implemented as library
           functions that call, respectively, setresuid(2) and setresgid(2).

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001, 4.3BSD.

## [](#SEE_ALSO)SEE ALSO

           geteuid(2), setresuid(2), setreuid(2), setuid(2), capabilities(7),
           credentials(7), user_namespaces(7)

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

    Linux man-pages 6.19            2026-02-08                     seteuid(2)

------------------------------------------------------------------------

Pages that refer to this page: [pmdaproc(1)](../man1/pmdaproc.1.html),  [setgid(2)](../man2/setgid.2.html),  [setreuid(2)](../man2/setreuid.2.html),  [setuid(2)](../man2/setuid.2.html),  [proc_sys_fs(5)](../man5/proc_sys_fs.5.html),  [credentials(7)](../man7/credentials.7.html),  [nptl(7)](../man7/nptl.7.html),  [pthreads(7)](../man7/pthreads.7.html)

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
