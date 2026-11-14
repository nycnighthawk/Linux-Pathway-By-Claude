---
{"title": "KEYCTL_GET_PERSISTENT(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/keyctl_get_persistent.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# KEYCTL_GET_PERSISTENT(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEYCTL_GET_PERSISTENT(2const)               KEYCTL_GET_PERSISTENT(2const)

## [](#NAME)NAME

           KEYCTL_GET_PERSISTENT - get the persistent keyring for a user

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/keyctl.h>  /* Definition of KEY* constants */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_keyctl, KEYCTL_GET_PERSISTENT, uid_t uid,
                        key_serial_t keyring);

## [](#DESCRIPTION)DESCRIPTION

           Get the persistent keyring (persistent-keyring(7)) for a specified
           user and link it to a specified keyring.

           The user ID is specified in uid.  If the value -1 is specified,
           the caller's real user ID is used.  The ID of the destination
           keyring is specified in keyring.

           The caller must have the CAP_SETUID capability in its user
           namespace in order to fetch the persistent keyring for a user ID
           that does not match either the real or effective user ID of the
           caller.

           If the call is successful, a link to the persistent keyring is
           added to the keyring whose ID was specified in keyring.

           The caller must have write permission on the keyring.

           The persistent keyring will be created by the kernel if it does
           not yet exist.

           Each time the KEYCTL_GET_PERSISTENT operation is performed, the
           persistent keyring will have its expiration timeout reset to the
           value in:

               /proc/sys/kernel/keys/persistent_keyring_expiry

           Should the timeout be reached, the persistent keyring will be
           removed and everything it pins can then be garbage collected.

           Persistent keyrings were added in Linux 3.13.

## [](#RETURN_VALUE)RETURN VALUE

           On success, the ID of the persistent keyring.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EPERM  uid specified a UID other than the calling thread's real or
                  effective UID, and the caller did not have the CAP_SETUID
                  capability.

## [](#VERSIONS)VERSIONS

           A wrapper is provided in the libkeyutils library:
           keyctl_get_persistent(3).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 3.13.

## [](#SEE_ALSO)SEE ALSO

           keyctl(2), keyctl_get_persistent(3)

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

    Linux man-pages 6.19            2026-02-08  KEYCTL_GET_PERSISTENT(2const)

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
