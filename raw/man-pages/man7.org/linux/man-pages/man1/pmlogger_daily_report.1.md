---
{"title": "pmlogger_daily_report(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmlogger_daily_report.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmlogger_daily_report(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOGGER_DAILY_REPORT(1) General Commands Manual PMLOGGER_DAILY_REPORT(1)

## [](#NAME)NAME

           pmlogger_daily_report - write Performance Co-Pilot daily summary
           reports

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmlogger_daily_report [-ApV?]  [-a archivefile]
           [-f outputfile] [-h hostname] [-l logfile] [-o directory] [-t
           interval]

## [](#DESCRIPTION)DESCRIPTION

           pmlogger_daily_report writes daily performance summary reports,
           much like those produced by sadc(1) and the sa2(8) utility.

           All of the command line arguments are optional and intended to be
           self explanatory.

           By default, the reports are not generated, but if the pcp-zeroconf
           package has been installed (there will be files in
           $PCP_VAR_DIR/config/pmlogconf/zeroconf) then the necessary metrics
           will have been included in the default pmlogger(1) configuration
           file and the reports will be generated.

           The reports are generated (by default) soon after midnight, once
           pmlogger_daily(1) has completed the merging of any partial
           archives to generate one archive for yesterday's activity.

           Each performance summary report is named sarXX (where XX is
           yesterdays day-of-the-month).  The outputfile may be changed with
           the -f option.  The report will be written to the $PCP_LOG_DIR/sa
           directory by default, but this may be changed with the -o option
           to a different directory.

           Note that there are sufficiently flexible command line options for
           pmlogger_daily_report to be used to read any archivefile and write
           the report to any output directory.

           If the -a option is not given, the default input archivefile is
           $PCP_ARCHIVE_DIR/HOSTNAME/YYYYMMDD, where HOSTNAME defaults to the
           local hostname (unless changed with the -h option) and YYYYMMDD is
           the base name of yesterdays merged archive, as produced by
           pmlogger(1) and pmlogger_daily(1).  If archivefile is a directory,
           then pmlogger_daily_report will use all PCP archives found in that
           directory to write the report (this is known as multi-archive
           mode, and may be considerably slower than specifying a single
           archive as the input).

           The reports themselves are created by the pmrep(1) utility using
           its default configuration file, see pmrep.conf(5).  The pmrep(1)
           configuration entries used to write the reports is currently
           hardwired into the pmlogger_daily_report script.

           Finally, the input archives must contain sufficient metrics as
           needed by pmrep(1) to write the report.  On platforms that support
           it, the pcp-zeroconf package configures PCP logging as required
           for this - hence pmlogger_daily_report should be used with the
           pmlogger(1) configuration that is set up by pcp-zeroconf.  As the
           name suggests, pcp-zeroconf requires no additional configuration
           after installation in order to capture the required archives
           needed by pmlogger_daily_report.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -a archive
                Specifies an alternate input archive file basename or
                directory path.

           -A   Use the start and end times of input archive for the report,
                as opposed to the default behaviour of 24 hours from midnight
                yesterday.

           -f filename
                Specifies an alternate output filename.  -h hostname
                Specifies an alternate hostname to use within the default
                input archive file path.

           -l file, --logfile=file
                In order to ensure that mail is not unintentionally sent when
                this script is run from pmlogger_daily(1) diagnostics are
                always sent to a log file.  By default, this file is
                $PCP_LOG_DIR/pmlogger/pmlogger_daily_report.log but this can
                be changed using the -l option.  If this log file already
                exists when the script starts, it will be renamed with a
                .prev suffix (overwriting any log file saved earlier) before
                diagnostics are generated to the log file.

           -p   If this option is specified then the status of the daily
                processing is polled and if the report has not been done in
                the last 24 hours then it is done now.  With this option,
                pmlogger_daily_report simply exits if the previous day's
                processing has already been done.

                This option is no longer required as the polling of
                pmlogger_daily(1) will ensure the report will be generated,
                however the option is retained for backwards compatibility.

           -t interval
                Specifies the sampling interval used when generating the
                report, in the format described in PCPIntro(1).  The default
                is every 10 minutes.

           -V, --verbose
                The output from the execution of the script may be extended
                using this option which enables verbose tracing of activity.
                By default the script generates no log output unless some
                error or warning condition is encountered.

           -?, --help
                Display usage message and exit.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmlogger_daily(1), pmlogger(1), pmrep(1), sadc(1) and
           sa2(8).

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

    Performance Co-Pilot               PCP           PMLOGGER_DAILY_REPORT(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmlogger_check(1)](../man1/pmlogger_check.1.html),  [pmlogger_daily(1)](../man1/pmlogger_daily.1.html),  [pmlogger.control(5)](../man5/pmlogger.control.5.html)

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
