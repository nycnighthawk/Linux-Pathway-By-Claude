---
{"title": "rpmuncompress(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/rpmuncompress.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpmuncompress(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ARGUMENTS](#ARGUMENTS) \| [OPERATIONS](#OPERATIONS) \| [OPTIONS](#OPTIONS) \| [EXTRACT OPTIONS](#EXTRACT_OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                       |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPMUNCOMPRESS(1)         General Commands Manual         RPMUNCOMPRESS(1)

## [](#NAME)NAME

           rpmuncompress - RPM utility for compressed files and archives

## [](#SYNOPSIS)SYNOPSIS

           rpmuncompress [options] FILE

           rpmuncompress [options] [extract-options] {-x|--extract} ARCHIVE

## [](#DESCRIPTION)DESCRIPTION

           rpmuncompress is a utility for transparently outputting compressed
           and uncompressed files, and extracting archives.

           It's normally invoked internally by rpmbuild(1) to handle %setup
           and %patch related tasks in spec files, but can be useful manually
           invoked as well.

## [](#ARGUMENTS)ARGUMENTS

           FILE
               A regular file, optionally compressed.

           ARCHIVE
               A tar(1), zip(1), CAR or Ruby GEM file. tar archives may be
               compressed.

## [](#OPERATIONS)OPERATIONS

           By default, rpmuncompress outputs FILE to standard output similar
           to cat(1), but transparently decompressing many popular
           compression formats, similar to zcat(1).

           -x, --extract
               Extract the ARCHIVE passed as argument into the current
               directory, transparently uncompressing tar(1) archives if
               needed.

## [](#OPTIONS)OPTIONS

           -n, --dry-run
               Output the shell command that would be executed without this
               option.

           See rpm-common(8) for options common to all rpm executables.

## [](#EXTRACT_OPTIONS)EXTRACT OPTIONS

           -C PATH, --path=PATH
               Extract into to PATH regardless of the archive's internal
               layout.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a nonzero failure code otherwise.

## [](#EXAMPLES)EXAMPLES

           rpmuncompress /tmp/3911.patch.gz | patch -p1
               Uncompress and output /tmp/3911.patch.gz, similar to zcat(1),
               and pipe to patch(1).

           rpmuncompress -x myproject.zip
               Extract myproject.zip archive into the current directory.

           rpmuncompress -x -C myproject myproject-1.0.7rc1.tar.gz
               Uncompress and extract myproject-1.0.7rc1.tar.gz archive into
               myproject directory, regardless of it's internal structure.

## [](#SEE_ALSO)SEE ALSO

           rpm-common(8), rpmbuild(1), popt(3)

           http://www.rpm.org/ 

## [](#COLOPHON)COLOPHON

           This page is part of the rpm (RPM Package Manager) project.
           Information about the project can be found at 
           ⟨https://github.com/rpm-software-management/rpm⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/rpm-software-management/rpm.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-27.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    RPM 6.1.90                      2026-08-03               RPMUNCOMPRESS(1)

------------------------------------------------------------------------

Pages that refer to this page: [rpm-macros(7)](../man7/rpm-macros.7.html)

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
