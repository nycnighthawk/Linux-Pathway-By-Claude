---
{"title": "pcp-xsos(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-xsos.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-xsos(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-XSOS(1)              General Commands Manual              PCP-XSOS(1)

## [](#NAME)NAME

           pcp-xsos - high-level summary reports for a system

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options] xsos [--all] [-dmnNopx] [-u units]

## [](#DESCRIPTION)DESCRIPTION

           pcp-xsos gives a summary report of a system using either a PCP
           archive or live metric values from that system.

           It is designed to be fast and performs a single-sample only,
           similar to tools like ps(1).  Thus, level of detail in reporting
           is traded off in favour of execution speed.  pcp-xsos is designed
           as an initial performance triage tool that quickly informs an
           operator as to avenues of investigation that may prove more
           fruitful.  At this time the focus is entirely on operating system
           metrics, however this is not a requirement and in time it may be
           extended to report on any performance domain with associated PCP
           metrics.

           When invoked via the pcp(1) command, the -h/--host, -a/--archive,
           -O/--origin pcp options become indirectly available, see
           PCPIntro(1) for their descriptions.

           The default report with no command line options presented is the
           operating system overview.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           --all
                iteratively report each subsection, one after the other.

           -o, --os
                display the default report with high level kernel
                information, including version, uptime, number of users,
                process states and aggregated processor utilisation.

           -d, --disks
                Report storage information from the archive or live host,
                including the total capacity for each block device as well as
                available filesystem space for each mounted filesystem.

           -m, --memory
                Detailed memory report, including percentage of total memory
                used for various operating system functions, swap use, and
                optionally hugepages and virtual machine balloon information.

           -n, --netdev
                Statistics for each configured network interface, including
                packet and byte transfer rates (since boot), errors, drops,
                and so on.  Additionally, socket statistics are also reported
                with this command line option, for raw, UDP and TCP (IPv4 and
                IPv6).

           -N, --netstats
                Report aggregate network statistics such as various ICMP and
                TCP error and timeout counters.

           -p, --ps
                Inspect running processes in a style similar to ps.  These
                are grouped and filtered to show the most important processes
                in terms of resource use (CPU, memory) as well as processes
                in zombie or blocked states.

           -u unit, --units=unit
                Change the byte display for various reports.  Valid values
                for unit are "b" (bytes), "k" (kibibytes), "m" (mibibytes),
                "g" (gibibytes) or "t" (tebibytes).

           -x, --nocolor
                Display reports without using colors to highlight various
                aspects of each subsystem.

           -?, --help
                Display usage message and exit.

## [](#NOTES)NOTES

           pcp-xsos is inspired by the xsos utility, aims to be command line
           compatible with it where possible and also provide a consistent
           output style.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see pmGetOptions(3)
           which provides pmgetopt(1) functionality used by pcp-xsos.

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pcp(1), ps(1), pmgetopt(1), pmGetOptions(3) and
           environ(7).

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

    Performance Co-Pilot               PCP                        PCP-XSOS(1)

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
