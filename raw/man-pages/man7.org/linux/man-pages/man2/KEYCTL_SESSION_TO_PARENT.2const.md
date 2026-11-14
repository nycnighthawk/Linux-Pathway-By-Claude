---
{"title": "KEYCTL_SESSION_TO_PARENT(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/KEYCTL_SESSION_TO_PARENT.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# KEYCTL_SESSION_TO_PARENT(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEYCTL_SESSION_TO_PARENT(2const)         KEYCTL_SESSION_TO_PARENT(2const)

## [](#NAME)NAME

           KEYCTL_SESSION_TO_PARENT - set the parent process's session
           keyring

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/keyctl.h>  /* Definition of KEY* constants */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_keyctl, KEYCTL_SESSION_TO_PARENT);

## [](#DESCRIPTION)DESCRIPTION

           Replace the session keyring to which the parent of the calling
           process subscribes with the session keyring of the calling
           process.

           The keyring will be replaced in the parent process at the point
           where the parent next transitions from kernel space to user space.

           The keyring must exist and must grant the caller link permission.
           The parent process must be single-threaded and have the same
           effective ownership as this process and must not be set-user-ID or
           set-group-ID.  The UID of the parent process's existing session
           keyring (f it has one), as well as the UID of the caller's session
           keyring much match the caller's effective UID.

           The fact that it is the parent process that is affected by this
           operation allows a program such as the shell to start a child
           process that uses this operation to change the shell's session
           keyring.  (This is what the keyctl(1) new_session command does.)

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EPERM  All of the UIDs (GIDs) of the parent process do not match
                  the effective UID (GID) of the calling process.

           EPERM  The UID of the parent's existing session keyring or the UID
                  of the caller's session keyring did not match the effective
                  UID of the caller.

           EPERM  The parent process is not single-threaded.

           EPERM  The parent process is init(1) or a kernel thread.

## [](#VERSIONS)VERSIONS

           A wrapper is provided in the libkeyutils library:
           keyctl_session_to_parent(3).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.32.

## [](#SEE_ALSO)SEE ALSO

           keyctl(2), keyctl_session_to_parent(3)

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

    Linux man-pages 6.19            2026-02-08KEYCTL_SESSION_TO_PARENT(2const)

------------------------------------------------------------------------

Pages that refer to this page: [keyctl(2)](../man2/keyctl.2.html),  [KEYCTL_SETPERM(2const)](../man2/KEYCTL_SETPERM.2const.html)

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
