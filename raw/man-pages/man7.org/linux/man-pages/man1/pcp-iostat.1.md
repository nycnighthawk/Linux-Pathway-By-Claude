---
{"title": "pcp-iostat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-iostat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-iostat(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [REPORT](#REPORT) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                       |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-IOSTAT(1)            General Commands Manual            PCP-IOSTAT(1)

## [](#NAME)NAME

           pmiostat, pcp-iostat - report block I/O statistics

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options] iostat [-u?]  [-G method] [-P precision] [-R
           pattern] [-x [dm][,t][,h][,noidle]]

## [](#DESCRIPTION)DESCRIPTION

           pcp-iostat reports I/O statistics for SCSI (by default) or other
           devices (if the -x option is specified).

## [](#OPTIONS)OPTIONS

           When invoked via the pcp(1) command, the pcp options -A/--align,
           -a/--archive, -h/--host, -O/--origin, -S/--start, -s/--samples,
           -T/--finish, -t/--interval, -v/--version, -Z/--timezone and
           -z/--hostzone become indirectly available; refer to PCPIntro(1)
           for a complete description of these options.

           The additional command line options available for pcp-iostat are:

           -G method, --aggregate=method
                Specifies that statistics for device names matching the regu‐
                lar expression specified with the -R regex option should be
                aggregated according to method.  Note this is aggregation
                based on matching device names (not temporal aggregation).
                When -G is used, the device name column is reported as
                method(regex), e.g.  if -G sum -R 'sd(a|b)$' is specified,
                the device column will be sum(sd(a|b)$) and summed statistics
                for sda and sdb will be reported in the remaining columns.
                If -G is specified but -R is not specified, then the default
                regex is .*, i.e. matching all device names.  If method is
                sum then the statistics are summed.  This includes the %util
                column, which may therefore exceed 100% if more than one de‐
                vice name matches.  If method is avg then the statistics are
                summed and then averaged by dividing by the number of match‐
                ing device names.  If method is min or max, the minimum or
                maximum statistics for matching devices are reported, respec‐
                tively.

           -P N, --precision=N
                This indicates the precision (number of decimal places) to
                report.  The default precision N may be set to something oth‐
                er than the default (2).  Note that the avgrq-sz and avgqu-sz
                fields are always reported with N+1 decimals of precision.
                These fields typically have values less than 1.

           -R pattern, --regex=pattern
                This restricts the report to device names matching a regular
                expression pattern.  The given pattern is searched as a perl
                style regular expression, and will match any portion of a de‐
                vice name.  e.g. '^sd[a-zA-Z]+' will match all device names
                starting with 'sd' followed by one or more alphabetic charac‐
                ters.  e.g. '^sd(a|b)$' will only match 'sda' and 'sdb'.
                e.g. 'sda$' will match 'sda' but not 'sdab'.  See also the -G
                option for aggregation options.

           -u, --no-interpolation
                When replaying a set of archives, by default values are re‐
                ported according to the requested sample interval (-t op‐
                tion), not according to the actual interval recorded in the
                archive(s).  Without this option PCP interpolates the values
                to be reported based on the records in the set of archives,
                which is particularly useful when the -t option is used to
                replay a set of archives with a longer sampling interval than
                that with which the archive(s) was originally recorded with.
                With the -u option, uninterpolated reporting is enabled -
                every value is reported according to the native recording in‐
                terval in the set of archives.  When the -u option is speci‐
                fied, the -t option makes no sense and is incompatible be‐
                cause the replay interval is always the same as the recording
                interval in the set of archive.  In addition, -u only makes
                sense when replaying archives, see the -a option on
                PCPIntro(1), and so if -u is specified then -a must also be
                specified.

           -V, --version
                Display version number and exit.

           -x comma-separated-options
                Specifies a comma-separated list of one or more extended re‐
                porting options as follows:
                dm - report statistics for device-mapper logical devices in‐
                stead of SCSI devices,
                t - prefix every line in the report with a timestamp in
                ctime(3) format,
                h - omit the heading, which is otherwise reported every 24
                samples,
                noidle - Do not display statistics for idle devices.

           -?, --help
                Display usage message and exit.

## [](#REPORT)REPORT

           The columns in the pcp-iostat report have the following interpre‐
           tation:

           Timestamp
                  When the -x t option is specified, this column is the time‐
                  stamp in ctime(3) format.

           Device Specifies the scsi device name, or if -x dm is specified,
                  the device-mapper logical device name.  When -G is speci‐
                  fied, this is replaced by the aggregation method and regu‐
                  lar expression - see the -G and -R options above.

           rrqm/s The number of read requests expressed as a rate per-second
                  that were merged during the reporting interval by the I/O
                  scheduler.

           wrqm/s The number of write requests expressed as a rate per-second
                  that were merged during the reporting interval by the I/O
                  scheduler.

           r/s    The number of read requests completed by the device (after
                  merges), expressed as a rate per second during the report‐
                  ing interval.

           w/s    The number of write requests completed by the device (after
                  merges), expressed as a rate per second during the report‐
                  ing interval.

           rkB/s  The average volume of data read from the device expressed
                  as KBytes/second during the reporting interval.

           wkB/s  The average volume of data written to the device expressed
                  as KBytes/second during the reporting interval.

           avgrq-sz
                  The average I/O request size for both reads and writes to
                  the device expressed as Kbytes during the reporting inter‐
                  val.

           avgqu-sz
                  The average queue length of read and write requests to the
                  device during the reporting interval.

           await  The average time in milliseconds that read and write re‐
                  quests were queued (and serviced) to the device during the
                  reporting interval.

           r_await
                  The average time in milliseconds that read requests were
                  queued (and serviced) to the device during the reporting
                  interval.

           w_await
                  The average time in milliseconds that write requests were
                  queued (and serviced) to the device during the reporting
                  interval.

           %util  The percentage of time during the reporting interval that
                  the device was busy processing requests.  A value of 100%
                  indicates device saturation.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to parameter‐
           ize the file and directory names used by PCP.  On each installa‐
           tion, the file /etc/pcp.conf contains the local values for these
           variables.  The $PCP_CONF variable may be used to specify an al‐
           ternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug pcp option enables the output of additional di‐
           agnostics on stderr to help triage problems, although the informa‐
           tion is sometimes cryptic and primarily intended to provide guid‐
           ance for developers rather end-users.  debug is a comma separated
           list of debugging options; use pmdbg(1) with the -l option to ob‐
           tain a list of the available debugging options and their meaning.

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pcp(1), iostat2pcp(1), pmcd(1), pmchart(1),
           pmlogger(1), pcp.conf(5) and pcp.env(5).

## [](#COLOPHON)COLOPHON

           This page is part of the PCP (Performance Co-Pilot) project.  In‐
           formation about the project can be found at ⟨http://www.pcp.io/⟩.
           If you have a bug report for this manual page, send it to
           pcp@groups.io.  This page was obtained from the project's upstream
           Git repository ⟨https://github.com/performancecopilot/pcp.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-08-04.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    Performance Co-Pilot               PCP                      PCP-IOSTAT(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmrep(1)](../man1/pmrep.1.html)

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
