---
{"title": "quotagrpadmins(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/quotagrpadmins.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# quotagrpadmins(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLE](#EXAMPLE) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    QUOTAGRPADMINS(5)          File Formats Manual          QUOTAGRPADMINS(5)

## [](#NAME)NAME

           quotagrpadmins - users responsible for group disk usage

## [](#SYNOPSIS)SYNOPSIS

           /etc/quotagrpadmins

## [](#DESCRIPTION)DESCRIPTION

           The quotagrpadmins file lists administrators of user groups who
           will receive a warning if warnquota --group command finds a group
           exceeding its disk usage limits.

           Each line consists of a group name followed by a colon and a user
           name. White space characters surrounding the names are allowed.
           Empty lines or lines starting with a hash sign or a semicolon are
           ignored.

## [](#EXAMPLE)EXAMPLE

           # comment
           users: root

## [](#FILES)FILES

           /etc/quotagrpadmins
                  list of group administrators

## [](#SEE_ALSO)SEE ALSO

           warnquota(8).

## [](#COLOPHON)COLOPHON

           This page is part of the quota (Linux Diskquota Tools) project.
           Information about the project can be found at [unknown -- if you
           know, please contact man-pages@man7.org] It is not known how to
           report bugs for this man page; if you know, please send a mail to
           man-pages@man7.org.  This page was obtained from the project's
           upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/quota/quota-tools.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2025-12-11.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                                            QUOTAGRPADMINS(5)

------------------------------------------------------------------------

Pages that refer to this page: [warnquota(8)](../man8/warnquota.8.html)

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
