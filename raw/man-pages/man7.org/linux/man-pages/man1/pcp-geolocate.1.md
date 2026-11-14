---
{"title": "pcp-geolocate(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-geolocate.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-geolocate(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [METRIC LABELS](#METRIC_LABELS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                   |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-GEOLOCATE(1)         General Commands Manual         PCP-GEOLOCATE(1)

## [](#NAME)NAME

           pcp-geolocate - discover collector system geographical labels

## [](#SYNOPSIS)SYNOPSIS

           pcp geolocate

## [](#DESCRIPTION)DESCRIPTION

           pcp-geolocate reports the latitude and longitude for the local
           Performance Co-Pilot collector host in JSON format.  This
           geolocation information is sourced from the cache file
           $PCP_SYSCONF_DIR/labels/optional/geolocate if it exists, else an
           attempt is made to perform geolocation based on the host IP
           address, via several online sources (REST APIs).

           The output from this command is suited for storing as metric
           labels by saving it to the cache file mentioned above.

           The opt-in systemd(1) service unit file for this command provides
           an automated location discovery for PCP metric labels.

## [](#METRIC_LABELS)METRIC LABELS

           The JSON output is the preferred format for storing geographical
           location as PCP metric labels.  Every PCP metric available from
           this host will be tagged with the labels for latitude and
           longitude, enabling tools that make use of this such as the
           Grafana geomap panel.

           For more information about metric labels refer to the pmcd(1),
           pminfo(1), pmlogger(1) and pmLookupLabels(3) manual entries.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pminfo(1), pmseries(1), pmlogger(1),
           systemd(1), pmLookupLabels(3), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                   PCP-GEOLOCATE(1)

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
