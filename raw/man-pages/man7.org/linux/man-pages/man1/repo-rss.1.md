---
{"title": "repo-rss(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/repo-rss.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# repo-rss(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [GENERAL OPTIONS](#GENERAL_OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    repo-rss(1)                                                   repo-rss(1)

## [](#NAME)NAME

           repo-rss - generates an RSS feed from one or more Yum repositories

## [](#SYNOPSIS)SYNOPSIS

           repo-rss [options] repoid1 [repoid2...]

## [](#DESCRIPTION)DESCRIPTION

           repo-rss is a program for generating RSS feeds for one or more Yum
           repositories.

## [](#GENERAL_OPTIONS)GENERAL OPTIONS

           -h, --help
                  Help; display a help message and then quit.

           -f <file>
                  Specify the file to which the RSS will be written.  Default
                  is repo-rss.xml.

           -l <link>
                  Specify the URL to the RSS feed.  Default is
                  http://yum.baseurl.org/.

           -t <title>
                  Specify the title for the RSS feed.  Default is "RSS
                  Repository - Recent Packages".

           -d <description>
                  Specify the description of the RSS feed.  Default is "Most
                  recent packages in Repositories".

           -r <days>
                  Specify the number of days to consider most recent.
                  Default is 3.

           --tempcache
                  Enable the use of a temporary directory for the yum cache.
                  This is enabled by default for non-root users.

## [](#EXAMPLES)EXAMPLES

           Generate an RSS for the updates-released repository and save it as
           updates-release.xml:
                  repo-rss -f updates-released.xml updates-released

## [](#FILES)FILES

           As repo-rss uses YUM libraries for retrieving all the information,
           it relies on YUM configuration for its default values like which
           repositories to use. Consult YUM documentation for details:

           /etc/yum.conf
           /etc/yum/repos.d/
           /var/cache/yum/

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

    Seth Vidal                         2005                       repo-rss(1)

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
