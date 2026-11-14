---
{"title": "pcp-nfsiostat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-nfsiostat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-nfsiostat(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OUTPUT FORMAT](#OUTPUT_FORMAT) \| [FIELD DESCRIPTIONS](#FIELD_DESCRIPTIONS) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-NFSIOSTAT(1)         General Commands Manual         PCP-NFSIOSTAT(1)

## [](#NAME)NAME

           pcp-nfsiostat - Emulate iostat for NFS mount points using
           /proc/self/mountstats

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options] nfsiostat [-a archive] [-S start] [-T finish]
           [-O origin] [-s samples] [-t interval] [-Z --timezone] [-h --host]
           [-z --hostzone] [-V Version]

## [](#DESCRIPTION)DESCRIPTION

           The pcp-nfsiostat command reports client-side Network File System
           (NFS) I/O statistics for each mounted NFS filesystem. For every
           NFS mountpoint, the output consists of a summary section followed
           by detailed read and write statistics blocks. These statistics
           include operation rates, data throughput, latency,
           retransmissions, queueing delays, and error counts. By default,
           pcp-nfsiostat monitors NFS mountpoints on the local host and
           reports live metrics collected via the  PCP NFS PMDA , or from an
           alternative host if specified. When an archive is specified,
           historical metrics are reported instead.

## [](#OUTPUT_FORMAT)OUTPUT FORMAT

           Statistics are reported per mounted NFS filesystem using the
           following layout:

           server:/export mounted on /mount/point:

                      ops/s       rpc bklog
                      0.017           0.000

           read:              ops/s   kB/s   kB/op   retrans   avg RTT (ms)   avg exe (ms)   avg queue (ms)   errors
                              ...

           write:             ops/s   kB/s   kB/op   retrans   avg RTT (ms)   avg exe (ms)   avg queue (ms)   errors
                              ...

## [](#FIELD_DESCRIPTIONS)FIELD DESCRIPTIONS

           ops/s  Number of NFS operations performed per second.

           rpc bklog
                  Average number of RPC requests waiting to be transmitted.

           kB/s   Kilobytes transferred per second.

           kB/op  Average number of kilobytes transferred per operation.

           retrans
                  Number of RPC retransmissions and the retransmission
                  percentage.

           avg RTT (ms)
                  Average round-trip time in milliseconds for RPC requests.

           avg exe (ms)
                  Average execution time in milliseconds spent servicing
                  requests on the server.

           avg queue (ms)
                  Average time in milliseconds spent waiting in the RPC
                  transmission queue.

           errors Number of failed operations and failure percentage.

## [](#OPTIONS)OPTIONS

           -a, --archive archive
                  Fetch NFS I/O statistics from the specified PCP archive.

           -s, --samples samples
                  Number of samples to collect before exiting.

           -t, --interval interval
                  Set the interval between two samples. The default is one
                  second.

           -S, --start start
                  Set the start of the time window when replaying an archive.

           -T, --finish finish
                  Set the end of the time window when replaying an archive.

           -O, --origin origin
                  Set the initial sample time within the time window when
                  replaying an archive.

           -h, --host host
                  Fetch NFS I/O statistics from the specified host.

           -z, --hostzone
                  Set the reporting timezone to the local timezone of the
                  metrics source.

           -Z, --timezone tz
                  Set the reporting timezone.

           -V, --version
                  Display version information and exit.

           -?, --help
                  Display usage information and exit.

## [](#NOTES)NOTES

           pcp-nfsiostat reports client-side NFS statistics collected from
           the kernel and exposed via the PCP NFS PMDA. The output format and
           metrics are similar to those reported by the nfsiostat(1) tool
           from the nfs-utils package.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pcp(1), nfsiostat(1), environ(7).

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

    Performance Co-Pilot               PCP                   PCP-NFSIOSTAT(1)

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
