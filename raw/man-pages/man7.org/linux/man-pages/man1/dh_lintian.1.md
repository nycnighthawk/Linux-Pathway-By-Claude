---
{"title": "dh_lintian(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_lintian.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_lintian(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_LINTIAN(1)                   Debhelper                   DH_LINTIAN(1)

## [](#NAME)NAME

           dh_lintian - install lintian override files into package build
           directories

## [](#SYNOPSIS)SYNOPSIS

           dh_lintian [debhelper options]

## [](#DESCRIPTION)DESCRIPTION

           dh_lintian is a debhelper program that is responsible for
           installing override files used by lintian into package build
           directories.

## [](#FILES)FILES

           debian/package.lintian-overrides
               Installed into usr/share/lintian/overrides/package in the
               package build directory. This file is used to suppress
               erroneous lintian diagnostics.

           debian/source/lintian-overrides
               These files are not installed, but will be scanned by lintian
               to provide overrides for the source package.

## [](#SEE_ALSO)SEE ALSO

           debhelper(1)

           This program is a part of debhelper.

           lintian(1)

## [](#AUTHOR)AUTHOR

           Steve Robbins <smr@debian.org>

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

    13.23                           2025-01-02                  DH_LINTIAN(1)

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
