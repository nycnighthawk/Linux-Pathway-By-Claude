---
{"title": "perf-help(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/perf-help.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# perf-help(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PERF](#PERF) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PERF-HELP(1)                   perf Manual                   PERF-HELP(1)

## [](#NAME)NAME

           perf-help - display help information about perf

## [](#SYNOPSIS)SYNOPSIS

           perf help [-a|--all] [COMMAND]

## [](#DESCRIPTION)DESCRIPTION

           With no options and no COMMAND given, the synopsis of the perf
           command and a list of the most commonly used perf commands are
           printed on the standard output.

           If the option --all or -a is given, then all available commands
           are printed on the standard output.

           If a perf command is named, a manual page for that command is
           brought up. The man program is used by default for this purpose,
           but this can be overridden by other options or configuration
           variables.

           Note that perf --help ... is identical to perf help ... because
           the former is internally converted into the latter.

## [](#OPTIONS)OPTIONS

           -a, --all
               Prints all the available commands on the standard output. This
               option supersedes any other option.

## [](#PERF)PERF

           Part of the perf(1) suite

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

    perf                            2009-06-06                   PERF-HELP(1)

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
