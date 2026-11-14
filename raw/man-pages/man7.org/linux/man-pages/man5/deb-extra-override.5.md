---
{"title": "deb-extra-override(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-extra-override.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-extra-override(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-extra-override(5)           dpkg suite          deb-extra-override(5)

## [](#NAME)NAME

           deb-extra-override - Debian archive extra override file

## [](#SYNOPSIS)SYNOPSIS

           override

## [](#DESCRIPTION)DESCRIPTION

           While most information about a binary/source package can be found
           in the control/.dsc file, all of it can be overridden when it's
           exported to Packages/Sources files.  The extra override file
           contains those overrides.

           The extra override file has a simple whitespace-delimited format.
           Comments are allowed (denoted with a #).

               package field-name value

           package is the name of the binary/source package.

           field-name is the name of the field that is overridden.

           value is the value to put in the field.  It can contain spaces as
           the line is split in no more than 3 columns when it's parsed.

           The extra override files used to make the official Packages lists
           may be found in the indices directory on any Debian mirror.

## [](#SEE_ALSO)SEE ALSO

           dpkg-scanpackages(1), dpkg-scansources(1), apt-ftparchive(1).

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

    1.22.6-77-g86fe7                2024-03-10          deb-extra-override(5)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-scanpackages(1)](../man1/dpkg-scanpackages.1.html),  [dpkg-scansources(1)](../man1/dpkg-scansources.1.html)

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
