---
{"title": "KEYCTL_SEARCH(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/keyctl_search.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# KEYCTL_SEARCH(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEYCTL_SEARCH(2const)                               KEYCTL_SEARCH(2const)

## [](#NAME)NAME

           KEYCTL_SEARCH - search a keyring for a key

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/keyctl.h>  /* Definition of KEY* constants */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_keyctl, KEYCTL_SEARCH, key_serial_t src,
                        char *type, char *desc,
                        unsigned long dst);

## [](#DESCRIPTION)DESCRIPTION

           Search for a key in a keyring tree, returning its ID and
           optionally linking it to a specified keyring.

           The tree to be searched is specified by passing the ID of the head
           keyring in src.  The search is performed breadth-first and
           recursively.

           The type and desc arguments specify the key to be searched for:
           type contains the key type (a null-terminated character string up
           to 32 bytes in size, including the terminating null byte), and
           desc contains the description of the key (a null-terminated
           character string up to 4096 bytes in size, including the
           terminating null byte).

           The source keyring must grant search permission to the caller.
           When performing the recursive search, only keyrings that grant the
           caller search permission will be searched.  Only keys with for
           which the caller has search permission can be found.

           If the key is found, its ID is returned as the function result.

           If the key is found and dst is nonzero, then, subject to the same
           constraints and rules as KEYCTL_LINK(2const), the key is linked
           into the keyring whose ID is specified in dst.  If the destination
           keyring specified in dst already contains a link to a key that has
           the same type and description, then that link will be displaced by
           a link to the key found by this operation.

           Instead of valid existing keyring IDs, the source (src) and
           destination (dst) keyrings can be one of the special keyring IDs
           listed under KEYCTL_GET_KEYRING_ID(2const).

## [](#RETURN_VALUE)RETURN VALUE

           On success, the ID of the key that was found.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL The size of the description in desc (including the
                  terminating null byte) exceeded 4096 bytes.

## [](#VERSIONS)VERSIONS

           A wrapper is provided in the libkeyutils library:
           keyctl_search(3).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.10.

## [](#SEE_ALSO)SEE ALSO

           keyctl(2), keyctl_search(3)

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

    Linux man-pages 6.19            2026-02-08          KEYCTL_SEARCH(2const)

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
