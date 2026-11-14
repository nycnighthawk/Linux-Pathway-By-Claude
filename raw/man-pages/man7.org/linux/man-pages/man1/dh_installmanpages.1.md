---
{"title": "dh_installmanpages(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installmanpages.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installmanpages(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLMANPAGES(1)           Debhelper           DH_INSTALLMANPAGES(1)

## [](#NAME)NAME

           dh_installmanpages - old-style man page installer (deprecated)

## [](#SYNOPSIS)SYNOPSIS

           dh_installmanpages [debhelper options] [file ...]

## [](#DESCRIPTION)DESCRIPTION

           dh_installmanpages is a debhelper program that is responsible for
           automatically installing man pages into usr/share/man/ in package
           build directories.

           This is a DWIM-style program, with an interface unlike the rest of
           debhelper. It is deprecated, and you are encouraged to use
           dh_installman(1) instead.

           dh_installmanpages scans the current directory and all
           subdirectories for filenames that look like man pages. (Note that
           only real files are looked at; symlinks are ignored.) It uses
           file(1) to verify that the files are in the correct format. Then,
           based on the files' extensions, it installs them into the correct
           man directory.

           All filenames specified as parameters will be skipped by
           dh_installmanpages.  This is useful if by default it installs some
           man pages that you do not want to be installed.

           After the man page installation step, dh_installmanpages will
           check to see if any of the man pages are .so links. If so, it
           changes them to symlinks.

## [](#OPTIONS)OPTIONS

           file ...
               Do not install these files as man pages, even if they look
               like valid man pages.

## [](#BUGS)BUGS

           dh_installmanpages will install the man pages it finds into all
           packages you tell it to act on, since it can't tell what package
           the man pages belong in. This is almost never what you really want
           (use -p to work around this, or use the much better
           dh_installman(1) program instead).

           Files ending in .man will be ignored.

           Files specified as parameters that contain spaces in their
           filenames will not be processed properly.

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

    13.29                           2026-01-15          DH_INSTALLMANPAGES(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh_installman(1)](../man1/dh_installman.1.html),  [debhelper(7)](../man7/debhelper.7.html)

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
