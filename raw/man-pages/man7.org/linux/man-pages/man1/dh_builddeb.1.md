---
{"title": "dh_builddeb(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_builddeb.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_builddeb(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_BUILDDEB(1)                  Debhelper                  DH_BUILDDEB(1)

## [](#NAME)NAME

           dh_builddeb - build Debian binary packages

## [](#SYNOPSIS)SYNOPSIS

           dh_builddeb [debhelper options] [--destdir=directory]
           [--filename=name] [-- params]

## [](#DESCRIPTION)DESCRIPTION

           dh_builddeb simply calls dpkg-deb(1) to build a Debian package or
           packages.  It will also build dbgsym packages when dh_strip(1) and
           dh_gencontrol(1) have prepared them.

           It supports building multiple binary packages in parallel, when
           enabled by DEB_BUILD_OPTIONS.

           When the Rules-Requires-Root field is not (effectively)
           binary-targets, dh_builddeb will pass --root-owner-group to
           dpkg-deb(1).

## [](#OPTIONS)OPTIONS

           --destdir=directory
               Use this if you want the generated .deb files to be put in a
               directory other than the default of "..".

           --filename=name
               Use this if you want to force the generated .deb file to have
               a particular file name. Does not work well if more than one
               .deb is generated!

           -- params
               Pass params to dpkg-deb(1) when it is used to build the
               package.

           -uparams
               This is another way to pass params to dpkg-deb(1).  It is
               deprecated; use -- instead.

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

    13.29                           2026-01-15                 DH_BUILDDEB(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh_gencontrol(1)](../man1/dh_gencontrol.1.html),  [debhelper(7)](../man7/debhelper.7.html)

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
