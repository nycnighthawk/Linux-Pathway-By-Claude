---
{"title": "pmsocks(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmsocks.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmsocks(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMSOCKS(1)               General Commands Manual               PMSOCKS(1)

## [](#NAME)NAME

           pmsocks - shell wrapper for performance monitoring across
           firewalls

## [](#SYNOPSIS)SYNOPSIS

           pmsocks path [args ...]

## [](#DESCRIPTION)DESCRIPTION

           pmsocks allows Performance Co-Pilot (PCP) clients running on hosts
           located on the internal side of a TCP/IP firewall to monitor
           remote hosts on the other side of the firewall.  This assumes the
           firewall has been configured with a compliant sockd daemon and the
           necessary access controls are satisfied.

           pmsocks is a thin shell wrapper around the tsocks(8) library using
           the tsocks(1) utility, which are not included with PCP.  You can
           obtain tsocks from https://tsocks.sourceforge.net/ .

## [](#FILES)FILES

           /etc/tsocks.conf
                configuration file for the tsocks(8) library.

## [](#SEE_ALSO)SEE ALSO

           pmcd(1), pmproxy(1), PMAPI(3) and tsocks(8).

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

    Performance Co-Pilot               PCP                         PMSOCKS(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmie_check(1)](../man1/pmie_check.1.html),  [pmlogger.control(5)](../man5/pmlogger.control.5.html)

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
