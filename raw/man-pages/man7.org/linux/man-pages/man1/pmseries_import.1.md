---
{"title": "pmseries_import(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmseries_import.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmseries_import(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMSERIES_IMPORT(1)       General Commands Manual       PMSERIES_IMPORT(1)

## [](#NAME)NAME

           pmseries_import - import PCP archive files for historical time
           series querying

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmseries_import [-h] [--archives path] [--json
           file] [--import-timeout time] [--noop] [--poll-interval delta] [-p
           port] [-Z TZ]

## [](#DESCRIPTION)DESCRIPTION

           pmseries_import monitors a given path for PCP archives, and
           automatically loads the contents into a key server (such as Valkey
           or Redis).  This is then suitable for fast time series querying
           using the pmseries(1) language, as provided by the command line
           tool and PCP REST API services of pmproxy(1).

           pmseries_import uses a simple polling technique, checking the
           archives directory for new archive files every 10 seconds.

           This utility is most commonly used within a container providing an
           automated Grafana dashboard setup for arbitrary PCP archives.
           This approach provides an environment containing a systemd(1)
           server to enable this archive monitoring utility, pre-configured
           grafana-server(1), valkey-server(1), and pmproxy(1) REST API
           services.

## [](#OPTIONS)OPTIONS

           --archives=path
                Specifies an alternate path to poll for new PCP archives.
                Default value is /archives.

           --jsonfile=file
                Specifies an alternate JSON format file to update whenever
                the time window boundaries are seen to have changed.  This
                file must contain JSON content, including a JSON map named
                "time" with "start" and "end" fields where string timestamps
                will be written.  The default value is
                /usr/local/var/lib/grafana/dashboards/pcp-archive-
                analysis.json.

           -h, --help
                Display command usage message and exit.

           --import-timeout=timeout
                Specify a number of seconds to allow for any individual
                archive import to complete, via the pmseries load command for
                that archive.  The default timeout value is 600 seconds (5
                minutes).

           --noop
                Skips all write operations (for debugging or testing
                purposes), reporting only diagnostic messages instead.

           --poll-interval=delta
                The frequency with which the archive directory will be
                scanned.  Default delta is once every 10 seconds.

           -p port, --port=port
                An optional port on which pmseries should connect to the key
                server.  The default port is 6379.

           -Z TZ, --timezone=TZ
                An optional TZ value indicating the timezone to which
                pmseries should convert all archive timestamps when sending
                values to the key server.

## [](#SEE_ALSO)SEE ALSO

           grafana-server(1), systemd(1), valkey-server(1), pmproxy(1) and
           pmseries(1).

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

    Performance Co-Pilot               PCP                 PMSERIES_IMPORT(1)

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
