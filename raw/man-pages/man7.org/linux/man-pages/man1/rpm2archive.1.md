---
{"title": "rpm2archive(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/rpm2archive.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm2archive(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ARGUMENTS](#ARGUMENTS) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM2ARCHIVE(1)           General Commands Manual           RPM2ARCHIVE(1)

## [](#NAME)NAME

           rpm2archive - Create tar or cpio archive from RPM Package Manager
           (RPM) package

## [](#SYNOPSIS)SYNOPSIS

           rpm2archive [options] [PACKAGE_FILE] ...

## [](#DESCRIPTION)DESCRIPTION

           rpm2archive converts RPM package files to other archive formats.

           If the standard output is a regular file or a pipe, the archive is
           written to the standard output. If the standard output is a
           terminal, the output is written to a file by the same name,
           appended with a .tgz or .cpio.gz suffix when compressed or .tar or
           .cpio otherwise depending on the format. The output is compressed
           in the gzip(1) format by default.

           rpm2archive does not verify package-level signatures or checksums,
           but it does verify the per-file checksums.

           Supports RPM package formats 3, 4 and 6.

## [](#ARGUMENTS)ARGUMENTS

           PACKAGE_FILE
               A binary or source RPM package.

           If no arguments are present, or a dash (-) is given as an
           argument, data is read from the standard input.

## [](#OPTIONS)OPTIONS

           -n, --nocompression
               Generate an uncompressed archive. If in the file creation
               mode, use .tar as postfix of the filename.

           -f, --format=<FORMAT>
               Generate archive in specified FORMAT:
               •   pax: Restricted Portable Archive Exchange as used by
                   tar(1) (default)
               •   cpio: The "new" ASCII cpio(5) format. Note that this
                   format has a 4GB limit on the individual file size.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a nonzero failure code otherwise.

## [](#EXAMPLES)EXAMPLES

           rpm2archive glint-1.0-1.i386.rpm | tar -xvz
               Extract glint-1.0-1.i386.rpm package contents with tar(1).

           rpm2archive --nocompression --format=cpio glint-1.0-1.i386.rpm |
           cpio -idv
               Extract glint-1.0-1.i386.rpm package contents as an
               uncompressed cpio(5), compatible with rpm2cpio(1) output.

           rpm2archive glint-1.0-1.i386.rpm ; tar -xvz
           glint-1.0-1.i386.rpm.tgz
               Extract glint-1.0-1.i386.rpm package contents into an archive
               named glint-1.0-1.i386.rpm.tgz and extract the written archive
               with tar(1).

           cat glint-1.0-1.i386.rpm | rpm2archive - | tar -tvz
               Feed glint-1.0-1.i386.rpm package into rpm2archive via
               standard input, and list contents with tar(1).

## [](#SEE_ALSO)SEE ALSO

           rpm2cpio(1), rpm(8)

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

    RPM 6.1.90                      2026-08-03                 RPM2ARCHIVE(1)

------------------------------------------------------------------------

Pages that refer to this page: [rpm2cpio(1)](../man1/rpm2cpio.1.html)

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
