---
{"title": "dpkg-realpath(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dpkg-realpath.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dpkg-realpath(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dpkg-realpath(1)                dpkg suite               dpkg-realpath(1)

## [](#NAME)NAME

           dpkg-realpath - print the resolved pathname with DPKG_ROOT support

## [](#SYNOPSIS)SYNOPSIS

           dpkg-realpath [option...] pathname

## [](#DESCRIPTION)DESCRIPTION

           dpkg-realpath is a tool to resolve a pathname, that takes the
           dpkg(1) root directory into account, either implicitly from the
           DPKG_ROOT environment variable or from the command-line --root or
           --instdir options, and returns an absolute pathname relative to
           the root directory.  The root directory must not be prefixed to
           the pathname to be resolved.

           This is intended to be used by other dpkg helpers, or by
           maintainer scripts instead of using realpath(1) or readlink(1) to
           canonicalize pathnames, as these latter commands do not support
           canonicalization relative to a different root than /.

           This program was introduced in dpkg 1.20.1.

## [](#OPTIONS)OPTIONS

           -z, --zero
               Use a NUL byte to end output lines instead of a new line
               character.

               Supported since dpkg 1.20.6.

           --instdir directory
           --root directory
               Set the root directory to directory, which is the base
               directory that pathnames get canonicalized against.  Defaults
               to «/» if DPKG_ROOT has not been set.

           -?, --help
               Show the usage message and exit.

           --version
               Show the version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           DPKG_ROOT
               If set and the --instdir or --root options have not been
               specified, it will be used as the filesystem root directory.

           DPKG_COLORS
               Sets the color mode.  The currently accepted values are: auto
               (default), always and never.

           DPKG_NLS
               If set, it will be used to decide whether to activate Native
               Language Support, also known as internationalization (or i18n)
               support.  The accepted values are: 0 and 1 (default).

               Supported since dpkg 1.22.7.

## [](#SEE_ALSO)SEE ALSO

           realpath(1), readlink(1).

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

    1.23.7-216-gff7e9               2026-03-07               dpkg-realpath(1)

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
