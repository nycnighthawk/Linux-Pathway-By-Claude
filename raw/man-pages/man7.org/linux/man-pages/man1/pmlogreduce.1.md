---
{"title": "pmlogreduce(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmlogreduce.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmlogreduce(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DATA REDUCTION](#DATA_REDUCTION) \| [CAVEATS](#CAVEATS) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOGREDUCE(1)           General Commands Manual           PMLOGREDUCE(1)

## [](#NAME)NAME

           pmlogreduce - temporal reduction of Performance Co-Pilot archives

## [](#SYNOPSIS)SYNOPSIS

           pmlogreduce [-z?]  [-A align] [-D debug] [-s samples] [-S
           starttime] [-t interval] [-T endtime] [-v volsamples] [-Z
           timezone] input output

## [](#DESCRIPTION)DESCRIPTION

           pmlogreduce reads one set of Performance Co-Pilot (PCP) archives
           identified by input and creates a temporally reduced PCP archive
           in output.  input is a comma-separated list of names, each of
           which may be the base name of an archive or the name of a
           directory containing one or more archives.  The data reduction
           involves statistical and temporal reduction of samples with an
           output sampling interval defined by the -t option in the output
           archive (independent of the sampling intervals in the input
           archives), and is further controlled by other command line
           arguments.

           For some metrics, temporal data reduction is not going to be
           helpful, so for metrics with types PM_TYPE_AGGREGATE or
           PM_TYPE_EVENT, a warning is issued if these metrics are found in
           input and they will be skipped and not appear in the output
           archive.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -A align, --align=align
                Specify a ``natural'' alignment of the output sample times;
                refer to PCPIntro(1).

           -s samples, --samples=samples
                The argument samples defines the number of samples to be
                written to output.  If samples is 0 or -s is not specified,
                pmlogreduce will sample until the end of the set of PCP
                archives, or the end of the time window as specified by -T,
                whichever comes first.  The -s option will override the -T
                option if it occurs sooner.

           -S starttime, --start=starttime
                Define the start of a time window to restrict the samples
                retrieved from the input archives; refer to PCPIntro(1).

           -t interval, --interval=interval
                Consecutive samples in the output archive will appear with a
                time delta defined by interval; refer to PCPIntro(1).  Note
                the default value is 600 (seconds, i.e. 10 minutes).

           -T endtime, --finish=endtime
                Define the termination of a time window to restrict the
                samples retrieved from the input archives; refer to
                PCPIntro(1).

           -v volsamples
                The output archive is potentially a multi-volume data set,
                and the -v option causes pmlogreduce to start a new volume
                after volsamples records have been written to the output
                archive.

                  Independent of any -v option, each volume of an archive is
                  limited to no more than 2^31 bytes, so pmlogreduce will
                  automatically create a new volume for the archive before
                  this limit is reached.

           -z, --hostzone
                Use the local timezone of the host from the input archives
                when displaying the date and time, or interpreting the -S and
                -T options.  The default is to initially use the timezone of
                the local host.

           -Z timezone, --timezone=timezone
                Use timezone when displaying the date and time, or
                interpreting the -S and -T options.  Timezone is in the
                format of the environment variable TZ as described in
                environ(7).

           -?, --help
                Display usage message and exit.

## [](#DATA_REDUCTION)DATA REDUCTION

           The statistical and temporal reduction follows the following
           rules:

           1.  Consecutive records from input are read without interpolation,
               and at most one output record is written for each interval,
               summarizing the performance data over that period.

           2.  If the semantics of a metric indicates it is instantaneous or
               discrete then output value is computed as the arithmetic mean
               of the observations (if any) over each interval.

           3.  If the semantics of a metric indicates it is a counter then
               the following transformations are applied:
               a)  Metrics with 32-bit precision are promoted to 64-bit
                   precision.
               b)  Any counter wrap (overflow) is noted, and appropriate
                   adjustment made in the value of the metric over each
                   interval.  This will be correct in the case of a single
                   counter wrap, but will silently underestimate in the case
                   where more than one counter wrap occurs between
                   consecutive observations in the input archives, and
                   silently overestimate in the case where a counter reset
                   occurs between consecutive observations in the input
                   archives; unfortunately these situations cannot be
                   detected, but are believed to be rare events for the sort
                   of production monitoring environments where pmlogreduce is
                   most likely to be deployed.

           4.  Any changes in instance domains, and indeed all metadata, is
               preserved.

           5.  Any ``mark'' records in the input archives (as created by
               pmlogextract(1)) will be preserved in the output archive, so
               periods where no data is available are maintained, and data
               interpolation will not occur across these periods when the
               output archive is subsequently processed with PCP
               applications.

## [](#CAVEATS)CAVEATS

           The preamble metrics (pmcd.pmlogger.archive, pmcd.pmlogger.host,
           and pmcd.pmlogger.port), which are automatically recorded by
           pmlogger at the start of the archive, may not be present in the
           archive output by pmlogreduce.  These metrics are only relevant
           while the archive is being created, and have no significance once
           recording has finished.

## [](#DIAGNOSTICS)DIAGNOSTICS

           All error conditions detected by pmlogreduce are reported on
           stderr with textual (if sometimes terse) explanation.

           Should the input archives be corrupted (this can happen if the
           pmlogger instance writing the archive suddenly dies), then
           pmlogreduce will detect and report the position of the corruption
           in the file, and any subsequent information from the input
           archives will not be processed.

           If any error is detected, pmlogreduce will exit with a non-zero
           status.

## [](#FILES)FILES

           For each of the input and output archives, several physical files
           are used.

           archive.meta
                metadata (metric descriptions, instance domains, etc.) for
                the archive

           archive.0
                initial volume of metrics values (subsequent volumes have
                suffixes 1, 2, ...) - for input these files may have been
                previously compressed with bzip2(1) or gzip(1) and thus may
                have an additional .bz2 or .gz suffix.

           archive.index
                temporal index to support rapid random access to the other
                files in the archive.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
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

           Debugging options specific to pmlogger are as follows:
           ┌────────┬───────────────────────────────────────────────────────┐
           │ Option │ Description                                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl0  │ initialization and time window                        │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl1  │ report new metric-instance observations               │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl2  │ report scan start and end times, dump input and       │
           │        │ output records                                        │
           └────────┴───────────────────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmlc(1), pmlogdump(1), pmlogextract(1), pmlogger(1),
           pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                     PMLOGREDUCE(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmlogextract(1)](../man1/pmlogextract.1.html),  [pmlogrewrite(1)](../man1/pmlogrewrite.1.html),  [LOGARCHIVE(5)](../man5/LOGARCHIVE.5.html)

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
