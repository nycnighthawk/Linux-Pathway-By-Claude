---
{"title": "uts_namespaces(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/uts_namespaces.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# uts_namespaces(7) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    uts_namespaces(7)    Miscellaneous Information Manual   uts_namespaces(7)

## [](#NAME)NAME

           uts_namespaces - overview of Linux UTS namespaces

## [](#DESCRIPTION)DESCRIPTION

           UTS namespaces provide isolation of two system identifiers: the
           hostname and the NIS domain name.  These identifiers are set using
           sethostname(2) and setdomainname(2), and can be retrieved using
           uname(2), gethostname(2), and getdomainname(2).  Changes made to
           these identifiers are visible to all other processes in the same
           UTS namespace, but are not visible to processes in other UTS
           namespaces.

           When a process creates a new UTS namespace using clone(2) or
           unshare(2) with the CLONE_NEWUTS flag, the hostname and domain
           name of the new UTS namespace are copied from the corresponding
           values in the caller's UTS namespace.

           Use of UTS namespaces requires a kernel that is configured with
           the CONFIG_UTS_NS option.

## [](#SEE_ALSO)SEE ALSO

           nsenter(1), unshare(1), clone(2), getdomainname(2),
           gethostname(2), setns(2), uname(2), unshare(2), namespaces(7)

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

    Linux man-pages 6.19            2026-02-08              uts_namespaces(7)

------------------------------------------------------------------------

Pages that refer to this page: [getino(1)](../man1/getino.1.html),  [nsenter(1)](../man1/nsenter.1.html),  [unshare(1)](../man1/unshare.1.html),  [clone(2)](../man2/clone.2.html),  [getdomainname(2)](../man2/getdomainname.2.html),  [gethostname(2)](../man2/gethostname.2.html),  [uname(2)](../man2/uname.2.html),  [lttng-ust(3)](../man3/lttng-ust.3.html),  [namespaces(7)](../man7/namespaces.7.html)

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
