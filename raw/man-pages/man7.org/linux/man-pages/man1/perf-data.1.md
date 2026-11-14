---
{"title": "perf-data(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/perf-data.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# perf-data(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS FOR CONVERT](#OPTIONS_FOR_CONVERT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                 |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PERF-DATA(1)                   perf Manual                   PERF-DATA(1)

## [](#NAME)NAME

           perf-data - Data file related processing

## [](#SYNOPSIS)SYNOPSIS

           perf data [<common options>] <command> [<options>]",

## [](#DESCRIPTION)DESCRIPTION

           Data file related processing.

## [](#COMMANDS)COMMANDS

           convert
               Converts perf data file into another format. It’s possible to
               set data-convert debug variable to get debug messages from
               conversion, like: perf --debug data-convert data convert ...

## [](#OPTIONS_FOR_CONVERT)OPTIONS FOR CONVERT

           --to-ctf
               Triggers the CTF conversion, specify the path of CTF data
               directory.

           --to-json
               Triggers JSON conversion. Specify the JSON filename to output.

           --tod
               Convert time to wall clock time.

           -i
               Specify input perf data file path.

           -f, --force
               Don’t complain, do it.

           --time
               Only convert samples within given time window: <start>,<stop>.
               Times have the format seconds.nanoseconds. If start is not
               given (i.e. time string is ,x.y) then analysis starts at the
               beginning of the file. If stop time is not given (i.e. time
               string is x.y,) then analysis goes to end of file. Multiple
               ranges can be separated by spaces, which requires the argument
               to be quoted e.g. --time "1234.567,1234.789 1235,"

                   Also support time percent with multiple time ranges. Time string is
                   'a%/n,b%/m,...' or 'a%-b%,c%-%d,...'.

                   For example:
                   Select the second 10% time slice:

                   perf data convert --to-json out.json --time 10%/2

                   Select from 0% to 10% time slice:

                   perf data convert --to-json out.json --time 0%-10%

                   Select the first and second 10% time slices:

                   perf data convert --to-json out.json --time 10%/1,10%/2

                   Select from 0% to 10% and 30% to 40% slices:

                   perf data convert --to-json out.json --time 0%-10%,30%-40%

           -v, --verbose
               Be more verbose (show counter open errors, etc).

           --all
               Convert all events, including non-sample events (comm, fork,
               ...), to output. Default is off, only convert samples.

## [](#SEE_ALSO)SEE ALSO

           perf(1) [1] Common Trace Format - http://www.efficios.com/ctf 

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

    perf                            2026-01-06                   PERF-DATA(1)

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
