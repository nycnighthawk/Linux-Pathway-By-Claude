---
{"title": "pcp-dmcache(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-dmcache.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-dmcache(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-DMCACHE(1)           General Commands Manual           PCP-DMCACHE(1)

## [](#NAME)NAME

           pcp-dmcache, pcp-lvmcache - report on logical storage device
           caches

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options] dmcache [-iRV?] [device ...]

## [](#DESCRIPTION)DESCRIPTION

           pcp-dmcache reports on the activity of any configured Device
           Mapper Cache targets.  The reported information includes device
           IOPs, cache and metadata device utilization, as well as hit and
           miss rates and ratios for both reads and writes for each cache
           device.

           pcp-lvmcache (Logical Volume Manager cache) is an exact synonym
           for pcp-dmcache (Device Mapper cache).

           By default, pcp-dmcache reports on all available cache target
           devices (one line each, per sample), but this can be restricted to
           specific devices on the command line.

## [](#OPTIONS)OPTIONS

           When invoked via the pcp(1) command, the -h/--host, -a/--archive,
           -O/--origin, -s/--samples, -t/--interval, -Z/--timezone and
           several other pcp options become indirectly available; refer to
           PCPIntro(1) for a complete description of these options.

           The additional command line options available for pcp-dmcache are:

           -i, --iops
                  displays total read and write operations instead of the
                  default cache hit ratio.

           -R, --repeat
                  changes the frequency at which the column heading is
                  displayed.  By default, a header is displayed after every
                  tenth sample.

           -V, --version
                  Display version number and exit.

           -?, --help
                  Display usage message and exit.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pcp(1), pmdadm(1), dmsetup(1) and lvmcache(7).

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

    Performance Co-Pilot               PCP                     PCP-DMCACHE(1)

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
