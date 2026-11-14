---
{"title": "KEYCTL_GET_KEYRING_ID(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/KEYCTL_GET_KEYRING_ID.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# KEYCTL_GET_KEYRING_ID(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEYCTL_GET_KEYRING_ID(2const)               KEYCTL_GET_KEYRING_ID(2const)

## [](#NAME)NAME

           KEYCTL_GET_KEYRING_ID - map a special key ID to a real key ID for
           this process

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/keyctl.h>  /* Definition of KEY* constants */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_keyctl, KEYCTL_GET_KEYRING_ID, key_serial_t key,
                        int arg3);

## [](#DESCRIPTION)DESCRIPTION

           Map a special key ID to a real key ID for this process.

           This operation looks up the special key whose ID is provided in
           key.  If the special key is found, the ID of the corresponding
           real key is returned as the function result.  The following values
           may be specified in key:

           KEY_SPEC_THREAD_KEYRING
                  This specifies the calling thread's thread-specific
                  keyring.  See thread-keyring(7).

           KEY_SPEC_PROCESS_KEYRING
                  This specifies the caller's process-specific keyring.  See
                  process-keyring(7).

           KEY_SPEC_SESSION_KEYRING
                  This specifies the caller's session-specific keyring.  See
                  session-keyring(7).

           KEY_SPEC_USER_KEYRING
                  This specifies the caller's UID-specific keyring.  See
                  user-keyring(7).

           KEY_SPEC_USER_SESSION_KEYRING
                  This specifies the caller's UID-session keyring.  See
                  user-session-keyring(7).

           KEY_SPEC_REQKEY_AUTH_KEY (since Linux 2.6.16)
                  This specifies the authorization key created by
                  request_key(2) and passed to the process it spawns to
                  generate a key.  This key is available only in a
                  request-key(8)-style program that was passed an
                  authorization key by the kernel and ceases to be available
                  once the requested key has been instantiated; see
                  request_key(2).

           KEY_SPEC_REQUESTOR_KEYRING (since Linux 2.6.29)
                  This specifies the key ID for the request_key(2)
                  destination keyring.  This keyring is available only in a
                  request-key(8)-style program that was passed an
                  authorization key by the kernel and ceases to be available
                  once the requested key has been instantiated; see
                  request_key(2).

           The behavior if the key specified in key does not exist depends on
           the value of arg3.  If arg3 contains a nonzero value, then —if it
           is appropriate to do so (e.g., when looking up the user, user-
           session, or session key)— a new key is created and its real key ID
           returned as the function result.  Otherwise, the operation fails
           with the error ENOKEY.

           If a valid key ID is specified in key, and the key exists, then
           this operation simply returns the key ID.  If the key does not
           exist, the call fails with error ENOKEY.

           The caller must have search permission on a keyring in order for
           it to be found.

## [](#RETURN_VALUE)RETURN VALUE

           On success, the ID of the requested keyring.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           ENOKEY The key specified in key did not exist, and arg3 was zero
                  (meaning don't create the key if it didn't exist).

## [](#VERSIONS)VERSIONS

           A wrapper is provided in the libkeyutils library:
           keyctl_get_keyring_ID(3).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.10.

## [](#SEE_ALSO)SEE ALSO

           keyctl(2), keyctl_get_keyring_ID(3)

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

    Linux man-pages 6.19            2026-02-08  KEYCTL_GET_KEYRING_ID(2const)

------------------------------------------------------------------------

Pages that refer to this page: [keyctl(2)](../man2/keyctl.2.html),  [KEYCTL_READ(2const)](../man2/KEYCTL_READ.2const.html),  [KEYCTL_SEARCH(2const)](../man2/KEYCTL_SEARCH.2const.html),  [KEYCTL_SETPERM(2const)](../man2/KEYCTL_SETPERM.2const.html)

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
