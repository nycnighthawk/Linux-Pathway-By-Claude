---
{"title": "pmdaperfevent(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdaperfevent.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdaperfevent(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [UPGRADING](#UPGRADING) \| [BUGS](#BUGS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAPERFEVENT(1)         General Commands Manual         PMDAPERFEVENT(1)

## [](#NAME)NAME

           pmdaperfevent - hardware performance counter performance metrics
           domain agent (PMDA)

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/perfevent/pmdaperfevent [-d domain] [-l logfile]
           [-U username] [-i port] [-p] [-u socket] [-6]

## [](#DESCRIPTION)DESCRIPTION

           pmdaperfevent is a Performance Metrics Domain Agent (PMDA) that
           configures and reads the hardware performance counters using the
           Linux kernel perf_event API.

           The perfevent PMDA exports metrics for hardware performance
           counters that are configurable from the Linux kernel perf_event
           API.  The PMDA uses the libpfm4 library to access the hardware
           performance counters so any counters that are supported in libpfm4
           should be available.  Also included is the ability to read the
           Intel RAPL counters via direct MSR access.  The PMDA supports
           automatically loading different counters for each hardware
           architecture.  A single configuration file is used to specify the
           desired counters for each hardware performance monitoring unit
           (PMU).  The configuration file allows different counters to be
           programmed on different CPUs and supports round-robin assignment
           of uncore counters needed for some AMD chips.

           The PMDA also counts for events exposed in the kernel via
           /sys/bus/event_source/devices directory. The PMU device name and
           the event name must be mentioned in the configuration file.
           Otherwise, the metric won't be available to monitor through this
           PMDA.

           The PMDA configures the counters to count events in both user and
           kernel mode.  This means that the hardware counters are
           unavailable to use by normal unprivileged user applications when
           they are in use by the PMDA.  The PMDA provides a mechanism to
           temporarily disable the system-wide counters in order to allow
           normal users to be able to use the counters if they wish.  See
           perfalloc(1) for details.

           Note that pmdaperfevent is affected by the value of the
           kernel.perf_event_paranoid setting, which can be adjusted by
           sysctl(8).

           A brief description of the pmdaperfevent command line options
           follows:

           -d   It is absolutely crucial that the performance metrics domain
                number specified here is unique and consistent.  That is,
                domain should be different for every PMDA on the one host,
                and the same domain number should be used for the same PMDA
                on all hosts.

           -l   Location of the log file.  By default, a log file named
                perfevent.log is written in the current directory of pmcd(1)
                when pmdaperfevent is started, i.e.  $PCP_LOG_DIR/pmcd.  If
                the log file cannot be created or is not writable, output is
                written to the standard error instead.

           -U   User account under which to run the agent.  The default is
                the privileged "root" account.

           -i   listen on given port number for connection from pmcd(1)

           -p   communicate with pmcd(1) via stdin/stdout

           -u   expect pmcd(1) to connect on given unix domain socket

           -6   expect pmcd(1) to connect on given ipv6 port (number or name)

## [](#INSTALLATION)INSTALLATION

           The perfevent PMDA is not activated by default To install the
           PMDA, do the following as root:

                # cd $PCP_PMDAS_DIR/perfevent
                # ./Install

           If you want to undo the installation, do the following as root:

                # cd $PCP_PMDAS_DIR/perfevent
                # ./Remove

           pmdaperfevent is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMCDCONF_PATH
                  command line options used to launch pmdaperfevent
           $PCP_PMDAS_DIR/perfevent/perfevent.conf
                  default configuration file for the PMDA.  See
                  perfevent.conf(5) for detailed information.
           $PCP_PMDAS_DIR/perfevent/help
                  default help text file for the perfevent metrics
           $PCP_PMDAS_DIR/perfevent/Install
                  installation script for the pmdaperfevent agent
           $PCP_PMDAS_DIR/perfevent/Remove
                  undo installation script for the pmdaperfevent agent
           $PCP_LOG_DIR/pmcd/perfevent.log
                  default log file for error messages and other information
                  from pmdaperfevent

## [](#UPGRADING)UPGRADING

           Some metric names have changed starting in version 3.10.8 to
           better conform to PMNS conventions.  pmlogrewrite(1) can be used
           to update old archives.  A helper utility,
           $PCP_PMDAS_DIR/perfevent/perfevent-makerewrite.pl will generate a
           config file that is suitable for use with pmlogrewrite(1) to
           update the metric names in existing archives.

## [](#BUGS)BUGS

           Each event is placed in its own group and there is no way to group
           related events together so they are guaranteed to be
           simultaneously active.  A workaround for this is to ensure that
           the number of configured events is less than or equal to the
           number of available hardware counters.  This means that the events
           will not be time-multiplexed by the kernel and will be
           simultaneously active.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           perfalloc(1), perfevent.conf(5), PCPIntro(1), pmcd(1),
           pmlogrewrite(1), PMAPI(3), pcp.conf(5), pcp.env(5) and sysctl(8).

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

    Performance Co-Pilot               PCP                   PMDAPERFEVENT(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcp-atop(1)](../man1/pcp-atop.1.html),  [perfalloc(1)](../man1/perfalloc.1.html),  [perfevent.conf(5)](../man5/perfevent.conf.5.html)

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
