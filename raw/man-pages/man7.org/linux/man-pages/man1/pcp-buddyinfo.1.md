---
{"title": "pcp-buddyinfo(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-buddyinfo.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-buddyinfo(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-BUDDYINFO(1)         General Commands Manual         PCP-BUDDYINFO(1)

## [](#NAME)NAME

           pcp-buddyinfo - report Linux kernel buddy algorithm statistics

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options] buddyinfo [-uVz?]  [-s samples] [-a archive] [-Z
           timezone]

## [](#DESCRIPTION)DESCRIPTION

           The pcp-buddyinfo command is used for viewing different stats
           related to buddyinfo.  It helps users analyze the dynamic
           behaviour of the buddy algorithm used in the Linux kernel virtual
           memory subsystem.  The information includes the total number of
           zones that are currently active, counts of different order pages,
           and so on.  By default, pcp-buddyinfo reports live data for the
           local host.

           The statistics shown are as follows:

           HEADER          DESCRIPTION
           _               _
           Normal          zones available
           Nodes           available nodes
           Order0          available pages of order 0
           Order1          available pages of order 1
           Order2          available pages of order 2
           Order3          available pages of order 3
           Order4          available pages of order 4
           Order5          available pages of order 5
           Order6          available pages of order 6
           Order7          available pages of order 7
           Order8          available pages of order 8
           Order9          available pages of order 9
           Order10         available pages of order 10

           Each column represents the number of pages of a certain order (a
           certain size) that are available at any given time. For example,
           for zone DMA (direct memory access), there are 90 of
           2^(0*PAGE_SIZE) chunks of memory. Similarly, there are 6 of
           2^(1*PAGE_SIZE) chunks, and 2 of 2^(2*PAGE_SIZE) chunks of memory
           available.

           The DMA row references the first 16 MB on a system, the HighMem
           row references all memory greater than 4 GB on a system, and the
           Normal row references all memory in between.

## [](#OPTIONS)OPTIONS

           -a file, --archive=file
                  Fetch buddyinfo metrics from the specified PCP archive.

           -s count, --samples=count
                  Limit reporting to count samples of buddyinfo statistics.

           -u, --no-interpol
                  disable the default interpolation mode when replaying an
                  archive.  With the -u option, interpolated reporting is
                  disabled and each sample is reported according to native
                  sampling intervals in the archive.  In this mode the -t
                  option is ignored.  Additionally, non-interpolated replay
                  makes sense only when replaying an archive (using the -a
                  option described above), so the -a option is mandatory when
                  -u is specified.

           -z, --hostzone
                  Use the local timezone of the host that is the source of
                  the performance metrics, as identified by either the -h or
                  the -a options.  The default is to use the timezone of the
                  local host.

           -Z timezone, --timezone=timezone
                  Use timezone for the date and time.  Timezone is in the
                  format of the environment variable TZ as described in
                  environ(7).

           -V, --version
                  Display version number and exit.

           -?, --help
                  Display usage message and exit.

## [](#NOTES)NOTES

           pcp-buddyinfo reports information extracted from the
           /proc/buddyinfo Linux kernel procfs file.

           If the default interpolation mode is disabled, it is possible that
           some metrics (recorded at different intervals) will be reported as
           having missing values for some samples even if they were recorded.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP. On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables. The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pcp(1), pmGetOptions(3), pcp.conf(5) and environ(7).

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

    Performance Co-Pilot               PCP                   PCP-BUDDYINFO(1)

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
