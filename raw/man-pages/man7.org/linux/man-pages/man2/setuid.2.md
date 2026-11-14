---
{"title": "setuid(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/setuid.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# setuid(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    setuid(2)                  System Calls Manual                  setuid(2)

## [](#NAME)NAME

           setuid - set user identity

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           int setuid(uid_t uid);

## [](#DESCRIPTION)DESCRIPTION

           setuid() sets the effective user ID of the calling process.  If
           the calling process is privileged (more precisely: if the process
           has the CAP_SETUID capability in its user namespace), the real UID
           and saved set-user-ID are also set.

           Under Linux, setuid() is implemented like the POSIX version with
           the _POSIX_SAVED_IDS feature.  This allows a set-user-ID (other
           than root) program to drop all of its user privileges, do some un-
           privileged work, and then reengage the original effective user ID
           in a secure manner.

           If the user is root or the program is set-user-ID-root, special
           care must be taken: setuid() checks the effective user ID of the
           caller and if it is the superuser, all process-related user ID's
           are set to uid.  After this has occurred, it is impossible for the
           program to regain root privileges.

           Thus, a set-user-ID-root program wishing to temporarily drop root
           privileges, assume the identity of an unprivileged user, and then
           regain root privileges afterward cannot use setuid().  You can
           accomplish this with seteuid(2).

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

           Note: there are cases where setuid() can fail even when the caller
           is UID 0; it is a grave security error to omit checking for a
           failure return from setuid().

## [](#ERRORS)ERRORS

           EAGAIN The call would change the caller's real UID (i.e., uid does
                  not match the caller's real UID), but there was a temporary
                  failure allocating the necessary kernel data structures.

           EAGAIN uid does not match the real user ID of the caller and this
                  call would bring the number of processes belonging to the
                  real user ID uid over the caller's RLIMIT_NPROC resource
                  limit.  Since Linux 3.1, this error case no longer occurs
                  (but robust applications should check for this error); see
                  the description of EAGAIN in execve(2).

           EINVAL The user ID specified in uid is not valid in this user
                  namespace.

           EPERM  The user is not privileged (Linux: does not have the
                  CAP_SETUID capability in its user namespace) and uid does
                  not match the real UID or saved set-user-ID of the calling
                  process.

## [](#VERSIONS)VERSIONS

       C library/kernel differences
           At the kernel level, user IDs and group IDs are a per-thread
           attribute.  However, POSIX requires that all threads in a process
           share the same credentials.  The NPTL threading implementation
           handles the POSIX requirements by providing wrapper functions for
           the various system calls that change process UIDs and GIDs.  These
           wrapper functions (including the one for setuid()) employ a
           signal-based technique to ensure that when one thread changes
           credentials, all of the other threads in the process also change
           their credentials.  For details, see nptl(7).

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001, SVr4.

           Not quite compatible with the 4.4BSD call, which sets all of the
           real, saved, and effective user IDs.

           The original Linux setuid() system call supported only 16-bit user
           IDs.  Subsequently, Linux 2.4 added setuid32() supporting 32-bit
           IDs.  The glibc setuid() wrapper function transparently deals with
           the variation across kernel versions.

## [](#NOTES)NOTES

           Linux has the concept of the filesystem user ID, normally equal to
           the effective user ID.  The setuid() call also sets the filesystem
           user ID of the calling process.  See setfsuid(2).

           If uid is different from the old effective UID, the process will
           be forbidden from leaving core dumps.

## [](#SEE_ALSO)SEE ALSO

           getuid(2), seteuid(2), setfsuid(2), setreuid(2), capabilities(7),
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

    Linux man-pages 6.19            2026-02-08                      setuid(2)

------------------------------------------------------------------------

Pages that refer to this page: [capsh(1)](../man1/capsh.1.html),  [access(2)](../man2/access.2.html),  [execve(2)](../man2/execve.2.html),  [getresuid(2)](../man2/getresuid.2.html),  [getuid(2)](../man2/getuid.2.html),  [seccomp(2)](../man2/seccomp.2.html),  [seteuid(2)](../man2/seteuid.2.html),  [setresuid(2)](../man2/setresuid.2.html),  [setreuid(2)](../man2/setreuid.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [vfork(2)](../man2/vfork.2.html),  [cap_get_proc(3)](../man3/cap_get_proc.3.html),  [euidaccess(3)](../man3/euidaccess.3.html),  [posix_spawn(3)](../man3/posix_spawn.3.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [capabilities(7)](../man7/capabilities.7.html),  [credentials(7)](../man7/credentials.7.html),  [nptl(7)](../man7/nptl.7.html),  [rpm-lua(7)](../man7/rpm-lua.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html)

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
