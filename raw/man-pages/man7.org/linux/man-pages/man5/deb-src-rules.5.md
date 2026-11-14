---
{"title": "deb-src-rules(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-src-rules.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-src-rules(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-src-rules(5)                dpkg suite               deb-src-rules(5)

## [](#NAME)NAME

           deb-src-rules - Debian source package rules file

## [](#SYNOPSIS)SYNOPSIS

           debian/rules

## [](#DESCRIPTION)DESCRIPTION

           This file contains the instructions necessary to build the binary
           packages from the source package.

           The debian/rules file is an executable Makefile, with a shebang
           that is usually set to "#!/usr/bin/make -f".

           It must support the following make targets:

           clean
               Clean up the source tree, by undoing any change done by any of
               the build and binary targets.  This target will be called with
               root privileges.

           build-indep
               Build architecture independent files required to build any
               architecture independent binary package.  If there are no
               architecture independent binary packages to generate, the
               target must still exist but do nothing.  This target must not
               require root privileges.

           build-arch
               Build architecture dependent files required to build any
               architecture dependent binary package.  If there are no
               architecture dependent binary packages to generate, the target
               must still exist but do nothing.  This target must not require
               root privileges.

           build
               Build architecture independent and dependent files, either by
               depending (at least transitively) on build-indep and/or build-
               arch or by inlining what those targets would do.  This target
               must not require root privileges.

           binary-indep
               Build architecture independent binary packages.  This target
               must depend (at least transitively) on either build-indep or
               build.  This target will be called with root privileges.

           binary-arch
               Build architecture dependent binary packages.  This target
               must depend (at least transitively) on either build-arch or
               build.  This target will be called with root privileges.

           binary
               Build architecture independent and dependent binary packages,
               either by depending (at least transitively) on binary-indep
               and/or binary-arch or by inlining what those targets would do.
               This target will be called with root privileges.

## [](#SEE_ALSO)SEE ALSO

           dpkg-architecture(1), dpkg-vendor(1), dpkg-buildflags(1),
           dpkg-parsechangelog(1), dpkg-shlibdeps(1), dpkg-gencontrol(1),
           dpkg-deb(1), dpkg-distaddfile(1).

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

    1.22.0-52-g1af0                 2023-08-30               deb-src-rules(5)

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
