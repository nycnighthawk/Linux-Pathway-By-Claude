---
{"title": "yum-debug-dump(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/yum-debug-dump.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# yum-debug-dump(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    yum-debug-dump(1)                                       yum-debug-dump(1)

## [](#NAME)NAME

           yum-debug-dump - write system RPM configuration to a debug-dump
           file

## [](#SYNOPSIS)SYNOPSIS

           yum-debug-dump

## [](#DESCRIPTION)DESCRIPTION

           yum-debug-dump is a program which creates a gzipped file
           containing a lot of information useful to developers trying to
           debug a problem.

           By default it will output a file to the current working directory
           named yum_debug_dump-<hostname>-<time>.txt.gz. This file contains
           no private information but does contain a complete list of all
           packages you have installed, all packages available in any
           repository, important configuration and system information.  You
           can view this file using the 'zless' command.

           You can use the coresponding program yum-debug-restore to act on
           this file and restore a set of packages (much like dump/restore).

## [](#FILES)FILES

           As yum-debug-dump uses YUM libraries for retrieving all the
           information, it relies on YUM configuration for its default values
           like which repositories to use. Consult YUM documentation for
           details:

           /etc/yum.conf
           /etc/yum/repos.d/
           /var/cache/yum/

## [](#SEE_ALSO)SEE ALSO

           yum-debug-restore(1)
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

    Seth Vidal                    28 April 2008             yum-debug-dump(1)

------------------------------------------------------------------------

Pages that refer to this page: [yum-debug-restore(1)](../man1/yum-debug-restore.1.html),  [yum-utils(1)](../man1/yum-utils.1.html)

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
