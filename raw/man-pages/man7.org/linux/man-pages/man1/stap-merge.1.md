---
{"title": "stap-merge(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stap-merge.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stap-merge(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STAP-MERGE(1)            General Commands Manual            STAP-MERGE(1)

## [](#NAME)NAME

           stap-merge - systemtap per-cpu binary merger

## [](#SYNOPSIS)SYNOPSIS

           stap-merge [ OPTIONS ] [ INPUT FILENAMES ]

## [](#DESCRIPTION)DESCRIPTION

           The stap-merge executable applies when the -b option has been used
           while running a stap script.  The -b option will generate files
           per-cpu, based on the timestamp field. Then stap-merge will merge
           and sort through the per-cpu files based on the timestamp field.

## [](#OPTIONS)OPTIONS

           The systemtap merge executable supports the following options.

           -v     Verbose mode, displays three extra fields per set of
                  collected data.

                  [cpunumber,sequencenumberofdata,thelengthofthedataset]

           -o OUTPUT_FILENAME

                  Specify the name of the file you would like the output to
                  be redirected into.  If this option is not specified than
                  the output will be pushed to standard out.

## [](#EXAMPLES)EXAMPLES

                  $ stap -v -b -e 'probe syscall.open { printf("%s(%d) open\n",
                  execname(), pid()) }'

           This should result in several stpd_cpu files (each labled with a
           number representing which cpu the file was produced from).

                  $ stap-merge -v stpd_cpu0 stpd_cpu1

           Running the stap-merge program in the same directory as the stap
           script earlier in the example, will produce an ordered sequence of
           packets with the three part label for each set of data.  This re‐
           sult will be pushed through the standard output.  An output file
           could have been specified using the "-o" option.

## [](#FILES)FILES

           Important files and their corresponding paths can be located in
           the
                  stappaths (7) manual page.

## [](#SEE_ALSO)SEE ALSO

           stapprobes(3stap),
           stappaths(7),
           staprun(8),
           stapvars(3stap),
           stapex(3stap),
           stap-server(8),
           gdb(1)

## [](#BUGS)BUGS

           Use the Bugzilla link of the project web page or our mailing list.
           http://sourceware.org/systemtap/ ,<systemtap@sourceware.org>.

## [](#COLOPHON)COLOPHON

           This page is part of the systemtap (a tracing and live-system
           analysis tool) project.  Information about the project can be
           found at ⟨https://sourceware.org/systemtap/⟩.  If you have a bug
           report for this manual page, send it to systemtap@sourceware.org.
           This page was obtained from the project's upstream Git repository
           ⟨git://sourceware.org/git/systemtap.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                                                STAP-MERGE(1)

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
