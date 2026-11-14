---
{"title": "debuginfo-install(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/debuginfo-install.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# debuginfo-install(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [WARNING MESSAGES](#WARNING_MESSAGES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    debuginfo-install(1)                                 debuginfo-install(1)

## [](#NAME)NAME

           debuginfo-install - install debuginfo packages and their
           dependencies

## [](#SYNOPSIS)SYNOPSIS

           debuginfo-install package

## [](#DESCRIPTION)DESCRIPTION

           debuginfo-install is a program which installs the RPMs needed to
           debug the specified package.  The package argument can be a
           wildcard, but will only match installed packages.  debuginfo-
           install will then enable any debuginfo repositories, and install
           the relevant debuginfo rpm.

## [](#EXAMPLES)EXAMPLES

           Download and install all the RPMs needed to debug the kernel RPM:
                  debuginfo-install kernel

## [](#WARNING_MESSAGES)WARNING MESSAGES

           Could not find debuginfo for:
                  You may sometimes see warning messages about certain
                  packages not being found if you run debuginfo-install for a
                  wildcard or glob. Debuginfo packages are not necessary for
                  "noarch" RPMs; these will generate a warning message.
                  Additionally, On 64-bit systems, no multilib debuginfo
                  packages are published, so if you have 32-bit packages
                  installed, these will also generate warning messages.

## [](#FILES)FILES

           As debuginfo-install uses YUM libraries for retrieving all the
           information, it relies on YUM configuration for its default values
           like which repositories to use. Consult YUM documentation for
           details:

           /etc/yum.conf
           /etc/yum/repos.d/
           /var/cache/yum/

## [](#SEE_ALSO)SEE ALSO

           yum.conf(5)
           http://yum-utils.baseurl.org/
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

    James Antill                 21 October 2008         debuginfo-install(1)

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
