---
{"title": "autofsd-probe(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/autofsd-probe.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# autofsd-probe(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                               |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    AUTOFSD-PROBE(1)         General Commands Manual         AUTOFSD-PROBE(1)

## [](#NAME)NAME

           autofsd-probe - probe AutoFS mount/unmount daemon

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/autofsd-probe [-h host] [-t timeout]

## [](#DESCRIPTION)DESCRIPTION

           autofsd-probe will check the status of the autofsd(1) daemon on
           the specified host.

           Unless directed to another host by the -h option, autofsd-probe
           will contact the AutoFS daemon on the local host.

           The AutoFS file system is built on the Remote Procedure Call
           (RPC(3)) library routines.  The -t option allows the total timeout
           and retry timeout intervals to be set for all remote procedure
           call operations used with autofsd-probe.  This option accepts an
           interval argument in the form described in the PCPIntro(1) manual
           page.

           autofsd-probe is typically used in an automated fashion from
           within pmdashping(1) and in conjunction with pmie(1), for
           monitoring response time and service failure.

           By default autofsd-probe will not produce any output, unless there
           is an error in which case a diagnostic message will be displayed
           and the exit status will indicate the reason for failure.

## [](#DIAGNOSTICS)DIAGNOSTICS

           If autofsd-probe succeeds, then 0 will be returned.  If the
           attempt to establish a connection with autofsd fails, then 2 is
           returned.  If the subsequent attempt to invoke an autofsd response
           fails, then 1 will be returned.

           In the case of a syntactical command line error, 4 is returned and
           the usage message is displayed.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           autofs(1), autofsd(1), PCPIntro(1), pmdashping(1), pmie(1) and
           RPC(3).

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

    Performance Co-Pilot               PCP                   AUTOFSD-PROBE(1)

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
