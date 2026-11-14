---
{"title": "rpmgraph(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/rpmgraph.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpmgraph(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ARGUMENTS](#ARGUMENTS) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPMGRAPH(1)              General Commands Manual              RPMGRAPH(1)

## [](#NAME)NAME

           rpmgraph - Generate an RPM Package Dependency Graph

## [](#SYNOPSIS)SYNOPSIS

           rpmgraph [options] PACKAGE_FILE ...

## [](#DESCRIPTION)DESCRIPTION

           rpmgraph reads rpm packages passed as arguments, sorts them as for
           installation with rpm(8), and produces a dependency graph on the
           standard output.

           Nodes in the dependency graph are package names, and edges in the
           directed graph point to the parent of each node. The parent node
           is defined as the last predecessor of a package when partially
           ordered using the package dependencies as a relation. That means
           that the parent of a given package is the package's last
           prerequisite.

           The output is in dot(1) directed graph format, and can be
           displayed or printed using the dotty(1) graph editor from the
           Graphviz project.

## [](#ARGUMENTS)ARGUMENTS

           PACKAGE_FILE
               Either an rpm package or an rpm-manifest(5) file.

## [](#OPTIONS)OPTIONS

           See rpm-common(8) for the options common to all rpm commands.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a nonzero failure code otherwise.

## [](#SEE_ALSO)SEE ALSO

           dot(1), dotty(1)

           http://www.graphviz.org/ 

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

    RPM 6.1.90                      2026-08-03                    RPMGRAPH(1)

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
