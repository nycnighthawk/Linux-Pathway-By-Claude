---
{"title": "webvis(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/webvis.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# webvis(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    WEBVIS(1)                General Commands Manual                WEBVIS(1)

## [](#NAME)NAME

           webvis - visualize system-level Web server activity

## [](#SYNOPSIS)SYNOPSIS

           webvis [-CVz] [-A align] [-a archive] [-b maxbusy] [-h host] [-i
           maxio] [-m max] [-n pmnsfile] [-O time] [-p port] [-r maxreq] [-S
           time] [-T time] [-t interval] [-x version] [-Z timezone]
           [interface ...]

## [](#DESCRIPTION)DESCRIPTION

           webvis displays an overview of system level Web server performance
           statistics collected from the Performance Co-Pilot (PCP)
           infrastructure.  The display is modulated by the values of the
           performance metrics retrieved from the target host (which is
           running pmcd(1) and the pmdaweblog(1) Performance Metrics Domain
           Agent) or from the PCP archive log identified by archive.  The
           display is updated every interval seconds (default 2 seconds).

           As in all pmview(1) scenes, when the mouse is moved over one of
           the bars, the current value and metric information for that bar
           will be shown in the text box near the top of the display.

           The height of the web request and network activity bars is
           proportional to the performance metric values relative to the
           maximum expected activity, as controlled by the -m and -r options
           (see below).  Similarly the -b and -i options control the scaling
           for disk activity bars.

           The bars in the webvis scene represent the following information;

           Requests by Size
               At the front of the scene, the "Requests by Size" row of bars
               shows the rate of requests for different size requests (the
               histograms are defined by the following byte counts: 0, 3
               Kbytes, 10 Kbytes, 30 Kbytes, 100 Kbytes, 300 Kbytes, 1 Mbyte,
               3 Mbytes and larger than 3 Mbytes).  Notice that the size
               divisions are not evenly distributed.  The "size" is the data
               portion of the response to each Web server request.  These
               rates are aggregated across all monitored Web servers.

           Requests by Type
               This row of bars shows the request rate for each type of HTTP
               request (get, post, head and other), aggregated across all
               monitored Web servers.  For a detailed display showing the
               break down of requests per Web server, see weblogvis(1).

           Network
               For every network interface there are two stacked bars.  One
               of the bars shows the input traffic while the other bar shows
               the output traffic.  The stacks are composed of the number of
               errors (red), the number of drops (orange) and the number of
               packets (green).  In general, if there are any "dropped input
               packets" then the corresponding network interface is
               saturated, or there are insufficient network resources
               available in the kernel to adequately service the input
               request load.  If this is the case then the Alarm Conditions
               rows (see below) may provide more detail into the source of
               the problem.

           Alarm Conditions
               The red row of bars shows an assortment of TCP error
               conditions (aggregated for all network interfaces), the orange
               bars show critical kernel buffer allocation problems, and the
               yellow bar shows severe paging conditions.  If any of these
               bars have a non-zero height then the system being monitored
               may require kernel parameter tuning, software reconfiguration
               or more hardware resources.  The performance metrics behind
               the bars are:

               network.tcp.drops
                      - rate of dropped connections

               network.tcp.conndrops
                      - rate of embryonic connections dropped

               network.tcp.timeoutdrop
                      - rate of connections dropped by rexmit timeout

               network.tcp.rcvbadsum
                      - rate of packets discarded for bad checksums

               network.tcp.rexmttimeo
                      - rate of retransmit timeouts

               network.tcp.sndrexmitpack
                      - rate of data packets retransmitted

               swap.pagesout
                      - page swap out rate (indicating insufficient memory)

               network.mbuf.failed
                      - rate of incidents where the kernel failed to find
                      mbuf space

               network.mbuf.waited
                      - rate of incidents where the kernel waited to find
                      mbuf space

           CPU This column shows CPU utilization, aggregated over all CPUs.
               (CPU idle time is not included in the column).

           Disk
               There are two cylinders showing disk metrics.  The first
               cylinder shows the rate of read (yellow) and write (violet)
               operations, aggregated over all disk spindles.  The second
               cylinder shows the average (over all disks) percentage of time
               for which a disk is busy or active.  This metric is not
               available in PCP1.x versions, therefore if webvis is being
               used to monitor a host running PCP1.x this cylinder will not
               be displayed.

               To adjust the scaling of these objects, refer to the -b and -i
               options described below.

           Mem There are two bars showing memory metrics.  The first bar
               shows utilized memory, with different colors representing
               different types of utilization (kernel, user, etc), while the
               second bar shows the amount of free memory.  If webvis is
               being used to monitor a host running PCP1.x then only the bar
               showing free memory will be displayed.

           If any optional interface arguments are specified in the command
           line, then just the network interfaces matching the interface
           arguments will appear in the Network section.  By default, all
           interfaces will be used.  The interface arguments are used as
           patterns for egrep(1) matching against the interface names, so ec
           would select all external Ethernet interfaces for a Challenge S.

           webvis uses pmview(1), and so the user interface follows that
           described for pmview(1), which in turn displays the scene within
           an Inventor examiner viewer.

           webvis passes most command line options to pmview(1).  Therefore,
           the command line options -A, -a, -C, -h, -n, -O, -p, -S, -t, -T,
           -x, -Z and -z, and the user interface are described in the
           pmview(1) man page.

           Options specific to webvis are:

           -b maxbusy
                  Controls the maximum (normalization) value for the average
                  percentage of the time active over all disks.  The default
                  value is 30% active.

           -i maxio
                  Controls the maximum (normalization) value for the sume of
                  the aggregate disk read and disk write rates.  The default
                  value is 100 I/Os per second.

           -m max Controls the maximum (normalization) value for the packet
                  input and packet output rates.  The default value is 750
                  packets/second.

           -r maxreq
                  Controls the maximum Web request rate.  The default is 5%
                  of the maximum packet rate (i.e. 38 requests/second by
                  default).  The maximum Web error rate is fixed at 20% of
                  the maximum Web request rate (i.e. 7 errors/second by
                  default).

           -V     The derived configuration file for pmview(1) is written on
                  standard output.  This may be saved and used directly with
                  pmview if the user wishes to customize the display, or
                  modify some of the normalization parameters.

## [](#FILES)FILES

           $PCP_VAR_DIR/pmns/*
                  default PMNS specification files
           $PCP_VAR_DIR/config/pmlogger/config.web
                  pmlogger(1) configuration file that can be used to create a
                  PCP archive suitable for display with webvis

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(4).

## [](#SEE_ALSO)SEE ALSO

           pmcd(1), pmchart(1), pmdaweblog(1), pmdawebping(1), pmdumplog(1),
           pminfo(1), pmlogger(1), pmval(1), pmview(1), weblogvis(1),
           webpingvis(1), pcp.conf(4) and pcp.env(4).

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

    Performance Co-Pilot                                            WEBVIS(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmdaweblog(1)](../man1/pmdaweblog.1.html),  [weblogvis(1)](../man1/weblogvis.1.html),  [webpingvis(1)](../man1/webpingvis.1.html)

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
