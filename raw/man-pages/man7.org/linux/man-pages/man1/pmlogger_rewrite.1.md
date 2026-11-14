---
{"title": "pmlogger_rewrite(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmlogger_rewrite.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmlogger_rewrite(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOGGER_REWRITE(1)      General Commands Manual      PMLOGGER_REWRITE(1)

## [](#NAME)NAME

           pmlogger_rewrite - helper script to rewrite Performance Co-Pilot
           archives

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmlogger_rewrite [-dNsVvw?]  [-c config] archive
           ...

## [](#DESCRIPTION)DESCRIPTION

           pmlogger_rewrite is a helper script that is used by
           pmlogger_daily(1) when rewriting Performance Co-Pilot (PCP)
           archives.  Rewriting is usually required to accommodate
           evolutionary changes in metadata so old archives can be updated
           and then merged with current archives.

           pmlogger_rewrite is a wrapper script for pmlogrewrite(1) that will
           potentially rewrite all of the archives matching the archive
           arguments.  Each archive argument may be a PCP archive file name,
           the basename for the files in a PCP archive, or a directory (in
           which case all subordinate PCP archives are found by recursive
           descent).

           pmlogrewrite is run with the -i option so rewriting is done ``in
           place''.  The -q option is also used, so if no rewriting is
           required then no changes are made to the archive files.

## [](#OPTIONS)OPTIONS

           The following options are passed through to pmlogrewrite: -c (or
           --config), -d (or --desperate), -s (or --scale), -v (or --verbose)
           and -w (or --warnings).  Refer to pmlogrewrite(1) for the meaning
           of these options.

           The remaining options are:

           -N, --showme
                Runs pmlogger_rewrite in a ``show me'' or ``dry run'' mode
                where the tasks that would be performed are reported, but no
                changes are made.  This is typically used for debugging in
                combination with one (verbose) or two (very verbose) -V op‐
                tions.

           -V, --verbose
                Increase script output verbosity.

           -?, --help
                Display usage message and exit.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to parameter‐
           ize the file and directory names used by PCP.  On each installa‐
           tion, the file /etc/pcp.conf contains the local values for these
           variables.  The $PCP_CONF variable may be used to specify an al‐
           ternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmlogger(1), pmlogger_daily(1) and pmlogrewrite(1).

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

    Performance Co-Pilot               PCP                PMLOGGER_REWRITE(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmlogcompress(1)](../man1/pmlogcompress.1.html)

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
