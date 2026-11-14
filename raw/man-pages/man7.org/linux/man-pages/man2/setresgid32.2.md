---
{"title": "setresuid(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/setresgid32.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# setresuid(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    setresuid(2)               System Calls Manual               setresuid(2)

## [](#NAME)NAME

           setresuid, setresgid - set real, effective, and saved user or
           group ID

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #define _GNU_SOURCE         /* See feature_test_macros(7) */
           #include <unistd.h>

           int setresuid(uid_t ruid, uid_t euid, uid_t suid);
           int setresgid(gid_t rgid, gid_t egid, gid_t sgid);

## [](#DESCRIPTION)DESCRIPTION

           setresuid() sets the real user ID, the effective user ID, and the
           saved set-user-ID of the calling process.

           An unprivileged process may change its real UID, effective UID,
           and saved set-user-ID, each to one of: the current real UID, the
           current effective UID, or the current saved set-user-ID.

           A privileged process (on Linux, one having the CAP_SETUID
           capability) may set its real UID, effective UID, and saved set-
           user-ID to arbitrary values.

           If one of the arguments equals -1, the corresponding value is not
           changed.

           Regardless of what changes are made to the real UID, effective
           UID, and saved set-user-ID, the filesystem UID is always set to
           the same value as the (possibly new) effective UID.

           Completely analogously, setresgid() sets the real GID, effective
           GID, and saved set-group-ID of the calling process (and always
           modifies the filesystem GID to be the same as the effective GID),
           with the same restrictions for unprivileged processes.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

           Note: there are cases where setresuid() can fail even when the
           caller is UID 0; it is a grave security error to omit checking for
           a failure return from setresuid().

## [](#ERRORS)ERRORS

           EAGAIN The call would change the caller's real UID (i.e., ruid
                  does not match the caller's real UID), but there was a
                  temporary failure allocating the necessary kernel data
                  structures.

           EAGAIN ruid does not match the caller's real UID and this call
                  would bring the number of processes belonging to the real
                  user ID ruid over the caller's RLIMIT_NPROC resource limit.
                  Since Linux 3.1, this error case no longer occurs (but
                  robust applications should check for this error); see the
                  description of EAGAIN in execve(2).

           EINVAL One or more of the target user or group IDs is not valid in
                  this user namespace.

           EPERM  The calling process is not privileged (did not have the
                  necessary capability in its user namespace) and tried to
                  change the IDs to values that are not permitted.  For
                  setresuid(), the necessary capability is CAP_SETUID; for
                  setresgid(), it is CAP_SETGID.

## [](#VERSIONS)VERSIONS

       C library/kernel differences
           At the kernel level, user IDs and group IDs are a per-thread
           attribute.  However, POSIX requires that all threads in a process
           share the same credentials.  The NPTL threading implementation
           handles the POSIX requirements by providing wrapper functions for
           the various system calls that change process UIDs and GIDs.  These
           wrapper functions (including those for setresuid() and
           setresgid()) employ a signal-based technique to ensure that when
           one thread changes credentials, all of the other threads in the
           process also change their credentials.  For details, see nptl(7).

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2024.  Linux 2.1.44, glibc 2.3.2.  HP-UX, FreeBSD.

           The original Linux setresuid() and setresgid() system calls
           supported only 16-bit user and group IDs.  Subsequently, Linux 2.4
           added setresuid32() and setresgid32(), supporting 32-bit IDs.  The
           glibc setresuid() and setresgid() wrapper functions transparently
           deal with the variations across kernel versions.

## [](#SEE_ALSO)SEE ALSO

           getresuid(2), getuid(2), setfsgid(2), setfsuid(2), setreuid(2),
           setuid(2), capabilities(7), credentials(7), user_namespaces(7)

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

    Linux man-pages 6.19            2026-02-08                   setresuid(2)

------------------------------------------------------------------------

Pages that refer to this page: [execve(2)](../man2/execve.2.html),  [getresuid(2)](../man2/getresuid.2.html),  [seteuid(2)](../man2/seteuid.2.html),  [setreuid(2)](../man2/setreuid.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [capabilities(7)](../man7/capabilities.7.html),  [credentials(7)](../man7/credentials.7.html),  [nptl(7)](../man7/nptl.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html)

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
