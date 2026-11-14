---
{"title": "unsetfiles(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/unsetfiles.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# unsetfiles(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ARGUMENTS](#ARGUMENTS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UNSETFILES(1)            General Commands Manual            UNSETFILES(1)

## [](#NAME)NAME

           unsetfiles - Remove SELinux file security contexts.

## [](#SYNOPSIS)SYNOPSIS

           unsetfiles [-hnrvx] pathname ...

## [](#DESCRIPTION)DESCRIPTION

           This program removes the SELinux file security contexts of files.
           It can help cleaning extended file attributes after disabling
           SELinux.

           unsetfiles will only work on SELinux disabled systems, since
           removing file security contexts is not supported by SELinux.

## [](#OPTIONS)OPTIONS

           -h     Show usage information and exit.

           -n     Do not actually remove any SELinux file security contexts.

           -r     Remove SELinux file security contexts recursive.

           -v     Be verbose about performed actions.

           -x     Do not cross filesystem boundaries.

## [](#ARGUMENTS)ARGUMENTS

           pathname ...
                  One or more path names to operate on.

## [](#SEE_ALSO)SEE ALSO

           restorecon(8), setfiles(8)

## [](#AUTHORS)AUTHORS

           Christian Göttsche (cgzones@googlemail.com)

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

    Security Enhanced Linux       December 2023                 UNSETFILES(1)

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
