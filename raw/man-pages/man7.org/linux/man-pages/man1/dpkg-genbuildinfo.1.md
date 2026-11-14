---
{"title": "dpkg-genbuildinfo(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dpkg-genbuildinfo.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dpkg-genbuildinfo(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dpkg-genbuildinfo(1)            dpkg suite           dpkg-genbuildinfo(1)

## [](#NAME)NAME

           dpkg-genbuildinfo - generate Debian .buildinfo files

## [](#SYNOPSIS)SYNOPSIS

           dpkg-genbuildinfo [option...]

## [](#DESCRIPTION)DESCRIPTION

           dpkg-genbuildinfo reads information from an unpacked and built
           Debian source tree and from the files it has generated and
           generates a Debian control file describing the build environment
           and the build artifacts (.buildinfo file).

           This program was introduced in dpkg 1.18.11.

## [](#OPTIONS)OPTIONS

           --build=type
               Specifies the build type from a comma-separated list of
               components.

               The allowed values are:

               any Generate build information including unqualified build
                   dependencies (Build-Depends) and architecture specific
                   build dependencies (Build-Depends-Arch).

               all Generate build information including unqualified build
                   dependencies (Build-Depends) and architecture independent
                   build dependencies (Build-Depends-Indep).

               source
                   Effectively ignored; generate build information with just
                   the unqualified build dependencies (Build-Depends).

               binary
                   Generate build information with all three types of build
                   dependencies.  This is an alias for any,all.

               full
                   Generate build information with all three types of build
                   dependencies.  This is an alias for any,all,source, and
                   the same as the default case when no build option is
                   specified.

           -ccontrolfile
               Specifies the main source control file to read information
               from.  The default is debian/control.

           -lchangelog-file
               Specifies the changelog file to read information from.  The
               default is debian/changelog.

           -ffiles-list-file
               Specifies where is the list of files that have been produced
               by the build, rather than using debian/files.

           -Fchangelog-format
               Specifies the format of the changelog.  See
               dpkg-parsechangelog(1) for information about alternative
               formats.

           -O[filename]
               Print the buildinfo file to standard output (or filename if
               specified) rather than to
               dir/source-name_binary-version_arch.buildinfo (where dir is ..
               by default or upload-files-dir if -u was used).

           -uupload-files-dir
               Look for the files to be uploaded in upload-files-dir rather
               than ..  (dpkg-genbuildinfo needs to find these files so that
               it can include their sizes and checksums in the .buildinfo
               file).

           --always-include-kernel
               By default, the Build-Kernel-Version field will not be written
               out.

               Specify this option to always write a Build-Kernel-Version
               field when generating the .buildinfo.

               Supported since dpkg 1.19.0.

           --always-include-path
               By default, the Build-Path field will only be written if the
               current directory starts with an allowed pattern.

               On Debian and derivatives the pattern matches on /build/ at
               the start of the pathname.

               Specify this option to always write a Build-Path field when
               generating the .buildinfo.

           --admindir=dir
               Change the location of the dpkg database.  The default
               location is /var/lib/dpkg.

           -q  dpkg-genbuildinfo might produce informative messages on
               standard error.  -q suppresses these messages.

           -?, --help
               Show the usage message and exit.

           --version
               Show the version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           DEB_BUILD_OPTIONS
               This variable can be used to enable or disable various
               features that affect the information included in the
               .buildinfo file, via the buildinfo option.  This option
               contains a comma-separated list of features, prefixed with the
               ‘+’ or ‘-’ modifiers, to denote whether to enable or disable
               them.  The special feature “all” can be used to enable or
               disable all other features.  The feature “path” controls
               whether to unconditionally include the Build-Path field.

               Supported since dpkg 1.18.19.

           DEB_BUILD_PROFILES
               If set, it will be used as the active build profile(s) to use
               when generating the .buildinfo file.  It is a space separated
               list of profile names, without any exclamation marks.

           DEB_BUILD_ARCH
               Sets the build architecture.  This affects the value for the
               Build-Architecture field, and the check for the
               cross-compilation mode.

           DEB_HOST_ARCH
               Sets the host architecture.  This affects the filename used
               for the .buildinfo file, and the check for the
               cross-compilation mode.

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
               The list of generated files.  dpkg-genbuildinfo reads the data
               here when producing a .buildinfo file.

## [](#SEE_ALSO)SEE ALSO

           deb-buildinfo(5).

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

    1.23.7-216-gff7e9               2026-03-07           dpkg-genbuildinfo(1)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-buildpackage(1)](../man1/dpkg-buildpackage.1.html),  [deb-buildinfo(5)](../man5/deb-buildinfo.5.html)

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
