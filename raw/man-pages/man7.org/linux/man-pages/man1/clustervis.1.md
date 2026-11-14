---
{"title": "clustervis(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/clustervis.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# clustervis(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CLUSTERVIS(1)            General Commands Manual            CLUSTERVIS(1)

## [](#NAME)NAME

           clustervis - visualize cpu and network performance on a cluster

## [](#SYNOPSIS)SYNOPSIS

           clustervis [-H nodesfile] [-h host[,host...]]  [-a
           archive[,archive...]]  [-m max] [pmview options]

## [](#DESCRIPTION)DESCRIPTION

           clustervis displays three dimensional bar charts of CPU
           utilization and network traffic for one or most hosts in a
           cluster.  An alternative two dimensional cluster performance
           monitoring tool is pmgcluster(1).  clustervis is designed to
           provide a scalable overview of the performance of large clusters.
           Other tools such as pmchart(1) and pmgsys(1) provide drill-down
           details on a per-host basis.  These tools may be launched by
           clicking on the purple base plane for a particular host and then
           selecting a tool from the launch menu in clustervis.

           The -H, -h and -a arguments are all mutually exclusive and have
           the following semantics; if none of -H, -h or -a is given, and
           either the file /etc/nodes or /etc/ace/nodes exists, or the
           $PCP_CLUSTER_CONFIG environment variable is set, then use the
           named file as the set of hosts for live monitoring.  If the
           default nodes file does not exist, the environment variable is not
           set and none of the three flags were given, an error is reported.
           Otherwise, if -H is given, then the set of hosts is given in
           nodesfile.

           The -h flag specifies one or more (comma separated with no spaces)
           hosts for live monitoring and the -a flag specifies one or more
           archives for archive replay (comma separated).

           The height of the CPU stack is proportional to the CPU utilization
           in each of the modes sys (red, executing in the kernel) and user
           (blue, executing user code).  The network traffic stack is shown
           for each network interface as the packet rate in (light blue), out
           (orange) and errors (red).  The hight of the network stack is
           modulated by the -m argument, with a default of 750 packets/second
           representing saturated network traffic.

           clustervis generates a pmview(1) configuration file, and passes
           most command line options to pmview(1).  Therefore, the command
           line options -A, -a, -C, -h, -n, -O, -p, -S, -t, -T, -Z and -z,
           and the user interface are described in the pmview(1) man page.

## [](#FILES)FILES

           $PCP_VAR_DIR/config/pmlogger/config.clustervis
                  A pmlogger(1) configuration file for clustervis metrics.
           /usr/pcp/lib/pmview-args
                  Shell procedures for parsing pmview(1) command line
                  options.
           /etc/nodes
                  Default set of hosts in the cluster.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           The PCP_CLUSTER_CONFIG environment variable may be used to specify
           the default nodes file instead of using the -H flag. Each line in
           the file is a host name (or a comment starting with #).  Other
           environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(4).

## [](#SEE_ALSO)SEE ALSO

           dkvis(1), mpvis(1), nfsvis(1), pmcd(1), pmchart(1), pmlogger(1),
           pmview(1), pcp.conf(4) and pcp.env(4).

           The CPU view for pmchart(1).

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

    Performance Co-Pilot                                        CLUSTERVIS(1)

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
