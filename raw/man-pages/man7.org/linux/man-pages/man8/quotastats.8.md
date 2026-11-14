---
{"title": "quotastats(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/quotastats.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# quotastats(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    QUOTASTATS(8)                     quota                     QUOTASTATS(8)

## [](#NAME)NAME

           quotastats - Program to query quota statistics

## [](#SYNOPSIS)SYNOPSIS

           /usr/sbin/quotastats

## [](#DESCRIPTION)DESCRIPTION

           quotastats queries the kernel for quota statistics.  It displays:

               •      Supported kernel quota version
               •      Number of dquot lookups
               •      Number of dquot drops
               •      Number of dquot reads
               •      Number of dquot writes
               •      Number of quotafile syncs
               •      Number of dquot cache hits
               •      Number of allocated dquots
               •      Number of free dquots
               •      Number of in use dquot entries (user/group)

## [](#OPTIONS)OPTIONS

           None.

## [](#SEE_ALSO)SEE ALSO

           quota(1).

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

                                  April 2, 2004                 QUOTASTATS(8)

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
