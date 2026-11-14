---
{"title": "pcpcompat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcpcompat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcpcompat(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [INTRODUCTION](#INTRODUCTION) \| [PYTHON2](#PYTHON2) \| [QT4](#QT4) \| [NSS](#NSS) \| [SAR2PCP, IOSTAT2PCP](#SAR2PCP,_IOSTAT2PCP) \| [PMLOGCONF-SETUP](#PMLOGCONF-SETUP) \| [PMMGR](#PMMGR) \| [PCP-COLLECTL](#PCP-COLLECTL) \| [PCP-WEBAPPS](#PCP-WEBAPPS) \| [PMWEBD](#PMWEBD) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                     |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCPCOMPAT(1)             General Commands Manual             PCPCOMPAT(1)

## [](#NAME)NAME

           PCPCompat, pcp-collectl, pmmgr, pmwebd - backward-compatibility in
           the Performance Co-Pilot (PCP)

## [](#INTRODUCTION)INTRODUCTION

           The Performance Co-Pilot (PCP) is a toolkit designed for
           monitoring and managing system-level performance.  These services
           are distributed and scalable to accommodate the most complex
           system configurations and performance problems.

           In order to achieve these goals effectively, protocol and on-disk
           compatibility is provided between different versions of PCP.  It
           is feasible (and indeed encouraged) to use current PCP tools to
           interrogate any remote, down-rev or up-rev pmcd(1) and also to
           replay any historical PCP archive (the PCP testsuite includes PCP
           archives created over 20 years ago!).

           From time to time the PCP developers deprecate and remove PCP
           utilities, replacing them with new versions of utilities providing
           comparable features.  This page describes replacement utilities
           for historical PCP tools.

## [](#PYTHON2)PYTHON2

           PCP provides python(1) interfaces for the PMAPI(3) (Performance
           Metrics API), the PMDA(3) API (Performance Metrics Domain Agents),
           the mmv_stats_register(3) API (Memory-Mapped Values) and PCP
           archive creation LOGIMPORT(3) API.

           With python version 2 reaching end-of-life in 2020 we have now
           removed all support for this version (from PCP version 7 and
           later).  All PCP APIs and python-based tools support python
           version 3 and have for several years - upgrading is strongly
           recommended.

## [](#QT4)QT4

           PCP provides optional graphical user interfaces built on the
           cross-platform Qt library, particularly pmchart(1) and pmtime(1).

           With Qt v4 reaching end-of-life in 2015 we have removed support
           for all versions before Qt v5.  In addition, some features are
           missing in early versions of Qt v5 that are now mandatory when
           building and using PCP Qt tools.  As a result the minimum required
           version of Qt for PCP v6 and beyond is now Qt 5.6.

## [](#NSS)NSS

           Versions of PCP before v6 used a combination of both Mozilla NSS
           (Network Security Services) and OpenSSL for the encryption
           component of the secure sockets functionality.  Starting with PCP
           v6 this has been simplified into exclusive use of OpenSSL for all
           use of encryption across PCP.  This change affects configuration
           of optional functionality in pmcd(1) and PMAPI(3) client tools
           using secure sockets.

           The net effect of this change is that encryption is configured in
           the same ways, using the same certificates, across the HTTPS
           functionality in pmproxy(1), as well as the encrypted PCP protocol
           functionality between pmcd, pmproxy and PMAPI client tools.
           Additionally, the key-value server service used by pmseries(1) and
           pmproxy also exclusively uses OpenSSL, and in a manner similar to
           PCP, which makes administering these services significantly
           simpler.

## [](#SAR2PCP,_IOSTAT2PCP)SAR2PCP, IOSTAT2PCP

           The sar2pcp(1) and iostat2pcp(1) utilities are deprecated, and
           will be retired in a future version of PCP (v7).  This is being
           replaced by native support for generating PCP archives within the
           tools of the sysstat package (which provides sar itself, as well
           as the sadf utility which produces PCP archives via the -l
           option).

## [](#PMLOGCONF-SETUP)PMLOGCONF-SETUP

           Earlier versions of PCP (prior to v5.1.1) provided a shell script
           that was used internally by pmlogconf(1), located in the
           PCP_BINADM_DIR directory, named pmlogconf-setup.  This script has
           been retired.  The equivalent functionality remains available in
           the unlikely event it should be needed via the -s or --setup
           option to pmlogconf(1).

           The version 1 pmlogconf-setup configuration file format (from
           IRIX) was also retired in this release, after more than 10 years
           of automatic transition to version 2 format by pmlogconf.

## [](#PMMGR)PMMGR

           The stand-alone PCP daemon manager pmmgr has been retired from PCP
           v5.2.0 onward.  It was phased out in favour of the simpler
           pmfind(1) service for setting up pmie(1) and pmlogger(1) ``farms''
           of discovered PCP collector systems with pmfind_check(1).  The new
           mechanisms, especially when integrated with systemd, require no
           additional daemons and are better integrated with the pmie and
           pmlogger service management used elsewhere in PCP.

## [](#PCP-COLLECTL)PCP-COLLECTL

           The pcp-collectl utility has been superseded by pmrep(1) from PCP
           v5 onward.

           The equivalent of pcp-collectl subsystem reporting is achieved as
           follows:

           pmrep :collectl-sc
                  Processor subsystem view.

           pmrep :collectl-sm
                  Memory subsystem view.

           pmrep :collectl-sd
                  Aggregate disks view.

           pmrep :collectl-sD
                  Per-disk-device view.

           pmrep :collectl-dm-sD
                  Device mapper view.

           pmrep :collectl-sn
                  Network subsystem view.

## [](#PCP-WEBAPPS)PCP-WEBAPPS

           The stand-alone web applications packaged with older PCP versions
           have been superseded by grafana-server(1) with the grafana-pcp
           plugin https://github.com/performancecopilot/grafana-pcp .

           This plugin provides an implementation of the Vector application,
           as well as data sources for pmdabpftrace(1) (bpftrace(8) scripts)
           and pmseries(1) (fast, scalable, distributed time series
           analysis).

## [](#PMWEBD)PMWEBD

           The pmwebd daemon has been superseded by pmproxy(1) from PCP v5
           onward.

           By default, pmproxy will now listen on both its original port
           (44322) and the PCP web API port (44323) when the time series
           support is built.

           pmproxy provides a compatible implementation of the live
           PMWEBAPI(3) interfaces used traditionally by the Vector web
           application (see the ``PCP-WEBAPPS'' section).  It also provides
           extensions to the original pmwebd REST APIs (such as derived
           metrics, namespace lookups and instance domain profiles), support
           for the HTTPS protocol, and fast, scalable time series querying
           using the pmseries(1) REST API with a distributed key-value server
           such as https://valkey.io/ .

           The partial Graphite API emulation provided by pmwebd has not been
           re-implemented - applications wishing to use similar services
           could use the scalable time series REST APIs described on
           PMWEBAPI(3).

## [](#SEE_ALSO)SEE ALSO

           pcp(1), pmcd(1), iostat2pcp(1), sar2pcp(1), pmrep(1), pmfind(1),
           pmfind_check(1), pmlogconf(1), pmproxy(1), pmseries(1),
           pmdabpftrace(1), python(1), grafana-server(1),
           mmv_stats_register(3), LOGIMPORT(3), PMAPI(3), PMDA(3) and
           PMWEBAPI(3).

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

    Performance Co-Pilot               PCP                       PCPCOMPAT(1)

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
