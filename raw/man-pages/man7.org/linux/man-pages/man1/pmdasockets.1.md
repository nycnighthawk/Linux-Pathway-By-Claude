---
{"title": "pmdasockets(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdasockets.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdasockets(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [INSTALLATION](#INSTALLATION) \| [FILTER CONFIGURATION](#FILTER_CONFIGURATION) \| [LOGGING CONFIGURATION](#LOGGING_CONFIGURATION) \| [METRICS](#METRICS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDASOCKETS(1)           General Commands Manual           PMDASOCKETS(1)

## [](#NAME)NAME

           pmdasockets - sockets statistics PMDA

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/sockets/pmdasockets [-D debug]

## [](#DESCRIPTION)DESCRIPTION

           pmdasockets is a Performance Metrics Domain Agent (PMDA) which
           exports metric values for current sockets on the local system.

           This PMDA currently collects its data through the ss(8) utility
           and requires that the program is installed in order to function.
           This dependency may change in the future.

## [](#INSTALLATION)INSTALLATION

           To install (enable) the sockets PMDA, do the following as root:

               # cd $PCP_PMDAS_DIR/sockets
               # ./Install

           To uninstall (disable), do the following as root:

               # cd $PCP_PMDAS_DIR/sockets
               # ./Remove

           pmdasockets is launched by pmcd(1) and should never be executed
           directly.  The Install and Remove scripts notify pmcd(1) when the
           agent is installed or removed.

## [](#FILTER_CONFIGURATION)FILTER CONFIGURATION

           The string valued metric network.persocket.filter specifies the
           ss(1) filter to be applied to optionally select socket states, IP
           addresses and other options that pmdasockets will collect (to
           populate it's instance domain).  This is loaded on PMDA startup
           from the file $(PCP_SYSCONF_DIR)/sockets/filter.conf (typically
           /etc/pcp/sockets/filter.conf) and defaults to state connected
           meaning only sockets in the connected state will be included.
           This can be changed persistently by editing filter.conf as the
           root user.  The filter can also be changed dynamically after the
           PMDA has started by using pmstore(1) to store a new filter string
           in the network.persocket.filter metric.  E.g.

               # pmstore network.persocket.filter "state all"

           will change the filter to include sockets in all states.  Note a
           dynamically stored filter is not persisted across PMDA restarts or
           reboots (edit the config file for a persistent change).  For
           further details of the filter syntax and options, consult ss(8).

## [](#LOGGING_CONFIGURATION)LOGGING CONFIGURATION

           The pmlogconf(1) configuration file for pmdasockets is
           $PCP_VAR_DIR/config/pmlogconf/networking/persocket-linux (where
           $PCP_VAR_DIR is typically /var/lib/pcp) which specifies to log all
           metrics below network.persocket in the PCP namespace with a
           default sampling interval of 60 seconds.  The logging interval and
           metrics to be logged can be changed by editing that file and then
           restarting the pmlogger service.  For details of the syntax, see
           pmlogconf(1).

## [](#METRICS)METRICS

           The metrics and metadata supported by pmdasockets correspond to
           fields reported by ss -noemitauOH and are also available as help
           text provided by the PMDA, e.g. to list all metrics, metadata
           descriptors and help text:

               # pminfo -fmdtT network.persocket

           Note that the PMDA must be installed (enabled) for this command to
           work correctly, see above.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP. On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

           Debugging options specific to pmdasockets are as follows:
           ┌────────┬───────────────────────────────────────────────────────┐
           │ Option │ Description                                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl0  │ loading socket state filter from                      │
           │        │ $PCP_SYSCONF_DIR/filter.conf and source of data       │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl1  │ parsing output from data source                       │
           └────────┴───────────────────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmcd(1), pmlogger(1) and ss(8).

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

    Performance Co-Pilot               PCP                     PMDASOCKETS(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcp-ss(1)](../man1/pcp-ss.1.html)

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
