---
{"title": "NS_GET_NSTYPE(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/ns_get_nstype.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# NS_GET_NSTYPE(2const) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NS_GET_NSTYPE(2const)                               NS_GET_NSTYPE(2const)

## [](#NAME)NAME

           NS_GET_NSTYPE - discovering the namespace type

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/nsfs.h>  /* Definition of NS_GET_NSTYPE */
           #include <sys/ioctl.h>

           int ioctl(int fd, NS_GET_NSTYPE);

## [](#DESCRIPTION)DESCRIPTION

           The NS_GET_NSTYPE operation can be used to discover the type of
           namespace referred to by the file descriptor fd.

           fd refers to a /proc/pid/ns/* file.

## [](#RETURN_VALUE)RETURN VALUE

           On success, the return value is one of the CLONE_NEW* values that
           can be specified to clone(2) or unshare(2) in order to create a
           namespace.

           On error, -1 is returned, and errno is set to indicate the error.

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

    Linux man-pages 6.19            2026-02-08          NS_GET_NSTYPE(2const)

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
