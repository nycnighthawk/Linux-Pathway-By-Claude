---
{"title": "deb-split(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-split.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-split(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FORMAT](#FORMAT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-split(5)                    dpkg suite                   deb-split(5)

## [](#NAME)NAME

           deb-split - Debian multi-part binary package format

## [](#SYNOPSIS)SYNOPSIS

           filename.deb

## [](#DESCRIPTION)DESCRIPTION

           The multi-part .deb format is used to split big packages into
           smaller pieces to ease transport in small media.

## [](#FORMAT)FORMAT

           The file is an ar archive with a magic value of !<arch>\n.  The
           file names might contain a trailing slash (since dpkg 1.15.6).

           The ar archive is composed of multiple members in a specific
           order:

           debian-split
               The first required member contains a series of lines,
               separated by newlines.  Currently eight lines are present:

               •   The format version number, 2.1 at the time this manual
                   page was written.

               •   The package name.

               •   The package version.

               •   The md5sum of the package.

               •   The total size of the package.

               •   The maximum part size.

               •   The current part number, followed by a slash and the total
                   amount of parts (as in ‘1/10’).

               •   The package architecture.

                   Supported since dpkg 1.16.1.

               Programs which read multi-part archives should be prepared for
               the minor format version number to be increased and additional
               lines to be present, and should ignore these if this is the
               case.

               If the major format version number has changed, an
               incompatible change has been made and the program should stop.
               If it has not, then the program should be able to safely
               continue, unless it encounters an unexpected member in the
               archive (except at the end), as described below.

           data.N
               The second, last required member, where N denotes the part
               number.  It contains the raw part data.

           These members must occur in this exact order.  Current
           implementations should ignore any additional members after data.N.
           Further members may be defined in the future, and (if possible)
           will be placed after these two.

## [](#SEE_ALSO)SEE ALSO

           deb(5), dpkg-split(1).

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

    1.23.7-216-gff7e9               2026-03-07                   deb-split(5)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-split(1)](../man1/dpkg-split.1.html)

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
