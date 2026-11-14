---
{"title": "rpmsort(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/rpmsort.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpmsort(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ARGUMENTS](#ARGUMENTS) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPMSORT(1)               General Commands Manual               RPMSORT(1)

## [](#NAME)NAME

           rpmsort - Sort input by RPM Package Manager (RPM) versioning

## [](#SYNOPSIS)SYNOPSIS

           rpmsort [ FILE ... ]

## [](#DESCRIPTION)DESCRIPTION

           rpmsort(1) sorts the content of the input files, and writes a
           sorted list to standard out - like sort(1), but aware of RPM
           versioning.

## [](#ARGUMENTS)ARGUMENTS

           FILE
               A text-file containing lines to sort. If FILE is omitted or -
               given, data is read from standard in and written to standard
               out.

## [](#OPTIONS)OPTIONS

           rpmsort has no options.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a nonzero failure code otherwise.

## [](#EXAMPLES)EXAMPLES

           echo -e 'rpm-4.18.0-3.fc38.x86_64\nrpm-4.18.0-1.fc38.x86_64' |
           rpmsort
                   rpm-4.18.0-1.fc38.x86_64
                   rpm-4.18.0-3.fc38.x86_64

## [](#SEE_ALSO)SEE ALSO

           rpm-version(7)

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

    RPM 6.1.90                      2026-08-03                     RPMSORT(1)

------------------------------------------------------------------------

Pages that refer to this page: [rpmsort(1)](../man1/rpmsort.1.html),  [rpm-version(7)](../man7/rpm-version.7.html)

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
