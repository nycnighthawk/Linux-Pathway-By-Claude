---
{"title": "semodule_unpackage(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/semodule_unpackage.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# semodule_unpackage(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SEMODULE_PACKAGE(8)      System Manager's Manual      SEMODULE_PACKAGE(8)

## [](#NAME)NAME

           semodule_unpackage - Extract policy module and file context file
           from an SELinux policy module package.

## [](#SYNOPSIS)SYNOPSIS

           semodule_unpackage ppfile modfile [fcfile]

## [](#DESCRIPTION)DESCRIPTION

           semodule_unpackage is a tool used to extract SELinux policy module
           file and file context file from an SELinux Policy Package.

## [](#EXAMPLE)EXAMPLE

           # Extract the httpd module file from httpd policy package.
           $ semodule_unpackage httpd.pp httpd.mod httpd.fc

## [](#SEE_ALSO)SEE ALSO

           semodule_package(8)

## [](#AUTHORS)AUTHORS

           This manual page was written by Dan Walsh <dwalsh@redhat.com>.
           The program was written by Stephen Smalley <stephen.smalley.work@gmail.com>

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

    Security Enhanced Linux          Nov 2005             SEMODULE_PACKAGE(8)

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
