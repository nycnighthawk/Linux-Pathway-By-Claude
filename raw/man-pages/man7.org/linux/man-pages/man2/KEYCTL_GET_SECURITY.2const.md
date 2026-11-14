---
{"title": "KEYCTL_GET_SECURITY(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/KEYCTL_GET_SECURITY.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# KEYCTL_GET_SECURITY(2const) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEYCTL_GET_SECURITY(2const)                   KEYCTL_GET_SECURITY(2const)

## [](#NAME)NAME

           KEYCTL_GET_SECURITY - manipulate the kernel's key management
           facility

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/keyctl.h>  /* Definition of KEY* constants */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(size_t n;
                        SYS_keyctl, KEYCTL_GET_SECURITY, key_serial_t key,
                        char buf[_Nullable n], size_t n);

## [](#DESCRIPTION)DESCRIPTION

           KEYCTL_GET_SECURITY (since Linux 2.6.26)
                  Get the LSM (Linux Security Module) security label of the
                  specified key.

           The ID of the key whose security label is to be fetched is
           specified in key.  The security label (terminated by a null byte)
           will be placed in the buffer pointed to by buf argument; the size
           of the buffer must be provided in n.

           If buf is specified as NULL or the buffer size specified in n is
           too small, the full size of the security label string (including
           the terminating null byte) is returned as the function result, and
           nothing is copied to the buffer.

           The caller must have view permission on the specified key.

           The returned security label string will be rendered in a form
           appropriate to the LSM in force.  For example, with SELinux, it
           may look like:

               unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023

           If no LSM is currently in force, then an empty string is placed in
           the buffer.

## [](#RETURN_VALUE)RETURN VALUE

           On success, the size of the LSM security label string (including
           the terminating null byte), irrespective of the provided buffer
           size.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#VERSIONS)VERSIONS

           A wrapper is provided in the libkeyutils library:
           keyctl_get_security(3).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.26.

## [](#SEE_ALSO)SEE ALSO

           keyctl(2), keyctl_get_security(3), keyctl_get_security_alloc(3)

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

    Linux man-pages 6.19            2026-02-08    KEYCTL_GET_SECURITY(2const)

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
