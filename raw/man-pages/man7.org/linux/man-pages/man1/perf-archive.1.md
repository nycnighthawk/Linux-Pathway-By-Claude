---
{"title": "perf-archive(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/perf-archive.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# perf-archive(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PERF-ARCHIVE(1)                perf Manual                PERF-ARCHIVE(1)

## [](#NAME)NAME

           perf-archive - Create archive with object files with build-ids
           found in perf.data file

## [](#SYNOPSIS)SYNOPSIS

           perf archive [file]

## [](#DESCRIPTION)DESCRIPTION

           This command runs perf-buildid-list --with-hits, and collects the
           files with the buildids found so that analysis of perf.data
           contents can be possible on another machine.

## [](#SEE_ALSO)SEE ALSO

           perf-record(1), perf-buildid-list(1), perf-report(1)

## [](#COLOPHON)COLOPHON

           This page is part of the perf (Performance analysis tools for
           Linux (in Linux source tree)) project.  Information about the
           project can be found at 
           ⟨https://perf.wiki.kernel.org/index.php/Main_Page⟩.  If you have a
           bug report for this manual page, send it to
           linux-kernel@vger.kernel.org.  This page was obtained from the
           project's upstream Git repository
           ⟨http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git⟩
           on 2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-08-03.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    perf                            2013-12-09                PERF-ARCHIVE(1)

------------------------------------------------------------------------

Pages that refer to this page: [perf(1)](../man1/perf.1.html),  [perf-inject(1)](../man1/perf-inject.1.html)

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
