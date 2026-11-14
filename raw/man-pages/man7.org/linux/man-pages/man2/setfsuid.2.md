---
{"title": "setfsuid(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/setfsuid.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# setfsuid(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    setfsuid(2)                System Calls Manual                setfsuid(2)

## [](#NAME)NAME

           setfsuid - set user identity used for filesystem checks

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/fsuid.h>

           [[deprecated]] int setfsuid(uid_t fsuid);

## [](#DESCRIPTION)DESCRIPTION

           On Linux, a process has both a filesystem user ID and an effective
           user ID.  The (Linux-specific) filesystem user ID is used for
           permissions checking when accessing filesystem objects, while the
           effective user ID is used for various other kinds of permissions
           checks (see credentials(7)).

           Normally, the value of the process's filesystem user ID is the
           same as the value of its effective user ID.  This is so, because
           whenever a process's effective user ID is changed, the kernel also
           changes the filesystem user ID to be the same as the new value of
           the effective user ID.  A process can cause the value of its
           filesystem user ID to diverge from its effective user ID by using
           setfsuid() to change its filesystem user ID to the value given in
           fsuid.

           Explicit calls to setfsuid() and setfsgid(2) are (were) usually
           used only by programs such as the Linux NFS server that need to
           change what user and group ID is used for file access without a
           corresponding change in the real and effective user and group IDs.
           A change in the normal user IDs for a program such as the NFS
           server is (was) a security hole that can expose it to unwanted
           signals.  (However, this issue is historical; see below.)

           setfsuid() will succeed only if the caller is the superuser or if
           fsuid matches either the caller's real user ID, effective user ID,
           saved set-user-ID, or current filesystem user ID.

## [](#RETURN_VALUE)RETURN VALUE

           On both success and failure, this call returns the previous
           filesystem user ID of the caller.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 1.2.

           At the time when this system call was introduced, one process
           could send a signal to another process with the same effective
           user ID.  This meant that if a privileged process changed its
           effective user ID for the purpose of file permission checking,
           then it could become vulnerable to receiving signals sent by
           another (unprivileged) process with the same user ID.  The
           filesystem user ID attribute was thus added to allow a process to
           change its user ID for the purposes of file permission checking
           without at the same time becoming vulnerable to receiving unwanted
           signals.  Since Linux 2.0, signal permission handling is different
           (see kill(2)), with the result that a process can change its
           effective user ID without being vulnerable to receiving signals
           from unwanted processes.  Thus, setfsuid() is nowadays unneeded
           and should be avoided in new applications (likewise for
           setfsgid(2)).

           The original Linux setfsuid() system call supported only 16-bit
           user IDs.  Subsequently, Linux 2.4 added setfsuid32() supporting
           32-bit IDs.  The glibc setfsuid() wrapper function transparently
           deals with the variation across kernel versions.

       C library/kernel differences
           In glibc 2.15 and earlier, when the wrapper for this system call
           determines that the argument can't be passed to the kernel without
           integer truncation (because the kernel is old and does not support
           32-bit user IDs), it will return -1 and set errno to EINVAL
           without attempting the system call.

## [](#BUGS)BUGS

           No error indications of any kind are returned to the caller, and
           the fact that both successful and unsuccessful calls return the
           same value makes it impossible to directly determine whether the
           call succeeded or failed.  Instead, the caller must resort to
           looking at the return value from a further call such as
           setfsuid(-1) (which will always fail), in order to determine if a
           preceding call to setfsuid() changed the filesystem user ID.  At
           the very least, EPERM should be returned when the call fails
           (because the caller lacks the CAP_SETUID capability).

## [](#SEE_ALSO)SEE ALSO

           kill(2), setfsgid(2), capabilities(7), credentials(7)

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

    Linux man-pages 6.19            2026-02-08                    setfsuid(2)

------------------------------------------------------------------------

Pages that refer to this page: [setfsgid(2)](../man2/setfsgid.2.html),  [setresuid(2)](../man2/setresuid.2.html),  [setuid(2)](../man2/setuid.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [capabilities(7)](../man7/capabilities.7.html),  [credentials(7)](../man7/credentials.7.html),  [path_resolution(7)](../man7/path_resolution.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html)

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
