---
{"title": "dh_installchangelogs(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_installchangelogs.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_installchangelogs(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_INSTALLCHANGELOGS(1)         Debhelper         DH_INSTALLCHANGELOGS(1)

## [](#NAME)NAME

           dh_installchangelogs - install changelogs into package build
           directories

## [](#SYNOPSIS)SYNOPSIS

           dh_installchangelogs [debhelper options] [-k] [-Xitem] [--no-trim]
           [upstream]

## [](#DESCRIPTION)DESCRIPTION

           dh_installchangelogs is a debhelper program that is responsible
           for installing changelogs into package build directories.

           An upstream changelog file may be specified as an option. If none
           is specified, dh_installchangelogs may look for files with names
           that seem likely to be changelogs as described in the next
           paragraphs.

           In non-native packages, dh_installchangelogs will first look for
           changelog files installed by the upstream build system into
           usr/share/doc/package (of the package build directory) and rename
           the most likely candidate (if any) to
           usr/share/doc/package/changelog.  Note that dh_installchangelogs
           does not look into any source directory (such as debian/tmp).
           Otherwise, dh_installchangelogs (at compatibility level 7 or any
           later) will look for changelog files in the source directory (e.g.
           the root or the docs subdirectory).  It will look for changelog,
           changes and history optionally with common extensions (such as
           .txt, .md, .rst, .org, etc.)

           If a changelog file is specified and is an html file (determined
           by file extension), it will be installed as
           usr/share/doc/package/changelog.html instead. If the html
           changelog is converted to plain text, that variant can be
           specified as a second parameter. When no plain text variant is
           specified, a short usr/share/doc/package/changelog is generated,
           pointing readers at the html changelog file.

           The debchange-style Debian changelogs are trimmed to include only
           entries more recent than the release date of oldstable.  No
           trimming will be performed if the --no-trim option is passed or if
           the DEB_BUILD_OPTIONS environment variable contains notrimdch.

## [](#FILES)FILES

           debian/changelog
           debian/NEWS
           debian/package.changelog
           debian/package.NEWS
               Automatically installed into usr/share/doc/package/ in the
               package build directory.

               Use the package specific name if package needs a different
               NEWS or changelog file.

               The changelog file is installed with a name of changelog for
               native packages, and changelog.Debian for non-native packages.
               The NEWS file is always installed with a name of NEWS.Debian.

## [](#OPTIONS)OPTIONS

           -k, --keep
               Keep the original name of the upstream changelog. This will be
               accomplished by installing the upstream changelog as
               changelog, and making a symlink from that to the original name
               of the changelog file. This can be useful if the upstream
               changelog has an unusual name, or if other documentation in
               the package refers to the changelog file.

           -Xitem, --exclude=item
               Exclude upstream changelog files that contain item anywhere in
               their filename from being installed.

               Note that directory name of the changelog is also part of the
               match.

           --no-trim
               Install the full changelog, not its trimmed version that
               includes only recent entries.

           upstream
               Install this file as the upstream changelog.

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

    13.31                           2026-05-24        DH_INSTALLCHANGELOGS(1)

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
