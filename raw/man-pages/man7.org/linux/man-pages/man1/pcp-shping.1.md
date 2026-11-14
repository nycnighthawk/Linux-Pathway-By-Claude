---
{"title": "pcp-shping(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-shping.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-shping(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-SHPING(1)            General Commands Manual            PCP-SHPING(1)

## [](#NAME)NAME

           pcp-shping - report on shell service availability and response

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options] shping [-cl?]  tag ...

## [](#DESCRIPTION)DESCRIPTION

           pcp-shping samples and reports on the shell-ping service metrics
           exported by the pmdashping(1) agent.

           The default report from pcp-shping shows two columns for each
           service tag, the first showing service status (zero indicating
           success) and the second service response time, for the last
           pmdashping command refresh cycle.

           When invoked via the pcp(1) command, the -h/--host, -a/--archive,
           -O/--origin, -s/--samples, -t/--interval, -Z/--timezone and
           several other pcp options become indirectly available, see
           PCPIntro(1) for their descriptions.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -c, --status
                Display a summary of the current shell-ping collector,
                including information about service refresh interval, the
                current command timeout setting, count of refreshes, and the
                full command line associated with each tag.

           -l, --tags
                Displays the valid tags.

           -?, --help
                Display usage message and exit.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pcp(1) and pmdashping(1).

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

    Performance Co-Pilot               PCP                      PCP-SHPING(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmdashping(1)](../man1/pmdashping.1.html)

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
