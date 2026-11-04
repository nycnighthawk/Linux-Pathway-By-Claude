---
{"title": "add_key(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/add_key.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# add_key(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    add_key(2)                 System Calls Manual                 add_key(2)

## [](#NAME)NAME

           add_key - add a key to the kernel's key management facility

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <keyutils.h>

           key_serial_t add_key(size_t size;
                                const char *type, const char *description,
                                const void payload[size], size_t size,
                                key_serial_t keyring);

           Note: There is no glibc wrapper for this system call; see NOTES.

## [](#DESCRIPTION)DESCRIPTION

           add_key() creates or updates a key of the given type and
           description, instantiates it with the payload of size size,
           attaches it to the nominated keyring, and returns the key's serial
           number.

           The key may be rejected if the provided data is in the wrong
           format or it is invalid in some other way.

           If the destination keyring already contains a key that matches the
           specified type and description, then, if the key type supports it,
           that key will be updated rather than a new key being created; if
           not, a new key (with a different ID) will be created and it will
           displace the link to the extant key from the keyring.

           The destination keyring serial number may be that of a valid
           keyring for which the caller has write permission.  Alternatively,
           it may be one of the following special keyring IDs:

           KEY_SPEC_THREAD_KEYRING
                  This specifies the caller's thread-specific keyring
                  (thread-keyring(7)).

           KEY_SPEC_PROCESS_KEYRING
                  This specifies the caller's process-specific keyring
                  (process-keyring(7)).

           KEY_SPEC_SESSION_KEYRING
                  This specifies the caller's session-specific keyring
                  (session-keyring(7)).

           KEY_SPEC_USER_KEYRING
                  This specifies the caller's UID-specific keyring
                  (user-keyring(7)).

           KEY_SPEC_USER_SESSION_KEYRING
                  This specifies the caller's UID-session keyring
                  (user-session-keyring(7)).

       Key types
           The key type is a string that specifies the key's type.
           Internally, the kernel defines a number of key types that are
           available in the core key management code.  Among the types that
           are available for user-space use and can be specified as the type
           argument to add_key() are the following:

           "keyring"
                  Keyrings are special key types that may contain links to
                  sequences of other keys of any type.  If this interface is
                  used to create a keyring, then payload should be NULL and
                  size should be zero.

           "user" This is a general purpose key type whose payload may be
                  read and updated by user-space applications.  The key is
                  kept entirely within kernel memory.  The payload for keys
                  of this type is a blob of arbitrary data of up to 32,767
                  bytes.

           "logon" (since Linux 3.3)
                  This key type is essentially the same as "user", but it
                  does not permit the key to read.  This is suitable for
                  storing payloads that you do not want to be readable from
                  user space.

           This key type vets the description to ensure that it is qualified
           by a "service" prefix, by checking to ensure that the description
           contains a ':' that is preceded by other characters.

           "big_key" (since Linux 3.13)
                  This key type is similar to "user", but may hold a payload
                  of up to 1 MiB.  If the key payload is large enough, then
                  it may be stored encrypted in tmpfs (which can be swapped
                  out) rather than kernel memory.

           For further details on these key types, see keyrings(7).

## [](#RETURN_VALUE)RETURN VALUE

           On success, add_key() returns the serial number of the key it
           created or updated.  On error, -1 is returned and errno is set to
           indicate the error.

## [](#ERRORS)ERRORS

           EACCES The keyring wasn't available for modification by the user.

           EDQUOT The key quota for this user would be exceeded by creating
                  this key or linking it to the keyring.

           EFAULT One or more of type, description, and payload points
                  outside process's accessible address space.

           EINVAL The size of the string (including the terminating null
                  byte) specified in type or description exceeded the limit
                  (32 bytes and 4096 bytes respectively).

           EINVAL The payload data was invalid.

           EINVAL type was "logon" and the description was not qualified with
                  a prefix string of the form "service:".

           EKEYEXPIRED
                  The keyring has expired.

           EKEYREVOKED
                  The keyring has been revoked.

           ENOKEY The keyring doesn't exist.

           ENOMEM Insufficient memory to create a key.

           EPERM  The type started with a period ('.').  Key types that begin
                  with a period are reserved to the implementation.

           EPERM  type was "keyring" and the description started with a
                  period ('.').  Keyrings with descriptions (names) that
                  begin with a period are reserved to the implementation.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.10.

## [](#NOTES)NOTES

           glibc does not provide a wrapper for this system call.  A wrapper
           is provided in the libkeyutils library.  (The accompanying package
           provides the <keyutils.h> header file.)  When employing the
           wrapper in that library, link with -lkeyutils.

## [](#EXAMPLES)EXAMPLES

           The program below creates a key with the type, description, and
           payload specified in its command-line arguments, and links that
           key into the session keyring.  The following shell session
           demonstrates the use of the program:

               $ ./a.out user mykey "Some payload";
               Key ID is 64a4dca
               $ grep '64a4dca' /proc/keys;
               064a4dca I--Q---    1 perm 3f010000  1000  1000 user    mykey: 12

       Program source

           #include <keyutils.h>
           #include <stdint.h>
           #include <stdio.h>
           #include <stdlib.h>
           #include <string.h>

           int
           main(int argc, char *argv[])
           {
               key_serial_t key;

               if (argc != 4) {
                   fprintf(stderr, "Usage: %s type description payload\n",
                           argv[0]);
                   exit(EXIT_FAILURE);
               }

               key = add_key(argv[1], argv[2], argv[3], strlen(argv[3]),
                             KEY_SPEC_SESSION_KEYRING);
               if (key == -1) {
                   perror("add_key");
                   exit(EXIT_FAILURE);
               }

               printf("Key ID is %jx\n", (uintmax_t) key);

               exit(EXIT_SUCCESS);
           }

## [](#SEE_ALSO)SEE ALSO

           keyctl(1), keyctl(2), request_key(2), keyctl(3), keyrings(7),
           keyutils(7), persistent-keyring(7), process-keyring(7),
           session-keyring(7), thread-keyring(7), user-keyring(7),
           user-session-keyring(7)

           The kernel source files Documentation/security/keys/core.rst and
           Documentation/keys/request-key.rst.

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

    Linux man-pages 6.19            2026-02-08                     add_key(2)

------------------------------------------------------------------------

Pages that refer to this page: [keyctl(2)](../man2/keyctl.2.html),  [request_key(2)](../man2/request_key.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [keyctl(3)](../man3/keyctl.3.html),  [keyctl_capabilities(3)](../man3/keyctl_capabilities.3.html),  [keyctl_chown(3)](../man3/keyctl_chown.3.html),  [keyctl_clear(3)](../man3/keyctl_clear.3.html),  [keyctl_describe(3)](../man3/keyctl_describe.3.html),  [keyctl_get_keyring_ID(3)](../man3/keyctl_get_keyring_ID.3.html),  [keyctl_get_persistent(3)](../man3/keyctl_get_persistent.3.html),  [keyctl_get_security(3)](../man3/keyctl_get_security.3.html),  [keyctl_instantiate(3)](../man3/keyctl_instantiate.3.html),  [keyctl_invalidate(3)](../man3/keyctl_invalidate.3.html),  [keyctl_join_session_keyring(3)](../man3/keyctl_join_session_keyring.3.html),  [keyctl_link(3)](../man3/keyctl_link.3.html),  [keyctl_move(3)](../man3/keyctl_move.3.html),  [keyctl_pkey_encrypt(3)](../man3/keyctl_pkey_encrypt.3.html),  [keyctl_pkey_query(3)](../man3/keyctl_pkey_query.3.html),  [keyctl_pkey_sign(3)](../man3/keyctl_pkey_sign.3.html),  [keyctl_read(3)](../man3/keyctl_read.3.html),  [keyctl_revoke(3)](../man3/keyctl_revoke.3.html),  [keyctl_search(3)](../man3/keyctl_search.3.html),  [keyctl_session_to_parent(3)](../man3/keyctl_session_to_parent.3.html),  [keyctl_setperm(3)](../man3/keyctl_setperm.3.html),  [keyctl_set_reqkey_keyring(3)](../man3/keyctl_set_reqkey_keyring.3.html),  [keyctl_set_timeout(3)](../man3/keyctl_set_timeout.3.html),  [keyctl_update(3)](../man3/keyctl_update.3.html),  [keyctl_watch_key(3)](../man3/keyctl_watch_key.3.html),  [proc_pid_attr(5)](../man5/proc_pid_attr.5.html),  [asymmetric-key(7)](../man7/asymmetric-key.7.html),  [keyrings(7)](../man7/keyrings.7.html),  [keyutils(7)](../man7/keyutils.7.html)

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
