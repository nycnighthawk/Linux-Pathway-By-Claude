---
{"title": "selinuxenabled(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/selinuxenabled.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# selinuxenabled(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                             |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    selinuxenabled(8)   SELinux Command Line documentation  selinuxenabled(8)

## [](#NAME)NAME

           selinuxenabled - tool to be used within shell scripts to determine
           if selinux is enabled

## [](#SYNOPSIS)SYNOPSIS

           selinuxenabled

## [](#DESCRIPTION)DESCRIPTION

           Indicates whether SELinux is enabled or disabled.

## [](#EXIT_STATUS)EXIT STATUS

           It exits with status 0 if SELinux is enabled and 1 if it is not
           enabled.

## [](#AUTHOR)AUTHOR

           Dan Walsh, <dwalsh@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           selinux(8), setenforce(8), getenforce(8)

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

    dwalsh@redhat.com              7 April 2004             selinuxenabled(8)

------------------------------------------------------------------------

Pages that refer to this page: [getenforce(8)](../man8/getenforce.8.html),  [setenforce(8)](../man8/setenforce.8.html)

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
