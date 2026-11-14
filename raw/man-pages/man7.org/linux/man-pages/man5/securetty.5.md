---
{"title": "securetty(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/securetty.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# securetty(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    securetty(5)               File Formats Manual               securetty(5)

## [](#NAME)NAME

           securetty - list of terminals on which root is allowed to login

## [](#DESCRIPTION)DESCRIPTION

           The file /etc/securetty contains the names of terminals (one per
           line, without leading /dev/) which are considered secure for the
           transmission of certain authentication tokens.

           It is used by (some versions of) login(1) to restrict the
           terminals on which root is allowed to login.  See login.defs(5) if
           you use the shadow suite.

           On PAM enabled systems, it is used for the same purpose by
           pam_securetty(8) to restrict the terminals on which empty
           passwords are accepted.

## [](#FILES)FILES

           /etc/securetty

## [](#SEE_ALSO)SEE ALSO

           login(1), login.defs(5), pam_securetty(8)

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

    Linux man-pages 6.19            2025-05-17                   securetty(5)

------------------------------------------------------------------------

Pages that refer to this page: [login(1@@shadow-utils)](../man1/login.1@@shadow-utils.html),  [pam_securetty(8)](../man8/pam_securetty.8.html)

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
