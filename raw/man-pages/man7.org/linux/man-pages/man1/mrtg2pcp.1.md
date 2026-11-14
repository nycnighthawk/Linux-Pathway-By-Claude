---
{"title": "mrtg2pcp(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/mrtg2pcp.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mrtg2pcp(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MRTG2PCP(1)              General Commands Manual              MRTG2PCP(1)

## [](#NAME)NAME

           mrtg2pcp - import MRTG data and create a PCP archive

## [](#SYNOPSIS)SYNOPSIS

           mrtg2pcp hostname devname timezone infile outfile

## [](#DESCRIPTION)DESCRIPTION

           mrtg2pcp is intended to read an MRTG log file as created by
           mrtg(1) and translate this into a Performance Co-Pilot (PCP)
           archive with the basename outfile.  The hostname, devname, and
           timezone arguments specify information about the system for which
           the statistics were gathered.

           The resultant PCP archive may be used with all PCP client tools to
           graph subsets of the data using pmchart(1), perform data reduction
           and reporting, filter with the PCP inference engine pmie(1), etc.

           A series of physical files will be created with the prefix
           outfile.  These are outfile.0 (the performance data), outfile.meta
           (the metadata that describes the performance data) and
           outfile.index (a temporal index to improve efficiency of replay
           operations for the archive).  If any of these files exists
           already, then mrtg2pcp will not overwrite them and will exit with
           an error message of the form

           __pmLogNewFile: ``blah.0'' already exists, not over-written

           mrtg2pcp is a Perl script that uses the PCP::LogImport Perl
           wrapper around the PCP libpcp_import library, and as such could be
           used as an example to develop new tools to import other types of
           performance data and create PCP archives.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           mrtg(1), pmchart(1), pmie(1), pmlogger(1), LOGIMPORT(3) and
           PCP::LogImport(3).

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

    Performance Co-Pilot               PCP                        MRTG2PCP(1)

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
