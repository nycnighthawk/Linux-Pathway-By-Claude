---
{"title": "dkvis(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dkvis.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dkvis(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMAND LINE OPTIONS](#COMMAND_LINE_OPTIONS) \| [LAUNCH](#LAUNCH) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DKVIS(1)                        Co-Pilot"                        DKVIS(1)

## [](#NAME)NAME

           dkvis - visualize disk I/O activity and performance

## [](#SYNOPSIS)SYNOPSIS

           dkvis [-brVw] [-m maxrate] [-X ndisk] [-Y nctl] [pmview options]
           [diskid ...]

## [](#DESCRIPTION)DESCRIPTION

           dkvis displays a three dimensional bar chart of disk activity.
           Each row of bars on the base plane represents a disk controller
           (or host adapter, or bus), and the bars within a row correspond to
           the disks attached to the controller.

           The label to the left of each row identifies the common part of
           disk name for all disks in that row, e.g. dks3 for all IRIX SCSI
           disks attached to controller number 3.

           The height of the bars is proportional to the activity.

           The user can specify a list of disks as diskid arguments using the
           disk naming scheme reported by
              $ pminfo -f disk.dev.total
           e.g. hda or dks0d4 or sda or scsi/host1/bus0/target4/lun0/disc or
           20000080e5114459/lun3/c2p1 depending on the type of disks.
           Alternatively, if the diskid argument contains one of the
           characters ^ or .  or [ then diskid will be treated as a regular
           expression in the style of egrep(1) and the matching set of disk
           names will be used instead of diskid.

           If one or more diskid arguments is specified, only the disks in
           this list are displayed in the view.  The disks are grouped in the
           scene by controller as in the default scene when all disks are
           present.

           dkvis generates a pmview(1) configuration file, and passes most
           command line options to pmview(1).  Therefore, the command line
           options -A, -a, -C, -h, -n, -O, -p, -S, -t, -T, -Z and -z, and the
           user interface are described in the pmview(1) man page.

## [](#COMMAND_LINE_OPTIONS)COMMAND LINE OPTIONS

           The dkvis specific options are:

           -b     Report the activity as data throughput in Kbytes per second
                  rather than the default I/O operations per second (IOPS).

           -m     Use maxrate as the maximum activity from which utilization
                  percentages are computed.  This effectively specifies the
                  height at which bars will be clipped.  If -b is specified
                  the default maximum value is 2048 Kbytes per second,
                  otherwise the default maximum value is 150 IOPS.

           -r     Display the read activity.  The default is to display the
                  total (read and write) activity.

           -V     Verbose mode - output the generated pmview(1) configuration
                  file.

           -w     Display the write activity.  The default is to display the
                  total (read and write) activity.

           -X     The default arrangement attempts to display up to 12 disks
                  on the same controller in a single row.  When more than 12
                  disks are associated with a controller, additional rows are
                  created in an attempt to achieve a baseplane footprint for
                  the scene that is as close to square as we can manage.

                  The -X option may be used to over-ride the default layout
                  algorithm and force a scene in which each row contains no
                  more than ndisk disks.

           -Y     The default arrangement attempts to display disks for up to
                  16 controller rows in a single block.  When more than 16
                  controller rows are present, additional blocks are created
                  in an attempt to achieve a baseplane footprint for the
                  scene that is as close to square as we can manage.

                  The -Y option may be used to over-ride the default layout
                  algorithm and force a scene in which blocks are assigned
                  such that each contains no more than nctl controller rows.

                  For backwards compatibility -R is a deprecated synonym for
                  -Y .

           Only one type of activity can be displayed per invocation of
           dkvis, hence -r and -w are mutually exclusive.

## [](#LAUNCH)LAUNCH

           The behavior of pmchart(1) when launched from dkvis is dependent
           on the number of disks in each row.  If there are more than 6
           controllers then a separate chart will be generated for each
           column of disks.  In other words, the first disk from each
           controller in one chart, the second disk in the next chart and so
           on.  Otherwise a separate chart will be generated for each disk
           controller.

## [](#FILES)FILES

           $PCP_VAR_DIR/config/pmlogger/config.dkvis
                  A pmlogger(1) configuration file for dkvis metrics.
           $PCP_SHARE_DIR/lib/pmview-args
                  Shell procedures for parsing pmview(1) command line
                  options.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(4).

## [](#SEE_ALSO)SEE ALSO

           dkstat(1), mpvis(1), nfsvis(1), pmchart(1), pmlogger(1),
           pmview(1), pcp.conf(4) and pcp.env(4).

           The Disk and DiskCntrls views for pmchart(1).

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

    Performance                                                      DKVIS(1)

------------------------------------------------------------------------

Pages that refer to this page: [clustervis(1)](../man1/clustervis.1.html),  [mpvis(1)](../man1/mpvis.1.html),  [nfsvis(1)](../man1/nfsvis.1.html),  [pmie(1)](../man1/pmie.1.html),  [pmview(1)](../man1/pmview.1.html)

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
