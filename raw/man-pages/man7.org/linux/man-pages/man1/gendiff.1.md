---
{"title": "gendiff(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/gendiff.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# gendiff(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ARGUMENTS](#ARGUMENTS) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GENDIFF(1)               General Commands Manual               GENDIFF(1)

## [](#NAME)NAME

           gendiff - Utility to aid in error-free diff file generation

## [](#SYNOPSIS)SYNOPSIS

           gendiff DIRECTORY DIFF-EXTENSION

## [](#DESCRIPTION)DESCRIPTION

           gendiff is a tool for generating a diff file from a single
           directory. The generated diff can be applied with the patch(1)
           program to recreate the changes.

           gendiff looks for any files with DIFF-EXTENSION as their extension
           in the specified DIRECTORY, and runs diff(1) on the files with
           DIFF-EXTENSION and the counterpart without it, in that order. This
           allows for generating diffs from source code without making a full
           copy of the directory, which you'd otherwise need when using the
           diff(1) utility directly.

           gendiff is commonly used to creating patches for the purposes of
           packaging software with rpmbuild(1).

## [](#ARGUMENTS)ARGUMENTS

           DIRECTORY
               The directory to generate a diff from.

           DIFF-EXTENSION
               The diff extension to look for.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a nonzero failure code otherwise.

## [](#EXAMPLES)EXAMPLES

           Assuming you need to modify a source file called somefile.cpp and
           have chosen the extension fix, copy it to somefile.cpp.fix before
           editing it. Then edit the original file (somefile.cpp).

           After editing all the files you need to edit in this fashion,
           enter the directory one level above where the source code resides,
           and run gendiff on it:

               gendiff myproject-1.0 .fix > myproject-1.0-fix.patch

## [](#SEE_ALSO)SEE ALSO

           diff(1), patch(1)

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

    RPM 6.1.90                      2026-08-03                     GENDIFF(1)

------------------------------------------------------------------------

Pages that refer to this page: [rpmbuild(1)](../man1/rpmbuild.1.html)

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
