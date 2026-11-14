---
{"title": "sepolicy-interface(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/sepolicy-interface.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sepolicy-interface(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sepolicy-interface(8)                               sepolicy-interface(8)

## [](#NAME)NAME

           sepolicy-interface - Print interface information based on the
           installed SELinux Policy

## [](#SYNOPSIS)SYNOPSIS

           sepolicy interface [-h] [-c] [-v] [-f FILE] [-a | -u | -l | -i
           INTERFACE [INTERFACE ... ]]

## [](#DESCRIPTION)DESCRIPTION

           Use sepolicy interface to print information of interface macros
           between domains in SELinux policy modules, as used in Reference
           Policy. The information is based on installed on-disk
           representation of the SELinux Policy and it may be different from
           the policy which is currently loaded.

## [](#OPTIONS)OPTIONS

           -a, --list_admin
                  List all domains with admin interface

           -c, --compile
                  Test compile of interfaces

           -h, --help
                  Display help message

           -i, --interface
                  Interface(s) to be displayed

           -l, --list
                  List all interfaces

           -u, --list_user
                  List all domains with SELinux user role interface

           -v, --verbose
                  Display extended information about the interface including
                  parameters and description if available.

           -f, --file
                  Interface file to be explored

## [](#EXAMPLE)EXAMPLE

           Show description of given interface
           # sepolicy interface -vi samba_rw_config
           List interfaces in given interface file and show their description
           # sepolicy interface -f my_policy.if -lv
           Run compile test for all interfaces in given file
           # sepolicy interface -f my_policy.if -lc

## [](#AUTHOR)AUTHOR

           This man page was written by Daniel Walsh <dwalsh@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           sepolicy(8), selinux(8)

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

                                     20121222           sepolicy-interface(8)

------------------------------------------------------------------------

Pages that refer to this page: [sepolicy(8)](../man8/sepolicy.8.html)

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
