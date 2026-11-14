---
{"title": "sepolicy-transition(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/sepolicy-transition.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sepolicy-transition(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sepolicy-transition(8)                             sepolicy-transition(8)

## [](#NAME)NAME

           sepolicy-transition - Examine the SELinux Policy and generate a
           process transition report

## [](#SYNOPSIS)SYNOPSIS

           sepolicy transition [-h] -s SOURCE

           sepolicy transition [-h] -s SOURCE -t TARGET

## [](#DESCRIPTION)DESCRIPTION

           sepolicy transition will show all domains that a given SELinux
           source domain can transition to, including the entrypoint.

           If a target domain is given, sepolicy transition will examine
           policy for all transition paths from the source domain to the
           target domain, and will list the paths.

## [](#OPTIONS)OPTIONS

           -h, --help
                  Display help message

           -s, --source
                  Specify the source SELinux domain type

           -t, --target
                  Specify the target SELinux domain type

## [](#EXAMPLE)EXAMPLE

           List all domain transition paths from init_t to httpd_t
           # sepolicy transition -s init_t -t httpd_t
           List all transitions available from samba domain, including entry points and booleans controlling each transition
           # sepolicy transition -s smbd_t

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

                                     20121005          sepolicy-transition(8)

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
