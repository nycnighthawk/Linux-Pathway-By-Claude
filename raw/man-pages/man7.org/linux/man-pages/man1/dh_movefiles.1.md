---
{"title": "dh_movefiles(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_movefiles.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_movefiles(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_MOVEFILES(1)                 Debhelper                 DH_MOVEFILES(1)

## [](#NAME)NAME

           dh_movefiles - move files out of debian/tmp into subpackages

## [](#SYNOPSIS)SYNOPSIS

           dh_movefiles [debhelper options] [--sourcedir=dir] [-Xitem]
           [file ...]

## [](#DESCRIPTION)DESCRIPTION

           dh_movefiles is a debhelper program that is responsible for moving
           files out of debian/tmp or some other directory and into other
           package build directories. This may be useful if your package has
           a Makefile that installs everything into debian/tmp, and you need
           to break that up into subpackages.

           Note: dh_install is a much better program, and you are recommended
           to use it instead of dh_movefiles.

## [](#FILES)FILES

           debian/package.files
               Lists the files to be moved into a package, separated by
               whitespace. The filenames listed should be relative to
               debian/tmp/. You can also list directory names, and the whole
               directory will be moved.

## [](#OPTIONS)OPTIONS

           --sourcedir=dir
               Instead of moving files out of debian/tmp (the default), this
               option makes it move files out of some other directory. Since
               the entire contents of the sourcedir is moved, specifying
               something like --sourcedir=/ is very unsafe, so to prevent
               mistakes, the sourcedir must be a relative filename; it cannot
               begin with a `/'.

           -Xitem, --exclude=item
               Exclude files that contain item anywhere in their filename
               from being installed.

           file ...
               Lists files to move. The filenames listed should be relative
               to debian/tmp/. You can also list directory names, and the
               whole directory will be moved. It is an error to list files
               here unless you use -p, -i, or -a to tell dh_movefiles which
               subpackage to put them in.

## [](#NOTES)NOTES

           Note that files are always moved out of debian/tmp by default
           (even if you have instructed debhelper to use a compatibility
           level higher than one, which does not otherwise use debian/tmp for
           anything at all). The idea behind this is that the package that is
           being built can be told to install into debian/tmp, and then files
           can be moved by dh_movefiles from that directory. Any files or
           directories that remain are ignored, and get deleted by dh_clean
           later.

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

    13.29                           2026-01-15                DH_MOVEFILES(1)

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
