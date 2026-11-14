---
{"title": "pmlogger_merge(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmlogger_merge.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmlogger_merge(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOGGER_MERGE(1)        General Commands Manual        PMLOGGER_MERGE(1)

## [](#NAME)NAME

           pmlogger_merge - helper script to merge Performance Co-Pilot
           archives

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmlogger_merge [-fNVE?]  [input-basename ...
           output-name]

## [](#DESCRIPTION)DESCRIPTION

           pmlogger_merge is a helper script that is used by
           pmlogger_daily(1) when merging all of the Performance Co-Pilot
           (PCP) archives for a single host on a single day into a combined
           PCP archive.

           pmlogger_merge is a wrapper script for pmlogextract(1) that merges
           all of the archives matching the input-basename arguments and
           creates a new archive using output-name as the base name for the
           physical files that constitute an archive.  The input-basename
           arguments may contain meta characters in the style of sh(1).

           If any of the files that are components of the input-basename
           archives has been compressed then on success pmlogger_merge will
           compress output-name using pmlogcompress(1).

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -f, --force
                This option causes all of the input files to be removed once
                the output archive has been created.

           -N, --showme
                Runs pmlogger_merge in a ``show me'' or ``dry run'' mode
                where the tasks that would be performed are reported, but no
                changes are made.  This is typically used for debugging in
                combination with one (verbose) or two (very verbose) -V
                options.

           -V, --verbose
                Increase verbosity in the output progress report.

           -E, --expunge
                When metric metadata differences are encountered between
                archives to be merged, the default behaviour is for
                pmlogger_merge to fail with a fatal error and the output-name
                archive is not created.  The -E flag instead issues a warning
                and excludes the affected metrics from the merged output
                archive.  This is intended for automated daily archive
                rotation where it is highly desirable for unattended daily
                archive merging, rewriting and compression to succeed.  See
                also pmlogger_daily(1) and the -x flag to pmlogextract(1).

           -?, --help
                Display usage message and exit.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmlogcompress(1), pmlogextract(1), pmlogger(1) and
           pmlogger_daily(1).

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

    Performance Co-Pilot               PCP                  PMLOGGER_MERGE(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmlogger_daily(1)](../man1/pmlogger_daily.1.html)

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
