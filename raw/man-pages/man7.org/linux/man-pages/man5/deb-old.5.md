---
{"title": "deb-old(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-old.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-old(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FORMAT](#FORMAT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-old(5)                      dpkg suite                     deb-old(5)

## [](#NAME)NAME

           deb-old - old style Debian binary package format

## [](#SYNOPSIS)SYNOPSIS

           filename.deb

## [](#DESCRIPTION)DESCRIPTION

           The .deb format is the Debian binary package file format.  This
           manual page describes the old format, used before Debian 0.93.
           See deb(5) for details of the new format.

## [](#FORMAT)FORMAT

           The file is two lines of format information as ASCII text,
           followed by two concatenated gzipped ustar files.

           The first line is the format version number padded to 8 digits,
           and is 0.939000 for all old-format archives.

           The second line is a decimal string (without leading zeroes)
           giving the length of the first gzipped tarfile.

           Each of these lines is terminated with a single newline character.

           The first tarfile contains the package metadata, as a series of
           ordinary files.  The file control must be present, as it contains
           the package control information.

           In some very old archives, the files in the control tarfile may
           optionally be in a DEBIAN subdirectory.  In that case, the DEBIAN
           subdirectory will be in the control tarfile too, and the control
           tarfile will have only files in that directory.  Optionally the
           control tarfile may contain an entry for ‘.’, that is, the current
           directory.

           The second gzipped tarfile is the filesystem archive, containing
           pathnames relative to the root directory of the system to be
           installed on.  The pathnames do not have leading slashes.

## [](#SEE_ALSO)SEE ALSO

           deb(5), deb-control(5), dpkg-deb(1).

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

    1.23.7-121-gd39fb               2026-03-07                     deb-old(5)

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
