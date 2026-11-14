---
{"title": "migspeed(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/migspeed.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# migspeed(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MIGSPEED(8)            Linux Administrator's Manual           MIGSPEED(8)

## [](#NAME)NAME

           migspeed - Test the speed of page migration

## [](#SYNOPSIS)SYNOPSIS

           migspeed -p pages from-nodes to-nodes

## [](#DESCRIPTION)DESCRIPTION

           migspeed attempts to move a sample of pages from the indicated
           node to the target node and measures the time it takes to perform
           the move.

           -p pages

           The default sample is 1000 pages. Override that with another
           number.

## [](#NOTES)NOTES

           Requires a NUMA policy aware kernel with support for page
           migration (Linux 2.6.16 and later).

## [](#COPYRIGHT)COPYRIGHT

           Copyright 2007 Christoph Lameter, Silicon Graphics, Inc.
           migratepages is under the GNU General Public License, v.2

## [](#SEE_ALSO)SEE ALSO

           numactl(8)

## [](#COLOPHON)COLOPHON

           This page is part of the numactl (NUMA commands) project.
           Information about the project can be found at 
           ⟨http://oss.sgi.com/projects/libnuma/⟩.  If you have a bug report
           for this manual page, send it to linux-numa@vger.kernel.org.  This
           page was obtained from the project's upstream Git repository
           ⟨https://github.com/numactl/numactl.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    SGI                             April 2005                    MIGSPEED(8)

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
