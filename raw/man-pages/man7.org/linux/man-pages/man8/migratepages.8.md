---
{"title": "migratepages(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/migratepages.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# migratepages(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [FILES](#FILES) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MIGRATEPAGES(8)        Linux Administrator's Manual       MIGRATEPAGES(8)

## [](#NAME)NAME

           migratepages - Migrate the physical location a processes pages

## [](#SYNOPSIS)SYNOPSIS

           migratepages pid from-nodes to-nodes

## [](#DESCRIPTION)DESCRIPTION

           migratepages moves the physical location of a processes pages
           without any changes of the virtual address space of the process.
           Moving the pages allows one to change the distances of a process
           to its memory. Performance may be optimized by moving a processes
           pages to the node where it is executing.

           If multiple nodes are specified for from-nodes or to-nodes then an
           attempt is made to preserve the relative location of each page in
           each nodeset.

           For example if we move from nodes 2-5 to 7,9,12-13 then the
           preferred mode of operation is to move pages from 2->7, 3->9,
           4->12 and 5->13. However, this is only posssible if enough memory
           is available.

           Valid node specifiers
                  all                 All nodes
                  number              Node number
                  number1{,number2}   Node number1 and Node number2
                  number1-number2     Nodes from number1 to number2
                  ! nodes             Invert selection of the following specification.

## [](#NOTES)NOTES

           Requires a NUMA policy aware kernel with support for page
           migration (linux 2.6.16 and later).

           migratepages will only move pages that are not shared with other
           processes if called by a user without administrative priviledges
           (but with the right to modify the process).

           migratepages will move all pages if invoked from root (or a user
           with administrative priviledges).

## [](#FILES)FILES

           /proc/<pid>/numa_maps for information about the NUMA memory use of
           a process.

## [](#COPYRIGHT)COPYRIGHT

           Copyright 2005-2006 Christoph Lameter, Silicon Graphics, Inc.
           migratepages is under the GNU General Public License, v.2

## [](#SEE_ALSO)SEE ALSO

           numactl(8) , set_mempolicy(2) , get_mempolicy(2) , mbind(2) ,
           sched_setaffinity(2) , sched_getaffinity(2) , proc(5) , ftok(3) ,
           shmat(2) , taskset(1)

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

    SGI                              Jan 2005                 MIGRATEPAGES(8)

------------------------------------------------------------------------

Pages that refer to this page: [migrate_pages(2)](../man2/migrate_pages.2.html),  [move_pages(2)](../man2/move_pages.2.html),  [cpuset(7)](../man7/cpuset.7.html),  [numactl(8)](../man8/numactl.8.html)

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
