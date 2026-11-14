---
{"title": "pmlogpaste(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmlogpaste.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmlogpaste(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOGPASTE(1)            General Commands Manual            PMLOGPASTE(1)

## [](#NAME)NAME

           pmlogpaste - paste text into a metric in a PCP archive

## [](#SYNOPSIS)SYNOPSIS

           pmlogpaste [-?]  [-f file] [-h hostname] [-l label] [-m metric]
           [-o outfile] [-t timezone]

## [](#DESCRIPTION)DESCRIPTION

           pmlogpaste takes input text from a file or the command line, and
           writes it as a metric value in a new PCP archive.  This metric
           value is timestamped with the current time, and is stored as a
           string type metric.

           The main purpose of this tool is to take captured output and
           preserve this in a PCP archive.  This allows, for example, the
           output of a benchmark run to be stored along with performance
           metrics captured during that run, in a single archive.  Archives
           can be merged using the pmlogextract(1) utility.

           pmlogpaste uses the LOGIMPORT(3) library interfaces internally,
           which support the creation of archives from external sources of
           performance data.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -f file, --file=file
                File with input text to be archived, or ``-'' for standard
                input.

           -h hostname, --hostname=hostname
                Source host name for the archive.  The default value is the
                local host name, or ``localhost'' if that cannot be obtained.

           -l label, --label=label
                Add context labels to the generated archive.  This option can
                be presented multiple times to produce multiple labels in the
                archive.  The label should be in the form name:value.

           -m metric, --metric=metric
                Metric name for the archive.  The default metric name is
                paste.value.

           -o outfile, --outfile=outfile
                Archive output file.  The default archive name is paste.

           -t timezone, --timezone=timezone
                Source timezone for the archive archive.  The default value
                is the local timezone.

           -?, --help
                Display usage message and exit.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmlogextract(1) and LOGIMPORT(3).

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

    Performance Co-Pilot               PCP                      PMLOGPASTE(1)

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
