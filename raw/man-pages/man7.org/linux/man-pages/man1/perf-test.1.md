---
{"title": "perf-test(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/perf-test.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# perf-test(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PERF-TEST(1)                   perf Manual                   PERF-TEST(1)

## [](#NAME)NAME

           perf-test - Runs sanity tests.

## [](#SYNOPSIS)SYNOPSIS

           perf test [<options>] [{list <test-name-fragment>|[<test-name-fragments>|<test-numbers>]}]

## [](#DESCRIPTION)DESCRIPTION

           This command does assorted sanity tests, initially through linked
           routines but also will look for a directory with more tests in the
           form of scripts.

           To get a list of available tests use perf test list, specifying a
           test name fragment will show all tests that have it.

           To run just specific tests, inform test name fragments or the
           numbers obtained from perf test list.

## [](#OPTIONS)OPTIONS

           -s, --skip
               Tests to skip (comma separated numeric list).

           -v, -vv, -vvv, --verbose
               With a single -v, verbose level 1, only failing test output is
               displayed. With -vv and higher all test output is shown.

           -S, --sequential
               Run all tests one after the other. By default "exclusive"
               tests are run sequentially, but other tests are run in
               parallel to speed execution.

           -r, --runs-per-test
               Run each test the given number of times, by default once. This
               option can be useful to determine if a test is flaky.

           -F, --dont-fork
               Do not fork child for each test, run all tests within single
               process, this sets sequential mode.

           --dso
               Specify a DSO for the "Symbols" test.

           -w, --workload=
               Run a built-in workload, to list them use --list-workloads,
               current ones include: noploop, thloop, leafloop, sqrtloop,
               brstack, datasym, context_switch_loop, deterministic,
               named_threads and landlock.

                   Used with the shell script regression tests.

                   Some accept an extra parameter:

                   seconds: leafloop, noploop, sqrtloop, thloop
                   nrloops: brstack, context_switch_loop

                   'named_threads' accepts the number of threads and the number of loops to
                   do in each thread.

                   The datasym, landlock and deterministic workloads don't accept any.

           --list-workloads
               List the available workloads to use with -w/--workload.

           --record-ctl=fifo:ctl-fifo[,ack-fifo]
               This option is used to communicate with a perf record session
               in order to control the recording scope to only the workload
               and avoid recording setup and teardown code. When specifying
               this option, the same FIFO path must be specified in the
               record session via:

                   perf record -D -1 --control=fifo:ctl-fifo[,ack-fifo] ...

                   Perf test sends 'enable' and 'disable' commands through ctl-fifo to
                   control event recording. If 'ack-fifo' is provided, the workload runner
                   waits for an 'ack' response after each command.

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

    perf                            2026-06-10                   PERF-TEST(1)

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
