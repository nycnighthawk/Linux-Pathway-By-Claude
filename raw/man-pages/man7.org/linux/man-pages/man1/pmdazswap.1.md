---
{"title": "pmdazswap(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdazswap.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdazswap(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                           |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDAZSWAP(1)             General Commands Manual             PMDAZSWAP(1)

## [](#NAME)NAME

           pmdazswap - zswap (compressed swap) PMDA

## [](#DESCRIPTION)DESCRIPTION

           pmdazswap is a Performance Metrics Domain Agent (PMDA) which
           exports metric values about compressed swap operation, as tracked
           by the zswap Linux kernel module.

           Zswap is a lightweight compressed cache for swap pages.  It takes
           pages that are in the process of being swapped out and attempts to
           compress them into a dynamically allocated RAM-based memory pool.
           Zswap trades CPU cycles for potentially reduced swap I/O.  This
           tradeoff can also result in a performance improvement if reads
           from the compressed cache are faster than reads from a swap
           device.

           This PMDA exports metrics about pool size, number of pages stored,
           and various counters for the reasons pages are rejected.

## [](#INSTALLATION)INSTALLATION

           Install the zswap PMDA by using the Install script as root:

               # cd $PCP_PMDAS_DIR/zswap
               # ./Install

           To uninstall, do the following as root:

               # cd $PCP_PMDAS_DIR/zswap
               # ./Remove

           pmdazswap is launched by pmcd(1) and should never be executed
           directly. The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILES)FILES

           $PCP_PMDAS_DIR/zswap/Install
               installation script for the pmdazswap agent

           $PCP_PMDAS_DIR/zswap/Remove
               undo installation script for the pmdazswap agent

           $PCP_LOG_DIR/pmcd/zswap.log
               default log file for error messages from pmdazswap

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP. On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1) and pmcd(1).

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

    Performance Co-Pilot               PCP                       PMDAZSWAP(1)

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
