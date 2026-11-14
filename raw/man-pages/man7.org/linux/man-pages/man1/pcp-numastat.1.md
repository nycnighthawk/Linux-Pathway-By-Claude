---
{"title": "pcp-numastat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-numastat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-numastat(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-NUMASTAT(1)          General Commands Manual          PCP-NUMASTAT(1)

## [](#NAME)NAME

           pcp-numastat - report on NUMA memory allocation

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options] numastat [-mnV?] [-w width] [-p [process ...]]

## [](#DESCRIPTION)DESCRIPTION

           pcp-numastat displays NUMA allocation statistics from the kernel
           memory allocator.  Each process has NUMA policies that specify on
           which node pages are allocated.  The performance counters in the
           kernel track on which nodes memory is allocated and these values
           are sampled and reported by pcp-numastat.

           Counters are maintained individually for each NUMA node.  Details
           of the semantics of each reported metric can be retrieved using
           the following command:

                # pminfo ‐dt mem.numa.alloc

## [](#OPTIONS)OPTIONS

           When invoked via the pcp(1) command, the -h/--host, -a/--archive,
           -O/--origin, -Z/--timezone and several other pcp options become
           indirectly available; refer to PCPIntro(1) for a complete
           description of these options.

           The additional command line options available for pcp-numastat
           are:

           -m, --meminfo
                Display meminfo-like system-wide memory usage.

           -n, --numastat
                Display the numastat statistics info.

           -p, --process
                Display per-process NUMA memory usage from proc.numa_maps
                metrics.  Any trailing process operands are treated as
                process IDs (when the operand is all digits) or regular
                expressions for command name matching.  Matching for command
                names is performed against the full command line (as reported
                by proc.psinfo.psargs).  When a single process ID operand is
                provided and it matches exactly one process, a detailed table
                of Hugepage, Heap, Stack and Private mappings is shown (as in
                numastat -p). When multiple process ID operands are provided,
                a per-process summary table is shown (also like numastat -p)
                and may be split into multiple node column blocks based on
                the available display width.

           In the per-process view, node columns are always shown for all
           NUMA nodes present on the system (as reported by PCP NUMA
           inventory metrics), even if individual proc.numa_maps metric
           instances omit some nodes. Missing per-process metrics are
           reported as zero.

           -V, --version
                  Display the current version of the command.

           -w width, --width=width
                  Limit display to width.

           -?, --help
                  Display usage message and exit.

## [](#NOTES)NOTES

           pcp-numastat is inspired by the numastat(1) command and produces
           the same output for the system-wide views. The per-process view
           (-p) follows the numastat -p layout.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pcp(1) and numastat(1).

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

    Performance Co-Pilot               PCP                    PCP-NUMASTAT(1)

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
