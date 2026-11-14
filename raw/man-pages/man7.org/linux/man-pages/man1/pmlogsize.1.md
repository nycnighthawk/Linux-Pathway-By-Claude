---
{"title": "pmlogsize(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmlogsize.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmlogsize(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                  |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOGSIZE(1)             General Commands Manual             PMLOGSIZE(1)

## [](#NAME)NAME

           pmlogsize - report sizes for parts of PCP archive(s)

## [](#SYNOPSIS)SYNOPSIS

           pmlogsize [-drv?]  [-D debug] [-x threshold] archive [...]

## [](#DESCRIPTION)DESCRIPTION

           pmlogsize prints information about the size of the index, metadata
           and data sections of a Performance Co-Pilot (PCP) archive.  The
           output is intended to guide improvements in archive encoding
           format for PCP developers and to help trim pmlogger(1)
           configuration files to remove metrics that are bloating the PCP
           archives with low-value data in production environments.

           The archive arguments can be any mixture of the names of the
           physical files of a PCP archive or the basename that is common to
           all the component physical files in a single archive.  In the
           latter case archive is replaced by a list of all of the matching
           component file names.

           Note the semantics is a little different to other PCP tools in
           that foo.meta means just the file foo.meta, not foo.index,
           foo.meta, foo.0, etc.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -d, --detail
                Enable detailed reporting.  This means space per instance
                domain in a metadata file and space per metric (for values)
                in a data file.

           -r, --replication
                Display additional information about possible replicated
                values in the data file and replicated instances in the
                metadata file.  This option implies -d.

           -x threshold, --threshold=threshold
                With -d (or -r), cut off the report after at least threshold
                percent of the associated space (metric values or instance
                domains) has been reported.  The default behaviour is
                equivalent to threshold being set to 100.

           -v, --verbose
                Enable verbose mode.  This option can be provided more than
                once for additional verbosity.

           -?, --help
                Display usage message and exit.

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmlogcheck(1), pmlogdump(1) and pmlogger(1).

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

    Performance Co-Pilot               PCP                       PMLOGSIZE(1)

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
