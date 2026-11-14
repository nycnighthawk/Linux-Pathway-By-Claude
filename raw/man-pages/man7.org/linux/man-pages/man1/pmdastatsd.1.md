---
{"title": "pmdastatsd(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdastatsd.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdastatsd(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [INSTALLATION](#INSTALLATION) \| [USAGE](#USAGE) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDASTATSD(1)            General Commands Manual            PMDASTATSD(1)

## [](#NAME)NAME

           pmdastatsd - StatsD protocol performance metric domain agent
           (PMDA)

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/statsd/pmdastatsd [-D debug] [-Z maximum udp packet
           size] [-P port] [-v] [-g] [-o debug output filename] [-s] [-r
           parser type] [-a port] [-z maximum of unprocessed packets]

## [](#DESCRIPTION)DESCRIPTION

           StatsD is simple, text-based UDP protocol for receiving monitoring
           data of applications in architecture client-server.  pmdastatsd is
           an Performance Metrics Domain Agent that collects StatsD data,
           aggregates them and makes them available to any Performance Co-
           Pilot client, which is ideal for easily tracking stats in your
           application.

           The statsd PMDA supports Counter, Gauge and Duration (with
           instances for minimum, maximum, median, average, 90th percentile,
           95th percentile, 99th percentile, count and standard deviation)
           metric types, offers multiple parsing options: Ragel or
           handwritten/custom parser, offers multiple aggregating options for
           duration metric type: basic histogram or HDR histogram, supports
           custom form of labels, logging, exports multiple metrics about
           itself and may be configured either with an ini file or command
           line options.

## [](#CONFIGURATION)CONFIGURATION

           A brief description of the pmdastatsd command line options
           follows:

           -Z, --max-udp=<value>
                Maximum allowed packet size, any larger then this will be
                thrown away.  Default: 1472

           -P, --port=<value>
                Which port agent will listen to for incoming traffic.
                Default: 8125

           -v, --verbose
                Verbosity level.  Prints info about agent execution into
                logfile. Valid values are 0-2. 0 = Default value, shows
                config information, read socket state, and first 100 dropped
                messages. 1 = Shows PMNS and related information. 2 = Most
                detailed verbosity level, also shows dropped messages above
                100.  All levels include those below.

           -o, --debug-output-filename=<value>
                You can send USR1 signal that 'asks' agent to output basic
                information about all aggregated metric into a
                $PCP_LOG_DIR/pmcd/statsd_{name} file.  Default: 0

           -s, --version
                Flag controlling whether or not to log current agent version
                on start.  Default: 0

           -p, --parser-type=<value>
                Flag specifying which parser to use for incoming packets;
                Basic = 0, Ragel = 1.  Ragel parser includes better logging
                when verbose = 2.  Default: 0

           -a, --duration-aggregation-type=<value>
                Flag specifying which aggregation scheme to use for duration
                metrics; basic histogram = 0, HDR histogram = 1.  Default: 1

           -z, -max-unprocessed-packets=<value>
                Maximum size of packet queue that the agent will save in
                memory.  There are 2 queues: one for packets that are waiting
                to be parsed and one for parsed packets before they are
                aggregated.  Default: 2048

           The agent also looks for a pmdastatsd.ini file in the
           $PCP_PMDAS_DIR/statsd directory.  There, the same options may be
           specified, albeit with slightly different names as follows:

                max_udp_packet_size=<value>
                port=<value>
                verbose=<value>
                debug=<value>
                debug_output_filename=<value>
                version=<value>
                parser_type=<value>
                duration_aggregation_type=<value>
                max_unprocessed_packets=<value>

           Should an option be specified in both pmdastatsd.ini and command
           line, then the latter takes precedence.  Most of the time you will
           want to configure the agent with an ini file, as the agent should
           never be executed directly.

           Location of the log file.  By default, a log file named statsd.log
           is written in the current directory of pmcd(1) when pmdastatsd is
           started, i.e.  $PCP_LOG_DIR/pmcd.  If the log file cannot be
           created or is not writable, output is written to standard error
           instead.

## [](#INSTALLATION)INSTALLATION

           If you want to install the pmdastatsd, do the following as root:

                # cd $PCP_PMDAS_DIR/statsd
                # ./Install

           To uninstall, do the following as root:

                # cd $PCP_PMDAS_DIR/statsd
                # ./Remove

           pmdastatsd is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#USAGE)USAGE

           Once started, pmdastatsd will listen on specified port for any
           content in a form of:

               <metricname>:<value>|<type>

           There may be multiple such messages in single datagram, split by a
           newline character, so this:

               <metricname>:<value>|<type>\n<metricname>:<value>|<type>

           is valid as well.  Constraints for each of the above variables
           are:

               <metricname> = [a-z][a-zA-Z0-9_.]*
               <value> = described further in each metric type subsection
               <type> = One of the following: c , g or ms

           If verbose logging is turned on, agent will log every message
           parsed and related failures.

           All recorded metrics will, if parsed and aggregated successfully,
           be made available under statsd.*  namespace.

       1 Counter metric
           Stores metrics as simple counters, adding any incoming values to
           already existing ones.

               <metricname>:<value>|c

           Where value is positive number.

           Example:

           After aggregating following messages:

               metric:20|c
               metric:10|c
               metric:3.3|c

           Value available to PCP will be:

               # pminfo --fetch statsd.metric

                   inst [0 or '/'] value 33.3

       2 Gauge metric
           Stores metrics as modifiable values, with an option to either set,
           increment or decrement values.

               <metricname>:<value>|g

           Where value can be in a form of:

               '-{value}', when negative value is supplied agent will
               subtract value stored with the value passed

               '+{value}', when positive value with a leading plus sign is
               supplied, the agent will add the passed value to the value
               stored

               '{value}', when a value without any leading sign is supplied,
               the agent will set the metric to the passed value.

           Initial value for metric of gauge type is 0.

           Example:

           After aggregating following messages:

               metric:20|g
               metric:+10|g
               metric:-3.3|g

           Value available to PCP will be:

               # pminfo --fetch statsd.metric

                   inst [0 or '/'] value 26.7

       3 Duration metric
           Aggregates values either via HDR histogram or simply stores all
           values and then calculates instances from all values received.

               <metricname>:<value>|ms

           Where value is a positive number.

           Example:

           With larger message count, the values may vary based on selected
           duration aggregation scheme.

           After aggregating following messages:

               metric:10|ms
               metric:20|ms

           Values available to PCP will be:

               # pminfo --fetch statsd.metric

                   inst[0 or '/min'] value 10
                   inst[1 or '/max'] value 20
                   inst[2 or '/median'] value 10
                   inst[3 or '/average'] value 15
                   inst[4 or '/percentile90'] value 20
                   inst[5 or '/percentile95'] value 20
                   inst[6 or '/percentile99'] value 20
                   inst[7 or '/count'] value 2
                   inst[8 or '/std_deviation'] value 5

           Note:

           Once you send given metricname with specified type, the agent will
           no longer aggregate any messages with same.  metricname but
           different type and will throw them away.

       4 Labels
           StatsD datagrams may also contain key:value pairs separated by
           commas like so:

               metric,tagX=X,tagW=W:5|c

               OR

               metric:5|ms|#tagX:X,tagW:W

           Where tagX is a key, X is a value and tagW is a key, W is a value.

           Both key and value of such a pair are [a-ZA-Z0-9_.]{1,}.

           Both formats are interchangeable and you may combine them
           together.  When key is not unique, right most value takes
           precedence.  This is valid:

               metric,tagX=1:5|c|#tagX:2

           Pair with key tagX will have value of 2.

           You may use these labels to map specific values to some PCP
           instances.  PCP labels are also assigned to these PCP instances.
           Pairs are ordered by key in resulting instance name and label
           descriptor.

           Single label:

               metric,tagX=X:5|c

           Such a payload would map to PCP as follows (non-related labels
           were omitted):

               # pminfo --fetch --labels statsd.metric

                   inst [0 or '/tagX=X'] value 5
                   inst [0 or '/tagX=X'] labels {'tagX':'X'}

           As shown earlier you may also send payload with multiple labels.
           When multiple labels are supplied they are split in instance name
           by '::'.  Example:

               metric,tagX=X,tagW=W:5|c

           This resolves to:

               # pminfo --fetch --labels statsd.metric

                   inst [0 or '/tagX=X::tagW=W'] value 5
                   inst [0 or '/tagX=X::tagW=W'] labels {'tagX':'X','tagW':'W'}

           Note:

           Be mindful of the fact that duration metric type already maps to
           instances even without any labels.  Sending labeled value to such
           a metric creates another 9 (as there are that many hardcoded)
           instances.

           Example:

               metric:200|ms
               metric:100|ms
               metric,target=cpu2:10|ms
               metric,target=cpu2:100|ms
               metric,target=cpu2:1000|ms

           Creates 18 instances.  Duration data type and label name compose
           instance name in following manner:

               # pminfo --fetch --labels statsd.metric

                   ...
                   inst [10 or '/max::target=cpu0'] value 1000
                   inst [10 or '/max::target=cpu0'] labels {'target':'cpu0'}
                   ...

       5 Hardcoded stats
           Agent also exports metrics about itself:

           statsd.pmda.received
                Number of datagrams that the agent has received

           statsd.pmda.parsed
                Number of datagrams that were successfully parsed

           statsd.pmda.dropped
                Number of datagrams that were dropped

           statsd.pmda.aggregated
                Number of datagrams that were aggregated

           statsd.pmda.metrics_tracked
                This metric has 3 instances.  counter - Number of tracked
                counter metrics.  gauge - Number of tracked gauge metrics.
                duration - Number of tracked duration metrics.  total -
                Number of tracked metrics total.

           statsd.pmda.time_spent_parsing
                Total time in microseconds spent parsing metrics. Includes
                time spent parsing a datagram and failing midway.

           statsd.pmda.time_spent_aggregating
                Total time in microseconds spent aggregating metrics.
                Includes time spent aggregating a metric and failing midway.

           statsd.pmda.settings.max_udp_packet_size
                Maximum UDP packet size

           statsd.pmda.settings.max_unprocessed_packets
                Maximum size of unprocessed packets Q

           statsd.pmda.settings.verbose
                Verbosity flag

           statsd.pmda.settings.debug_output_filename
                Debug output filename

           statsd.pmda.settings.port
                Port that is listened to

           statsd.pmda.settings.parser_type
                Used parser type

           statsd.pmda.settings.duration_aggregation_type
                Used duration aggregation type

           These names are blacklisted for user usage.  No messages with
           these names will processed.  While not yet reserved, the whole
           statsd.pmda.*  namespace is not recommended to use for user
           metrics.

## [](#FILES)FILES

           $PCP_PMCDCONF_PATH
                  command line options used to launch pmdastatsd
           $PCP_PMDAS_DIR/statsd/Install
                  installation script for the pmdastatsd agent
           $PCP_PMDAS_DIR/statsd/Remove
                  undo installation script for the pmdastatsd agent
           $PCP_LOG_DIR/pmcd/statsd.log
                  default log file for error messages and other information
                  from pmdastatsd

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

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                      PMDASTATSD(1)

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
