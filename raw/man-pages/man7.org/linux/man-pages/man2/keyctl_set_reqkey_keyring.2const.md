---
{"title": "KEYCTL_SET_REQKEY_KEYRING(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/keyctl_set_reqkey_keyring.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# KEYCTL_SET_REQKEY_KEYRING(2const) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEYCTL_SET_REQKEY_KEYRING(2const)       KEYCTL_SET_REQKEY_KEYRING(2const)

## [](#NAME)NAME

           KEYCTL_SET_REQKEY_KEYRING - set the implicit destination keyring

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/keyctl.h>  /* Definition of KEY* constants */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_keyctl, KEYCTL_SET_REQKEY_KEYRING, int op);

## [](#DESCRIPTION)DESCRIPTION

           Set the default keyring to which implicitly requested keys will be
           linked for this thread, and return the previous setting.  Implicit
           key requests are those made by internal kernel components, such as
           can occur when, for example, opening files on an AFS or NFS
           filesystem.  Setting the default keyring also has an effect when
           requesting a key from user space; see request_key(2) for details.

           The op argument should contain one of the following values, to
           specify the new default keyring:

           KEY_REQKEY_DEFL_NO_CHANGE
                  Don't change the default keyring.  This can be used to
                  discover the current default keyring (without changing it).

           KEY_REQKEY_DEFL_DEFAULT
                  This selects the default behavior, which is to use the
                  thread-specific keyring if there is one, otherwise the
                  process-specific keyring if there is one, otherwise the
                  session keyring if there is one, otherwise the UID-specific
                  session keyring, otherwise the user-specific keyring.

           KEY_REQKEY_DEFL_THREAD_KEYRING
                  Use the thread-specific keyring (thread-keyring(7)) as the
                  new default keyring.

           KEY_REQKEY_DEFL_PROCESS_KEYRING
                  Use the process-specific keyring (process-keyring(7)) as
                  the new default keyring.

           KEY_REQKEY_DEFL_SESSION_KEYRING
                  Use the session-specific keyring (session-keyring(7)) as
                  the new default keyring.

           KEY_REQKEY_DEFL_USER_KEYRING
                  Use the UID-specific keyring (user-keyring(7)) as the new
                  default keyring.

           KEY_REQKEY_DEFL_USER_SESSION_KEYRING
                  Use the UID-specific session keyring
                  (user-session-keyring(7)) as the new default keyring.

           KEY_REQKEY_DEFL_REQUESTOR_KEYRING (since Linux 2.6.29)
                  Use the requestor keyring.

           All other values are invalid.

           The setting controlled by this operation is inherited by the child
           of fork(2) and preserved across execve(2).

## [](#RETURN_VALUE)RETURN VALUE

           On success, the ID of the previous default keyring to which
           implicitly requested keys were linked (one of
           KEY_REQKEY_DEFL_USER_*).

           On error, -1 is returned, and errno is set to indicate the error.

## [](#VERSIONS)VERSIONS

           A wrapper is provided in the libkeyutils library:
           keyctl_set_reqkey_keyring(3)

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.13.

## [](#SEE_ALSO)SEE ALSO

           keyctl(2), keyctl_set_reqkey_keyring(3)

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

    Linux man-pages 6.19            2026-02-0K8EYCTL_SET_REQKEY_KEYRING(2const)

------------------------------------------------------------------------

Pages that refer to this page: [keyctl(2)](../man2/keyctl.2.html)

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
