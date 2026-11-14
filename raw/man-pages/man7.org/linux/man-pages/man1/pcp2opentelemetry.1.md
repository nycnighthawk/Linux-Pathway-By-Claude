---
{"title": "pcp2opentelemetry(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp2opentelemetry.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp2opentelemetry(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION FILE](#CONFIGURATION_FILE) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP2OPENTELEMETRY(1)     General Commands Manual     PCP2OPENTELEMETRY(1)

## [](#NAME)NAME

           pcp2opentelemetry - pcp-to-opentelemetry exporter

## [](#SYNOPSIS)SYNOPSIS

           pcp2opentelemetry [-5CEGHIjLmnrRvVxXz?]  [-4 action] [-8|-9 limit]
           [-a archive] [-A align] [--archive-folio folio] [-b|-B space-
           scale] [-c config] [--container container] [-D debug]
           [--daemonize] [-e derived] [-f format] [-F outfile] [-h host] [-i
           instances] [-J rank] [-K spec] [-N predicate] [-o timeout] [-O
           origin] [-p password] [-P|-0 precision] [-q|-Q count-scale] [-s
           samples] [-S starttime] [-t interval] [-T endtime] [-u url] [-U
           username] [-y|-Y time-scale] [-Z timezone] metricspec [...]

## [](#DESCRIPTION)DESCRIPTION

           pcp2opentelemetry is a customizable performance metrics exporter
           tool from PCP to OpenTelemetry - https://opentelemetry.io  -
           format.  Any available performance metric, live or archived,
           system and/or application, can be selected for exporting using
           either command line arguments or a configuration file.

           pcp2opentelemetry is a close relative of pmrep(1).  Refer to
           pmrep(1) for the metricspec description accepted on
           pcp2opentelemetry command line.  See pmrep.conf(5) for description
           of the pcp2opentelemetry.conf configuration file syntax.  This
           page describes pcp2opentelemetry specific options and
           configuration file differences with pmrep.conf(5).  pmrep(1) also
           lists some usage examples of which most are applicable with
           pcp2opentelemetry as well.

           Only the command line options listed on this page are supported,
           other options available for pmrep(1) are not supported.

           Options via environment values (see pmGetOptions(3)) override the
           corresponding built-in default values (if any).  Configuration
           file options override the corresponding environment variables (if
           any).  Command line options override the corresponding
           configuration file options (if any).

## [](#CONFIGURATION_FILE)CONFIGURATION FILE

           pcp2opentelemetry uses a configuration file with syntax described
           in pmrep.conf(5).  The following options are common with
           pmrep.conf: version, source, speclocal, derived, header, globals,
           samples, interval, type, type_prefer, ignore_incompat,
           names_change, instances, live_filter, rank, limit_filter,
           limit_filter_force, invert_filter, predicate, omit_flat,
           include_labels, precision, precision_force, count_scale,
           count_scale_force, space_scale, space_scale_force, time_scale,
           time_scale_force.  The rest of the pmrep.conf options are
           recognized but ignored for compatibility.

       pcp2opentelemetry specific options
           url (string)
               Send OpenTelemetry output as a HTTP POST to the given url.
               Corresponding command line option is -u.  Defaults to None.

           http_pass (string)
               Use given password for Basic Authentication when sending a
               HTTP POST.  Corresponding command line option is -p.  Defaults
               to None.

           http_user (string)
               Use given username for Basic Authentication when sending a
               HTTP POST.  Corresponding command line option is -U.  Defaults
               to None.

           http_timeout (number)
               Maximum time (in seconds) when sending a HTTP POST.
               Corresponding command line option is -o.  Defaults to 2.5
               seconds.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -0 precision, --precision-force=precision
                Like -P but this option will override per-metric
                specifications.

           -4 action, --names-change=action
                Specify which action to take on receiving a metric names
                change event during sampling.  These events occur when a PMDA
                discovers new metrics sometime after starting up, and informs
                running client tools like pcp2opentelemetry.  Valid values
                for action are update (refresh metrics being sampled), ignore
                (do nothing - the default behaviour) and abort (exit the
                program if such an event occurs).

           -5, --ignore-unknown
                Silently ignore any metric name that cannot be resolved.  At
                least one metric must be found for the tool to start.

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

           -b scale, --space-scale=scale
                Unit/scale for space (byte) metrics, possible values include
                bytes, Kbytes, KB, Mbytes, MB, and so forth.  This option
                will not override possible per-metric specifications.  See
                also pmParseUnitsStr(3).

           -B scale, --space-scale-force=scale
                Like -b but this option will override per-metric
                specifications.

           -c config, --config=config
                Specify the config file or directory to use.  In case config
                is a directory all files in it ending .conf will be included.
                The default is the first found of: ./pcp2opentelemetry.conf,
                $HOME/.pcp2opentelemetry.conf,
                $HOME/pcp/pcp2opentelemetry.conf, and
                $PCP_SYSCONF_DIR/pcp2opentelemetry.conf.  For details, see
                the above section and pmrep.conf(5).

           --container=container
                Fetch performance metrics from the specified container,
                either local or remote (see -h).

           -C, --check
                Exit before reporting any values, but after parsing the
                configuration and metrics and printing possible headers.

           --daemonize
                Daemonize on startup.

           -e derived, --derived=derived
                Specify derived performance metrics.  If derived starts with
                a slash (``/'') or with a dot (``.'') it will be interpreted
                as a PCP derived metrics configuration file, otherwise it
                will be interpreted as comma- or semicolon-separated derived
                metric expressions.  For complete description of derived
                metrics and PCP derived metrics configuration files see
                pmLoadDerivedConfig(3) and pmRegisterDerived(3).
                Alternatively, using pmrep.conf(5) configuration syntax
                allows defining derived metrics as part of metricsets.

           -E, --exact-types
                Write numbers as number data types, not as strings,
                potentially losing some precision.

           -f format, --timestamp-format=format
                Use the format string for formatting the timestamp.  The
                format will be used with Python's datetime.strftime method
                which is mostly the same as that described in strftime(3).
                The default is %Y-%m-%d %H:%M:%S.

           -F outfile, --output-file=outfile
                Specify the output file outfile.

           -G, --no-globals
                Do not include global metrics in reporting (see
                pmrep.conf(5)).

           -h host, --host=host
                Fetch performance metrics from pmcd(1) on host, rather than
                from the default localhost.

           -H, --no-header
                Do not print any headers.

           -i instances, --instances=instances
                Retrieve and report only the specified metric instances.  By
                default all instances, present and future, are reported.

                Refer to pmrep(1) for complete description of this option.

           -I, --ignore-incompat
                Ignore incompatible metrics.  By default incompatible metrics
                (that is, their type is unsupported or they cannot be scaled
                as requested) will cause pcp2opentelemetry to terminate with
                an error message.  With this option all incompatible metrics
                are silently omitted from reporting.  This may be especially
                useful when requesting non-leaf nodes of the PMNS tree for
                reporting.

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

           -m, --include-labels
                Include PCP metric labels in the output.

           -N predicate, --predicate=predicate
                Specify a comma-separated list of predicate filter reference
                metrics.  By default ranking (see -J) happens for each metric
                individually.  With predicates, ranking is done only for the
                specified predicate metrics.  When reporting, rest of the
                metrics sharing the same instance domain (see PCPIntro(1)) as
                the predicate will include only the highest/lowest ranking
                instances of the corresponding predicate.  Ranking does not
                imply sorting, see -6.

                So for example, using proc.memory.rss (resident memory size
                of process) as the predicate metric together with
                proc.io.total_bytes and mem.util.used as metrics to be
                reported, only the processes using most/least (as per -J)
                memory will be included when reporting total bytes written by
                processes.  Since mem.util.used is a single-valued metric
                (thus not sharing the same instance domain as the process
                related metrics), it will be reported as usual.

           -o, --http-timeout
                Timeout (in seconds) when sending a HTTP POST with the -u
                option.  Default value is 2.5 seconds.

           -O origin, --origin=origin
                When reporting archived metrics, start reporting at origin
                within the time window (see -S and -T).  Refer to PCPIntro(1)
                for a complete description of the syntax for origin.

           -p, --http-pass
                Password when using HTTP basic authentication with the -u
                option.

           -P precision, --precision=precision
                Use precision for numeric non-integer output values.  The
                default is to use 3 decimal places (when applicable).  This
                option will not override possible per-metric specifications.

           -q scale, --count-scale=scale
                Unit/scale for count metrics, possible values include count x
                10^-1, count, count x 10, count x 10^2, and so forth from
                10^-8 to 10^7.  (These values are currently space-sensitive.)
                This option will not override possible per-metric
                specifications.  See also pmParseUnitsStr(3).

           -Q scale, --count-scale-force=scale
                Like -q but this option will override per-metric
                specifications.

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
                specified, pcp2opentelemetry will sample and report
                continuously (in real time mode) or until the end of the set
                of PCP archives (in archive mode).  See also -T.

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

                When used to define the runtime before pcp2opentelemetry will
                exit, if no samples is given (see -s) then the number of
                reported samples depends on interval (see -t).  If samples is
                given then interval will be adjusted to allow reporting of
                samples during runtime.  In case all of -T, -s, and -t are
                given, endtime determines the actual time pcp2opentelemetry
                will run.

           -u, --url
                URL for sending an HTTP POST (instead of default standard
                output).

           -U, --http-user
                Username when using HTTP basic authentication with the -u
                option.

           -v, --omit-flat
                Report only set-valued metrics with instances (e.g.
                disk.dev.read) and omit single-valued ``flat'' metrics
                without instances (e.g.  kernel.all.sysfork).  See -i and -I.

           -V, --version
                Display version number and exit.

           -x, --with-extended
                Write extended information.

           -X, --with-everything
                Write everything known about metrics, including PCP internal
                IDs.  Labels are, however, omitted for backward
                compatibility, use -m to include them as well.

           -y scale, --time-scale=scale
                Unit/scale for time metrics, possible values include nanosec,
                ns, microsec, us, millisec, ms, and so forth up to hour, hr.
                This option will not override possible per-metric
                specifications.  See also pmParseUnitsStr(3).

           -Y scale, --time-scale-force=scale
                Like -y but this option will override per-metric
                specifications.

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

           pcp2opentelemetry.conf
                pcp2opentelemetry configuration file (see -c)

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

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), mkaf(1), pcp(1), pcp2elasticsearch(1),
           pcp2graphite(1), pcp2influxdb(1), pcp2openmetrics(1),
           pcp2spark(1), pcp2xlsx(1), pcp2xml(1), pcp2json(1), pcp2zabbix(1),
           pmcd(1), pminfo(1), pmrep(1), pmGetOptions(3),
           pmLoadDerivedConfig(3), pmParseUnitsStr(3), pmRegisterDerived(3),
           pmSpecLocalPMDA(3), LOGARCHIVE(5), pcp.conf(5), pmrep.conf(5),
           PMNS(5) and environ(7).

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

    Performance Co-Pilot               PCP               PCP2OPENTELEMETRY(1)

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
