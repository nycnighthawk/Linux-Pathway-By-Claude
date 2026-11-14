---
{"title": "pmstat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmstat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmstat(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OUTPUT](#OUTPUT) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                          |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMSTAT(1)                General Commands Manual                PMSTAT(1)

## [](#NAME)NAME

           pcp-vmstat, pmstat - high-level system performance overview

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options] vmstat [interval [samples]]

           pmstat [-gLlPVxz?]  [-a archive] [-A align] [-D debug] [-h host]
           [-H file] [-n pmnsfile] [-O offset] [-p port] [-s samples] [-S
           starttime] [-t interval] [-T endtime] [-Z timezone]

           pcp-vmstat ...

## [](#DESCRIPTION)DESCRIPTION

           pmstat provides a one line summary of system performance every
           interval unit of time (the default is 5 seconds).  pmstat is
           intended to monitor system performance at the highest level, after
           which other tools may be used to examine subsystems in which
           potential performance problems may be observed in greater detail.

           pcp-vmstat is a simple wrapper for use with the pcp(1) command,
           providing a more familiar command line format for some users.  It
           also enables the extended reporting option by default, see the -x
           option below.

           Multiple hosts may be monitored by supplying more than one host
           with multiple -h flags (for live monitoring) or by providing a
           name of the hostlist file, where each line contain one host name,
           with -H, or multiple -a flags (for retrospective monitoring from
           sets of archives).

           By default, pmstat fetches metrics by connecting to the
           Performance Metrics Collector Daemon (PMCD) on the local host.  If
           the -L option is specified, then pmcd(1) is bypassed, and metrics
           are fetched from PMDAs on the local host using the stand-alone
           PM_CONTEXT_LOCAL variant of pmNewContext(3).  When the -h option
           is specified, pmstat connects to the pmcd(1) on host and fetches
           metrics from there.  As mentioned above, multiple hosts may be
           monitored by supplying multiple -h flags.

           Alternatively, if the -a option is used, the metrics are retrieved
           from the Performance Co-Pilot archive files identified by archive,
           which is a comma-separated list of names, each of which may be the
           base name of an archive or the name of a directory containing one
           or more archives.  Multiple sets of archives may be replayed by
           supplying multiple -a flags.  When the -a flag is used, the -P
           flag may also be used to pause the output after each interval.

           Stand-alone mode can only connect to the local host, using a set
           of archives implies a host name, and nominating a host precludes
           using an archive, so the options -L, -a and -h are mutually
           exclusive.

           pmstat may relinquish its own timing control, and operate under
           the control of a pmtime(1) process that uses a GUI dialog to
           provide timing control.  In this case, either the -g option should
           be used to start pmstat as the sole client of a new pmtime(1)
           instance, or -p should be used to attach pmstat to an existing
           pmtime(1) instance via the IPC channel identified by the port
           argument.

           The -S, -T, -O and -A options may be used to define a time window
           to restrict the samples retrieved, set an initial origin within
           the time window, or specify a ``natural'' alignment of the sample
           times; refer to PCPIntro(1) for a complete description of these
           options.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -a archive, --archive=archive
                Performance metric values are retrieved from the set of
                Performance Co-Pilot (PCP) archive files identified by the
                archive argument, which is a comma-separated list of names,
                each of which may be the base name of an archive or the name
                of a directory containing one or more archives.

           -A align, --align=align
                Force the initial sample to be aligned on the boundary of a
                natural time unit align.  Refer to PCPIntro(1) for a complete
                description of the syntax for align.

           -g, --guimode
                Start pmstat as the client of a new pmtime(1) server process
                for replay of archived performance data using the pmtime(1)
                graphical user interface.

           -h host, --host=host
                Fetch performance metrics from pmcd(1) on host, rather than
                from the default localhost.

           -H path, --hostsfile=path
                Specify the path to a file containing a set of hostnames
                where pmcd(1) is running , rather than using the default
                localhost.

           -K spec, --spec-local=spec
                When fetching metrics from a local context (see -L), the -K
                option may be used to control the DSO PMDAs that should be
                made accessible.  The spec argument conforms to the syntax
                described in pmSpecLocalPMDA(3).  More than one -K option may
                be used.

           -l, --suffix
                Prints the last 7 characters of a hostname in summaries
                involving more than one host (when more than one -h option
                has been specified on the command line).

           -L, --local-PMDA
                Use a local context to collect metrics from DSO PMDAs on the
                local host without PMCD.  See also -K.

           -n pmnsfile, --namespace=pmnsfile
                Load an alternative Performance Metrics Name Space (PMNS(5))
                from the file pmnsfile.

           -O origin, --origin=origin
                When reporting archived metrics, start reporting at origin
                within the time window (see -S and -T).  Refer to PCPIntro(1)
                for a complete description of the syntax for origin.

           -p port, --guiport=port
                Attach pmstat to an existing pmtime(1) time control process
                instance via the IPC channel identified by the port argument.
                This option is normally only used by other tools, e.g.
                pmchart(1), when they launch pmstat with synchronized time
                control.

           -P, --pause
                Pause between updates for archive replay.

           -s samples, --samples=samples
                The samples option defines the number of samples to be
                retrieved and reported.  If samples is 0 or -s is not
                specified, pmstat will sample and report continuously - this
                is the default behavior.

           -S starttime, --start=starttime
                When reporting archived metrics, the report will be
                restricted to those records logged at or after starttime.
                Refer to PCPIntro(1) for a complete description of the syntax
                for starttime.

           -t interval, --interval=interval
                Set the reporting interval to something other than the
                default 5 seconds.  The interval argument follows the syntax
                described in PCPIntro(1), and in the simplest form may be an
                unsigned integer (the implied units in this case are
                seconds).

           -T endtime, --finish=endtime
                When reporting archived metrics, the report will be
                restricted to those records logged before or at endtime.

           -V, --version
                Display version number and exit.

           -x, --xcpu
                The extended CPU metrics option, causes three additional CPU
                metrics to be reported, namely wait for I/O ("wa"),
                virtualisation steal time ("st"), and virtual guest time
                ("gu").

           -z, --hostzone
                Change the reporting timezone to the local timezone at the
                host that is the source of the performance metrics, as
                identified via either the -h or -a options.

           -Z timezone, --timezone=timezone
                By default, pmtime reports the time of day according to the
                local timezone on the system where pmstat is run.  The -Z
                option changes the timezone to timezone in the format of the
                environment variable TZ as described in environ(7).

           -?, --help
                Display usage message and exit.

## [](#OUTPUT)OUTPUT

           The output from pmstat is directed to standard output, and the
           columns in the report are interpreted as follows:

           loadavg
                  The 1 minute load average.

           memory The swpd column indicates average swap space used during
                  the interval, in Kbytes.  The free column indicates average
                  free memory during the interval, in Kbytes.  The buff
                  column indicates average buffer memory in use during the
                  interval, in Kbytes.  The cache column indicates average
                  cached memory in use during the interval, in Kbytes.

                  If the values become large, they are reported as Mbytes (m
                  suffix) or Gbytes (g suffix).

           swap   The metrics in this area of the kernel instrumentation are
                  of varying value.  We try to report the average number of
                  pages that are paged in (pi) and out (po) per second during
                  the interval.  If the corresponding page swapping metrics
                  are unavailable, we report the average rate per second of
                  swap operations in (si) and out (so) during the interval.
                  It is normal for the ``in'' values to be non-zero, but the
                  system is suffering memory stress if the ``out'' values are
                  non-zero over an extended period.

                  If the values become large, they are reported as thousands
                  of operations per second (K suffix) or millions of
                  operations per second (M suffix).

           io     The bi and bo columns indicate the average rate per second
                  of block input and block output operations (respectfully)
                  during the interval.  Unless all file systems have a 1
                  Kbyte block size, these rates do not directly indicate
                  Kbytes transferred.

                  If the values become large, they are reported as thousands
                  of operations per second (K suffix) or millions of
                  operations per second (M suffix).

           system Interrupt rate (in) and context switch rate (cs).  Rates
                  are expressed as average operations per second during the
                  interval.  Note that the interrupt rate is normally at
                  least HZ (the clock interrupt rate, usually 100) interrupts
                  per second.

                  If the values become large, they are reported as thousands
                  of operations per second (K suffix) or millions of
                  operations per second (M suffix).

           cpu    Percentage of CPU time spent executing user and "nice user"
                  code (us), system and interrupt processing code (sy), idle
                  loop (id).

           If any values for the associated performance metrics are
           unavailable, the value appears as ``?'' in the output.

## [](#FILES)FILES

           $PCP_VAR_DIR/pmns/*
                default PMNS specification files

           $PCP_VAR_DIR/config/pmlogger/config.pmstat
                pmlogger(1) configuration for creating an archive suitable
                for replay with pmstat

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmclient(1), pmtime(1), PMAPI(3), pmNewContext(3),
           pcp.conf(5), pcp.env(5) and PMNS(5).

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

    Performance Co-Pilot               PCP                          PMSTAT(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcpintro(1)](../man1/pcpintro.1.html),  [pmcd(1)](../man1/pmcd.1.html),  [pmclient(1)](../man1/pmclient.1.html),  [pmrep(1)](../man1/pmrep.1.html),  [pmtime(1)](../man1/pmtime.1.html),  [pmgetoptions(3)](../man3/pmgetoptions.3.html)

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
