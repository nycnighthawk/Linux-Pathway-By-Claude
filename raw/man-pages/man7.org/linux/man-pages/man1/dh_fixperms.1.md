---
{"title": "dh_fixperms(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_fixperms.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_fixperms(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_FIXPERMS(1)                  Debhelper                  DH_FIXPERMS(1)

## [](#NAME)NAME

           dh_fixperms - fix permissions of files in package build
           directories

## [](#SYNOPSIS)SYNOPSIS

           dh_fixperms [debhelper options] [-Xitem]

## [](#DESCRIPTION)DESCRIPTION

           dh_fixperms is a debhelper program that is responsible for setting
           the permissions of files and directories in package build
           directories to a sane state -- a state that complies with Debian
           policy.

           dh_fixperms makes all files in usr/share/doc in the package build
           directory (excluding files in the examples/ directory) be mode
           644. It also changes the permissions of all man pages to mode 644.
           It removes group and other write permission from all files. It
           removes execute permissions from any libraries, headers, Perl
           modules, or desktop files that have it set. It makes all files in
           the standard bin and sbin directories, usr/games/ and etc/init.d
           executable (since v4). Finally, it removes the setuid and setgid
           bits from all files in the package.

           When the Rules-Requires-Root field has the (effective) value of
           binary-targets, dh_fixperms will also reset the ownership of all
           paths to "root:root".

## [](#OPTIONS)OPTIONS

           -Xitem, --exclude item
               Exclude files that contain item anywhere in their filename
               from having their permissions changed. You may use this option
               multiple times to build up a list of things to exclude.

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

    13.29                           2026-01-15                 DH_FIXPERMS(1)

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
