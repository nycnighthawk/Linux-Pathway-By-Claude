---
{"title": "pcp-tapestat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-tapestat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-tapestat(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [REPORT](#REPORT) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                       |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-TAPESTAT(1)          General Commands Manual          PCP-TAPESTAT(1)

## [](#NAME)NAME

           pcp-tapestat - report tape I/O statistics

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options] tapestat [-u?]  [-G method] [-P precision] [-R
           pattern] [-x [t][,h][,noidle]]

## [](#DESCRIPTION)DESCRIPTION

           pcp-tapestat reports I/O statistics for tape devices.

## [](#OPTIONS)OPTIONS

           When invoked via the pcp(1) command, the pcp options -A/--align,
           -a/--archive, -h/--host, -O/--origin, -S/--start, -s/--samples,
           -t/--interval, -T/--finish, -V/--version, -Z/--timezone and
           -z/--hostzone become indirectly available; refer to PCPIntro(1)
           for a complete description of these options.

           The additional command line options available for pcp-tapestat
           are:

           -G method, --aggregate=method
                Specifies that statistics for device names matching the
                regular expression specified with the -R regex option should
                be aggregated according to method.  Note this is aggregation
                based on matching device names (not temporal aggregation).
                When -G is used, the device name column is reported as
                method(regex), e.g.  if -G sum -R 'st(0|1)$' is specified,
                the device column will be sum(st(0|1)$) and summed statistics
                for st0 and st1 will be reported in the remaining columns.
                If -G is specified but -R is not specified, then the default
                regex is .*, i.e. matching all device names.  If method is
                sum then the statistics are summed.  If method is avg then
                the statistics are summed and then averaged by dividing by
                the number of matching device names.  If method is min or
                max, the minimum or maximum statistics for matching devices
                are reported, respectively.

           -P N, --precision=N
                This indicates the precision (number of decimal places) to
                report.  The default precision N may be set to something
                other than the default (2).  Note that the avgrq-sz and
                avgqu-sz fields are always reported with N+1 decimals of
                precision.  These fields typically have values less than 1.

           -R pattern, --regex=pattern
                This restricts the report to device names matching a regular
                expression pattern.  The given pattern is searched as a perl
                style regular expression, and will match any portion of a
                device name.  e.g. '^st[0-9]+' will match all device names
                starting with 'st' followed by one or more numbers.  e.g.
                '^st(0|1)$' will only match 'st0' and 'st1'.  e.g. 'st0$'
                will match 'st0' but not 'st1'.  See also the -G option for
                aggregation options.

           -u, --no-interpolation
                When replaying a set of archives, by default values are
                reported according to the requested sample interval (-t
                option), not according to the actual interval recorded in the
                archive(s).  Without this option PCP interpolates the values
                to be reported based on the records in the set of archives,
                which is particularly useful when the -t option is used to
                replay a set of archives with a longer sampling interval than
                that with which the archive(s) was originally recorded with.
                With the -u option, uninterpolated reporting is enabled -
                every value is reported according to the native recording
                interval in the set of archives.  When the -u option is
                specified, the -t option makes no sense and is incompatible
                because the replay interval is always the same as the
                recording interval in the set of archive.  In addition, -u
                only makes sense when replaying archives, see the -a option
                on PCPIntro(1), and so if -u is specified then -a must also
                be specified.

           -V, --version
                Display version number and exit.

           -x comma-separated-options
                Specifies a comma-separated list of one or more extended
                reporting options as follows:
                t - prefix every line in the report with a timestamp in
                ctime(3) format,
                h - omit the heading, which is otherwise reported every 24
                samples,
                noidle - Do not display statistics for idle devices.

           -?, --help
                Display usage message and exit.

## [](#REPORT)REPORT

           The columns in the pcp-tapestat report have the following
           interpretation:

           Timestamp
                  When the -x t option is specified, this column is the
                  timestamp in ctime(3) format.

           Device Specifies the tape device name.  When -G is specified, this
                  is replaced by the aggregation method and regular
                  expression - see the -G and -R options above.

           r/s    The number of reads issued expressed as the number per
                  second averaged over the interval.

           w/s    The number of writes issued expressed as the number per
                  second averaged over the interval.

           kb_r/s The amount of data read expressed in kilobytes per second
                  averaged over the interval.

           kb_w/s The amount of data written expressed in kilobytes per
                  second averaged over the interval.

           r_pct  Read percentage wait - the percentage of time over the
                  interval spent waiting for read requests to complete.  The
                  time is measured from when the request is dispatched to the
                  SCSI mid-layer until it signals that it completed.

           w_pct  Write percentage wait - the percentage of time over the
                  interval spent waiting for write requests to complete.  The
                  time is measured from when the request is dispatched to the
                  SCSI mid-layer until it signals that it completed.

           o_pct  Overall percentage wait - the percentage of time over the
                  interval spent waiting for any I/O request to complete
                  (read, write, and other).

           Rs/s   The number of I/Os, expressed as the number per second
                  averaged over the interval, where a non-zero residual value
                  was encountered.

           o_cnt  The  number of I/Os, expressed as the number per second
                  averaged over the interval, that were included as "other".
                  Other I/O includes ioctl calls made to the tape driver and
                  implicit operations performed by the tape driver such as
                  rewind on close (for tape devices that implement rewind on
                  close).  It does not include any I/O performed using
                  methods outside of the tape driver (e.g. via sg ioctls).

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug pcp option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pcp(1), pmcd(1), pmchart(1), pmlogger(1), pcp.conf(5)
           and pcp.env(5).

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

    Performance Co-Pilot               PCP                    PCP-TAPESTAT(1)

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
