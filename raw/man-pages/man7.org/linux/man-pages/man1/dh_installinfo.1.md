---
{"title": "dh_installinfo(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installinfo.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installinfo(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLINFO(1)               Debhelper               DH_INSTALLINFO(1)

## [](#NAME)NAME

           dh_installinfo - install info files

## [](#SYNOPSIS)SYNOPSIS

           dh_installinfo [debhelper options] [-A] [file ...]

## [](#DESCRIPTION)DESCRIPTION

           dh_installinfo is a debhelper program that is responsible for
           installing info files into usr/share/info in the package build
           directory.

           From debhelper compatibility level 11 on, dh_install will fall
           back to looking in debian/tmp for files, if it does not find them
           in the current directory (or wherever you've told it to look using
           --sourcedir).

## [](#FILES)FILES

           debian/package.info
               List info files to be installed.

               Supports substitution variables in compat 13 and later as
               documented in debhelper(7).

## [](#OPTIONS)OPTIONS

           -A, --all
               Install all files specified by command line parameters in ALL
               packages acted on.

           --sourcedir=dir
               Look in the specified directory for files to be installed.
               This option requires compat 11 or later (it is silently
               ignored in compat 10 or earlier).

               Note that this is not the same as the --sourcedirectory option
               used by the dh_auto_* commands. You rarely need to use this
               option, since dh_installinfo automatically looks for files in
               debian/tmp in debhelper compatibility level 11 and above.

           file ...
               Install these info files into the first package acted on. (Or
               in all packages if -A is specified).

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

    13.23                           2025-01-02              DH_INSTALLINFO(1)

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
