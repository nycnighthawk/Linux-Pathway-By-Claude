---
{"title": "yum-verify(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/yum-verify.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# yum-verify(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [GENERAL OPTIONS](#GENERAL_OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    yum-verify(1)                                               yum-verify(1)

## [](#NAME)NAME

           yum verify plugin

## [](#SYNOPSIS)SYNOPSIS

           yum [options] verify [package ...]

## [](#DESCRIPTION)DESCRIPTION

           This plugin extends yum with some commands that give verification
           information on the installed system, much like rpm -V. You can
           change how the verification is done and which files it applies to.
           In case any mismatches are found, the exit status is set to 1.

           added yum commands are:
            * verify
            * verify-rpm
            * verify-all

           all of which take the same arguments as the list yum command. You
           can only verify packages that are installed on the system.

           verify Is the generic verification command, and is intended to
                  give the most useful output. It removes all false matches
                  due to multilib and ignores changes to configuration files
                  by default.

           verify-rpm
                  Does the same checks as rpm -V.

           verify-all
                  Is used to list all the differences, including some that
                  rpm itself will ignore.

## [](#GENERAL_OPTIONS)GENERAL OPTIONS

           These are the options added to yum that are available in the
           verify commands.  They are:

           --verify-filenames
                  This option is used to limit the filenames that the
                  packages will perform verification.

           --verify-configuration-files
                  This option is only useful in the generic verify command,
                  and will enable/disable verification of files that are
                  tagged as configuration files.

## [](#EXAMPLES)EXAMPLES

           To do the same as rpm -Va, use:

                  yum verify-rpm

           To verify the packages starting with the name yum, use:

                  yum verify 'yum*'

           To verify the binaries that are in a bin directory, use:

                  yum verify --verify-filenames='*bin/*'

           To verify all include files, Eg. for multilib problems, use:

                  yum verify-all --verify-filenames='/usr/include/*'

## [](#SEE_ALSO)SEE ALSO

           yum(8)
           yum.conf(5)
           the verify.conf file in /etc/yum/plugins.d

## [](#AUTHORS)AUTHORS

           James Antill <james.antill@redhat.com>.

## [](#BUGS)BUGS

           Currently yum-verify does not do verify-script checking or dependency checking,
           only file checking.

           Should you find any other bugs, you should first
           consult the FAQ section on http://yum.baseurl.org/wiki/Faq and if unsuccessful
           in finding a resolution contact the mailing list: yum-devel@lists.baseurl.org.
           To file a bug use http://bugzilla.redhat.com for Fedora/RHEL/Centos
           related bugs and http://yum.baseurl.org/report for all other bugs.

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

    James Antill                  01 March 2008                 yum-verify(1)

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
