---
{"title": "KEYCTL_SETPERM(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/KEYCTL_SETPERM.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# KEYCTL_SETPERM(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEYCTL_SETPERM(2const)                             KEYCTL_SETPERM(2const)

## [](#NAME)NAME

           KEYCTL_SETPERM - change the permissions mask on a key

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/keyctl.h>  /* Definition of KEY* constants */
           #include <sys/syscall.h>   /* Definition of SYS_* constants */
           #include <unistd.h>

           long syscall(SYS_keyctl, KEYCTL_SETPERM, key_serial_t key,
                        key_perm_t perms);

## [](#DESCRIPTION)DESCRIPTION

           Change the permissions of the key with the ID provided in the key
           argument to the permissions provided in the perms argument.

           If the caller doesn't have the CAP_SYS_ADMIN capability, it can
           change permissions only for the keys it owns.  (More precisely:
           the caller's filesystem UID must match the UID of the key.)

           The key must grant setattr permission to the caller regardless of
           the caller's capabilities.

           The permissions in perms specify masks of available operations for
           each of the following user categories:

           possessor (since Linux 2.6.14)
                  This is the permission granted to a process that possesses
                  the key (has it attached searchably to one of the process's
                  keyrings); see keyrings(7).

           user   This is the permission granted to a process whose
                  filesystem UID matches the UID of the key.

           group  This is the permission granted to a process whose
                  filesystem GID or any of its supplementary GIDs matches the
                  GID of the key.

           other  This is the permission granted to other processes that do
                  not match the user and group categories.

           The user, group, and other categories are exclusive: if a process
           matches the user category, it will not receive permissions granted
           in the group category; if a process matches the user or group
           category, then it will not receive permissions granted in the
           other category.

           The possessor category grants permissions that are cumulative with
           the grants from the user, group, or other category.

           Each permission mask is eight bits in size, with only six bits
           currently used.  The available permissions are:

           view   This permission allows reading attributes of a key.

                  This permission is required for the KEYCTL_DESCRIBE(2const)
                  operation.

           The permission bits for each category are:

                  KEY_POS_VIEW
                  KEY_USR_VIEW
                  KEY_GRP_VIEW
                  KEY_OTH_VIEW

           read   This permission allows reading a key's payload.

                  This permission is required for the KEYCTL_READ(2const)
                  operation.

                  The permission bits for each category are

                  KEY_POS_READ
                  KEY_USR_READ
                  KEY_GRP_READ
                  KEY_OTH_READ

           write  This permission allows update or instantiation of a key's
                  payload.  For a keyring, it allows keys to be linked and
                  unlinked from the keyring,

                  This permission is required for the KEYCTL_UPDATE(2const),
                  KEYCTL_REVOKE(2const), KEYCTL_CLEAR(2const),
                  KEYCTL_LINK(2const), and KEYCTL_UNLINK(2const) operations.

                  The permission bits for each category are:

                  KEY_POS_WRITE
                  KEY_USR_WRITE
                  KEY_GRP_WRITE
                  KEY_OTH_WRITE

           search This permission allows keyrings to be searched and keys to
                  be found.  Searches can recurse only into nested keyrings
                  that have search permission set.

                  This permission is required for the
                  KEYCTL_GET_KEYRING_ID(2const),
                  KEYCTL_JOIN_SESSION_KEYRING(2const), KEYCTL_SEARCH(2const),
                  and KEYCTL_INVALIDATE (2const) operations.

                  The permission bits for each category are:

                  KEY_POS_SEARCH
                  KEY_USR_SEARCH
                  KEY_GRP_SEARCH
                  KEY_OTH_SEARCH

           link   This permission allows a key or keyring to be linked to.

                  This permission is required for the KEYCTL_LINK(2const) and
                  KEYCTL_SESSION_TO_PARENT(2const) operations.

                  The permission bits for each category are:

                  KEY_POS_LINK
                  KEY_USR_LINK
                  KEY_GRP_LINK
                  KEY_OTH_LINK

           setattr (since Linux 2.6.15)
                  This permission allows a key's UID, GID, and permissions
                  mask to be changed.

                  This permission is required for the KEYCTL_REVOKE(2const),
                  KEYCTL_CHOWN(2const), and KEYCTL_SETPERM (2const)
                  operations.

                  The permission bits for each category are:

                  KEY_POS_SETATTR
                  KEY_USR_SETATTR
                  KEY_GRP_SETATTR
                  KEY_OTH_SETATTR

           As a convenience, the following macros are defined as masks for
           all of the permission bits in each of the user categories:

                  KEY_POS_ALL
                  KEY_USR_ALL
                  KEY_GRP_ALL
                  KEY_OTH_ALL

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL operation was KEYCTL_SETPERM and an invalid permission bit
                  was specified in perms.

## [](#VERSIONS)VERSIONS

           A wrapper is provided in the libkeyutils library:
           keyctl_setperm(3).

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.10.

## [](#SEE_ALSO)SEE ALSO

           keyctl(2), keyctl_setperm(3)

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

    Linux man-pages 6.19            2026-02-08         KEYCTL_SETPERM(2const)

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
