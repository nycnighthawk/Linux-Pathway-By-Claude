---
{"title": "dh_auto_configure(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_auto_configure.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_auto_configure(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_AUTO_CONFIGURE(1)            Debhelper            DH_AUTO_CONFIGURE(1)

## [](#NAME)NAME

           dh_auto_configure - automatically configure a package prior to
           building

## [](#SYNOPSIS)SYNOPSIS

           dh_auto_configure [build system options] [debhelper options]
           [-- params]

## [](#DESCRIPTION)DESCRIPTION

           dh_auto_configure is a debhelper program that tries to
           automatically configure a package prior to building. It does so by
           running the appropriate command for the build system it detects
           the package uses.  For example, it looks for and runs a
           ./configure script, Makefile.PL, Build.PL, or cmake. A standard
           set of parameters is determined and passed to the program that is
           run. Some build systems, such as make, do not need a configure
           step; for these dh_auto_configure will exit without doing
           anything.

           This is intended to work for about 90% of packages. If it doesn't
           work, you're encouraged to skip using dh_auto_configure at all,
           and just run ./configure or its equivalent manually.

## [](#OPTIONS)OPTIONS

           See "BUILD SYSTEM OPTIONS" in debhelper(7) for a list of common
           build system selection and control options.

           -- params
               Pass params to the program that is run, after the parameters
               that dh_auto_configure usually passes. For example:

                 dh_auto_configure -- --with-foo --enable-bar

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

    13.29                           2026-01-15           DH_AUTO_CONFIGURE(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh(1)](../man1/dh.1.html),  [debhelper(7)](../man7/debhelper.7.html),  [debhelper-compat-upgrade-checklist(7)](../man7/debhelper-compat-upgrade-checklist.7.html)

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
