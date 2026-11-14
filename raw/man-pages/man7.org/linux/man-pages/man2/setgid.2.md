---
{"title": "setgid(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/setgid.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# setgid(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    setgid(2)                  System Calls Manual                  setgid(2)

## [](#NAME)NAME

           setgid - set group identity

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           int setgid(gid_t gid);

## [](#DESCRIPTION)DESCRIPTION

           setgid() sets the effective group ID of the calling process.  If
           the calling process is privileged (more precisely: has the
           CAP_SETGID capability in its user namespace), the real GID and
           saved set-group-ID are also set.

           Under Linux, setgid() is implemented like the POSIX version with
           the _POSIX_SAVED_IDS feature.  This allows a set-group-ID program
           that is not set-user-ID-root to drop all of its group privileges,
           do some un-privileged work, and then reengage the original
           effective group ID in a secure manner.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL The group ID specified in gid is not valid in this user
                  namespace.

           EPERM  The calling process is not privileged (does not have the
                  CAP_SETGID capability in its user namespace), and gid does
                  not match the real group ID or saved set-group-ID of the
                  calling process.

## [](#VERSIONS)VERSIONS

       C library/kernel differences
           At the kernel level, user IDs and group IDs are a per-thread
           attribute.  However, POSIX requires that all threads in a process
           share the same credentials.  The NPTL threading implementation
           handles the POSIX requirements by providing wrapper functions for
           the various system calls that change process UIDs and GIDs.  These
           wrapper functions (including the one for setgid()) employ a
           signal-based technique to ensure that when one thread changes
           credentials, all of the other threads in the process also change
           their credentials.  For details, see nptl(7).

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001, SVr4.

           The original Linux setgid() system call supported only 16-bit
           group IDs.  Subsequently, Linux 2.4 added setgid32() supporting
           32-bit IDs.  The glibc setgid() wrapper function transparently
           deals with the variation across kernel versions.

## [](#SEE_ALSO)SEE ALSO

           getgid(2), setegid(2), setregid(2), capabilities(7),
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

    Linux man-pages 6.19            2026-02-08                      setgid(2)

------------------------------------------------------------------------

Pages that refer to this page: [capsh(1)](../man1/capsh.1.html),  [pmdammv(1)](../man1/pmdammv.1.html),  [access(2)](../man2/access.2.html),  [getgid(2)](../man2/getgid.2.html),  [getgroups(2)](../man2/getgroups.2.html),  [setreuid(2)](../man2/setreuid.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [cap_get_proc(3)](../man3/cap_get_proc.3.html),  [euidaccess(3)](../man3/euidaccess.3.html),  [proc_sys_fs(5)](../man5/proc_sys_fs.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [credentials(7)](../man7/credentials.7.html),  [nptl(7)](../man7/nptl.7.html),  [rpm-lua(7)](../man7/rpm-lua.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html)

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
