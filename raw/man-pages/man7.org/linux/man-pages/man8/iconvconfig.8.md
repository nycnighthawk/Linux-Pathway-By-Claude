---
{"title": "iconvconfig(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/iconvconfig.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# iconvconfig(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    iconvconfig(8)           System Manager's Manual           iconvconfig(8)

## [](#NAME)NAME

           iconvconfig - create iconv module configuration cache

## [](#SYNOPSIS)SYNOPSIS

           iconvconfig [options] [directory]...

## [](#DESCRIPTION)DESCRIPTION

           The iconv(3) function internally uses gconv modules to convert to
           and from a character set.  A configuration file is used to
           determine the needed modules for a conversion.  Loading and
           parsing such a configuration file would slow down programs that
           use iconv(3), so a caching mechanism is employed.

           The iconvconfig program reads iconv module configuration files and
           writes a fast-loading gconv module configuration cache file.

           In addition to the system provided gconv modules, the user can
           specify custom gconv module directories with the environment
           variable GCONV_PATH.  However, iconv module configuration caching
           is used only when the environment variable GCONV_PATH is not set.

## [](#OPTIONS)OPTIONS

           --nostdlib
                  Do not search the system default gconv directory, only the
                  directories provided on the command line.

           --output=outputfile
           -o outputfile
                  Use outputfile for output instead of the system default
                  cache location.

           --prefix=pathname
                  Set the prefix to be prepended to the system pathnames.
                  See FILES, below.  By default, the prefix is empty.
                  Setting the prefix to foo, the gconv module configuration
                  would be read from foo/usr/lib/gconv/gconv-modules and the
                  cache would be written to
                  foo/usr/lib/gconv/gconv-modules.cache.

           --help
           -?     Print a usage summary and exit.

           --usage
                  Print a short usage summary and exit.

           --version
           -V     Print the version number, license, and disclaimer of
                  warranty for iconv.

## [](#EXIT_STATUS)EXIT STATUS

           Zero on success, nonzero on errors.

## [](#FILES)FILES

           /usr/lib/gconv
                  Usual default gconv module path.

           /usr/lib/gconv/gconv-modules
                  Usual system default gconv module configuration file.

           /usr/lib/gconv/gconv-modules.cache
                  Usual system gconv module configuration cache.

           Depending on the architecture, the above files may instead be
           located at directories with the path prefix /usr/lib64.

## [](#SEE_ALSO)SEE ALSO

           iconv(1), iconv(3)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2025-05-17                 iconvconfig(8)

------------------------------------------------------------------------

Pages that refer to this page: [iconv(1)](../man1/iconv.1.html),  [iconv(3)](../man3/iconv.3.html)

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
