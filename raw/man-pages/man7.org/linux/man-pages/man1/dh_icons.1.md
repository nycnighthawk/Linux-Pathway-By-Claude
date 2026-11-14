---
{"title": "dh_icons(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_icons.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_icons(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_ICONS(1)                     Debhelper                     DH_ICONS(1)

## [](#NAME)NAME

           dh_icons - Update caches of Freedesktop icons

## [](#SYNOPSIS)SYNOPSIS

           dh_icons [debhelper options] [-n]

## [](#DESCRIPTION)DESCRIPTION

           dh_icons is a debhelper program that updates caches of Freedesktop
           icons when needed, using the update-icon-caches program provided
           by GTK+2.12.  Currently this program does not handle installation
           of the files, though it may do so at a later date, so should be
           run after icons are installed in the package build directories.

           It takes care of adding maintainer script fragments to call
           update-icon-caches for icon directories. (This is not done for
           gnome and hicolor icons, as those are handled by triggers.)  These
           commands are inserted into the maintainer scripts by
           dh_installdeb(1).

## [](#OPTIONS)OPTIONS

           -n, --no-scripts
               Do not modify maintainer scripts.

## [](#SEE_ALSO)SEE ALSO

           debhelper

           This program is a part of debhelper.

## [](#AUTHOR)AUTHOR

           Ross Burton <ross@burtonini.com> Jordi Mallach <jordi@debian.org>
           Josselin Mouette <joss@debian.org>

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

    13.29                           2026-01-15                    DH_ICONS(1)

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
