---
{"title": "dh_installwm(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installwm.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installwm(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLWM(1)                 Debhelper                 DH_INSTALLWM(1)

## [](#NAME)NAME

           dh_installwm - register a window manager

## [](#SYNOPSIS)SYNOPSIS

           dh_installwm [debhelper options] [-n] [--priority=n] [wm ...]

## [](#DESCRIPTION)DESCRIPTION

           dh_installwm is a debhelper program that is responsible for
           generating the postinst and prerm commands that register a window
           manager with update-alternatives(8). The window manager's man page
           is also registered as a slave symlink (in v6 mode and up).  It
           must be installed in usr/share/man/man1/ in the package build
           directory prior to calling dh_installwm.  In compat 9 and earlier,
           the manpage was optional.

## [](#FILES)FILES

           debian/package.wm
               List window manager programs to register.

               Supports substitution variables in compat 13 and later as
               documented in debhelper(7).

## [](#OPTIONS)OPTIONS

           --priority=n
               Set the priority of the window manager. Default is 20, which
               is too low for most window managers; see the Debian Policy
               document for instructions on calculating the correct value.

           -n, --no-scripts
               Do not modify postinst/prerm scripts. Turns this command into
               a no-op.

           -A, --all
               Modify scripts for window managers specified by command line
               parameters in ALL packages acted on, not just the first.

           wm ...
               Window manager programs to register.

## [](#NOTES)NOTES

           Note that this command is not idempotent. dh_prep(1) should be
           called between invocations of this command. Otherwise, it may
           cause multiple instances of the same text to be added to
           maintainer scripts.

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

    13.23                           2025-01-02                DH_INSTALLWM(1)

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
