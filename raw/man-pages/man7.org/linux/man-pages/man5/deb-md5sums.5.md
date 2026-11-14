---
{"title": "deb-md5sums(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-md5sums.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-md5sums(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-md5sums(5)                  dpkg suite                 deb-md5sums(5)

## [](#NAME)NAME

           deb-md5sums - package MD5 file digests

## [](#SYNOPSIS)SYNOPSIS

           DEBIAN/md5sums

## [](#DESCRIPTION)DESCRIPTION

           A package declares the MD5 digests for the package file contents
           by including an md5sums file in its control archive (i.e.
           DEBIAN/md5sums during package creation).  This file is used for
           integrity verification and deduplication purposes, and not for any
           kind of security purpose.

           This file contains a list of MD5 digests (as 32 case-insensitive
           hexadecimal characters) followed by two spaces (U+0020 SPACE) and
           the absolute pathname of a plain file, one per line.

           Trailing slashes (U+002F /) in the pathname will be trimmed.
           Neither trailing whitespace nor empty or whitespace-only lines are
           accepted.

           If the control file does not exist in the binary package, dpkg(1)
           will generate the matching information at unpack time (since dpkg
           1.16.3).

## [](#EXAMPLE)EXAMPLE

            53c0d4afe4bc4eccb5cb234d2e06ef4d  usr/bin/dpkg
            f8da2bc74cdcad8b81c48a4f0d7bb0a8  usr/bin/dpkg-deb
            70b913132de56e95e75de504979309b4  usr/bin/dpkg-divert
            […]

## [](#SEE_ALSO)SEE ALSO

           md5sum(1), dpkg-deb(1), dpkg(1).

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

    1.22.6-77-g86fe7                2024-03-10                 deb-md5sums(5)

------------------------------------------------------------------------

Pages that refer to this page: [deb(5)](../man5/deb.5.html)

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
