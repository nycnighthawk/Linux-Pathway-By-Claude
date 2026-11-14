---
{"title": "sepolicy-booleans(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/sepolicy-booleans.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sepolicy-booleans(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    sepolicy-booleans(8)                                 sepolicy-booleans(8)

## [](#NAME)NAME

           sepolicy-booleans - Query SELinux Policy to see description of
           booleans

## [](#SYNOPSIS)SYNOPSIS

           sepolicy booleans [-h] [ -a | -b booleanname ... ]

## [](#DESCRIPTION)DESCRIPTION

           sepolicy booleans will show all booleans and their descriptions,
           or you can choose individual booleans to display.  Please make
           sure that selinux-policy-devel is present in your system since it
           contains boolean descriptions extracted from the policy source
           code. Otherwise sepolicy booleans will only show descriptions
           generated based on boolean names.

## [](#OPTIONS)OPTIONS

           -h, --help
                  Display help message

           -a, --all
                  Display all boolean descriptions

           -b, --boolean
                  boolean to get description

## [](#EXAMPLE)EXAMPLE

           List descriptions of samba_create_home_dirs and samba_enable_home_dirs booleans
           # sepolicy booleans -b samba_create_home_dirs samba_enable_home_dirs

## [](#AUTHOR)AUTHOR

           This man page was written by Daniel Walsh <dwalsh@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           sepolicy(8), selinux(8), getsebool(8), setsebool(8)

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

                                     20121112            sepolicy-booleans(8)

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
