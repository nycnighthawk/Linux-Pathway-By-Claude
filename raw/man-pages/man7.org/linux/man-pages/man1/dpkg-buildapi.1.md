---
{"title": "dpkg-buildapi(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dpkg-buildapi.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dpkg-buildapi(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dpkg-buildapi(1)                dpkg suite               dpkg-buildapi(1)

## [](#NAME)NAME

           dpkg-buildapi - returns the build API level to use during package
           build

## [](#SYNOPSIS)SYNOPSIS

           dpkg-buildapi [option...] [command]

## [](#DESCRIPTION)DESCRIPTION

           dpkg-buildapi is a tool to retrieve the dpkg-build-api(7) level to
           use during build of source Debian packages.

           This program was introduced in dpkg 1.22.0.

## [](#COMMANDS)COMMANDS

           --help
               Show the usage message and exit.

           --version
               Show the version and exit.

## [](#OPTIONS)OPTIONS

           -ccontrol-file
               Specifies the main source control file to read information
               from.  The default is debian/control.

## [](#ENVIRONMENT)ENVIRONMENT

           DPKG_BUILD_API
               The build API level to use.  This is intended to be used
               internally by the tools executed from debian/rules to avoid
               having to parse debian/control multiple times, and not to set
               the global build API level from debian/rules, otherwise build
               drivers (such as dpkg-buildpackage(1)) cannot access it.

           DPKG_COLORS
               Sets the color mode.  The currently accepted values are: auto
               (default), always and never.

           DPKG_NLS
               If set, it will be used to decide whether to activate Native
               Language Support, also known as internationalization (or i18n)
               support.  The accepted values are: 0 and 1 (default).

## [](#FILES)FILES

       Packaging support
           /usr/local/share/dpkg/buildapi.mk
               Makefile snippet that parses the build API level into a
               variable.

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

    1.22.19-74-gf1ca0               2025-05-18               dpkg-buildapi(1)

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
