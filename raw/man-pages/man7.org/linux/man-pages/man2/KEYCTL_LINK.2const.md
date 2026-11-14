---
{"title": "KEYCTL_LINK(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/KEYCTL_LINK.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# KEYCTL_LINK(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEYCTL_LINK(2const)                                   KEYCTL_LINK(2const)

## [](#NAME)NAME

           KEYCTL_LINK - link a key to a keyring

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/keyctl.h>  /* Definition of KEY* constants */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_keyctl, KEYCTL_LINK, key_serial_t key,
                        key_serial_t keyring);

## [](#DESCRIPTION)DESCRIPTION

           Create a link from a keyring to a key.

           The key to be linked is specified in key; the keyring is specified
           in keyring.

           If a key with the same type and description is already linked in
           the keyring, then that key is displaced from the keyring.

           Before creating the link, the kernel checks the nesting of the
           keyrings and returns appropriate errors if the link would produce
           a cycle or if the nesting of keyrings would be too deep (The limit
           on the nesting of keyrings is determined by the kernel constant
           KEYRING_SEARCH_MAX_DEPTH, defined with the value 6, and is
           necessary to prevent overflows on the kernel stack when
           recursively searching keyrings).

           The caller must have link permission on the key being added and
           write permission on the keyring.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EDEADLK
                  The requested link would result in a cycle.

           ELOOP  The requested link would cause the maximum nesting depth
                  for keyrings to be exceeded.

           ENFILE (before Linux 3.13)
                  The keyring is full.  (Before Linux 3.13, the available
                  space for storing keyring links was limited to a single
                  page of memory; since Linux 3.13, there is no fixed limit.)

## [](#VERSIONS)VERSIONS

           A wrapper is provided in the libkeyutils library: keyctl_link(3).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.10.

## [](#SEE_ALSO)SEE ALSO

           keyctl(2), keyctl_link(3), KEYCTL_UNLINK(2const)

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

    Linux man-pages 6.19            2026-02-08            KEYCTL_LINK(2const)

------------------------------------------------------------------------

Pages that refer to this page: [keyctl(2)](../man2/keyctl.2.html),  [KEYCTL_INSTANTIATE(2const)](../man2/KEYCTL_INSTANTIATE.2const.html),  [KEYCTL_SEARCH(2const)](../man2/KEYCTL_SEARCH.2const.html),  [KEYCTL_SETPERM(2const)](../man2/KEYCTL_SETPERM.2const.html),  [KEYCTL_UNLINK(2const)](../man2/KEYCTL_UNLINK.2const.html)

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
