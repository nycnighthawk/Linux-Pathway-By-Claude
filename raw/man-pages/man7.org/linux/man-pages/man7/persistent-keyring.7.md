---
{"title": "persistent-keyring(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/persistent-keyring.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# persistent-keyring(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    persist...keyring(7) Miscellaneous Information Manualpersist...keyring(7)

## [](#NAME)NAME

           persistent-keyring - per-user persistent keyring

## [](#DESCRIPTION)DESCRIPTION

           The persistent keyring is a keyring used to anchor keys on behalf
           of a user.  Each UID the kernel deals with has its own persistent
           keyring that is shared between all threads owned by that UID.  The
           persistent keyring has a name (description) of the form
           _persistent.<UID> where <UID> is the user ID of the corresponding
           user.

           The persistent keyring may not be accessed directly, even by
           processes with the appropriate UID.  Instead, it must first be
           linked to one of a process's keyrings, before that keyring can
           access the persistent keyring by virtue of its possessor permits.
           This linking is done with the keyctl_get_persistent(3) function.

           If a persistent keyring does not exist when it is accessed by the
           keyctl_get_persistent(3) operation, it will be automatically
           created.

           Each time the keyctl_get_persistent(3) operation is performed, the
           persistent keyring's expiration timer is reset to the value in:

               /proc/sys/kernel/keys/persistent_keyring_expiry

           Should the timeout be reached, the persistent keyring will be
           removed and everything it pins can then be garbage collected.  The
           keyring will then be re-created on a subsequent call to
           keyctl_get_persistent(3).

           The persistent keyring is not directly searched by request_key(2);
           it is searched only if it is linked into one of the keyrings that
           is searched by request_key(2).

           The persistent keyring is independent of clone(2), fork(2),
           vfork(2), execve(2), and _exit(3).  It persists until its
           expiration timer triggers, at which point it is garbage collected.
           This allows the persistent keyring to carry keys beyond the life
           of the kernel's record of the corresponding UID (the destruction
           of which results in the destruction of the user-keyring(7) and the
           user-session-keyring(7)).  The persistent keyring can thus be used
           to hold authentication tokens for processes that run without user
           interaction, such as programs started by cron(8).

           The persistent keyring is used to store UID-specific objects that
           themselves have limited lifetimes (e.g., kerberos tokens).  If
           those tokens cease to be used (i.e., the persistent keyring is not
           accessed), then the timeout of the persistent keyring ensures that
           the corresponding objects are automatically discarded.

       Special operations
           The keyutils library provides the keyctl_get_persistent(3)
           function for manipulating persistent keyrings.  (This function is
           an interface to the keyctl(2) KEYCTL_GET_PERSISTENT operation.)
           This operation allows the calling thread to get the persistent
           keyring corresponding to its own UID or, if the thread has the
           CAP_SETUID capability, the persistent keyring corresponding to
           some other UID in the same user namespace.

## [](#NOTES)NOTES

           Each user namespace owns a keyring called .persistent_register
           that contains links to all of the persistent keys in that
           namespace.  (The .persistent_register keyring can be seen when
           reading the contents of the /proc/keys file for the UID 0 in the
           namespace.)  The keyctl_get_persistent(3) operation looks for a
           key with a name of the form _persistent.UID in that keyring,
           creates the key if it does not exist, and links it into the
           keyring.

## [](#SEE_ALSO)SEE ALSO

           keyctl(1), keyctl(3), keyctl_get_persistent(3), keyrings(7),
           process-keyring(7), session-keyring(7), thread-keyring(7),
           user-keyring(7), user-session-keyring(7)

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

    Linux man-pages 6.19            2026-06-05           persist...keyring(7)

------------------------------------------------------------------------

Pages that refer to this page: [add_key(2)](../man2/add_key.2.html),  [keyctl(2)](../man2/keyctl.2.html),  [KEYCTL_GET_PERSISTENT(2const)](../man2/KEYCTL_GET_PERSISTENT.2const.html),  [request_key(2)](../man2/request_key.2.html),  [keyctl_get_persistent(3)](../man3/keyctl_get_persistent.3.html),  [keyrings(7)](../man7/keyrings.7.html),  [keyutils(7)](../man7/keyutils.7.html),  [process-keyring(7)](../man7/process-keyring.7.html),  [session-keyring(7)](../man7/session-keyring.7.html),  [thread-keyring(7)](../man7/thread-keyring.7.html),  [user-keyring(7)](../man7/user-keyring.7.html),  [user-session-keyring(7)](../man7/user-session-keyring.7.html)

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
