---
{"title": "yum-utils(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/yum-utils.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# yum-utils(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    yum-utils(1)                                                 yum-utils(1)

## [](#NAME)NAME

           yum-utils - tools for manipulating repositories and extended
           package management

## [](#SYNOPSIS)SYNOPSIS

           debuginfo-install - install debuginfo packages and their dependencies
           find-repos-of-install - report which repository the package was installed from
           needs-restarting - report process ids that started running before they or some component they use were updated
           package-cleanup - manage package cleanup, duplicates, orphaned packages and outstanding dependency problems
           repo-graph - outputs a full package dependency list in dot format
           repo-rss - generates an RSS feed from one or more repositories
           repoclosure - reads metadata of repositories, checks dependencies and displays list of unresolved dependencies
           repodiff - takes two or more repositories, returns a list of added, removed or changed packages
           repomanage - manages a directory of rpm packages, returns a list of newest or oldest packages in a directory
           repoquery - query yum repositories and get additional information on the them
           reposync - synchronize a remote yum repository to a local directory using yum to retrieve packages
           repotrack - track packages and its dependencies and downloads them
           show-changed-rco - list of changes to a package Requires, Conflicts and Obsoletes data from installed to a specified rpm file
           show-installed - gives a compact description of packages installed and makes use of comps groups in repositories
           verifytree - verify that a local yum repository is consistent
           yum-builddep - installs missing dependencies to build a specified package
           yum-complete-transaction - finds incomplete or aborted yum transactions and attempts to complete them
           yum-config-manager - toggle yum repositories, add new repositories and set main yum configuration options
           yum-debug-dump - creates gzipped file containing information for debugging problems
           yum-debug-restore - replays any transactions captured in gzipped file in yum shell
           yum-groups-manager - create and edit yum's group metadata
           yumdb - query or alter the yum database
           yumdownloader - downloads packages from yum repositories including source RPMs

## [](#DESCRIPTION)DESCRIPTION

           yum-utils is a collection of tools and programs for managing yum
           repositories, installing debug packages, source packages, extended
           information from repositories and administration.

## [](#NOTES)NOTES

           See respective tools for additional help for commands without a
           manual page

## [](#SEE_ALSO)SEE ALSO

           debuginfo-install(1), package-cleanup(1), repodiff(1),
           repoquery(1), reposync(1), repo-rss(1), show-changed-rco(1),
           show-installed(1), yumdownloader(1), yum-builddep(1),
           yum-debug-dump(1), yum-groups-manager(1), yumdb(8),
           yum-complete-transaction(8)

## [](#AUTHOR)AUTHOR

           Shawn Starr <shawn.starr@rogers.com>

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

    yum-utils                      August 2011                   yum-utils(1)

------------------------------------------------------------------------

Pages that refer to this page: [yum-aliases(1@@yum-utils)](../man1/yum-aliases.1@@yum-utils.html),  [yum(8@@yum)](../man8/yum.8@@yum.html)

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
