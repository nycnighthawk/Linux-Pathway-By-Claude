---
{"title": "dh_installexamples(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installexamples.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installexamples(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLEXAMPLES(1)           Debhelper           DH_INSTALLEXAMPLES(1)

## [](#NAME)NAME

           dh_installexamples - install example files into package build
           directories

## [](#SYNOPSIS)SYNOPSIS

           dh_installexamples [debhelper options] [-A] [-Xitem] [file ...]

## [](#DESCRIPTION)DESCRIPTION

           dh_installexamples is a debhelper program that is responsible for
           installing examples into usr/share/doc/package/examples in package
           build directories.

           From debhelper compatibility level 11 on, dh_install will fall
           back to looking in debian/tmp for files, if it does not find them
           in the current directory (or wherever you've told it to look using
           --sourcedir).

## [](#FILES)FILES

           debian/package.examples
               Lists example files or directories to be installed.

               If upstream provides an examples directory, you will often
               want to use examples/* rather than examples in this file.  The
               latter would create /usr/share/doc/package/examples/examples,
               which is rarely what you want.

               Supports substitution variables in compat 13 and later as
               documented in debhelper(7).

## [](#OPTIONS)OPTIONS

           -A, --all
               Install any files specified by command line parameters in ALL
               packages acted on.

           --sourcedir=dir
               Look in the specified directory for files to be installed.
               This option requires compat 11 or later (it is silently
               ignored in compat 10 or earlier).

               Note that this is not the same as the --sourcedirectory option
               used by the dh_auto_* commands. You rarely need to use this
               option, since dh_installexamples automatically looks for files
               in debian/tmp in debhelper compatibility level 11 and above.

           --doc-main-package=main-package
               Set the main package for a documentation package.  This is
               used to install the documentation of the documentation package
               in /usr/share/doc/main-package as recommended by the Debian
               policy manual 3.9.7 in §12.3.

               In compat 11 (or later), this option is only useful if
               debhelper's auto-detection of the main package is wrong.  The
               option can also be used to silence a warning from debhelper
               when the auto-detection fails but the default happens to be
               correct.

               This option cannot be used when dh_installexamples is
               instructed to act on multiple packages.  If you need this
               option, you will generally need to combine it with -p to
               ensure exactly one package is acted on.

               The X-Doc-Main-Package field can be used instead since
               debhelper/13.28. It has similar semantics but does not require
               command line options.

           -Xitem, --exclude=item
               Exclude files that contain item anywhere in their filename
               from being installed.

           file ...
               Install these files (or directories) as examples into the
               first package acted on. (Or into all packages if -A is
               specified.)

## [](#NOTES)NOTES

           Note that dh_installexamples will happily copy entire directory
           hierarchies if you ask it to (similar to cp -a). If it is asked to
           install a directory, it will install the complete contents of the
           directory.

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

    13.29                           2026-01-15          DH_INSTALLEXAMPLES(1)

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
