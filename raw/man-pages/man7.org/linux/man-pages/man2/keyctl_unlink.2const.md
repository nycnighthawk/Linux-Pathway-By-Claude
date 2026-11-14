---
{"title": "KEYCTL_UNLINK(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/keyctl_unlink.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# KEYCTL_UNLINK(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEYCTL_UNLINK(2const)                               KEYCTL_UNLINK(2const)

## [](#NAME)NAME

           KEYCTL_UNLINK - unlink a key from a keyring

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/keyctl.h>  /* Definition of KEY* constants */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_keyctl, KEYCTL_UNLINK, key_serial_t key,
                        key_serial_t keyring);

## [](#DESCRIPTION)DESCRIPTION

           Unlink a key from a keyring.

           The ID of the key to be unlinked is specified in key; the ID of
           the keyring from which it is to be unlinked is specified in
           keyring.

           If the key is not currently linked into the keyring, an error
           results.

           The caller must have write permission on the keyring from which
           the key is being removed.

           If the last link to a key is removed, then that key will be
           scheduled for destruction.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           ENOENT The key to be unlinked isn't linked to the keyring.

## [](#VERSIONS)VERSIONS

           A wrapper is provided in the libkeyutils library:
           keyctl_unlink(3).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.10.

## [](#SEE_ALSO)SEE ALSO

           keyctl(2), keyctl_unlink(3), KEYCTL_LINK(2const)

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

    Linux man-pages 6.19            2026-02-08          KEYCTL_UNLINK(2const)

------------------------------------------------------------------------

Pages that refer to this page: [keyctl(2)](../man2/keyctl.2.html),  [KEYCTL_LINK(2const)](../man2/KEYCTL_LINK.2const.html),  [KEYCTL_SETPERM(2const)](../man2/KEYCTL_SETPERM.2const.html)

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
