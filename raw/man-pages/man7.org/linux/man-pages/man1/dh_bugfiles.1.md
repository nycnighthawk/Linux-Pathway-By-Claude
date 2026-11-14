---
{"title": "dh_bugfiles(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_bugfiles.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_bugfiles(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_BUGFILES(1)                  Debhelper                  DH_BUGFILES(1)

## [](#NAME)NAME

           dh_bugfiles - install bug reporting customization files into
           package build directories

## [](#SYNOPSIS)SYNOPSIS

           dh_bugfiles [-A] [debhelper options]

## [](#DESCRIPTION)DESCRIPTION

           dh_bugfiles is a debhelper program that is responsible for
           installing bug reporting customization files (bug scripts and/or
           bug control files and/or presubj files) into package build
           directories.

## [](#FILES)FILES

           debian/package.bug-script
               This is the script to be run by the bug reporting program for
               generating a bug report template. This file is installed as
               usr/share/bug/package in the package build directory if no
               other types of bug reporting customization files are going to
               be installed for the package in question. Otherwise, this file
               is installed as usr/share/bug/package/script. Finally, the
               installed script is given execute permissions.

           debian/package.bug-control
               It is the bug control file containing some directions for the
               bug reporting tool. This file is installed as
               usr/share/bug/package/control in the package build directory.

           debian/package.bug-presubj
               The contents of this file are displayed to the user by the bug
               reporting tool before allowing the user to write a bug report
               on the package to the Debian Bug Tracking System. This file is
               installed as usr/share/bug/package/presubj in the package
               build directory.

## [](#OPTIONS)OPTIONS

           -A, --all
               Install debian/bug-* files to ALL packages acted on when
               respective debian/package.bug-* files do not exist. Normally,
               debian/bug-* will be installed to the first package only.

## [](#SEE_ALSO)SEE ALSO

           /usr/share/doc/reportbug/README.developers.gz

           debhelper(1)

           This program is a part of debhelper.

## [](#AUTHOR)AUTHOR

           Modestas Vainius <modestas@vainius.eu>

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

    13.23                           2025-01-02                 DH_BUGFILES(1)

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
