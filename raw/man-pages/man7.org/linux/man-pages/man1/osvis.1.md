---
{"title": "osvis(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/osvis.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# osvis(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMAND LINE OPTIONS](#COMMAND_LINE_OPTIONS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    OSVIS(1)                 General Commands Manual                 OSVIS(1)

## [](#NAME)NAME

           osvis - visualize high-level system activity

## [](#SYNOPSIS)SYNOPSIS

           osvis [-V] [-b bytes] [-d activity] [-i ops] [-m packets] [pmview
           options] [interface ...]

## [](#DESCRIPTION)DESCRIPTION

           osvis displays an high-level overview of performance statistics
           collected from the Performance Co-Pilot (PCP(1)) infrastructure.
           The display is modulated by the values of the performance metrics
           retrieved from the target host (which is running pmcd(1)) or from
           the PCP archive log identified by archive.  The display is updated
           every interval seconds (default 2 seconds).

           As in all pmview(1) scenes, when the mouse is moved over one of
           the bars, the current value and metric information for that bar
           will be shown in the text box near the top of the display.  The
           height and/or color of the bars is proportional to the performance
           metric values relative to the maximum expected activity, as
           controlled by the -d, -i and -m options (see below).

           The bars in the osvis scene represent the following information:

           CPU This column shows CPU utilization, aggregated over all CPUs.

           Disk
               The first stack is the rate of disk read and write operations
               aggregated over all disk spindles.  The second bar is the
               average time the disks are busy, which approximates average
               time utilization of all disks.

           Disk Controllers
               The average time the disks were busy on each controller, which
               approximates the average time utilization of all disks on each
               controller.

           Load
               The three bars represent the average load for the past 1, 5
               and 15 minutes.  This is normalized by twice the number of
               CPUs on the machine.

           Mem The stack shows memory utilization by breaking down real
               memory into kernel, file system and user usage.  The memory
               utilization metrics (mem.util) may not be available on all
               hosts, so Mem may only show the amount of free memory as a
               single bar on some hosts.

           Network Input
               The two rows of bars show the input byte rate and the input
               packet rate for each network interface, except loopback and
               slip interfaces.

           Network Output
               The two rows of bars show the output byte rate and the output
               packet rate for each network interface, except for loopback
               and slip interfaces.

## [](#COMMAND_LINE_OPTIONS)COMMAND LINE OPTIONS

           If any optional interface arguments are specified in the command
           line, then just the network interfaces matching the interface
           arguments will appear in the Network Input and Network Output
           sections.  By default, all interfaces will be used.  The interface
           arguments are used as patterns for egrep(1) matching against the
           interface names, so ec would select all external Ethernet
           interfaces for a Challenge S.

           osvis uses pmview(1), and so the user interface follows that
           described for pmview(1), which in turn displays the scene within
           an Inventor examiner viewer.

           osvis passes most command line options to pmview(1).  Therefore,
           the command line options -A, -a, -C, -h, -n, -O, -p, -S, -t, -T,
           -x, -Z and -z, and the user interface are described in the
           pmview(1) man page.

           Options specific to osvis are:

           -b     Controls the maximum expected network throughput, in bytes.
                  The default value is 65536 bytes.

           -d     Controls the maximum expected disk utilization, as a
                  percentage.  The default value is 30%.

           -i     Controls the maximum (normalization) value for the disk
                  read and write rates.  The default value is 100
                  operations/second.

           -m     Controls the maximum (normalization) value for the packet
                  input and packet output rates.  The default value is 750
                  packets/second.

           -V     The derived configuration file for pmview(1) is written on
                  standard output.  This may be saved and used directly with
                  pmview if the user wishes to customize the display, or
                  modify some of the normalization parameters.

## [](#FILES)FILES

           $PCP_VAR_DIR/pmns/*
                  default PMNS specification files
           $PCP_VAR_DIR/config/pmlogger/config.osvis
                  pmlogger(1) configuration file that can be used to create a
                  PCP archive suitable for display with osvis

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(4).

## [](#SEE_ALSO)SEE ALSO

           pmcd(1), pmlogger(1), pmview(1), pcp.conf(4), pcp.env(4) and
           pmlaunch(5).

## [](#DIAGNOSTICS)DIAGNOSTICS

           osvis will silently remove those blocks from the scene whose
           metrics are not available from the live host or the archive.

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

    Performance Co-Pilot                                             OSVIS(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmview(1)](../man1/pmview.1.html)

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
