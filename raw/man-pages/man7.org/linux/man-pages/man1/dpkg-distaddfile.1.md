---
{"title": "dpkg-distaddfile(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dpkg-distaddfile.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dpkg-distaddfile(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dpkg-distaddfile(1)             dpkg suite            dpkg-distaddfile(1)

## [](#NAME)NAME

           dpkg-distaddfile - add entries to debian/files

## [](#SYNOPSIS)SYNOPSIS

           dpkg-distaddfile [option...] filename section priority

## [](#DESCRIPTION)DESCRIPTION

           dpkg-distaddfile adds an entry for a named file to debian/files.

           It takes three non-option arguments, the filename and the section
           and priority for the .changes file.

           The filename should be specified relative to the directory where
           dpkg-genchanges will expect to find the files, usually .., rather
           than being a pathname relative to the current directory when
           dpkg-distaddfile is run.

## [](#OPTIONS)OPTIONS

           -ffiles-list-file
               Read or write the list of files to be uploaded here, rather
               than using debian/files.

           -?, --help
               Show the usage message and exit.

           --version
               Show the version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           DPKG_COLORS
               Sets the color mode.  The currently accepted values are: auto
               (default), always and never.

               Supported since dpkg 1.18.5.

           DPKG_NLS
               If set, it will be used to decide whether to activate Native
               Language Support, also known as internationalization (or i18n)
               support.  The accepted values are: 0 and 1 (default).

               Supported since dpkg 1.19.0.

## [](#FILES)FILES

           debian/files
               The list of generated files which are part of the upload being
               prepared.  dpkg-distaddfile can be used to add additional
               files.

## [](#SEE_ALSO)SEE ALSO

           deb-src-files(5).

## [](#COLOPHON)COLOPHON

           This page is part of the dpkg (Debian Package Manager) project.
           Information about the project can be found at 
           ⟨https://wiki.debian.org/Teams/Dpkg/⟩.  If you have a bug report
           for this manual page, see
           ⟨http://bugs.debian.org/cgi-bin/pkgreport.cgi?src=dpkg⟩.  This
           page was obtained from the project's upstream Git repository ⟨git
           clone https://git.dpkg.org/git/dpkg/dpkg.git⟩ on 2026-08-03.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    1.23.7-216-gff7e9               2026-03-07            dpkg-distaddfile(1)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-buildtree(1)](../man1/dpkg-buildtree.1.html),  [deb-src-files(5)](../man5/deb-src-files.5.html),  [deb-src-rules(5)](../man5/deb-src-rules.5.html)

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
