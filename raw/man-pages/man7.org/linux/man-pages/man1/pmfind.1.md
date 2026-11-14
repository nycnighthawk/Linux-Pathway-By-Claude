---
{"title": "pmfind(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmfind.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmfind(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MECHANISMS](#MECHANISMS) \| [SIGNALS](#SIGNALS) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMFIND(1)                General Commands Manual                PMFIND(1)

## [](#NAME)NAME

           pmfind - find PCP services on the network

## [](#SYNOPSIS)SYNOPSIS

           pmfind [-CqrSV?]  [-D debug] [-m mechanism] [-s service] [-t
           timeout]

## [](#DESCRIPTION)DESCRIPTION

           pmfind searches for instances of the specified PCP service being
           advertised on the network and prints a list of URLs corresponding
           to the services discovered.  It can be used in conjunction with
           pmfind_check(1) to automate the monitoring of remote PCP collector
           systems.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -C, --containers
                Performs containers discovery as well, for each discovered
                pmcd(1) service.

           -m mechanism, --mechanism=mechanism
                This option sets the mechanism that pmfind uses when
                performing service discovery.  By default, or if the keyword
                all is specified, every available mechanism will be used
                (iteratively).  See the ``MECHANISMS'' section for a
                description of each available discovery mechanism.

           -q, --quiet
                This option suppresses all output on the standard output
                stream.

           -r, --resolve
                Requests that DNS name resolution be attempted for the
                addresses of any discovered services.  The default is to
                display the network addresses of any discovered services.

           -s service, --service=service
                By default pmfind will search for all supported PCP services,
                however a specific PCP service to discover can be specified
                using the -s option.  Supported services are pmcd(1), and
                pmproxy(1).

           -S, --sources
                Reports source identifiers for each discovered pmcd(1)
                service.  These identifiers are unique for each host, and are
                formed using the (non-optional) context labels available for
                every PCP collector.  Because the discovery process will
                often identify multiple paths to an individual collector
                host, this option is an important part of the process of
                using pmfind in conjunction with pmfind_check(1), to ensure
                only one pmie(1) and/or pmlogger(1) process is started for
                each discovered collector host.  The source identifiers
                reported by pmfind are the same as the source identifiers
                reported by the pminfo(1) and pmseries(1) commands.

           -t seconds, --timeout=seconds
                Sets the maximum amount of time in seconds that pmfind will
                take before interrupting the service discovery.  The time
                argument is a floating point number representing the number
                of seconds before timing out.  The default is to take as much
                time as is needed to complete the process.

           -V, --version
                Display version number and exit.

           -?, --help
                Display usage message and exit.

## [](#MECHANISMS)MECHANISMS

           Supported mechanisms for service discovery are:

           probe=<net-address>/<mask-bits>
                  Actively probes the given subnet for the requested PCP
                  service(s).  <net-address> is an Inet or IPv6 network
                  address and <mask-bits> is the number of bits used to
                  define the subnet.  For example, 192.168.1.0/24 defines an
                  8 bit subnet consisting of the addresses 192.168.1.0
                  through 192.168.1.255.  An optional suffix ",maxThreads=N"
                  may be added to limit the number of threads used while
                  probing.  The default is the value of FD_SETSIZE (which is
                  typically 1024) or the number of addresses in the subnet,
                  whichever is less.  An optional suffix ",timeout=N" may be
                  added to limit the amount of time spent waiting for each
                  connection attempt.  N is a floating point number
                  specifying the number of seconds to wait.  The default is
                  0.02 seconds (20 milliseconds).

           shell  Probes the list of addresses provided by scripts for
                  requested PCP service(s).  Several optional, comma-
                  separated parameters can also be provided.  The "path=DIR"
                  option specifies the directory where commands like
                  pcp-kube-pods(1) are located (defaults to
                  $PCP_BINADM_DIR/discover/).  This setting can be further
                  restricted to an individual command using the command=CMD
                  option, but the default is to use all available commands
                  from the path.  The "maxThreads=N" option limits the number
                  of threads used while probing.  The default is the value of
                  FD_SETSIZE (which is typically 1024) or the number of
                  addresses returned by the scripts, whichever is less.  The
                  "timeout=N" option may be added to limit the amount of time
                  spent waiting for each connection attempt.  N is a floating
                  point number specifying the number of seconds to wait.  The
                  default is 0.02 seconds (20 milliseconds).

## [](#SIGNALS)SIGNALS

           pmfind will interrupt the service discovery process when one of
           the following signals is received: SIGHUP, SIGPIPE, SIGINT,
           SIGTERM, SIGXFSZ, SIGXCPU.  pmfind will report any results which
           were discovered up to point of the interruption.

## [](#DIAGNOSTICS)DIAGNOSTICS

           The value of the exit status from the command is zero when
           services were successfully located, one if no services were found,
           and two if an error occurred.

           In the event of an error a message will be generated on standard
           error that is intended to be self-explanatory.

## [](#FILES)FILES

           $PCP_BINADM_DIR/discover
                default path to address discovery scripts

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

           PCPIntro(1), pmcd(1), pmfind_check(1), pmie(1), pminfo(1),
           pmlogger(1), pmproxy(1), pmseries(1), pcp-kube-pods(1), PMAPI(3),
           PMWEBAPI(3), pmDiscoverServices(3), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                          PMFIND(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcpcompat(1)](../man1/pcpcompat.1.html),  [pcp-kube-pods(1)](../man1/pcp-kube-pods.1.html),  [pmfind_check(1)](../man1/pmfind_check.1.html),  [pmlogctl(1)](../man1/pmlogctl.1.html),  [pmdiscoverservices(3)](../man3/pmdiscoverservices.3.html)

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
