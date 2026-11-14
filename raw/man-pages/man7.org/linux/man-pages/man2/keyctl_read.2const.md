---
{"title": "KEYCTL_READ(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/keyctl_read.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# KEYCTL_READ(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEYCTL_READ(2const)                                   KEYCTL_READ(2const)

## [](#NAME)NAME

           KEYCTL_READ - read a key

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/keyctl.h>  /* Definition of KEY* constants */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(size_t size;
                        SYS_keyctl, KEYCTL_READ, key_serial_t key,
                        char buf[_Nullable size], size_t size);

## [](#DESCRIPTION)DESCRIPTION

           Read the payload data of a key.

           The ID of the key whose payload is to be read is specified in key.
           This can be the ID of an existing key, or any of the special key
           IDs listed for KEYCTL_GET_KEYRING_ID(2const).

           The payload is placed in the buffer pointed by buf; the size of
           that buffer must be specified in size.

           The returned data will be processed for presentation according to
           the key type.  For example, a keyring will return an array of
           key_serial_t entries representing the IDs of all the keys that are
           linked to it.  The user key type will return its data as is.

           If buf is not NULL, as much of the payload data as will fit is
           copied into the buffer.  On a successful return, the return value
           is always the total size of the payload data.  To determine
           whether the buffer was of sufficient size, check to see that the
           return value is less than or equal to the value supplied in size.

           The key must either grant the caller read permission, or grant the
           caller search permission when searched for from the process
           keyrings (i.e., the key is possessed).

## [](#RETURN_VALUE)RETURN VALUE

           On success, the amount of data that is available in the key,
           irrespective of the provided buffer size.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EOPNOTSUPP
                  The key type does not support reading (e.g., the type is
                  "login").

## [](#VERSIONS)VERSIONS

           A wrapper is provided in the libkeyutils library: keyctl_read(3).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.10.

## [](#SEE_ALSO)SEE ALSO

           keyctl(2), keyctl_read(3), keyctl_read_alloc(3)

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

    Linux man-pages 6.19            2026-02-08            KEYCTL_READ(2const)

------------------------------------------------------------------------

Pages that refer to this page: [keyctl(2)](../man2/keyctl.2.html),  [KEYCTL_ASSUME_AUTHORITY(2const)](../man2/KEYCTL_ASSUME_AUTHORITY.2const.html),  [KEYCTL_SETPERM(2const)](../man2/KEYCTL_SETPERM.2const.html)

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
