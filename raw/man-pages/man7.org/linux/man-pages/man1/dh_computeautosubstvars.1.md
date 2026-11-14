---
{"title": "dh_computeautosubstvars(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_computeautosubstvars.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_computeautosubstvars(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_COMPUTEAUTOSUBSTVARS(1)      Debhelper      DH_COMPUTEAUTOSUBSTVARS(1)

## [](#NAME)NAME

           dh_computeautosubstvars - compute substvars relevant to most
           packages

## [](#SYNOPSIS)SYNOPSIS

           dh_computeautosubstvars [debhelper options] [-- params]

## [](#DESCRIPTION)DESCRIPTION

           dh_computeautosubstvars is a debhelper program that is responsible
           for computing substvars relevant to most packages. It needs to be
           run before dh_gencontrol but after all the content has been added
           into the package staging directory (debian/package/).

           Note that this command generally assumes compat 14 or later where
           dh_gencontrol will apply relationship substvars automatically. It
           can be used in older compat levels but the substvars will not be
           used automatically in that case.

## [](#OPTIONS)OPTIONS

           This helper only accepts standard debhelper options. Please refer
           to debhelper(7) for these.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

           This program is a part of debhelper.

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

    13.31                           2026-05-24     DH_COMPUTEAUTOSUBSTVARS(1)

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
