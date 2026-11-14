---
{"title": "rpmdeps(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/rpmdeps.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpmdeps(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPERATIONS](#OPERATIONS) \| [ARGUMENTS](#ARGUMENTS) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                               |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPMDEPS(1)               General Commands Manual               RPMDEPS(1)

## [](#NAME)NAME

           rpmdeps - Generate RPM Package Dependencies

## [](#SYNOPSIS)SYNOPSIS

           rpmdeps <operation> [options]

           rpmdeps <operation> [options] FILE ...

## [](#DESCRIPTION)DESCRIPTION

           rpmdeps generates package dependencies for one or more files,
           received either as a list of filenames on the standard input, or
           command line arguments.

           rpmdeps is not normally invoked directly, but doing so can be
           useful for troubleshooting dependency generation and developing
           new dependency generators. The installation directory of rpmdeps
           can be determined with rpm -E "%{_rpmconfigdir}".

           Note that the actual rpmdeps command is only used for automatic
           dependency generation in a legacy compatibility mode of
           rpmbuild(1).

## [](#OPERATIONS)OPERATIONS

           --alldeps
               Print all the dependencies.

           --conflicts
               Print the conflicts dependencies.

           --enhances
               Print the enhances dependencies.

           --obsoletes
               Print the obsoletes dependencies.

           --orderwithrequires
               Print the orderwithrequires dependencies.

           -P, --provides
               Print the provides dependencies.

           --recommends
               Print the recommends dependencies.

           -R, --requires
               Print the requires dependencies.

           --suggests
               Print the suggests dependencies.

           --supplements
               Print the supplements dependencies.

## [](#ARGUMENTS)ARGUMENTS

           FILE
               Any regular file.

## [](#OPTIONS)OPTIONS

           See rpm-common(8) for the options common to all operations.

## [](#ENVIRONMENT)ENVIRONMENT

           RPM_BUILD_ROOT
               The prefix path to strip out when generating dependencies
               based on actual paths.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a nonzero failure code otherwise.

## [](#EXAMPLES)EXAMPLES

           rpmdeps --requires /bin/ls
               Output the automatic requires dependencies of the ls(1)
               binary.

           find popt-1.19-build/BUILDROOT -type f | /usr/lib/rpm/rpmdeps -P
               Output the automatic provides of all files in the
               popt-1.19-build/BUILDROOT directory

## [](#SEE_ALSO)SEE ALSO

           rpm(8), rpmbuild(1), rpm-common(8)

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

    RPM 6.1.90                      2026-08-03                     RPMDEPS(1)

------------------------------------------------------------------------

Pages that refer to this page: [rpm-dependency-generators(7)](../man7/rpm-dependency-generators.7.html)

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
