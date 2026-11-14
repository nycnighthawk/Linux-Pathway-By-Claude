---
{"title": "pcp-free(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-free.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-free(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-FREE(1)              General Commands Manual              PCP-FREE(1)

## [](#NAME)NAME

           pcp-free - report on free and used memory in the system

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options] free [-bkmgroltVw?]  [-c count] [-s interval]

## [](#DESCRIPTION)DESCRIPTION

           pcp-free gives a summary display of the total amount of free and
           used physical memory and swap in the system, as well as the caches
           used by the kernel.

           When invoked via the pcp(1) command, the -h/--host, -a/--archive,
           -O/--origin, -s/--samples, -t/--interval, -Z/--timezone and
           several other pcp options become indirectly available, see
           PCPIntro(1) for their descriptions.

           The displayed columns are:

           total  Total installed memory (MemTotal and SwapTotal in
                  /proc/meminfo)

           used   Used memory (calculated as total - free - buffers - cache)

           free   Unused memory (MemFree and SwapFree in /proc/meminfo)

           shared Memory used (mostly) by tmpfs (Shmem in /proc/meminfo)

           buffers
                  Memory used by kernel buffers (Buffers in /proc/meminfo)

           cache  Memory used by the page cache and slabs (Cached and
                  SReclaimable in /proc/meminfo)

           buff/cache
                  Sum of buffers and cache

           available
                  Estimation of how much memory is available for starting new
                  applications, without swapping.  Unlike the data provided
                  by the cache or free fields, this field takes into account
                  page cache and also that not all reclaimable memory slabs
                  will be reclaimed due to items being in use (MemAvailable
                  in /proc/meminfo).

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -b, --bytes
                Display the amount of memory in bytes.

           -c count, --samples=count, --count=count
                Terminate the display after count iterations.  See also -s.

           -g, --gigabytes
                Display the amount of memory in gigabytes.

           -k, --kilobytes
                Display the amount of memory in kilobytes.  This is the
                default.

           -l, --lohi
                Display detailed low and high memory statistics.

           -m, --megabytes
                Display the amount of memory in megabytes.

           -o   Disable the display of a "buffer adjusted" line.  If the -o
                option is not specified, free subtracts buffer memory from
                the used memory and adds it to the free memory reported.

           -r, --terabytes
                Display the amount of memory in terabytes.

           -s delay, --interval=delay, --seconds=delay
                Activate continuous polling delay seconds apart.  You may
                specify any floating point number for delay, or indeed any
                valid pmParseInterval(3) specification, which includes
                microsecond resolution delay times.  This can be used in
                conjunction with the -c option.

           -t, --total
                Display a line containing the totals.

           -V, --version
                Display version number and exit.

           -w, --wide
                Switch to the wide mode.  The wide mode produces lines longer
                than 80 characters.  In this mode buffers and cache are
                reported in two separate columns.

           -?, --help
                Display usage message and exit.

## [](#NOTES)NOTES

           pcp-free is inspired by the free(1) command and aims to be command
           line and output compatible with it.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pcp(1), free(1), pmParseInterval(3) and environ(7).

## [](#COLOPHON)COLOPHON

           This page is part of the PCP (Performance Co-Pilot) project.
           Information about the project can be found at 
           ⟨http://www.pcp.io/⟩.  If you have a bug report for this manual
           page, send it to pcp@groups.io.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/performancecopilot/pcp.git⟩ on 2026-08-04.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-08-04.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Performance Co-Pilot               PCP                        PCP-FREE(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcp(1)](../man1/pcp.1.html)

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
