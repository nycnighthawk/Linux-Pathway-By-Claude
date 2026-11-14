---
{"title": "repoclosure(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/repoclosure.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# repoclosure(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    repoclosure(1)                                             repoclosure(1)

## [](#NAME)NAME

           repoclosure - display a list of unresolved dependencies for a yum
           repository

## [](#SYNOPSIS)SYNOPSIS

           repoclosure [options]

## [](#DESCRIPTION)DESCRIPTION

           repoclosure is a program that reads package metadata from one or
           more yum repositories, checks all dependencies, and displays a
           list of packages with unresolved dependencies.

## [](#OPTIONS)OPTIONS

           -h, --help
                  Display a help message, and then quit.

           -c CONFIG, --config=CONFIG
                  Config file to use (defaults to /etc/yum.conf).

           -a ARCH, --arch=ARCH
                  Check packages of the given archs, can be specified
                  multiple times (default: current arch).

           --basearch=BASEARCH
                  Set the basearch for yum to run as.

           -b, --builddeps
                  Check build dependencies only (needs source repos enabled).

           -l LOOKASIDE, --lookaside=LOOKASIDE
                  Specify a lookaside repo id to query, can be specified
                  multiple times.

           -r REPOID, --repoid=REPOID
                  Specify repo ids to query, can be specified multiple times
                  (default is all enabled).

           -t, --tempcache
                  Use a temp dir for storing/accessing yum-cache.

           -q, --quiet
                  Run quietly: no warnings printed to stderr.

           -n, --newest
                  Check only the newest packages in the repos.

           --repofrompath=REPOID,PATH/URL
                  Specify a path or url to a repository (same path as in a
                  baseurl) to add to the repositories for this query. This
                  option can be used multiple times. If you want to view only
                  the pkgs from this repository combine this with --repoid.
                  The repoid for the repository is specified by REPOID.

           -p PKG, --pkg=PKG
                  Check closure for this package only

           -g GROUP, --group=GROUP
                  Check closure for packages in this group only

## [](#SEE_ALSO)SEE ALSO

           yum.conf(5)
           http://yum.baseurl.org/

## [](#AUTHORS)AUTHORS

           See the Authors file included with this program.

## [](#COLOPHON)COLOPHON

           This page is part of the yum-utils (Yum Package Manager utilities)
           project.  Information about the project can be found at 
           ⟨https://github.com/rpm-software-management/yum⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/rpm-software-management/yum-utils.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2020-03-11.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                 13 January 2013               repoclosure(1)

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
