---
{"title": "nfsiostat(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/nfsiostat.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nfsiostat(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    nfsiostat(8)             System Manager's Manual             nfsiostat(8)

## [](#NAME)NAME

           nfsiostat - Emulate iostat for NFS mount points using
           /proc/self/mountstats

## [](#SYNOPSIS)SYNOPSIS

           nfsiostat [[<interval>] [<count>]] [<options>][<mount_point>]

## [](#DESCRIPTION)DESCRIPTION

           The nfsiostat command displays NFS client per-mount statistics.

           <interval>
                  specifies the amount of time in seconds between each
                  report.  The first report contains statistics for the time
                  since each file system was mounted.  Each subsequent report
                  contains statistics collected during the interval since the
                  previous report.

           <count>
                  If the <count> parameter is specified, the value of <count>
                  determines the number of reports generated at <interval>
                  seconds apart. if the interval parameter is specified
                  without the <count> parameter, the command generates
                  reports continuously.

           <options>
                  Define below

           <mount_point>
                  If one or more <mount point> names are specified,
                  statistics for only these mount points will be displayed.
                  Otherwise, all NFS mount points on the client are listed.

           The meaning of each column of nfsiostat's output is the following:
                   - op/s
                          This is the number of operations per second.
                   - rpc bklog
                          This is the length of the backlog queue.
                   - kB/s (MB/s)
                          This is the number of kB (or MB) written/read per
                          second.
                   - kB/op (MB/op)
                          This is the number of kB (or MB) written/read per
                          each operation.
                   - retrans
                          This is the number of retransmissions.
                   - avg RTT (ms)
                          This is the duration from the time that client's
                          kernel sends the RPC request until the time it
                          receives the reply.
                   - avg exe (ms)
                          This is the duration from the time that NFS client
                          does the RPC request to its kernel until the RPC
                          request is completed, this includes the RTT time
                          above.
                   - avg queue (ms)
                          This is the duration from the time the NFS client
                          created the RPC request task to the time the
                          request is transmitted.
                   - errors
                          This is the number of operations that completed
                          with an error status (status < 0).  This count is
                          only available on kernels with RPC iostats version
                          1.1 or above.

           Note that if an interval is used as argument to nfsiostat, then
           the difference from previous interval will be displayed, otherwise
           the results will be from the time that the share was mounted.

## [](#OPTIONS)OPTIONS

           -a  or  --attr
                  displays statistics related to the attribute cache

           -d  or  --dir
                  displays statistics related to directory operations

           -h  or  --help
                  shows help message and exit

           -l LIST or  --list=LIST
                  only print stats for first LIST mount points

           -m or  --megabytes
                  display throughput in megabytes per second

           -p  or  --page
                  displays statistics related to the page cache

           -s  or  --sort
                  Sort NFS mount points by ops/second

           --version
                  show program's version number and exit

## [](#FILES)FILES

           /proc/self/mountstats

## [](#SEE_ALSO)SEE ALSO

           iostat(8), mountstats(8), nfsstat(8)

## [](#AUTHOR)AUTHOR

           Chuck Lever <chuck.lever@oracle.com>

## [](#COLOPHON)COLOPHON

           This page is part of the nfs-utils (NFS utilities) project.
           Information about the project can be found at 
           ⟨http://linux-nfs.org/wiki/index.php/Main_Page⟩.  If you have a bug
           report for this manual page, see
           ⟨http://linux-nfs.org/wiki/index.php/Main_Page⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨git://git.linux-nfs.org/projects/steved/nfs-utils.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-23.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                   15 Apr 2010                   nfsiostat(8)

------------------------------------------------------------------------

Pages that refer to this page: [mountstats(8)](../man8/mountstats.8.html)

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
