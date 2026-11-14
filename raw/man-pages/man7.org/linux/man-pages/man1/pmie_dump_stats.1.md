---
{"title": "pmie_dump_stats(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmie_dump_stats.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmie_dump_stats(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMIE_DUMP_STATS(1)       General Commands Manual       PMIE_DUMP_STATS(1)

## [](#NAME)NAME

           pmie_dump_stats - dump the contents of pmie stats files

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmie_dump_stats file [...]

## [](#DESCRIPTION)DESCRIPTION

           Each pmie(1) process maintains a file of state and statistics in
           binary files in the $PCP_TMP_DIR/pmie directory, named with the
           process' PID.

           These files are used by the pmcd PMDA to instantiate the pmcd.pmie
           performance metrics.

           pmie_dump_stats is a stand alone utility that dumps the contents
           of these files in a terse, but script-friendly format.  It is
           designed for use in the pmiectl(1) script.

## [](#SEE_ALSO)SEE ALSO

           pmie(1) and pmiectl(1).

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

    Performance Co-Pilot               PCP                 PMIE_DUMP_STATS(1)

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
