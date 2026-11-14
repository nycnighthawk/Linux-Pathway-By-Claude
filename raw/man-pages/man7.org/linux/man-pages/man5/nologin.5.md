---
{"title": "nologin(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/nologin.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nologin(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    nologin(5)                 File Formats Manual                 nologin(5)

## [](#NAME)NAME

           nologin - prevent unprivileged users from logging into the system

## [](#DESCRIPTION)DESCRIPTION

           If the file /etc/nologin exists and is readable, login(1) will
           allow access only to root.  Other users will be shown the contents
           of this file and their logins will be refused.  This provides a
           simple way of temporarily disabling all unprivileged logins.

## [](#FILES)FILES

           /etc/nologin

## [](#SEE_ALSO)SEE ALSO

           login(1), shutdown(8)

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

    Linux man-pages 6.19            2025-05-17                     nologin(5)

------------------------------------------------------------------------

Pages that refer to this page: [login(1@@shadow-utils)](../man1/login.1@@shadow-utils.html),  [nologin(8@@shadow-utils)](../man8/nologin.8@@shadow-utils.html),  [pam_nologin(8)](../man8/pam_nologin.8.html)

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
