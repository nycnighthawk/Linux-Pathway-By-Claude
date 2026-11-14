---
{"title": "dpkg-vendor(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dpkg-vendor.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dpkg-vendor(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dpkg-vendor(1)                  dpkg suite                 dpkg-vendor(1)

## [](#NAME)NAME

           dpkg-vendor - queries information about distribution vendors

## [](#SYNOPSIS)SYNOPSIS

           dpkg-vendor [option...] command

## [](#DESCRIPTION)DESCRIPTION

           dpkg-vendor is a tool to query information about vendors listed in
           /usr/local/etc/dpkg/origins.  /usr/local/etc/dpkg/origins/default
           contains information about the current vendor.

           The origin files provide metadata about specific vendors, such as
           their URL or where to file bug reports, and are usually used both
           to determine the behavior of tools and resulting contents during
           package builds targeting a specific vendor, and to describe the
           provenance of packages.

           Packages can explicitly declare their vendor by including an
           Origin field, otherwise the vendor for a package without such
           field is assumed to be the one pointed to by the default origin
           symbolic link.

           The default symbolic link is also used to denote the origin of the
           current installation managed by dpkg, be that a full distribution
           or an overlay on top of an existing base system that contains
           either no packaging system or a native one.

           This program was introduced in dpkg 1.15.1.

## [](#COMMANDS)COMMANDS

           --is vendor
               Exits with 0 if the current vendor is vendor.  Otherwise exits
               with 1.

           --derives-from vendor
               Exits with 0 if the current vendor distribution is a
               derivative of vendor, otherwise exits with 1.  It uses the
               Parent field to browse all ancestors of the current vendor.

           --query field
               Print on standard output the value of the vendor-specific
               field for the current vendor.

           --help
               Show the usage message and exit.

           --version
               Show the version and exit.

## [](#OPTIONS)OPTIONS

           --vendor vendor
               Assumes the current vendor is vendor instead of discovering it
               with the DEB_VENDOR environment variable or
               /usr/local/etc/dpkg/origins/default.

## [](#ENVIRONMENT)ENVIRONMENT

           DEB_VENDOR
               This setting defines the current vendor.  If not set, it will
               discover the current vendor by reading
               /usr/local/etc/dpkg/origins/default.

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

       Packaging support
           /usr/local/share/dpkg/vendor.mk
               Makefile snippet that sets the current vendor and its parent
               into variables, and provides make macros to check for
               derivatives.

               Supported since dpkg 1.16.1.

## [](#SEE_ALSO)SEE ALSO

           deb-origin(5).

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

    1.23.7-216-gff7e9               2026-03-07                 dpkg-vendor(1)

------------------------------------------------------------------------

Pages that refer to this page: [deb-origin(5)](../man5/deb-origin.5.html),  [deb-src-rules(5)](../man5/deb-src-rules.5.html),  [deb-substvars(5)](../man5/deb-substvars.5.html)

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
