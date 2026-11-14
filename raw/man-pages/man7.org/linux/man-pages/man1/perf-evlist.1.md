---
{"title": "perf-evlist(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/perf-evlist.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# perf-evlist(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PERF-EVLIST(1)                 perf Manual                 PERF-EVLIST(1)

## [](#NAME)NAME

           perf-evlist - List the event names in a perf.data file

## [](#SYNOPSIS)SYNOPSIS

           perf evlist <options>

## [](#DESCRIPTION)DESCRIPTION

           This command displays the names of events sampled in a perf.data
           file.

## [](#OPTIONS)OPTIONS

           -i, --input=
               Input file name. (default: perf.data unless stdin is a fifo)

           -f, --force
               Don’t complain, do it.

           -F, --freq=
               Show just the sample frequency used for each event.

           -v, --verbose
               Show all fields.

           -g, --group
               Show event group information.

           --trace-fields
               Show tracepoint field names.

## [](#SEE_ALSO)SEE ALSO

           perf-record(1), perf-list(1), perf-report(1)

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

    perf                            2021-03-06                 PERF-EVLIST(1)

------------------------------------------------------------------------

Pages that refer to this page: [perf(1)](../man1/perf.1.html)

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
