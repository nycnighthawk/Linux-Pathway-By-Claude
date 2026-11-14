---
{"title": "KEYCTL_DESCRIBE(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/KEYCTL_DESCRIBE.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# KEYCTL_DESCRIBE(2const) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEYCTL_DESCRIBE(2const)                           KEYCTL_DESCRIBE(2const)

## [](#NAME)NAME

           KEYCTL_DESCRIBE - describe a key

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/keyctl.h>  /* Definition of KEY* constants */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(size_t size;
                        SYS_keyctl, KEYCTL_DESCRIBE, key_serial_t key,
                        char desc[_Nullable size], size_t size);

## [](#DESCRIPTION)DESCRIPTION

           Obtain a string describing the attributes of a specified key.

           The ID of the key to be described is specified in key.  The
           descriptive string is returned in the buffer pointed to by desc;
           size specifies the size of that buffer in bytes.

           The key must grant the caller view permission.

           The returned string is null-terminated and contains the following
           information about the key:

               type;uid;gid;perm;description

           In the above, type and description are strings, uid and gid are
           decimal strings, and perm is a hexadecimal permissions mask.  The
           descriptive string is written with the following format:

               %s;%d;%d;%08x;%s

           Note: the intention is that the descriptive string should be
           extensible in future kernel versions.  In particular, the
           description field will not contain semicolons; it should be parsed
           by working backwards from the end of the string to find the last
           semicolon.  This allows future semicolon-delimited fields to be
           inserted in the descriptive string in the future.

           Writing to the buffer is attempted only when desc is non-NULL and
           the specified buffer size is large enough to accept the
           descriptive string (including the terminating null byte).  In
           order to determine whether the buffer size was too small, check to
           see if the return value of the operation is greater than size.

## [](#RETURN_VALUE)RETURN VALUE

           On success, the size of the description (including the terminating
           null byte), irrespective of the provided buffer size.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#VERSIONS)VERSIONS

           A wrapper is provided in the libkeyutils library:
           keyctl_describe(3).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.10.

## [](#SEE_ALSO)SEE ALSO

           keyctl(2), keyctl_describe(3), keyctl_describe_alloc(3)

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

    Linux man-pages 6.19            2026-02-08        KEYCTL_DESCRIBE(2const)

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
