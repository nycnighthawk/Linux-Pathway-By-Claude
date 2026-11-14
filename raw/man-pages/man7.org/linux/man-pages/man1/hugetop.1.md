---
{"title": "hugetop(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/hugetop.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# hugetop(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [STANDARDS](#STANDARDS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                    |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    HUGETOP(1)               General Commands Manual               HUGETOP(1)

## [](#NAME)NAME

           hugetop - report huge page information

## [](#SYNOPSIS)SYNOPSIS

           hugetop [option ...]

## [](#DESCRIPTION)DESCRIPTION

           The hugetop command reports the huge page information of system
           and processes. It displays a summary of the system huge page
           status. For each process that has at least one huge page, the
           number of private and shared pages, along with the process PID and
           command name are displayed.

## [](#OPTIONS)OPTIONS

           -d, --delay=N
                  Refresh the display every n in seconds.  By default,
                  hugetop refreshes the display every three seconds.  To exit
                  the program, hit q.  This cannot be combined with the -o
                  option.

           -n, --numa
                  Display per NUMA node huge page information.

           -o, --once
                  Display the output once and then exit.

           -H, --human
                  Display human-readable output.

           -h, --help
                  Display help text and exit.

           -V, --version
                  Display version information and exit.

## [](#EXIT_STATUS)EXIT STATUS

           0      Success.

           Others Errno.

## [](#AUTHOR)AUTHOR

           zhenwei pi <pizhenwei@bytedance.com>

## [](#SEE_ALSO)SEE ALSO

           pmap(1)

## [](#STANDARDS)STANDARDS

           No standards apply.

## [](#REPORTING_BUGS)REPORTING BUGS

           Please send bug reports to ⟨procps@freelists.org⟩.

## [](#COLOPHON)COLOPHON

           This page is part of the procps-ng (/proc filesystem utilities)
           project.  Information about the project can be found at 
           ⟨https://gitlab.com/procps-ng/procps⟩.  If you have a bug report
           for this manual page, see
           ⟨https://gitlab.com/procps-ng/procps/blob/master/Documentation/bugs.md⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://gitlab.com/procps-ng/procps.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    procps-ng                       2024-01-18                     HUGETOP(1)

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
