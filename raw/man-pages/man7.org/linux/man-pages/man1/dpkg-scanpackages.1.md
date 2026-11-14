---
{"title": "dpkg-scanpackages(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dpkg-scanpackages.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dpkg-scanpackages(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dpkg-scanpackages(1)            dpkg suite           dpkg-scanpackages(1)

## [](#NAME)NAME

           dpkg-scanpackages - create Packages index files

## [](#SYNOPSIS)SYNOPSIS

           dpkg-scanpackages [option...] binary-path [override-file
           [path-prefix]] > Packages

## [](#DESCRIPTION)DESCRIPTION

           dpkg-scanpackages sorts through a tree of Debian binary packages
           and creates a Packages file, used by apt(8), dselect(1), etc, to
           tell the user what packages are available for installation.  These
           Packages files are the same as those found on Debian archive sites
           and media discs.  You might use dpkg-scanpackages yourself if
           making a directory of local packages to install on a cluster of
           machines.

           Note: If you want to access the generated Packages file with
           apt(8) you will probably need to compress the file with xz(1)
           (generating a Packages.xz file), bzip2(1) (generating a
           Packages.bz2 file) or gzip(1) (generating a Packages.gz file).
           apt(8) ignores uncompressed Packages files except on local access
           (i.e.  file:// sources).

           binary-path is the name of the tree of the binary packages to
           process (for example, contrib/binary-i386).  It is best to make
           this relative to the root of the Debian archive, because every
           Filename field in the new Packages file will start with this
           string.

           override-file is the name of a file to read which contains
           information about how the package fits into the distribution.  The
           file can be compressed (since dpkg 1.15.5).  See deb-override(5).

           path-prefix is an optional string to be prepended to the Filename
           fields.

           If more than one version of a package is found only the newest one
           is included in the output.  If they have the same version and only
           differ in architecture only the first one found is used.

## [](#OPTIONS)OPTIONS

           -t, --type type
               Scan for *.type packages, instead of *.deb.

           -e, --extra-override file
               Scan file to find supplementary overrides.  The file can be
               compressed (since dpkg 1.15.5).  See deb-extra-override(5) for
               more information on its format.

           -a, --arch arch
               Use a pattern consisting of *_all.deb and *_arch.deb, or
               *_arch.deb if --no-implicit-arch has been specified, instead
               of scanning for all debs.

           --no-implicit-arch
               Do not implicitly add architecture all binary packages when
               specifying --arch.

               Supported since dpkg 1.23.6.

           -h, --hash hash-list
               Only generate file hashes for the comma-specified list
               specified.  The default is to generate all currently supported
               hashes.  Supported values: md5, sha1, sha256.

               Supported since dpkg 1.17.14.

           -m, --multiversion
               Include all found packages in the output.

           -M, --medium id-string
               Add an X-Medium field containing the value id-string.

               This field is required if you want to generate Packages.cd
               files for use by the media access method of dselect.

               Supported since dpkg 1.15.5.

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

## [](#DIAGNOSTICS)DIAGNOSTICS

           dpkg-scanpackages outputs the usual self-explanatory errors.  It
           also warns about packages that are in the wrong subdirectory, are
           duplicated, have a Filename field in their control file, are
           missing from the override file, or have maintainer substitutions
           which do not take effect.

## [](#SEE_ALSO)SEE ALSO

           dpkg(1), dselect(1), deb-override(5), deb-extra-override(5),
           dpkg-scansources(1).

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

    1.23.7-216-gff7e9               2026-03-07           dpkg-scanpackages(1)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-scansources(1)](../man1/dpkg-scansources.1.html),  [dselect(1)](../man1/dselect.1.html),  [deb-extra-override(5)](../man5/deb-extra-override.5.html),  [deb-override(5)](../man5/deb-override.5.html)

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
