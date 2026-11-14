---
{"title": "dh_missing(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_missing.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_missing(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_MISSING(1)                   Debhelper                   DH_MISSING(1)

## [](#NAME)NAME

           dh_missing - check for missing files

## [](#SYNOPSIS)SYNOPSIS

           dh_missing [-Xitem] [--sourcedir=dir] [debhelper options]

## [](#DESCRIPTION)DESCRIPTION

           dh_missing compares the list of installed files with the files in
           the source directory. If any of the files (and symlinks) in the
           source directory were not installed to somewhere, it will warn on
           stderr about that (--list-missing) or fail (--fail-missing).

           Please note that in compat 11 and earlier without either of these
           options, dh_missing will silently do nothing.  In compat 12,
           --list-missing is the default  In compat 13 and later,
           --fail-missing is the default.

           This may be useful if you have a large package and want to make
           sure that you don't miss installing newly added files in new
           upstream releases.

           Remember to test different kinds of builds (dpkg-buildpackage
           -A/-B/...) as you may experience varying results when only a
           subset of the packages are built.

## [](#FILES)FILES

           debian/not-installed
               List the files that are deliberately not installed in any
               binary package.  Paths listed in this file are ignored by
               dh_missing.  However, it is not a method to exclude files from
               being installed by any of the debhelper tool.  If you want a
               tool to not install a given file, please use its --exclude
               option (where available).

               dh_missing will expand wildcards in this file (since debhelper
               11.1).  Wildcards without matches will be ignored.

               Supports substitution variables in compat 13 and later as
               documented in debhelper(7).

## [](#OPTIONS)OPTIONS

           --list-missing
               Warn on stderr about source files not installed to somewhere.

               Note that many dh-tools acting on a path will mark the path as
               installed even if it has been excluded via -X or --exclude.
               This is also seen when a dh-tool is acting on a directory and
               exclusion is used to ignore some files in the directory.  In
               either case, this will make dh_missing silently assume the
               excluded files have been handled.

               This is the default in compat 12.

           --fail-missing
               This option is like --list-missing, except if a file was
               missed, it will not only list the missing files, but also fail
               with a nonzero exit code.

               This is the default in compat 13 and later.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

           This program is a part of debhelper.

## [](#AUTHOR)AUTHOR

           Michael Stapelberg <stapelberg@debian.org>

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

    13.29                           2026-01-15                  DH_MISSING(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh_assistant(1)](../man1/dh_assistant.1.html),  [dh_install(1)](../man1/dh_install.1.html),  [debhelper(7)](../man7/debhelper.7.html)

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
