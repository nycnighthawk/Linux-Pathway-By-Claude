---
{"title": "setfsgid(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/setfsgid.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# setfsgid(2) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    setfsgid(2)                System Calls Manual                setfsgid(2)

## [](#NAME)NAME

           setfsgid - set group identity used for filesystem checks

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/fsuid.h>

           [[deprecated]] int setfsgid(gid_t fsgid);

## [](#DESCRIPTION)DESCRIPTION

           On Linux, a process has both a filesystem group ID and an
           effective group ID.  The (Linux-specific) filesystem group ID is
           used for permissions checking when accessing filesystem objects,
           while the effective group ID is used for some other kinds of
           permissions checks (see credentials(7)).

           Normally, the value of the process's filesystem group ID is the
           same as the value of its effective group ID.  This is so, because
           whenever a process's effective group ID is changed, the kernel
           also changes the filesystem group ID to be the same as the new
           value of the effective group ID.  A process can cause the value of
           its filesystem group ID to diverge from its effective group ID by
           using setfsgid() to change its filesystem group ID to the value
           given in fsgid.

           setfsgid() will succeed only if the caller is the superuser or if
           fsgid matches either the caller's real group ID, effective group
           ID, saved set-group-ID, or current the filesystem user ID.

## [](#RETURN_VALUE)RETURN VALUE

           On both success and failure, this call returns the previous
           filesystem group ID of the caller.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 1.2.

       C library/kernel differences
           In glibc 2.15 and earlier, when the wrapper for this system call
           determines that the argument can't be passed to the kernel without
           integer truncation (because the kernel is old and does not support
           32-bit group IDs), it will return -1 and set errno to EINVAL
           without attempting the system call.

## [](#NOTES)NOTES

           The filesystem group ID concept and the setfsgid() system call
           were invented for historical reasons that are no longer applicable
           on modern Linux kernels.  See setfsuid(2) for a discussion of why
           the use of both setfsuid(2) and setfsgid() is nowadays unneeded.

           The original Linux setfsgid() system call supported only 16-bit
           group IDs.  Subsequently, Linux 2.4 added setfsgid32() supporting
           32-bit IDs.  The glibc setfsgid() wrapper function transparently
           deals with the variation across kernel versions.

## [](#BUGS)BUGS

           No error indications of any kind are returned to the caller, and
           the fact that both successful and unsuccessful calls return the
           same value makes it impossible to directly determine whether the
           call succeeded or failed.  Instead, the caller must resort to
           looking at the return value from a further call such as
           setfsgid(-1) (which will always fail), in order to determine if a
           preceding call to setfsgid() changed the filesystem group ID.  At
           the very least, EPERM should be returned when the call fails
           (because the caller lacks the CAP_SETGID capability).

## [](#SEE_ALSO)SEE ALSO

           kill(2), setfsuid(2), capabilities(7), credentials(7)

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

    Linux man-pages 6.19            2026-02-08                    setfsgid(2)

------------------------------------------------------------------------

Pages that refer to this page: [setfsuid(2)](../man2/setfsuid.2.html),  [setresuid(2)](../man2/setresuid.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [credentials(7)](../man7/credentials.7.html),  [path_resolution(7)](../man7/path_resolution.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html)

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
