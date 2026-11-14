---
{"title": "pmprobe(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmprobe.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmprobe(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                              |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMPROBE(1)               General Commands Manual               PMPROBE(1)

## [](#NAME)NAME

           pmprobe - lightweight probe for performance metrics

## [](#SYNOPSIS)SYNOPSIS

           pmprobe [-dfFiILvVz?]  [-a archive] [-b batchsize]
           [--container=name] [-D debug] [--derived=file] [-h hostname] [-K
           spec] [-n pmnsfile] [-O time] [-Z timezone] [metricname ...]

## [](#DESCRIPTION)DESCRIPTION

           pmprobe determines the availability of performance metrics
           exported through the facilities of the Performance Co-Pilot (PCP).

           The metrics of interest are named in the metricname arguments.  If
           metricname is a non-leaf node in the Performance Metrics Name
           Space (PMNS(5)), then pmprobe will recursively descend the PMNS
           and report on all leaf nodes.  If no metricname argument is given,
           the root of the namespace is used.

           This recursive expansion of the PMNS can be inhibited by the -F
           (go faster) option, which reduces the number of roundtrips to
           pmcd(1) when the metricname arguments are known to be leaf nodes
           ahead of time.

           The output format is spartan and intended for use in wrapper
           scripts creating configuration files for other PCP tools.  By
           default, there is one line of output per metric, with the metric
           name followed by a count of the number of available values.  Error
           conditions are encoded as a negative value count (as per the
           PMAPI(3) protocols, but may be decoded using pmerr(1)) and
           followed by a textual description of the error.

           Unless directed to another host by the -h option, pmprobe will
           contact the Performance Metrics Collector Daemon (PMCD) on the
           local host.

           The -a option causes pmprobe to use the specified set of archives
           rather than connecting to a PMCD.

           The -L option causes pmprobe to use a local context to collect
           metrics from PMDAs on the local host without PMCD.  Only some
           metrics are available in this mode.

           The -a, -h and -L options are mutually exclusive.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -a archive, --archive=archive
                Performance metric values are retrieved from the set of
                Performance Co-Pilot (PCP) archive files identified by the
                archive argument, which is a comma-separated list of names,
                each of which may be the base name of an archive or the name
                of a directory containing one or more archives.

           -b, --batch
                This option may be used to define the maximum number of
                metrics to be fetched in a single request for the -v option
                and any pmLookupName(3) request that pmprobe calls with a
                list of leaf metric names.  The default value for batchsize
                is 128.  This option is useful to avoid limitations on PDU
                request sizes and also to stagger fetches, which may
                otherwise timeout if pmcd(1) or a PMDA is slow to respond,
                particularly if a large number of metrics are probed.

           --container=container
                Specify an individual container to be queried.

           -d, --version
                Display version number and exit.

           --derived=dmfile
                The dmfile argument specifies a file that contains derived
                metric definitions in the format described for
                pmLoadDerivedConfig(3).  This option provides a way to load
                derived metric definitions that is an alternative to the more
                generic use of the PCP_DERIVED_CONFIG environment variable as
                described in PCPIntro(1).  Using the --derived option and the
                PCP_DERIVED_CONFIG environment variable to specify the same
                configuration is a bad idea, so choose one or the other
                method.

           -f, --force
                When used with -i or -I the set of instances reported will be
                all of those known at the source of the performance data.  By
                default the set of reported instances are those for which
                values are currently available, which may be smaller than the
                set reported with -f.

           -F, --faster
                Assume given metric names are PMNS leaf nodes.

           -h host, --host=host
                Connect to pmcd(1) on host, rather than on the default
                localhost.

           -i, --internal
                Report the internal identifiers for each instance.  The
                values are in decimal and prefixed by ``?''.  As a special
                case, the literal string PM_IN_NULL is reported for singular
                metrics.

           -I, --external
                Report the external identifiers for each instance.  The
                literal string PM_IN_NULL is reported for singular metrics.

           -K spec, --spec-local=spec
                When using the -L/ option to fetch metrics from a local
                context, this option controls the DSO PMDAs that should be
                made accessible.  The spec argument conforms to the syntax
                described in pmSpecLocalPMDA(3).  More than one -K option may
                be used.

           -L, --local-PMDA
                Use a local context to collect metrics from DSO PMDAs on the
                local host without PMCD.  See also -K.

           -n pmnsfile, --namespace=pmnsfile
                Normally pmprobe operates on the distributed Performance
                Metrics Name Space (PMNS), however, if the -n option is
                specified an alternative local PMNS file is loaded from the
                file pmnsfile.

           -O time, --origin=time
                When used in conjunction with an archive source of metrics
                and the options -f/, the time argument defines a time origin
                at which the metrics should be fetched from the set of
                archives.  Refer to PCPIntro(1) for a complete description of
                this option, and the syntax for the time argument.

           -v, --values
                Report the value for each instance, as per the formatting
                rules of pmPrintValue(3).  When fetching from a set of
                archives, only those instances present in the first archive
                record for a metric will be displayed; see also the -O
                option.  The -v option is mutually exclusive with either the
                -I or -i options.

           -V, --verbose
                This option provides a cryptic summary of the number of
                messages sent and received across the PMAPI interface.

           -z, --hostzone
                Change the reporting timezone to the local timezone at the
                host that is the source of the performance metrics, as
                identified via either the -h or -a options.

           -Z timezone, --timezone=timezone
                By default, pmprobe reports the time of day according to the
                local timezone on the system where pmprobe is run.  The -Z
                option changes the timezone to timezone in the format of the
                environment variable TZ as described in environ(7).

           -?, --help
                Display usage message and exit.

## [](#EXAMPLES)EXAMPLES

           $ pmprobe disk.dev
           disk.dev.read 2
           disk.dev.write 2
           disk.dev.total 2
           disk.dev.blkread 2
           disk.dev.blkwrite 2
           disk.dev.blktotal 2
           disk.dev.active 2
           disk.dev.response 2

           $ pmprobe -I disk.dev.read disk.dev.write disk.all.total
           disk.dev.read 2 "sda" "sdb"
           disk.dev.write 2 "sda" "sdb"
           disk.all.total 1 PM_IN_NULL

           $ pmprobe -v pmcd.numagents pmcd.version pmcd.control.timeout
           pmcd.numagents 1 9
           pmcd.version 1 "5.0.0"
           pmcd.control.timeout 1 5

           $ pmprobe -v disk.dev.total disk.all.total
           disk.dev.total -1012 Unknown metric name
           disk.all.total 1 4992466

## [](#FILES)FILES

           $PCP_VAR_DIR/pmns/*
                default PMNS specification files

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

           Debugging options specific to pmprobe are as follows:
           ┌────────┬────────────────────────────────┐
           │ Option │ Description                    │
           ├────────┼────────────────────────────────┤
           │ appl0  │ batch information when -b used │
           └────────┴────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pminfo(1), pmlogdump(1), PMAPI(3),
           pmErrStr(3), pmGetOptions(3), pmSpecLocalPMDA(3), pcp.conf(5),
           pcp.env(5) and PMNS(5).

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

    Performance Co-Pilot               PCP                         PMPROBE(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcp-dstat(1)](../man1/pcp-dstat.1.html),  [pminfo(1)](../man1/pminfo.1.html),  [pmrep(1)](../man1/pmrep.1.html),  [pmtrace(1)](../man1/pmtrace.1.html),  [pmdatrace(3)](../man3/pmdatrace.3.html),  [pcp-dstat(5)](../man5/pcp-dstat.5.html)

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
