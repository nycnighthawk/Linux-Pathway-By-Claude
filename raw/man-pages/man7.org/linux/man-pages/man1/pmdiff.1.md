---
{"title": "pmdiff(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdiff.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdiff(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDIFF(1)                General Commands Manual                PMDIFF(1)

## [](#NAME)NAME

           pmdiff - compares archives and report significant differences

## [](#SYNOPSIS)SYNOPSIS

           pmdiff [-dzV?]  [-B starttime] [-E endtime] [-p precision] [-q
           thres] [-S starttime] [--skip-excluded] [--skip-missing] [-T
           endtime] [-x metric] [-X file] [-Z timezone] archive1 [archive2]

## [](#DESCRIPTION)DESCRIPTION

           pmdiff compares the average values for every metric in either one
           or two sets of archives, in a given time window, for changes that
           are likely to be of interest when searching for performance
           regressions.

           The archive specifiers archive1 and archive2 may be comma-
           separated lists of names, each of which may be the base name of an
           archive or the name of a directory containing one or more
           archives. Each archive in the resulting set of archives must have
           been previously created using pmlogger(1).  The pmlogsummary(1)
           utility is used to obtain the average values used for comparison.

           There are two sorts of invocation of the tool: with either one or
           two sets of archives.

           In the first case, the only sensible command line requires use of
           all four time window arguments.  These are specified using the
           same time window format described in PCPIntro(1), and are
           -S/--start and -T/--finish for the start and end times of the
           first time window of interest in the archive set, and -B/--before
           and -E/--end for the start and end times of the second time window
           of interest.

           In the second case, with two sets of archives, the -B/--before and
           -E/--end options might be unnecessary.  This might be the case,
           for example, when comparing the same time window of two
           consecutive days (usually two separate sets of archives), or a
           time window on the same day of different weeks.

           In either case, pmdiff produces a sorted summary of those metrics
           in the specified window whose values have deviated the most from a
           minimal threshold.  The level of deviation is calculated by
           dividing the average value of each metric in both logs, and then
           calculating whether the ratio falls outside of a range considered
           normal.  This ratio can be adjusted using the -q/--threshold
           option, and by default it is 2 (i.e. report all metrics with
           average values that have more than doubled in the two time windows
           or more than halved in the two time windows).

           If the baseline value is zero and the comparison value is non-
           zero, the ratio is reported as ``|+|'' (infinitely large).  If the
           comparison value is zero and the baseline value is non-zero, the
           ratio is reported as ``|-|'' (infinitely small).

           Reported metrics are sorted in ascending ratio order.

           Should any metrics be present in one window but missing from the
           other, a diagnostic will be displayed listing each missing metric
           and the archive set from which it was missing.

           Metrics with counter semantics are converted to rates before being
           evaluated.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -d, --keep
                Debug mode, keep intermediate files.

           -B time, --begin=time
                Start time for the second time window.

           -E time, --end=time
                End time for the second time window.

           -p precision, --precision=precision
                Print all floating point numbers with precision digits after
                the decimal place.

           -q threshold, --threshold=threshold
                Change the threshold for interesting metrics, see above for
                more details.

           -S time, --start=time
                Start time of the first time window.

           -T time, --finish=time
                End time of the first time window.

           -V, --version
                Display version number and exit.

           -x metric
                Compare each metric in each archive set in the time windows
                specified to a given egrep(1) pattern, excluding those that
                match from the report output.

           -X file
                Allows a file to be specified which containing egrep(1)
                patterns which are applied to the metric names to optionally
                exclude some from the report.

           -z, --hostzone
                Use the local timezone from the given archive set.

           -Z timezone, --timezone=timezone
                Changes the timezone in the archive labels to timezone in the
                format of the environment variable TZ as described in
                environ(7).

           -?, --help
                Display usage message and exit.

           --skip-excluded
                Cull the list of names of metrics being excluded from the
                output.

           --skip-missing
                By default, pmdiff will report the names of any metrics that
                are in one archive set but not the other.  This option
                suppresses that reporting.

## [](#FILES)FILES

           $PCP_LOG_DIR/pmlogger/<hostname>
                Default directory for PCP archives containing performance
                metric values collected from the host hostname.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmlogger(1), pmlogsummary(1), egrep(1), pcp.conf(5)
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

    Performance Co-Pilot               PCP                          PMDIFF(1)

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
