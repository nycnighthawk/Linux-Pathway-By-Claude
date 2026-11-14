---
{"title": "dh_installmenu(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installmenu.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installmenu(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLMENU(1)               Debhelper               DH_INSTALLMENU(1)

## [](#NAME)NAME

           dh_installmenu - install Debian menu files into package build
           directories

## [](#SYNOPSIS)SYNOPSIS

           dh_installmenu [debhelper options] [-n]

## [](#DESCRIPTION)DESCRIPTION

           dh_installmenu is a debhelper program that is responsible for
           installing files used by the Debian menu package into package
           build directories.

           It also automatically generates the postinst and postrm commands
           needed to interface with the Debian menu package. These commands
           are inserted into the maintainer scripts by dh_installdeb(1).

## [](#FILES)FILES

           debian/package.menu
               Debian menu files, installed into usr/share/menu/package in
               the package build directory. See menufile(5) for its format.

           debian/package.menu-method
               Debian menu method files, installed into
               etc/menu-methods/package in the package build directory.

## [](#OPTIONS)OPTIONS

           -n, --no-scripts
               Do not modify postinst/postrm scripts.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7) update-menus(1) menufile(5)

           This program is a part of debhelper.

## [](#AUTHOR)AUTHOR

           Joey Hess <joeyh@debian.org>

## [](#COLOPHON)COLOPHON

           This page is part of the debhelper (helper programs for
           debian/rules) project.  Information about the project can be found
           at [unknown -- if you know, please contact man-pages@man7.org] If
           you have a bug report for this manual page, send it to
           submit@bugs.debian.org.  This page was obtained from the project's
           upstream Git repository
           ⟨https://salsa.debian.org/debian/debhelper.git⟩ on 2026-08-03.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-07-22.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    13.23                           2025-01-02              DH_INSTALLMENU(1)

------------------------------------------------------------------------

Pages that refer to this page: [debhelper(7)](../man7/debhelper.7.html)

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
