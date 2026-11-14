---
{"title": "yum-builddep(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/yum-builddep.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# yum-builddep(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [GENERAL OPTIONS](#GENERAL_OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    yum-builddep(1)                                           yum-builddep(1)

## [](#NAME)NAME

           yum-builddep - install missing dependencies for building an RPM
           package

## [](#SYNOPSIS)SYNOPSIS

           yum-builddep package

           yum-builddep /path/to/local/package.src.rpm

           yum-builddep /path/to/local/package.spec

## [](#DESCRIPTION)DESCRIPTION

           yum-builddep is a program which installs the RPMs needed to build
           the specified package.  The source RPM for the specified package
           must be available in a Yum repository (which will be automatically
           enabled, if it is disabled) or it can be a local source RPM or a
           spec file.

           Note, that only the BuildRequires information within the SRPM
           header information is used to determine build dependencies. This
           will specifically omit any dependencies that are required only for
           specific architectures.

## [](#GENERAL_OPTIONS)GENERAL OPTIONS

           --target ARCH
                  Set target architecture for spec parsing.

           --define 'MACRO EXPR'
                  Define the rpm MACRO with value EXPR for spec parsing.

## [](#EXAMPLES)EXAMPLES

           Download and install all the RPMs needed to build the kernel RPM:
                  yumdownloader --source kernel && rpm2cpio kernel*src.rpm |
                  cpio -i kernel.spec && \
                  yum-builddep kernel.spec

           The kernel includes specific BuildRequires dependencies for
           different architectures. In order to make sure that those
           dependencies are downloaded and installed, the SRPM should be
           downloaded, the .spec file extracted from it and used to determine
           the full dependency list.

## [](#FILES)FILES

           As yum-builddep uses YUM libraries for retrieving all the
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

    Panu Matilainen               17 July 2005                yum-builddep(1)

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
