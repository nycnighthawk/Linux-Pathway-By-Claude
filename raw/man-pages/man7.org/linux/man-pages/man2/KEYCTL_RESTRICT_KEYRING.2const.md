---
{"title": "KEYCTL_RESTRICT_KEYRING(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/KEYCTL_RESTRICT_KEYRING.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# KEYCTL_RESTRICT_KEYRING(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEYCTL_RESTRICT_KEYRING(2const)           KEYCTL_RESTRICT_KEYRING(2const)

## [](#NAME)NAME

           KEYCTL_RESTRICT_KEYRING - restrict keys that may be linked to a
           keyring

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/keyctl.h>  /* Definition of KEY* constants */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_keyctl, KEYCTL_RESTRICT_KEYRING, key_serial_t keyring,
                        const char *_Nullable type, const char *restriction);

## [](#DESCRIPTION)DESCRIPTION

           Apply a key-linking restriction to the keyring with the ID
           provided in keyring.  The caller must have setattr permission on
           the key.  If type is NULL, any attempt to add a key to the keyring
           is blocked; otherwise it contains a pointer to a string with a key
           type name and restriction contains a pointer to string that
           describes the type-specific restriction.  As of Linux 4.12, only
           the type "asymmetric" has restrictions defined:

           builtin_trusted
                  Allows only keys that are signed by a key linked to the
                  built-in keyring (".builtin_trusted_keys").

           builtin_and_secondary_trusted
                  Allows only keys that are signed by a key linked to the
                  secondary keyring (".secondary_trusted_keys") or, by
                  extension, a key in a built-in keyring, as the latter is
                  linked to the former.

           key_or_keyring:key
           key_or_keyring:key:chain
                  If key specifies the ID of a key of type "asymmetric", then
                  only keys that are signed by this key are allowed.

                  If key specifies the ID of a keyring, then only keys that
                  are signed by a key linked to this keyring are allowed.

                  If ":chain" is specified, keys that are signed by a keys
                  linked to the destination keyring (that is, the keyring
                  with the ID specified in the keyring argument) are also
                  allowed.

           Note that a restriction can be configured only once for the
           specified keyring; once a restriction is set, it can't be
           overridden.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EDEADLK
                  The requested keyring restriction would result in a cycle.

           EEXIST keyring already has a restriction set.

           ENOENT The type provided in type argument doesn't support setting
                  key linking restrictions.

           EOPNOTSUPP
                  type was "asymmetric", and the key specified in the
                  restriction specification provided in restriction has type
                  other than "asymmetric" or "keyring".

## [](#VERSIONS)VERSIONS

           A wrapper is provided in the libkeyutils library:
           keyctl_restrict_keyring(3).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 4.12.

## [](#SEE_ALSO)SEE ALSO

           keyctl(2), keyctl_restrict_keyring(3)

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

    Linux man-pages 6.19            2026-02-08KEYCTL_RESTRICT_KEYRING(2const)

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
