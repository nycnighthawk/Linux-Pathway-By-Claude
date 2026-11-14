---
{"title": "pcpintro(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/PCPIntro.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcpintro(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [INTRODUCTION](#INTRODUCTION) \| [OVERVIEW](#OVERVIEW) \| [COMMON COMMAND LINE ARGUMENTS](#COMMON_COMMAND_LINE_ARGUMENTS) \| [INTERVAL SPECIFICATION AND ALIGNMENT](#INTERVAL_SPECIFICATION_AND_ALIGNMENT) \| [TIME WINDOW SPECIFICATION](#TIME_WINDOW_SPECIFICATION) \| [PERFORMANCE METRICS - IDENTIFIERS, NAMES, VALUES](#PERFORMANCE_METRICS_-_IDENTIFIERS,_NAMES,_VALUES) \| [PERFORMANCE METRIC SPECIFICATIONS](#PERFORMANCE_METRIC_SPECIFICATIONS) \| [SECURE PMCD CONNECTIONS](#SECURE_PMCD_CONNECTIONS) \| [PMCD HOST SPECIFICATION](#PMCD_HOST_SPECIFICATION) \| [FILES](#FILES) \| [ENVIRONMENT](#ENVIRONMENT) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCPINTRO(1)              General Commands Manual              PCPINTRO(1)

## [](#NAME)NAME

           PCPIntro - introduction to the Performance Co-Pilot (PCP)

## [](#INTRODUCTION)INTRODUCTION

           The Performance Co-Pilot (PCP) is a toolkit designed for
           monitoring and managing system-level performance.  These services
           are distributed and scalable to accommodate the most complex
           system configurations and performance problems.

           PCP supports many different platforms, including (but not limited
           to) Linux, macOS, Solaris and Windows.  From a high-level PCP can
           be considered to contain two classes of software utility:

           PCP Collectors
                   These are the parts of PCP that collect and extract
                   performance data from various sources, for example the
                   operating system kernel.

           PCP Monitors
                   These are the parts of PCP that display data collected
                   from hosts (or archives) that have the PCP Collector
                   installed.  Many monitor tools are available as part of
                   the core PCP release, while other (typically graphical)
                   monitoring tools are available separately in the PCP GUI
                   package.

           This manual entry describes the high-level features and options
           common to most PCP utilities available on all platforms.

## [](#OVERVIEW)OVERVIEW

           The PCP architecture is distributed in the sense that any PCP tool
           may be executing remotely.  On the host (or hosts) being
           monitored, each domain of performance metrics, whether the kernel,
           a service layer, a database management system, a web server, an
           application, etc.  requires a Performance Metrics Domain Agent
           (PMDA) which is responsible for collecting performance
           measurements from that domain.  All PMDAs are controlled by the
           Performance Metrics Collector Daemon (pmcd(1)) on the same host.

           Client applications (the monitoring tools) connect to pmcd(1),
           which acts as a router for requests, by forwarding requests to the
           appropriate PMDA and returning the responses to the clients.
           Clients may also access performance data from sets of PCP archives
           (created using pmlogger(1)) for retrospective analysis.

       Security philosophy
           PCP redistributes a wealth of performance information within a
           host and across its networks.  The following security philosophy
           underlies the setting of several defaults that control how much
           information is sent and received.

           By default, the information exposed by PMCD about a host is
           approximately of the same level of confidentiality as available to
           a completely unprivileged user on that host.  So, performance data
           that is available to be read completely freely on a machine may be
           made available by PMCD to the network.

           However, the host running PMCD and its network is not assumed to
           run only friendly applications.  Therefore, write type operations,
           including from the local host, are not permitted by default.

           These defaults may be overridden (expanded or reduced) in several
           ways, including by specifying network ACLs in pmcd.conf,
           activating non-default PMDAs, or by using PMCD connections that
           pass user credentials.  For example, some PMDAs automatically
           provide greater information for particular credentialed users or
           groups.

       Applications
           The following performance monitoring applications are primarily
           console based, typically run directly from the command line, and
           are just a small subset of the tools available as part of the base
           PCP package.

           Each tool or command is documented completely in its own reference
           page.

           pmstat Outputs an ASCII high-level summary of system performance.

           pmie   An inference engine that can evaluate predicate-action
                  rules to perform alarms and automate system management
                  tasks.

           pminfo Interrogate specific performance metrics and the metadata
                  that describes them.

           pmlogger
                  Generates PCP archives of performance metrics suitable for
                  replay by most PCP tools.

           pmrep  Highly customizable performance metrics reporter with
                  support for various different output modes.

           pmval  Simple periodic reporting for some or all instances of a
                  performance metric, with optional VCR time control.

           If the PCP GUI package is installed then the following additional
           tools are available.

           pmchart
                  Displays trends over time of arbitrarily selected
                  performance metrics from one or more hosts.

           pmtime Time control utility for coordinating the time between
                  multiple tools (including pmchart and pmval).

           pmdumptext
                  Produce ASCII reports for arbitrary combinations of
                  performance metrics.

## [](#COMMON_COMMAND_LINE_ARGUMENTS)COMMON COMMAND LINE ARGUMENTS

           There is a set of common command line arguments that are used
           consistently by most PCP tools.

           -a archive, --archive=archive
                  Performance metric information is retrospectively retrieved
                  from the set of Performance Co-Pilot (PCP) archives
                  identified by archive previously generated by pmlogger(1).
                  See LOGIMPORT(3) and LOGARCHIVE(5) for archive creation
                  interfaces and format documentation.

                  archive is a comma-separated list of names, each of which
                  may be the name of a directory containing one or more
                  archives, the base name common to all of the physical files
                  created by an instance of pmlogger(1), or any one of the
                  physical files, e.g.  /path/to/myarchives (directory) or
                  myarchive (base name) or myarchive.meta (the metadata file)
                  or myarchive.index (the temporal index) or myarchive.0 (the
                  first data volume of archive) or myarchive.0.bz2 or
                  myarchive.0.bz (the first data volume compressed with
                  bzip2(1)) or myarchive.0.gz or myarchive.0.Z or
                  myarchive.0.z (the first data volume compressed with
                  gzip(1)), myarchive.1 or myarchive.3.bz2 or myarchive.42.gz
                  etc.

           -h host, --host=host
                  Unless directed to another host by the -h (or --host)
                  option, or to a set of archives by the -a (or --archive)
                  option, the source of performance metrics will be the
                  Performance Metrics Collector Daemon (PMCD) on the local
                  host.  Refer to the PMCD HOST SPECIFICATION section later
                  for further details on the many options available when
                  forming the host specification, as well as a detailed
                  description of the default local host connection.  The -a
                  (or --archive), and -h (or --host) options are mutually
                  exclusive.

                  -s samples, --samples=samples
                         The argument samples defines the number of samples
                         to be retrieved and reported.  If samples is 0 or -s
                         (or --samples) is not specified, the application
                         will sample and report continuously (in real time
                         mode) or until the end of the set of PCP archives
                         (in archive mode).

           -z, --hostzone
                  Change the reporting timezone to the local timezone at the
                  host that is the source of the performance metrics, as
                  identified via either the -h (or --host) or -a (or
                  --archive) options.

           -Z timezone, --timezone=timezone
                  By default, applications report the time of day according
                  to the local timezone on the system where the application
                  is executed.  The -Z (or --timezone) option changes the
                  timezone to timezone in the format of the environment
                  variable TZ as described in environ(7).

           -D debugspec, --debug=debugspec
                  Sets the PCP debugging options to debugspec to enable
                  diagnostics and tracing that is most helpful for developers
                  or when trying to diagnose the misbehaviour of a PCP
                  application.  debugspec should be a comma-separated list of
                  debugging option name(s) and/or decimal integers, see
                  pmdbg(1) for a description of the supported option names
                  and values.

                  In the absence of a live or archive source of metrics, a
                  heuristic search for archives for the local host can be
                  invoked via the -O (or --origin) option.  When using this
                  option without an explicit source of metrics, monitor tools
                  attempt to use archives from a system archive location such
                  as $PCP_LOG_DIR/pmlogger/`hostname`.  Refer to the TIME
                  WINDOW SPECIFICATION section below for details on the
                  acceptable syntax for the origin option, but a typical
                  invocation in this mode would be -O today or --origin
                  yesterday.

## [](#INTERVAL_SPECIFICATION_AND_ALIGNMENT)INTERVAL SPECIFICATION AND ALIGNMENT

           Most PCP tools operate with periodic sampling or reporting, and
           the -t (or --interval) and -A (or --align) options may be used to
           control the duration of the sample interval and the alignment of
           the sample times.

           -t interval, --interval=interval
                  Set the update or reporting interval.

                  The interval argument is specified as a sequence of one or
                  more elements of the form
                            number[units]
                  where number is an integer or floating point constant
                  (parsed using strtod(3)) and the optional units is one of:
                  seconds, second, secs, sec, s, minutes, minute, mins, min,
                  m, hours, hour, h, days, day and d.  If the unit is empty,
                  second is assumed.

                  In addition, the upper case (or mixed case) version of any
                  of the above is also acceptable.

                  Spaces anywhere in the interval are ignored, so 4 days 6
                  hours 30 minutes, 4day6hour30min, 4d6h30m and 4d6.5h are
                  all equivalent.

                  Multiple specifications are additive, for example ``1hour
                  15mins 30secs'' is interpreted as 3600+900+30 seconds.

           -A align, --align=align
                  By default samples are not necessarily aligned on any
                  natural unit of time.  The -A or --align option may be used
                  to force the initial sample to be aligned on the boundary
                  of a natural time unit.  For example -A 1sec, -A 30min and
                  --align 1hour specify alignment on whole seconds, half and
                  whole hours respectively.

                  The align argument follows the syntax for an interval
                  argument described above for the -t or --interval option.

                  Note that alignment occurs by advancing the time as
                  required, and that -A (or --align) acts as a modifier to
                  advance both the start of the time window (see the next
                  section) and the origin time (if the -O or --origin option
                  is specified).

## [](#TIME_WINDOW_SPECIFICATION)TIME WINDOW SPECIFICATION

           Many PCP tools are designed to operate in some time window of
           interest, for example to define a termination time for real-time
           monitoring or to define a start and end time within a set of PCP
           archives.

           In the absence of the -O (or --origin) and -A (or --align) options
           to specify an initial sample time origin and time alignment (see
           above), the PCP application will retrieve the first sample at the
           start of the time window.

           The following options may be used to specify a time window of
           interest.

           -S starttime, --start=starttime
                  By default the time window commences immediately in real-
                  time mode, or coincides with time at the start of the set
                  of PCP archives in archive mode.  The -S or --start option
                  may be used to specify a later time for the start of the
                  time window.

                  The starttime parameter may be given in one of three forms
                  (interval is the same as for the -t or --interval option as
                  described above, datetime is described below):

                  interval
                         To specify an offset from the current time (in real-
                         time mode) or the beginning of a set of PCP archives
                         (in archive mode) simply specify the interval of
                         time as the argument.  For example -S 30min will set
                         the start of the time window to be exactly 30
                         minutes from now in real-time mode, or exactly 30
                         minutes from the start of a set of PCP archives.

                  -interval
                         To specify an offset from the end of a set of PCP
                         archives, prefix the interval argument with a minus
                         sign.  In this case, the start of the time window
                         precedes the time at the end of the set of archives
                         by the given interval.  For example -S -1hour will
                         set the start of the time window to be exactly one
                         hour before the time of the last sample in a set of
                         PCP archives.

                  @datetime
                         To specify the calendar date and time (local time in
                         the reporting timezone) for the start of the time
                         window, use the datetime syntax preceded by an at
                         sign.  Refer to the datetime description below for
                         detailed information.

           -T endtime, --finish=endtime
                  By default the end of the time window is unbounded (in
                  real-time mode) or aligned with the time at the end of a
                  set of PCP archives (in archive mode).  The -T or --finish
                  option may be used to specify an earlier time for the end
                  of the time window.

                  The endtime parameter may be given in one of three forms
                  (interval is the same as for the -t or --interval option as
                  described above, datetime is described below):

                  interval
                         To specify an offset from the start of the time
                         window simply use the interval of time as the
                         argument.  For example -T 2h30m will set the end of
                         the time window to be 2 hours and 30 minutes after
                         the start of the time window.

                  -interval
                         To specify an offset back from the time at the end
                         of a set of PCP archives, prefix the interval
                         argument with a minus sign.  For example -T -90m
                         will set the end of the time window to be 90 minutes
                         before the time of the last sample in a set of PCP
                         archives.

                  @datetime
                         To specify the calendar date and time (local time in
                         the reporting timezone) for the end of the time
                         window, use the datetime syntax preceded by an at
                         sign.  Refer to the datetime description below for
                         detailed information.

           -O origin, --origin=origin
                  By default samples are fetched from the start of the time
                  window (see description of -S or --start option) to the end
                  of the time window (see description of -T or --finish
                  option).  The -O or --origin option allows the
                  specification of an origin within the time window to be
                  used as the initial sample time.  This is useful for
                  interactive use of a PCP tool with the pmtime(1) VCR replay
                  facility.

                  The origin argument accepted by -O (or --origin) conforms
                  to the same syntax and semantics as the starttime argument
                  for the -T (or --finish) option.

                  For example --origin -0 specifies that the initial position
                  should be at the end of the time window; this is most
                  useful when wishing to replay ``backwards'' within the time
                  window.

           The datetime argument for the -O (or --origin), -S (or --start)
           and -T (or --finish) options consists of:
                     date time zone day relative
           A date can be one of: YY-MM-DD, MM/DD/YY, DD Month YYYY, or Month
           DD YYYY.  A time can be one of: HH:MM:SS, HH:MM.  HH:MM can use
           either the 12 hour (via an am or pm suffix) or 24 hour convention.
           A day of the week can be a spelled out day of the week, optionally
           preceded by an ordinal number such as second Tuesday.  A zone is a
           time zone value as specified by the tzselect(8) command.  A
           relative time can be a time unit that is: preceded by a cardinal
           number such as 1 year or 2 months, preceded by one of the time
           words this or last, or succeeded by the time word ago.  A relative
           time can also be one of the time words: yesterday, today,
           tomorrow, now.  Examples of datetime strings are: 1996-03-04
           13:07:47 EST Mon, 1996-03-05 14:07:47 EST -1hour, Mon Mar  4
           13:07:47 1996, Mar 4 1996, Mar 4, Mar, 13:07:50 or 13:08.

           For any missing low order fields, the default value of 0 is
           assumed for hours, minutes and seconds, 1 for day of the month and
           Jan for months.  Hence, the following are equivalent: --start '@
           Mar 1996' and --start '@ Mar 1 00:00:00 1996'.

           If any high order fields are missing, they are filled in by
           starting with the year, month and day from the current time (real-
           time mode) or the time at the beginning of the set of PCP archives
           (archive mode) and advancing the time until it matches the fields
           that are specified.  So, for example if the time window starts by
           default at ``Mon Mar 4 13:07:47 1996'', then --start @13:10
           corresponds to 13:10:00 on Mon Mar 4, 1996, while --start @10:00
           corresponds to 10:00:00 on Tue Mar 5, 1996 (note this is the
           following day).

           For greater precision than afforded by datetime(3), the seconds
           component may be a floating point number.

           If a timezone is not included in a datetime then there are several
           interpretations available depending on the other command line
           options used.  The default is to use the local timezone on the
           system where the PCP tool is being run.  A -Z or --timezone option
           specifies an explicit timezone, else a -z or --hostzone option
           changes the timezone to the local timezone at the host that is the
           source of the performance metrics.

## [](#PERFORMANCE_METRICS_-_IDENTIFIERS,_NAMES,_VALUES)PERFORMANCE METRICS - IDENTIFIERS, NAMES, VALUES

           The number of performance metric names supported by PCP on most
           platforms ranges from many hundreds to several thousand.  The PCP
           libraries and applications use an internal identification scheme
           that unambiguously associates a single integer with each known
           performance metric.  This integer is known as the Performance
           Metric Identifier, or PMID.  Although not a requirement, PMIDs
           tend to have global consistency across all systems, so a
           particular performance metric usually has the same PMID.

           For all users and most applications, direct use of the PMIDs would
           be inappropriate (this would limit the range of accessible
           metrics, make the code hard to maintain, force the user interface
           to be particularly baroque, and so on).  Hence a Performance
           Metrics Name Space (PMNS) is used to provide external names and a
           hierarchic classification for performance metrics.  A PMNS is
           represented as a tree, with each node having a label, a pointer to
           either a PMID (for leaf nodes) or a set of descendent nodes in the
           PMNS (for non-leaf nodes).

           A node label must begin with an alphabetic character, followed by
           zero or more characters drawn from the alphabetics, the digits and
           character ``_'' (underscore).  For alphabetic characters in a node
           label, upper and lower case are distinguished.

           By convention, the name of a performance metric is constructed by
           concatenation of the node labels on a path through the PMNS from
           the root node to a leaf node, with a ``.'' as a separator.  The
           root node in the PMNS is unlabeled, so all names begin with the
           label associated with one of the descendent nodes below the root
           node of the PMNS, for example kernel.percpu.syscall.  Typically
           (although this is not a requirement) there would be at most one
           name for each PMID in a PMNS.  For example kernel.all.cpu.idle and
           disk.dev.read are the unique names for two distinct performance
           metrics, each with a unique PMID.

           Groups of related PMIDs may be named by naming a non-leaf node in
           the PMNS tree, for example disk.

           The default local PMNS used by pmcd is located at
           $PCP_VAR_DIR/pmns/root however the environment variable
           PMNS_DEFAULT may be set to the full pathname of a different PMNS
           which will then be used as the default local PMNS.

           Most applications do not use the local PMNS directly, but rather
           import parts of the PMNS as required from the same place that
           performance metrics are fetched, i.e. from pmcd(1) for live
           monitoring or from a set of PCP archives for retrospective
           monitoring.

           To explore the PMNS use pminfo(1), or if the PCP GUI package is
           installed the New Chart and Metric Search windows within
           pmchart(1).

           Some performance metrics have a singular value.  For example, the
           available memory or number of context switches have one value per
           performance metric source, that is, one value per host.  The
           metric descriptor (metadata) for each metric makes this fact known
           to applications that process values for these single-valued
           metrics.

           Some performance metrics have a set of values or instances in each
           implementing performance metric domain.  For example, one value
           for each disk, one value for each process, one value for each CPU,
           or one value for each activation of a given application.  When a
           metric has multiple instances, the PMNS does not represent this in
           metric names; rather, a single metric may have an associated set
           of values.  Multiple values are associated with the members of an
           instance domain, such that each instance has a unique instance
           identifier within the associated instance domain.  For example,
           the ''per CPU´´ instance domain may use the instance identifiers
           0, 1, 2, 3, and so on to identify the configured processors in the
           system.  Internally, instance identifiers are encoded as binary
           values, but each performance metric domain also supports
           corresponding strings as external names for the instance
           identifiers, and these names are used at the user interface to the
           PCP utilities.

           Multiple performance metrics may be associated with a single
           instance domain.  For example, per-process metrics under proc all
           share the same instance domain.

           PCP arranges for information describing instance domains to be
           exported from the performance metric domains to the applications
           that require this information.  Applications may also choose to
           retrieve values for all instances of a performance metric, or some
           arbitrary subset of the available instances.

           Metric names and the instance domain concept provides two-
           dimensions for the modelling of performance metrics.  This is a
           clear and simple model, however on some occasions it does not
           suffice.  For example, a metric may wish to represent higher
           dimensional data such as ``per CPU'' counters for each running
           process.  In these cases it is common to create a compound
           instance, where the name is composed of each component with a
           separator in-between (for example, ``87245::cpu7'' might be used
           to separate process ID from CPU ID) to create flattened instance
           names.  Additionally, such cases benefit from the use of metric
           instances labels to explicitly show the separate components
           (continuing the example from above, labels
           ``{"pid":87245,"cpu":7}'' might be used).

## [](#PERFORMANCE_METRIC_SPECIFICATIONS)PERFORMANCE METRIC SPECIFICATIONS

           In configuration files and (to a lesser extent) command line
           options, metric specifications adhere to the following syntax
           rules by most tools.  See the tool specific manual pages for the
           exact syntax supported.

           If the source of performance metrics is real-time from pmcd(1)
           then the accepted syntax is
                     host:metric[instance1,instance2,...]

           If the source of performance metrics is a set of PCP archives then
           the accepted syntax is
                     archive/metric[instance1,instance2,...]

           The host:, archive/ and [instance1,instance2,...]  components are
           all optional.

           The , delimiter in the list of instance names may be replaced by
           white space.

           Special characters in instance names may be escaped by surrounding
           the name in double quotes or preceding the character with a
           backslash.

           White space is ignored everywhere except within a quoted instance
           name.

           An empty instance is silently ignored, and in particular ``[]'' is
           the same as no instance, while ``[one,,,two]'' is parsed as
           specifying just the two instances ``one'' and ``two''.

           As a special case, if the host is the single character ``@'' then
           this refers to a PM_CONTEXT_LOCAL source, see pmNewContext(3).

## [](#SECURE_PMCD_CONNECTIONS)SECURE PMCD CONNECTIONS

           Since PCP version 3.6.11, a monitor can explicitly request a
           secure connection to a collector host running pmcd(1) or
           pmproxy(1) using the PM_CTXFLAG_SECURE context flag.  If the PCP
           Collector host supports this feature - refer to the
           pmcd.feature.secure metric for confirmation of this - a TLS/SSL
           (Transport Layer Security or Secure Sockets Layer) connection can
           be established which uses public key cryptography and related
           techniques.  These features aim to prevent eavesdropping and data
           tampering from a malicious third party, as well as providing
           server-side authentication (confident identification of a server
           by a client) which can be used to guard against man-in-the-middle
           attacks.

           A secure pmcd connection requires use of certificate-based
           authentication.  The security features offered by pmcd and pmproxy
           are implemented using the OpenSSL APIs and utilities.  The
           openssl(1) tool can be used to create certificates suitable for
           establishing trust between PCP monitor and collector hosts.

           A complete description is beyond the scope of this document, refer
           to the PCP ENVIRONMENT, FILES and SEE ALSO sections for detailed
           information.  This includes links to tutorials on the steps
           involved in setting up the available security features.

## [](#PMCD_HOST_SPECIFICATION)PMCD HOST SPECIFICATION

           In the absence of an explicit hostname specification, most tools
           will default to the local host in live update mode.  In PCP
           releases since 3.8.4 onward, this results in an efficient local
           protocol being selected - typically a Unix domain socket.  If this
           option is used (which can also be explicitly requested via the
           unix: host specification described below), it is important to note
           that all connections will be automatically authenticated.  In
           other words, the credentials of the user invoking a client tool
           will automatically be made available to pmcd(1) and all of its
           PMDAs, on the users behalf, such that results can be customized to
           the privilege levels of individual users.

           Names of remote hosts running the pmcd(1) daemon can of course
           also be provided to request a remote host be used.  The most basic
           form of pmcd host specification is a simple host name, possibly
           including the domain name if necessary.  However, this can be
           extended in a number of ways to further refine attributes of the
           connection made to pmcd.

           The pmcd port number and also optional pmproxy(1) hostname and its
           port number, can be given as part of the host specification, since
           PCP version 3.0.  These supersede (and override) the old-style
           PMCD_PORT, PMPROXY_HOST and PMPROXY_PORT environment variables.

           The following are valid hostname specifications that specify
           connections to pmcd on host nas1.acme.com with/without a list of
           ports, with/without a pmproxy(1) connection through a firewall,
           and with IPv6 and IPv4 addresses as shown.

                $ pcp --host nas1.acme.com:44321,4321@firewall.acme.com:44322
                $ pcp --host nas1.acme.com:44321@firewall.acme.com:44322
                $ pcp --host nas1.acme.com:44321@firewall.acme.com
                $ pcp --host nas1.acme.com@firewall.acme.com
                $ pcp --host nas1.acme.com:44321
                $ pcp --host [fe80::2ad2:44ff:fe88:e4f1%p2p1]
                $ pcp --host 192.168.0.103

           In addition, ``connection attributes'' can also be specified.
           These include username, password (can be given interactively and
           may depend on the authentication mechanism employed), whether to
           target a specific running container, whether to use secure
           (encrypted) or native (naked) protocol, and so on.  The previous
           examples all default to native protocol, and use no
           authentication.  This can be altered, as in the following
           examples.

                $ pcp --host pcps://app2.acme.com?container=cae8e6edc0d5
                $ pcp --host pcps://nas1.acme.com:44321?username=tanya&method=gssapi
                $ pcp --host pcps://nas2.acme.com@firewalls.r.us?method=plain
                $ pcp --host pcp://nas3.acme.com
                $ pcp --host 192.168.0.103?container=cae8e6edc0d5,method=scram-sha-256
                $ pcp --host unix:
                $ pcp --host local:

           The choice of authentication method, and other resulting
           parameters like username, optionally password, etc, depends on the
           SASL2 configuration used by each (remote) pmcd.  Tutorials are
           available specifying various aspects of configuring the
           authentication module(s) used, these fine details are outside the
           scope of this document.

           In all situations, host names can be used interchangeably with
           IPv4 or IPv6 addressing (directly), as shown above.  In the case
           of an IPv6 address, the full address must be enclosed by square
           brackets and the scope (interface) must also be specified.

           The final local: example above is now the default for most tools.
           This connection is an automatically authenticated local host
           connection on all platforms that support Unix domain sockets.  No
           password is required and authentication is automatic.  This is
           also the most efficient (lowest overhead) communication channel.

           The difference between unix: and local: is that the former is a
           strict Unix domain socket specification (connection fails if it
           cannot connect that way), whereas the latter has a more forgiving
           fallback to using localhost (i.e. a regular Inet socket connection
           is used when Unix domain socket connections are unavailable).

## [](#FILES)FILES

           /etc/pcp.conf
                Configuration file for the PCP runtime environment, see
                pcp.conf(5).

           /etc/pcp/tls.conf
                Optionally contains OpenSSL configuration information,
                including locations of certificates providing trusted
                identification for collector and monitor hosts.

           $HOME/.pcp
                User-specific directories containing configuration files for
                customisation of the various monitor tools, such as
                pmchart(1).

           $PCP_RC_DIR/pmcd
                Script for starting and stopping pmcd(1).

           $PCP_PMCDCONF_PATH
                Control file for pmcd(1).

           $PCP_PMCDOPTIONS_PATH
                Command line options passed to pmcd(1) when it is started
                from $PCP_RC_DIR/pmcd.  All the command line option lines
                should start with a hyphen as the first character.  This file
                can also contain environment variable settings of the form
                "VARIABLE=value".

           $PCP_BINADM_DIR
                Location of PCP utilities for collecting and maintaining PCP
                archives, PMDA help text, PMNS files etc.

           $PCP_PMDAS_DIR
                Parent directory of the installation directory for Dynamic
                Shared Object (DSO) PMDAs.

           $PCP_RUN_DIR/pmcd.pid
                If pmcd is running, this file contains an ascii decimal
                representation of its process ID.

           $PCP_LOG_DIR/pmcd
                Default location of log files for pmcd(1), current directory
                for running PMDAs.  Archives generated by pmlogger(1) are
                generally below $PCP_LOG_DIR/pmlogger.

           $PCP_LOG_DIR/pmcd/pmcd.log
                Diagnostic and status log for the current running pmcd(1)
                process.  The first place to look when there are problems
                associated with pmcd.

           $PCP_LOG_DIR/pmcd/pmcd.log.prev
                Diagnostic and status log for the previous pmcd(1) instance.

           $PCP_LOG_DIR/NOTICES
                Log of pmcd(1) and PMDA starts, stops, additions and
                removals.

           $PCP_VAR_DIR/config
                Contains directories of configuration files for several PCP
                tools.

           $PCP_SERVICES_DIR/local
                Local script for controlling PCP boot, shutdown and restart
                actions.  This was formerly located in
                $PCP_SYSCONF_DIR/pmcd/rc.local and a symbolic link is
                installed for that name to provide compatibility.

           $PCP_VAR_DIR/pmns
                Directory containing the set of PMNS files for all installed
                PMDAs.

           $PCP_VAR_DIR/pmns/root
                The ASCII PMNS(5) exported by pmcd(1) by default.  This PMNS
                is be the super set of all other PMNS files installed in
                $PCP_VAR_DIR/pmns.

           In addition, if the PCP product is installed the following files
           and directories are relevant.

           $PCP_LOG_DIR/NOTICES
                  In addition to the pmcd(1) and PMDA activity, may be used
                  to log alarms and notices from pmie(1) via pmpost(1).

           $PCP_PMLOGGERCONTROL_PATH
                  Control file for pmlogger(1) instances launched from
                  $PCP_RC_DIR/pmlogger and/or managed by pmlogger_check(1)
                  and pmlogger_daily(1) as part of a production PCP archive
                  collection setup.

## [](#ENVIRONMENT)ENVIRONMENT

           In addition to the PCP run-time environment and configuration
           variables described in the PCP ENVIRONMENT section below, the
           following environment variables apply to all installations.

           Note that most uses of these environment variables are optimized
           to check the environment only the first time the variable might be
           used.  As the environment usually is not checked again, the only
           safe strategy is to ensure all PCP-related environment variables
           are set before the first call into any of the PCP libraries.

           PCP_ALLOW_BAD_CERT_DOMAIN
                  When set, allow clients to accept certificates with
                  mismatched domain names with no prompt when they are sent
                  by pmcd or other server components.  See
                  PCP_SECURE_SOCKETS.

           PCP_ALLOW_SERVER_SELF_CERT
                  When set, allow clients to accept self-signed certificates
                  with no prompt when they are sent by pmcd or other server
                  components.  See PCP_SECURE_SOCKETS.

           PCP_CONSOLE
                  When set, this changes the default console from /dev/tty
                  (on Unix) or CON: (on Windows) to be the specified console.
                  The special value of none can be used to indicate no
                  console is available for use.  This is used in places where
                  console-based tools need to interact with the user, and in
                  particular is used when authentication is being performed.

           PCP_DEBUG
                  When set, this variable provides an alternate to the -D
                  command line option described above to initialize the
                  diagnostic and debug options for applications that use
                  pmGetOptions(3) to process command line options and
                  arguments.  The value for $PCP_DEBUG is the same as for the
                  -D command line option, namely a comma-separated list of
                  debugging option name(s), and/or decimal integers, see
                  pmdbg(1) for a description of the supported option names
                  and values.

           PCP_DERIVED_CONFIG
                  When set, this variable defines a colon separated list of
                  files and/or directories (the syntax is the same as for the
                  $PATH variable for sh(1)).  The components are expanded
                  into a list of files as follows: if a component of
                  $PCP_DERIVED_CONFIG is a file, then that file is added to
                  the list, else if a component is a directory then recursive
                  descent is used to enumerate all files below that directory
                  and these are added to the list.

                  Each file in the resulting list is assumed to contain
                  definitions of derived metrics as per the syntax described
                  in pmLoadDerivedConfig(3), and these are loaded in order.

                  Derived metrics may be used to extend the available metrics
                  with new (derived) metrics using simple arithmetic
                  expressions.

                  If PCP_DERIVED_CONFIG is set, the derived metric
                  definitions are processed automatically as each new source
                  of performance metrics is established (i.e. each time a
                  pmNewContext(3) is called) or when requests are made
                  against the PMNS.

                  Any component in the $PCP_DERIVED_CONFIG list or the
                  expanded list of files that is not a file, or is not a
                  directory or is not accessible (due to permissions or a bad
                  symbolic link) will be silently ignored.

           PCP_DERIVED_CONTROL
                  Settings for control options that may be used when
                  processing derived metrics.  Refer to
                  pmSetDerivedControl(3) for details.

           PCP_IGNORE_MARK_RECORDS
                  When PCP archives logs are created there may be temporal
                  gaps associated with discontinuities in the time series of
                  logged data, for example when pmcd(1) is restarted or when
                  multiple archives are concatenated with pmlogextract(1).
                  These discontinuities are internally noted with a <mark>
                  record in the PCP archives, and value interpolation as
                  described in pmSetMode(3) is not supported across <mark>
                  records (because the values before and after a <mark>
                  record are not necessarily from a continuous time series).
                  Sometimes the user knows the data semantics are sound in
                  the region of the <mark> records, and
                  $PCP_IGNORE_MARK_RECORDS may be used to suppress the
                  default behaviour.

                  If PCP_IGNORE_MARK_RECORDS is set (but has no value) then
                  all <mark> records will be ignored.  Otherwise the value
                  $PCP_IGNORE_MARK_RECORDS follows the syntax for an interval
                  argument described above for the -t option, and <mark>
                  records will be ignored if the time gap between the last
                  record before the <mark> and the first record after the
                  <mark> is not more than interval.

           PCP_SECURE_SOCKETS
                  When set, this variable forces any monitor tool connections
                  to be established using the certificate-based secure
                  sockets feature.  If the connections cannot be established
                  securely, they will fail.

           PCP_TLSCONF_PATH
                  Specifies the location from which TLS (Transport Layer
                  Security) configuration settings will be read.  These
                  settings are used by PCP client tools, pmcd and pmproxy
                  whenever secure (encrypted) communication is requested.

           PCP_STDERR
                  Many PCP tools support the environment variable PCP_STDERR,
                  which can be used to control where error messages are sent.
                  When unset, the default behavior is that ``usage'' messages
                  and option parsing errors are reported on standard error,
                  other messages after initial startup are sent to the
                  default destination for the tool, i.e. standard error for
                  ASCII tools, or a dialog for GUI tools.

                  If PCP_STDERR is set to the literal value DISPLAY then all
                  messages will be displayed in a dialog.  This is used for
                  any tools launched from a Desktop environment.

                  If PCP_STDERR is set to any other value, the value is
                  assumed to be a filename, and all messages will be written
                  there.

                  PMCD_CONNECT_TIMEOUT
                         When attempting to connect to a remote pmcd(1) on a
                         machine that is booting, the connection attempt
                         could potentially block for a long time until the
                         remote machine finishes its initialization.  Most
                         PCP applications and some of the PCP library
                         routines will abort and return an error if the
                         connection has not been established after some
                         specified interval has elapsed.  The default
                         interval is 5 seconds.  This may be modified by
                         setting PMCD_CONNECT_TIMEOUT in the environment to a
                         real number of seconds for the desired timeout.
                         This is most useful in cases where the remote host
                         is at the end of a slow network, requiring longer
                         latencies to establish the connection correctly.

                  PMCD_RECONNECT_TIMEOUT
                         When a monitor or client application loses a
                         connection to a pmcd(1), the connection may be re-
                         established by calling a service routine in the PCP
                         library.  However, attempts to reconnect are
                         controlled by a back-off strategy to avoid flooding
                         the network with reconnection requests.  By default,
                         the back-off delays are 5, 10, 20, 40 and 80 seconds
                         for consecutive reconnection requests from a client
                         (the last delay will be repeated for any further
                         attempts after the fifth).  Setting the environment
                         variable PMCD_RECONNECT_TIMEOUT to a comma separated
                         list of positive integers will re-define the back-
                         off delays, for example setting
                         PMCD_RECONNECT_TIMEOUT to ``1,2'' will back-off for
                         1 second, then attempt another connection request
                         every 2 seconds thereafter.

                  PMCD_REQUEST_TIMEOUT
                         For monitor or client applications connected to
                         pmcd(1), there is a possibility of the application
                         "hanging" on a request for performance metrics or
                         metadata or help text.  These delays may become
                         severe if the system running pmcd crashes, or the
                         network connection is lost.  By setting the
                         environment variable PMCD_REQUEST_TIMEOUT to a
                         number of seconds, requests to pmcd will timeout
                         after this number of seconds.  The default behavior
                         is to be willing to wait 10 seconds for a response
                         from every pmcd for all applications.

                  PMCD_WAIT_TIMEOUT
                         When pmcd(1) is started from $PCP_RC_DIR/pmcd the
                         check on pmcd's readiness will wait up to
                         PMCD_WAIT_TIMEOUT seconds.  If pmcd has a long
                         startup time (such as on a very large system), then
                         PMCD_WAIT_TIMEOUT can be set to provide a maximum
                         wait longer than the default 60 seconds.

           PMNS_DEFAULT
                  If set, then interpreted as the full pathname to be used as
                  the default local PMNS for pmLoadNameSpace(3).  Otherwise,
                  the default local PMNS is located at
                  $PCP_VAR_DIR/pcp/pmns/root for base PCP installations.

           PCP_COUNTER_WRAP
                  Many of the performance metrics exported from PCP agents
                  have the semantics of counter meaning they are expected to
                  be monotonically increasing.  Under some circumstances, one
                  value of these metrics may be smaller than the previously
                  fetched value.  This can happen when a counter of finite
                  precision overflows, or when the PCP agent has been reset
                  or restarted, or when the PCP agent is exporting values
                  from some underlying instrumentation that is subject to
                  some asynchronous discontinuity.

                  The environment variable PCP_COUNTER_WRAP may be set to
                  indicate that all such cases of a decreasing ``counter''
                  should be treated as a counter overflow, and hence the
                  values are assumed to have wrapped once in the interval
                  between consecutive samples.  This ``wrapping'' behavior
                  was the default in earlier PCP versions, but by default has
                  been disabled in PCP release from version 1.3 on.

           PCP_PMDAS_DIR
                  The PCP_PMDAS_DIR environment variable may be used to
                  modify the directory used by pmcd(1) and pmNewContext(3)
                  (for PM_CONTEXT_LOCAL contexts) when searching for a daemon
                  or DSO PMDA.

           PMCD_PORT
                  The TCP/IP port(s) used by pmcd(1) to create the socket for
                  incoming connections and requests, was historically 4321
                  and more recently the officially registered port 44321; in
                  the current release, both port numbers are used by default
                  as a transitional arrangement.  This may be over-ridden by
                  setting PMCD_PORT to a different port number, or a comma-
                  separated list of port numbers.  If a non-default port is
                  used when pmcd is started, then every monitoring
                  application connecting to that pmcd must also have
                  PMCD_PORT set in their environment before attempting a
                  connection.

           The following environment variables are relevant to installations
           in which pmlogger(1), the PCP archiver, is used.

           PMLOGGER_PORT
                  The environment variable PMLOGGER_PORT may be used to
                  change the base TCP/IP port number used by pmlogger(1) to
                  create the socket to which pmlc(1) instances will try and
                  connect.  The default base port number is 4330.  When used,
                  PMLOGGER_PORT should be set in the environment before
                  pmlogger is executed.

           PMLOGGER_REQUEST_TIMEOUT
                  When pmlc(1) connects to pmlogger(1), there is a remote
                  possibility of pmlc "hanging" on a request for information
                  as a consequence of a failure of the network or pmlogger.
                  By setting the environment variable
                  PMLOGGER_REQUEST_TIMEOUT to a number of seconds, requests
                  to pmlogger will timeout after this number of seconds.  The
                  default behavior is to be willing to wait forever for a
                  response from each request to a pmlogger.  When used,
                  PMLOGGER_REQUEST_TIMEOUT should be set in the environment
                  before pmlc is executed.

           If you have the PCP product installed, then the following
           environment variables are relevant to the Performance Metrics
           Domain Agents (PMDAs).

           PMDA_LOCAL_PROC
                  Use this variable has been deprecated and it is now
                  ignored.  If the ``proc'' PMDA is configured as a DSO for
                  use with pmcd(1) on the local host then all of the ``proc''
                  metrics will be available to applications using a
                  PM_CONTEXT_LOCAL context.

                  The previous behaviour was that if this variable was set,
                  then a context established with the type of
                  PM_CONTEXT_LOCAL will have access to the ``proc'' PMDA to
                  retrieve performance metrics about individual processes.

           PMDA_LOCAL_SAMPLE
                  Use this variable has been deprecated and it is now
                  ignored.  If the ``sample'' PMDA is configured as a DSO for
                  use with pmcd(1) on the local host then all of the
                  ``sample'' metrics will be available to applications using
                  a PM_CONTEXT_LOCAL context.

                  The previous behaviour was that if this variable was set,
                  then a context established with the type of
                  PM_CONTEXT_LOCAL will have access to the ``sample'' PMDA if
                  this optional PMDA has been installed locally.

           PCP_PMCDCONF_PATH
                  Overrides the path to the pmcd(1) configuration file.  When
                  set to $PCP_SYSCONF_DIR/local.conf, a PM_CONTEXT_LOCAL
                  context will load only the DSO PMDAs listed in that file,
                  without requiring pmcd(1) to be running.  This is the
                  recommended way to restrict local context to a minimal,
                  well-known set of DSO PMDAs.  Pair with PMNS_DEFAULT
                  (below) for a matching namespace.

           PMNS_DEFAULT
                  Overrides the default Performance Metrics Name Space used
                  when no explicit namespace is specified.  When set to
                  $PCP_VAR_DIR/pmns/local.root, a PM_CONTEXT_LOCAL context
                  will use the merged namespace for the DSO PMDAs listed in
                  $PCP_SYSCONF_DIR/local.conf, rather than the full system
                  namespace.  See also pmns(5) and PMNS_DEFAULT in
                  pcpintro(1).

           PMIECONF_PATH
                  If set, pmieconf(1) will form its pmieconf(5) specification
                  (set of parameterized pmie(1) rules) using all valid
                  pmieconf files found below each subdirectory in this colon-
                  separated list of subdirectories.  If not set, the default
                  is $PCP_VAR_DIR/config/pmieconf.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#SEE_ALSO)SEE ALSO

           pcp(1), pmcd(1), pmie(1), pmie_daily(1), pminfo(1), pmlc(1),
           pmlogger(1), pmlogger_daily(1), pmrep(1), pmstat(1), pmval(1),
           systemctl(1), LOGIMPORT(3), LOGARCHIVE(5), pcp.conf(5),
           pcp.env(5), PMNS(5) and chkconfig(8).

           If the PCP GUI package is installed, then the following entries
           are also relevant:
           pmchart(1), pmtime(1), and pmdumptext(1).

           If the secure sockets extensions have been enabled, then the
           following references are also relevant:
           https://pcp.io/documentation.html 
           https://pcp.readthedocs.io/en/latest/QG/EncryptedConnections.html 
           https://pcp.readthedocs.io/en/latest/QG/AuthenticatedConnections.html 

           Also refer to the books Performance Co-Pilot User's and
           Administrator's Guide and Performance Co-Pilot Programmer's Guide
           which can be found at https://pcp.readthedocs.io/en/latest/ .

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

    Performance Co-Pilot               PCP                        PCPINTRO(1)

------------------------------------------------------------------------

Pages that refer to this page: [atop-daily(1)](../man1/atop-daily.1.html),  [autofsd-probe(1)](../man1/autofsd-probe.1.html),  [collectl2pcp(1)](../man1/collectl2pcp.1.html),  [dbprobe(1)](../man1/dbprobe.1.html),  [guidellm2pcp(1)](../man1/guidellm2pcp.1.html),  [htop(1)](../man1/htop.1.html),  [indomcachectl(1)](../man1/indomcachectl.1.html),  [mkaf(1)](../man1/mkaf.1.html),  [pcp(1)](../man1/pcp.1.html),  [pcp2arrow(1)](../man1/pcp2arrow.1.html),  [pcp2elasticsearch(1)](../man1/pcp2elasticsearch.1.html),  [pcp2graphite(1)](../man1/pcp2graphite.1.html),  [pcp2influxdb(1)](../man1/pcp2influxdb.1.html),  [pcp2json(1)](../man1/pcp2json.1.html),  [pcp2openmetrics(1)](../man1/pcp2openmetrics.1.html),  [pcp2opentelemetry(1)](../man1/pcp2opentelemetry.1.html),  [pcp2spark(1)](../man1/pcp2spark.1.html),  [pcp2template(1)](../man1/pcp2template.1.html),  [pcp2xlsx(1)](../man1/pcp2xlsx.1.html),  [pcp2xml(1)](../man1/pcp2xml.1.html),  [pcp2zabbix(1)](../man1/pcp2zabbix.1.html),  [pcp-atop(1)](../man1/pcp-atop.1.html),  [pcp-atopsar(1)](../man1/pcp-atopsar.1.html),  [pcp-buddyinfo(1)](../man1/pcp-buddyinfo.1.html),  [pcp-check(1)](../man1/pcp-check.1.html),  [pcp-dmcache(1)](../man1/pcp-dmcache.1.html),  [pcp-dstat(1)](../man1/pcp-dstat.1.html),  [pcp-free(1)](../man1/pcp-free.1.html),  [pcp-geolocate(1)](../man1/pcp-geolocate.1.html),  [pcpintro(1)](../man1/pcpintro.1.html),  [pcp-iostat(1)](../man1/pcp-iostat.1.html),  [pcp-ipcs(1)](../man1/pcp-ipcs.1.html),  [pcp-meminfo(1)](../man1/pcp-meminfo.1.html),  [pcp-mpstat(1)](../man1/pcp-mpstat.1.html),  [pcp-netstat(1)](../man1/pcp-netstat.1.html),  [pcp-nfsiostat(1)](../man1/pcp-nfsiostat.1.html),  [pcp-numastat(1)](../man1/pcp-numastat.1.html),  [pcp-pidstat(1)](../man1/pcp-pidstat.1.html),  [pcp-ps(1)](../man1/pcp-ps.1.html),  [pcp-python(1)](../man1/pcp-python.1.html),  [pcp-reboot-init(1)](../man1/pcp-reboot-init.1.html),  [pcp-rocestat(1)](../man1/pcp-rocestat.1.html),  [pcp-shping(1)](../man1/pcp-shping.1.html),  [pcp-slabinfo(1)](../man1/pcp-slabinfo.1.html),  [pcp-ss(1)](../man1/pcp-ss.1.html),  [pcp-tapestat(1)](../man1/pcp-tapestat.1.html),  [pcp-uptime(1)](../man1/pcp-uptime.1.html),  [pcp-verify(1)](../man1/pcp-verify.1.html),  [pcp-xsos(1)](../man1/pcp-xsos.1.html),  [pcp-zoneinfo(1)](../man1/pcp-zoneinfo.1.html),  [pmcd(1)](../man1/pmcd.1.html),  [pmcd_wait(1)](../man1/pmcd_wait.1.html),  [pmchart(1)](../man1/pmchart.1.html),  [pmclient(1)](../man1/pmclient.1.html),  [pmdaactivemq(1)](../man1/pmdaactivemq.1.html),  [pmdaamdgpu(1)](../man1/pmdaamdgpu.1.html),  [pmdaapache(1)](../man1/pmdaapache.1.html),  [pmdabind2(1)](../man1/pmdabind2.1.html),  [pmdabonding(1)](../man1/pmdabonding.1.html),  [pmdabpf(1)](../man1/pmdabpf.1.html),  [pmdabpftrace(1)](../man1/pmdabpftrace.1.html),  [pmdabtrfs(1)](../man1/pmdabtrfs.1.html),  [pmdachrony(1)](../man1/pmdachrony.1.html),  [pmdacifs(1)](../man1/pmdacifs.1.html),  [pmdadarwin(1)](../man1/pmdadarwin.1.html),  [pmdadb2(1)](../man1/pmdadb2.1.html),  [pmdadbping(1)](../man1/pmdadbping.1.html),  [pmdadenki(1)](../man1/pmdadenki.1.html),  [pmdadm(1)](../man1/pmdadm.1.html),  [pmdadocker(1)](../man1/pmdadocker.1.html),  [pmdads389(1)](../man1/pmdads389.1.html),  [pmdads389log(1)](../man1/pmdads389log.1.html),  [pmdaelasticsearch(1)](../man1/pmdaelasticsearch.1.html),  [pmdafarm(1)](../man1/pmdafarm.1.html),  [pmdagfs2(1)](../man1/pmdagfs2.1.html),  [pmdagluster(1)](../man1/pmdagluster.1.html),  [pmdagpfs(1)](../man1/pmdagpfs.1.html),  [pmdahacluster(1)](../man1/pmdahacluster.1.html),  [pmdahaproxy(1)](../man1/pmdahaproxy.1.html),  [pmdahdb(1)](../man1/pmdahdb.1.html),  [pmdaib(1)](../man1/pmdaib.1.html),  [pmdajbd2(1)](../man1/pmdajbd2.1.html),  [pmdakernel(1)](../man1/pmdakernel.1.html),  [pmdakvm(1)](../man1/pmdakvm.1.html),  [pmdalibvirt(1)](../man1/pmdalibvirt.1.html),  [pmdalio(1)](../man1/pmdalio.1.html),  [pmdalmsensors(1)](../man1/pmdalmsensors.1.html),  [pmdalogger(1)](../man1/pmdalogger.1.html),  [pmdalustre(1)](../man1/pmdalustre.1.html),  [pmdalustrecomm(1)](../man1/pmdalustrecomm.1.html),  [pmdamailq(1)](../man1/pmdamailq.1.html),  [pmdamemcache(1)](../man1/pmdamemcache.1.html),  [pmdammv(1)](../man1/pmdammv.1.html),  [pmdamongodb(1)](../man1/pmdamongodb.1.html),  [pmdamounts(1)](../man1/pmdamounts.1.html),  [pmdamssql(1)](../man1/pmdamssql.1.html),  [pmdamysql(1)](../man1/pmdamysql.1.html),  [pmdanetcheck(1)](../man1/pmdanetcheck.1.html),  [pmdanetfilter(1)](../man1/pmdanetfilter.1.html),  [pmdanfsclient(1)](../man1/pmdanfsclient.1.html),  [pmdanginx(1)](../man1/pmdanginx.1.html),  [pmdanixl(1)](../man1/pmdanixl.1.html),  [pmdanutcracker(1)](../man1/pmdanutcracker.1.html),  [pmdanvidia(1)](../man1/pmdanvidia.1.html),  [pmdaopenmetrics(1)](../man1/pmdaopenmetrics.1.html),  [pmdaopentelemetry(1)](../man1/pmdaopentelemetry.1.html),  [pmdaopenvswitch(1)](../man1/pmdaopenvswitch.1.html),  [pmdaoracle(1)](../man1/pmdaoracle.1.html),  [pmdaoverhead(1)](../man1/pmdaoverhead.1.html),  [pmdaperfevent(1)](../man1/pmdaperfevent.1.html),  [pmdapipe(1)](../man1/pmdapipe.1.html),  [pmdapodman(1)](../man1/pmdapodman.1.html),  [pmdapostfix(1)](../man1/pmdapostfix.1.html),  [pmdapostgresql(1)](../man1/pmdapostgresql.1.html),  [pmdaproc(1)](../man1/pmdaproc.1.html),  [pmdarabbitmq(1)](../man1/pmdarabbitmq.1.html),  [pmdards(1)](../man1/pmdards.1.html),  [pmdaredis(1)](../man1/pmdaredis.1.html),  [pmdaresctrl(1)](../man1/pmdaresctrl.1.html),  [pmdarocestat(1)](../man1/pmdarocestat.1.html),  [pmdaroot(1)](../man1/pmdaroot.1.html),  [pmdarsyslog(1)](../man1/pmdarsyslog.1.html),  [pmdasample(1)](../man1/pmdasample.1.html),  [pmdasendmail(1)](../man1/pmdasendmail.1.html),  [pmdashping(1)](../man1/pmdashping.1.html),  [pmdasimple(1)](../man1/pmdasimple.1.html),  [pmdaslurm(1)](../man1/pmdaslurm.1.html),  [pmdasmart(1)](../man1/pmdasmart.1.html),  [pmdasockets(1)](../man1/pmdasockets.1.html),  [pmdastatsd(1)](../man1/pmdastatsd.1.html),  [pmdasummary(1)](../man1/pmdasummary.1.html),  [pmdasystemd(1)](../man1/pmdasystemd.1.html),  [pmdatrace(1)](../man1/pmdatrace.1.html),  [pmdatrivial(1)](../man1/pmdatrivial.1.html),  [pmdatxmon(1)](../man1/pmdatxmon.1.html),  [pmdaunbound(1)](../man1/pmdaunbound.1.html),  [pmdauwsgi(1)](../man1/pmdauwsgi.1.html),  [pmdavalkey(1)](../man1/pmdavalkey.1.html),  [pmdaxfs(1)](../man1/pmdaxfs.1.html),  [pmdazfs(1)](../man1/pmdazfs.1.html),  [pmdazimbra(1)](../man1/pmdazimbra.1.html),  [pmdazswap(1)](../man1/pmdazswap.1.html),  [pmdbg(1)](../man1/pmdbg.1.html),  [pmdiff(1)](../man1/pmdiff.1.html),  [pmdumptext(1)](../man1/pmdumptext.1.html),  [pmfind(1)](../man1/pmfind.1.html),  [pmfind_check(1)](../man1/pmfind_check.1.html),  [pmgetopt(1)](../man1/pmgetopt.1.html),  [pmie(1)](../man1/pmie.1.html),  [pmie2col(1)](../man1/pmie2col.1.html),  [pmie_check(1)](../man1/pmie_check.1.html),  [pmieconf(1)](../man1/pmieconf.1.html),  [pminfo(1)](../man1/pminfo.1.html),  [pmlc(1)](../man1/pmlc.1.html),  [pmlogbasename(1)](../man1/pmlogbasename.1.html),  [pmlogcheck(1)](../man1/pmlogcheck.1.html),  [pmlogcompress(1)](../man1/pmlogcompress.1.html),  [pmlogctl(1)](../man1/pmlogctl.1.html),  [pmlogdump(1)](../man1/pmlogdump.1.html),  [pmlogextract(1)](../man1/pmlogextract.1.html),  [pmlogger(1)](../man1/pmlogger.1.html),  [pmlogger_check(1)](../man1/pmlogger_check.1.html),  [pmlogger_daily(1)](../man1/pmlogger_daily.1.html),  [pmlogger_daily_report(1)](../man1/pmlogger_daily_report.1.html),  [pmlogger_janitor(1)](../man1/pmlogger_janitor.1.html),  [pmlogger_merge(1)](../man1/pmlogger_merge.1.html),  [pmlogger_rewrite(1)](../man1/pmlogger_rewrite.1.html),  [pmloglabel(1)](../man1/pmloglabel.1.html),  [pmlogmv(1)](../man1/pmlogmv.1.html),  [pmlogpaste(1)](../man1/pmlogpaste.1.html),  [pmlogpush(1)](../man1/pmlogpush.1.html),  [pmlogreduce(1)](../man1/pmlogreduce.1.html),  [pmlogrewrite(1)](../man1/pmlogrewrite.1.html),  [pmlogsize(1)](../man1/pmlogsize.1.html),  [pmlogsummary(1)](../man1/pmlogsummary.1.html),  [pmprobe(1)](../man1/pmprobe.1.html),  [pmproxy(1)](../man1/pmproxy.1.html),  [pmpython(1)](../man1/pmpython.1.html),  [pmrep(1)](../man1/pmrep.1.html),  [pmsearch(1)](../man1/pmsearch.1.html),  [pmseries(1)](../man1/pmseries.1.html),  [pmsleep(1)](../man1/pmsleep.1.html),  [pmstat(1)](../man1/pmstat.1.html),  [pmtime(1)](../man1/pmtime.1.html),  [pmval(1)](../man1/pmval.1.html),  [pmview(1)](../man1/pmview.1.html),  [telnet-probe(1)](../man1/telnet-probe.1.html),  [vllmbench2pcp(1)](../man1/vllmbench2pcp.1.html),  [pcpintro(3)](../man3/pcpintro.3.html),  [pmaddderived(3)](../man3/pmaddderived.3.html),  [pmaddderivedtext(3)](../man3/pmaddderivedtext.3.html),  [pmapi(3)](../man3/pmapi.3.html),  [pmdagetoptions(3)](../man3/pmdagetoptions.3.html),  [pmderivederrstr(3)](../man3/pmderivederrstr.3.html),  [pmgetconfig(3)](../man3/pmgetconfig.3.html),  [pmgetcontexthostname(3)](../man3/pmgetcontexthostname.3.html),  [pmgetderivedcontrol(3)](../man3/pmgetderivedcontrol.3.html),  [pmgetoptions(3)](../man3/pmgetoptions.3.html),  [pmiaddmetric(3)](../man3/pmiaddmetric.3.html),  [pmloadderivedconfig(3)](../man3/pmloadderivedconfig.3.html),  [\_\_pmlogwritemark(3)](../man3/__pmlogwritemark.3.html),  [pmparsehostattrsspec(3)](../man3/pmparsehostattrsspec.3.html),  [pmparsehostspec(3)](../man3/pmparsehostspec.3.html),  [pmparseinterval(3)](../man3/pmparseinterval.3.html),  [pmparsemetricspec(3)](../man3/pmparsemetricspec.3.html),  [pmparsetimewindow(3)](../man3/pmparsetimewindow.3.html),  [pmregisterderived(3)](../man3/pmregisterderived.3.html),  [pmsetdebug(3)](../man3/pmsetdebug.3.html),  [pmunregisterderived(3)](../man3/pmunregisterderived.3.html),  [pmwebapi(3)](../man3/pmwebapi.3.html),  [zbxpcp(3)](../man3/zbxpcp.3.html),  [LOGARCHIVE(5)](../man5/LOGARCHIVE.5.html),  [mmv(5)](../man5/mmv.5.html),  [pcp-atoprc(5)](../man5/pcp-atoprc.5.html),  [pcp.conf(5)](../man5/pcp.conf.5.html),  [pcp-dstat(5)](../man5/pcp-dstat.5.html),  [pcp.env(5)](../man5/pcp.env.5.html),  [pmlogger.control(5)](../man5/pmlogger.control.5.html),  [pmns(5)](../man5/pmns.5.html),  [pmrep.conf(5)](../man5/pmrep.conf.5.html)

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
