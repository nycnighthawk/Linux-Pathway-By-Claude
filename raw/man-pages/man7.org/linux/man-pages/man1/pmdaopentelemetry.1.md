---
{"title": "pmdaopentelemetry(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdaopentelemetry.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdaopentelemetry(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION SOURCES](#CONFIGURATION_SOURCES) \| [URL SOURCES](#URL_SOURCES) \| [METRIC FILTERING](#METRIC_FILTERING) \| [LABEL FILTERING](#LABEL_FILTERING) \| [SCRIPTED SOURCES](#SCRIPTED_SOURCES) \| [SELinux CONSIDERATIONS](#SELinux_CONSIDERATIONS) \| [METRIC NAMING](#METRIC_NAMING) \| [DYNAMIC METRIC NAMES](#DYNAMIC_METRIC_NAMES) \| [METADATA](#METADATA) \| [CONTROL METRICS](#CONTROL_METRICS) \| [LIMITATIONS](#LIMITATIONS) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAOPENTELEMETRY(1)     General Commands Manual     PMDAOPENTELEMETRY(1)

## [](#NAME)NAME

           pmdaopentelemetry - OpenTelemetry PMDA

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/opentelemetry/pmdaopentelemetry [-D debug] [-n] [-c
           config] [-d domain] [-l logfile] [-R refresh_timeout] [-r root]
           [-t timeout] [-u user]

## [](#DESCRIPTION)DESCRIPTION

           pmdaopentelemetry is a Performance Metrics Domain Agent (PMDA)
           which dynamically creates PCP metrics from configured
           OpenTelemetry endpoints that provide HTTP based access to
           application metrics.

           The default config directory is
           $PCP_PMDAS_DIR/opentelemetry/config.d/, see ``CONFIGURATION
           SOURCES'' below.  The default URL fetch timeout is 2 seconds.  The
           default user, if not specified with the -u option, is the "pcp"
           user.  If the -n option is given, the list of configuration files
           will not be sorted prior to processing.  This list is sorted by
           default but that can be expensive if there are a large number of
           configuration files (URLs and/or scripts).

           The -d option may be used to override the default performance
           metrics domain number, which defaults to 164.  It is strongly
           recommended not to change this.  The domain number should be
           different for every PMDA on the one host, and the same domain
           number should be used for pmdaopentelemetry PMDA on all hosts.
           See also the -r option, which allows the root of the dynamic
           namespace to be changed from the default opentelemetry.

           The -l option may be used to specify logfile as the destination
           for PMDA messages instead of the default,
           $PCP_LOG_DIR/pmcd/opentelemetry.log.  As a special case, logfile
           may be "-" to send messages to the stderr stream instead, e.g.
           -l-.  This would normally be the stderr stream for the parent
           process, pmcd(1), which may itself have redirected stderr.  This
           redirection is normally most useful in a containerized
           environment, or when using dbpmda(1).

           The -r option allows the root of the dynamic namespace to be
           changed to root from the default, opentelemetry.  In conjunction
           with other command line options, this allows pmdaopentelemetry to
           be deployed as a different PMDA with distinct metrics namespace
           and metrics domain on the same host system.  Note that all PMDAs
           require a unique domain number so the -d option must also be
           specified.  Use of the -r option may also change the defaults for
           some other command line options, e.g. the default log file name
           and the default configuration directory.

           The -R option allows the user to configure the timeout, in
           seconds, between cluster refreshes. The default value is 10
           seconds.

## [](#CONFIGURATION_SOURCES)CONFIGURATION SOURCES

           As it runs, pmdaopentelemetry periodically recursively scans the
           $PCP_PMDAS_DIR/opentelemetry/config.d directory (or the directory
           specified with the -c option), looking for source URL files
           (*.url) and executable scripts or binaries.  Any files that do not
           have the .url suffix or are not executable, are ignored - this
           allows documentation files such as "README" and non-executable
           "common" script function definitions to be present without being
           considered as config files.

           A remote server does not have to be up or stay running - the PMDA
           tolerates remote URLs that may come and go over time.  The PMDA
           will relay data and metadata when/if they are available, and will
           return errors when/if they are down.  PCP metric IDs, internal and
           external instance domain identifiers are persisted and will be
           restored when individual metric sources become available and/or
           when the PMDA is restarted.  In addition, the PMDA checks
           directory modification times and will rescan for new or changed
           configuration files dynamically.  It is not necessary to restart
           the PMDA when adding, removing or changing configuration files.

## [](#URL_SOURCES)URL SOURCES

           Each file with the .url suffix found in the config directory or
           sub-directory contains one complete HTTP or HTTPS URL at which
           pmdaopentelemetry can reach a OpenTelemetry endpoint.  Local file
           access is also supported with a conventional
           file:///somepath/somefile URL, in which case somepath/somefile
           should contain OpenTelemetry formatted metric data.

           The first line of a .url config file should be the URL, as
           described above.  Subsequent lines, if any, are prefixed with a
           keyword that can be used to alter the http GET request.  A keyword
           must end with ':' (colon) and the text extends to the end of the
           line.  Comment lines that start with # and blank lines are
           ignored.  The only currently supported keywords are HEADER: and
           FILTER:.

           HEADER: headername: value ... to end of line
           Adds headername and its value to the headers passed in the http
           GET request for the configured URL.  An example configuration file
           that provides 3 commonly used headers and an authentication token
           might be :

              http://somehost/path/endpoint.html
              # this is a comment
              HEADER: Accept: text/html
              HEADER: Keep-Alive: 300
              HEADER: Connection: keep-alive
              HEADER: Authorization: token ABCDEF1234567890

           As mentioned above, header values extend to the end of the line.
           They may contain any valid characters, including colons.  Multiple
           spaces will be collapsed to a single space, and leading and
           trailing spaces are trimmed.  A common use for headers is to
           configure a proxy agent and the assorted parameters it may
           require.

## [](#METRIC_FILTERING)METRIC FILTERING

           Metric filtering is a configuration file feature that allows
           ingested metrics to be included or excluded, i.e. filtered.  This
           is useful because most end-points return multiple metrics, and
           usually only some are interesting for monitoring purposes.  The
           syntax is:
           FILTER: INCLUDE METRIC regex
           or
           FILTER: EXCLUDE METRIC regex
           Dynamically created metric names that match regex will be either
           included or excluded in the name space, as specified.  Note that
           only the PMNS leaf component of the metric name (as ingested from
           the URL source) is compared with the regex pattern.  The simple
           rule is that the first matching filter regex for a particular
           metric leaf name is the rule that prevails.  If no filter regex
           matches (or there are no filters), then the metric is included by
           default, i.e. the default filter if none are specified is FILTER:
           INCLUDE METRIC .*  This is backward compatible with older versions
           of the configuration file that did not support filters.  Multiple
           FILTER: lines would normally be used, e.g. to include some metrics
           but exclude all others, use FILTER: EXCLUDE METRIC .*  as the last
           of several filters that include the desired metrics.  Conversely,
           to exclude some metrics but include all others, use FILTER:
           EXCLUDE METRIC regex.  In this case it's not necessary (though
           doesn't hurt) to specify the final FILTER: INCLUDE METRIC .*
           because, as stated above, any metric that does not match any
           filter regex will be included by default.

## [](#LABEL_FILTERING)LABEL FILTERING

           Label filtering uses similar FILTER: syntax and semantics as
           metric filtering.  FILTER: EXCLUDE LABEL regex will delete all
           labels with label name matching regex from all metrics defined by
           the configuration file.  The same rules as for metric filters
           apply for label filters too - an implicit rule: FILTER: INCLUDE
           LABEL .*  applies to all labels that do not match any earlier
           label filter rule.  FILTER: OPTIONAL LABEL regex specifies that
           matching label names are to be included in the returned metric
           labelsets (i.e. included), but are not to be used as part of the
           the external instance names.  All included labels that are not
           optional (i.e. the intrinsic labels) will be concatenated together
           and used for external instance naming.  In addition, non-intrinsic
           labels (i.e. labels tagged as OPTIONAL) will have the
           PM_LABEL_OPTIONAL flag set in the labelsets returned by notes
           callbacks.  This flag affects how the labels are used in certain
           clients.  For further details, see pmLookupLabels(3) and related
           man pages for further details.  Note that external instance names
           begin with the unique numeric internal instance identifier
           followed by a space, so external instance names are always unique.

           Caution is needed with label filtering because by default, all
           labels are used to construct the PCP instance name.  By excluding
           some labels (or changing them to optional), the instance names
           will change.  By excluding some labels, different instances
           returned by the URL or scripted configuration entry for the same
           metric may become duplicates.  When such duplicates occur, the
           last duplicate instance returned by the end-point URL or script
           prevails over any earlier instances.  For these reasons, it is
           recommended that label filtering rules be configured when the
           configuration file is first defined, and not changed thereafter.
           If a label filtering change is required, the configuration file
           should be renamed, which effectively defines a new metric (or set
           of peer metrics as returned by the URL or script), with the new
           (or changed) instance naming.

           Unrecognized keywords in configuration files are reported in the
           PMDA log file but otherwise ignored.

## [](#SCRIPTED_SOURCES)SCRIPTED SOURCES

           Executable scripts present in the
           $PCP_PMDAS_DIR/opentelemetry/config.d directory or sub-directories
           will be executed and the stdout stream containing OpenTelemetry
           formatted metric data will be parsed as though it had come from a
           URL or file.  The stderr stream from a script will be sent to the
           PMDA log file, which by default can be found in
           $(PCP_LOG_DIR)/pmcd/opentelemetry.log.

           Note that scripted sources do not support label or metric
           filtering (as described above for URL sources) - they can simply
           do their own filtering in the script itself with sed(1), awk(1),
           or whatever tool is desired.

           For full details of the OpenTelemetry exposition formats see
           https://github.com/open-telemetry/opentelemetry-proto/ 
           blob/main/opentelemetry/proto/metrics/v1/metrics.proto.

## [](#SELinux_CONSIDERATIONS)SELinux CONSIDERATIONS

           Scripted config files are executed by the pmdaopentelemetry PMDA
           with the same SELinux context and policy as the local pmcd(1).
           For simple scripts, this is normally fine.  However AVC errors may
           result for scripts that make library or system calls that are
           restricted by the prevailing SELinux context and policies.  In
           these cases it is not feasible to unilaterally grant pmcd or it's
           PMDAs an unconfined execution policy.  In these site specific
           cases it will be necessary to create a local SELinux policy
           module.  This can be done by capturing the AVC record(s) from the
           local audit log, generate a local policy module using audit2allow,
           and then load the new module using semodule, e.g. as follows :

                  $ sudo grep '^type=AVC.*pcp' /var/log/audit/audit.log \
                  | audit2allow -M mypolicy
                  $ sudo semodule -i mypolicy.pp

           If these local policies need to be persistent across reboots, then
           a scriptlet similar to the above example may be added to the local
           pmcd RC file (typically /etc/pcp/pmcd/rc.local).  For further
           details, see audit2allow(1) and semodule(1).

## [](#METRIC_NAMING)METRIC NAMING

           All metrics from a file named JOB.*  will be exported as PCP
           metrics with the opentelemetry.JOB metric name prefix.  Therefore,
           the JOB name must be a valid non-leaf name for PCP PMNS metric
           names.  If the JOB name has multiple dot-separated components, the
           resulting PMNS names will include those components and care is
           needed to ensure there are no overlapping definitions, e.g.
           metrics returned by JOB.response may overlap or conflict with
           metrics returned by JOB.response.time.

           Config file entries (URLs or scripts) found in subdirectories of
           the config directory will also result in hierarchical metric
           names.  For example, a config file named
           $PCP_PMDAS_DIR/opentelemetry/config.d/mysource/latency/get.url
           will result in metrics being created (by fetching that source URL)
           below opentelemetry.mysource.latency.get in the PCP namespace.
           Scripts found in subdirectories of the config directory similarly
           result in hierarchical PCP metric names.

## [](#DYNAMIC_METRIC_NAMES)DYNAMIC METRIC NAMES

           As described above, changes and new additions can be made to files
           in the configuration directory without having to restart the PMDA.
           These changes are detected automatically and the PCP metric names
           below opentelemetry in the PMNS will be updated accordingly, i.e.
           new metrics will be dynamically added and/or existing metrics
           removed.  In addition, pmdaopentelemetry honors the
           PMCD_NAMES_CHANGE pmFetch(3) protocol that was introduced in PCP
           version 4.0.  In particular, if opentelemetry metrics are being
           logged by a PCP version 4.0 or later pmlogger(1), new metrics that
           appear as a result of changes in the PMDA configuration directory
           will automatically start to be logged, provided the root of the
           opentelemetry PMDA namespace is configured for logging in the
           pmlogger configuration file.  See pmlogger(1) for details.  An
           example of such a pmlogger configuration file is :

              log mandatory on 2 second {
                   # log all metrics below the root of the opentelemetry namespace
                   opentelemetry
              }

## [](#METADATA)METADATA

           Metric data returned by URL or scripted configuration files may
           contain metadata that can be used by the opentelemetry PMDA to
           specify the semantics, data type, scaling and units of dynamically
           created metrics.  This metadata is found for each metric under the
           metric list header in the opentelemetry json data structure.  For
           additional information about PCP metadata, see pmLookupDesc(3) and
           pmParseUnitsStr(3) and examples in shipped configuration files.

           Metadata must be supplied in the json data by the opentelemetry
           source end-point (URL or script).  An alternative is to specify
           this in the URL configuration file directly, which has the
           advantage of not having to modify the source/end-point if the
           metadata is incorrect or missing.  Metadata specified in the URL
           configuration file over-rides any in-line metadata.

           The configuration file syntax for specifying metadata is:
           METADATA: regex type indom semantics units ... to EOL
           Where:
           METADATA: is literal
           regex is an extended regular expression to match one or more
           metric names returned by the URL,
           type is one of the PCP numeric types (32, u32, 64, u64, float or
           double),
           indom is an arbitrary instance domain name, or PM_INDOM_NULL,
           semantics is either counter, instant or discrete and
           units is either none or a string extending to end of line that is
           parsable by pmParseUnitsStr(3), i.e. the units, dimensions and
           scaling to be used for matching metrics.

           An example configuration file that ingests metrics from the
           Grafana /metrics end-point on localhost, filters out all metrics
           returned by that URL except for grafana_api_response_status_total
           and then specifies the metric type is an unsigned 32 bit integer
           with a non-singular instance domain named response and counter
           semantics with units of count.

           http://localhost:3000/metrics 
           FILTER: INCLUDE METRIC grafana_api_response_status_total
           FILTER: EXCLUDE METRIC .*
           METADATA: grafana_api_response_status_total u32 response counter
           count

           Note that the name in the indom field is presently ignored unless
           it is PM_INDOM_NULL, in which case the metric has no instance
           domain (i.e. singular), even if it has labels which would
           otherwise be used for instance naming.

## [](#CONTROL_METRICS)CONTROL METRICS

           The PMDA maintains special control metrics, as described below.
           Apart from opentelemetry.control.debug, each of these metrics has
           one instance for each configured metric source.  All of these
           metrics have integer values with counter semantics, except
           opentelemetry.control.status, which has a string value.  It is
           important to note that fetching any of the opentelemetry.control
           metrics will only update the counters and status values if the
           corresponding URL is actually fetched.  If the source URL is not
           fetched, the control metric values do not trigger a refresh and
           the control values reported represent the most recent fetch of
           each corresponding source.

           The instance domain for the opentelemetry.control metrics is
           adjusted dynamically as new sources are discovered.  If there are
           no sources configured, the metric names are still defined but the
           instance domain will be empty and a fetch will return no values.

           opentelemetry.control.status
                  A string representing the status of the last fetch of the
                  corresponding source.  This will generally be success for
                  an http response code of 200 or an exit code of 0 for
                  scripted sources.  This metric can be used for service
                  availability monitoring - provided, as stated above, the
                  corresponding source URL is fetched too.

           opentelemetry.control.status_code
                  This metric is similar to opentelemetry.control.status
                  except that it is the integer response code of the last
                  fetch.  A value of 200 usually signifies success and any
                  other value failure. For scripted sources, a zero exit code
                  signifies success and any non zero code failure.  This
                  metric can also be used for service availability
                  monitoring, with the same caveats as
                  opentelemetry.control.status.

           opentelemetry.control.calls
                  total number of times each configured metric source has
                  been fetched (if it is a URL) or executed (if it's a
                  script), since the PMDA started.  This metric has counter
                  semantics and would normally be converted to a rate/second
                  by client tools.

           opentelemetry.control.fetch_time
                  Total time in milliseconds that each configured metric
                  source has taken to return a document, excluding the time
                  to parse the document.  This metric has counter semantics
                  and would normally be rate converted by client tools but is
                  also useful in raw form as the accumulated parse time since
                  the PMDA was started.

           opentelemetry.control.parse_time
                  Total time in milliseconds that each configured metric
                  source has taken to parse each document, excluding the time
                  to fetch the document.  This metric has counter semantics
                  and would normally be rate converted by client tools but is
                  also useful in raw form as the accumulated parse time since
                  the PMDA was started.

           When converted to a rate, the calls metric represents the average
           fetch rate of each source over the sampling interval (time delta
           between samples).  The fetch_time and parse_time counters, when
           converted to a rate, represent the average fetch and parsing
           latency (respectfully), during the sampling interval.

           The opentelemetry.control.debug metric has a singular value,
           defaulting to 0.  If a non-zero value is stored into this metric
           using pmstore(1), additional debug messages will be written to the
           PMDA log file.

## [](#LIMITATIONS)LIMITATIONS

           pmdaopentelemetry and libpcp internals impose some numerical
           constraints about the number of sources (4095), metrics (1024)
           within each source, and instances for each metric (4194304).

## [](#INSTALLATION)INSTALLATION

           Install the OpenTelemetry PMDA by using the Install script as
           root:

               # cd $PCP_PMDAS_DIR/opentelemetry
               # ./Install

           To uninstall, the following must be done as root:

               # cd $PCP_PMDAS_DIR/opentelemetry
               # ./Remove

           pmdaopentelemetry is launched by pmcd(1) and should never be
           executed directly.  The Install and Remove scripts notify pmcd
           when the agent is installed or removed.

           When scripts and .url files are added, removed or changed in the
           configuration directory, it is usually not necessary to restart
           the PMDA - the changes will be detected and managed on subsequent
           requests to the PMDA.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/opentelemetry/Install
               installation script for the pmdaopentelemetry agent

           $PCP_PMDAS_DIR/opentelemetry/Remove
               undo installation script for the pmdaopentelemetry agent

           $PCP_PMDAS_DIR/opentelemetry/config.d/
               contains URLs and scripts used by the pmdaopentelemetry agent
               as sources of opentelemetry metric data.

           $PCP_LOG_DIR/pmcd/opentelemetry.log
               default log file for error messages from pmdaopentelemetry

           $PCP_VAR_DIR/config/164.*
               files containing internal tables for metric and instance ID
               number persistence (domain 164).

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on the PMDA log file, which is
           $PCP_LOG_DIR/pmcd/opentelemetry.log by default (see also -l
           above), to help triage problems, although the information is
           sometimes cryptic and primarily intended to provide guidance for
           developers rather end-users.  debug is a comma separated list of
           debugging options; use pmdbg(1) with the -l option to obtain a
           list of the available debugging options and their meaning.

           Debugging options specific to pmdaopentelemetry are as follows:
           ┌────────┬───────────────────────────────────────────────────────┐
           │ Option │ Description                                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl0  │ Detailed debugging that is particularly useful for    │
           │        │ examining the http headers passed to each fetch       │
           │        │ request, filter settings and other processing         │
           │        │ details.                                              │
           └────────┴───────────────────────────────────────────────────────┘

           In addition, the metric opentelemetry.control.debug controls the
           appl0 debug setting for a running pmdaopentelemetry and this can
           be changed with the following command:
                $ pmstore opentelemetry.control.debug value
           where value is either 1 (to enable appl0 diagnostics) or 0 (to
           disable appl0 diagnostics).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), audit2allow(1), pmcd(1), pmdaopenmetrics(1),
           pmdbg(1), pminfo(1), pmlogger(1), pmstore(1), semodule(1),
           PMAPI(3), PMWEBAPI(3), pmFetch(3) and pmLookupLabels(3).

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

    Performance Co-Pilot               PCP               PMDAOPENTELEMETRY(1)

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
