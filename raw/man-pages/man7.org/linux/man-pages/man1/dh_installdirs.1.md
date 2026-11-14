---
{"title": "dh_installdirs(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installdirs.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installdirs(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLDIRS(1)               Debhelper               DH_INSTALLDIRS(1)

## [](#NAME)NAME

           dh_installdirs - create subdirectories in package build
           directories

## [](#SYNOPSIS)SYNOPSIS

           dh_installdirs [debhelper options] [-A] [--sourcedir=dir]
           [--create-in-sourcedir] [dir ...]

## [](#DESCRIPTION)DESCRIPTION

           dh_installdirs is a debhelper program that is responsible for
           creating subdirectories in package build directories.

           Many packages can get away with omitting the call to
           dh_installdirs completely.  Notably, other dh_* commands are
           expected to create directories as needed.

## [](#FILES)FILES

           debian/package.dirs
               Lists directories to be created in package.

               Generally, there is no need to list directories created by the
               upstream build system or directories needed by other debhelper
               commands.

               Supports substitution variables in compat 13 and later as
               documented in debhelper(7).

## [](#OPTIONS)OPTIONS

           -A, --all
               Create any directories specified by command line parameters in
               ALL packages acted on, not just the first.

           --create-in-sourcedir, --no-create-in-sourcedir
               Whether to create the specified directories in the source
               directory (usually debian/tmp) in addition to in the package
               build directory (usually debian/package).

               The default is --no-create-in-sourcedir.

           --sourcedir=dir
               Consider dir the source directory for the packages acted on
               instead of the default (which is usually debian/tmp).

               Please note that this option is dependent on the
               --create-in-sourcedir option (when --no-create-in-sourcedir is
               in effect, this option does nothing in dh_installdirs).

           dir ...
               Create these directories in the package build directory of the
               first package acted on. (Or in all packages if -A is
               specified.)

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

    13.23                           2025-01-02              DH_INSTALLDIRS(1)

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
