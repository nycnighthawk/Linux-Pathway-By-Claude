---
{"title": "pcp-rocestat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-rocestat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-rocestat(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-ROCESTAT(1)          General Commands Manual          PCP-ROCESTAT(1)

## [](#NAME)NAME

           pcp-rocestat - Reports statistics for nVidia RoCE devices.

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options] rocestat [--hw_stats|--lane_stats]

## [](#DESCRIPTION)DESCRIPTION

           The pcp-rocestat tool utilizes ethtool counters for each device
           and reports throughput per priority queue.  By default pcp-
           rocestat reports live data for the local host.  It has the ability
           to analyze data from PDP archives as well.

## [](#OPTIONS)OPTIONS

           --hw_stats
                  Display hardware counters.

           --lane_stats
                  Display lane statistics.

           -a archive, --archive=archive
                  Specify the PCP archive to examine.

           -s samples, --samples=samples
                  Specify number of samples to report.

           -S starttime, --start=starttime
                  Report the samples from the archive from the given time.

           -T endtime, --finish=endtime
                  Report samples from the archive until the given time.

           -V, --version
                  Display version number and exit.

           -?, --help
                  Display usage message and exit.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pcp(1), pmParseInterval(3) and environ(7).

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

    Performance Co-Pilot               PCP                    PCP-ROCESTAT(1)

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
