---
{"title": "deb-src-files(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-src-files.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-src-files(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-src-files(5)                dpkg suite               deb-src-files(5)

## [](#NAME)NAME

           deb-src-files - Debian distribute files format

## [](#SYNOPSIS)SYNOPSIS

           debian/files

## [](#DESCRIPTION)DESCRIPTION

           This file contains the list of artifacts that are to be
           distributed via the .changes control file.

           The debian/files file has a simple whitespace-delimited format.

               filename section priority [ keyword=value...  ]

           filename is the name of the artifact to distribute.

           section and priority correspond to the respective control fields
           available in the .deb.  The allowed values are specific to each
           distribution archive.

           keyword=value...  corresponds to an optional whitespace-delimited
           list of attributes for this entry.  The only currently supported
           keyword is:

           •   automatic

               With value yes, to mark automatically generated files.

## [](#NOTES)NOTES

           This file is not intended to be modified directly, use one of
           dpkg-gencontrol or dpkg-distaddfile to add entries to it.

## [](#SEE_ALSO)SEE ALSO

           dpkg-genchanges(1), dpkg-distaddfile(1).

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

    1.23.7-121-gd39fb               2026-03-07               deb-src-files(5)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-distaddfile(1)](../man1/dpkg-distaddfile.1.html),  [dpkg-genchanges(1)](../man1/dpkg-genchanges.1.html)

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
