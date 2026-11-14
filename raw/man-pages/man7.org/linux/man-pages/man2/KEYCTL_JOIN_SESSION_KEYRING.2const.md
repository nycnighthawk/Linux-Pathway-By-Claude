---
{"title": "KEYCTL_JOIN_SESSION_KEYRING(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/KEYCTL_JOIN_SESSION_KEYRING.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# KEYCTL_JOIN_SESSION_KEYRING(2const) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEYCTL_JOIN_SESSION_KEYRING(2const)   KEYCTL_JOIN_SESSION_KEYRING(2const)

## [](#NAME)NAME

           KEYCTL_JOIN_SESSION_KEYRING - replace the session keyring this
           process subscribes to with a new one

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/keyctl.h>  /* Definition of KEY* constants */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_keyctl, KEYCTL_JOIN_SESSION_KEYRING,
                        char *_Nullable desc);

## [](#DESCRIPTION)DESCRIPTION

           Replace the session keyring this process subscribes to with a new
           session keyring.

           If desc is NULL, an anonymous keyring with the description "_ses"
           is created and the process is subscribed to that keyring as its
           session keyring, displacing the previous session keyring.

           Otherwise, desc is treated as the description (name) of a keyring,
           and the behavior is as follows:

           •  If a keyring with a matching description exists, the process
              will attempt to subscribe to that keyring as its session
              keyring if possible; if that is not possible, an error is
              returned.  In order to subscribe to the keyring, the caller
              must have search permission on the keyring.

           •  If a keyring with a matching description does not exist, then a
              new keyring with the specified description is created, and the
              process is subscribed to that keyring as its session keyring.

## [](#RETURN_VALUE)RETURN VALUE

           On success, the ID of the joined session keyring.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#VERSIONS)VERSIONS

           A wrapper is provided in the libkeyutils library:
           keyctl_join_session_keyring(3).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.10.

## [](#SEE_ALSO)SEE ALSO

           keyctl(2), keyctl_join_session_keyring(3)

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

    Linux man-pages 6.19            2026-02K-E0Y8CTL_JOIN_SESSION_KEYRING(2const)

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
