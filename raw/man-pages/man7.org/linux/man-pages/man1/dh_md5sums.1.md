---
{"title": "dh_md5sums(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_md5sums.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_md5sums(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_MD5SUMS(1)                   Debhelper                   DH_MD5SUMS(1)

## [](#NAME)NAME

           dh_md5sums - generate DEBIAN/md5sums file

## [](#SYNOPSIS)SYNOPSIS

           dh_md5sums [debhelper options] [-x] [-Xitem] [--include-conffiles]

## [](#DESCRIPTION)DESCRIPTION

           dh_md5sums is a debhelper program that is responsible for
           generating a DEBIAN/md5sums file, which lists the md5sums of each
           file in the package.  These files are used by dpkg --verify or the
           debsums(1) program.

           All files in DEBIAN/ are omitted from the md5sums file, as are all
           conffiles (unless you use the --include-conffiles switch).

           The md5sums file is installed with proper permissions and
           ownerships.

## [](#OPTIONS)OPTIONS

           -Xitem, --exclude=item
               Exclude files that contain item anywhere in their filename
               from being listed in the md5sums file.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

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

    13.29                           2026-01-15                  DH_MD5SUMS(1)

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
