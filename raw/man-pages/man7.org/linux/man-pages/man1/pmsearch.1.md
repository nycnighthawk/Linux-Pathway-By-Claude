---
{"title": "pmsearch(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmsearch.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmsearch(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMSEARCH(1)              General Commands Manual              PMSEARCH(1)

## [](#NAME)NAME

           pmsearch - help text and names search for metrics, instances and
           instance domains

## [](#SYNOPSIS)SYNOPSIS

           pmsearch [-CdinqsStTV?]  [-c config] [-D debug] [-h host] [-p
           port] [-N number] [-O offset] [query | indom]

## [](#DESCRIPTION)DESCRIPTION

           pmsearch performs full text search queries to find metrics using
           names and help text from metrics, instance domains and instances.

           It makes use of capabilities of the Performance Co-Pilot (PCP)
           pmproxy(1) service, the Valkey distributed key-value store and
           associated ValkeySearch module.

           Note that in order to use these services, it is mandatory that
           pmproxy is communicating with a Valkey key-value server that has
           the valkey-search.so module loaded.  When configured to do so,
           pmproxy will then automatically index PCP metric names, instance
           names, metric and instance domain help text into the ValkeySearch
           store, from PCP archives that it discovers locally.  Refer to
           pmlogger(1) and pmlogger_daily(1) for further details.

           By default pmsearch communicates with a local key-value server
           however the -h and -p options can be used to specify an alternate
           Valket instance.  If this instance is a node of a Valkey cluster,
           all other instances in the cluster will be discovered and used
           automatically.

## [](#OPTIONS)OPTIONS

           -c config, --config=config
                Specify the config file to use.

           -C, --no-colour
                No highlighting in results text.

           -d, --docid
                Report document ID of each search result.  Documents are
                identified using a unique SHA-1 hash which is always
                displayed in a 40-hexdigit human readable form.

           -h host, --host=host
                Connect to the key-value server at host, rather than the one
                the localhost.

           -i, --info
                Report search engine internal metrics.

           -n, --indom
                Perform an instance domain related entities search

           -N N, --number=N
                Return N, search results at most.

           -O N, --offset=N
                Paginated results from given offset.

           -p port, --port=port
                Connect to the key-value server at port, rather than the
                default 6379.

           -q, --query
                Perform a general text search (default).

           -s, --suggest
                Perform a name suggestion search

           -S, --score
                Report score (rank) of each result.

           -T, --total
                Report total number of of search results.

           -t, --times
                Report elapsed search execution time.

           -V, --version
                Display version number and exit.

           -?, --help
                Display usage message and exit.

## [](#EXAMPLES)EXAMPLES

             $ pmsearch kernel idle
             Type: metric
             Name: kernel.all.cpu.idle
             One line: total idle CPU time from /proc/stat for all CPUs

             Type: metric
             Name: kernel.all.idletime
             One line: time the current kernel has been idle since boot

             Type: metric
             Name: kernel.percpu.cpu.idle
             InDom: 60.0
             One line: percpu idle CPU time metric from /proc/stat

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

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmproxy(1), pmlogger(1) and pmlogger_daily(1).

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

    Performance Co-Pilot               PCP                        PMSEARCH(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmsearchinfo(3)](../man3/pmsearchinfo.3.html),  [pmsearchsetup(3)](../man3/pmsearchsetup.3.html),  [pmsearchtextindom(3)](../man3/pmsearchtextindom.3.html),  [pmsearchtextquery(3)](../man3/pmsearchtextquery.3.html),  [pmsearchtextsuggest(3)](../man3/pmsearchtextsuggest.3.html),  [pmwebapi(3)](../man3/pmwebapi.3.html)

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
