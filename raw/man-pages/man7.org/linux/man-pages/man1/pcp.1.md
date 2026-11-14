---
{"title": "pcp(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMAND MODE](#COMMAND_MODE) \| [SUMMARY MODE](#SUMMARY_MODE) \| [SUMMARY MODE OPTIONS](#SUMMARY_MODE_OPTIONS) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP(1)                   General Commands Manual                   PCP(1)

## [](#NAME)NAME

           pcp, pcp-summary - run a command or summarize an installation

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options...]  pcp-command [command options...]
           pcp [-LPV?]  [-a archive] [-D debug] [-h host] [-O origin] [-n
           pmnsfile]

## [](#DESCRIPTION)DESCRIPTION

           The pcp command is used in one of two modes.  By default, it
           summarizes the Performance Co-Pilot (PCP) installation on the
           local host.  This mode can also be used to summarize the
           installation from a remote host, or a historical installation from
           a set of PCP archives.  This mode indirectly invokes the pcp-
           summary command (in the absence of any other requested command).

           Alternatively, a command can be passed to pcp to run, again
           possibly in the context of a remote host or set of historical
           archives.

## [](#COMMAND_MODE)COMMAND MODE

           When pcp is invoked with a command to run, it will search for the
           named command in $PCP_BINADM_DIR and also $HOME/.pcp/bin (these
           are usually scripts, and are installed with a "pcp-" prefix).
           This mode of operation allows system performance tools to be
           implemented using PMAPI(3) services, while still preserving all of
           their usual command line options.  These options are thus
           (indirectly) augmented with the standard PCP option set, as
           described in PCPIntro(1).

           This provides a convenient mechanism for obtaining retrospective
           or remote monitoring capabilities while preserving the behaviour
           of the system tools.

           For example, the pcp-free(1) utility can be invoked as follows,
           for recorded data from host munch:

           $ pcp -a $PCP_LOG_DIR/pmlogger/munch/20140317 -O 11:35:50am free -m
                        total       used       free     shared    buffers     cached
           Mem:         23960      14554       9406          0        176       2137
           -/+ buffers/cache:      12240      11720
           Swap         12047          0      12047

           A complete list of the available and installed tools is provided
           along with the pcp(1) usage message, but some examples include:
           pcp-free(1), pcp-uptime(1) and pcp-numastat(1).

## [](#SUMMARY_MODE)SUMMARY MODE

           The summary report includes: the OS version, a summary of the
           hardware inventory, the local timezone, the PCP software version,
           the state of the pmcd(1) process and associated Performance
           Metrics Domain Agents (PMDAs), as well as information about any
           local PCP archivers (pmlogger(1)), remote PCP archivers
           (pmproxy(1)), and PCP inference engines (pmie(1)) that are
           running.

           All of the displayed values are performance metric values and
           further information for each can be obtained using the command:

              $ pminfo -dtT metric

           The complete set of metrics required by pcp to produce its output
           is contained in $PCP_VAR_DIR/config/pmlogconf/tools/pcp-summary.

## [](#SUMMARY_MODE_OPTIONS)SUMMARY MODE OPTIONS

           With no arguments, pcp reports on the local host, however the
           following options are accepted:

           -a archive, --archive=archive
                Report the PCP configuration as described in the set of PCP
                archives, archive, which is a comma-separated list of names,
                each of which may be the base name of an archive or the name
                of a directory containing one or more archives.

           -h host, --host=host
                Report the PCP configuration on host rather than the local
                host.

           -L, --local-PMDA
                Use a local context to collect metrics from DSO PMDAs on the
                local host without PMCD.

           -n pmnsfile, --namespace=pmnsfile
                Load an alternative Performance Metrics Name Space (PMNS(5))
                from the file pmnsfile.

           -O origin, --origin=origin
                When reporting archived metrics, start reporting at origin
                within the time window.

           -P, --pmie
                Display pmie(1) performance information - counts of rules
                evaluating to true, false, or indeterminate, as well as the
                expected rate of rule calculation, for each pmie process
                running on the default host.  Refer to the individual metric
                help text for full details on these values.

           -V, --version
                Display version number and exit.

           -?, --help
                Display usage message and exit.

## [](#DIAGNOSTICS)DIAGNOSTICS

           pcp will terminate with an exit status of 1 if pmcd on the target
           host could not be reached or the set of archives could not be
           opened, or 2 for any other error.

## [](#FILES)FILES

           $HOME/.pcp/bin
                Per-user location for command scripts.

           $PCP_BINADM_DIR
                System location for installed command scripts.

           $PCP_VAR_DIR/config/pmlogconf/tools/pcp-summary
                pmlogconf(1) configuration file for collecting all of the
                metrics required by pcp

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

           PCPIntro(1), pcp-free(1), pcp-numastat(1), pcp-python(1),
           pcp-uptime(1), pcp-verify(1), pmcd(1), pmie(1), pmlogconf(1),
           pmlogger(1), pmproxy(1), pcp.conf(5), pcp.env(5) and PMNS(5).

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

    Performance Co-Pilot               PCP                             PCP(1)

------------------------------------------------------------------------

Pages that refer to this page: [osvis(1)](../man1/osvis.1.html),  [pcp(1)](../man1/pcp.1.html),  [pcp2arrow(1)](../man1/pcp2arrow.1.html),  [pcp2elasticsearch(1)](../man1/pcp2elasticsearch.1.html),  [pcp2graphite(1)](../man1/pcp2graphite.1.html),  [pcp2influxdb(1)](../man1/pcp2influxdb.1.html),  [pcp2json(1)](../man1/pcp2json.1.html),  [pcp2openmetrics(1)](../man1/pcp2openmetrics.1.html),  [pcp2opentelemetry(1)](../man1/pcp2opentelemetry.1.html),  [pcp2spark(1)](../man1/pcp2spark.1.html),  [pcp2template(1)](../man1/pcp2template.1.html),  [pcp2xlsx(1)](../man1/pcp2xlsx.1.html),  [pcp2xml(1)](../man1/pcp2xml.1.html),  [pcp2zabbix(1)](../man1/pcp2zabbix.1.html),  [pcp-atop(1)](../man1/pcp-atop.1.html),  [pcp-atopsar(1)](../man1/pcp-atopsar.1.html),  [pcp-buddyinfo(1)](../man1/pcp-buddyinfo.1.html),  [pcpcompat(1)](../man1/pcpcompat.1.html),  [pcp-dmcache(1)](../man1/pcp-dmcache.1.html),  [pcp-dstat(1)](../man1/pcp-dstat.1.html),  [pcp-free(1)](../man1/pcp-free.1.html),  [pcpintro(1)](../man1/pcpintro.1.html),  [pcp-iostat(1)](../man1/pcp-iostat.1.html),  [pcp-ipcs(1)](../man1/pcp-ipcs.1.html),  [pcp-meminfo(1)](../man1/pcp-meminfo.1.html),  [pcp-mpstat(1)](../man1/pcp-mpstat.1.html),  [pcp-netstat(1)](../man1/pcp-netstat.1.html),  [pcp-nfsiostat(1)](../man1/pcp-nfsiostat.1.html),  [pcp-numastat(1)](../man1/pcp-numastat.1.html),  [pcp-pidstat(1)](../man1/pcp-pidstat.1.html),  [pcp-ps(1)](../man1/pcp-ps.1.html),  [pcp-python(1)](../man1/pcp-python.1.html),  [pcp-rocestat(1)](../man1/pcp-rocestat.1.html),  [pcp-shping(1)](../man1/pcp-shping.1.html),  [pcp-slabinfo(1)](../man1/pcp-slabinfo.1.html),  [pcp-ss(1)](../man1/pcp-ss.1.html),  [pcp-tapestat(1)](../man1/pcp-tapestat.1.html),  [pcp-uptime(1)](../man1/pcp-uptime.1.html),  [pcp-verify(1)](../man1/pcp-verify.1.html),  [pcp-xsos(1)](../man1/pcp-xsos.1.html),  [pcp-zoneinfo(1)](../man1/pcp-zoneinfo.1.html),  [pmgetopt(1)](../man1/pmgetopt.1.html),  [pmpython(1)](../man1/pmpython.1.html),  [pmrep(1)](../man1/pmrep.1.html),  [pmstat(1)](../man1/pmstat.1.html),  [pmview(1)](../man1/pmview.1.html),  [pmisetimportprogram(3)](../man3/pmisetimportprogram.3.html),  [pcp-atoprc(5)](../man5/pcp-atoprc.5.html)

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
