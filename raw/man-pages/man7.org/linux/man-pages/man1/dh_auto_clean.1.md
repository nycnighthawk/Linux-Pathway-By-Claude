---
{"title": "dh_auto_clean(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_auto_clean.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_auto_clean(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_AUTO_CLEAN(1)                Debhelper                DH_AUTO_CLEAN(1)

## [](#NAME)NAME

           dh_auto_clean - automatically cleans up after a build

## [](#SYNOPSIS)SYNOPSIS

           dh_auto_clean [build system options] [debhelper options]
           [-- params]

## [](#DESCRIPTION)DESCRIPTION

           dh_auto_clean is a debhelper program that tries to automatically
           clean up after a package build. It does so by running the
           appropriate command for the build system it detects the package
           uses. For example, if there's a Makefile and it contains a
           distclean, realclean, or clean target, then this is done by
           running make (or MAKE, if the environment variable is set). If
           there is a setup.py or Build.PL, it is run to clean the package.

           This is intended to work for about 90% of packages. If it doesn't
           work, or tries to use the wrong clean target, you're encouraged to
           skip using dh_auto_clean at all, and just run make clean manually.

## [](#OPTIONS)OPTIONS

           See "BUILD SYSTEM OPTIONS" in debhelper(7) for a list of common
           build system selection and control options.

           -- params
               Pass params to the program that is run, after the parameters
               that dh_auto_clean usually passes.

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

    13.29                           2026-01-15               DH_AUTO_CLEAN(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh_clean(1)](../man1/dh_clean.1.html),  [debhelper(7)](../man7/debhelper.7.html)

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
