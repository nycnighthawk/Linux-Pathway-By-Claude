---
{"title": "dpkg-gencontrol(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dpkg-gencontrol.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dpkg-gencontrol(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dpkg-gencontrol(1)              dpkg suite             dpkg-gencontrol(1)

## [](#NAME)NAME

           dpkg-gencontrol - generate Debian control files

## [](#SYNOPSIS)SYNOPSIS

           dpkg-gencontrol [option...]

## [](#DESCRIPTION)DESCRIPTION

           dpkg-gencontrol reads information from an unpacked Debian source
           tree and generates a binary package control file (which defaults
           to debian/tmp/DEBIAN/control); during this process it will
           simplify the relation fields.

           Thus Pre-Depends, Depends, Recommends and Suggests are simplified
           in this order by removing dependencies which are known to be true
           according to the stronger dependencies already parsed.  It will
           also remove any self-dependency (in fact it will remove any
           dependency which evaluates to true given the current version of
           the package as installed).  Logically it keeps the intersection of
           multiple dependencies on the same package.  The order of
           dependencies is preserved as best as possible: if any dependency
           must be discarded due to another dependency appearing further in
           the field, the superseding dependency will take the place of the
           discarded one.

           The other relation fields (Enhances, Conflicts, Breaks, Replaces
           and Provides) are also simplified individually by computing the
           union of the various dependencies when a package is listed
           multiple times in the field.

           dpkg-gencontrol also adds an entry for the binary package to
           debian/files.

## [](#OPTIONS)OPTIONS

           -vversion
               Sets the version number of the binary package which will be
               generated.

           -Vname=value
               Set an output substitution variable.  See deb-substvars(5) for
               discussion of output substitution.

           -Tsubstvars-file
               Read substitution variables in substvars-file; the default is
               debian/substvars.  This option can be used multiple times to
               read substitution variables from multiple files (since dpkg
               1.15.6).

           -Dfield=value
               Override or add an output control file field.

           -Ufield
               Remove an output control file field.

           -ccontrol-file
               Specifies the main source control file to read information
               from.  The default is debian/control.

           -lchangelog-file
               Specifies the changelog file to read information from.  The
               default is debian/changelog.

           -ffiles-list-file
               Read or write the list of files to be uploaded here, rather
               than using debian/files.

           -Fchangelog-format
               Specifies the format of the changelog.  See
               dpkg-parsechangelog(1) for information about alternative
               formats.

           -ppackage
               Generate information for the binary package package.  If the
               source control file lists only one binary package then this
               option may be omitted; otherwise it is essential to select
               which binary package's information to generate.

           -nfilename
               Assume the filename of the package will be filename instead of
               the normal package_version_arch.deb filename.

           -is, -ip, -isp
               These options are ignored for compatibility with older
               versions of the dpkg build scripts but are now deprecated.
               Previously they were used to tell dpkg-gencontrol to include
               the Section and Priority fields in the control file.  This is
               now the default behavior.  If you want to get the old behavior
               you can use the -U option to delete the fields from the
               control file.

           -Ppackage-build-dir
               Scan package-build-dir instead of debian/tmp.  This value is
               used to find the default value of the Installed-Size
               substitution variable and control file field, and for the
               default location of the output file.

           -O[filename]
               Print the control file to standard output (or filename if
               specified), rather than to debian/tmp/DEBIAN/control (or
               package-build-dir/DEBIAN/control if -P was used).

               Support for optional argument since dpkg 1.17.2.

           -?, --help
               Show the usage message and exit.

           --version
               Show the version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           DEB_HOST_ARCH
               Sets the host architecture.

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

           debian/control
               The source package template control file, giving
               version-independent information about the source package and
               the binary packages it can produce.

           debian/files
               The list of generated files which are part of the upload being
               prepared.  dpkg-gencontrol adds the presumed filenames of
               binary packages whose control files it generates here.

## [](#SEE_ALSO)SEE ALSO

           deb-substvars(5), deb-src-control(5), deb-changelog(5),
           deb-control(5).

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

    1.23.7-216-gff7e9               2026-03-07             dpkg-gencontrol(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh_gencontrol(1)](../man1/dh_gencontrol.1.html),  [dpkg-buildtree(1)](../man1/dpkg-buildtree.1.html),  [deb-src-rules(5)](../man5/deb-src-rules.5.html),  [deb-substvars(5)](../man5/deb-substvars.5.html)

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
