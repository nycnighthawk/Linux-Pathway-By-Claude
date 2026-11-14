---
{"title": "pcp-reboot-init(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-reboot-init.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-reboot-init(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-REBOOT-INIT(1)       General Commands Manual       PCP-REBOOT-INIT(1)

## [](#NAME)NAME

           pcp-reboot-init - Performance Co-Pilot helper script after system
           reboot

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/reboot-init

## [](#DESCRIPTION)DESCRIPTION

           The pcp-reboot-init service performs ``one-trip'' initialization
           after system reboot for the various components of the Performance
           Co-Pilot (PCP).

           The script is normally called from init(1) or systemd(1) scripts
           prior to starting other PCP components.  It should not need to be
           run at other times, but is idempotent so repeated execution is
           harmless, but useless.

           The reboot-init script is intended to be run as the ``root'' user,
           and will fail otherwise.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           The file /etc/pcp.conf contains the local values for PCP_
           variables used in this script.

## [](#SEE_ALSO)SEE ALSO

           init(1), PCPIntro(1), systemd(1), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                 PCP-REBOOT-INIT(1)

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
