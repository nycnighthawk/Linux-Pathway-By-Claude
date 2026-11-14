---
{"title": "genhomedircon(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/genhomedircon.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# genhomedircon(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GENHOMEDIRCON(8)                 SELinux                 GENHOMEDIRCON(8)

## [](#NAME)NAME

           genhomedircon - generate SELinux file context configuration
           entries for user home directories

## [](#DESCRIPTION)DESCRIPTION

           genhomedircon is a script that executes semodule to rebuild the
           currently active SELinux policy (without reloading it) and to
           create the labels for each user home directory based on directory
           paths returned by calls to getpwent().

           The latter functionality depends on the "usepasswd" parameter
           being set to "true" (default) in /etc/selinux/semanage.conf.

           This script is usually executed by semanage although this default
           behavior can be optionally modified by setting to "true" the
           "disable-genhomedircon" in /etc/selinux/semanage.conf.

           Directories can be excluded from the list of home directories by
           the setting "ignoredirs" in /etc/selinux/semanage.conf.

## [](#AUTHOR)AUTHOR

           This manual page was written by Dan Walsh <dwalsh@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           semanage.conf(5), semodule(8), semanage(8), getpwent(3),
           getpwent_r(3)

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

    Security Enhanced Linux          Sep 2011                GENHOMEDIRCON(8)

------------------------------------------------------------------------

Pages that refer to this page: [selabel_file(5)](../man5/selabel_file.5.html)

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
