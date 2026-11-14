---
{"title": "repotrack(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/repotrack.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# repotrack(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    repotrack(1)                                                 repotrack(1)

## [](#NAME)NAME

           repotrack - track a package and its dependencies and download them

## [](#SYNOPSIS)SYNOPSIS

           repotrack [options] package1 [package2...]

## [](#DESCRIPTION)DESCRIPTION

           repotrack is a program for keeping track of a particular package
           and its dependencies. It will download one or more packages and
           all dependencies.

## [](#OPTIONS)OPTIONS

           -h, --help
                  Display a help message, and then quit.

           -c CONFIG, --config=CONFIG
                  Config file to use (defaults to /etc/yum.conf).

           -a ARCH, --arch=ARCH
                  Act as if running the specified arch (default: current
                  arch).

           -r REPOID, --repoid=REPOID
                  Specify repo ids to query, can be specified multiple times
                  (default is all enabled).

           --repofrompath=<repoid>,<path/url>
                  Specify repoid & paths of additional repositories - unique
                  repoid and complete path required, can be specified
                  multiple times.  Example:
                  --repofrompath=myrepo,/path/to/repo

           -t, --tempcache
                  Use a temp dir for storing/accessing yum-cache.

           -p DESTDIR, --download_path=DESTDIR
                  Path to download packages to.

           -u, --urls
                  Instead of downloading RPMs, list the URLs that would be
                  downloaded.

           -n, --newest
                  Toggle downloading only the newest packages (defaults to
                  newest-only).

           -q, --quiet
                  Output as little information as possible.

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

                                 13 January 2013                 repotrack(1)

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
