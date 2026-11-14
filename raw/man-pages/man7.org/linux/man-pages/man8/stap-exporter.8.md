---
{"title": "stap-exporter(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/stap-exporter.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stap-exporter(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OPERATION](#OPERATION) \| [EXAMPLE](#EXAMPLE) \| [SAFETY AND SECURITY](#SAFETY_AND_SECURITY) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STAP-EXPORTER(8)         System Manager's Manual         STAP-EXPORTER(8)

## [](#NAME)NAME

           stap-exporter - systemtap-prometheus interoperation mechanism

## [](#SYNOPSIS)SYNOPSIS

           stap-exporter [ OPTIONS ]

## [](#DESCRIPTION)DESCRIPTION

           stap-exporter runs a set of systemtap scripts and relays their
           procfs outputs to remote HTTP clients on demand.  This makes
           systemtap scripts directly usable as individual prometheus
           exporters.  This is assisted by a set of macros provided in the
           prometheus.stpm tapset file.

## [](#OPTIONS)OPTIONS

           The stap-exporter program supports the following options.

           -p --port PORT
                  Listen to the specified TCP port for HTTP requests. Port
                  9900 is used by default.

           -k --keepalive KEEPALIVE
                  Scripts that run longer than KEEPALIVE seconds beyond the
                  last request are shut down.  There is no timeout by
                  default, so once started, scripts are kept running.

           -s --scripts SCRIPTS
                  Search the directory SCRIPTS for *.stp files to be exposed.
                  The default is given in the stappaths.7 man page.

           -h --help
                  Print help message.

## [](#OPERATION)OPERATION

           Upon startup, stap-exporter searches the directory specified by
           the -s directory for files named *.stp.  The name of each file
           becomes available as a URL component for subsequent GET HTTP
           requests.  For example, when an HTTP client asks for /foo.stp, and
           the foo.stp script (executable / shell-script) was known, then it
           is spawned with additional stap options to set a module name.
           This predictable module name makes it possible for stap-exporter
           to transcribe a procfs file from that running script to HTTP
           clients.

           After a configurable period of disuse (-k or --keepalive option),
           a systemtap script is terminated.  It will be restarted again if a
           client requests.

           All files whose name includes the substring autostart are started
           immediately (and restarted if they stop), rather than on-demand.
           These are excluded from keepalive considerations.  Scripts that
           may be too slow to start or wish to report long-term statistics
           are candidates for this treatment.

## [](#EXAMPLE)EXAMPLE

           Suppose that example.stp contains the following script.  It counts
           read syscalls on a per-thread & per-cpu basis.

                  global arr%

                  probe syscall.read {
                      arr[tid(), cpu()]++
                  }

                  probe prometheus {
                      @prometheus_dump_array2(arr, "count", "tid", "cpu")
                  }

           The prometheus_dump_array macros are used to produce metrics from
           an array.  Systemtap provides a prometheus_dump_arrayN macro for
           all N from 1 to 8.  The first argument of the macros represents an
           array with N-element keys.  The second argument represents the
           name of the metric. The remaining N arguments represent the names
           of the metric's labels.

           One may launch stap-exporter as root, or equivalent stapdev privi‐
           leges, then after a brief delay, use any web client to fetch data:

                  # stap-exporter -p 9999 -k 60 -c . &

                  $ curl http://localhost:9999/example.stp
                  Refresh page to access metrics.  [...]

                  $ curl http://localhost:9999/example.stp
                  count{tid="12614",cpu="0"} 9
                  count{tid="12170",cpu="3"} 107
                  count{tid="1802",cpu="0"} 33687
                  count{tid="12617",cpu="1"} 99
                  [...]

           The same URL may be added to a Prometheus server's scrape_config
           section, or a Performance Co-Pilot pmdaprometheus config.d direc‐
           tory, to collect this data into a monitoring system.

## [](#SAFETY_AND_SECURITY)SAFETY AND SECURITY

           The stap-exporter server does not enforce any particular security
           mechanisms.  Therefore, deployment in an untrusted environment
           needs to consider:

           script selection
                  Since systemtap scripts are run under the privileges of the
                  stap-exporter process (probably root), the system adminis‐
                  trator must select only safe & robust scripts.  Check the
                  scripts installed by default before activating the service.
                  Scripts cannot take input from the web clients.

           TCP/IP firewalling
                  Since stap-exporter exposes the selected TCP/HTTP port to
                  all interfaces on the host, it may be necessary to add a
                  firewall.  It is unlikely to be appropriate to expose such
                  a service to an untrusted network.

           HTTP filtering
                  Since stap-exporter exposes the configured systemtap
                  scripts to all HTTP clients without authentication, it may
                  be necessary to protect it from abuse even on mostly trust‐
                  ed networks.  An HTTP proxy may be used to impose URL- or
                  client- or usage- or authentication-dependent filters.

           HTTPS  Since stap-exporter speaks only plain HTTP, an HTTP proxy
                  may be used to support HTTPS secure protocols.

## [](#SEE_ALSO)SEE ALSO

           stap(1), stapprobes(3stap), stappaths(7) tapset::prometheus(7)

## [](#BUGS)BUGS

           Use the Bugzilla link of the project web page or our mailing list.
           http://sourceware.org/systemtap/ , <systemtap@sourceware.org>.

           error::reporting(7stap),
           https://sourceware.org/systemtap/wiki/HowToReportBugs 

## [](#COLOPHON)COLOPHON

           This page is part of the systemtap (a tracing and live-system
           analysis tool) project.  Information about the project can be
           found at ⟨https://sourceware.org/systemtap/⟩.  If you have a bug
           report for this manual page, send it to systemtap@sourceware.org.
           This page was obtained from the project's upstream Git repository
           ⟨git://sourceware.org/git/systemtap.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                                             STAP-EXPORTER(8)

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
