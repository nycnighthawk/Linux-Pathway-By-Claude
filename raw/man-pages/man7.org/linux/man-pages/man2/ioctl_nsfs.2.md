---
{"title": "ioctl_nsfs(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ioctl_nsfs.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ioctl_nsfs(2) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ioctl_nsfs(2)              System Calls Manual              ioctl_nsfs(2)

## [](#NAME)NAME

           ioctl_nsfs - ioctl() operations for Linux namespaces

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/nsfs.h>  /* Definition of NS_* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, unsigned long op, ...);

## [](#DESCRIPTION)DESCRIPTION

       Discovering namespace relationships
           NS_GET_USERNS(2const)
           NS_GET_PARENT(2const)

       Discovering the namespace type
           NS_GET_NSTYPE(2const)

       Discovering the owner of a user namespace
           NS_GET_OWNER_UID(2const)

## [](#ERRORS)ERRORS

           ENOTTY fd does not refer to a /proc/pid/ns/* file.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), fstat(2), proc(5), namespaces(7)

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

    Linux man-pages 6.19            2026-02-08                  ioctl_nsfs(2)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl(2)](../man2/ioctl.2.html),  [NS_GET_NSTYPE(2const)](../man2/NS_GET_NSTYPE.2const.html),  [NS_GET_OWNER_UID(2const)](../man2/NS_GET_OWNER_UID.2const.html),  [NS_GET_USERNS(2const)](../man2/NS_GET_USERNS.2const.html),  [namespaces(7)](../man7/namespaces.7.html),  [pid_namespaces(7)](../man7/pid_namespaces.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html)

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
