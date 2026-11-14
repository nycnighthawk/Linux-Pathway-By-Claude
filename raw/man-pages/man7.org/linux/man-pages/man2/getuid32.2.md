---
{"title": "getuid(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/getuid32.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# getuid(2) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    getuid(2)                  System Calls Manual                  getuid(2)

## [](#NAME)NAME

           getuid, geteuid - get user identity

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           uid_t getuid(void);
           uid_t geteuid(void);

## [](#DESCRIPTION)DESCRIPTION

           getuid() returns the real user ID of the calling process.

           geteuid() returns the effective user ID of the calling process.

## [](#ERRORS)ERRORS

           These functions are always successful and never modify errno.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           4.3BSD, POSIX.1-1988.

           In UNIX V6 the getuid() call returned (euid << 8) + uid.  UNIX V7
           introduced separate calls getuid() and geteuid().

           The original Linux getuid() and geteuid() system calls supported
           only 16-bit user IDs.  Subsequently, Linux 2.4 added getuid32()
           and geteuid32(), supporting 32-bit IDs.  The glibc getuid() and
           geteuid() wrapper functions transparently deal with the variations
           across kernel versions.

           On Alpha, instead of a pair of getuid() and geteuid() system
           calls, a single getxuid() system call is provided, which returns a
           pair of real and effective UIDs.  The glibc getuid() and geteuid()
           wrapper functions transparently deal with this.  See syscall(2)
           for details regarding register mapping.

## [](#SEE_ALSO)SEE ALSO

           getresuid(2), setreuid(2), setuid(2), credentials(7)

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

    Linux man-pages 6.19            2026-02-08                      getuid(2)

------------------------------------------------------------------------

Pages that refer to this page: [homectl(1)](../man1/homectl.1.html),  [importctl(1)](../man1/importctl.1.html),  [journalctl(1)](../man1/journalctl.1.html),  [localectl(1)](../man1/localectl.1.html),  [loginctl(1)](../man1/loginctl.1.html),  [machinectl(1)](../man1/machinectl.1.html),  [portablectl(1)](../man1/portablectl.1.html),  [ps(1)](../man1/ps.1.html),  [storagectl(1)](../man1/storagectl.1.html),  [strace(1)](../man1/strace.1.html),  [systemctl(1)](../man1/systemctl.1.html),  [systemd(1)](../man1/systemd.1.html),  [systemd-analyze(1)](../man1/systemd-analyze.1.html),  [systemd-inhibit(1)](../man1/systemd-inhibit.1.html),  [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [systemd-vmspawn(1)](../man1/systemd-vmspawn.1.html),  [timedatectl(1)](../man1/timedatectl.1.html),  [updatectl(1)](../man1/updatectl.1.html),  [userdbctl(1)](../man1/userdbctl.1.html),  [getresuid(2)](../man2/getresuid.2.html),  [seteuid(2)](../man2/seteuid.2.html),  [setpgid(2)](../man2/setpgid.2.html),  [setresuid(2)](../man2/setresuid.2.html),  [setreuid(2)](../man2/setreuid.2.html),  [setuid(2)](../man2/setuid.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [getlogin(3)](../man3/getlogin.3.html),  [id_t(3type)](../man3/id_t.3type.html),  [pam_close_session(3)](../man3/pam_close_session.3.html),  [pam_open_session(3)](../man3/pam_open_session.3.html),  [sysexits.h(3head)](../man3/sysexits.h.3head.html),  [credentials(7)](../man7/credentials.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html),  [systemd-tmpfiles(8)](../man8/systemd-tmpfiles.8.html)

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
