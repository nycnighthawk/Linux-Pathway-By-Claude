---
{"title": "pmdumptext(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdumptext.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdumptext(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MULTIPLE SOURCES](#MULTIPLE_SOURCES) \| [UNIT CONVERSION](#UNIT_CONVERSION) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDUMPTEXT(1)            General Commands Manual            PMDUMPTEXT(1)

## [](#NAME)NAME

           pmdumptext - dump performance metrics to an ASCII table

## [](#SYNOPSIS)SYNOPSIS

           pmdumptext [-CFGHilmMNoruVXz?]  [-a archive] [-A align] [-c
           config] [-d delimiter] [-D debug] [-f format] [-h host] [-n
           pmnsfile] [-O offset] [-P precision] [-R lines] [-s sample] [-S
           starttime] [-t interval] [-T endtime] [-U string] [-w width] [-Z
           timezone] [metric ...]

## [](#DESCRIPTION)DESCRIPTION

           pmdumptext outputs the values of performance metrics collected
           live or from a set of Performance Co-Pilot (PCP) archives.  By
           default, the metric values are displayed in tab separated columns,
           prefixed by a timestamp.

           Unless directed to another host by the -h option, or to one or
           more sets of archives by the -a option, or an explict host: or
           archive/ prefix in the metric (see below for more information),
           pmdumptext will contact the Performance Metrics Collector Daemon
           (PMCD) on the local host to obtain the required information.

           pmdumptext may be run in interactive mode with the -i option which
           displays the values in equal width columns.  Without this option,
           no attempt is made to line up any values allowing the output to be
           easily parsed by other applications.

           The format of the output can be further controlled by changing the
           precision of the values with -P, the width of the columns with -w,
           and the format of the values with the -G and -F options for the
           shortest of scientific or fixed digits, and a fixed width format,
           respectively.

           By default pmdumptext will scale metric values to ``canonical''
           units of bytes, seconds and counts.  The one exception is with the
           -r option where the values are not scaled.  The -u option reports
           the units of each metric.

           The metrics to be dumped can be listed on the command line, in a
           config file, or piped to pmdumptext on stdin.  A metric consists
           of an optional source (host or archive), the metric name, and an
           optional instance list immediately after the name.  A colon is
           used to separate a host name from the metric, and a forward slash
           (``/'') to separate an archive name from the metric.  Instances
           are enclosed in square brackets and a comma is used between each
           instance if more than one is stated.  For example, some legal
           metrics are:

                   kernel.all.cpu.idle
                   myhost:kernel.all.cpu.idle[cpu0,cpu3]
                   /path/to/myarchive/kernel.all.cpu.idle[cpu1]

           When a metric does not contain a host: or archive/ prefix, e.g.
           kernel.all.cpu.idle above, then the source of the metric is
           determined by the following rules:
           (a) PMCD on host from the -h option if any, else
           (b) the archive from the first -a option if any, else
           (c) the host from the first metric prior to this one with a host:
               prefix if any, else
           (d) the archive from the first metric prior to this one with an
               archive/ prefix if any, else
           (e) PMCD on the local host, which is equivalent to local::metric.

           The format of a metric is further described in PCPIntro(1) in the
           PERFORMANCE METRIC SPECIFICATIONS section.  A normalization value
           may optionally follow a metric name in a config file or on stdin.
           The metric value will be scaled by this value.  For example, if
           the file system ``/dev/root'' has a capacity of 1965437 bytes,
           then the percentage of the file system that is used could be
           dumped with this config:

                   filesys.used[/dev/root] 19654.37

           A normalization value may not be used with metrics specified as
           command line arguments.

           A metric name is not required to be a leaf node in the Performance
           Metrics Name Space (PMNS), except when one or more instances are
           specified.  For example, to dump all file system metrics, only
           filesys is required to dump filesys.capacity, filesys.used,
           filesys.free etc.

## [](#OPTIONS)OPTIONS

           The command line options -A (or --align), -O (or --origin), -S (or
           --start) and -T (or --finish) control the alignment, offset, start
           and end time when visualizing metrics from archives.  These
           options are common to most Performance Co-Pilot tools and are
           fully described in PCPIntro(1).

           The other available options are:

           -a archive, --archive=archive
                Specifies the historical archive from which metrics can be
                obtained for a particular host.  archive is the full path to
                an individual archive file, or the name of a directory con‐
                taining archives, or the basename of an archive - all previ‐
                ously created by pmlogger(1).  Multiple sets of archives
                (separated by commas or in different -a options) from differ‐
                ent hosts may be given, but only one set of archives per host
                is permitted.  Any metrics that are not associated with a
                specific host or archive will use the first archive as their
                source.

           -c config, --config=config
                If no metrics are listed on the command line, a config file
                can be used to specify the metrics to be dumped.  Unlike the
                command line metrics, each metric may be followed by a nor‐
                malization value.  Empty lines and lines that begin with
                ``#'' are ignored.

           -C, --check
                Exit before dumping any values, but after parsing the met‐
                rics.  Metrics, instances, normals and units are listed if
                -m, -l, -N and/or -u are specified.

           -d delimiter, --delimiter=delimiter
                Specify the delimiter that separates each column of output.
                The delimiter may only be a single character.

           -f format, --time-format=format
                Use the format string for formatting the timestamp with each
                set of values.  The syntax of this string is the same as that
                described in strftime(3).  An empty format string (e.g. '')
                will remove the timestamps from the output.

           -F, --fixed
                Output the values in a fixed width format of 6 characters.
                Positive numbers are represented as dd.ddu and negative num‐
                bers as [-]d.ddu.  The postfix multiplier may have the values
                K(10^3), M(10^6), G(10^9) and T(10^12).  For example, 4567
                would be displayed as 4.57K, even if the units of the metric
                are bytes.

           -G, --scientific
                Output the values using the shortest of a scientific format
                or a decimal notation.

           -h host, --host=host
                Fetch performance metrics from pmcd(1) on host, rather than
                the default localhost.

           -H, --headers
                Show all headers before dumping any metric values.  This is
                equivalent to -lmNu.

           -i, --interactive
                Output the data in fixed width columns using fixed width val‐
                ues (see -F) so that it is human-readable.  This option may
                not be used with -P as fixed point values are not fixed
                width.  This option will also affect the output of -m and -u
                options as the metric, instance and unit names will be trun‐
                cated.

           -l, --source
                Show the source of the metrics.  In interactive mode, the
                host of the metrics is shown.  In non-interactive mode, this
                option shows the source of the metrics with the metric name
                even if -m is not specified.

           -m, --metrics
                Output the metric names before the metric values.  The source
                and units of the metrics may also be dumped with the -l and
                -u options respectively.  If in interactive mode, the metrics
                names may be truncated, and the instance names, where rele‐
                vant, are also truncated on the follow line.

           -M   Output the column number and complete metric names before
                dumping any values.  If the -l flag is also specified, the
                source of the metrics is also shown.

           -n pmnsfile, --namespace=pmnsfile
                Load an alternative local PMNS from the file pmnsfile.

           -o, --offset
                When a timestamp is being reported (i.e. unless an empty for‐
                mat string is given with the -f option), the timestamp is
                prefixed with the offset in seconds from the start of the set
                of archives or the beginning of the execution of pmdumptext.

           -N   Output the normalization factors before the metric values.

           -p precision, --precision=precision
                Set the precision of the values.  This option may not be used
                with -F as the precision is constant.  The default precision
                is 3.

           -r, --raw
                Output the raw metric values, do not convert counters to
                rates and do not scale values to ``canonical'' units.  This
                option also causes pmdumptext to ignore the normalization
                values for each metric.

           -R lines, --repeat=lines
                Repeat the header every lines of output.  This option is use‐
                ful in interactive mode when using a graphical window to
                avoid the header scrolling beyond the window's buffer, and to
                realign the header if the window is resized.

           -s samples, --samples=samples
                pmdumptext will terminate after this many samples.

           -t interval, --interval=interval
                The interval option follows the syntax described in
                PCPIntro(1), and in the simplest form may be an unsigned in‐
                teger (the implied units in this case are seconds).  The de‐
                fault interval is 1 second.

           -u, --units
                Output the units of the metrics before the first values, but
                after the metric names if -m is also specified.

           -U string, --unavailable=string
                Change the output when values are unavailable to string.  The
                default string is ``?''.

           -V, --version
                Display version number and exit.

           -w width, --widthfR=width
                Set the column width of the output.  Strings will be truncat‐
                ed to this width, and maybe postfixed by ``...'' if the width
                is greater than 5.

           -X, --extended
                Output the column number and complete metric names, one-per-
                line, both before dumping the first set of values and again
                each time the header is repeated.

           -z, --hostzone
                Use the local timezone of the host that is the source of the
                performance metrics, as identified by either the -h or the
                first -a options.  The default is to use the timezone of the
                local host.

           -Z timezone, --timezone=timezone
                Use timezone for the date and time.  Timezone is in the for‐
                mat of the environment variable TZ as described in
                environ(7).

           -?, --help
                Display usage message and exit.

## [](#MULTIPLE_SOURCES)MULTIPLE SOURCES

           pmdumptext supports the dumping of metrics from multiple hosts or
           set of archives.  The metrics listed on the command line or in the
           config file may have no specific source or come from different
           sources.

           However, restrictions apply when archives are specified on the
           command line (-a) and/or in the configuration file.  Firstly,
           there may be only one set of archives for any one host.  Secondly,
           the hosts of any metrics with host sources must correspond to the
           host of a set of archives, either on the command line or previous‐
           ly as the source of another metric.

           The options -a and -h may not be used together.

## [](#UNIT_CONVERSION)UNIT CONVERSION

           All metrics that have the semantics of counters are automatically
           converted to rates over the sample time interval.  In interactive
           mode, pmdumptext will also change the units of some metrics so
           that they are easier to comprehend:

           o      All metrics with space units (bytes to terabytes) are
                  scaled to bytes.  Note that 1024 bytes with be represented
                  as 1.02K, not 1.00K.

           o      Metrics that are counters with time units (nanoseconds to
                  hours) represent time utilization over the sample interval.
                  The unit strings of such metrics is changed to ``Time Uti‐
                  lization'' or abbreviated to ``util'' and the values are
                  normalized to the range zero to one.

## [](#EXAMPLES)EXAMPLES

           o To examine the load on two hosts foo and bar, simultaneously:

         $ pmdumptext -il 'foo:kernel.all.load[1]' 'bar:kernel.all.load[1]'
                      Source        foo     bar
         Wed Jul 30 11:37:53      0.309   0.409
         Wed Jul 30 11:37:54      0.309   0.409
         Wed Jul 30 11:37:55      0.309   0.409

           o To output the memory utilization on a remote host called bong
           with a simpler timestamp:

         $ pmdumptext -imu -h bong -f '%H:%M:%S' mem.util
           Metric        kernel  fs_ctl  _dirty  _clean    free    user
            Units             b       b       b       b       b       b
         09:32:28         8.98M   0.97M   0.00    3.90M   7.13M  46.13M
         09:32:29         8.99M   0.98M   0.00    5.71M   5.39M  46.03M
         09:32:30         8.99M   1.07M   0.00    5.81M   4.55M  46.69M
         09:32:31         9.03M   1.16M   0.00    6.45M   3.48M  47.00M
         09:32:32         9.09M   1.18M  20.48K   6.23M   3.29M  47.30M

           o To dump all metrics collected in an archive at a 30 second in‐
           terval to a file for processing by another tool:

         $ pminfo -a archive | pmdumptext -t 30s -m -a archive > outfile

## [](#FILES)FILES

           $PCP_VAR_DIR/pmns/*
                default PMNS specification files

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to parameter‐
           ize the file and directory names used by PCP.  On each installa‐
           tion, the file /etc/pcp.conf contains the local values for these
           variables.  The $PCP_CONF variable may be used to specify an al‐
           ternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional diagnos‐
           tics on stderr to help triage problems, although the information
           is sometimes cryptic and primarily intended to provide guidance
           for developers rather end-users.  debug is a comma separated list
           of debugging options; use pmdbg(1) with the -l option to obtain a
           list of the available debugging options and their meaning.

           Debugging options specific to pmdumptext are as follows:
           ┌────────┬───────────────────────────────────────────────────────┐
           │ Option │ Description                                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl0  │ detailed diagnostics for metrics, their source and    │
           │        │ timezone, metadata, units normalization, output for‐  │
           │        │ mat, etc.                                             │
           └────────┴───────────────────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmchart(1), pmlogger(1), pmrep(1), PMAPI(3),
           strftime(3) and environ(7).

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

    Performance Co-Pilot                                        PMDUMPTEXT(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcpintro(1)](../man1/pcpintro.1.html),  [pmchart(1)](../man1/pmchart.1.html),  [pmclient(1)](../man1/pmclient.1.html),  [pmlogsummary(1)](../man1/pmlogsummary.1.html),  [pmrep(1)](../man1/pmrep.1.html),  [pmval(1)](../man1/pmval.1.html),  [pmview(1)](../man1/pmview.1.html)

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
