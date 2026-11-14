---
{"title": "deb-origin(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-origin.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-origin(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FIELDS](#FIELDS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-origin(5)                   dpkg suite                  deb-origin(5)

## [](#NAME)NAME

           deb-origin - Vendor-specific information files

## [](#SYNOPSIS)SYNOPSIS

           /usr/local/etc/dpkg/origins/filename

## [](#DESCRIPTION)DESCRIPTION

           The files in /usr/local/etc/dpkg/origins can provide information
           about various vendors that are providing Debian packages.  These
           files are usually used both to determine the behavior of tools and
           resulting contents during package builds targeting a specific
           vendor, and to describe the provenance of packages.

           Packages can explicitly declare their vendor by including an
           Origin field, otherwise the vendor for a package without such
           field is assumed to be the one pointed to by the default origin
           symbolic link.

           They contain a number of fields, or comments when the line starts
           with ‘#’.  Each field begins with a tag, such as Vendor or Parent,
           followed by a colon and the body of the field.  Fields are
           delimited only by field tags.  In other words, field text may be
           multiple lines in length, but the tools will join lines when
           processing the body of the field.

           The file should be named according to the vendor name.  The usual
           convention is to name the vendor file using the vendor name in all
           lowercase, but some variation is permitted.

           Namely (since dpkg 1.21.10), first, non-alphanumeric characters
           (‘[^A-Za-z0-9]’) are mapped to dashes (‘-’), then the resulting
           name will be tried in sequence by lower-casing it, keeping it as
           is, lower-casing then capitalizing it (that is upper-casing the
           first character), and only capitalizing it.

## [](#FIELDS)FIELDS

           Vendor: vendor-name (required)
               The value of this field determines the vendor name.

           Vendor-URL: vendor-url
               The value of this field determines the vendor URL.

           Bugs: bug-url
               The value of this field determines the type and address of the
               bug tracking system used by this vendor.  It can be a mailto
               URL or a debbugs URL (e.g., debbugs://bugs.debian.org/).

           Parent: vendor-name
               The value of this field determines the vendor name of the
               vendor that this vendor derives from.

## [](#EXAMPLE)EXAMPLE

            Vendor: Debian
            Vendor-URL: https://www.debian.org/
            Bugs: debbugs://bugs.debian.org

## [](#SEE_ALSO)SEE ALSO

           dpkg-vendor(1).

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

    1.22.12-10-g32fee               2025-01-01                  deb-origin(5)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-vendor(1)](../man1/dpkg-vendor.1.html),  [deb822(5)](../man5/deb822.5.html)

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
