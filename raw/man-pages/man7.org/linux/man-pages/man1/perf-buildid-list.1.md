---
{"title": "perf-buildid-list(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/perf-buildid-list.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# perf-buildid-list(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PERF-BUILDID-LIST(1)           perf Manual           PERF-BUILDID-LIST(1)

## [](#NAME)NAME

           perf-buildid-list - List the buildids in a perf.data file

## [](#SYNOPSIS)SYNOPSIS

           perf buildid-list <options>

## [](#DESCRIPTION)DESCRIPTION

           This command displays the buildids found in a perf.data file, so
           that other tools can be used to fetch packages with matching
           symbol tables for use by perf report.

           It can also be used to show the build id of the running kernel or
           in an ELF file using -i/--input.

## [](#OPTIONS)OPTIONS

           -H, --with-hits
               Show only DSOs with hits.

           -i, --input=
               Input file name. (default: perf.data unless stdin is a fifo)

           -f, --force
               Don’t do ownership validation.

           -k, --kernel
               Show running kernel build id.

           -m, --kernel-maps
               Show buildid, start/end text address, and path of running
               kernel and its modules.

           -v, --verbose
               Be more verbose.

## [](#SEE_ALSO)SEE ALSO

           perf-record(1), perf-top(1), perf-report(1)

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

    perf                            2022-07-18           PERF-BUILDID-LIST(1)

------------------------------------------------------------------------

Pages that refer to this page: [perf(1)](../man1/perf.1.html),  [perf-archive(1)](../man1/perf-archive.1.html),  [perf-buildid-cache(1)](../man1/perf-buildid-cache.1.html),  [perf-kvm(1)](../man1/perf-kvm.1.html)

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
