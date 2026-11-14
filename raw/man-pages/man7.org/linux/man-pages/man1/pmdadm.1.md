---
{"title": "pmdadm(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdadm.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdadm(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [CONFIGURATION](#CONFIGURATION) \| [METRICS](#METRICS) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDADM(1)                General Commands Manual                PMDADM(1)

## [](#NAME)NAME

           pmdadm - Device Mapper PMDA

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/dm/pmdadm [-D debug]

## [](#DESCRIPTION)DESCRIPTION

           pmdadm is a Performance Metrics Domain Agent (PMDA) which exports
           metric values for Device Mapper on the local system.

           This PMDA collects its data through the dmsetup(8) utility and the
           dmstats API and requires that the program is installed in order to
           function.  In addition, at least one statistics region must be
           created using the dmstats(8) utility in order to get basic counter
           values.  See below for examples.

           Note that device-mapper statistics collection is not enabled by
           default and is not persistent across reboots (unless a system
           administrator has configured something to run in rc.local or
           equivalent).  This is because there are overheads associated with
           statistics collection.  In addition, the pmdadm PMDA does not
           automatically enable any statistics collection because it may not
           be the only consumer of the data.

## [](#INSTALLATION)INSTALLATION

           Install the DM PMDA by using the Install script as root:

               # cd $PCP_PMDAS_DIR/dm
               # ./Install

           To uninstall, the following must be done as root:

               # cd $PCP_PMDAS_DIR/dm
               # ./Remove

           pmdadm is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd when the
           agent is installed or removed.

## [](#CONFIGURATION)CONFIGURATION

           This PMDA uses the dmstats API (the userspace device-mapper
           support library) to capture device-mapper performance data.
           Using this PMDA, users need the userspace device-mapper support
           library (libdevmapper) and the userspace command line tool
           dmstats(8).  Before device-mapper metrics will be available for
           PCP, statistics regions have to be created.  For example, to
           enable basic statistics for all local device-mapper logical
           devices, use the following command:

                # dmstats create --alldevices

           To create statistics regions with specified histogram boundaries,
           use the following:

                # dmstats create --alldevices --bounds histogram_boundaries

           Specify the boundaries of a latency histogram to be tracked for
           the region as a comma separated list of latency values. Latency
           values are given in nanoseconds. An optional unit suffix of ns,
           us, ms, or s may be given after each value to specify units of
           nanoseconds, microseconds, miliseconds or seconds respectively.
           For example,

                # dmstats create --alldevices --bounds 10us,30us,50us,70us,90us

           Further details and more complex examples can be found in
           dmstats(8).

## [](#METRICS)METRICS

           Basic Counters
               Basic counters provide access to the raw counter data from the
               kernel, allowing further processing to be carried out by
               another program.
               The Kernel provides thirteen separate counters for each
               statistics area.  The first eleven of these match the counters
               provided in /proc/diskstats or /sys/block/*/*/stat. The final
               pair provide separate counters for read and write time.

               dmstats.read
                   Count of reads completed this interval per device-mapper
                   device.

               dmstats.reads_merged
                   Count of reads merged this interval per device-mapper
                   device.

               dmstats.read_bytes
                   Count of kbytes read this interval per device-mapper
                   device.

               dmstats.reads_time
                   Accumulated duration of all read requests per device-
                   mapper device.

               dmstats.write
                   Count of writes completed this interval per device-mapper
                   device.

               dmstats.writes_merged
                   Count of writes completed this interval per device-mapper
                   device.

               dmstats.write_bytes
                   Count of kbytes write this interval per device-mapper
                   device.

               dmstats.writes_time
                   Accumulated duration of all write requests per device-
                   mapper device.

               dmstats.in_progress
                   Count of requests currently in progress per device-mapper
                   device.

               dmstats.io_ticks
                   Nanoseconds spent servicing request per device-mapper
                   device.

               dmstats.queue_ticks
                   This field is incremented at each I/O start, I/O
                   completion, I/O merge, or read of these stats by the
                   number of I/Os in progress multiplied by the number of
                   nanoseconds spent doing I/O since the last update of this
                   field. This can provide an easy measure of both I/O
                   completion time and the backlog that may be accumulating.

               dmstats.read_ticks
                   Nanoseconds spent servicing reads per device-mapper
                   device.

               dmstats.write_ticks
                   Nanoseconds spent servicing writes per device-mapper
                   device.

           Histogram fields
               Histograms measure the frequency distribution of user
               specified I/O latency intervals.  Histogram bin boundaries are
               specified when a region is created.
               Instance name represents devicename, region id and bin
               boundaries.

               dmstats.histogram.hist_count
                   A list of the histogram counts for the current statistics
                   area in order of ascending latency value. Each value
                   represents the number of I/Os with latency times falling
                   into that bin's time range during the sample period.

               dmstats.histogram.hist.bins
                   The number of latency histogram bins configured for the
                   area.

## [](#EXAMPLES)EXAMPLES

           # dmstats create looptest0 --bounds 10us,30us,50us
           looptest0: Created new region with 1 area(s) as region ID 0

           # pminfo -f dmstats.read dmstats.histogram.hist_count

           dmstats.read
               inst [0 or "looptest0"] value 4099

           dmstats.histogram.hist_count
               inst [0 or "looptest0:0:0s"] value 1
               inst [1 or "looptest0:0:10us"] value 3752
               inst [2 or "looptest0:0:30us"] value 250
               inst [3 or "looptest0:0:50us"] value 96

## [](#FILES)FILES

           $PCP_PMDAS_DIR/dm/help
               default help text file for the dm metrics

           $PCP_PMDAS_DIR/dm/Install
               installation script for the pmdadm agent

           $PCP_PMDAS_DIR/dm/Remove
               undo installation script for the pmdadm agent

           $PCP_LOG_DIR/pmcd/dm.log
               default log file for error messages from pmdadm

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP. On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmstore(1), dmsetup(8) and dmstats(8).

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

    Performance Co-Pilot               PCP                          PMDADM(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcp-dmcache(1)](../man1/pcp-dmcache.1.html)

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
