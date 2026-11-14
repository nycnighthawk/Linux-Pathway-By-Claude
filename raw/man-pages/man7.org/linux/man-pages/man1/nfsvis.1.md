---
{"title": "nfsvis(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/nfsvis.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nfsvis(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMAND LINE OPTIONS](#COMMAND_LINE_OPTIONS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NFSVIS(1)                General Commands Manual                NFSVIS(1)

## [](#NAME)NAME

           nfsvis - visualize performance of NFS statistics

## [](#SYNOPSIS)SYNOPSIS

           nfsvis [-V] [-c version] [-m maxrate] [-s version] [pmview
           options]

## [](#DESCRIPTION)DESCRIPTION

           nfsvis displays a three dimensional bar chart of NFS request
           statistics.  The display is updated with new values retrieved from
           the target host or archive every interval seconds (default is 2
           seconds).

           Two blocks of statistics are displayed - one for the NFS server
           and one for the NFS client requests.  The height of the bars is
           proportional to the rate at which the various request types are
           processed.

           nfsvis generates a pmview(1) configuration file, and passes most
           command line options to pmview(1).  Therefore, the command line
           options -A, -a, -C, -h, -n, -O, -p, -S, -t, -T, -Z and -z, and the
           user interface are described in the pmview(1) man page.

## [](#COMMAND_LINE_OPTIONS)COMMAND LINE OPTIONS

           The nfsvis specific options are:

           -c     Monitor NFS version 2 or 3 client metrics.  The default is
                  version 2.

           -m     Use maxrate as the maximum NFS request rate over all
                  classes of request, from which the height of the bars is
                  computed.  This effectively specifies the height at which
                  bars will be clipped.

           -s     Monitor NFS version 2 or 3 server metrics.  The default is
                  version 2.

           -V     Verbose mode - output the generated pmview(1) configuration
                  file.

## [](#FILES)FILES

           $PCP_VAR_DIR/config/pmlogger/config.nfsvis
                  A pmlogger(1) configuration file for nfsvis metrics.
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

           dkvis(1), mpvis(1), pmchart(1), pmlogger(1) and pmview(1).

           The NFS view for pmchart(1).

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

    Performance Co-Pilot                                            NFSVIS(1)

------------------------------------------------------------------------

Pages that refer to this page: [clustervis(1)](../man1/clustervis.1.html),  [dkvis(1)](../man1/dkvis.1.html),  [mpvis(1)](../man1/mpvis.1.html),  [pmview(1)](../man1/pmview.1.html)

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
