---
{"title": "NS_GET_OWNER_UID(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ns_get_owner_uid.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# NS_GET_OWNER_UID(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NS_GET_OWNER_UID(2const)                         NS_GET_OWNER_UID(2const)

## [](#NAME)NAME

           NS_GET_OWNER_UID - discovering the owner of a user namespace

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/nsfs.h>  /* Definition of NS_GET_OWNER_UID */
           #include <sys/ioctl.h>

           int ioctl(int fd, NS_GET_OWNER_UID, uid_t *uid);

## [](#DESCRIPTION)DESCRIPTION

           The NS_GET_OWNER_UID operation can be used to discover the owner
           user ID of a user namespace (i.e., the effective user ID of the
           process that created the user namespace).

           fd refers to a /proc/pid/ns/user file.

           The owner user ID is returned in the uid_t pointed to by the third
           argument.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL fd does not refer to a user namespace.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 4.11.

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), ioctl_nsfs(2)

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

    Linux man-pages 6.19            2026-02-08       NS_GET_OWNER_UID(2const)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_nsfs(2)](../man2/ioctl_nsfs.2.html)

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
