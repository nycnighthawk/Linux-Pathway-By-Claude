---
{"title": "keyutils(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/keyutils.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# keyutils(7) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [UTILITIES](#UTILITIES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEYUTILS(7)               Kernel key management               KEYUTILS(7)

## [](#NAME)NAME

           keyutils - in-kernel key management utilities

## [](#DESCRIPTION)DESCRIPTION

           The keyutils package is a library and a set of utilities for
           accessing the kernel keyrings facility.

           A header file is supplied to provide the definitions and
           declarations required to access the library:

                  #include <keyutils.h>

           To link with the library, the following:

                  -lkeyutils

           should be specified to the linker.

           Three system calls are provided:

           add_key(2)
                  Supply a new key to the kernel.

           request_key(2)
                  Find an existing key for use, or, optionally, create one if
                  one does not exist.

           keyctl(2)
                  Control a key in various ways.  The library provides a
                  variety of wrappers around this system call and those
                  should be used rather than calling it directly.

           See the add_key(2), request_key(2), and keyctl(2) manual pages for
           more information.

           The keyctl() wrappers are listed on the keyctl(3) manual page.

## [](#UTILITIES)UTILITIES

           A program is provided to interact with the kernel facility by a
           number of subcommands, e.g.:

                  keyctl add user foo bar @s

           See the keyctl(1) manual page for information on that.

           The kernel has the ability to upcall to userspace to fabricate new
           keys.  This can be triggered by request_key(), but userspace is
           better off using add_key() instead if it possibly can.

           The upcalling mechanism is usually routed via the request-key(8)
           program.  What this does with any particular key is configurable
           in:

                  /etc/request-key.conf
                  /etc/request-key.d/

           See the request-key.conf(5) and the request-key(8) manual pages
           for more information.

## [](#SEE_ALSO)SEE ALSO

           keyctl(1), keyctl(3), keyrings(7), persistent-keyring(7),
           process-keyring(7), session-keyring(7), thread-keyring(7),
           user-keyring(7), user-session-keyring(7), pam_keyinit(8)

## [](#COLOPHON)COLOPHON

           This page is part of the keyutils (key management utilities)
           project.  Information about the project can be found at [unknown
           -- if you know, please contact man-pages@man7.org] If you have a
           bug report for this manual page, send it to
           keyrings@linux-nfs.org.  This page was obtained from the project's
           upstream Git repository
           ⟨http://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git⟩
           on 2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2023-03-20.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    Linux                          21 Feb 2014                    KEYUTILS(7)

------------------------------------------------------------------------

Pages that refer to this page: [add_key(2)](../man2/add_key.2.html),  [keyctl(2)](../man2/keyctl.2.html),  [request_key(2)](../man2/request_key.2.html),  [keyctl(3)](../man3/keyctl.3.html),  [keyctl_capabilities(3)](../man3/keyctl_capabilities.3.html),  [keyctl_chown(3)](../man3/keyctl_chown.3.html),  [keyctl_clear(3)](../man3/keyctl_clear.3.html),  [keyctl_describe(3)](../man3/keyctl_describe.3.html),  [keyctl_dh_compute(3)](../man3/keyctl_dh_compute.3.html),  [keyctl_get_keyring_ID(3)](../man3/keyctl_get_keyring_ID.3.html),  [keyctl_get_persistent(3)](../man3/keyctl_get_persistent.3.html),  [keyctl_get_security(3)](../man3/keyctl_get_security.3.html),  [keyctl_instantiate(3)](../man3/keyctl_instantiate.3.html),  [keyctl_invalidate(3)](../man3/keyctl_invalidate.3.html),  [keyctl_join_session_keyring(3)](../man3/keyctl_join_session_keyring.3.html),  [keyctl_link(3)](../man3/keyctl_link.3.html),  [keyctl_move(3)](../man3/keyctl_move.3.html),  [keyctl_pkey_encrypt(3)](../man3/keyctl_pkey_encrypt.3.html),  [keyctl_pkey_query(3)](../man3/keyctl_pkey_query.3.html),  [keyctl_pkey_sign(3)](../man3/keyctl_pkey_sign.3.html),  [keyctl_read(3)](../man3/keyctl_read.3.html),  [keyctl_restrict_keyring(3)](../man3/keyctl_restrict_keyring.3.html),  [keyctl_revoke(3)](../man3/keyctl_revoke.3.html),  [keyctl_search(3)](../man3/keyctl_search.3.html),  [keyctl_session_to_parent(3)](../man3/keyctl_session_to_parent.3.html),  [keyctl_setperm(3)](../man3/keyctl_setperm.3.html),  [keyctl_set_reqkey_keyring(3)](../man3/keyctl_set_reqkey_keyring.3.html),  [keyctl_set_timeout(3)](../man3/keyctl_set_timeout.3.html),  [keyctl_update(3)](../man3/keyctl_update.3.html),  [keyctl_watch_key(3)](../man3/keyctl_watch_key.3.html),  [asymmetric-key(7)](../man7/asymmetric-key.7.html),  [keyrings(7)](../man7/keyrings.7.html)

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
