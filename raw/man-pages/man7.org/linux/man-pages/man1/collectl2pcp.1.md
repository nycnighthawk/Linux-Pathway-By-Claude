---
{"title": "collectl2pcp(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/collectl2pcp.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# collectl2pcp(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                  |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    COLLECTL2PCP(1)          General Commands Manual          COLLECTL2PCP(1)

## [](#NAME)NAME

           collectl2pcp - import collectl data to a PCP archive

## [](#SYNOPSIS)SYNOPSIS

           collectl2pcp [-fv?]  [-D debug] file [file ...]  archive

## [](#DESCRIPTION)DESCRIPTION

           collectl2pcp reads raw collectl(1) data from each file and creates
           a new PCP archive with basename archive.  Each input file may be
           gzipped (with .gz suffix).  The PCP archive and at least one input
           file are required arguments.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -f, --force
                Overwrite archive (and the index and meta files) if it
                already exists.

           -v, --verbose
                Report progress and errors verbosely.  This also reports a
                count of unsupported metric data in the collectl(1) input
                file(s), which is normally silently skipped.

           -?, --help
                Display usage message and exit.

           file [file ...]
                These are the collectl(1) input files.  If more than one is
                given, they must contain data for the same host and be given
                in time-stamp chronological order on the command line.  Note
                that when collectl(1) is run as a service, it normally
                creates files with date based names that will sort
                chronologically (e.g. /var/log/collectl/*.gz will be sorted
                correctly).

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

           collectl(1), PCPIntro(1), LOGIMPORT(3), pcp.conf(5), pcp.env(5)
           and PMNS(5).

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

    Performance Co-Pilot               PCP                    COLLECTL2PCP(1)

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
