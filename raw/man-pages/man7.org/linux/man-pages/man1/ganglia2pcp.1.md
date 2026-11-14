---
{"title": "ganglia2pcp(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ganglia2pcp.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ganglia2pcp(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                  |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GANGLIA2PCP(1)           General Commands Manual           GANGLIA2PCP(1)

## [](#NAME)NAME

           ganglia2pcp - import ganglia data and create a PCP archive

## [](#SYNOPSIS)SYNOPSIS

           ganglia2pcp [-D debug] [-d outdir] [-e end] [-f outfile] [-h
           hostname] [-s start] [-V version] [-Z timezone] input_dir

## [](#DESCRIPTION)DESCRIPTION

           ganglia2pcp is intended to read a set of ganglia files stored in
           the rrd format and translate them into a Performance Co-Pilot
           (PCP) archive with the basename outfile.

           The intent of this converter is to take all of the rrd files found
           in the input_dir and generate a single pcp archive file.  The
           mapping of ganglia metrics to pcp metrics is defined internally.

           The resultant PCP achive may be used with all the PCP client tools
           to graph subsets of the data using pmchart(1), perform data
           reduction and reporting, filter with the PCP inference engine
           pmie(1), etc.

           A series of physical files will be created with the prefix
           outfile.  These are outfile.0 (the performance data), outfile.meta
           (the metadata that describes the performance data) and
           outfile.index (a temporal index to improve efficiency of replay
           operations for the archive).  If any of these files exists
           already, then sar2pcp will not overwrite them and will exit with
           an error message of the form

           __pmLogNewFile: ``blah.0'' already exists, not over-written

           ganglia2pcp is a Perl script that uses the PCP::LogImport Perl
           wrapper around the PCP libpcp_import library, and as such could be
           used as an example to develop new tools to import other types of
           performance data and create PCP archives.  The RRDs Perl wrapper
           is used to parse the raw rrd format files.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -d outdir
                The outdir argument specifies a output to write to.  The
                default is the current directory.

           -e end
                The end argument specifies a end time in a format understood
                by str2time.  The default start time is current time.

           -f outfile
                The outfile argument specifies a output file name.  The
                default name is in the standard pmlogger format based on the
                start time, e.g., 20150201.00.10.

           -h hostname
                The hostname argument specifies a hostname to write to the
                archive.  The default is taken from the directory name that
                the rrd files reside in.

           -s start
                The start argument specifies a start time in a format
                understood by str2time.  The default start time is 24 prior
                to current time.

           -V version
                The -V option specifies the version for the output PCP
                archive.  By default the archive version $PCP_ARCHIVE_VERSION
                (set to 3 in current PCP releases) is used, and the only
                values currently supported for version are 2 or 3.

           -Z timezone
                The timezone argument sets the source timezone in the PCP
                archive (the default is to use the local timezone).  The
                timezone must have the format +HHMM (for hours and minutes
                East of UTC) or -HHMM (for hours and minutes West of UTC) or
                UTC.  Note in particular that neither the zoneinfo (aka
                Olson) format, e.g. Europe/Paris, nor the Posix TZ format,
                e.g.  EST+5 is allowed.  Example: timezone=``+1100''.

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

           Debugging options specific to ganglia2pcp are as follows:
           ┌────────┬─────────────────────────────┐
           │ Option │ Description                 │
           ├────────┼─────────────────────────────┤
           │ appl0  │ setup and metrics discovery │
           ├────────┼─────────────────────────────┤
           │ appl1  │ metric-value generation     │
           └────────┴─────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           pmie(1), pmchart(1), pmlogger(1), pmlogextract(1),
           pmlogsummary(1), Date::Parse(3pm), Date::Format(3pm),
           PCP::LogImport(3pm), RRDs(3pm) and LOGIMPORT(3).

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

    Performance Co-Pilot               PCP                     GANGLIA2PCP(1)

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
