---
{"title": "lxc-top(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lxc-top.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lxc-top(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lxc-top(1)                                                     lxc-top(1)

## [](#NAME)NAME

           lxc-top - monitor container statistics

## [](#SYNOPSIS)SYNOPSIS

           lxc-top [--help] [--delay delay] [--sort sortby] [--reverse]

## [](#DESCRIPTION)DESCRIPTION

           lxc-top displays container statistics. The output is updated every
           delay seconds, and is ordered according to the sortby value given.
           lxc-top  will display as many containers as can fit in your termi‐
           nal. Press 'q' to quit. Press one of the sort key letters to  sort
           by  that  statistic.  Pressing a sort key letter a second time re‐
           verses the sort order.

## [](#OPTIONS)OPTIONS

           -d, --delay delay
                  Amount of time in seconds to delay between screen updates.
                  The default is 3 seconds.

           -s, --sort sortby
                  Sort the containers by name, cpu use, or memory use. The
                  sortby argument should be one of the letters n,c,b,m,k to
                  sort by name, cpu use, block I/O, memory, or kernel memory
                  use respectively. The default is 'n'.

           -r, --reverse
                  Reverse the default sort order. By default, names sort in
                  ascending alphabetical order and values sort in descending
                  amounts (ie. largest value first).

## [](#EXAMPLE)EXAMPLE

           lxc-top --delay 1 --sort m
                  Display containers, updating every second, sorted by memory
                  use.

## [](#NOTES)NOTES

           For performance reasons the kernel does not account kernel memory
           use unless a kernel memory limit is set. If a limit is not set,
           lxc-top will display kernel memory use as 0. If no containers are
           being accounted, the KMem column will not be displayed. A limit
           can be set by specifying

                 lxc.cgroup.memory.kmem.limit_in_bytes = number

           in your container configuration file, see lxc.conf(5).

## [](#SEE_ALSO)SEE ALSO

           lxc(7), lxc-create(1), lxc-copy(1), lxc-destroy(1), lxc-start(1),
           lxc-stop(1), lxc-execute(1), lxc-console(1), lxc-monitor(1),
           lxc-wait(1), lxc-cgroup(1), lxc-ls(1), lxc-info(1), lxc-freeze(1),
           lxc-unfreeze(1), lxc-attach(1), lxc.conf(5)

## [](#COLOPHON)COLOPHON

           This page is part of the lxc (Linux containers) project.  Informa‐
           tion about the project can be found at 
           ⟨http://linuxcontainers.org/⟩.  If you have a bug report for this
           manual page, send it to lxc-devel@lists.linuxcontainers.org.  This
           page was obtained from the project's upstream Git repository
           ⟨https://github.com/lxc/lxc.git⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-07-23.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                    2026-04-29                     lxc-top(1)

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
