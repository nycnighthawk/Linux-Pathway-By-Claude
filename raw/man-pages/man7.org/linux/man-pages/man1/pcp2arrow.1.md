---
{"title": "pcp2arrow(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp2arrow.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp2arrow(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION FILE](#CONFIGURATION_FILE) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP2ARROW(1)             General Commands Manual             PCP2ARROW(1)

## [](#NAME)NAME

           pcp2arrow - pcp-to-arrow metrics exporter

## [](#SYNOPSIS)SYNOPSIS

           pcp2arrow [-jLnrRVz?]  [-8|-9 limit] [-a archive] [-A align]
           [--archive-folio folio] [-c config] [--container container] [-D
           debug] [-h host] [-i instances] [-J rank] [-K spec] [-o outfile]
           [-O origin] [-s samples] [-S starttime] [-t interval] [-T endtime]
           [-Z timezone] [metricspec...]

## [](#DESCRIPTION)DESCRIPTION

           pcp2arrow is a customizable performance metrics exporter tool from
           PCP to Apache Arrow.  It is particularly useful as a mechanism for
           producing the Parquet columnar data format, for use with Pandas or
           similar data analysis modules.  Each PCP metric, and each instance
           of each metric, will form a unique column named according to the
           PCP metric specification - that is, metric name followed by square
           bracket enclosed instance name (for metrics with an instance
           domain).

           Any available performance metric, live or archived, system and/or
           application, can be selected for exporting using either command
           line arguments or a configuration file.

           With no metricspec options, all available metrics are considered
           for exporting.

           pcp2arrow is a close relative of pmrep(1).  Refer to pmrep(1) for
           the metricspec description accepted on pcp2arrow command line.
           See pmrep.conf(5) for description of the pcp2arrow.conf
           configuration file syntax.  This page describes pcp2arrow specific
           options and configuration file differences with pmrep.conf(5).
           pmrep(1) also lists some usage examples of which most are
           applicable with pcp2arrow as well.

           Only the command line options listed on this page are supported,
           other options available for pmrep(1) are not supported.

           Options via environment values (see pmGetOptions(3)) override the
           corresponding built-in default values (if any).  Configuration
           file options override the corresponding environment variables (if
           any).  Command line options override the corresponding
           configuration file options (if any).

## [](#CONFIGURATION_FILE)CONFIGURATION FILE

           pcp2arrow uses a configuration file with syntax described in
           pmrep.conf(5).  The following options are common with pmrep.conf:
           version, source, speclocal, derived, header, globals, samples,
           interval, type, type_prefer, ignore_incompat, names_change,
           instances, live_filter, rank, limit_filter, limit_filter_force,
           invert_filter, predicate, omit_flat, include_labels, precision,
           precision_force, count_scale, count_scale_force, space_scale,
           space_scale_force, time_scale, time_scale_force.  The rest of the
           pmrep.conf options are recognized but ignored for compatibility.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -8 limit, --limit-filter=limit
                Limit results to instances with values above/below limit.  A
                positive integer will include instances with values at or
                above the limit in reporting.  A negative integer will
                include instances with values at or below the limit in
                reporting.  A value of zero performs no limit filtering.
                This option will not override possible per-metric
                specifications.  See also -J and -N.

           -9 limit, --limit-filter-force=limit
                Like -8 but this option will override per-metric
                specifications.

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

           --archive-folio=folio
                Read metric source archives from the PCP archive folio
                created by tools like pmchart(1) or, less often, manually
                with mkaf(1).

           -c config, --config=config
                Specify the config file or directory to use.  In case config
                is a directory all files in it ending .conf will be included.
                The default is the first found of: ./pcp2arrow.conf,
                $HOME/.pcp2arrow.conf, $HOME/pcp/pcp2arrow.conf, and
                $PCP_SYSCONF_DIR/pcp2arrow.conf.  For details, see the above
                section and pmrep.conf(5).

           --container=container
                Fetch performance metrics from the specified container,
                either local or remote (see -h).

           -C, --check
                Exit before reporting any values, but after parsing the
                configuration and metrics and printing possible headers.

           -h host, --host=host
                Fetch performance metrics from pmcd(1) on host, rather than
                from the default localhost.

           -H, --no-header
                Do not print any headers.

           -i instances, --instances=instances
                Retrieve and report only the specified metric instances.  By
                default all instances, present and future, are reported.

                Refer to pmrep(1) for complete description of this option.

           -j, --live-filter
                Perform instance live filtering.  This allows capturing all
                named instances even if processes are restarted at some point
                (unlike without live filtering).  Performing live filtering
                over a huge number of instances will add some internal
                overhead so a bit of user caution is advised.  See also -n.

           -J rank, --rank=rank
                Limit results to highest/lowest ranked instances of set-
                valued metrics.  A positive integer will include highest
                valued instances in reporting.  A negative integer will
                include lowest valued instances in reporting.  A value of
                zero performs no ranking.  Ranking does not imply sorting,
                see -6.  See also -8.

           -K spec, --spec-local=spec
                When fetching metrics from a local context (see -L), the -K
                option may be used to control the DSO PMDAs that should be
                made accessible.  The spec argument conforms to the syntax
                described in pmSpecLocalPMDA(3).  More than one -K option may
                be used.

           -L, --local-PMDA
                Use a local context to collect metrics from DSO PMDAs on the
                local host without PMCD.  See also -K.

           -n, --invert-filter
                Perform ranking before live filtering.  By default instance
                live filtering (when requested, see -j) happens before
                instance ranking (when requested, see -J).  With this option
                the logic is inverted and ranking happens before live
                filtering.

           -o outfile, --output-file=outfile
                Specify the output file outfile.  -O origin, --origin=origin
                When reporting archived metrics, start reporting at origin
                within the time window (see -S and -T).  Refer to PCPIntro(1)
                for a complete description of the syntax for origin.

           -r, --raw
                Output raw metric values, do not convert cumulative counters
                to rates.  This option will override possible per-metric
                specifications.

           -R, --raw-prefer
                Like -r but this option will not override per-metric
                specifications.

           -s samples, --samples=samples
                The samples argument defines the number of samples to be
                retrieved and reported.  If samples is 0 or -s is not
                specified, pcp2arrow will sample and report continuously (in
                real time mode) or until the end of the set of PCP archives
                (in archive mode).  See also -T.

           -S starttime, --start=starttime
                When reporting archived metrics, the report will be
                restricted to those records logged at or after starttime.
                Refer to PCPIntro(1) for a complete description of the syntax
                for starttime.

           -t interval, --interval=interval
                Set the reporting interval to something other than the
                default 1 second.  The interval argument follows the syntax
                described in PCPIntro(1), and in the simplest form may be an
                unsigned integer (the implied units in this case are
                seconds).  See also the -T option.

           -T endtime, --finish=endtime
                When reporting archived metrics, the report will be
                restricted to those records logged before or at endtime.
                Refer to PCPIntro(1) for a complete description of the syntax
                for endtime.

                When used to define the runtime before pcp2arrow will exit,
                if no samples is given (see -s) then the number of reported
                samples depends on interval (see -t).  If samples is given
                then interval will be adjusted to allow reporting of samples
                during runtime.  In case all of -T, -s, and -t are given,
                endtime determines the actual time pcp2arrow will run.

           -v, --omit-flat
                Report only set-valued metrics with instances (e.g.
                disk.dev.read) and omit single-valued ``flat'' metrics
                without instances (e.g.  kernel.all.sysfork).  See -i and -I.

           -V, --version
                Display version number and exit.

           -z, --hostzone
                Use the local timezone of the host that is the source of the
                performance metrics, as identified by either the -h or the -a
                options.  The default is to use the timezone of the local
                host.

           -Z timezone, --timezone=timezone
                Use timezone for the date and time.  Timezone is in the
                format of the environment variable TZ as described in
                environ(7).  Note that when including a timezone string in
                output, ISO 8601 -style UTC offsets are used (so something
                like -Z EST+5 will become UTC-5).

           -?, --help
                Display usage message and exit.

## [](#FILES)FILES

           pcp2arrow.conf
                pcp2arrow configuration file (see -c)

           $PCP_SYSCONF_DIR/pmrep/*.conf
                system provided default pmrep configuration files

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

           Of particular note, PCP_DISCRETE_ONCE can be set to ensure that
           discrete metric values are reported only once, unless they change
           at some point.

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), mkaf(1), pcp(1), pmcd(1), pminfo(1), pmrep(1),
           pmGetOptions(3), pmSpecLocalPMDA(3), LOGARCHIVE(5), pcp.conf(5),
           pmrep.conf(5), PMNS(5) and environ(7).

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

    Performance Co-Pilot               PCP                       PCP2ARROW(1)

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
