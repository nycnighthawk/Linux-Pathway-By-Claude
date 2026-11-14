---
{"title": "mountstats(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/mountstats.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mountstats(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mountstats(8)            System Manager's Manual            mountstats(8)

## [](#NAME)NAME

           mountstats - Displays various NFS client per-mount statistics

## [](#SYNOPSIS)SYNOPSIS

           mountstats [-h|--help] [-v|--version] [-f|--file infile]
           [-S|--since sincefile] [ [-n|--nfs] | [-r|--rpc] | [-R|--raw] |
           [-x|--xprt] ] [mountpoint]...

           mountstats iostat [-h|--help] [-v|--version] [-f|--file infile]
           [-S|--since sincefile] [interval] [count] [mountpoint]...

           mountstats nfsstat [-h|--help] [-v|--version] [-f|--file infile]
           [-S|--since sincefile] [-3] [-4] [mountpoint]...

## [](#DESCRIPTION)DESCRIPTION

           The mountstats command displays various NFS client statistics for
           each given mountpoint.

           If no mountpoint is given, statistics will be displayed for all
           NFS mountpoints on the client.

       Sub-commands
           Valid mountstats(8) subcommands are:

           mountstats
                  Display a combination of per-op RPC statistics, NFS event
                  counts, and NFS byte counts.  This is the default sub-
                  command that will be executed if no sub-command is given.

           iostat Display iostat-like statistics.

           nfsstat
                  Display nfsstat-like statistics.

## [](#OPTIONS)OPTIONS

       Options valid for all sub-commands
           -h, --help
                  show the help message and exit

           -v, --version
                  show program's version number and exit

           -f infile, --file infile
                  Read stats from infile instead of /proc/self/mountstats.
                  infile must be in the same format as /proc/self/mountstats.
                  This may be used with the -S|--since options to display the
                  delta between two different points in time.  This may not
                  be used with the interval or count options of the iostat
                  sub-command.

           -S sincefile, --since sincefile
                  Show difference between current stats and those in
                  sincefile.  sincefile must be in the same format as
                  /proc/self/mountstats.  This may be used with the -f|--file
                  options to display the delta between two different points
                  in time.  This may not be used with the interval or count
                  options of the iostat sub-command.

       Options specific to the mountstats sub-command
           -n, --nfs Display only the NFS statistics

           -r, --rpc
                  Display only the RPC statistics

           -R, --raw
                  Display only the raw statistics.  This is intended for use
                  with the -f|--file and -S|--since options.

           -x, --xprt
                  Display only the transport statistics

       Options specific to the iostat sub-command
           interval
                  Specifies the amount of time in seconds between each
                  report.  The first report contains statistics for the time
                  since each file system was mounted.  Each subsequent report
                  contains statistics collected during the interval since the
                  previous report.  This may not be used with the -f|--file
                  or -S|--since options.

           count  Determines the number of reports generated at interval
                  seconds apart.  If the interval parameter is specified
                  without the count parameter, the command generates reports
                  continuously.  This may not be used with the -f|--file or
                  -S|--since options.

       Options specific to the nfsstat sub-command
           -3     Show only NFS version 3 statistics.  The default is to show
                  both version 3 and version 4 statistics.

           -4     Show only NFS version 4 statistics.  The default is to show
                  both version 3 and version 4 statistics.

## [](#FILES)FILES

           /proc/self/mountstats

## [](#SEE_ALSO)SEE ALSO

           iostat(8), nfsiostat(8), nfsstat(8)

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

                                   12 Dec 2014                  mountstats(8)

------------------------------------------------------------------------

Pages that refer to this page: [pmdanfsclient(1)](../man1/pmdanfsclient.1.html),  [mountstats(8)](../man8/mountstats.8.html),  [nfsiostat(8)](../man8/nfsiostat.8.html)

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
