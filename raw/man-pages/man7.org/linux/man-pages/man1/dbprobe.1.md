---
{"title": "dbprobe(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dbprobe.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dbprobe(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DBPROBE(1)               General Commands Manual               DBPROBE(1)

## [](#NAME)NAME

           dbprobe - database response time and availability information

## [](#SYNOPSIS)SYNOPSIS

           dbprobe.pl [delay]

## [](#DESCRIPTION)DESCRIPTION

           The dbprobe utility is used by pmdadbping(1) to measure response
           time from a database.  A given query is executed on the database
           at the requested interval (delay, which defaults to 60 seconds).
           This response time measure can be exported via the Performance Co-
           Pilot framework for live and historical monitoring using
           pmdadbping(1).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmdadbping(1) and DBI(3).

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

    Performance Co-Pilot               PCP                         DBPROBE(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmdadbping(1)](../man1/pmdadbping.1.html)

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
