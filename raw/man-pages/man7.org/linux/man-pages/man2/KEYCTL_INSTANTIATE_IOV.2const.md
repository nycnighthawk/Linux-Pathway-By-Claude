---
{"title": "KEYCTL_INSTANTIATE(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/KEYCTL_INSTANTIATE_IOV.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# KEYCTL_INSTANTIATE(2const) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEYCTL_INSTANTIATE(2const)                     KEYCTL_INSTANTIATE(2const)

## [](#NAME)NAME

           KEYCTL_INSTANTIATE, KEYCTL_INSTANTIATE_IOV, KEYCTL_NEGATE,
           KEYCTL_REJECT - key instantiation functions

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/keyctl.h>  /* Definition of KEY* constants */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(size_t n;
                        SYS_keyctl, KEYCTL_INSTANTIATE, key_serial_t key,
                        const void payload[n], size_t n,
                        key_serial_t keyring);
           long syscall(size_t n;
                        SYS_keyctl, KEYCTL_INSTANTIATE_IOV, key_serial_t key,
                        const struct iovec payload[n], unsigned int n,
                        key_serial_t keyring);
           long syscall(SYS_keyctl, KEYCTL_NEGATE, key_serial_t key,
                        unsigned int timeout, key_serial_t keyring);
           long syscall(SYS_keyctl, KEYCTL_REJECT, key_serial_t key,
                        unsigned int timeout, int error, key_serial_t keyring);

## [](#DESCRIPTION)DESCRIPTION

           KEYCTL_INSTANTIATE
                  (Positively) instantiate an uninstantiated key with a
                  specified payload.

                  The ID of the key to be instantiated is provided in key.

                  The key payload is specified in the buffer pointed to by
                  payload; the size of that buffer is specified in n.

                  The payload may be a null pointer and the buffer size may
                  be 0 if this is supported by the key type (e.g., it is a
                  keyring).

                  The operation may be fail if the payload data is in the
                  wrong format or is otherwise invalid.

                  If keyring is nonzero, then, subject to the same
                  constraints and rules as KEYCTL_LINK(2const), the
                  instantiated key is linked into the keyring whose ID
                  specified in keyring.

                  The caller must have the appropriate authorization key, and
                  once the uninstantiated key has been instantiated, the
                  authorization key is revoked.  In other words, this
                  operation is available only from a request-key(8)-style
                  program.  See request_key(2) for an explanation of
                  uninstantiated keys and key instantiation.

           KEYCTL_INSTANTIATE_IOV
                  Instantiate an uninstantiated key with a payload specified
                  via a vector of buffers.

                  This operation is the same as KEYCTL_INSTANTIATE, but the
                  payload data is specified as an array of iovec structures
                  (see iovec(3type)).

                  The pointer to the payload vector is specified in payload.
                  The number of items in the vector is specified in n.

                  The key and keyring are interpreted as for
                  KEYCTL_INSTANTIATE.

           KEYCTL_NEGATE
                  Negatively instantiate an uninstantiated key.

                  This operation is equivalent to the call:

                      keyctl(KEYCTL_REJECT, key, timeout, ENOKEY, keyring);

           KEYCTL_REJECT
                  Mark a key as negatively instantiated and set an expiration
                  timer on the key.  This operation provides a superset of
                  the functionality of the earlier KEYCTL_NEGATE operation.

                  The ID of the key that is to be negatively instantiated is
                  specified in key.  The timeout argument specifies the
                  lifetime of the key, in seconds.  The error argument
                  specifies the error to be returned when a search hits this
                  key; typically, this is one of EKEYREJECTED, EKEYREVOKED,
                  or EKEYEXPIRED.

                  If keyring is nonzero, then, subject to the same
                  constraints and rules as KEYCTL_LINK(2const), the
                  negatively instantiated key is linked into the keyring
                  whose ID is specified in keyring.

                  The caller must have the appropriate authorization key.  In
                  other words, this operation is available only from a
                  request-key(8)-style program.  See request_key(2).

                  The caller must have the appropriate authorization key, and
                  once the uninstantiated key has been instantiated, the
                  authorization key is revoked.  In other words, this
                  operation is available only from a request-key(8)-style
                  program.  See request_key(2) for an explanation of
                  uninstantiated keys and key instantiation.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#VERSIONS)VERSIONS

           Wrappers are provided in the libkeyutils library:
           keyctl_instantiate(3), keyctl_instantiate_iov(3),
           keyctl_negate(3), and keyctl_reject(3).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           KEYCTL_INSTANTIATE
           KEYCTL_NEGATE
                  Linux 2.6.10.

           KEYCTL_INSTANTIATE_IOV
           KEYCTL_REJECT
                  Linux 2.6.39.

## [](#SEE_ALSO)SEE ALSO

           keyctl(2), keyctl_instantiate(3), keyctl_instantiate_iov(3),
           keyctl_negate(3), keyctl_reject(3)

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

    Linux man-pages 6.19            2026-02-08     KEYCTL_INSTANTIATE(2const)

------------------------------------------------------------------------

Pages that refer to this page: [keyctl(2)](../man2/keyctl.2.html),  [KEYCTL_ASSUME_AUTHORITY(2const)](../man2/KEYCTL_ASSUME_AUTHORITY.2const.html),  [KEYCTL_UPDATE(2const)](../man2/KEYCTL_UPDATE.2const.html)

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
