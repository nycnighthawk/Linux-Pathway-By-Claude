---
{"title": "dh_clean(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_clean.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_clean(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_CLEAN(1)                     Debhelper                     DH_CLEAN(1)

## [](#NAME)NAME

           dh_clean - clean up package build directories

## [](#SYNOPSIS)SYNOPSIS

           dh_clean [debhelper options] [-k] [-d] [-Xitem] [path ...]

## [](#DESCRIPTION)DESCRIPTION

           dh_clean is a debhelper program that is responsible for cleaning
           up.  It should be the last step of the clean target and other
           debhelper commands generally assume that dh_clean will clean up
           after them.

           It removes the package build directories, and removes some other
           files including debian/files, and any detritus left behind by
           other debhelper commands. It also removes common files and
           directories that should not appear in a Debian diff:
             #*# *~ DEADJOE *.orig *.rej *.SUMS __pycache__ TAGS .deps/* *.P
           *-stamp

           It does not run "make clean" to clean up after the build process.
           Use dh_auto_clean(1) to do things like that.

## [](#FILES)FILES

           debian/clean
               Can list other paths to be removed.

               Note that directories listed in this file must end with a
               trailing slash.  Any content in these directories will be
               removed as well.

               Supports substitution variables in compat 13 and later as
               documented in debhelper(7).

## [](#OPTIONS)OPTIONS

           -k, --keep
               This is deprecated, use dh_prep(1) instead.

               The option is removed in compat 12.

           -d, --dirs-only
               Only clean the package build directories, do not clean up any
               other files at all.

           -Xitem --exclude=item
               Exclude files that contain item anywhere in their filename
               from being deleted, even if they would normally be deleted.
               You may use this option multiple times to build up a list of
               things to exclude.

           path ...
               Delete these paths too.

               Note that directories passed as arguments must end with a
               trailing slash.  Any content in these directories will be
               removed as well.

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

    13.31                           2026-05-24                    DH_CLEAN(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh_assistant(1)](../man1/dh_assistant.1.html),  [debhelper(7)](../man7/debhelper.7.html)

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
