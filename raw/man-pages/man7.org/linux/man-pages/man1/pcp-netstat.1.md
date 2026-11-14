---
{"title": "pcp-netstat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-netstat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-netstat(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-NETSTAT(1)           General Commands Manual           PCP-NETSTAT(1)

## [](#NAME)NAME

           pcp-netstat - Report statistics for different network protocols
           and network interfaces.

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options] netstat [--statistics] [-p [TCP|IP|UDP|ICMP]]
           [-i] [-s samples] [-a archive] [-S start_time] [-T end_time]

## [](#DESCRIPTION)DESCRIPTION

           The pcp-netstat command is used for viewing the different kinds of
           statistics related to the network protocols and the network
           interfaces. This tool is useful for checking the status of your
           network interfaces, network connections and for troubleshooting
           network issues.  This tool can also be used to analyze network
           statistics for all available protocols, including TCP, UDP, ICMP,
           and IP protocols.

           By default pcp-netstat reports live data for the local host. It
           has the capabilities to analyze the data on the archives as well.

## [](#OPTIONS)OPTIONS

           --statistics
                  shows output similar to netstat -s, which displays summary
                  statistics for each protocol

           -i     shows output similar to netstat -i -a -n, which displays a
                  table of all network interfaces

           -p, --TCP|IP|UDP|ICMP
                  filter network statistics specific to a protocol

           -a file, --archive=file
                  Fetch /proc/netstat for a specified archive file

           -s count, --samples=count
                  Get the network statistics for specified number of samples
                  count

           -S, --start=time
                  Filter the samples from the archive from the given time

           -T, --finish=time
                  Filter the samples from the archive until the given time

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

    Performance Co-Pilot               PCP                     PCP-NETSTAT(1)

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
