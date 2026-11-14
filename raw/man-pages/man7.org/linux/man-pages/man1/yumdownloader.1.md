---
{"title": "yumdownloader(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/yumdownloader.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# yumdownloader(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [GENERAL OPTIONS](#GENERAL_OPTIONS) \| [ADDITIONAL OPTIONS](#ADDITIONAL_OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                 |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    yumdownloader(1)                                         yumdownloader(1)

## [](#NAME)NAME

           yumdownloader - download RPM packages from Yum repositories

## [](#SYNOPSIS)SYNOPSIS

           yumdownloader [options] package1 [package2...]

## [](#DESCRIPTION)DESCRIPTION

           yumdownloader is a program for downloading RPMs from Yum
           repositories.

## [](#GENERAL_OPTIONS)GENERAL OPTIONS

           -h, --help
                  Help; display a help message and then quit.

           --destdir DIR
                  Specify a destination directory for the download.  Defaults
                  to the current directory.

           --urls Instead of downloading RPMs, list the URLs that would be
                  downloaded.

           --resolve
                  When downloading RPMs, resolve dependencies and also
                  download the required packages.

           --source
                  Instead of downloading the binary RPMs, download the source
                  RPMs.

           --archlist=ARCH1[,ARCH2...]
                  Limit the query to packages of given and compatible
                  architectures. Valid values are all architectures known to
                  rpm/yum such as 'i386' and 'src' for source RPMS. Note that
                  repoquery will now change yum's "arch" to the first value
                  in the archlist. So "--archlist=i386,i686" will change
                  yum's canonical arch to i386, but allow packages of i386
                  and i686.

## [](#ADDITIONAL_OPTIONS)ADDITIONAL OPTIONS

           Yumdownloader inherits all other options from yum. See the yum(8)
           man page for more information

## [](#EXAMPLES)EXAMPLES

           Download the kernel RPM to /var/tmp:
                  yumdownloader --destdir /var/tmp kernel

           List the URL for the kernel and kernel-smp RPMs:
                  yumdownloader --urls kernel kernel-smp

## [](#FILES)FILES

           As yumdownloader uses YUM libraries for retrieving all the
           information, it relies on YUM configuration for its default values
           like which repositories to use. Consult YUM documentation for
           details:

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

    Gijs Hollestelle             28 November 2005            yumdownloader(1)

------------------------------------------------------------------------

Pages that refer to this page: [yum-utils(1)](../man1/yum-utils.1.html),  [yum(8@@yum)](../man8/yum.8@@yum.html)

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
