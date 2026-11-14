---
{"title": "show-changed-rco(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/show-changed-rco.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# show-changed-rco(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    show-installed(1)                                       show-installed(1)

## [](#NAME)NAME

           show-changed-rco - show changes in an RPM package

## [](#SYNOPSIS)SYNOPSIS

           show-changed-rco [options]

## [](#DESCRIPTION)DESCRIPTION

           show-changed-rco gives a compact description of the changes to a
           packages Requires, Conflicts and Obsoletes data from the installed
           (or old) to a specified rpm file.

## [](#OPTIONS)OPTIONS

           -h, --help
                  show this help message and exit

           -C, --cache
                  Tells repoquery to run entirely from YUM cache - does not
                  download any metadata or update the cache. Queries in this
                  mode can fail or give partial/incorrect results if the
                  cache isn't fully populated beforehand with eg "yum
                  makecache".

           -c <config file>, --config=<config file>
                  Use alternative config file (default is /etc/yum.conf).

           --repoid=<repo>
                  Specify which repository to query. Using this option
                  disables all repositories not explicitly enabled with
                  --repoid option (can be used multiple times). By default
                  repoquery uses whatever repositories are enabled in YUM
                  configuration.

           --enablerepo=<repo>
                  In addition to the default set, query the given additional
                  repository, even if it is disabled in YUM configuration.
                  Can be used multiple times.

           --disablerepo=<repo>
                  Do not query the given repository, even if it is enabled in
                  YUM configuration.  Can be used multiple times.

           --repofrompath=<repoid>,<path/url>
                  Specify a path or url to a repository (same path as in a
                  baseurl) to add to the repositories for this query. This
                  option can be used multiple times. If you want to view only
                  the pkgs from this repository combine this with --repoid.
                  The repoid for the repository is specified by <repoid>.

           --old-packages=<pkg>
                  Explicitly list the valid old packages to match the new
                  packages against.

           --ignore-arch
                  Ignore arch. so you can compare foo-2.i686 to foo-1.x86_64.

           --skip-new
                  Only give output for packages which we've found an old
                  package for.

## [](#SEE_ALSO)SEE ALSO

           yum.conf(5)
           http://yum.baseurl.org/

## [](#AUTHORS)AUTHORS

           See the Authors file included with this program.

## [](#BUGS)BUGS

           There are of course no bugs, but should you find any, you should
           first consult the FAQ section on http://yum.baseurl.org/wiki/Faq
           and if unsuccessful in finding a resolution contact the mailing
           list: yum-devel@lists.baseurl.org.  To file a bug use
           http://bugzilla.redhat.com for Fedora/RHEL/Centos related bugs and
           http://yum.baseurl.org/report for all other bugs.

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

    James Antill                  30 March 2011             show-installed(1)

------------------------------------------------------------------------

Pages that refer to this page: [yum-utils(1)](../man1/yum-utils.1.html)

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
