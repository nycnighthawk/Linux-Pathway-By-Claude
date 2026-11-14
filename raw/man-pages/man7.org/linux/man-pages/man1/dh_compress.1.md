---
{"title": "dh_compress(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_compress.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_compress(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [CONFORMS TO](#CONFORMS_TO) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_COMPRESS(1)                  Debhelper                  DH_COMPRESS(1)

## [](#NAME)NAME

           dh_compress - compress files and fix symlinks in package build
           directories

## [](#SYNOPSIS)SYNOPSIS

           dh_compress [debhelper options] [-Xitem] [-A] [file ...]

## [](#DESCRIPTION)DESCRIPTION

           dh_compress is a debhelper program that is responsible for
           compressing the files in package build directories, and makes sure
           that any symlinks that pointed to the files before they were
           compressed are updated to point to the new files.

           By default, dh_compress compresses files that Debian policy
           mandates should be compressed, namely all files in usr/share/info,
           usr/share/man, files in usr/share/doc that are larger than 4k in
           size, (except the copyright file, .html and other web files, image
           files, and files that appear to be already compressed based on
           their extensions), and all changelog files. Plus PCF fonts
           underneath usr/share/fonts/X11/

## [](#FILES)FILES

           debian/package.compress
               These files are deprecated.

               If this file exists, the default files are not compressed.
               Instead, the file is ran as a shell script, and all filenames
               that the shell script outputs will be compressed. The shell
               script will be run from inside the package build directory.
               Note though that using -X is a much better idea in general;
               you should only use a debian/package.compress file if you
               really need to.

## [](#OPTIONS)OPTIONS

           -Xitem, --exclude=item
               Exclude files that contain item anywhere in their filename
               from being compressed. For example, -X.tiff will exclude TIFF
               files from compression.  You may use this option multiple
               times to build up a list of things to exclude.

           -A, --all
               Compress all files specified by command line parameters in ALL
               packages acted on.

           file ...
               Add these files to the list of files to compress.

## [](#CONFORMS_TO)CONFORMS TO

           Debian policy, version 3.0

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

    13.31                           2026-05-24                 DH_COMPRESS(1)

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
