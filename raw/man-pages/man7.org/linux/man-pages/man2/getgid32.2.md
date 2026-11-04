---
{"title": "getgid(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/getgid32.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# getgid(2) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    getgid(2)                  System Calls Manual                  getgid(2)

## [](#NAME)NAME

           getgid, getegid - get group identity

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           gid_t getgid(void);
           gid_t getegid(void);

## [](#DESCRIPTION)DESCRIPTION

           getgid() returns the real group ID of the calling process.

           getegid() returns the effective group ID of the calling process.

## [](#ERRORS)ERRORS

           These functions are always successful and never modify errno.

## [](#VERSIONS)VERSIONS

           On Alpha, instead of a pair of getgid() and getegid() system
           calls, a single getxgid() system call is provided, which returns a
           pair of real and effective GIDs.  The glibc getgid() and getegid()
           wrapper functions transparently deal with this.  See syscall(2)
           for details regarding register mapping.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           4.3BSD, POSIX.1-1988.

           The original Linux getgid() and getegid() system calls supported
           only 16-bit group IDs.  Subsequently, Linux 2.4 added getgid32()
           and getegid32(), supporting 32-bit IDs.  The glibc getgid() and
           getegid() wrapper functions transparently deal with the variations
           across kernel versions.

## [](#SEE_ALSO)SEE ALSO

           getresgid(2), setgid(2), setregid(2), credentials(7)

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

    Linux man-pages 6.19            2026-02-08                      getgid(2)

------------------------------------------------------------------------

Pages that refer to this page: [ps(1)](../man1/ps.1.html),  [strace(1)](../man1/strace.1.html),  [getgroups(2)](../man2/getgroups.2.html),  [setgid(2)](../man2/setgid.2.html),  [setreuid(2)](../man2/setreuid.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [group_member(3)](../man3/group_member.3.html),  [id_t(3type)](../man3/id_t.3type.html),  [credentials(7)](../man7/credentials.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html)

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
