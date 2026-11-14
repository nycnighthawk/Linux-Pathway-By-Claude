---
{"title": "sepolicy-communicate(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/sepolicy-communicate.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sepolicy-communicate(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sepolicy-communicate(8)                           sepolicy-communicate(8)

## [](#NAME)NAME

           sepolicy-communicate - Generate a report showing if two SELinux
           Policy Domains can communicate

## [](#SYNOPSIS)SYNOPSIS

           sepolicy communicate [-h] -s SOURCE -t TARGET [-c TCLASS] [-S
           SOURCEACCESS] [-T TARGETACCESS]

## [](#DESCRIPTION)DESCRIPTION

           Use sepolicy communicate to examine SELinux Policy and determine
           if a source SELinux Domain can communicate with a target SELinux
           Domain.  The default command looks to see if there are any file
           types that the source domain can write, which the target domain
           can read.

## [](#OPTIONS)OPTIONS

           -c, --class
                  Specify the SELinux class which the source domain will
                  attempt to communicate with the target domain.  (Default
                  file)

           -h, --help
                  Display help message

           -s, --source
                  Specify the source SELinux domain type.

           -S, --sourceaccess
                  Specify the list of accesses used by the source SELinux
                  domain type to communicate with the target domain. Default
                  Open, Write.

           -t, --target
                  Specify the target SELinux domain type.

           -T, --targetaccess
                  Specify the list of accesses used by the target SELinux
                  domain type to receive communications from the source
                  domain. Default Open, Read.

## [](#EXAMPLE)EXAMPLE

           List types that can be used to communicate between samba daemon and apache server
           # sepolicy communicate -s httpd_t -t smbd_t
           Consider a type to be accessible by the source domain when it can be opened and appended to (as opposed to opened and written to)
           # sepolicy communicate -s httpd_t -t smbd_t -S open,append

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

                                     20121005         sepolicy-communicate(8)

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
