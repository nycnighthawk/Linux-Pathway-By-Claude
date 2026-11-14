---
{"title": "mkaf(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/mkaf.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mkaf(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                      |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MKAF(1)                  General Commands Manual                  MKAF(1)

## [](#NAME)NAME

           mkaf - create a Performance Co-Pilot archive folio

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/mkaf [-?]  [findopts] filename ...

## [](#DESCRIPTION)DESCRIPTION

           A collection of one or more Performance Co-Pilot (see PCPIntro(1))
           archives may be combined with mkaf to produce a PCP archive folio
           and the associated archive folio control file.  Some PCP tools use
           mkaf to create archive folios, e.g. the ``record'' facility in the
           pmchart(1) and pmview(1) tools, to facilitate playback with
           pmafm(1).

           mkaf processes each filename argument, and if this is a component
           file from a PCP archive that archive is added to the folio.

           If filename is a directory, then this is searched recursively
           using find(1).  Any filename argument beginning with a ``-'' is
           assumed to be a find(1) command line option (findopts); the
           default is -follow if no findopts are specified.

           The first named archive in the folio is assumed to be associated
           with the default host for any tool that tries to replay multiple
           archives from the folio.

           The folio control file is written to standard output, and has the
           following format.

           1. The first line contains the word PCPFolio.

           2. The second line contains the tag Version: followed by the
              format version number (currently 1).

           3. For subsequent lines, blank lines and lines beginning with
              ``#'' are ignored.

           4. The line beginning with the tag Created: documents where and
              when the folio was created.

           5. The line beginning with the tag Creator: identifies the tool
              which created the folio (and is assumed to know how to replay
              the archive folio).  If present, the second argument is the
              name of a configuration file that the creator tool could use to
              replay the archive folio, e.g. with the replay command for
              pmafm(1).  In the case of mkaf (unlike pmchart(1) or pmview(1))
              there is no knowledge of the contents of the archives, so the
              ``creator'' cannot replay the archive, however pmchart(1) is
              able to replay any archive, and so this tool is identified as
              the Creator: for archive folios created by mkaf(1).

           6. This is then followed by one or more lines beginning with the
              tag Archive: followed by the hostname and base name of the
              archive.

           For example
                $ mkaf mydir/gonzo
           might produce the following folio control file.

           PCPFolio
           Version: 1
           # use pmafm(1) to process this PCP archive folio
           #
           Created: on gonzo at Tue Jul  2 03:35:54 EST 1996
           Creator: pmchart
           #               Host                    Basename
           #
           Archive:        gonzo                   mydir/gonzo/960627
           Archive:        gonzo                   mydir/gonzo/960628
           Archive:        gonzo                   mydir/gonzo/960629
           Archive:        gonzo                   mydir/gonzo/960630
           Archive:        gonzo                   mydir/gonzo/960701
           Archive:        gonzo                   mydir/gonzo/960701.00.10
           Archive:        gonzo                   mydir/gonzo/960701.05.25
           Archive:        gonzo                   mydir/gonzo/960702.00.10

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -?   Display usage message and exit.

           -findopts
                Options to be passed to find(1).  The default is -follow.

## [](#DIAGNOSTICS)DIAGNOSTICS

           Some informational messages, warnings and pathological conditions
           are reported on standard error.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           find(1), PCPIntro(1), pmafm(1), pmchart(1), pmview(1), pcp.conf(5)
           and pcp.env(5).

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

    Performance Co-Pilot               PCP                            MKAF(1)

------------------------------------------------------------------------

Pages that refer to this page: [mkaf(1)](../man1/mkaf.1.html),  [pcp2arrow(1)](../man1/pcp2arrow.1.html),  [pcp2elasticsearch(1)](../man1/pcp2elasticsearch.1.html),  [pcp2graphite(1)](../man1/pcp2graphite.1.html),  [pcp2influxdb(1)](../man1/pcp2influxdb.1.html),  [pcp2json(1)](../man1/pcp2json.1.html),  [pcp2openmetrics(1)](../man1/pcp2openmetrics.1.html),  [pcp2opentelemetry(1)](../man1/pcp2opentelemetry.1.html),  [pcp2spark(1)](../man1/pcp2spark.1.html),  [pcp2template(1)](../man1/pcp2template.1.html),  [pcp2xlsx(1)](../man1/pcp2xlsx.1.html),  [pcp2xml(1)](../man1/pcp2xml.1.html),  [pcp2zabbix(1)](../man1/pcp2zabbix.1.html),  [pcp-atop(1)](../man1/pcp-atop.1.html),  [pcp-atopsar(1)](../man1/pcp-atopsar.1.html),  [pmafm(1)](../man1/pmafm.1.html),  [pmlogger_check(1)](../man1/pmlogger_check.1.html),  [pmlogger_daily(1)](../man1/pmlogger_daily.1.html),  [pmrep(1)](../man1/pmrep.1.html),  [pmgetoptions(3)](../man3/pmgetoptions.3.html),  [LOGARCHIVE(5)](../man5/LOGARCHIVE.5.html)

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
