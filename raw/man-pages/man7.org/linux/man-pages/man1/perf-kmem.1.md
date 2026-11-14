---
{"title": "perf-kmem(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/perf-kmem.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# perf-kmem(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PERF-KMEM(1)                   perf Manual                   PERF-KMEM(1)

## [](#NAME)NAME

           perf-kmem - Tool to trace/measure kernel memory properties

## [](#SYNOPSIS)SYNOPSIS

           perf kmem [<options>] {record|stat}

## [](#DESCRIPTION)DESCRIPTION

           There are two variants of perf kmem:

               'perf kmem [<options>] record [<perf-record-options>] <command>' to
               record the kmem events of an arbitrary workload. Additional 'perf
               record' options may be specified after record, such as '-o' to
               change the output file name.

               'perf kmem [<options>] stat' to report kernel memory statistics.

## [](#OPTIONS)OPTIONS

           -i <file>, --input=<file>
               For stat, select the input file (default: perf.data unless
               stdin is a fifo)

           -f, --force
               Don’t do ownership validation

           -v, --verbose
               Be more verbose. (show symbol address, etc)

           --caller
               Show per-callsite statistics

           --alloc
               Show per-allocation statistics

           -s <key[,key2...]>, --sort=<key[,key2...]>
               Sort the output (default: frag,hit,bytes for slab and
               bytes,hit for page). Available sort keys are ptr, callsite,
               bytes, hit, pingpong, frag for slab and page, callsite, bytes,
               hit, order, migtype, gfp for page. This option should be
               preceded by one of the mode selection options - i.e. --slab,
               --page, --alloc and/or --caller.

           -l <num>, --line=<num>
               Print n lines only

           --raw-ip
               Print raw ip instead of symbol

           --slab
               Analyze SLAB allocator events.

           --page
               Analyze page allocator events

           --live
               Show live page stat. The perf kmem shows total allocation stat
               by default, but this option shows live (currently allocated)
               pages instead. (This option works with --page option only)

           --time=<start>,<stop>
               Only analyze samples within given time window: <start>,<stop>.
               Times have the format seconds.microseconds. If start is not
               given (i.e., time string is ,x.y) then analysis starts at the
               beginning of the file. If stop time is not given (i.e, time
               string is x.y,) then analysis goes to end of file.

## [](#SEE_ALSO)SEE ALSO

           perf-record(1)

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

    perf                            2021-10-08                   PERF-KMEM(1)

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
