---
{"title": "pcp-uptime(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-uptime.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-uptime(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-UPTIME(1)            General Commands Manual            PCP-UPTIME(1)

## [](#NAME)NAME

           pcp-uptime - tell how long the system has been running

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options] uptime [-V?]

## [](#DESCRIPTION)DESCRIPTION

           pcp-uptime gives a one line display of the following information.
           The current time, how long the system has been running, how many
           users are currently logged on, and the system load averages for
           the past 1, 5, and 15 minutes.

           When invoked via the pcp(1) command, the -h/--host, -a/--archive,
           -O/--origin, -Z/--timezone and several other pcp options become
           indirectly available.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -V, --version
                Display version number and exit.

           -?, --help
                Display usage message and exit.

           When replaying from an archive using the -a option, the required
           information may not be available at the default starting time, in
           which case the reported values will be ``?''.  In this case, use
           the -S or -O options to move the starting time into a point in the
           archive where the required information is available.

## [](#NOTES)NOTES

           pcp-uptime is inspired by the uptime(1) command and aims to be
           command line and output compatible with it.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pcp(1), uptime(1) and environ(7).

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

    Performance Co-Pilot               PCP                      PCP-UPTIME(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcp(1)](../man1/pcp.1.html)

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
