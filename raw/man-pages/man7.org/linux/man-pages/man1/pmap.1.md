---
{"title": "pmap(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmap.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmap(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [STANDARDS](#STANDARDS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                               |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMAP(1)                  General Commands Manual                  PMAP(1)

## [](#NAME)NAME

           pmap - report memory map of a process

## [](#SYNOPSIS)SYNOPSIS

           pmap [option ...] pid ...

## [](#DESCRIPTION)DESCRIPTION

           The pmap command reports the memory map of a process or processes.

## [](#OPTIONS)OPTIONS

           -x, --extended
                  Show the extended format.

           -d, --device
                  Show the device format.

           -q, --quiet
                  Do not display some header or footer lines.

           -A, --range low[,high]
                  Limit results to the given range to low and high address
                  range.  Notice that the low and high arguments are single
                  string separated with comma. high can be omitted.

           -X     Show even more details than the -x option. WARNING: format
                  changes according to /proc/PID/smaps

           -XX    Show everything the kernel provides

           -p, --show-path
                  Show full path to files in the mapping column

           -k, --use-kernel-name
                  If available, use names provided by the kernel instead of
                  "[ anon ]"

           -c, --read-rc
                  Read the default configuration

           -C, --read-rc-from file
                  Read the configuration from file

           -n, --create-rc
                  Create new default configuration

           -N, --create-rc-to file
                  Create new configuration to file

           -h, --help
                  Display help text and exit.

           -V, --version
                  Display version information and exit.

## [](#EXIT_STATUS)EXIT STATUS

           0      Success.

           1      Failure.

           42     Did not find all processes asked for.

## [](#SEE_ALSO)SEE ALSO

           ps(1), pgrep(1)

## [](#STANDARDS)STANDARDS

           No standards apply, but pmap looks an awful lot like a SunOS
           command.

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

    procps-ng                       2020-06-04                        PMAP(1)

------------------------------------------------------------------------

Pages that refer to this page: [hugetop(1)](../man1/hugetop.1.html),  [proc_pid_smaps(5)](../man5/proc_pid_smaps.5.html)

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
