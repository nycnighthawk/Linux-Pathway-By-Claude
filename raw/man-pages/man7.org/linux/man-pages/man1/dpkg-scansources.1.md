---
{"title": "dpkg-scansources(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dpkg-scansources.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dpkg-scansources(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dpkg-scansources(1)             dpkg suite            dpkg-scansources(1)

## [](#NAME)NAME

           dpkg-scansources - create Sources index files

## [](#SYNOPSIS)SYNOPSIS

           dpkg-scansources [option...] binary-dir [override-file
           [path-prefix]] > Sources

## [](#DESCRIPTION)DESCRIPTION

           dpkg-scansources scans the given binary-dir for .dsc files.  These
           are used to create a Debian source index, which is output to
           stdout.

           The override-file, if given, is used to set priorities in the
           resulting index stanzas and to override the maintainer field given
           in the .dsc files.  The file can be compressed (since dpkg
           1.15.5).  See deb-override(5) for the format of this file.

           Note: Since the override file is indexed by binary, not source
           packages, there's a bit of a problem here.  The current
           implementation uses the highest priority of all the binary
           packages produced by a .dsc file for the priority of the source
           package, and the override entry for the first binary package
           listed in the .dsc file to modify maintainer information.  This
           might change.

           The path-prefix, if given, is prepended to the directory field in
           the generated source index.  You generally use this to make the
           directory fields contain the path from the top of the Debian
           archive hierarchy.

           Note: If you want to access the generated Sources file with apt(8)
           you will probably need to compress the file with gzip(1)
           (generating a Sources.gz file).  apt(8) ignores uncompressed
           Sources files except on local access (i.e.  file:// sources).

## [](#OPTIONS)OPTIONS

           -n, --no-sort
               Do not sort the index stanzas.  Normally they are sorted by
               source package name.

           -e, --extra-override file
               Scan file to find supplementary overrides.  The file can be
               compressed (since dpkg 1.15.5).  See deb-extra-override(5) for
               more information on its format.

               Supported since dpkg 1.15.4.

           -s, --source-override file
               Use file as the source override file.  The file can be
               compressed (since dpkg 1.15.5).  The default is the name of
               the override file you specified with .src appended.

               The source override file is in a different format from the
               binary override file.  It contains only two whitespace
               separated fields, the first is the source package name and the
               second is the section.  Blank lines and comment lines are
               ignored in the normal manner.  If a package appears in both
               files the source override takes precedence for setting the
               section.

           --debug
               Turn debugging on.

           --help
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

## [](#SEE_ALSO)SEE ALSO

           deb-override(5), deb-extra-override(5), dpkg-scanpackages(1).

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

    1.23.7-216-gff7e9               2026-03-07            dpkg-scansources(1)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-scanpackages(1)](../man1/dpkg-scanpackages.1.html),  [deb-extra-override(5)](../man5/deb-extra-override.5.html),  [deb-override(5)](../man5/deb-override.5.html)

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
