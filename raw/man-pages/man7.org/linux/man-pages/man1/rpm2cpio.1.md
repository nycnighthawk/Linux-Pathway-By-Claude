---
{"title": "rpm2cpio(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/rpm2cpio.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm2cpio(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ARGUMENTS](#ARGUMENTS) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM2CPIO(1)              General Commands Manual              RPM2CPIO(1)

## [](#NAME)NAME

           rpm2cpio - Extract cpio archive from RPM Package Manager (RPM)
           package

## [](#SYNOPSIS)SYNOPSIS

           rpm2cpio PACKAGE_FILE

           rpm2cpio -

## [](#DESCRIPTION)DESCRIPTION

           rpm2cpio converts the specified rpm package to a cpio(1) archive
           on the standard output.

           Note: the cpio(5) format cannot host individual files over 4GB in
           size, and so this tool is considered obsolete.  Use rpm2archive(1)
           instead.

## [](#ARGUMENTS)ARGUMENTS

           PACKAGE_FILE
               A binary or source RPM package.

           If dash (-) is given as the argument, data is read from the
           standard input.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a nonzero failure code otherwise.

## [](#EXAMPLES)EXAMPLES

           rpm2cpio glint-1.0-1.i386.rpm | cpio -dium
               Extract glint-1.0-1.i386.rpm contents relative to current
               directory.

           cat glint-1.0-1.i386.rpm | rpm2cpio - | cpio -tv
               View glint-1.0-1.i386.rpm file list with cpio(1).

## [](#SEE_ALSO)SEE ALSO

           cpio(1), rpm(8), rpm2archive(1)

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

    RPM 6.1.90                      2026-08-03                    RPM2CPIO(1)

------------------------------------------------------------------------

Pages that refer to this page: [rpm2archive(1)](../man1/rpm2archive.1.html),  [rpmbuild(1)](../man1/rpmbuild.1.html),  [rpm(8)](../man8/rpm.8.html)

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
