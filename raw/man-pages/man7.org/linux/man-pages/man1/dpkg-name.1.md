---
{"title": "dpkg-name(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dpkg-name.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dpkg-name(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [BUGS](#BUGS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dpkg-name(1)                    dpkg suite                   dpkg-name(1)

## [](#NAME)NAME

           dpkg-name - rename Debian packages to full package names

## [](#SYNOPSIS)SYNOPSIS

           dpkg-name [option...]  [--] file...

## [](#DESCRIPTION)DESCRIPTION

           This manual page documents the dpkg-name program which provides an
           easy way to rename Debian packages into their full package names.
           A full package name consists of
           package_version_architecture.package-type as specified in the
           control file of the package.  The version part of the filename
           consists of the upstream version information optionally followed
           by a hyphen and the revision information.  The package-type part
           comes from that field if present or will fall back to deb.

## [](#OPTIONS)OPTIONS

           -a, --no-architecture
               The destination filename will not have the architecture
               information.

           -k, --symlink
               Create a symlink, instead of moving.

           -o, --overwrite
               Existing files will be overwritten if they have the same name
               as the destination filename.

           -s, --subdir [dir]
               Files will be moved into a subdirectory.  If the directory
               given as argument exists the files will be moved into that
               directory otherwise the name of the target directory is
               extracted from the section field in the control part of the
               package.  The target directory will be
               «unstable/binary-architecture/section».  If the section is not
               found in the control, then no-section is assumed, and in this
               case, as well as for sections non-free and contrib the target
               directory is «section/binary-architecture».  The section field
               is not required so a lot of packages will find their way to
               the no-section area.

               Warning: Use this option with care, it is messy.

           -c, --create-dir
               This option can used together with the -s option.  If a target
               directory isn't found it will be created automatically.

               Warning: Use this option with care.

           -?, --help
               Show the usage message and exit.

           -v, --version
               Show the version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           DEB_HOST_ARCH
               Sets the host architecture.  This affects the architecture
               name used in the package filename.

           DPKG_COLORS
               Sets the color mode.  The currently accepted values are: auto
               (default), always and never.

               Supported since dpkg 1.18.5.

           DPKG_NLS
               If set, it will be used to decide whether to activate Native
               Language Support, also known as internationalization (or i18n)
               support.  The accepted values are: 0 and 1 (default).

               Supported since dpkg 1.19.0.

## [](#BUGS)BUGS

           Some packages don't follow the name structure
           package_version_architecture.deb.  Packages renamed by dpkg-name
           will follow this structure.  Generally this will have no impact on
           how packages are installed by dselect(1)/dpkg(1), but other
           installation tools might depend on this naming structure.

## [](#EXAMPLES)EXAMPLES

           dpkg-name bar-foo.deb
               The file bar-foo.deb will be renamed to bar-foo_1.0-2_i386.deb
               or something similar (depending on whatever information is in
               the control part of bar-foo.deb).

           find /root/debian/ -name '*.deb' | xargs -n 1 dpkg-name -a
               All files with the extension deb in the directory /root/debian
               and its subdirectory's will be renamed by dpkg-name if
               required into names with no architecture information.

           find -name '*.deb' | xargs -n 1 dpkg-name -a -o -s -c
               Don't do this.  Your archive will be messed up completely
               because a lot of packages don't come with section information.
               Don't do this.

           dpkg-deb --build debian-tmp && dpkg-name -o -s .. debian-tmp.deb
               This can be used when building new packages.

## [](#SEE_ALSO)SEE ALSO

           deb(5), deb-control(5), dpkg(1), dpkg-deb(1), find(1), xargs(1).

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

    1.23.7-216-gff7e9               2026-03-07                   dpkg-name(1)

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
