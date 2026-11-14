---
{"title": "sestatus(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/sestatus.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sestatus(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sestatus(8)         SELinux command line documentation        sestatus(8)

## [](#NAME)NAME

           sestatus - SELinux status tool

## [](#SYNOPSIS)SYNOPSIS

           sestatus [-v] [-b]

           This tool is used to get the status of a system running SELinux.

## [](#DESCRIPTION)DESCRIPTION

           This manual page describes the sestatus program.

           This tool is used to get the status of a system running SELinux.
           It displays data about whether SELinux is enabled or disabled,
           location of key directories, and the loaded policy with its status
           as shown in the example:
                  > sestatus
                  SELinux status:              enabled
                  SELinuxfs mount:             /selinux
                  SELinux root directory:      /etc/selinux
                  Loaded policy name:          targeted
                  Current mode:                permissive
                  Mode from config file:       enforcing
                  Policy MLS status:           enabled
                  Policy deny_unknown status:  allow
                  Memory protection checking:  actual (secure)
                  Max kernel policy version:   26

           sestatus can also be used to display:

                  -   The security context of files and processes listed in
                      the /etc/sestatus.conf file. The format of this file is
                      described in sestatus.conf(5).

                  -   The status of booleans.

## [](#OPTIONS)OPTIONS

           -v
                  Displays the contexts of files and processes listed in the
                  /etc/sestatus.conf file. It also checks whether the file is
                  a symbolic link, if so then the context of the target file
                  is also shown.

                  The following contexts will always be displayed:
                         The current process context
                         The init process context
                         The controlling terminal file context

           -b
                  Display the current state of booleans.

## [](#FILES)FILES

           /etc/sestatus.conf

## [](#AUTHOR)AUTHOR

           This man page was written by Daniel Walsh <dwalsh@redhat.com>.
           The program was written by Chris PeBenito <pebenito@gentoo.org>

## [](#SEE_ALSO)SEE ALSO

           selinux(8), sestatus.conf(5)

## [](#COLOPHON)COLOPHON

           This page is part of the selinux (Security-Enhanced Linux user-
           space libraries and tools) project.  Information about the project
           can be found at ⟨https://github.com/SELinuxProject/selinux/wiki⟩.
           If you have a bug report for this manual page, see
           ⟨https://github.com/SELinuxProject/selinux/wiki/Contributing⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/SELinuxProject/selinux⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Security Enhanced Linux        26 Nov 2011                    sestatus(8)

------------------------------------------------------------------------

Pages that refer to this page: [selinux_config(5)](../man5/selinux_config.5.html),  [sestatus.conf(5)](../man5/sestatus.conf.5.html)

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
