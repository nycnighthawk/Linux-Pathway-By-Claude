---
{"title": "find-repos-of-install(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/find-repos-of-install.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# find-repos-of-install(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    find-repos-of-install(1)                         find-repos-of-install(1)

## [](#NAME)NAME

           find-repos-of-install - report which Yum repository a package was
           installed from

## [](#SYNOPSIS)SYNOPSIS

           find-repos-of-install [options] package1 [package2...]

## [](#DESCRIPTION)DESCRIPTION

           find-repos-of-install is a program which reports the Yum
           repository that a specified package was installed from.

## [](#OPTIONS)OPTIONS

           --version
                  Report program version and exit.

           -h, --help
                  Display a help message, and then quit.

           --repoid=REPOID
                  Specify repo ids to query, can be specified multiple times
                  (default is all enabled).

           --enablerepo=ENABLEREPOS
                  In addition to the default set, query the given additional
                  repository, even if it is disabled in YUM configuration.
                  Can be used multiple times.

           --disablerepo=DISABLEREPOS
                  Do not query the given repository, even if it is enabled in
                  YUM configuration.  Can be used multiple times.

           --repofrompath=REPOID,PATH/URL
                  Specify a path or url to a repository (same path as in a
                  baseurl) to add to the repositories for this query. This
                  option can be used multiple times. If you want to view only
                  the pkgs from this repository combine this with --repoid.
                  The repoid for the repository is specified by REPOID.

           -C, --cache
                  Tells repoquery to run entirely from YUM cache - does not
                  download any metadata or update the cache. Queries in this
                  mode can fail or give partial/incorrect results if the
                  cache isn't fully populated beforehand with eg "yum
                  makecache".

           --tempcache
                  Use a temp dir for storing/accessing yum-cache.

           --sync2yumdb
                  Sync anything that is found to the yumdb, if available.

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

                                 13 January 2013     find-repos-of-install(1)

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
