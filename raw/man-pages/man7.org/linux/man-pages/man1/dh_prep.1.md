---
{"title": "dh_prep(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_prep.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_prep(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_PREP(1)                      Debhelper                      DH_PREP(1)

## [](#NAME)NAME

           dh_prep - perform cleanups in preparation for building a binary
           package

## [](#SYNOPSIS)SYNOPSIS

           dh_prep [debhelper options] [-Xitem]

## [](#DESCRIPTION)DESCRIPTION

           dh_prep is a debhelper program that performs some file cleanups in
           preparation for building a binary package. (This is what dh_clean
           -k used to do.) It removes the package build directories,
           debian/tmp, and some temp files that are generated when building a
           binary package.

           It is typically run at the top of the binary-arch and binary-indep
           targets, or at the top of a target such as install that they
           depend on.

## [](#OPTIONS)OPTIONS

           -Xitem --exclude=item
               Exclude files that contain item anywhere in their filename
               from being deleted, even if they would normally be deleted.
               You may use this option multiple times to build up a list of
               things to exclude.

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

    13.29                           2026-01-15                     DH_PREP(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh_clean(1)](../man1/dh_clean.1.html),  [dh_installcatalogs(1)](../man1/dh_installcatalogs.1.html),  [dh_installemacsen(1)](../man1/dh_installemacsen.1.html),  [dh_installinit(1)](../man1/dh_installinit.1.html),  [dh_installinitramfs(1)](../man1/dh_installinitramfs.1.html),  [dh_installmodules(1)](../man1/dh_installmodules.1.html),  [dh_installsystemd(1)](../man1/dh_installsystemd.1.html),  [dh_installsystemduser(1)](../man1/dh_installsystemduser.1.html),  [dh_installsysusers(1)](../man1/dh_installsysusers.1.html),  [dh_installtmpfiles(1)](../man1/dh_installtmpfiles.1.html),  [dh_installudev(1)](../man1/dh_installudev.1.html),  [dh_installwm(1)](../man1/dh_installwm.1.html),  [dh_systemd_enable(1)](../man1/dh_systemd_enable.1.html),  [dh_systemd_start(1)](../man1/dh_systemd_start.1.html),  [dh_ucf(1)](../man1/dh_ucf.1.html),  [dh_usrlocal(1)](../man1/dh_usrlocal.1.html),  [debhelper(7)](../man7/debhelper.7.html)

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
