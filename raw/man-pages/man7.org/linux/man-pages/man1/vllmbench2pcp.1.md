---
{"title": "vllmbench2pcp(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/vllmbench2pcp.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# vllmbench2pcp(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    VLLM2PCP(1)              General Commands Manual              VLLM2PCP(1)

## [](#NAME)NAME

           vllmbench2pcp - vLLM benchmark results importer

## [](#SYNOPSIS)SYNOPSIS

           vllmbench2pcp [-hv] [-a archive] [-H hostname] results [...]

## [](#DESCRIPTION)DESCRIPTION

           vllmbench2pcp is a performance metrics importer tool that creates
           a PCP archive from the JSON results of a vLLM benchmark.

           An archive spanning the time for which the benchmark and its run
           iterations were active.  Discrete PCP metrics are created for each
           recorded aspect of a run, and logged once at the start and once at
           the end of each iteration, followed by a mark record.

           This allows PCP tools to report on these metrics in a meaningful
           way alongside other system (kernel, hardware, vLLM, and so on)
           metrics gathered during the benchmark.

           The only mandatory command line argument is the JSON results file
           from a vllm bench invocation.  This JSON can optionally be wrapped
           with additional Model Furnace metadata, and if this is detected
           additional PCP labels will be extracted and stored (such as model
           and inference server names).

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -a archive, --archive=archive
                Specified the name of the output PCP archive to be produced.
                By default, an archive name using the timestamp of the start
                of the benchmark run will be used.

           -H hostname, --hostname=hostname
                Sets the hostname that will be stamped into the PCP archive
                label header.

           -h, --help
                Display usage message and exit.

           -v, --verbose
                Report progress as each run is identified and its values
                saved.

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pminfo(1), pmrep(1), LOGARCHIVE(5), and PMNS(5).

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

    Performance Co-Pilot               PCP                        VLLM2PCP(1)

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
