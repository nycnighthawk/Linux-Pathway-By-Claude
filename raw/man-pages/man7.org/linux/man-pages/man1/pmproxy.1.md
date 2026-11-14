---
{"title": "pmproxy(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmproxy.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmproxy(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION](#CONFIGURATION) \| [STARTING AND STOPPING PMPROXY](#STARTING_AND_STOPPING_PMPROXY) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [FILES](#FILES) \| [ENVIRONMENT](#ENVIRONMENT) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMPROXY(1)               General Commands Manual               PMPROXY(1)

## [](#NAME)NAME

           pmproxy - proxy for performance metrics collector and querying

## [](#SYNOPSIS)SYNOPSIS

           pmproxy [-AdfFt?]  [-c conffile] [-D debug] [-h host[,host ...]
           [-i ipaddress] [-l logfile] [-L bytes] [-p port[,port ...]  [-r
           port[,port ...]  [-s sockname] [-U username] [-x outfile]

## [](#DESCRIPTION)DESCRIPTION

           pmproxy acts as a protocol proxy, allowing Performance Co-Pilot
           (PCP) monitoring clients to connect to one or more pmcd(1) and/or
           key-value servers (such as https://valkey.io/ ) indirectly.

           In its default mode of operation pmproxy provides the REST API for
           PCP services (see PMWEBAPI(3) for details).  This includes
           provision of an Open Metrics - https://openmetrics.io  - text
           interface for PCP metrics at /metrics, real-time access to PCP
           metrics through the /pmapi interfaces, and access to the fast,
           scalable PCP time series query capabilities offered in conjunction
           with a key-value server (see pmseries(1) for details) via the
           /query REST interfaces.

           pmproxy can be deployed in a firewall domain, or on a cluster
           ``head'' node where the IP (Internet Protocol) address of the
           hosts where pmcd and/or a key-value server (such as
           https://valkey.io/ ) are running may be unknown to the PCP
           monitoring clients, but where the IP address of the host running
           pmproxy is known to these clients.  Similarly, the clients may
           have network connectivity only to the host where pmproxy is
           running, while there is network connectivity from that host to the
           hosts of interest where pmcd and/or a key-value server are
           running.

           The behaviour of the PCP monitoring clients is controlled by
           either the PMPROXY_HOST environment variable or through the
           extended hostname specification (see PCPIntro(1) for details).  If
           neither of these mechanisms is used, clients will make their
           PMAPI(3) connections directly to pmcd.  If the proxy hostname
           syntax is used or PMPROXY_HOST is set, then this should be the
           hostname or IP address of the system where pmproxy is running, and
           the clients will connect to pmcd or a key-value server indirectly
           through the protocol proxy services of pmproxy.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -A   Disable service advertisement.  By default, pmproxy will
                advertise its presence on the network using any available
                mechanisms, assisting remote monitoring tools with finding
                it.  These mechanisms are disabled with this option.

           -c conffile, --config=conffile
                Specify the path to an optional configuration conffile, with
                format as described in the ``CONFIGURATION'' section.  This
                option implies pmproxy is running in timeseries mode.

           -d, --deprecated
                By default pmproxy prefers to run in the new timeseries mode,
                providing REST APIs, asynchronous network I/O, scalable time
                series, and secure connections using OpenSSL.  However,
                legacy deployments may wish to use the original synchronous
                pmproxy implementation using libpcp networking; this can be
                achieved using this option.  Note that the -d and -t options
                are mutually exclusive.

           -f, --foreground
                By default pmproxy is started as a daemon.  The -f option
                indicates that it should run in the foreground.  This is most
                useful when trying to diagnose problems with establishing
                connections.

           -F, --managed
                Like -f, the -F option runs pmproxy in the foreground, but
                also does some housekeeping (like create a ``pid'' file and
                change user id).  This is intended for use when pmproxy is
                launched from systemd(1) or launchd(1) and the daemonising
                has already been done by systemd(1) or launchd(1) and does
                not need to be done again by pmproxy, which is the case when
                neither -f nor -F is specified.

                At most one of -f and -F may be specified.

           -h host, --keyhost=host
                Specify an alternate key-value server host to connect to for
                time series querying, overriding any configuration file
                settings.  This option implies pmproxy is running in
                timeseries mode.

           -i ipaddress, --interface=ipaddress
                This option is usually only used on hosts with more than one
                network interface (very common for firewall and ``head'' node
                hosts where pmproxy is likely to be deployed to arbitrate
                access to an internal network).  If no -i options are
                specified pmproxy accepts PCP client connections on any of
                its host's IP addresses.  The -i option is used to specify
                explicitly an IP address that PCP client connections should
                be accepted on.  ipaddress should be in the standard dotted
                form (e.g. 100.23.45.6).  The -i option may be used multiple
                times to define a list of IP addresses.  When one or more -i
                options is specified, attempted connections made on any other
                IP addresses will be refused.

           -l logfile, --log=logfile
                By default a log file named pmproxy.log is written in the
                current directory.  The -l option causes the log file to be
                written to a given logfile instead of the default.  If this
                logfile cannot be created or is not writable, output is
                written to the standard error instead.

           -L bytes
                PDUs received by pmproxy from PCP monitoring clients are
                restricted to a maximum size of 65536 bytes by default to
                defend against Denial of Service attacks.  The -L option may
                be used to change the maximum incoming PDU size.

           -p port, --port=port
                Specify an alternate port number to listen on for client
                connections.  The default value is 44322.

           -Q, --certreqd
                Require that all client connections provide a trusted client
                certificate.

           -r port, --keyport=port
                Specify an alternate key-value server port number to connect
                to for time series querying, overriding any configuration
                file settings.  This option implies pmproxy is running in
                timeseries mode.

           -s sockname, --socket=sockname
                Specify the path to a local unix domain socket (for platforms
                supporting this socket family only).  The default value is
                $PCP_RUN_DIR/pmproxy.socket.  This option implies pmproxy is
                running in timeseries mode.

           -S, --reqauth
                Require that all client connections be authenticated.

           -t, --timeseries
                Operate in automatic archive timeseries discovery mode.  This
                mode of operation will enable the PMWEBAPI(3) REST APIs,
                dynamically and automatically detect active system archives
                being written by pmlogger(1) and import them into a key-value
                server (such as https://valkey.io/ ), for fast, scalable time
                series querying described in pmseries(1).  Note that in this
                mode of operation, pmproxy only "log-tails" and ingests
                actively growing archives, e.g. as written by one or more
                pmlogger(1) instances.  When an archive is first discovered
                (usually but not limited to pmproxy startup), all metadata is
                loaded and sent to the configured key-value server however
                note that only new archive metric value data from the tail
                end of each archive is ingested.  Compressed archives never
                grow and so are ignored.  See the --load option to
                pmseries(1) for a supported mechanism for manually loading
                all of the metric value data from previously collected
                (inactive) archives, whether compressed or not.  It would be
                normal, though not mandated, for a set of archives being
                manually loaded to cover the same time period, e.g. archive
                data for a particular week for one or more hosts in the same
                data-centre.

           -U username, --username=username
                Assume the identity of the given username before starting to
                accept incoming packets from PCP monitoring clients.

           -x outfile
                Before the pmproxy logfile can be opened, pmproxy may
                encounter a fatal error which prevents it from starting.  By
                default the output describing this error is sent to /dev/tty
                but it may redirected to outfile.

           -?, --help
                Display usage message and exit.

## [](#CONFIGURATION)CONFIGURATION

           When running in the timeseries mode of operation, runtime
           configuration is relatively complex and typically handled via the
           $PCP_SYSCONF_DIR/pmproxy/pmproxy.conf file.  This file is in the
           common ``ini'' format, with section headers and individual
           variables and values with each section.  The configuration file
           installed as part of PCP documents every available section and
           option.

           At a high level, the [pmproxy] section can be used to explicitly
           enable or disable each of the different protocols.

           The [http] section provides fine-tuning over HTTP server settings
           used by pmproxy.  chunksize sets the chunked transfer encoding
           buffer size, and defaults to the system pagesize.  Access control
           HTTP protocol settings can be adjusted using the Access-Control-
           Allow-Headers and Access-Control-Max-Age options.  Discussion of
           these HTTP protocol headers is beyond the scope of this document,
           but suitable default values are described within the pmproxy.conf
           configuration file.

           The [keys] section allows connection information for one or more
           backing key-value server processes to be configured (hostnames and
           ports).  Note to access multiple (scalable) key-value servers, the
           servers variable in this section can be a comma-separated list of
           hostname:port pairs.  Alternatively, it can be a single key-value
           server host that will be queried using the "CLUSTER INFO" command
           to automatically configure multiple backing hosts.

           In earlier versions of PCP (before 6) an alternative configuration
           setting section was used for this purpose - key-value servers were
           specified in the [pmseries] section and this is still accepted as
           a fallback for backwards compatibility.

## [](#STARTING_AND_STOPPING_PMPROXY)STARTING AND STOPPING PMPROXY

           Normally, pmproxy is started automatically at boot time and
           stopped when the system is being brought down.  Under certain
           circumstances it is necessary to start or stop pmproxy manually.
           To do this one must become superuser and type

           # $PCP_RC_DIR/pmproxy start

           to start pmproxy, or

           # $PCP_RC_DIR/pmproxy stop

           to stop pmproxy.  Starting pmproxy when it is already running is
           the same as stopping it and then starting it again.

           Normally pmproxy listens for PCP client connections on TCP/IP port
           number 44322 (as well as 44323 with timeseries enabled) registered
           at https://www.iana.org/ .  Either the environment variable
           PMPROXY_PORT or the -p command line option may be used to specify
           alternative port number(s) when pmproxy is started; in each case,
           the specification is a comma-separated list of one or more
           numerical port numbers.  Should both methods be used or multiple
           -p options appear on the command line, pmproxy will listen on the
           union of the set of ports specified via all -p options and the
           PMPROXY_PORT environment variable.  If non-default ports are used
           with pmproxy care should be taken to ensure that PMPROXY_PORT is
           also set in the environment of any client application that will
           connect to pmproxy, or that the extended host specification syntax
           is used (see PCPIntro(1) for details).

## [](#DIAGNOSTICS)DIAGNOSTICS

           If pmproxy is already running the message "Error:
           OpenRequestSocket bind: Address already in use" will appear.  This
           may also appear if pmproxy was shutdown with an outstanding
           request from a client.  In this case, a request socket has been
           left in the TIME_WAIT state and until the system closes it down
           (after some timeout period) it will not be possible to run
           pmproxy.

           In addition to the standard PCP debugging options, see pmdbg(1),
           pmproxy currently supports the debugging option context for
           tracing client connections and disconnections.

## [](#FILES)FILES

           $PCP_PMPROXYOPTIONS_PATH
                command line options for pmproxy when launched from
                $PCP_RC_DIR/pmproxy All the command line option lines should
                start with a hyphen as the first character.

           $PCP_SYSCONFIG_DIR/pmproxy
                Environment variables that will be set when pmproxy executes.
                Only settings of the form "PMPROXY_VARIABLE=value" will be
                honoured.

           ./pmproxy.log
                (or $PCP_LOG_DIR/pmproxy/pmproxy.log when started
                automatically)
                All messages and diagnostics are directed here

           /etc/pki/tls
                default OpenSSL certificate database directory, optionally
                used for Secure Socket Layer connection in timeseries mode of
                operation.  These certificates can be created and queried
                using the openssl tool, amongst others.

## [](#ENVIRONMENT)ENVIRONMENT

           In addition to the PCP environment variables described in the PCP
           ENVIRONMENT section below, there are several environment variables
           that influence the interactions between a PCP monitoring client,
           pmproxy and pmcd.

           PMCD_PORT
                  For the PCP monitoring client this (or the default port
                  number) is passed to pmproxy and used to connect to pmcd.
                  In the environment of pmproxy PMCD_PORT is not used.

           PMPROXY_HOST
                  For the PCP monitoring client this is the hostname or IP
                  address of the host where pmproxy is running.  In recent
                  versions of PCP (since version 3) this has been superseded
                  by the extended hostname syntax (see PCPIntro(1) for
                  details).

           PMPROXY_PORT
                  For the PCP monitoring client this is the port on which
                  pmproxy will accept connections.  The default is 44322, as
                  well as 44323 with timeseries enabled.

           PMCD_CONNECT_TIMEOUT, PMCD_RECONNECT_TIMEOUT and
           PMCD_REQUEST_TIMEOUT
                  (see PCPIntro(1)) For the PCP monitoring client, setting
                  these environment variables will modify the timeouts used
                  for interactions between the client and pmproxy
                  (independent of which pmcd is being used).  For pmproxy
                  these same environment variables control the timeouts
                  between pmproxy and all pmcd(1) instances (independent of
                  which monitoring client is involved).

           If set to the value 1, the PMPROXY_LOCAL environment variable will
           cause pmproxy to run in a localhost-only mode of operation, where
           it binds only to the loopback interface.

           The PMPROXY_MAXPENDING variable can be set to indicate the maximum
           length to which the queue of pending client connections may grow.

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

           Debugging options specific to pmproxy are as follows:
           ┌────────┬───────────────────────────────────────────────────────┐
           │ Option │ Description                                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl0  │ client connections and disconnections                 │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl1  │ desperate logging mode, where a period followed by    │
           │        │ the PID of pmproxy is inserted in the name of         │
           │        │ Rlogfile before the last period, so for example       │
           │        │ pmproxy.log becomes pmproxy.<pid>.log                 │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl2  │ log incoming HTTP URLs (this is also enabled by the   │
           │        │ http debugging option, but the latter has broader     │
           │        │ scope because it turns on debugging in the libraries  │
           │        │ that pmproxy uses)                                    │
           └────────┴───────────────────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmdbg(1), pmlogger(1), pmseries(1),
           PMAPI(3), PMWEBAPI(3), pmGetOptions(3), pcp.conf(5) and
           pcp.env(5).

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

    Performance Co-Pilot               PCP                         PMPROXY(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcp(1)](../man1/pcp.1.html),  [pcp-check(1)](../man1/pcp-check.1.html),  [pcpcompat(1)](../man1/pcpcompat.1.html),  [pcpintro(1)](../man1/pcpintro.1.html),  [pcp-kube-pods(1)](../man1/pcp-kube-pods.1.html),  [pmfind(1)](../man1/pmfind.1.html),  [pmlogger(1)](../man1/pmlogger.1.html),  [pmlogger_daily(1)](../man1/pmlogger_daily.1.html),  [pmlogpush(1)](../man1/pmlogpush.1.html),  [pmsearch(1)](../man1/pmsearch.1.html),  [pmseries(1)](../man1/pmseries.1.html),  [pmseries_import(1)](../man1/pmseries_import.1.html),  [pmsocks(1)](../man1/pmsocks.1.html),  [pmdiscoverservices(3)](../man3/pmdiscoverservices.3.html),  [pmdiscoversetup(3)](../man3/pmdiscoversetup.3.html),  [pmnewcontext(3)](../man3/pmnewcontext.3.html),  [pmparsehostattrsspec(3)](../man3/pmparsehostattrsspec.3.html),  [pmparsehostspec(3)](../man3/pmparsehostspec.3.html),  [pmsearchinfo(3)](../man3/pmsearchinfo.3.html),  [pmsearchsetup(3)](../man3/pmsearchsetup.3.html),  [pmsearchtextindom(3)](../man3/pmsearchtextindom.3.html),  [pmsearchtextquery(3)](../man3/pmsearchtextquery.3.html),  [pmsearchtextsuggest(3)](../man3/pmsearchtextsuggest.3.html),  [pmseriesdescs(3)](../man3/pmseriesdescs.3.html),  [pmseriesquery(3)](../man3/pmseriesquery.3.html),  [pmseriessetup(3)](../man3/pmseriessetup.3.html),  [pmwebapi(3)](../man3/pmwebapi.3.html),  [pmwebtimerregister(3)](../man3/pmwebtimerregister.3.html),  [labels.conf(5)](../man5/labels.conf.5.html),  [pmlogger.control(5)](../man5/pmlogger.control.5.html)

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
