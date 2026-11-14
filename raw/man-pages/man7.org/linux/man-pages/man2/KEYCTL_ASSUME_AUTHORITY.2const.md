---
{"title": "KEYCTL_ASSUME_AUTHORITY(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/KEYCTL_ASSUME_AUTHORITY.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# KEYCTL_ASSUME_AUTHORITY(2const) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEYCTL_ASSUME_AUTHORITY(2const)           KEYCTL_ASSUME_AUTHORITY(2const)

## [](#NAME)NAME

           KEYCTL_ASSUME_AUTHORITY - assume the authority to instantiate a
           key

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/keyctl.h>  /* Definition of KEY* constants */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_keyctl, KEYCTL_ASSUME_AUTHORITY, key_serial_t key);

## [](#DESCRIPTION)DESCRIPTION

           Assume (or divest) the authority for the calling thread to
           instantiate a key.

           The key argument specifies either a nonzero key ID to assume
           authority, or the value 0 to divest authority.

           If key is nonzero, then it specifies the ID of an uninstantiated
           key for which authority is to be assumed.  That key can then be
           instantiated using one of KEYCTL_INSTANTIATE(2const),
           KEYCTL_INSTANTIATE_IOV(2const), KEYCTL_REJECT(2const), or
           KEYCTL_NEGATE(2const).  Once the key has been instantiated, the
           thread is automatically divested of authority to instantiate the
           key.

           Authority over a key can be assumed only if the calling thread has
           present in its keyrings the authorization key that is associated
           with the specified key.  (In other words, the
           KEYCTL_ASSUME_AUTHORITY operation is available only from a
           request-key(8)-style program; see request_key(2) for an
           explanation of how this operation is used.)  The caller must have
           search permission on the authorization key.

           If the specified key has a matching authorization key, then the ID
           of that key is returned.  The authorization key can be read
           (KEYCTL_READ(2const)) to obtain the callout information passed to
           request_key(2).

           If the ID given in key is 0, then the currently assumed authority
           is cleared (divested), and the value 0 is returned.

           The KEYCTL_ASSUME_AUTHORITY mechanism allows a program such as
           request-key(8) to assume the necessary authority to instantiate a
           new uninstantiated key that was created as a consequence of a call
           to request_key(2).  For further information, see request_key(2)
           and the kernel source file
           Documentation/security/keys/request-key.rst.

## [](#RETURN_VALUE)RETURN VALUE

           On success, either 0, if the ID given was 0, or the ID of the
           authorization key matching the specified key, if a nonzero key ID
           was provided.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#VERSIONS)VERSIONS

           A wrapper is provided in the libkeyutils library:
           keyctl_assume_authority(3).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.16.

## [](#SEE_ALSO)SEE ALSO

           keyctl(2), keyctl_assume_authority(3)

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

    Linux man-pages 6.19            2026-02-08KEYCTL_ASSUME_AUTHORITY(2const)

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
